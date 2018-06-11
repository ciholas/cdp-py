# pylint: disable=trailing-whitespace, too-few-public-methods

from collections import defaultdict
import struct
from cdp.ciholas_serial_number import CiholasSerialNumber
from math import log10

class CDP():
    """CDP : Ciholas Data Protocol Python Class Definition"""

    data_item_classes = {}

    def __init__(self, data=None, serial_number=0):
        self.sequence = 0  # 4B - unsigned integer sequence number
        self.serial_number = CiholasSerialNumber(serial_number)
        self.data_items = []
        self.data_items_by_type = defaultdict(list)

        if data is not None:
            self.decode(data)

    def decode(self, data):
        cdp_header_size = 20

        # Check if the packet is at least large enough to hold a CDP header
        if len(data) < cdp_header_size:
            raise ValueError("Packet Size Error")

        # Get CDP header
        _mark, self.sequence, _string, serial = struct.unpack("<II8sI", data[:cdp_header_size])

        if _mark != 0x3230434c:
            raise ValueError("CDP Header - Unrecognized Mark: 0x{:04x}".format(_mark))

        _string = _string.decode()
        if _string != "CDP0002\0" and _string != "LCM_SELF":
            raise ValueError("CDP Header - Unrecognized String: {}".format(_string))

        self.serial_number = CiholasSerialNumber(serial)
        data = data[cdp_header_size:]

        di_header_size = 4
        while len(data) >= di_header_size:
            # Get data item header
            di_type, di_size = struct.unpack("<HH", data[:di_header_size])
            data = data[di_header_size:]

            # Check if size of the remaining data matches the size specified in the data item header
            if len(data) < di_size:
                print("Type: 0x{:04X}, Expected data size: {}, Actual data size: {}".format(di_type, di_size, len(data)))
                break

            try:
                di_class = CDP.data_item_classes[di_type]
            except KeyError:
                # Unregistered unrecognized type
                class_name = 'Unknown0x{:04X}'.format(di_type)

                # Dynamically create a CDP data item class for this unknown type
                di_class = type(class_name, (CDPDataItem,), dict(type=di_type))

                # Register new CDP data item class
                CDP.data_item_classes[di_type] = di_class

            data_item = di_class(data[:di_size])
            self.add_data_item(data_item)
            data = data[di_size:]

        # Check if there is no more data available to read
        if data:
            raise ValueError("Incomplete CDP Packet")

    def encode(self):
        data = struct.pack("<II8sI", 0x3230434C, self.sequence,
                           b'CDP0002', self.serial_number.as_int)
        for item in self.data_items:
            data += item._encode()
        return data

    def add_data_item(self, data_item):
        data_item.cdp_header_sequence = self.sequence
        data_item.cdp_header_serial = self.serial_number
        self.data_items.append(data_item)
        self.data_items_by_type[data_item.type].append(data_item)

    def add_data_items(self, data_items):
        for item in data_items:
            self.add_data_item(item)

    @classmethod
    def register_data_item(cls, di_class):
        cls.data_item_classes[di_class.type] = di_class


class DataItemAttribute():
    """Data Item Attribute: CDP Data Item Attribute Class Definition"""

    def __init__(self, name, format, size, default):
        self.name = name  # String corresponding to the data attribute name
        self.format = format  # Format char used for packing/unpacking the data attribute
        self.size = size  # Size in bytes of the data attribute
        self.default = default
        self.is_list = False

    def _decode(self, data):
        value, = struct.unpack("<" + self.format, data[:self.size])
        return (value, self.size)

    def _encode(self, value):
        return struct.pack("<" + self.format, value)


class DIUInt8Attr(DataItemAttribute):
    """Data Item Attribute: CDP Data Item Unsigned 8-bit Integer Attribute Class Definition"""

    def __init__(self, name):
        super().__init__(name, 'B', 1, 0)


class DIInt8Attr(DataItemAttribute):
    """Data Item Attribute: CDP Data Item 8-bit Integer Attribute Class Definition"""

    def __init__(self, name):
        super().__init__(name, 'b', 1, 0)


class DIUInt16Attr(DataItemAttribute):
    """Data Item Attribute: CDP Data Item Unsigned 16-bit Integer Attribute Class Definition"""
    def __init__(self, name):
        super().__init__(name, 'H', 2, 0)


