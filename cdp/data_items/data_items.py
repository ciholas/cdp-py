# pylint: disable=trailing-whitespace, too-few-public-methods, unused-wildcard-import

from cdp.cdp import *

class MPUAccelerometerV1(CDPDataItem):
    """CDP Data Item: Ciholas Data Protocol Accelerometer Data Item Definition"""

    type = 0x0001
    definition = [DIInt16Attr('x'),  # 2B - raw x accelerometer value
                  DIInt16Attr('y'),  # 2B - raw y accelerometer value
                  DIInt16Attr('z'),  # 2B - raw z accelerometer value
                  DIUInt32Attr('gnt')]  # 4B - global network time

    def get_xyz(self):
        return [self.x, self.y, self.z]


class MPUGyroscopeV1(CDPDataItem):
    """CDP Data Item: Ciholas Data Protocol Gyroscope Data Item Definition"""

    type = 0x0002
    definition = [DIInt16Attr('x'),  # 2B - raw x gyroscope value
                  DIInt16Attr('y'),  # 2B - raw y gyroscope value
                  DIInt16Attr('z'),  # 2B - raw z gyroscope value
                  DIUInt32Attr('gnt')]  # 4B - global network time

    def get_xyz(self):
        return [self.x, self.y, self.z]


class MPUMagnetometerV1(CDPDataItem):
    """CDP Data Item: Ciholas Data Protocol Magnetometer Data Item Definition"""

    type = 0x0003
    definition = [DIInt16Attr('x'),  # 2B - raw x magnetometer value
                  DIInt16Attr('y'),  # 2B - raw y magnetometer value
                  DIInt16Attr('z'),  # 2B - raw z magnetometer value
                  DIUInt32Attr('gnt')]  # 4B - global network time

    def get_xyz(self):
        return [self.x, self.y, self.z]


class LPSPressureV1(CDPDataItem):
    """CDP Data Item: Ciholas Data Protocol Pressure Data Item Definition"""

    type = 0x0005
    definition = [DIInt32Attr('pressure'),  # 4B - raw pressure value from LPS25H
                  DIUInt32Attr('gnt')]  # 4B - global network time


class LPSTemperatureV1(CDPDataItem):
    """CDP Data Item: Ciholas Data Protocol Temperature Data Item Definition"""

    type = 0x0006
    definition = [DIInt16Attr('temperature'),  # 2B - raw LPS25H temperature value
                  DIUInt32Attr('gnt')]  # 4B - global network time


class UserDefinedV1(CDPDataItem):
    """CDP Data Item: Ciholas Data Protocol User Defined Data Item Definition"""

    type = 0x0007
    definition = [DIVariableLengthBytesAttr('payload')]


class MPUAccelerometerV2(CDPDataItem):
    """CDP Data Item: Ciholas Data Protocol Accelerometer Data Item Definition"""

    type = 0x0008
    definition = [DIInt16Attr('x'),  # 2B - raw x accelerometer value
                  DIInt16Attr('y'),  # 2B - raw y accelerometer value
                  DIInt16Attr('z'),  # 2B - raw z accelerometer value
                  DIUInt32Attr('gnt'),  # 4B - global network time
                  DIUInt8Attr('scale'),  # 1B - value for accelerometer scale
                  DIUInt16Attr('dlpf')]  # 2B - value indicating Digital Low-Pass Filter setting

    def get_xyz(self):
        return [self.x, self.y, self.z]


class MPUGyroscopeV2(CDPDataItem):
    """CDP Data Item: Ciholas Data Protocol Gyroscope Data Item Definition"""

    type = 0x0009
    definition = [DIInt16Attr('x'),  # 2B - raw x gyroscope value
                  DIInt16Attr('y'),  # 2B - raw y gyroscope value
                  DIInt16Attr('z'),  # 2B - raw z gyroscope value
                  DIUInt32Attr('gnt'),  # 4B - global network time
                  DIUInt16Attr('scale'),  # 2B - full scale value in degrees/s
                  DIUInt8Attr('dlpf')]  # 1B - value indicating Digital Low-Pass Filter setting

    def get_xyz(self):
        return [self.x, self.y, self.z]


