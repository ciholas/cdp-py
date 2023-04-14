# Ciholas, Inc. - www.ciholas.com
# Licensed under: creativecommons.org/licenses/by/4.0
# pylint: disable=trailing-whitespace, too-few-public-methods, unused-wildcard-import

from cdp.cdp import *

class MPUAccelerometerV1(CDPDataItem):
    """CDP Data Item: Ciholas Data Protocol MPU Accelerometer V1 Data Item Definition. Replaced by 0x0008 in v2.0.
       This data type is used to report the accelerometer data from an onboard MPU-9250."""

    type = 0x0001
    definition = [DIInt16Attr('x'),  # The signed raw x accelerometer value.
                  DIInt16Attr('y'),  # The signed raw y accelerometer value.
                  DIInt16Attr('z'),  # The signed raw z accelerometer value.
                  DIUInt32Attr('gnt')]  # The timestamp when the MPU-9250 recorded the data. This value is represented in Global Network Time, which is roughly 1.026 microseconds per tick.

    def get_xyz(self):
        """Returns x, y, and z accelerometer values in the form of a list."""
        return [self.x, self.y, self.z]


class MPUGyroscopeV1(CDPDataItem):
    """CDP Data Item: Ciholas Data Protocol MPU Gyroscope V1 Data Item Definition. Replaced by 0x0009 in v2.0.
       This data type is used to report the gyroscope data from an onboard MPU-9250."""

    type = 0x0002
    definition = [DIInt16Attr('x'),  # The signed raw x gyroscope value.
                  DIInt16Attr('y'),  # The signed raw y gyroscope value.
                  DIInt16Attr('z'),  # The signed raw z gyroscope value.
                  DIUInt32Attr('gnt')]  # The timestamp when the MPU-9250 recorded the data. This value is represented in Global Network Time, which is roughly 1.026 microseconds per tick.

    def get_xyz(self):
        """Returns x, y, and z gyroscope values in the form of a list."""
        return [self.x, self.y, self.z]


class MPUMagnetometerV1(CDPDataItem):
    """CDP Data Item: Ciholas Data Protocol MPU Magnetometer V1 Data Item Definition. Replaced by 0x012B in v3.0.
       This data type is used to report the magnetometer data from an onboard MPU-9250."""

    type = 0x0003
    definition = [DIInt16Attr('x'),  # The signed raw x magnetometer value.
                  DIInt16Attr('y'),  # The signed raw y magnetometer value.
                  DIInt16Attr('z'),  # The signed raw z magnetometer value.
                  DIUInt32Attr('gnt')]  # The timestamp when the MPU-9250 recorded the data. This value is represented in Global Network Time, which is roughly 1.026 microseconds per tick.

    def get_xyz(self):
        """Returns x, y, and z magnetometer values in the form of a list."""
        return [self.x, self.y, self.z]


class LPSPressureV1(CDPDataItem):
    """CDP Data Item: Ciholas Data Protocol LPS Pressure V1 Data Item Definition. Replaced by 0x012C in v3.0.
       This data type is used to report the pressure measured by an onboard LPS25H."""

    type = 0x0005
    definition = [DIInt32Attr('pressure'),  # Signed raw pressure value from LPS25H.
                  DIUInt32Attr('gnt')]  # The timestamp when the LPS25H recorded the data. This value is represented in Global Network Time, which is roughly 1.026 microseconds per tick.


class LPSTemperatureV1(CDPDataItem):
    """CDP Data Item: Ciholas Data Protocol LPS Temperature V1 Data Item Definition. Replaced by 0x012E in v3.0.
       This data type is used to report the temperature measured by an onboard LPS25H."""

    type = 0x0006
    definition = [DIInt16Attr('temperature'),  # Signed raw LPS25H temperature value.
                  DIUInt32Attr('gnt')]  # The timestamp when the LPS25H recorded the data. This value is represented in Global Network Time, which is roughly 1.026 microseconds per tick.


class UserDefinedV1(CDPDataItem):
    """CDP Data Item: Ciholas Data Protocol User Defined V1 Data Item Definition. Removed in v3.2.
       This data type is used to report any user defined data bytes."""

    type = 0x0007
    definition = [DIVariableLengthBytesAttr('payload')]  # The format of the contents are defined by the user.


class MPUAccelerometerV2(CDPDataItem):
    """CDP Data Item: Ciholas Data Protocol MPU Accelerometer V2 Data Item Definition. Replaced by 0x0129 in v3.0.
       This data type is used to report the accelerometer data from an onboard MPU-9250."""

    type = 0x0008
    definition = [DIInt16Attr('x'),  # The signed raw x accelerometer value.
                  DIInt16Attr('y'),  # The signed raw y accelerometer value.
                  DIInt16Attr('z'),  # The signed raw z accelerometer value.
                  DIUInt32Attr('gnt'),  # The timestamp when the MPU-9250 recorded the data. This value is represented in Global Network Time, which is roughly 1.026 microseconds per tick.
                  DIUInt8Attr('scale'),  # The full-scale representation in Gs.
                  DIUInt16Attr('dlpf')]  # The MPU-9250 DLPF rate in Hz.

    def get_xyz(self):
        """Returns x, y, and z accelerometer values in the form of a list."""
        return [self.x, self.y, self.z]


class MPUGyroscopeV2(CDPDataItem):
    """CDP Data Item: Ciholas Data Protocol MPU Gyroscope V2 Data Item Definition. Replaced by 0x012A in v3.0.
       This data type is used to report the gyroscope data from an onboard MPU-9250."""

    type = 0x0009
    definition = [DIInt16Attr('x'),  # The signed raw x gyroscope value.
                  DIInt16Attr('y'),  # The signed raw y gyroscope value.
                  DIInt16Attr('z'),  # The signed raw z gyroscope value.
                  DIUInt32Attr('gnt'),  # The timestamp when the MPU-9250 recorded the data. This value is represented in Global Network Time, which is roughly 1.026 microseconds per tick.
                  DIUInt16Attr('scale'),  # The full-scale value in degrees/s.
                  DIUInt8Attr('dlpf')]  # The MPU-9250 DLPF rate in Hz.

    def get_xyz(self):
        """Returns x, y, and z gyroscope values in the form of a list."""
        return [self.x, self.y, self.z]


class MPUQuaternionV2(CDPDataItem):
    """CDP Data Item: Ciholas Data Protocol MPU Quaternion V2 Data Item Definition. Replaced by 0x012D in v3.0.
       This data type is used to report quaternion data from an onboard MPU-9250."""

    type = 0x000A
    definition = [DIInt32Attr('x'),  # The signed raw x quaternion value.
                  DIInt32Attr('y'),  # The signed raw y quaternion value.
                  DIInt32Attr('z'),  # The signed raw z quaternion value.
                  DIInt32Attr('w'),  # The signed raw w quaternion value.
                  DIUInt32Attr('gnt')]  # The timestamp when the MPU-9250 recorded the data. This value is represented in Global Network Time, which is roughly 1.026 microseconds per tick.

    def get_xyzw_floats(self):
        """Returns x, y, z, and w quaternion values as floats in the form of a list."""
        return [(self.x * 1.0) / (1<<30),
                (self.y * 1.0) / (1<<30),
                (self.z * 1.0) / (1<<30),
                (self.w * 1.0) / (1<<30)]


class LogMessageV1(CDPDataItem):
    """CDP Data Item: Ciholas Data Protocol Log Message V1 Data Item Definition. Removed in v3.2.
       This data type is used to transmit debug information. The messages can originate from the firmware, cuwb_server, or some other application."""

    type = 0x00FD
    definition = [DIUInt16Attr('log_data'),  # 3 bits = Log level. 13 bits = Message identifier.
                  DIVariableLengthStrAttr('message')]  # An ASCII string. The string may or may not be NULL terminated at the discretion of the sender.

    def get_log_level(self):
        """Returns the SysLog severity level."""
        return self.log_data >> 13

    def get_message_identifier(self):
        """Returns unique message identifier."""
        return self.log_data & 0x1FFF


class PositionV1(CDPDataItem):
    """CDP Data Item: Ciholas Data Protocol Position V1 Data Item Definition. Replaced by 0x012F in v3.0.
       This data type is used to report the 3 dimensional position of the reporting device."""

    type = 0x0100
    definition = [DIInt32Attr('x'),  # The signed x-coordinate in millimeters.
                  DIInt32Attr('y'),  # The signed y-coordinate in millimeters.
                  DIInt32Attr('z'),  # The signed z-coordinate in millimeters.
                  DIUInt32Attr('quality'),  # Quality indicator.
                  DIUInt16Attr('smoothing'),  # The effective smoothing factor (the number of positions averaged minus 1).
                  DIUInt16Attr('sequence'),  # The sequence number of the packet from the reporting device that was used to calculate the position.
                  DIUInt32Attr('gnt')]  # The calculated timestamp of the transmission of the packet from the reporting device used to calculate the position. This value is represented in Global Network Time, which is roughly 1.026 microseconds per tick.

    def get_xyz(self):
        """Returns x, y, and z coordinates values in mm in the form of a list."""
        return [self.x, self.y, self.z]


class DistanceV1(CDPDataItem):
    """CDP Data Item: Ciholas Data Protocol Distance V1 Data Item Definition. Replaced by 0x012F in v3.0.
       This data type is used to report the distance between 2 devices, an initiator and a responder. The CDP packet is sent from the responder."""

    type = 0x0101
    definition = [DISerialNumberAttr('initiator_serial_number'),  # The serial number of initiator.
                  DIInt32Attr('distance'),  # The signed two's complement integer distance between the two devices in millimeters.
                  DIInt16Attr('first_path'),  # The signed two's complement integer first path signal quality in millibels.
                  DIInt16Attr('total_path'),  # The signed two's complement integer total path signal quality in millibels.
                  DIUInt16Attr('sequence'),  # The sequence number of the packet from the CUWB Server that was used to calculate the distance.
                  DIUInt32Attr('gnt')]  # The timestamp when the reflector device received the final packet of the TWR process. This value is represented in Global Network Time, which is roughly 1.026 microseconds per tick.

    def get_first_path(self):
        """Returns the first path signal quality in decibels."""
        return self.first_path/100

    def get_total_path(self):
        """Returns the total path signal quality in decibels."""
        return self.total_path/100


class InfrastructureV1(CDPDataItem):
    """CDP Data Item: Ciholas Data Protocol Infrastructure Position V1 Data Item Definition. Replaced by 0x0102 in v3.2.
       This data type is used to report the 3 dimensional position of a stationary device."""

    type = 0x0102
    definition = [DIUInt8Attr('node_type'),  # Type of the infrastructure node. Seeder = 0x01. Anchor = 0x02.
                  DISerialNumberAttr('serial_number'),  # Serial number of infrastructure node.
                  DIInt32Attr('x'),  # The signed x-coordinate from the origin.
                  DIInt32Attr('y'),  # The signed y-coordinate from the origin.
                  DIInt32Attr('z')]  # The signed z-coordinate from the origin.


class AnchorStatusV1(CDPDataItem):
    """CDP Data Item: Ciholas Data Protocol Anchor Status V1 Data Item Definition. Replaced by 0x010E in v3.0.
       This data type is used to report the status of an anchor that provided location data about the reporting device."""

    type = 0x0103
    definition = [DISerialNumberAttr('serial_number'),  # The serial number of the anchor.
                  DIUInt8Attr('status')]  # Status of the anchor's data. 0 = Data is good. 1 = Unknown. 2 = Data does not match other anchors. 3 = Anchor data is inconsitent with previous data.


class AnnouncementStatusV1(CDPDataItem):
    """CDP Data Item: Ciholas Data Protocol Announcement Status V1 Data Item Definition. Removed in v3.2.
       This data type is used to report how a device configuration request was handled."""

    type = 0x0104
    definition = [DISerialNumberAttr('serial_number'),  # Serial number of the device.
                  DIUInt8Attr('status')]  # Status of the device.