class DIInt16Attr(DataItemAttribute):
    """Data Item Attribute: CDP Data Item 16-bit Integer Attribute Class Definition"""
    def __init__(self, name):
        super().__init__(name, 'h', 2, 0)


class DIUInt32Attr(DataItemAttribute):
    """Data Item Attribute: CDP Data Item Unsigned 32-bit Integer Attribute Class Definition"""

    def __init__(self, name):
        super().__init__(name, 'I', 4, 0)


class DIInt32Attr(DataItemAttribute):
    """Data Item Attribute: CDP Data Item 32-bit Integer Attribute Class Definition"""

    def __init__(self, name):
        super().__init__(name, 'i', 4, 0)


class DIFloatAttr(DataItemAttribute):
    """Data Item Attribute: CDP Data Item Float Attribute Class Definition"""

    def __init__(self, name):
        super().__init__(name, 'f', 4, 0.0)


class DIUInt64Attr(DataItemAttribute):
    """Data Item Attribute: CDP Data Item Unsigned 32-bit Integer Attribute Class Definition"""

    def __init__(self, name):
        super().__init__(name, 'Q', 8, 0)


class DIInt64Attr(DataItemAttribute):
    """Data Item Attribute: CDP Data Item 32-bit Integer Attribute Class Definition"""

    def __init__(self, name):
        super().__init__(name, 'q', 8, 0)


class DIDoubleAttr(DataItemAttribute):
    """Data Item Attribute: CDP Data Item Double Attribute Class Definition"""

    def __init__(self, name):
        super().__init__(name, 'd', 8, 0.0)


class DIBoolAttr(DataItemAttribute):
    """Data Item Attribute: CDP Data Item Boolean Attribute Class Definition"""

    def __init__(self, name):
        super().__init__(name, '?', 1, False)
        
def nullstrip(s):
    """Return a string truncated at the first null character"""
    try:
        # Remove any junk data and before decoding
        # to avoid Unicode Decode errors
        s = s[:s.index(b'\x00')]
    except ValueError:
        pass
    
    try:
        # Decode bytes object using UTF-8 encoding scheme
        s = s.decode()
    except UnicodeDecodeError:
        # String has byte(s) the cannot be decoded. Set to hex string representation. 
        s = s.hex()
    return s


class DIFixedLengthStrAttr(DataItemAttribute):
    """Data Item Attribute: CDP Data Item Fixed Length String Attribute Class Definition"""

    def __init__(self, name, size):
        super().__init__(name, 's', size, '')

    def _decode(self, data):
        fmt = str(self.size) + self.format  # Prepend count to 's'
        value, = struct.unpack("<" + fmt, data[:self.size])
        value = nullstrip(value)  # Convert bytes object to str
        return (value, self.size)

    def _encode(self, value):
        value = value.encode()  # Convert str to bytes object
        fmt = str(self.size) + self.format  # Prepend count to 's'
        return struct.pack("<" + fmt, value)


class DIVariableLengthStrAttr(DataItemAttribute):
    """Data Item Attribute: CDP Data Item Variable Length String Attribute Class Definition"""

    def __init__(self, name):
        super().__init__(name, 's', -1, '')

    def _decode(self, data):
        size = len(data)
        fmt = str(size) + self.format  # Prepend count to 's'
        value, = struct.unpack("<" + fmt, data[:size])
        value = nullstrip(value)  # Convert bytes object to str
        return (value, size)

    def _encode(self, value):
        value = value.encode()  # Convert str to bytes object
        fmt = str(len(value)) + self.format  # Prepend count to 's'
        return struct.pack("<" + fmt, value)


class DIFixedLengthBytesAttr(DataItemAttribute):
    """Data Item Attribute: CDP Data Item Fixed Length Bytes Attribute Class Definition"""

    def __init__(self, name, size):
        super().__init__(name, 's', size, b'')

    def _decode(self, data):
        fmt = str(self.size) + self.format  # Prepend count to 's'
        value, = struct.unpack("<" + fmt, data[:self.size])
        return (value, self.size)

    def _encode(self, value):
        fmt = str(self.size) + self.format  # Prepend count to 's'
        return struct.pack("<" + fmt, value)