class MPUQuaternionV2(CDPDataItem):
    """CDP Data Item: Ciholas Data Protocol Quaternion Data Item Definition"""

    type = 0x000A
    definition = [DIInt32Attr('x'),  # 4B - raw x quaternion value
                  DIInt32Attr('y'),  # 4B - raw y quaternion value
                  DIInt32Attr('z'),  # 4B - raw z quaternion value
                  DIInt32Attr('w'),  # 4B - raw w quaternion value
                  DIUInt32Attr('gnt')]  # 4B - global network time

    def get_xyzw_floats(self):
        return [(self.x * 1.0) / (1<<30),
                (self.y * 1.0) / (1<<30),
                (self.z * 1.0) / (1<<30),
                (self.w * 1.0) / (1<<30)]


class LogMessageV1(CDPDataItem):
    """CDP Data Item: Ciholas Data Protocol Log Message Data Item Definition"""

    type = 0x00FD
    definition = [DIUInt16Attr('log_data'),  # 3b - log level/13b - message identifier
                  DIVariableLengthStrAttr('message')]  # ASCII string

    def get_log_level(self):
        """Returns the SysLog severity level"""
        return self.log_data >> 13

    def get_message_identifier(self):
        """Returns unique message identifier """
        return self.log_data & 0x1FFF


class PositionV1(CDPDataItem):
    """CDP Data Item: Ciholas Data Protocol Position Data Item Definition"""

    type = 0x0100
    definition = [DIInt32Attr('x'),  # 4B - x-coordinate in millimeters
                  DIInt32Attr('y'),  # 4B - y-coordinate in millimeters
                  DIInt32Attr('z'),  # 4B - z-coordinate in millimeters
                  DIUInt32Attr('quality'),  # 4B - quality indicator
                  DIUInt16Attr('smoothing'),  # 2B - effective smoothing factor
                  DIUInt16Attr('sequence'),  # 2B - sequence number sent from device
                  DIUInt32Attr('gnt')]  # 4B - global network time

    def get_xyz(self):
        return [self.x, self.y, self.z]


class DistanceV1(CDPDataItem):
    """CDP Data Item: Ciholas Data Protocol Distance Data Item Definition"""

    type = 0x0101
    definition = [DISerialNumberAttr('initiator_serial_number'),  # Initiator's serial number
                  DIInt32Attr('distance'),  # 4B - distance between the two devices in millimeters
                  DIInt16Attr('first_path'),  # 2B - first path signal quality in millibels
                  DIInt16Attr('total_path'),  # 2B - total path signal quality in millibels
                  DIUInt16Attr('sequence'),  # 2B - sequence of packet used to compute the distance
                  DIUInt32Attr('gnt')]  # 4B - global network time

    def get_first_path(self):
        """Returns the first path signal quality in decibels"""
        return self.first_path/100

    def get_total_path(self):
        """Returns the total path signal quality in decibels"""
        return self.total_path/100


class InfrastructureV1(CDPDataItem):
    """CDP Data Item: Ciholas Data Protocol Infrastructure Position Data Item Definition"""

    type = 0x0102
    definition = [DIUInt8Attr('node_type'),  # 1B - type of the infrastructure node
                  DISerialNumberAttr('serial_number'),  # Infrastructure node's serial number
                  DIInt32Attr('x'),  # 4B - x-coordinate from the origin
                  DIInt32Attr('y'),  # 4B - y-coordinate from the origin
                  DIInt32Attr('z')]  # 4B - z-coordinate from the origin


class AnchorStatusV1(CDPDataItem):
    """CDP Data Item: Ciholas Data Protocol Anchor Status Data Item Definition"""

    type = 0x0103
    definition = [DISerialNumberAttr('serial_number'),  # Anchor's serial number
                  DIUInt8Attr('status')]  # 1B - status of the anchor's data


class AnnouncementStatusV1(CDPDataItem):
    """CDP Data Item: Ciholas Data Protocol Announcement Status Data Item Definition"""

    type = 0x0104
    definition = [DISerialNumberAttr('serial_number'),
                  DIUInt8Attr('status')]