class AnchorPositionStatusV1(CDPDataItem):
    """CDP Data Item: Ciholas Data Protocol Anchor Position Status V1 Data Item Definition. Deprecated.
       This data type is used to report the status of an anchor that provided location data about the reporting device."""

    type = 0x0105
    definition = [DISerialNumberAttr('serial_number'),  # The serial number of the anchor.
                  DIUInt8Attr('status'),  # Status of the anchor's data. 0 = Data is good. 1 = Unknown. 2 = Data does not match other anchors. 3 = Data is inconsistent with previous data. 4 = Network Time not locked.
                  DIInt16Attr('first_path'),  # The signed two's complement integer first path signal quality in millibels.
                  DIInt16Attr('total_path'),  # The signed two's complement integer total path signal quality in millibels.
                  DIUInt16Attr('quality')]  # A number between 0 and 10,000 representing quality, with 0 being poor quality and 10,000 being high quality.

    def get_first_path(self):
        """Returns the first path signal quality in decibels."""
        return self.first_path/100

    def get_total_path(self):
        """Returns the total path signal quality in decibels."""
        return self.total_path/100


class AnchorHealthV1(CDPDataItem):
    """CDP Data Item: Ciholas Data Protocol Anchor Health V1 Data Item Definition. Deprecated.
       This data type is used to report the health of anchors in the network."""

    type = 0x0106
    definition = [DISerialNumberAttr('serial_number'),  # Serial number of the anchor.
                  DIUInt32Attr('beacons_reported'),  # Reported beacons since last health packet.
                  DIUInt32Attr('beacons_discarded'),  # Discarded beacons since last health packet.
                  DIUInt16Attr('average_quality'),  # Average of the quality number between 0 and 10,000, with 0 being poor quality and 10,000 being high quality for the anchor since the last Anchor Health Information.
                  DIUInt8Attr('report_period')]  # Period of the packet in seconds.


class InfrastructureV2(CDPDataItem):
    """CDP Data Item: Ciholas Data Protocol Infrastructure Position V2 Data Item Definition. Replaced by 0x0111 in v3.2.
       This data type is used to report the 3 dimensional position of a stationary device."""

    type = 0x0107
    definition = [DISerialNumberAttr('serial_number'),  # Serial number of the infrastructure node.
                  DIInt32Attr('x'),  # The signed x-coordinate from the origin.
                  DIInt32Attr('y'),  # The signed y-coordinate from the origin.
                  DIInt32Attr('z'),  # The signed z-coordinate from the origin.
                  DIUInt8Attr('node_type'),  # Type of the infrastructure node. Seeder = 0x01. Anchor = 0x02.
                  DIUInt8Attr('node_status')]  # Status of the node. Inactive = 0x01. Active = 0x02.


class NodeStatusChangeV1(CDPDataItem):
    """CDP Data Item: Ciholas Data Protocol Node Status Change V1 Data Item Definition. Deprecated.
       This data type is used to report when the status for a node has changed."""

    type = 0x0108
    definition = [DISerialNumberAttr('serial_number'),  # Serial number of the node.
                  DIUInt8Attr('node_status')]  # Status of the node. Inactive = 0x01.


class DeliverUserDataV1(CDPDataItem):
    """CDP Data Item: Ciholas Data Protocol Deliver User Data V1 Data Item Definition. Protected.
       This data type is used to forward any user data that is sent to the server to the DW devices that are on the network."""

    type = 0x010C
    definition = [DISerialNumberAttr('serial_number'),  # Serial number of the recipient.
                  DIVariableLengthBytesAttr('payload')]  # The format of the contents are defined by the user.


class NodeStatusChangeV2(CDPDataItem):
    """CDP Data Item: Ciholas Data Protocol Node Status Change V2 Data Item Definition. Current in v3.3.
       This data type is used to report when the status for a node has changed."""

    type = 0x010D
    definition = [DISerialNumberAttr('serial_number'),  # The serial number of the node.
                  DIUInt8Attr('interface_id'),  # The interface identifier of the node.
                  DIUInt8Attr('node_status')]  # The status of the node. Inactive = 0x01.


class AnchorPositionStatusV2(CDPDataItem):
    """CDP Data Item: Ciholas Data Protocol Anchor Position Status V2 Data Item Definition. Replaced by 0x0136 in v3.2.
       This data type is used to report the status of an anchor that provided location data about the reporting device."""

    type = 0x010E
    definition = [DISerialNumberAttr('serial_number'),  # The serial number of the anchor.
                  DIUInt8Attr('interface_id'),  # The interface identifier of the anchor.
                  DIUInt8Attr('status'),  # Status of the anchor's data. 0 = Data is good. 1 = Unknown. 2 = Data does not match other anchors. 3 = Data is inconsistent with previous data. 4 = Network Time is not locked.
                  DIInt16Attr('first_path'),  # The signed two's complement integer first path signal quality in millibels.
                  DIInt16Attr('total_path'),  # The signed two's complement integer total path signal quality in millibels.
                  DIUInt16Attr('quality')]  # A number between 0 and 10,000 representing quality, with 0 being poor quality and 10,000 being high quality.

    def get_first_path(self):
        """Returns the first path signal quality in decibels."""
        return self.first_path/100

    def get_total_path(self):
        """Returns the total path signal quality in decibels."""
        return self.total_path/100


class AnchorHealthV2(CDPDataItem):
    """CDP Data Item: Ciholas Data Protocol Anchor Health V2 Data Item Definition. Deprecated.
       This data type is used to report the health of anchors in the network."""

    type = 0x010F
    definition = [DISerialNumberAttr('serial_number'),  # The serial number of the anchor.
                  DIUInt8Attr('interface_id'),  # The interface identifier of the anchor.
                  DIUInt32Attr('beacons_reported'),  # The total quantity of tag Beacons that were reported by the anchor since the last Anchor Health Information.
                  DIUInt32Attr('beacons_discarded'),  # The total quantity of tag Beacons that were discarded from the anchor since the last Anchor Health Information.
                  DIUInt16Attr('average_quality'),  # The average quality number between 0 and 10,000, with 0 being poor quality and 10,000 being high quality for the anchor since the last Anchor Health Information.
                  DIUInt8Attr('report_period')]  # Period of the packet in seconds.


class InfrastructureV3(CDPDataItem):
    """CDP Data Item: Ciholas Data Protocol Infrastructure Position V3 Data Item Definition. Deprecated.
       This data type is used to report the 3 dimensional position of a stationary device."""

    type = 0x0110
    definition = [DISerialNumberAttr('serial_number'),  # Serial number of the infrastructure node.
                  DIUInt8Attr('interface_id'),  # The infrastructure node's interface identifier.
                  DIInt32Attr('x'),  # The signed x-coordinate from the origin.
                  DIInt32Attr('y'),  # The signed y-coordinate from the origin.
                  DIInt32Attr('z'),  # The signed z-coordinate from the origin.
                  DIUInt8Attr('node_type'),  # Type of the infrastructure node.
                  DIUInt8Attr('node_status')]  # Status of the node.


class InfrastructureV4(CDPDataItem):
    """CDP Data Item: Ciholas Data Protocol Infrastructure Position V4 Data Item Definition. Replaced by 0x0137 in v3.2.
       This data type is used to report the 3 dimensional position of a stationary device."""

    type = 0x0111
    definition = [DISerialNumberAttr('serial_number'),  # The serial number of the infrastructure node.
                  DIUInt8Attr('interface_id'),  # The infrastructure node's interface identifier.
                  DIInt32Attr('x'),  # The signed x-coordinate from the origin.
                  DIInt32Attr('y'),  # The signed y-coordinate from the origin.
                  DIInt32Attr('z'),  # The signed z-coordinate from the origin.
                  DIUInt8Attr('node_type'),  # Type of the infrastructure node. Seeder = 0x01. Anchor = 0x02.
                  DIUInt8Attr('node_active_state'),  # Whether the node is inactive/active. Inactive = 0x01. Active = 0x02.
                  DIUInt8Attr('node_lock_state')]  # Whether the node is unlocked/locked. Unlocked = 0x01. Locked = 0x02.


class TWRV1(CDPDataItem):
    """CDP Data Item: Ciholas Data Protocol TWR V1 Data Item Definition. Deprecated.
       This data type is used to transmit the TWR data between two devices."""

    type = 0x0112
    definition = [DISerialNumberAttr('serial_number_1'),  # The serial number of the first device.
                  DISerialNumberAttr('serial_number_2'),  # The serial number of the second device.
                  DIUInt8Attr('interface_id_1'),  # The interface identifier of the first device.
                  DIUInt8Attr('interface_id_2'),  # The interface identifier of the second device.
                  DIUInt64Attr('rx_timestamp'),  # Timestamp of last received packet.
                  DIUInt64Attr('distance')]  # The distance between the two devices, in millimeters.


class CDPStreamInformation(CDPDataItem):
    """CDP Data Item: Ciholas Data Protocol CDP Stream Information Data Item Definition. Current in v3.3.
       This data type is used to send the information that defines a stream the server is using."""

    type = 0x011A
    definition = [DIUInt32Attr('destination_ip'),  # The IP address of this stream.
                  DIUInt16Attr('destination_port'),  # The port of this stream.
                  DIUInt32Attr('interface_ip'),  # The interface IP address for this stream.
                  DIUInt32Attr('interface_netmask'),  # The interface netmask for this stream.
                  DIUInt16Attr('interface_port'),  # The interface/listening port being used by the net app. 0 indicates this field is not being used.
                  DIUInt8Attr('ttl'),  # The TTL of this stream.
                  DIVariableLengthStrAttr('name')]  # The name for this stream.


class HostnameAnnounce(CDPDataItem):
    """CDP Data Item: Ciholas Data Protocol Hostname Announce Data Item Definition. Current in v3.3.
       This data type is used to send the hostname of the computer that is running the server."""

    type = 0x011B
    definition = [DIVariableLengthStrAttr('hostname')]  # The hostname of the sending computer.


class InstanceAnnounce(CDPDataItem):
    """CDP Data Item: Ciholas Data Protocol Instance Announce Data Item Definition. Current in v3.3.
       This data type is used to send the instance name for the network."""

    type = 0x011C
    definition = [DIVariableLengthStrAttr('instance_name')]  # The instance name (name of database file) for the sending net app.


class AppSettingsChunk(CDPDataItem):
    """CDP Data Item: Ciholas Data Protocol App Settings Chunk Data Item Definition. Public.
       This data type is used to send a piece of the network settings for logging purposes."""

    type = 0x0121
    definition = [DIUInt16Attr('number_of_chunks'),  # The chunks needed to transmit all app settings.
                  DIUInt16Attr('chunk_id'),  # The ID of this chunk.
                  DIFixedLengthStrAttr('instance_name', 256),  # The instance name of the network.
                  DIVariableLengthBytesAttr('chunk_data')]  # 2^15 bytes of the database. The final chunk will have less bytes in it.


class SetMagnetometerCalibration(CDPDataItem):
    """CDP Data Item: Ciholas Data Protocol Set Magnetometer Calibration Data Item Definition. Removed in v3.2.
       Tells the server to send the magnetometer calibration values to a device."""

    type = 0x0123
    definition = [DISerialNumberAttr('serial_number'),  # The serial number of the device the calibrations are for.
                  DIInt16Attr('calibration_x'),  # The signed calibration values for the X axis.
                  DIInt16Attr('calibration_y'),  # The signed calibration values for the Y axis.
                  DIInt16Attr('calibration_z')]  # The signed calibration values for the Z axis.