class DIVariableLengthBytesAttr(DataItemAttribute):
    """Data Item Attribute: CDP Data Item Variable Length Bytes Attribute Class Definition"""

    def __init__(self, name):
        super().__init__(name, 's', -1, b'')

    def _decode(self, data):
        size = len(data)
        fmt = str(size) + self.format  # Prepend count to 's'
        value, = struct.unpack("<" + fmt, data[:size])
        return (value, size)

    def _encode(self, value):
        fmt = str(len(value)) + self.format  # Prepend count to 's'
        return struct.pack("<" + fmt, value)


class DISerialNumberAttr(DataItemAttribute):
    """Data Item Attribute: CDP Data Item Serial Number Attribute Class Definition"""

    def __init__(self, name):
        super().__init__(name, 'I', 4, CiholasSerialNumber())

    def _decode(self, data):
        serial_number, = struct.unpack("<" + self.format, data[:self.size])
        return (CiholasSerialNumber(serial_number), self.size)

    def _encode(self, serial_number):
        return struct.pack("<" + self.format, serial_number.as_int)


class UWBSignalStrength():
    """UWB Signal Strength: UWB Signal Strength Class Definition"""

    def __init__(self):
        self.fp_ampl1 = 0  # FP amplitude 1 of the reception
        self.fp_ampl2 = 0  # FP amplitude 2 of the reception
        self.fp_ampl3 = 0  # FP amplitude 3 of the reception
        self.rx_preamble_acc = 0  # Received preamble accumulation of the reception
        self.cir_power = 0  # Channel impulse response power of the reception
        self.std_noise = 0  # Standard noise of the reception

    def get_first_path(self, prf=64):
        """Provide First Path amplitude in dB given DW1000 RF state information"""
        if prf == 16:
            prf_value = 115.72
        else:
            prf_value = 121.74

        _preamble_count = self.rx_preamble_acc

        # Sanity check to prevent division by zero
        if _preamble_count == 0:
            _preamble_count = 0.1
        if self.fp_ampl1 == 0 or self.fp_ampl2 == 0 or self.fp_ampl3 == 0:
            return 200.0
        return 10.0 * log10( (self.fp_ampl1**2.0 + self.fp_ampl2**2.0 + self.fp_ampl3**2.0)/_preamble_count**2.0) - prf_value

    def get_total_path(self, prf=64):
        """Provide Total Path amplitude in dB given DW1000 RF state information"""
        if prf == 16:
            prf_value = 115.72
        else:
            prf_value = 121.74

        _preamble_count = self.rx_preamble_acc
        _cir_power = self.cir_power

        # Sanity check to prevent taking log of zero
        if _cir_power == 0:
            _cir_power = 0.1
        # Sanity check to prevent division by zero
        if _preamble_count == 0:
            _preamble_count = 0.1

        return 10.0 * log10( (_cir_power * 2.0**17.0) /_preamble_count**2.0) - prf_value


    def __str__(self):
        return "{}, {}, {}, {}, {}, {}".format(self.fp_ampl1,
                                               self.fp_ampl2,
                                               self.fp_ampl3,
                                               self.rx_preamble_acc,
                                               self.cir_power,
                                               self.std_noise)


class DISignalStrengthAttr(DataItemAttribute):
    """Data Item Attribute: CDP Data Item Signal Strength Attribute Class Definition"""

    def __init__(self, name):
        super().__init__(name, 'HHHHHH', 12, UWBSignalStrength())

    def _decode(self, data):
        uwb_ss = UWBSignalStrength()
        uwb_ss.fp_ampl1, \
            uwb_ss.fp_ampl2, \
            uwb_ss.fp_ampl3, \
            uwb_ss.rx_preamble_acc, \
            uwb_ss.cir_power, \
            uwb_ss.std_noise = struct.unpack("<" + self.format, data[:self.size])
        return (uwb_ss, self.size)

    def _encode(self, uwb_ss):
        return struct.pack("<" + self.format,
                           uwb_ss.fp_ampl1,
                           uwb_ss.fp_ampl2,
                           uwb_ss.fp_ampl3,
                           uwb_ss.rx_preamble_acc,
                           uwb_ss.cir_power,
                           uwb_ss.std_noise)