class AnchorPositionStatusV1(CDPDataItem):
    """CDP Data Item: Ciholas Data Protocol Anchor Position Status Data Item Definition"""

    type = 0x0105
    definition = [DISerialNumberAttr('serial_number'),  # Anchor's serial number
                  DIUInt8Attr('status'),  # 1B - status of the anchor's data
                  DIInt16Attr('first_path'),  # 2B - first path signal quality in millibels
                  DIInt16Attr('total_path'),  # 2B - total path signal quality in millibels
                  DIUInt16Attr('quality')]

    def get_first_path(self):
        """Returns the first path signal quality in decibels"""
        return self.first_path/100

    def get_total_path(self):
        """Returns the total path signal quality in decibels"""
        return self.total_path/100


class AnchorHealthV1(CDPDataItem):
    """CDP Data Item: Ciholas Data Protocol Anchor Health Data Item Definition"""

    type = 0x0106
    definition = [DISerialNumberAttr('serial_number'),  # Anchor's serial number
                  DIUInt32Attr('beacons_reported'),  # 4B - Reported beacons since last health pkt
                  DIUInt32Attr('beacons_discarded'),  # 4B - Discarded beacons since last health pkt
                  DIUInt16Attr('average_quality'),  # 2B - Average of the quality number
                  DIUInt8Attr('report_period')]  # 1B - period of the packet in seconds


class InfrastructureV2(CDPDataItem):
    """CDP Data Item: Ciholas Data Protocol Infrastructure Data Item Definition"""

    type = 0x0107
    definition = [DISerialNumberAttr('serial_number'),  # Infrastructure node's serial number
                  DIInt32Attr('x'),  # 4B - x-coordinate from the origin
                  DIInt32Attr('y'),  # 4B - y-coordinate from the origin
                  DIInt32Attr('z'),  # 4B - z-coordinate from the origin
                  DIUInt8Attr('node_type'),  # 1B - type of the infrastructure node
                  DIUInt8Attr('node_status')]  # 1B - status of the node


class NodeStatusChangeV1(CDPDataItem):
    """CDP Data Item: Ciholas Data Protocol Node Status Change Data Item Definition"""

    type = 0x0108
    definition = [DISerialNumberAttr('serial_number'),  # Node's serial number
                  DIUInt8Attr('node_status')]  # 1B - status of the node


class NodeStatusChangeV2(CDPDataItem):
    """CDP Data Item: Ciholas Data Protocol Node Status Change Data Item Definition"""

    type = 0x010D
    definition = [DISerialNumberAttr('serial_number'),  # Node's serial number
                  DIUInt8Attr('interface_id'),  # 1B - interface identifier of the node
                  DIUInt8Attr('node_status')]  # 1B - status of the node


class AnchorPositionStatusV2(CDPDataItem):
    """CDP Data Item: Ciholas Data Protocol Anchor Position Status Data Item Definition"""

    type = 0x010E
    definition = [DISerialNumberAttr('serial_number'),  # Anchor's serial number
                  DIUInt8Attr('interface_id'),  # 1B - interface identifier of the anchor
                  DIUInt8Attr('status'),  # 1B - status of the anchor's data
                  DIInt16Attr('first_path'),  # 2B - first path signal quality in millibels
                  DIInt16Attr('total_path'),  # 2B - total path signal quality in millibels
                  DIUInt16Attr('quality')]

    def get_first_path(self):
        """Returns the first path signal quality in decibels"""
        return self.first_path/100

    def get_total_path(self):
        """Returns the total path signal quality in decibels"""
        return self.total_path/100


class AnchorHealthV2(CDPDataItem):
    """CDP Data Item: Ciholas Data Protocol Anchor Health Data Item Definition"""

    type = 0x010F
    definition = [DISerialNumberAttr('serial_number'),  # Anchor's serial number
                  DIUInt8Attr('interface_id'),  # 1B - interface identifier of the anchor
                  DIUInt32Attr('beacons_reported'),  # 4B - reported beacons since last pkt
                  DIUInt32Attr('beacons_discarded'),  # 4B - discarded beacons since last health pkt
                  DIUInt16Attr('average_quality'),  # 2B - average of the quality number
                  DIUInt8Attr('report_period')]  # 1B - period of the packet in seconds