class AnchorHealthV3(CDPDataItem):
    """CDP Data Item: Ciholas Data Protocol Anchor Health V3 Data Item Definition. Removed in v3.2.
    This data type is used to report the health of anchors in the network."""

    type = 0x0124
    definition = [DISerialNumberAttr('serial_number'),  # The serial number of the anchor.
                  DIUInt8Attr('interface_id'),  # The interface identifier of the anchor.
                  DIUInt32Attr('ticks_reported'),  # The total quantity of anchor Ticks that were reported by the anchor since the last Anchor Health Information.
                  DIUInt32Attr('timed_rxs_reported'),  # The total quantity of anchor Time Rxs that were reported by the anchor since the last Anchor Health Information.
                  DIUInt32Attr('beacons_reported'),  # The total quantity of tag Beacons that were reported since the last Anchor Health Information.
                  DIUInt32Attr('beacons_discarded'),  # The total quantity of tag Beacons that were discarded from the anchor since the last Anchor Health Information.
                  DIUInt16Attr('average_quality'),  # The average quality number between 0 and 10,000, with 0 being poor quality and 10,000 being high quality for the anchor since the last Anchor Health Information.
                  DIUInt8Attr('report_period')]  # The period of the packet in seconds.


class FullDeviceID:
    """Full Device ID Class Definition. Current in v3.3.
       This structure specifies the full identifier for a device, including both its serial number and interface identifier."""

    definition = [DISerialNumberAttr('serial_number'), # The serial number of the device.
                  DIUInt8Attr('interface_id')] # The interface identifier of the device.

    def __init__(self, serial_number=0, interface_id=0):
        self.serial_number = CiholasSerialNumber(serial_number)
        self.interface_id = interface_id

    def __str__(self):
        return "{}-{}".format(self.serial_number, self.interface_id)


class AnchorHealthV4(CDPDataItem):
    """CDP Data Item: Ciholas Data Protocol Anchor Health V4 Data Item Definition. Replaced by 0x014A in v3.3.
       This data type is used to report the health of anchors in the network."""

    type = 0x0125
    definition = [DISerialNumberAttr('serial_number'),  # The serial number of the anchor.
                  DIUInt8Attr('interface_id'),  # The interface identifier of the anchor.
                  DIUInt32Attr('ticks_reported'),  # The total quantity of anchor Ticks that were reported by the anchor since the last Anchor Health Information.
                  DIUInt32Attr('timed_rxs_reported'),  # The total quantity of anchor Timed Rxs that were reported by the anchor since the last Anchor Health Information.
                  DIUInt32Attr('beacons_reported'),  # The total quantity of tag Beacons that were reported by the anchor since the last Anchor Health Information.
                  DIUInt32Attr('beacons_discarded'),  # The total quantity of tag Beacons that were discarded from the anchor since the last Anchor Health Information.
                  DIUInt16Attr('average_quality'),  # The average of the quality number between 0 and 10,000, with 0 being poor quality and 10,000 being high quality for the anchor since the last Anchor Health Information.
                  DIUInt8Attr('report_period'),  # The period of the packet in seconds.
                  DIUInt8Attr('interanchor_comms_error_code'),  # Indicates whether there are any problems with inter-anchor communications involving this anchor. 0 = No error. 1 = Recommend blacklisting. 2 = Bad survey. 3 = Unknown.
                  DIListAttr('bad_paired_anchors', FullDeviceID)]  # A list of FullDeviceID structures that specify the anchors that this anchor is having trouble communicating with.

    def add_bad_paired_anchors(self, serial_number=0, interface_identifier=0):
        """Adds a FullDeviceID object to the list of bad paired anchors."""
        self.bad_paired_anchors.append(FullDeviceID(serial_number, interface_identifier))


class MagnetometerCalibrationResponse(CDPDataItem):
    """CDP Data Item: Ciholas Data Protocol Magnetometer Calibration Response Data Item Definition. Removed in v3.2.
       This data type is emitted by a wired device after it receives a set magnetometer calibration command."""

    type = 0x0126
    definition = [DIInt16Attr('calibration_x'),  # The signed calibration value for the X axis.
                  DIInt16Attr('calibration_y'),  # The signed calibration value for the Y axis.
                  DIInt16Attr('calibration_z')]  # The signed calibration value for the Z axis.


class DistanceV2(CDPDataItem):
    """CDP Data Item: Ciholas Data Protocol Distance V2 Data Item Definition. Current in v3.3.
       This data type is used to transmit the distance data between two devices."""

    type = 0x0127
    definition = [DISerialNumberAttr('serial_number_1'),  # The serial number of the first device.
                  DISerialNumberAttr('serial_number_2'),  # The serial number of the second device.
                  DIUInt8Attr('interface_id_1'),  # The interface identifier of the first device.
                  DIUInt8Attr('interface_id_2'),  # The interface identifier of the second device.
                  DIUInt64Attr('rx_timestamp'),  # Time at which the last packet was received.
                  DIUInt32Attr('distance'),  # The distance, in millimeters, between the two devices.
                  DIUInt16Attr('quality')]  # The quality of the computed device.


class ErrorPattern:
    """Error Pattern Class Definition. Current in v3.3."""

    definition = [DIUInt8Attr('pattern')]  # A single byte made up of three 2-bit color codes.
    colors = ['W','Y','B','G']

    def __init__(self, pattern=0):
        self.pattern = pattern

    def __str__(self):
        "{}{}{}".format(self.colors[(self.pattern >> 4) & 0x03],
                        self.colors[(self.pattern >> 2) & 0x03],
                        self.colors[(self.pattern >> 0) & 0x03])


class DeviceStatus(CDPDataItem):
    """CDP Data Item: Ciholas Data Protocol Device Status Definition. Replaced by 0x0138 in v3.2.
       This data type contains information about the current states of a device."""

    type = 0x0128
    definition = [DIUInt32Attr('memory'), # How much memory is free on the device.
                  DIUInt32Attr('flags'), # The device status flags.
                  DIUInt16Attr('minutes_remaining'), # When charging (flags.charging=1) this indicates the estimate of minutes until the device is fully charged. When discharging (flags.charging=0) this indicates the estimate of minutes until the device is fully discharged. When 65535, the time remaining is unknown.
                  DIUInt8Attr('battery_percentage'), # Percentage of battery charge left from 0 to 100. A value of 255 means no measurable battery is present.
                  DIInt8Attr('temperature'), # The two's complement temperature in degrees Celsius.
                  DIUInt8Attr('processor_usage'), # Percentage of processor usage from 0-100. A value of 255 represents an unknown value.
                  DIListAttr('error_patterns', ErrorPattern)]  # Array of current error states by their LED pattern.


class AccelerometerV1(CDPDataItem):
    """CDP Data Item: Ciholas Data Protocol Accelerometer V1 Definition. Replaced by 0x0139 in v3.2.
       This data type is used to report the accelerometer data from an onboard MPU-9250."""

    type = 0x0129
    definition = [DIUInt64Attr('network_time'), # The timestamp when the sensor recorded the data. This value is represented in Network Time, which is roughly 15.65 picoseconds per tick.
                  DIInt32Attr('x'), # The two's complement X accelerometer value.
                  DIInt32Attr('y'), # The two's complement Y accelerometer value.
                  DIInt32Attr('z'), # The two's complement Z accelerometer value.
                  DIUInt8Attr('scale')] # The full-scale representation in Gs.


class GyroscopeV1(CDPDataItem):
    """CDP Data Item: Ciholas Data Protocol Gyroscope V1 Definition. Replaced by 0x013A in v3.2.
       This data type is used to report the gyroscope data from an onboard MPU-9250."""

    type = 0x012A
    definition = [DIUInt64Attr('network_time'), # The timestamp when the sensor recorded the data. This value is represented in Network Time, which is roughly 15.65 picoseconds per tick.
                  DIInt32Attr('x'), # The two's complement X gyroscope value.
                  DIInt32Attr('y'), # The two's complement Y gyroscope value.
                  DIInt32Attr('z'), # The two's complement Z gyroscope value.
                  DIUInt16Attr('scale')] # The full-scale representation in degrees per second.


class MagnetometerV1(CDPDataItem):
    """CDP Data Item: Ciholas Data Protocol Magnetometer V1 Definition. Replaced by 0x013B in v3.2.
       This data type is used to report the magnetometer data from an onboard MPU-9250."""

    type = 0x012B
    definition = [DIUInt64Attr('network_time'), # The timestamp when the sensor recorded the data. This value is represented in Network Time, which is roughly 15.65 picoseconds per tick.
                  DIInt32Attr('x'), # The two's complement X magnetometer value.
                  DIInt32Attr('y'), # The two's complement Y magnetometer value.
                  DIInt32Attr('z'), # The two's complement Z magnetometer value.
                  DIUInt16Attr('scale')] # The full-scale representation in microtesla.


class PressureV1(CDPDataItem):
    """CDP Data Item: Ciholas Data Protocol Pressure V1 Definition. Replaced by 0x013C in v3.2.
       This data type is used to report the pressure measured by an onboard LPS25H."""

    type = 0x012C
    definition = [DIUInt64Attr('network_time'), # The timestamp when the sensor recorded the data. This value is represented in Network Time, which is roughly 15.65 picoseconds per tick.
                  DIInt32Attr('pressure'), # The two's complement pressure value.
                  DIUInt32Attr('scale')] # The full-scale representation in millibar.


class QuaternionV1(CDPDataItem):
    """CDP Data Item: Ciholas Data Protocol Quaternion V1 Definition. Replaced by 0x012D in v3.2.
       This data type is used to report quaternion data from an onboard MPU-9250."""

    type = 0x012D
    definition = [DIUInt64Attr('network_time'), # The timestamp when the sensor recorded the data. This value is represented in Network Time, which is roughly 15.65 picoseconds per tick.
                  DIInt32Attr('x'), # The two's complement X quaternion value.
                  DIInt32Attr('y'), # The two's complement Y quaternion value.
                  DIInt32Attr('z'), # The two's complement Z quaternion value.
                  DIInt32Attr('w'), # The two's complement W quaternion value.
                  DIBoolAttr('normalized')] # 1 for normalized, 0 for unnormalized.


class TemperatureV1(CDPDataItem):
    """CDP Data Item: Ciholas Data Protocol Temperature V1 Definition. Replaced by 0x012E in v3.2.
       This data type is used to report the temperature measured by an onboard LPS25H."""

    type = 0x012E
    definition = [DIUInt64Attr('network_time'), # The timestamp when the sensor recorded the data. This value is represented in Network Time, which is roughly 15.65 picoseconds per tick.
                  DIInt16Attr('temperature'), # The two's complement temperature value.
                  DIUInt16Attr('scale')] # The full-scale representation in degrees Celsius.


class PositionV2(CDPDataItem):
    """CDP Data Item: Ciholas Data Protocol Position V2 Data Item Definition. Replaced by 0x013E in v3.2.
       This data type is used to report the 3 dimensional position of the reporting device."""

    type = 0x012F
    definition = [DIUInt64Attr('network_time'),  # The timestamp when the sensor recorded the data. This value is represented in Network Time, which is roughly 15.65 picoseconds per tick.
                  DIInt32Attr('x'),  # The signed x-coordinate in millimeters.
                  DIInt32Attr('y'),  # The signed y-coordinate in millimeters.
                  DIInt32Attr('z'),  # The signed z-coordinate in millimeters.
                  DIUInt32Attr('quality'),  # The quality indicator.
                  DIUInt16Attr('smoothing')]  # The effective smoothing factor (the number of positions averaged minus 1).

    def get_xyz(self):
        """Returns x, y, and z coordinates values in mm in the form of a list."""
        return [self.x, self.y, self.z]


class GyroscopeCalibration(CDPDataItem):
    """CDP Data Item: Ciholas Data Protocol Gyroscope Calibration Data Item Definition. Removed in v3.2.
       This data type is emitted by a wired device after it receives a set magnetometer calibration command."""

    type = 0x0130
    definition = [DISerialNumberAttr('serial_number'),  # The serial number of the recipient.
                  DIInt32Attr('calibration_x'),  # The signed calibration value for the X axis.
                  DIInt32Attr('calibration_y'),  # The signed calibration value for the Y axis.
                  DIInt32Attr('calibration_z'),  # The signed calibration value for the Z axis.
                  DIInt16Attr('scale')]  # The full-scale representation in degrees/sec.


