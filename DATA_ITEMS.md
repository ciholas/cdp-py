### FullDeviceID
Full Device ID Class Definition. Current in v3.3.   
This structure specifies the full identifier for a device, including both its serial number and interface identifier.

| Field Name    | Size | Description |
|:---|:---:|:---|
| serial_number | 4B | The serial number of the device. |
| interface_id | 1B | The interface identifier of the device. |
### ErrorPattern
Error Pattern Class Definition. Current in v3.3.

| Field Name    | Size | Description |
|:---|:---:|:---|
| pattern | 1B | A single byte made up of three 2-bit color codes. |
### PositionAnchorStatusStructure
Position Anchor Status Class Definition. Current in v3.3.   
The ANCHOR STATUS ARRAY field in the Position's Anchor Status data item is an array of these Anchor Status Structures.

| Field Name    | Size | Description |
|:---|:---:|:---|
| anchor_serial_number | 4B | The serial number of the anchor. |
| anchor_interface_identifier | 1B | The interface identifier of the anchor. |
| status | 1B | 0 = Anchor data is good.<br/>1 = Anchor is unknown.<br/>2 = Anchor data does not match other anchors.<br/>3 = Anchor data is inconsistent with previous data.<br/>4 = Network time not synchronized.<br/>5 = Anchor data is not good enough for tracking.<br/>6 = Duplicate anchor data.<br/>7 = Old data used to fill for a missed packed. |
| first_path | 2B | The first path signal quality in millibels.<br/>This value is a signed two's complement integer. |
| total_path | 2B | The total path signal quality in millibels.<br/>This value is a signed two's complement integer. |
| quality | 2B | A number from 0 to 10,000, with 0 being poor quality and 10,000 being high quality. |
	Methods:
	  get_first_path(self)
	    Returns the first path signal quality in decibels.
	  get_total_path(self)
	    Returns the total path signal quality in decibels.
### PositionAnchorStatusStructureV4
Position Anchor Status Class Definition V4. Public.   
The ANCHOR STATUS ARRAY field in the Position's Anchor Status V4 data item is an array of these Anchor Status Structures.

| Field Name    | Size | Description |
|:---|:---:|:---|
| anchor_serial_number | 4B | The serial number of the anchor. |
| anchor_interface_identifier | 1B | The interface identifier of the anchor. |
| status | 1B | 0 = Anchor data is good.<br/>1 = Anchor is unknown.<br/>2 = Anchor data does not match other anchors.<br/>3 = Anchor data is inconsistent with previous data.<br/>4 = Network time not synchronized.<br/>5 = Anchor data is not good enough for tracking.<br/>6 = Duplicate anchor data.<br/>7 = Old data used to fill for a missed packed. |
| quality | 2B | A number from 0 to 10,000, with 0 being poor quality and 10,000 being high quality. |
### Image
Image Class Definition. Public.

| Field Name    | Size | Description |
|:---|:---:|:---|
| type | 1B | The type of image this data represents.<br/>0 = Recover.<br/>1 = Bootloader.<br/>2 = Firmware.<br/>3 = Almanac.<br/>4 = Application. |
| version | 32B | The version string of the image, null-terminated.<br/>If the string is less than the max (32B), it is padded with junk data. |
| sha1 | 20B | The IVSHA1 of the image with a maximum size of 20B. |
### 0x010D - NodeStatusChangeV2
CDP Data Item: Ciholas Data Protocol Node Status Change V2 Data Item Definition. Current in v3.3.   
This data type is used to report when the status for a node has changed.

| Field Name    | Size | Description |
|:---|:---:|:---|
| serial_number | 4B | The serial number of the node. |
| interface_id | 1B | The interface identifier of the node. |
| node_status | 1B | The status of the node.<br/>Inactive = 0x01. |
### 0x011A - CDPStreamInformation
CDP Data Item: Ciholas Data Protocol CDP Stream Information Data Item Definition. Current in v3.3.   
This data type is used to send the information that defines a stream the server is using.