class InfrastructureV3(CDPDataItem):
    """CDP Data Item: Ciholas Data Protocol Infrastructure Position Data Item Definition"""

    type = 0x0110
    definition = [DISerialNumberAttr('serial_number'),  # Infrastructure node's serial number
                  DIUInt8Attr('interface_id'),  # 1B - Infrastructure node's interface identifier
                  DIInt32Attr('x'),  # 4B - x-coordinate from the origin
                  DIInt32Attr('y'),  # 4B - y-coordinate from the origin
                  DIInt32Attr('z'),  # 4B - z-coordinate from the origin
                  DIUInt8Attr('node_type'),  # 1B - type of the infrastructure node
                  DIUInt8Attr('node_status')]  # 1B - status of the node


class InfrastructureV4(CDPDataItem):
    """CDP Data Item: Ciholas Data Protocol Infrastructure Position Data Item Definition"""

    type = 0x0111
    definition = [DISerialNumberAttr('serial_number'),  # Infrastructure node's serial number
                  DIUInt8Attr('interface_id'),  # 1B - Infrastructure node's interface identifier
                  DIInt32Attr('x'),  # 4B - x-coordinate from the origin
                  DIInt32Attr('y'),  # 4B - y-coordinate from the origin
                  DIInt32Attr('z'),  # 4B - z-coordinate from the origin
                  DIUInt8Attr('node_type'),  # 1B - type of the infrastructure node
                  DIUInt8Attr('node_active_state'),  # 1B - inactive/active
                  DIUInt8Attr('node_lock_state')]  # 1B - unlocked/locked


class TWRV1(CDPDataItem):
    """CDP Data Item: Ciholas Data Protocol TWR Data Item Definition"""

    type = 0x0112
    definition = [DISerialNumberAttr('serial_number_1'),  # first device serial number
                  DISerialNumberAttr('serial_number_2'),  # second device serial number
                  DIUInt8Attr('interface_id_1'),  # 1B - first device interface identifier
                  DIUInt8Attr('interface_id_2'),  # 1B - second device interface identifier
                  DIUInt64Attr('rx_timestamp'),  # 8B  - timestamp of last received packet
                  DIUInt64Attr('distance')]  # 8B - distance between the two devices


class CDPStreamInformation(CDPDataItem):
    """CDP Data Item: Ciholas Data Protocol CDP Stream Information Data Item Definition"""

    type = 0x011A
    definition = [DIUInt32Attr('destination_ip'),  # 4B - IP address of this stream
                  DIUInt16Attr('destination_port'),  # 2B - port of this stream
                  DIUInt32Attr('interface_ip'),  # 4B - stream's interface IP
                  DIUInt32Attr('interface_netmask'),  # 4B - stream's interface netmask
                  DIUInt16Attr('interface_port'),  # 2B  - interface/listening port for this stream
                  DIUInt8Attr('ttl'),  # 1B - ttl of this stream
                  DIVariableLengthStrAttr('name')]  # name for this stream


class HostnameAnnounce(CDPDataItem):
    """CDP Data Item: Ciholas Data Protocol Hostname Announce Data Item Definition"""

    type = 0x011B
    definition = [DIVariableLengthStrAttr('hostname')]  # Hostname of the sending computer


class InstanceAnnounce(CDPDataItem):
    """CDP Data Item: Ciholas Data Protocol Instance Announce Data Item Definition"""

    type = 0x011C
    definition = [DIVariableLengthStrAttr('instance_name')]  # Database filename


class SetMagnetometerCalibration(CDPDataItem):
    """CDP Data Item: Ciholas Data Protocol Set Magnetometer Calibration Data Item Definition"""

    type = 0x0123
    definition = [DISerialNumberAttr('serial_number'),  # Recipient's serial number
                  DIInt16Attr('calibration_x'),  # 2B - calibration value for the x axis
                  DIInt16Attr('calibration_y'),  # 2B - calibration value for the y axis
                  DIInt16Attr('calibration_z')]  # 2B - calibration value for the z axis