class PortInfo:
    """Connection Info Class Definition. Protected."""

    definition = [DIUInt16Attr('port_id'),  # The ID of the port. 4 bits = priority, 12 bits = port number.
                  DIUInt64Attr('neighbor'),  # The ID of the neighbor bridge to this port. If there are multiple neighbors, only one will appear.
                  DIUInt16Attr('neighbor_port'),  # The ID of the neighbor's port.
                  DIUInt8Attr('protocol'),  # Indicates if STP(0) or RSTP(1) is being used.
                  DIUInt8Attr('state'),  # Indicates if the port is blocking packets(0) or forwarding(1).
                  DIUInt8Attr('role'),  # Indicates the role of the port. 0 = Unknown. 1 = Root (port faces the root) 2 = Designated (port faces away from the root). 3 = Alternate (port is redundant). 4 = Backup (port is a self-loop). 5 = Disabled.
                  DIUInt16Attr('info_timer')]  # How long until the port's information becomes outdated (only relevant on designated, alternate, and backup ports).

    def __init__(self, port_id=0, neighbor=0, neighbor_port=0, protocol=0, state=0, role=0, info_timer=0):
        self.port_id = port_id
        self.neighbor = neighbor
        self.neighbor_port = neighbor_port
        self.protocol = protocol
        self.state = state
        self.role = role
        self.info_timer = info_timer


class RstpReport(CDPDataItem):
    """CDP Data Item: Ciholas Data Protocol Connection Report Data Item Definition. Protected."""

    type = 0x0131
    definition = [DIBoolAttr('enabled'),  # Boolean indicating if rapid spanning tree protocol for bridges is enabled.
                  DIUInt64Attr('root'),  # The ID (2 bytes of priority and 6 bytes of MAC address) of the root bridge of the tree.
                  DIUInt16Attr('max_age'),  # The maximum length of a branch of a tree.
                  DIUInt16Attr('forward_delay'),  # Ports wait this long before forwarding packets after losing a neighbor.
                  DIUInt8Attr('num_ports'),  # The number of ports on the device, corresponds to number of connection Info units.
                  DIListAttr('port_info', PortInfo)]  # Port-specific data.


class PositionV3(CDPDataItem):
    """CDP Data Item: Ciholas Data Protocol Position V3 Data Item Definition. Current in v3.3.
       This data type is used to report the 3 dimensional position of the reporting device."""

    type = 0x0135
    definition = [DISerialNumberAttr('serial_number'),  # The serial number of the reporting device.
                  DIUInt64Attr('network_time'),  # The timestamp when the sensor recorded the data. This value is represented in Network Time, which is roughly 15.65 picoseconds per tick.
                  DIInt32Attr('x'),  # The signed x-coordinate in millimeters.
                  DIInt32Attr('y'),  # The signed y-coordinate in millimeters.
                  DIInt32Attr('z'),  # The signed z-coordinate in millimeters.
                  DIUInt16Attr('quality'),  # The quality of the assessed position, with 0 being an assessment of poor quality and 10,000 being an assessment of perfect quality.
                  DIUInt8Attr('anchor_count'),  # The number of anchors involved in the calculation of this position.
                  DIUInt8Attr('flags'),  # 1 bit = inactive mode. 1 bit = was not calculated. 6 bits = unused.
                  DIUInt16Attr('smoothing')]  # The effective smoothing factor (the number of positions averages minus 1).

    def get_xyz(self):
        """Returns x, y, and z coordinates values in mm in the form of a list."""
        return [self.x, self.y, self.z]

    def is_inactive(self):
        """Returns true if the reporting device is in inactive mode, false otherwise."""
        return (self.flags >> 7) == 1

    def was_not_calculated(self):
        """Returns true if the position of the reporting device was not calculated, false otherwise."""
        return ((self.flags >> 6) & 0x01) == 1


class PositionAnchorStatusStructure:
    """Position Anchor Status Class Definition. Current in v3.3.
       The ANCHOR STATUS ARRAY field in the Position's Anchor Status data item is an array of these Anchor Status Structures."""

    definition = [DISerialNumberAttr('anchor_serial_number'), # The serial number of the anchor.
                  DIUInt8Attr('anchor_interface_identifier'), # The interface identifier of the anchor.
                  DIUInt8Attr('status'), # 0 = Anchor data is good. 1 = Anchor is unknown. 2 = Anchor data does not match other anchors. 3 = Anchor data is inconsistent with previous data. 4 = Network time not synchronized. 5 = Anchor data is not good enough for tracking. 6 = Duplicate anchor data. 7 = Old data used to fill for a missed packed.
                  DIInt16Attr('first_path'), # The first path signal quality in millibels. This value is a signed two's complement integer.
                  DIInt16Attr('total_path'), # The total path signal quality in millibels. This value is a signed two's complement integer.
                  DIUInt16Attr('quality')] # A number from 0 to 10,000, with 0 being poor quality and 10,000 being high quality.

    def __init__(self, anchor_serial_number=0, anchor_interface_identifier=0, status=0, first_path=0, total_path=0, quality=0):
        self.anchor_serial_number = CiholasSerialNumber(anchor_serial_number)
        self.anchor_interface_id = anchor_interface_identifier
        self.status = status
        self.first_path = first_path
        self.total_path = total_path
        self.quality = quality

    def __str__(self):
        return "{}-{}, {}, {}, {}, {}".format(self.anchor_serial_number, self.anchor_interface_id, self.status, self.first_path, self.total_path, self.quality)

    def get_first_path(self):
        """Returns the first path signal quality in decibels."""
        return self.first_path/100

    def get_total_path(self):
        """Returns the total path signal quality in decibels."""
        return self.total_path/100


class AnchorPositionStatusV3(CDPDataItem):
    """CDP Data Item: Ciholas Data Protocol Anchor Position Status V3 Data Item Definition. Current in v3.3.
       This data type is used to report the status of an anchor that provided location data about the reporting device."""

    type = 0x0136
    definition = [DISerialNumberAttr('tag_serial_number'),  # The serial number of the tag.
                  DIUInt64Attr('network_time'),  # The Network Time of the position.
                  DIListAttr('anchor_status_array', PositionAnchorStatusStructure)]  # Array of Anchor Status Structures.


class DeviceActivityState(CDPDataItem):
    """CDP Data Item: Ciholas Data Protocol Device Activity State V5 Data Item Definition. Current in v3.3.
       This data type is used to report the current state of a device on the network."""

    type = 0x0137
    definition = [DISerialNumberAttr('serial_number'),  # The device's serial number.
                  DIUInt8Attr('interface_id'),  # The device's interface identifier.
                  DIInt32Attr('x'),  # The signed x-coordinate from the origin.
                  DIInt32Attr('y'),  # The signed y-coordinate from the origin.
                  DIInt32Attr('z'),  # The signed z-coordinate from the origin.
                  DIUInt8Attr('role_id'),  # The identifier for the role this device is currently functioning as. Pair with the Role Report to match this identifier to the role's name.
                  DIUInt8Attr('connectivity_state'),  # Specifies Ethernet or UWB connectivity.
                  DIUInt8Attr('synchronization_state')]  # Specifies TX and RX sync status.


class DeviceHardwareStatusV2(CDPDataItem):
    """CDP Data Item: Ciholas Data Protocol Device Hardwave Status V2 Data Item Definition. Current in v3.3.
       This data type contains information about the current states of a device."""

    type = 0x0138
    definition = [DISerialNumberAttr('serial_number'), # The serial number of the reporting device.
                  DIUInt32Attr('memory'), # How much memory is free on the device.
                  DIUInt32Attr('flags'), # Device Status Flags.
                  DIUInt16Attr('minutes_remaining'), # When charging (flags.charging=1) this indicates the estimate of minutes until the device is fully charged. When discharging (flags.charging=0) this indicates the estimate of minutes until the device is fully discharged. When 65535, the time remaining is unknown.
                  DIUInt8Attr('battery_percentage'), # Percentage of battery charge left from 0-100. A value of 255 means no measurable battery is present.
                  DIInt8Attr('temperature'), # The two's complement temperature in degrees Celsius.
                  DIUInt8Attr('processor_usage'), # Percentage of processor usage from 0-100. A value of 255 represents an unknown value.
                  DIListAttr('error_patterns', ErrorPattern)]  # Array of current error states by their LED pattern.


class AccelerometerV2(CDPDataItem):
    """CDP Data Item: Ciholas Data Protocol Accelerometer V2 Data Item Definition. Replaced by 0x17A in v4.5.
       This data type is used to report the accelerometer data from an onboard MPU-9250."""

    type = 0x0139
    definition = [DISerialNumberAttr('serial_number'), # The serial number of the reporting device.
                  DIUInt64Attr('network_time'), # The timestamp when the sensor recorded the data. This value is represented in Network Time, which is roughly 15.65 picoseconds per tick.
                  DIInt32Attr('x'), # The two's complement X accelerometer value.
                  DIInt32Attr('y'), # The two's complement Y accelerometer value.
                  DIInt32Attr('z'), # The two's complement Z accelerometer value.
                  DIUInt8Attr('scale')] # The full-scale representation in Gs.


class GyroscopeV2(CDPDataItem):
    """CDP Data Item: Ciholas Data Protocol Gyroscope V2 Data Item Definition. Replaced by 0x17B in v4.5.
       This data type is used to report the gyroscope data from an onboard MPU-9250."""

    type = 0x013A
    definition = [DISerialNumberAttr('serial_number'), # The serial number of the reporting device.
                  DIUInt64Attr('network_time'), # The timestamp when the sensor recorded the data. This value is represented in Network Time, which is roughly 15.65 picoseconds per tick.
                  DIInt32Attr('x'), # The two's complement X gyroscope value.
                  DIInt32Attr('y'), # The two's complement Y gyroscope value.
                  DIInt32Attr('z'), # The two's complement Z gyroscope value.
                  DIUInt16Attr('scale')] # The full-scale representation in Degrees Per Second.


class MagnetometerV2(CDPDataItem):
    """CDP Data Item: Ciholas Data Protocol Magnetometer V2 Data Item Definition. Replaced by 0x17C in v4.5.
       This data type is used to report the magnetometer data from an onboard MPU-9250."""

    type = 0x013B
    definition = [DISerialNumberAttr('serial_number'), # The serial number of the reporting device.
                  DIUInt64Attr('network_time'), # The timestamp when the sensor recorded the data. This value is represented in Network Time, which is roughly 15.65 picoseconds per tick.
                  DIInt32Attr('x'), # The two's complement X magnetometer value.
                  DIInt32Attr('y'), # The two's complement Y magnetometer value.
                  DIInt32Attr('z'), # The two's complement Z magnetometer value.
                  DIUInt16Attr('scale')] # The full-scale representation in microtesla.


class PressureV2(CDPDataItem):
    """CDP Data Item: Ciholas Data Protocol Pressure V2 Data Item Definition. Current in v3.3.
       This data type is used to report the pressure measured by an onboard LPS25H."""

    type = 0x013C
    definition = [DISerialNumberAttr('serial_number'), # The serial number of the reporting device.
                  DIUInt64Attr('network_time'), # The timestamp when the sensor recorded the data. This value is represented in Network Time, which is roughly 15.65 picoseconds per tick.
                  DIInt32Attr('pressure'), # The two's complement pressure value.
                  DIUInt32Attr('scale')] # The full-scale representation in millibar.