| Field Name    | Size | Description |
|:---|:---:|:---|
| destination_ip | 4B | The IP address of this stream. |
| destination_port | 2B | The port of this stream. |
| interface_ip | 4B | The interface IP address for this stream. |
| interface_netmask | 4B | The interface netmask for this stream. |
| interface_port | 2B | The interface/listening port being used by the net app.<br/>0 indicates this field is not being used. |
| ttl | 1B | The TTL of this stream. |
| name | XB | The name for this stream. |
### 0x011B - HostnameAnnounce
CDP Data Item: Ciholas Data Protocol Hostname Announce Data Item Definition. Current in v3.3.   
This data type is used to send the hostname of the computer that is running the server.

| Field Name    | Size | Description |
|:---|:---:|:---|
| hostname | XB | The hostname of the sending computer. |
### 0x011C - InstanceAnnounce
CDP Data Item: Ciholas Data Protocol Instance Announce Data Item Definition. Current in v3.3.   
This data type is used to send the instance name for the network.

| Field Name    | Size | Description |
|:---|:---:|:---|
| instance_name | XB | The instance name (name of database file) for the sending net app. |
### 0x0121 - AppSettingsChunk
CDP Data Item: Ciholas Data Protocol App Settings Chunk Data Item Definition. Public.   
This data type is used to send a piece of the network settings for logging purposes.

| Field Name    | Size | Description |
|:---|:---:|:---|
| number_of_chunks | 2B | The chunks needed to transmit all app settings. |
| chunk_id | 2B | The ID of this chunk. |
| instance_name | 256B | The instance name of the network. |
| chunk_data | XB | 2^15 bytes of the database.<br/>The final chunk will have less bytes in it. |
### 0x0127 - DistanceV2
CDP Data Item: Ciholas Data Protocol Distance V2 Data Item Definition. Current in v3.3.   
This data type is used to transmit the distance data between two devices.

| Field Name    | Size | Description |
|:---|:---:|:---|
| serial_number_1 | 4B | The serial number of the first device. |
| serial_number_2 | 4B | The serial number of the second device. |
| interface_id_1 | 1B | The interface identifier of the first device. |
| interface_id_2 | 1B | The interface identifier of the second device. |
| rx_timestamp | 8B | Time at which the last packet was received. |
| distance | 4B | The distance, in millimeters, between the two devices. |
| quality | 2B | The quality of the computed device. |
### 0x0135 - PositionV3
CDP Data Item: Ciholas Data Protocol Position V3 Data Item Definition. Current in v3.3.   
This data type is used to report the 3 dimensional position of the reporting device.

| Field Name    | Size | Description |
|:---|:---:|:---|
| serial_number | 4B | The serial number of the reporting device. |
| network_time | 8B | The timestamp when the sensor recorded the data.<br/>This value is represented in Network Time, which is roughly 15.65 picoseconds per tick. |
| x | 4B | The signed x-coordinate in millimeters. |
| y | 4B | The signed y-coordinate in millimeters. |
| z | 4B | The signed z-coordinate in millimeters. |
| quality | 2B | The quality of the assessed position, with 0 being an assessment of poor quality and 10,000 being an assessment of perfect quality. |
| anchor_count | 1B | The number of anchors involved in the calculation of this position. |
| flags | 1B | 1 bit = inactive mode.<br/>1 bit = was not calculated.<br/>6 bits = unused. |
| smoothing | 2B | The effective smoothing factor (the number of positions averages minus 1). |
	Methods:
	  get_xyz(self)
	    Returns x, y, and z coordinates values in mm in the form of a list.
	  is_inactive(self)
	    Returns true if the reporting device is in inactive mode, false otherwise.
	  was_not_calculated(self)
	    Returns true if the position of the reporting device was not calculated, false otherwise.