class UWBCondensedSignalStrength():
    """UWB Condensed Signal Strength: UWB Condensed Signal Strength Class Definition"""

    def __init__(self):
        self.fp_rssi = 0  # First path RSSI
        self.tp_rssi = 0  # Total path RSSI

    def __str__(self):
        return "{}, {}".format(self.fp_rssi,
                               self.tp_rssi)


class DICondensedSignalStrengthAttr(DataItemAttribute):
    """Data Item Attribute: CDP Data Item Condensed Signal Strength Attribute Class Definition"""

    def __init__(self, name):
        super().__init__(name, "bb", 2, UWBCondensedSignalStrength())

    def _decode(self, data):
        uwb_css = UWBCondensedSignalStrength()
        uwb_css.fp_rssi, \
            uwb_css.tp_rssi = struct.unpack("<" + self.format, data[:self.size])
        return (uwb_css, self.size)

    def _encode(self, uwb_css):
        return struct.pack("<" + self.format, uwb_css.fp_rssi, uwb_css.tp_rssi)


class DIListAttr():
    """Data Item Attribute: CDP Data Item List Attribute Class Definition"""

    def __init__(self, name, class_name):
        self.name = name  # String corresponding to the data attibute name
        self.class_name = class_name  # Name of the helper structure
        self.default = []
        self.is_list = True

    def _decode(self, data):
        lst = []
        data_size = len(data)
        while data:
            di_subdata = self.class_name()
            for attr in self.class_name.definition:
                value, size = attr._decode(data)
                data = data[size:]
                setattr(di_subdata, attr.name, value)
            lst.append(di_subdata)
        return lst, data_size

    def _encode(self, lst):
        data = b''
        for di_subdata in lst:
            for attr in self.class_name.definition:
                value = getattr(di_subdata, attr.name)
                data += attr._encode(value)
        return data

class DISerialNumberListAttr(DIListAttr):

    def __init__(self, name):
        super().__init__(name, CiholasSerialNumber)

    def _decode(self, data):
        lst = []
        data_size = len(data)
        while data:
            serial_number, = struct.unpack("<I", data[:4])
            data = data[4:]
            lst.append(CiholasSerialNumber(serial_number))
        return lst, data_size

    def _encode(self, lst):
        data = b''
        for serial_number in lst:
            data += struct.pack("<I", serial_number.as_int)
        return data


class CDPDataItem():
    """CDP Data Item: Ciholas Data Protocol Data Item Class Definition"""

    type = 0xFFFF
    definition = [DIVariableLengthBytesAttr('data')]

    def __init__(self, di_data=None, **kwargs):
        self.cdp_header_sequence = 0
        self.cdp_header_serial = CiholasSerialNumber()
        self.di_size = 0 if di_data is None else len(di_data)  # Size of the data in the CDP Data Item
        self.di_data = di_data
        self.di_name = self.__class__.__name__  # String version of the data item name

        # If present, set Data Item attributes from keyword arguments
        self.__dict__.update(kwargs)

    def __getattr__(self, key):
        if self.di_data is not None:
            self._decode()
        else:
            for attr in self.definition:
                # Check if data attribute has not been defined yet before initializing
                # it to its default value
                if not attr.name in dir(self):
                    setattr(self, attr.name, attr.default)

        if key in dir(self):
            return getattr(self, key)

        # Raise appropriately formatted attribute error
        return object.__getattribute__(self, key)

    def _decode(self):
        for attr in self.definition:
            value, size = attr._decode(self.di_data)
            self.di_data = self.di_data[size:]
            setattr(self, attr.name, value)
        self.di_data = None

    def _encode(self):
        data = b''
        for attr in self.definition:
            value = getattr(self, attr.name)
            data += attr._encode(value)
        self.di_size = len(data)
        return struct.pack("<HH", self.type, self.di_size) + data

    def __str__(self):
        # Generic printable representation of a CDP data item.
        # If a specific format is needed, override this method in the child class
        string = "{}, 0x{:04X}".format(self.cdp_header_serial, self.type)
        for attr in self.definition:
            value = getattr(self, attr.name)

            if attr.is_list:
                value = ", ".join(str(di_subdata) for di_subdata in value)
            elif attr.format == 's' and isinstance(value, bytes):
                value = value.hex()

            string += ", {}".format(value)
        return string