class QuaternionV2(CDPDataItem):
    """CDP Data Item: Ciholas Data Protocol Quaternion V2 Data Item Definition. Current in v3.3.
       This data type is used to report quaternion data from an onboard MPU-9250."""

    type = 0x013D
    definition = [DISerialNumberAttr('serial_number'), # The serial number of the reporting device.
                  DIUInt64Attr('network_time'), # The timestamp when the sensor recorded the data. This value is represented in Network Time, which is roughly 15.65 picoseconds per tick.
                  DIInt32Attr('x'), # The two's complement X quaternion value.
                  DIInt32Attr('y'), # The two's complement Y quaternion value.
                  DIInt32Attr('z'), # The two's complement Z quaternion value.
                  DIInt32Attr('w'), # The two's complement W quaternion value.
                  DIUInt8Attr('quaternion_type')] # An enumeration of all different types of quaternions. 0 = Using accelerometer and gyroscope not normalized. 1 = Using accelerometer and gyroscope normalized. 2 = Using accelerometer, gyroscope, and magnetometer normalized.


class TemperatureV2(CDPDataItem):
    """CDP Data Item: Ciholas Data Protocol Temperature V2 Data Item Definition. Current in v3.3.
       This data type is used to report the temperature measured by an onboard LPS25H."""

    type = 0x013E
    definition = [DISerialNumberAttr('serial_number'), # The serial number of the reporting device.
                  DIUInt64Attr('network_time'), # The timestamp when the sensor recorded the data. This value is represented in Network Time, which is roughly 15.65 picoseconds per tick.
                  DIInt16Attr('temperature'), # The two's complement temperature value.
                  DIUInt16Attr('scale')] # The full-scale representation in degrees Celsius.


class DeviceNames(CDPDataItem):
    """CDP Data Item: Ciholas Data Protocol Device Names Data Item Definition. Current in v3.3.
       This data type is used to report the device names."""

    type = 0x013F
    definition = [DISerialNumberAttr('serial_number'), # The serial number of the device.
                  DIVariableLengthStrAttr('name')] # The name of the device provided in the CUWB Manager.


class Synchronization(CDPDataItem):
    """CDP Data Item: Ciholas Data Protocol Synchronization Data Item Definition. Current in v3.3.
       This data type is used to report current synchronization counts."""

    type = 0x0140
    definition = [DIUInt16Attr('max_tx_sync_count'), # The maximum possible number of anchors that can be Transmit Synchronized on this network.
                  DIUInt16Attr('current_tx_sync_count'), # The current number of anchors that are Transmit Synchronized on this network.
                  DIUInt16Attr('max_rx_sync_count'), # The maximum possible number of anchors that can be Receive Synchronized on this network.
                  DIUInt16Attr('current_rx_sync_count')] # The current number of anchors that are Receive Synchronized on this network.


class RoleReport(CDPDataItem):
    """CDP Data Item: Ciholas Data Protocol Role Report Data Item Definition. Current in v3.3.
       This data type is used to track the number of devices on a particular role."""

    type = 0x0141
    definition = [DIUInt16Attr('role_id'), # The identifier of the given role.
                  DIUInt16Attr('max_quantity'), # The maximum number of devices that are configured to the given role.
                  DIUInt16Attr('active_quantity'), # The current number of devices that are actively participating in the network as a member of the given role.
                  DIVariableLengthStrAttr('role_name')] # The name of the given role.


class UWBNetworkCommand:
    """UWB Network Command Class Definition. Protected."""

    def __init__(self, destination_group=0, type=0, length=0, data=0):
        self.destination_group = CiholasSerialNumber(destination_group)
        self.type = type
        self.length = length
        self.data = data

    def __str__(self):
        return "{}, 0x{:02X}, {}, {}".format(self.destination_group,
                                             self.type,
                                             self.length,
                                             self.data.hex())


class DirectCommand(CDPDataItem):
    """CDP Data Item: Ciholas Data Protocol Direct Command Data Item Definition. Protected.
       Execute command sent over Ethernet."""

    type = 0x0142
    definition = [DIListAttr('commands', UWBNetworkCommand)] # List of UWB Network Commands.

    def _decode(self):
        self.commands = []
        while self.di_data:
            grp, typ, lng = struct.unpack("<IBH", self.di_data[:7])
            cmd_data = self.di_data[7:7+lng]
            self.commands.append(UWBNetworkCommand(grp, typ, lng, cmd_data))
            self.di_data = self.di_data[7+lng:]
        self.di_data = None

    def _encode(self):
        data = b''
        for cmd in self.commands:
            data += struct.pack("<IBH{:d}s".format(cmd.length), cmd.destination_group.as_int,
                                cmd.type, cmd.length, cmd.data)
        self.di_size = len(data)
        return struct.pack("<HH", self.type, self.di_size) + data

    def add_uwb_network_command(self, destination_group=0, type=0, length=0, data=0):
        """Adds a UWBNetworkCommand object to the list of commands."""
        self.commands.append(UWBNetworkCommand(destination_group, type, length, data))


class UserDefinedV2(CDPDataItem):
    """CDP Data Item: Ciholas Data Protocol User Defined V2 Data Item Definition. Public.
       This data type is used to report any user defined data bytes."""

    type = 0x0148
    definition = [DISerialNumberAttr('serial_number'),  # The serial number of the device sending the user-defined data.
                  DIVariableLengthBytesAttr('payload')]  # The format of the contents are defined by the user.


class NetworkTime(CDPDataItem):
    """CDP Data Item: Ciholas Data Protocol Network Time Data Item Definition. Protected."""

    type = 0x0149
    definition = [DISerialNumberAttr('server_instance'),  # The server instance this packet is intended for.
                  DIUInt64Attr('network_time'),  # The Network Time when this packet was transmitted.
                  DIUInt8Attr('nt_quality')]  # The Network Time quality at the time this packet was transmitted.


class AnchorHealthV5(CDPDataItem):
    """CDP Data Item: Ciholas Data Protocol Anchor Health V5 Data Item Definition. Current in v3.3.
       This data type is used to report the health of anchors in the network."""

    type = 0x014A
    definition = [DISerialNumberAttr('serial_number'), # The serial number of the anchor.
                  DIUInt8Attr('interface_id'),  # The interface identifier of the anchor.
                  DIUInt32Attr('ticks_reported'),  # The total quantity of anchor Ticks that were reported by the anchor since the last Anchor Health Information.
                  DIUInt32Attr('timed_rxs_reported'),  # The total quantity of Timed Rxs that were reported by the anchor since the last Anchor Health Information.
                  DIUInt32Attr('beacons_reported'),  # The total quantity of tag Beacons that were reported by the anchor since the last Anchor Health Information.
                  DIUInt32Attr('beacons_discarded'),  # The total quantity of tag Beacons that were discarded from the anchor since the last Anchor Health Information.
                  DIUInt32Attr('beacons_late'), # The total quantity of tag Beacons that were late from the anchor since the last Anchor Health Information.
                  DIUInt16Attr('average_quality'),  # The average of the quality number from 0 to 10,000, with 0 being poor quality, 10,000 being high quality for the anchor since the last Anchor Health Information.
                  DIUInt8Attr('report_period'),  # Period of the packet in seconds.
                  DIUInt8Attr('interanchor_comms_error_code'),  # Specifies type of comms errors between anchors. 0 = No Error. 1 = Blacklisting. 2 = Bad Survey.
                  DIListAttr('bad_paired_anchors', FullDeviceID)]  # Array of neighboring anchors that this anchor is having trouble communicating with.

    def add_bad_paired_anchors(self, serial_number=0, interface_identifier=0):
        """Adds a FullDeviceID object to the list of bad paired anchors."""
        self.bad_paired_anchors.append(FullDeviceID(serial_number, interface_identifier))


class GlobalPingTimingReportV1(CDPDataItem):
    """CDP Data Item: Ciholas Data Protocol Global Ping Timing Report V1 Data Item Definition. Current in v3.3.
       This data type is used to track the amount of relative delay between ping receptions from different anchors for the same tag transmission."""

    type = 0x014C
    num_time_count_indexes = 1001
    definition = [DIUInt32Attr('initial_ping_count'),  # The number of starting Pings that were received (and thus the number of positions that were calculated).
                  DIUInt32Attr('position_calculation_delay'),  # Time from the reception of initial Ping to the start of the position calculation.
                  DIUInt32ListAttr('arrival_time_counts')]  # An array of 1001 counters that track the number of Pings that were received X msec after the initial Ping, where the index in the array is X-1. Index 1000 represents all Pings that were received at least 1 full second later than the initial Ping.


class TopologyInfo(CDPDataItem):
    """CDP Data Item: Ciholas Data Protocol Topology Info Data Item Definition. Protected.
       This data type describes a physical connection between two entities. This includes DWETHs, Anchors, and other LLDP-enabled computers."""

    type = 0x0157
    definition = [DIBoolAttr('internal'),  # Indicates if the anchor is internal.
                  DIUInt8Attr('links'),  # Indicates the number of active links on the anchor.
                  DIBoolAttr('up'),  # Indicates if the link is being added or removed.
                  DIFixedLengthStrAttr('sender', 32),  # The ID of the sender.
                  DIFixedLengthStrAttr('sender_port', 32),  # The port ID of the sender.
                  DIFixedLengthStrAttr('neighbor', 32),  # The neighbor's ID.
                  DIFixedLengthStrAttr('neighbor_port', 32)]  # The neighbor's port ID.


class PtpInfo(CDPDataItem):
    """CDP Data Item: Ciholas Data Protocol PTP Info Data Item Definition. Protected.
       This data type is sent by anchors running PTP for time modeling purposes."""

    type = 0x0158
    definition = [DIFixedLengthBytesAttr('master_mac', 6),  # The mac address of the master clock.
                  DISerialNumberAttr('master_serial'),  # The serial number of the master clock.
                  DIInt64Attr('master_to_slave'),  # The time a packet took to travel from the master clock to the slave clock in nanoseconds.
                  DIInt64Attr('slave_to_master'),  # The time a packet took to travel from the slave clock to the master clock in nanoseconds.
                  DIInt64Attr('mean_path_delay'),  # The onboard calculated average of the travel times in nanoseconds.
                  DIInt64Attr('offset'),  # The offset of the slave from the master in nanoseconds.
                  DIInt64Attr('model')]  # The offset calculated by the time model in nanoseconds.


class NtRealTimeMappingV1(CDPDataItem):
    """CDP Data Item: Ciholas Data Protocol NT Realtime Mapping V1 Data Item Definition. Public.
       This data type is emitted periodically with information for mapping NT time to real time."""

    type = 0x015A
    definition = [DIUInt64Attr('network_time_previous'),  # The Network Time as recorded approximately 1 second before this data item was transmitted.
                  DIUInt64Attr('real_time_previous'),  # The real time, measured in microseconds, as recorded approximately 1 second before this data item was transmitted.
                  DIUInt64Attr('network_time_current'),  # The most recently recorded Network Time available at the time this data item was transmitted.
                  DIUInt64Attr('real_time_current')]  # The most recently recorded real time, measured in microseconds, available at the time this data item was transmitted.


class SetPersistentProperty(CDPDataItem):
    """CDP Data Item: Ciholas Data Protocol Set Persistent Property Definition. Protected.
       This data type sets or clears a persistent property on a device."""

    type = 0x015B
    definition = [DISerialNumberAttr('serial_number'),  # The serial number of the device to set the persistent property for.
                  DIUInt8Attr('config'),  # Whether to set or clear the persistent property. 1 = Set. 0 = Clear.
                  DIUInt16Attr('property_id'),  # The ID of the property to set or clear.
                  DIVariableLengthBytesAttr('property_value')]  # The value of the property.

    def clear_persistent_property(self):
        """Sets the config field to 0 to clear the persistent property."""
        self.config = 0

    def set_persistent_property(self):
        """Sets the config field to 1 to set the persistent property."""
        self.config = 1


class GetPersistentPropertyValue(CDPDataItem):
    """CDP Data Item: Ciholas Data Protocol Get Persistent Property Value Definition. Protected.
       This data type retrieves the value of a persistent property on the device."""

    type = 0x015C
    definition = [DISerialNumberAttr('serial_number'),  # The serial number of the device to get the persistent property from.
                  DIUInt16Attr('property_id')]  # The ID of the property to get.