class AnchorHealthV3(CDPDataItem):
    """CDP Data Item: Ciholas Data Protocol Anchor Health Data Item Definition"""

    type = 0x0124
    definition = [DISerialNumberAttr('serial_number'),  # Anchor's serial number
                  DIUInt8Attr('interface_id'),  # 1B - interface identifier of the anchor
                  DIUInt32Attr('ticks_reported'),  # 4B - reported ticks since last health pkt
                  DIUInt32Attr('timed_rxs_reported'),  #4B - reported timedrxs since last health pkt
                  DIUInt32Attr('beacons_reported'),  # 4B - reported beacons since last health pkt
                  DIUInt32Attr('beacons_discarded'),  # 4B - discarded beacons since last health pkt
                  DIUInt16Attr('average_quality'),  # 2B - average of the quality number
                  DIUInt8Attr('report_period')]  # 1B - period of the packet in seconds


class FullDeviceID:
    """Full Device ID Class Definition """

    definition = [DISerialNumberAttr('serial_number'), # device's serial number
                  DIUInt8Attr('interface_id')] # interface identifier of the device

    def __init__(self, serial_number=0, interface_id=0):
        self.serial_number = CiholasSerialNumber(serial_number)
        self.interface_id = interface_id

    def __str__(self):
        return "{}-{}".format(self.serial_number, self.interface_id)


class AnchorHealthV4(CDPDataItem):
    """CDP Data Item: Ciholas Data Protocol Anchor Health Data Item Definition"""

    type = 0x0125
    definition = [DISerialNumberAttr('serial_number'),  # Anchor's serial number
                  DIUInt8Attr('interface_id'),  # 1B - interface identifier of the anchor
                  DIUInt32Attr('ticks_reported'),  # 4B - reported ticks since last health pkt
                  DIUInt32Attr('timed_rxs_reported'),  #4B - reported timedrxs since last health pkt
                  DIUInt32Attr('beacons_reported'),  # 4B - reported beacons since last health pkt
                  DIUInt32Attr('beacons_discarded'),  # 4B - discarded beacons since last health pkt
                  DIUInt16Attr('average_quality'),  # 2B - average of the quality number
                  DIUInt8Attr('report_period'),  # 1B - period of the packet in seconds
                  DIUInt8Attr('interanchor_comms_error_code'),  # 1B - specifies type of comms errors between anchors
                  DIListAttr('bad_paired_anchors', FullDeviceID)]  # list of all partners with bad comms to this anchor

    def add_bad_paired_anchors(self, serial_number=0, interface_identifier=0):
        self.bad_paired_anchors.append(FullDeviceID(serial_number, interface_identifier))


class MagnetometerCalibrationResponse(CDPDataItem):
    """
    CDP Data Item: Ciholas Data Protocol
    Magnetometer Calibration Response Data Item Definition
    """

    type = 0x0126
    definition = [DIUInt16Attr('calibration_x'),
                  DIUInt16Attr('calibration_y'),
                  DIUInt16Attr('calibration_z')]

class DistanceV2(CDPDataItem):
    """
    CDP Data Item: Ciholas Data Protocol Distance V2 Data Item Definition
    """

    type = 0x0127
    definition = [DISerialNumberAttr('serial_number_1'),  # first device serial number
                  DISerialNumberAttr('serial_number_2'),  # second device serial number
                  DIUInt8Attr('interface_id_1'),  # 1B - first device interface identifier
                  DIUInt8Attr('interface_id_2'),  # 1B - second device interface identifier
                  DIUInt64Attr('rx_timestamp'),  # 8B  - timestamp of last received packet
                  DIUInt32Attr('distance'), # 4B - distance between the two devices in millimeters
                  DIUInt16Attr('quality')] # 2B - quality of the computed distance

class ErrorPattern:
    """Error Pattern Class Definition"""

    definition = [DIUInt8Attr('pattern')]
    colors = ['W','Y','B','G']

    def __init__(self, pattern=0):
        self.pattern = pattern

    def __str__(self):
        "{}{}{}".format(self.colors[(self.pattern >> 4) & 0x03],
                        self.colors[(self.pattern >> 2) & 0x03],
                        self.colors[(self.pattern >> 0) & 0x03])

