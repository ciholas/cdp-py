CDP-PY Changelog
--

## HEAD

## 1.7.1
* Fixed PyPi release process

## 1.7.0
* Modified cdp class data decoding to increase speed/performance
* Modified CiholasSerialNumber to Cache string representation
* Modified CiholasSerialNumber to implement boolean operators
* Modified CiholasSerialNumber to increase speed/performance
* Added DeviceData support
* Modified DeviceData to use the DeviceDataItem class
* Added TickV5 (0x80B2) and TimedRxV6 (0x80B3) data items
* Changed CommandWindowUsageReport (0x017D) average_used_windows field name to percentage_used_windows
* Added DeviceStatusV3 data item (0x80D4)

## 1.6.2
* Added DeviceData data item (0x8042)

## 1.6.1
* Bug Fixes

## 1.6.0
* Added Image Discovery V2 (0x0171), and Image Notification V2 (0x0172)
* Added POE System Stats V2 data item (0x0173)
* Added Bounding Box Report (0x016A)
* Added Bounding Cylinder Report (0x016B)
* Added boundary status data item (0x0176)
* Added positionless boundary status data item (0x0177)
* Added User Defined V3 data item (0x0179)
* Added Clock Packet (0x80AD) and NTC Command Acknowledge (0x80B0) data items

## 1.5.0
* Added new Bootload Progress data item (0x0160)
* Added new Topology Info data item (0x0157)
* Added new Ptp Info data item (0x0158)
* Added new NT Real Time Mapping data item (0x015A)
* Added the Set Persistent Property (0x015B)
* Added Get Persistent Property Value (0x015C)
* Added Get Persistent Property List (0x015D)
* Added Get Persistent Property Value Response (0x015E)
* Added Get Persistent Property List Response (0x015F)
* Added new Set Diagnostic LED data item (0x803D)
* Added new linkMD Cable Diagnostic data item (0x0163)
* Added new POE System Stats data item (0x0165)
* Added new Polar Coordinates V1 data item (0x0164)

## 1.4.0
* Added getters for the flags in the Position V3 data item
* Changed attribute type for final field in QuaternionV2 data item

## 1.3.2
* Fixed parsing issue with the README.md file

## 1.3.1
* Updated project documentation

## 1.3.0
* Added new Anchor Health V5 data item (0x014A)
* Added new Global Ping Timing Report V1 data item (0x014C)
* Added new Network Time data item (0x0149)
* Added new Deliver User Data V1 data item (0x010C)
* Added new Connection Report data item (0x0131)
* Added new Rx Stats CDP data item attribute
* Added new App Settings Chunk (0x0121)
* Added Image Discovery V1 (0x8009)

## 1.2.0
* Added new User Defined V2 (0x0148)
* Added the TimedRxV5 (0x802C)
* Added TickV4 (0x802D)
* Added PingV5 (0x802F)

## 1.1.0
* Added new CDP data items: 0x0135-0x0142

## 1.0.1
* Fixed issue with initializing a list attribute to its default value
* Added CDP Gyroscope Calibration (0x0130)

## 1.0.0
* Initial cdp-py public release