class GetPersistentPropertyList(CDPDataItem):
    """CDP Data Item: Ciholas Data Protocol Get Persistent Property List Definition. Protected.
       This data type retrieves a list of the persistent properties on a device."""

    type = 0x015D
    definition = [DISerialNumberAttr('serial_number')]  # The serial number of the device to get the persistent properties from.


class GetPersistentPropertyValueResponse(CDPDataItem):
    """CDP Data Item: Ciholas Data Protocol Get Persistent Property Value Response Definition. Protected.
       This data type retrieves the response of a persistent property on a device."""

    type = 0x015E
    definition = [DISerialNumberAttr('serial_number'),  # The serial number of the device the response is coming from.
                  DIUInt16Attr('property_id'),  # Identifier of the requested persistent property.
                  DIVariableLengthBytesAttr('value')]  # Value of the requested persistent property.


class GetPersistentPropertyListResponse(CDPDataItem):
    """CDP Data Item: Ciholas Data Protocol Get Persistent Property List Response Definition. Protected."""

    type = 0x015F
    definition = [DISerialNumberAttr('serial_number'),  # The serial number of the device the responses are coming from.
                  DIUInt16ListAttr('property_ids')]  # Identifiers of the requested list of the device's persistent properties.


class BootloadProgress(CDPDataItem):
    """CDP Data Item: Ciholas Data Protocol Bootload Progress Definition. Public.
       This data type contains information on the progress of a bootload, including a rough percentage done."""

    type = 0x0160
    definition = [DISerialNumberAttr('serial_number'),  # The serial number of the device being bootloaded.
                  DIUInt8Attr('last_received_total_path_rssi'),  # Signal strength of the last signal received.
                  DIUInt16Attr('last_heard_packet_time'),  # The time that the last packet was heard in seconds.
                  DIFixedLengthBytesAttr('flags', 25),  # A set of 25 bytes representing the sectors that have been received by the device.
                  DIUInt8Attr('max_sectors_per_flag'),  # The maximum number of sectors to be represented by a single bit in the flags attribute.
                  DIUInt8Attr('last_max_sector_flag'),  # The position of the last flag that represents the maximum number of sectors. All after will represent one less sector per flag.
                  DIUInt16Attr('percentage')]  # Estimated percentage of sectors completed. Guaranteed to be less than or equal to the actual.


class PositionAnchorStatusStructureV4:
    """Position Anchor Status Class Definition V4. Public.
       The ANCHOR STATUS ARRAY field in the Position's Anchor Status V4 data item is an array of these Anchor Status Structures."""

    definition = [DISerialNumberAttr('anchor_serial_number'), # The serial number of the anchor.
                  DIUInt8Attr('anchor_interface_identifier'), # The interface identifier of the anchor.
                  DIUInt8Attr('status'), # 0 = Anchor data is good. 1 = Anchor is unknown. 2 = Anchor data does not match other anchors. 3 = Anchor data is inconsistent with previous data. 4 = Network time not synchronized. 5 = Anchor data is not good enough for tracking. 6 = Duplicate anchor data. 7 = Old data used to fill for a missed packed.
                  DIUInt16Attr('quality')] # A number from 0 to 10,000, with 0 being poor quality and 10,000 being high quality.

    def __init__(self, anchor_serial_number=0, anchor_interface_identifier=0, status=0, quality=0):
        self.anchor_serial_number = CiholasSerialNumber(anchor_serial_number)
        self.anchor_interface_id = anchor_interface_identifier
        self.status = status
        self.quality = quality

    def __str__(self):
        return "{}-{}, {}, {}".format(self.anchor_serial_number, self.anchor_interface_id, self.status, self.quality)


class AnchorPositionStatusV4(CDPDataItem):
    """CDP Data Item: Ciholas Data Protocol Anchor Position Status V4 Data Item Definition. Public.
       This data type is used to report the status of an anchor that provided location data about the reporting device."""

    type = 0x0161
    definition = [DISerialNumberAttr('tag_serial_number'),  # The serial number of the tag.
                  DIUInt64Attr('network_time'),  # The Network Time of the position.
                  DIListAttr('anchor_status_array', PositionAnchorStatusStructureV4)]  # Array of Anchor Status Structures.


class LinkMDStatus(CDPDataItem):
    """CDP Data Item: Ciholas Data Protocol LinkMD Diagnostic Status Data Item Definition. Public.
       This data type is used to provide cable status such as wire fault type and distance to fault from the device."""

    type = 0x0163
    definition = [DIUInt8Attr('port_number'),  # Ethernet switch port number.
                  DIUInt8Attr('cable_condition'),  # Ethernet cable condition. 0 = Normal condition. 1 = Open condition. 2 = Shorted condition. 3 = Cable Diagnostic failed. 4 = Cable is connected so linkmd was not performed.
                  DIUInt32Attr('distance_to_fault')]  # Distance to fault condition, in cm, in case of open and shorted cable condition.


class PolarCoordinatesV1(CDPDataItem):
    """CDP Data Item: Ciholas Data Protocol Polar Coordinates V1 Data Item Definition. Public.
       This data type is used to report the position of the reporting device in polar coordinates."""

    type = 0x0164
    definition = [DISerialNumberAttr('serial_number'),  # The serial number of the reporting device.
                  DIUInt64Attr('network_time'),  # The timestamp when the sensor recorded the data. This value is represented in Network Time, which is roughly 15.65 picoseconds per tick.
                  DIUInt32Attr('rho'),  # The distance from the center of the anchor(s) to the tag in millimeters.
                  DIFloatAttr('theta'),  # The azimuth angle pointing from the center of the anchor(s) to the tag in degrees.  NOTE: This is a float value.
                  DIFloatAttr('phi'),  # The elevation angle pointing from the center of the anchor(s) to the tag in degrees.  NOTE: This is a float value.
                  DIUInt16Attr('quality'),  # The quality of the assessed position from 0 to 10000.
                  DIUInt8Attr('anchor_count'),  # The number of anchors involved in the calculation of this position.
                  DIUInt8Attr('flags'),  # 1 bit = inactive mode. 1 bit = was not calculated. 6 bits = unused.
                  DIUInt16Attr('smoothing')]  # The effective smoothing factor.


class PoeSystemStats(CDPDataItem):
    """CDP Data Item: Ciholas Data Protocol POE MCU System Status Data Item Definition. Protected.
        This data type is used to report POE system status."""

    type = 0x0165
    definition = [DIUInt64Attr('last_power_outage'),  # Time since last power outage in ms.
                  DIUInt64Attr('system_uptime'), # System uptime in ms.
                  DIUInt32Attr('power_limit_in'), # Power limit of input in mW.
                  DIUInt32Attr('power_limit_out'), # Power limit of output in mW.
                  DIUInt32Attr('power_limit_local'), # Local power limit in mW.
                  DIInt32Attr('p1_pair_voltage_1'), # Ethernet port 1 PR12 voltage in mV.
                  DIInt32Attr('p1_pair_voltage_2'), # Ethernet port 1 PR36 voltage in mV.
                  DIInt32Attr('p1_pair_voltage_3'), # Ethernet port 1 PR45 voltage in mV.
                  DIInt32Attr('p1_pair_voltage_4'), # Ethernet port 1 PR78 voltage in mV.
                  DIInt32Attr('p2_pair_voltage_1'), # Ethernet port 2 PR12 voltage in mV.
                  DIInt32Attr('p2_pair_voltage_2'), # Ethernet port 2 PR36 voltage in mV.
                  DIInt32Attr('p2_pair_voltage_3'), # Ethernet port 2 PR45 voltage in mV.
                  DIInt32Attr('p2_pair_voltage_4'), # Ethernet port 2 PR78 voltage in mV.
                  DIUInt16Attr('veth'), # Ethernet voltage in mV.
                  DIUInt16Attr('power_outage_count'), # Number of power outages since boot.
                  DIInt16Attr('p1_current'), # Ethernet port 1 current in mA.
                  DIInt16Attr('p2_current'), # Ethernet port 2 current in mA.
                  DIUInt8Attr('bot_fet'), # Bottom FET status formatted as a port mask.
                  DIUInt8Attr('top_fet'), # Top FET status formatted as a port mask.
                  DIUInt8Attr('desired_class'), # Class requested by the device.
                  DIUInt8Attr('granted_class'), # Class granted to the device.
                  DIUInt8Attr('downstream_requested_class'), # Downstream requested class.
                  DIUInt8Attr('downstream_granted_class'), # Downstream granted class.
                  DIUInt8Attr('lposc_cal'), # Calibration percentage for the low power oscillator.
                  DIUInt8Attr('mps_mode'), # MPS mode. 0 = OFF, 1 = ON, 2 = AUTO, 3 = PAUSED.
                  DIUInt8Attr('state'), # State machine state.
                  DIUInt8Attr('upstream_port'), # Port to treat as upstream.
                  DIUInt8Attr('mps_active_last_log'), # Power measurement MPS state.
                  DIUInt8Attr('poe_p1_mode'), # POE Port 1 mode. 0 = BOOT, 1 = OFF, 2 = INPUT, 3 = OUTPUT, 4 = CLASSIFYING.
                  DIUInt8Attr('poe_p2_mode'), # POE Port 2 mode. 0 = BOOT, 1 = OFF, 2 = INPUT, 3 = OUTPUT, 4 = CLASSIFYING.
                  DIUInt8Attr('poe_p1_pair_polarity_1'), # POE port 1 PR12 polarity. 0 = OPEN, 1 = NEGATIVE, 2 = POSITIVE.
                  DIUInt8Attr('poe_p1_pair_polarity_2'), # POE port 1 PR36 polarity. 0 = OPEN, 1 = NEGATIVE, 2 = POSITIVE.
                  DIUInt8Attr('poe_p1_pair_polarity_3'), # POE port 1 PR45 polarity. 0 = OPEN, 1 = NEGATIVE, 2 = POSITIVE.
                  DIUInt8Attr('poe_p1_pair_polarity_4'), # POE port 1 PR78 polarity. 0 = OPEN, 1 = NEGATIVE, 2 = POSITIVE.
                  DIUInt8Attr('poe_p2_pair_polarity_1'), # POE port 2 PR12 polarity. 0 = OPEN, 1 = NEGATIVE, 2 = POSITIVE.
                  DIUInt8Attr('poe_p2_pair_polarity_2'), # POE port 2 PR36 polarity. 0 = OPEN, 1 = NEGATIVE, 2 = POSITIVE.
                  DIUInt8Attr('poe_p2_pair_polarity_3'), # POE port 2 PR45 polarity. 0 = OPEN, 1 = NEGATIVE, 2 = POSITIVE.
                  DIUInt8Attr('poe_p2_pair_polarity_4'), # POE port 2 PR78 polarity. 0 = OPEN, 1 = NEGATIVE, 2 = POSITIVE.
                  DIUInt8Attr('poe_p1_source'), # Port 1 POE source. 0 = UNKNOWN, 1 = INJECTOR, 2 = PSE, 3 = INVALID.
                  DIUInt8Attr('poe_p2_source')] # Port 2 POE source. 0 = UNKNOWN, 1 = INJECTOR, 2 = PSE, 3 = INVALID.


class ImageV2:
    """Image Class V2 Definition. Public."""

    definition = [DIUInt8Attr('image_type'), # The type of image this data represents.
                  DIFixedLengthStrAttr('version', 32), # The version string of the image, null-terminated. If the string is less than the max (32B), it is padded with junk data.
                  DIFixedLengthBytesAttr('sha1', 20), # The IVSHA1 of the image with a maximum size of 20B.
                  DIUInt32Attr('image_length'), # The number of bytes the image contains.
                  DIUInt16Attr('flags'), # Flags that can extend the meaning of this image information.
                  DIVariableLengthBytesAttr('options')] # Additional information will be stored here, per the flags.

    def __init__(self, type=0, version=0, sha1=0, image_length=0, flags=0, options=b'', data=None):
        if data:
            self._decode(data)
        else:
            self.image_type = type
            self.version = version
            self.sha1 = sha1
            self.image_length = image_length
            self.flags = flags
            self.options = options

    def __str__(self):
        return "{}, {}, {}, {}, {}, {}".format(self.image_type, self.version, self.sha1.hex(), self.image_length, self.flags, self.options)

    def _decode(self, data):
        """Decodes a byte array as the ImageV2 object."""
        for attr in ImageV2.definition:
            value, size = attr._decode(data)
            data = data[size:]
            setattr(self, attr.name, value)