### 0x0136 - AnchorPositionStatusV3
CDP Data Item: Ciholas Data Protocol Anchor Position Status V3 Data Item Definition. Current in v3.3.   
This data type is used to report the status of an anchor that provided location data about the reporting device.

| Field Name    | Size | Description |
|:---|:---:|:---|
| tag_serial_number | 4B | The serial number of the tag. |
| network_time | 8B | The Network Time of the position. |
| anchor_status_array | 12XB | Array of Anchor Status Structures. See [PositionAnchorStatusStructure](#positionanchorstatusstructure) for details. |
### 0x0137 - DeviceActivityState
CDP Data Item: Ciholas Data Protocol Device Activity State V5 Data Item Definition. Current in v3.3.   
This data type is used to report the current state of a device on the network.

| Field Name    | Size | Description |
|:---|:---:|:---|
| serial_number | 4B | The device's serial number. |
| interface_id | 1B | The device's interface identifier. |
| x | 4B | The signed x-coordinate from the origin. |
| y | 4B | The signed y-coordinate from the origin. |
| z | 4B | The signed z-coordinate from the origin. |
| role_id | 1B | The identifier for the role this device is currently functioning as.<br/>Pair with the Role Report to match this identifier to the role's name. |
| connectivity_state | 1B | Specifies Ethernet or UWB connectivity. |
| synchronization_state | 1B | Specifies TX and RX sync status. |
### 0x0138 - DeviceHardwareStatusV2
CDP Data Item: Ciholas Data Protocol Device Hardwave Status V2 Data Item Definition. Current in v3.3.   
This data type contains information about the current states of a device.

| Field Name    | Size | Description |
|:---|:---:|:---|
| serial_number | 4B | The serial number of the reporting device. |
| memory | 4B | How much memory is free on the device. |
| flags | 4B | Device Status Flags. |
| minutes_remaining | 2B | When charging (flags.charging=1) this indicates the estimate of minutes until the device is fully charged.<br/>When discharging (flags.charging=0) this indicates the estimate of minutes until the device is fully discharged.<br/>When 65535, the time remaining is unknown. |
| battery_percentage | 1B | Percentage of battery charge left from 0-100.<br/>A value of 255 means no measurable battery is present. |
| temperature | 1B | The two's complement temperature in degrees Celsius. |
| processor_usage | 1B | Percentage of processor usage from 0-100.<br/>A value of 255 represents an unknown value. |
| error_patterns | 1XB | Array of current error states by their LED pattern. See [ErrorPattern](#errorpattern) for details. |
### 0x0139 - AccelerometerV2
CDP Data Item: Ciholas Data Protocol Accelerometer V2 Data Item Definition. Current in v3.3.   
This data type is used to report the accelerometer data from an onboard MPU-9250.

| Field Name    | Size | Description |
|:---|:---:|:---|
| serial_number | 4B | The serial number of the reporting device. |
| network_time | 8B | The timestamp when the sensor recorded the data.<br/>This value is represented in Network Time, which is roughly 15.65 picoseconds per tick. |
| x | 4B | The two's complement X accelerometer value. |
| y | 4B | The two's complement Y accelerometer value. |
| z | 4B | The two's complement Z accelerometer value. |
| scale | 1B | The full-scale representation in Gs. |
### 0x013A - GyroscopeV2
CDP Data Item: Ciholas Data Protocol Gyroscope V2 Data Item Definition. Current in v3.3.   
This data type is used to report the gyroscope data from an onboard MPU-9250.

| Field Name    | Size | Description |
|:---|:---:|:---|
| serial_number | 4B | The serial number of the reporting device. |
| network_time | 8B | The timestamp when the sensor recorded the data.<br/>This value is represented in Network Time, which is roughly 15.65 picoseconds per tick. |
| x | 4B | The two's complement X gyroscope value. |
| y | 4B | The two's complement Y gyroscope value. |
| z | 4B | The two's complement Z gyroscope value. |
| scale | 2B | The full-scale representation in Degrees Per Second. |
### 0x013B - MagnetometerV2
CDP Data Item: Ciholas Data Protocol Magnetometer V2 Data Item Definition. Current in v3.3.   
This data type is used to report the magnetometer data from an onboard MPU-9250.

| Field Name    | Size | Description |
|:---|:---:|:---|
| serial_number | 4B | The serial number of the reporting device. |
| network_time | 8B | The timestamp when the sensor recorded the data.<br/>This value is represented in Network Time, which is roughly 15.65 picoseconds per tick. |
| x | 4B | The two's complement X magnetometer value. |
| y | 4B | The two's complement Y magnetometer value. |
| z | 4B | The two's complement Z magnetometer value. |
| scale | 2B | The full-scale representation in microtesla. |
### 0x013C - PressureV2
CDP Data Item: Ciholas Data Protocol Pressure V2 Data Item Definition. Current in v3.3.   
This data type is used to report the pressure measured by an onboard LPS25H.

| Field Name    | Size | Description |
|:---|:---:|:---|
| serial_number | 4B | The serial number of the reporting device. |
| network_time | 8B | The timestamp when the sensor recorded the data.<br/>This value is represented in Network Time, which is roughly 15.65 picoseconds per tick. |
| pressure | 4B | The two's complement pressure value. |
| scale | 4B | The full-scale representation in millibar. |
### 0x013D - QuaternionV2
CDP Data Item: Ciholas Data Protocol Quaternion V2 Data Item Definition. Current in v3.3.   
This data type is used to report quaternion data from an onboard MPU-9250.

| Field Name    | Size | Description |
|:---|:---:|:---|
| serial_number | 4B | The serial number of the reporting device. |
| network_time | 8B | The timestamp when the sensor recorded the data.<br/>This value is represented in Network Time, which is roughly 15.65 picoseconds per tick. |
| x | 4B | The two's complement X quaternion value. |
| y | 4B | The two's complement Y quaternion value. |
| z | 4B | The two's complement Z quaternion value. |
| w | 4B | The two's complement W quaternion value. |
| quaternion_type | 1B | An enumeration of all different types of quaternions.<br/>0 = Using accelerometer and gyroscope not normalized.<br/>1 = Using accelerometer and gyroscope normalized.<br/>2 = Using accelerometer, gyroscope, and magnetometer normalized. |
### 0x013E - TemperatureV2
CDP Data Item: Ciholas Data Protocol Temperature V2 Data Item Definition. Current in v3.3.   
This data type is used to report the temperature measured by an onboard LPS25H.

| Field Name    | Size | Description |
|:---|:---:|:---|
| serial_number | 4B | The serial number of the reporting device. |
| network_time | 8B | The timestamp when the sensor recorded the data.<br/>This value is represented in Network Time, which is roughly 15.65 picoseconds per tick. |
| temperature | 2B | The two's complement temperature value. |
| scale | 2B | The full-scale representation in degrees Celsius. |
### 0x013F - DeviceNames
CDP Data Item: Ciholas Data Protocol Device Names Data Item Definition. Current in v3.3.   
This data type is used to report the device names.

| Field Name    | Size | Description |
|:---|:---:|:---|
| serial_number | 4B | The serial number of the device. |
| name | XB | The name of the device provided in the CUWB Manager. |
### 0x0140 - Synchronization
CDP Data Item: Ciholas Data Protocol Synchronization Data Item Definition. Current in v3.3.   
This data type is used to report current synchronization counts.

| Field Name    | Size | Description |
|:---|:---:|:---|
| max_tx_sync_count | 2B | The maximum possible number of anchors that can be Transmit Synchronized on this network. |
| current_tx_sync_count | 2B | The current number of anchors that are Transmit Synchronized on this network. |
| max_rx_sync_count | 2B | The maximum possible number of anchors that can be Receive Synchronized on this network. |
| current_rx_sync_count | 2B | The current number of anchors that are Receive Synchronized on this network. |
### 0x0141 - RoleReport
CDP Data Item: Ciholas Data Protocol Role Report Data Item Definition. Current in v3.3.   
This data type is used to track the number of devices on a particular role.

| Field Name    | Size | Description |
|:---|:---:|:---|
| role_id | 2B | The identifier of the given role. |
| max_quantity | 2B | The maximum number of devices that are configured to the given role. |
| active_quantity | 2B | The current number of devices that are actively participating in the network as a member of the given role. |
| role_name | XB | The name of the given role. |
### 0x0148 - UserDefinedV2
CDP Data Item: Ciholas Data Protocol User Defined V2 Data Item Definition. Public.   
This data type is used to report any user defined data bytes.

| Field Name    | Size | Description |
|:---|:---:|:---|
| serial_number | 4B | The serial number of the device sending the user-defined data. |
| payload | XB | The format of the contents are defined by the user. |
### 0x014A - AnchorHealthV5
CDP Data Item: Ciholas Data Protocol Anchor Health V5 Data Item Definition. Current in v3.3.   
This data type is used to report the health of anchors in the network.

| Field Name    | Size | Description |
|:---|:---:|:---|
| serial_number | 4B | The serial number of the anchor. |
| interface_id | 1B | The interface identifier of the anchor. |
| ticks_reported | 4B | The total quantity of anchor Ticks that were reported by the anchor since the last Anchor Health Information. |
| timed_rxs_reported | 4B | The total quantity of Timed Rxs that were reported by the anchor since the last Anchor Health Information. |
| beacons_reported | 4B | The total quantity of tag Beacons that were reported by the anchor since the last Anchor Health Information. |
| beacons_discarded | 4B | The total quantity of tag Beacons that were discarded from the anchor since the last Anchor Health Information. |
| beacons_late | 4B | The total quantity of tag Beacons that were late from the anchor since the last Anchor Health Information. |
| average_quality | 2B | The average of the quality number from 0 to 10,000, with 0 being poor quality, 10,000 being high quality for the anchor since the last Anchor Health Information. |
| report_period | 1B | Period of the packet in seconds. |
| interanchor_comms_error_code | 1B | Specifies type of comms errors between anchors.<br/>0 = No Error.<br/>1 = Blacklisting.<br/>2 = Bad Survey. |
| bad_paired_anchors | 5XB | Array of neighboring anchors that this anchor is having trouble communicating with. See [FullDeviceID](#fulldeviceid) for details. |
	Methods:
	  add_bad_paired_anchors(self, serial_number=0, interface_identifier=0)
	    Adds a FullDeviceID object to the list of bad paired anchors.
### 0x014C - GlobalPingTimingReportV1
CDP Data Item: Ciholas Data Protocol Global Ping Timing Report V1 Data Item Definition. Current in v3.3.   
This data type is used to track the amount of relative delay between ping receptions from different anchors for the same tag transmission.

| Field Name    | Size | Description |
|:---|:---:|:---|
| initial_ping_count | 4B | The number of starting Pings that were received (and thus the number of positions that were calculated). |
| position_calculation_delay | 4B | Time from the reception of initial Ping to the start of the position calculation. |
| arrival_time_counts | XB | An array of 1001 counters that track the number of Pings that were received X msec after the initial Ping, where the index in the array is X-1.<br/>Index 1000 represents all Pings that were received at least 1 full second later than the initial Ping. |
### 0x015A - NtRealTimeMappingV1
CDP Data Item: Ciholas Data Protocol NT Realtime Mapping V1 Data Item Definition. Public.   
This data type is emitted periodically with information for mapping NT time to real time.

| Field Name    | Size | Description |
|:---|:---:|:---|
| network_time_previous | 8B | The Network Time as recorded approximately 1 second before this data item was transmitted. |
| real_time_previous | 8B | The real time, measured in microseconds, as recorded approximately 1 second before this data item was transmitted. |
| network_time_current | 8B | The most recently recorded Network Time available at the time this data item was transmitted. |
| real_time_current | 8B | The most recently recorded real time, measured in microseconds, available at the time this data item was transmitted. |
### 0x0160 - BootloadProgress
CDP Data Item: Ciholas Data Protocol Bootload Progress Definition. Public.   
This data type contains information on the progress of a bootload, including a rough percentage done.

| Field Name    | Size | Description |
|:---|:---:|:---|
| serial_number | 4B | The serial number of the device being bootloaded. |
| last_received_total_path_rssi | 1B | Signal strength of the last signal received. |
| last_heard_packet_time | 2B | The time that the last packet was heard in seconds. |
| flags | 25B | A set of 25 bytes representing the sectors that have been received by the device. |
| max_sectors_per_flag | 1B | The maximum number of sectors to be represented by a single bit in the flags attribute. |
| last_max_sector_flag | 1B | The position of the last flag that represents the maximum number of sectors.<br/>All after will represent one less sector per flag. |
| percentage | 2B | Estimated percentage of sectors completed.<br/>Guaranteed to be less than or equal to the actual. |
### 0x0161 - AnchorPositionStatusV4
CDP Data Item: Ciholas Data Protocol Anchor Position Status V4 Data Item Definition. Public.   
This data type is used to report the status of an anchor that provided location data about the reporting device.

| Field Name    | Size | Description |
|:---|:---:|:---|
| tag_serial_number | 4B | The serial number of the tag. |
| network_time | 8B | The Network Time of the position. |
| anchor_status_array | 8XB | Array of Anchor Status Structures. See [PositionAnchorStatusStructureV4](#positionanchorstatusstructurev4) for details. |
### 0x0163 - LinkMDStatus
CDP Data Item: Ciholas Data Protocol LinkMD Diagnostic Status Data Item Definition. Public.   
This data type is used to provide cable status such as wire fault type and distance to fault from the device.

| Field Name    | Size | Description |
|:---|:---:|:---|
| port_number | 1B | Ethernet switch port number. |
| cable_condition | 1B | Ethernet cable condition.<br/>0 = Normal condition.<br/>1 = Open condition.<br/>2 = Shorted condition.<br/>3 = Cable Diagnostic failed.<br/>4 = Cable is connected so linkmd was not performed. |
| distance_to_fault | 4B | Distance to fault condition, in cm, in case of open and shorted cable condition. |
### 0x0164 - PolarCoordinatesV1
CDP Data Item: Ciholas Data Protocol Polar Coordinates V1 Data Item Definition. Public.   
This data type is used to report the position of the reporting device in polar coordinates.

| Field Name    | Size | Description |
|:---|:---:|:---|
| serial_number | 4B | The serial number of the reporting device. |
| network_time | 8B | The timestamp when the sensor recorded the data.<br/>This value is represented in Network Time, which is roughly 15.65 picoseconds per tick. |
| rho | 4B | The distance from the center of the anchor(s) to the tag in millimeters. |
| theta | 4B | The azimuth angle pointing from the center of the anchor(s) to the tag in degrees.<br/> NOTE: This is a float value. |
| phi | 4B | The elevation angle pointing from the center of the anchor(s) to the tag in degrees.<br/> NOTE: This is a float value. |
| quality | 2B | The quality of the assessed position from 0 to 10000. |
| anchor_count | 1B | The number of anchors involved in the calculation of this position. |
| flags | 1B | 1 bit = inactive mode.<br/>1 bit = was not calculated.<br/>6 bits = unused. |
| smoothing | 2B | The effective smoothing factor. |
### 0x8009 - ImageDiscoveryV1
CDP Data Item: Ciholas Data Protocol Image Discovery V1 Data Item Definition. Public.   
This data type contains information to inform the CUWB Network about the images the device is currently running. The CUWB network will use this information to determine if the device needs a firmware upgrade.

| Field Name    | Size | Description |
|:---|:---:|:---|
| manufacturer | 64B | The manufacturer in a null-terminated string format.<br/>If the string is less than the max (64B), it is padded with junk data. |
| product | 32B | The product type in a null-terminated string format.<br/>If the string is less than the max (32B), it is padded with junk data. |
| running_image_type | 1B | Type of the current running image.<br/>0 = Recover.<br/>1 = Bootloader.<br/>2 = Firmware.<br/>3 = Almanac.<br/>4 = Application. |
| image_information | 53XB | An array of Image Information Structures identifying the images on the device. See [Image](#image) for details. |
	Methods:
	  add_image(self, type=0, version=0, sha1=0)
	    Adds an Image object to the image information list.
### 0x802C - TimedRxV5
CDP Data Item: Ciholas Data Protocol Timed Reception V5 Data Item Definition. Current in v3.3.   
This data type is emitted by an anchor when it receives another anchor's Network Time Synchronization packet over UWB.  The serial number in the CDP Packet header will be the serial number of the receiving anchor.

| Field Name    | Size | Description |
|:---|:---:|:---|
| tx_nt64 | 8B | The Global Network Time at which the UWB Packet was transmitted. |
| rx_dt64 | 8B | The Decawave Time at which the UWB Packet was received. |
| rx_nt64 | 8B | The Global Network Time at which the UWB Packet was received. |
| source_serial_number | 4B | The serial number of the anchor that transmitted the UWB Packet. |
| source_interface_id | 1B | Identifier of the interface from which the transmitting anchor transmitted the UWB Packet. |
| signal_strength | 12B | Signal strength data of the reception. |
| interface_id | 1B | Identifier of the interface on which the receiving anchor received the UWB Packet. |
| tx_nt_quality | 1B | The quality of the Network Time Synchronization of the transmitting anchor at the time of its transmission. |
| rx_nt_quality | 1B | The quality of the Network Time Synchronization of the receiving anchor at the time of its reception. |
| rx_packet_type | 1B | The type of UWB Packet received. |
### 0x802D - TickV4
CDP Data Item: Ciholas Data Protocol Tick V4 Data Item Definition. Current in v3.3.   
This data type is emitted by an anchor when it transmits a Network Time Synchronization packet.  The serial number in the CDP Packet header will be the serial number of the transmitting anchor.

| Field Name    | Size | Description |
|:---|:---:|:---|
| nt64 | 8B | The Global Network Time at which this Network Time Packet was transmitted. |
| dt64 | 8B | The Decawave Time at which this Network Time Packet was transmitted. |
| nt_quality | 1B | The quality of the Network Time Synchronization of the anchor at the time of this transmission. |
| interface_id | 1B | The identifier for the interface through which the device transmitted this Network Time Packet. |
### 0x802F - PingV5
CDP Data Item: Ciholas Data Protocol Ping V5 Data Item Definition. Current in v3.3.   
This data type is emitted by an anchor when it receives a tag's UWB Beacon.  The serial number in the CDP Packet header will be the serial number of the receiving anchor.

| Field Name    | Size | Description |
|:---|:---:|:---|
| source_serial_number | 4B | The serial number of the tag that transmitted the UWB Beacon. |
| sequence | 2B | The rolling sequence number of the Beacons emitted by the tag. |
| beacon_type | 1B | There are several Beacon types which effect various properties of the UWB Beacon, such as the UWB packet length.<br/>NOTE: This does not effect the length of the Ping. |
| nt_quality | 1B | The quality of the Network Time Synchronization of the anchor at the time of the reception of this UWB Beacon. |
| dt64 | 8B | The Decawave Time at which the UWB Beacon was received at this anchor. |
| nt64 | 8B | The Global Network Time at which the UWB Beacon was received at this anchor. |
| signal_strength | 12B | The signal strength data of the reception. |
| interface_id | 1B | Identifier of the interface on which this anchor received the UWB Beacon. |
| payload | XB | Additional data received in the UWB Beacon. |