class DeviceStatus(CDPDataItem):
    """
    CDP Data Item: Ciholas Data Protocol Device Status Definition
    """

    type = 0x0128
    definition = [DIUInt32Attr('memory'), # How much memory is free on the device
                  DIUInt32Attr('flags'), # Device Status Flags
                  DIUInt16Attr('minutes_remaining'), # number of minutes til charged or empty battery, 65535 for unknown
                  DIUInt8Attr('battery_percentage'), # batteries percentage, 255 for unknown
                  DIInt8Attr('temperature'), # temperature in degrees Celsius
                  DIUInt8Attr('processor_usage'), # percent of processor being used, 255 for unknown
                  DIListAttr('error_patterns', ErrorPattern)]

class AccelerometerV1(CDPDataItem):
    """
    CDP Data Item: Ciholas Data Protocol Accelerometer V1 Definition
    """

    type = 0x0129
    definition = [DIUInt64Attr('network_time'), # The timestamp when the sensor recorded the data. 
                  DIInt32Attr('x'), # 2s compliment X accelerometer value
                  DIInt32Attr('y'), # 2s compliment Y accelerometer value
                  DIInt32Attr('z'), # 2s compliment Z accelerometer value
                  DIUInt8Attr('scale')] # the full-scall representation in Gs

class GyroscopeV1(CDPDataItem):
    """
    CDP Data Item: Ciholas Data Protocol Gyroscope V1 Definition
    """

    type = 0x012A
    definition = [DIUInt64Attr('network_time'), # The timestamp when the sensor recorded the data. 
                  DIInt32Attr('x'), # 2s compliment X gyroscope value
                  DIInt32Attr('y'), # 2s compliment Y gyroscope value
                  DIInt32Attr('z'), # 2s compliment Z gyroscope value
                  DIUInt16Attr('scale')] # the full-scall representation in degrees per second

class MagnetometerV1(CDPDataItem):
    """
    CDP Data Item: Ciholas Data Protocol Magnetometer V1 Definition
    """

    type = 0x012B
    definition = [DIUInt64Attr('network_time'), # The timestamp when the sensor recorded the data. 
                  DIInt32Attr('x'), # 2s compliment X magnetometer value
                  DIInt32Attr('y'), # 2s compliment Y magnetometer value
                  DIInt32Attr('z'), # 2s compliment Z magnetometer value
                  DIUInt16Attr('scale')] # the full-scall representation in microtesla

class PressureV1(CDPDataItem):
    """
    CDP Data Item: Ciholas Data Protocol Pressure V1 Definition
    """

    type = 0x012C
    definition = [DIUInt64Attr('network_time'), # The timestamp when the sensor recorded the data. 
                  DIInt32Attr('z'), # 2s compliment pressure value
                  DIUInt32Attr('scale')] # the full-scall representation in millibar

class QuaternionV1(CDPDataItem):
    """
    CDP Data Item: Ciholas Data Protocol Quaternion V1 Definition
    """

    type = 0x012D
    definition = [DIUInt64Attr('network_time'), # The timestamp when the sensor recorded the data. 
                  DIInt32Attr('x'), # 2s compliment X quaternion value
                  DIInt32Attr('y'), # 2s compliment Y quaternion value
                  DIInt32Attr('z'), # 2s compliment Z quaternion value
                  DIInt32Attr('w'), # 2s compliment W quaternion value
                  DIBoolAttr('normalized')] # the full-scall representation in millibar

class TemperatureV1(CDPDataItem):
    """
    CDP Data Item: Ciholas Data Protocol Temperature V1 Definition
    """

    type = 0x012E
    definition = [DIUInt64Attr('network_time'), # The timestamp when the sensor recorded the data. 
                  DIInt16Attr('temperature'), # 2s compliment temperature value
                  DIUInt32Attr('scale')] # the full-scall representation in degrees Celsius 

class PositionV2(CDPDataItem):
    """CDP Data Item: Ciholas Data Protocol Position Data Item Definition"""

    type = 0x012F
    definition = [DIUInt64Attr('network_time'),  # 8B - global network time
                  DIInt32Attr('x'),  # 4B - x-coordinate in millimeters
                  DIInt32Attr('y'),  # 4B - y-coordinate in millimeters
                  DIInt32Attr('z'),  # 4B - z-coordinate in millimeters
                  DIUInt32Attr('quality'),  # 4B - quality indicator
                  DIUInt16Attr('smoothing')]  # 2B - effective smoothing factor

    def get_xyz(self):
        return [self.x, self.y, self.z]