class BoundingBoxReport(CDPDataItem):
    """CDP Data Item: Ciholas Data Protocol Bounding Box Report Data Item Definition. Public.
       This data type is used to report the bounding box parameters."""

    type = 0x016A
    definition = [DIUInt32Attr('min_x'), # The minimum x-coordinate of the bounding zone in millimeters.
                  DIUInt32Attr('min_y'), # The minimum y-coordinate of the bounding zone in millimeters.
                  DIUInt32Attr('min_z'), # The minimum z-coordinate of the bounding zone in millimeters.
                  DIUInt32Attr('max_x'), # The maximum x-coordinate of the bounding zone in millimeters.
                  DIUInt32Attr('max_y'), # The maximum y-coordinate of the bounding zone in millimeters.
                  DIUInt32Attr('max_z')] # The maximum z-coordinate of the bounding zone in millimeters.


class BoundingCylinderReport(CDPDataItem):
    """CDP Data Item: Ciholas Data Protocol Bounding Cylinder Report Data Item Definition. Public.
       This data type is used to report the bounding cylinder parameters."""

    type = 0x016B
    definition = [DIUInt32Attr('x'), # The x-coordinate of the bottom center of the cylinder in millimeters.
                  DIUInt32Attr('y'), # The y-coordinate of the bottom center of the cylinder in millimeters.
                  DIUInt32Attr('z'), # The z-coordinate of the bottom center of the cylinder in millimeters.
                  DIUInt32Attr('radius'), # The radius of the cylinder in millimeters.
                  DIUInt32Attr('height')] # The height of the cylinder in millimeters.


class ImageDiscoveryV2(CDPDataItem):
    """CDP Data Item: Ciholas Data Protocol Image Discovery V2 Data Item Definition. Public.
    This data type contains information to inform the CUWB Network about the images the device is currently running. The CUWB network will use this information to determine if the device needs a firmware upgrade."""

    type = 0x0171
    definition = [DIUInt8Attr('vid'), # Virtual Vendor ID for device images.
                  DIUInt8Attr('pid'), # Virtual Product ID for device images.
                  DIUInt8Attr('running_image_type'), # Type of the current running image.
                  DIVariableLengthBytesAttr('tlvs')] # An array of TLV (Type Length Value) entries. Every entry will be prefixed with one byte for Type and one byte for Length.
                                                     # 1 = Sector size (size 2 bytes). 2 = No Change Echo (size 0 bytes). 3 = Bootloading Timeout (size 1 byte). 4 = Image Information V2 (size varies).

def ImageNotificationV2(CDPDataItem):
    """CDP Data Item: Ciholas Data Protocol Image Notification V2 Data Item Definition. Public.
    This data type notifies a device or device group of what images the CUWB Network can upload to them."""

    type = 0x0172
    definition = [DIUInt8Attr('vid'), # Virtual Vendor ID for device images.
                  DIUInt8Attr('pid'), # Virtual Product ID for device images.
                  DIUInt8Attr('running_image_type'), # Type of the current running image.
                  DIVariableLengthBytesAttr('tlvs')] # An array of TLV (Type Length Value) entries. Every entry will be prefixed with one byte for Type and one byte for Length.
                                                     # 1 = Sector size (size 2 bytes). 2 = No Change Echo (size 0 bytes). 3 = Bootloading Timeout (size 1 byte). 4 = Image Information V2 (size varies).


class Image:
    """Image Class Definition. Public."""

    definition = [DIUInt8Attr('type'),  # The type of image this data represents. 0 = Recover. 1 = Bootloader. 2 = Firmware. 3 = Almanac. 4 = Application.
                  DIFixedLengthStrAttr('version', 32),  # The version string of the image, null-terminated. If the string is less than the max (32B), it is padded with junk data.
                  DIFixedLengthBytesAttr('sha1', 20)]  # The IVSHA1 of the image with a maximum size of 20B.

    def __init__(self, type=0, version=0, sha1=0):
        self.type = type
        self.version = version
        self.sha1 = sha1

    def __str__(self):
        return "{}, {}, {}".format(self.type, self.version, self.sha1.hex())


class PoeSystemStatsV2(CDPDataItem):
    """CDP Data Item: Ciholas Data Protocol POE MCU System Status V2 Data Item Definition. Protected.
        This data type is used to report POE system status."""

    type = 0x0173
    definition = [DIUInt64Attr('last_power_outage'),  # Time since last power outage in ms.
                  DIUInt64Attr('system_uptime'), # System uptime in ms.
                  DIUInt32Attr('power_limit_in'), # Power limit of input in mW.
                  DIUInt32Attr('power_limit_out'), # Power limit of output in mW.
                  DIUInt32Attr('power_limit_local'), # Local power limit in mW.
                  DIInt32Attr('p1_pair_voltage_1'), # Ethernet port 1 PR12 voltage in mV.
                  DIInt32Attr('p1_pair_voltage_2'), # Ethernet port 1 PR36 voltage in mV.
                  DIInt32Attr('p1_pair_voltage_3'), # Ethernet port 1 PR45 voltage in mV.
                  DIInt32Attr('p1_pair_voltage_4'), # Ethernet port 1 PR78 voltage in mV.
                  DIInt32Attr('p2_pair_voltage_1'), # Ethernet port 2 PR12 voltage in mV.
                  DIInt32Attr('p2_pair_voltage_2'), # Ethernet port 2 PR36 voltage in mV.
                  DIInt32Attr('p2_pair_voltage_3'), # Ethernet port 2 PR45 voltage in mV.
                  DIInt32Attr('p2_pair_voltage_4'), # Ethernet port 2 PR78 voltage in mV.
                  DIInt32Attr('p1_current'), # Ethernet port 1 current in uA.
                  DIInt32Attr('p2_current'), # Ethernet port 2 current in uA.
                  DIInt32Attr('local_current'), # Local current in uA.
                  DIUInt16Attr('veth'), # Ethernet voltage in mV.
                  DIUInt16Attr('power_outage_count'), # Number of power outages since boot.
                  DIUInt8Attr('fets_status'), # Top and Bottom FET status formatted as a port mask. P2-PR78, P2-PR12, P1-PR78, P1-PR12, P2-PR45, P2-PR36, P1-PR45, P1-PR36.
                  DIUInt8Attr('desired_class'), # Class requested by the device.
                  DIUInt8Attr('granted_class'), # Class granted to the device.
                  DIUInt8Attr('downstream_requested_class'), # Downstream requested class.
                  DIUInt8Attr('downstream_granted_class'), # Downstream granted class.
                  DIUInt8Attr('mps_mode'), # MPS mode. MPS mode. 0 = UNKNOWN, 1 = OFF, 2 = TYPE 1/2, 3 = TYPE 3/4 CLASS 1-4, 4 = TYPE 3/4 CLASS 5-8.
                  DIUInt8Attr('state'), # State machine state.
                  DIUInt8Attr('upstream_port'), # Port to treat as upstream.
                  DIUInt8Attr('mps_active_last_log'), # Power measurement MPS state.
                  DIUInt8Attr('poe_p1_mode'), # POE Port 1 mode. 0 = BOOT, 1 = OFF, 2 = INPUT, 3 = OUTPUT, 4 = CLASSIFYING.
                  DIUInt8Attr('poe_p2_mode'), # POE Port 2 mode. 0 = BOOT, 1 = OFF, 2 = INPUT, 3 = OUTPUT, 4 = CLASSIFYING.
                  DIUInt8Attr('poe_p1_pair_polarity_1'), # POE port 1 PR12 polarity. 0 = OPEN/NEGATIVE, 1 = POSITIVE.
                  DIUInt8Attr('poe_p1_pair_polarity_2'), # POE port 1 PR36 polarity. 0 = OPEN/NEGATIVE, 1 = POSITIVE.
                  DIUInt8Attr('poe_p1_pair_polarity_3'), # POE port 1 PR45 polarity. 0 = OPEN/NEGATIVE, 1 = POSITIVE.
                  DIUInt8Attr('poe_p1_pair_polarity_4'), # POE port 1 PR78 polarity. 0 = OPEN/NEGATIVE, 1 = POSITIVE.
                  DIUInt8Attr('poe_p2_pair_polarity_1'), # POE port 2 PR12 polarity. 0 = OPEN/NEGATIVE, 1 = POSITIVE.
                  DIUInt8Attr('poe_p2_pair_polarity_2'), # POE port 2 PR36 polarity. 0 = OPEN/NEGATIVE, 1 = POSITIVE.
                  DIUInt8Attr('poe_p2_pair_polarity_3'), # POE port 2 PR45 polarity. 0 = OPEN/NEGATIVE, 1 = POSITIVE.
                  DIUInt8Attr('poe_p2_pair_polarity_4'), # POE port 2 PR78 polarity. 0 = OPEN/NEGATIVE, 1 = POSITIVE.
                  DIUInt8Attr('poe_p1_source'), # Port 1 POE source. 0 = UNKNOWN, 1 = INJECTOR, 2 = PSE, 3 = PSE3+, 4 = INVALID.
                  DIUInt8Attr('poe_p2_source')] # Port 2 POE source. 0 = UNKNOWN, 1 = INJECTOR, 2 = PSE, 3 = PSE3+, 4 = INVALID.


class BoundaryStatus(CDPDataItem):
    """CDP Data Item: Ciholas Data Protocol Boundary Status Data Item Definition. Protected.
        This data type is used to report boundary status of the system."""

    type = 0x0176
    definition = [DIUInt64Attr('network_time'),  # The timestamp when the sensor recorded the data. This value is represented in Network Time, which is roughly 15.65 picoseconds per tick.
                 DIInt32Attr('x'),  # The signed x-coordinate in millimeters.
                 DIInt32Attr('y'),  # The signed y-coordinate in millimeters.
                 DIInt32Attr('z'),  # The signed z-coordinate in millimeters.
                 DIUInt8Attr('status')]     # Current boundary status. 0 = NORMAL, 1 = WARNING, 2 = BREACHED.


class PositionlessBoundaryStatus(CDPDataItem):
    """CDP Data Item: Ciholas Data Protocol Positionless Boundary Status Data Item Definition. Protected.
        This data type is used to report positionless boundary status of the system."""

    type = 0x0177
    definition = [DIUInt64Attr('network_time'),  # The timestamp when the sensor recorded the data. This value is represented in Network Time, which is roughly 15.65 picoseconds per tick.
                 DIUInt8Attr('status')]     # Current boundary status. 0 = NORMAL, 1 = WARNING, 2 = BREACHED.


class QuaternionV3(CDPDataItem):
    """CDP Data Item: Ciholas Data Protocol Quaternion V3 Data Item Definition. Current in v4.0.
       This data type is used to report quaternion data, either from on-chip sensors or other sources."""

    type = 0x0178
    definition = [DISerialNumberAttr('serial_number'), # The serial number of the reporting device.
                  DIUInt64Attr('network_time'), # The timestamp when the sensor recorded the data. This value is represented in Network Time, which is roughly 15.65 picoseconds per tick.
                  DIInt32Attr('x'), # The two's complement X quaternion value.
                  DIInt32Attr('y'), # The two's complement Y quaternion value.
                  DIInt32Attr('z'), # The two's complement Z quaternion value.
                  DIInt32Attr('w'), # The two's complement W quaternion value.
                  DIUInt8Attr('quaternion_type'), # An enumeration of all different types of quaternions. 0 = Using accelerometer and gyroscope not normalized. 1 = Using accelerometer and gyroscope normalized. 2 = Using accelerometer, gyroscope, and magnetometer normalized.  3 = Using phase data normalized.
                  DIUInt16Attr('quality')] # The quality of the assessed quaternion from 0 to 10000.  If the quaternion is computed using an algorithm that does not support a quality calculation, then this value will be 0x4000.


class UserDefinedV3(CDPDataItem):
    """CDP Data Item: Ciholas Data Protocol User Defined V3 Data Item Definition. Public.
       This data type is used to report any user defined data bytes."""

    type = 0x0179
    definition = [DISerialNumberAttr('serial_number'),  # The serial number of the device sending the user-defined data.
                  DIUInt64Attr('network_time'), # The network time of the user-defined data.
                  DIVariableLengthBytesAttr('payload')]  # The format of the contents are defined by the user.


class AccelerometerV3(CDPDataItem):
    """CDP Data Item: Ciholas Data Protocol Accelerometer V3 Data Item Definition. Current in v4.5.
       This data type is used to report the accelerometer data from any accelerometer agnostic of chip placement."""

    type = 0x017A
    definition = [DISerialNumberAttr('serial_number'), # The serial number of the reporting device.
                  DIUInt64Attr('network_time'), # The timestamp when the sensor recorded the data. This value is represented in Network Time, which is roughly 15.65 picoseconds per tick.
                  DIInt32Attr('x'), # The two's complement X accelerometer value.
                  DIInt32Attr('y'), # The two's complement Y accelerometer value.
                  DIInt32Attr('z'), # The two's complement Z accelerometer value.
                  DIUInt8Attr('scale')] # The full-scale representation in Gs.


class GyroscopeV3(CDPDataItem):
    """CDP Data Item: Ciholas Data Protocol Gyroscope V2 Data Item Definition. Current in v4.5.
       This data type is used to report the gyroscope data from any gyroscope agnostic of chip placement."""

    type = 0x017B
    definition = [DISerialNumberAttr('serial_number'), # The serial number of the reporting device.
                  DIUInt64Attr('network_time'), # The timestamp when the sensor recorded the data. This value is represented in Network Time, which is roughly 15.65 picoseconds per tick.
                  DIInt32Attr('x'), # The two's complement X gyroscope value.
                  DIInt32Attr('y'), # The two's complement Y gyroscope value.
                  DIInt32Attr('z'), # The two's complement Z gyroscope value.
                  DIUInt16Attr('scale')] # The full-scale representation in Degrees Per Second.


class MagnetometerV3(CDPDataItem):
    """CDP Data Item: Ciholas Data Protocol Magnetometer V3 Data Item Definition. Current in v4.5.
       This data type is used to report the magnetometer data from any magnetometer agnostic of chip placement."""

    type = 0x017C
    definition = [DISerialNumberAttr('serial_number'), # The serial number of the reporting device.
                  DIUInt64Attr('network_time'), # The timestamp when the sensor recorded the data. This value is represented in Network Time, which is roughly 15.65 picoseconds per tick.
                  DIInt32Attr('x'), # The two's complement X magnetometer value.
                  DIInt32Attr('y'), # The two's complement Y magnetometer value.
                  DIInt32Attr('z'), # The two's complement Z magnetometer value.
                  DIUInt16Attr('scale')] # The full-scale representation in microtesla.


class CommandWindowUsageReport(CDPDataItem):
    """CDP Data Item: Ciholas Data Protocol Command Window Usage Report Data Item Definition.  Protected.
       This data type is used to report information related to the transmission of command packets. Includes info on the command windows as well."""
    
    type = 0x017D
    definition = [DIFloatAttr('average_used_windows'),   # The average number of command windows that have a preallocated use at any given time.
                  DIFloatAttr('average_reused_transmissions'),   # The average number of simultaneous transmissions occurring to support spatially reused transmissions. a value of 1.0 indicates that on average only 1 transmission is occurring per command window where a command is actually available.
                  DIFloatAttr('average_bytes_per_packet'),   # The average number of bytes in transmitted command packets.
                  DIFloatAttr('average_command_drops_per_second'),   # Average number of commands that have been dropped per second because no command windows were available.
                  DIUInt16Attr('preschedule_size'),  # The maximum number of command windows that the network will preallocate a use for.
                  DIUInt16Attr('current_used_preschedule_slots')] # The number of command windows that currently have a preallocated use.


class ImageDiscoveryV1(CDPDataItem):
    """CDP Data Item: Ciholas Data Protocol Image Discovery V1 Data Item Definition. Public.
       This data type contains information to inform the CUWB Network about the images the device is currently running. The CUWB network will use this information to determine if the device needs a firmware upgrade."""

    type = 0x8009
    definition = [DIFixedLengthStrAttr('manufacturer', 64),  # The manufacturer in a null-terminated string format. If the string is less than the max (64B), it is padded with junk data.
                  DIFixedLengthStrAttr('product', 32),  # The product type in a null-terminated string format. If the string is less than the max (32B), it is padded with junk data.
                  DIUInt8Attr('running_image_type'),  # Type of the current running image. 0 = Recover. 1 = Bootloader. 2 = Firmware. 3 = Almanac. 4 = Application.
                  DIListAttr('image_information', Image)] # An array of Image Information Structures identifying the images on the device.

    def add_image(self, type=0, version=0, sha1=0):
        """Adds an Image object to the image information list."""
        self.image_information.append(Image(type, version, sha1))


class TimedRxV5(CDPDataItem):
    """CDP Data Item: Ciholas Data Protocol Timed Reception V5 Data Item Definition. Current in v3.3.
       This data type is emitted by an anchor when it receives another anchor's Network Time Synchronization packet over UWB.  The serial number in the CDP Packet header will be the serial number of the receiving anchor."""

    type = 0x802C
    definition = [DIUInt64Attr('tx_nt64'),  # The Global Network Time at which the UWB Packet was transmitted.
                  DIUInt64Attr('rx_dt64'),  # The Decawave Time at which the UWB Packet was received.
                  DIUInt64Attr('rx_nt64'),  # The Global Network Time at which the UWB Packet was received.
                  DISerialNumberAttr('source_serial_number'),  # The serial number of the anchor that transmitted the UWB Packet.
                  DIUInt8Attr('source_interface_id'),  # Identifier of the interface from which the transmitting anchor transmitted the UWB Packet.
                  DISignalStrengthAttr('signal_strength'),  # Signal strength data of the reception.
                  DIUInt8Attr('interface_id'),  # Identifier of the interface on which the receiving anchor received the UWB Packet.
                  DIUInt8Attr('tx_nt_quality'),  # The quality of the Network Time Synchronization of the transmitting anchor at the time of its transmission.
                  DIUInt8Attr('rx_nt_quality'),  # The quality of the Network Time Synchronization of the receiving anchor at the time of its reception.
                  DIUInt8Attr('rx_packet_type')]  # The type of UWB Packet received.


class TickV4(CDPDataItem):
    """CDP Data Item: Ciholas Data Protocol Tick V4 Data Item Definition. Current in v3.3.
       This data type is emitted by an anchor when it transmits a Network Time Synchronization packet.  The serial number in the CDP Packet header will be the serial number of the transmitting anchor."""

    type = 0x802D
    definition = [DIUInt64Attr('nt64'),  # The Global Network Time at which this Network Time Packet was transmitted.
                  DIUInt64Attr('dt64'),  # The Decawave Time at which this Network Time Packet was transmitted.
                  DIUInt8Attr('nt_quality'),  # The quality of the Network Time Synchronization of the anchor at the time of this transmission.
                  DIUInt8Attr('interface_id')]  # The identifier for the interface through which the device transmitted this Network Time Packet.


class PingV5(CDPDataItem):
    """CDP Data Item: Ciholas Data Protocol Ping V5 Data Item Definition. Current in v3.3.
       This data type is emitted by an anchor when it receives a tag's UWB Beacon.  The serial number in the CDP Packet header will be the serial number of the receiving anchor."""

    type = 0x802F
    definition = [DISerialNumberAttr('source_serial_number'),  # The serial number of the tag that transmitted the UWB Beacon.
                  DIUInt16Attr('sequence'),  # The rolling sequence number of the Beacons emitted by the tag.
                  DIUInt8Attr('beacon_type'),  # There are several Beacon types which effect various properties of the UWB Beacon, such as the UWB packet length. NOTE: This does not effect the length of the Ping.
                  DIUInt8Attr('nt_quality'),  # The quality of the Network Time Synchronization of the anchor at the time of the reception of this UWB Beacon.
                  DIUInt64Attr('dt64'),  # The Decawave Time at which the UWB Beacon was received at this anchor.
                  DIUInt64Attr('nt64'),  # The Global Network Time at which the UWB Beacon was received at this anchor.
                  DISignalStrengthAttr('signal_strength'),  # The signal strength data of the reception.
                  DIUInt8Attr('interface_id'),  # Identifier of the interface on which this anchor received the UWB Beacon.
                  DIVariableLengthBytesAttr('payload')]  # Additional data received in the UWB Beacon.


class LEDStates:
    """LED States Class Definition. Protected."""

    definition = [DIUInt16Attr('start_time_offset'),  # Offset from now for start time of Diagnostic LEDs in milliseconds.
                  DIUInt16Attr('led_duration'),  # On Time of the Diagnostic LEDs in milliseconds.
                  DIUInt16Attr('led_period'),  # Period in milliseconds that this LED state should repeat.
                  DIUInt8Attr('red'),  # 0 -> Off, 255 -> On, 1 to 254 -> PWM.
                  DIUInt8Attr('green'),  # 0 -> Off, 255 -> On, 1 to 254 -> PWM.
                  DIUInt8Attr('blue')]  # 0 -> Off, 255 -> On, 1 to 254 -> PWM.

    def __init__(self, start_time_offset=0, led_duration=0, led_period=0, red=0, green=0, blue=0):
        self.start_time_offset = start_time_offset
        self.led_duration = led_duration
        self.led_period = led_period
        self.red = red
        self.green = green
        self.blue = blue

    def __str__(self):
        return ", ".join(str(getattr(self, attr.name)) for attr in self.definition)


class SetDiagnosticLED(CDPDataItem):
    """CDP Data Item: Ciholas Data Protocol Set Diagnostic LED Data Item Definition. Protected.
       This data type allows setting the Diagnostic LEDs on a device."""

    type = 0x803D
    definition = [DISerialNumberAttr('destination_group'),  # Destination group for the command.
                  DIListAttr('led_states', LEDStates)]  # Array of Diagnostic LED Structures.

    def add_led_states(self, start_time_offset=0, led_duration=0,
                       led_period=0, red=0, green=0, blue=0):
        """Adds an LED State object to the LED states list."""
        self.led_states.append(LEDStates(start_time_offset, led_duration,
                                         led_period, red, green, blue))


class DeviceData(CDPDataItem):
    """CDP Data Item: Ciholas Data Protocol Device Data Data Item Definition. Protected.
       This data type contains general and specific info for device data types."""

    type = 0x8042
    definition = [DIUInt64Attr('nt64'), # Reception time at the anchor.
                  DISignalStrengthAttr('signal_strength'), # Signal Strength of the reception.
                  DIUInt8Attr('interface_id'), # Interface ID of the receiver.
                  DIUInt8Attr('nt_quality'), # The quality of the reported Network Time.
                  DIVariableLengthBytesAttr('device_data')] # Contents of the Device Data UWB packet.


# When adding a new data item to cdp-py, follow the template given below.
# class <classname>(CDPDataItem):
#     """CDP Data Item: Ciholas Data Protocol <description> Data Item Definition. <version description (current in v3.3, deprecated, protected, etc.)>.
#        This data type <more detailed description (optional)>."""
#
#     type = <typename (0x0000)>
#     definition = [DataItemAttribute('<fieldname>'),  # <Description.>
#                   DataItemAttribute('<fieldname>')]  # <Description.>
#
#     def <method_name>(self):
#     """<Method description.>"""
#        return <return>
