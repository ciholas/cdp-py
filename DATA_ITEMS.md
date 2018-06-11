Data Items
----------

## Creating New Data Item Definitions

1. Create a new class that inherits from `CDPDataItem` to the corresponding file.

2. Declare the `type` and `definition` of the data item as class variables. The `definition` variable should be assigned a list containing any of the following predefined data item's attributes:

| Data Item Attribute              | Size  | Signed | Argument(s)       |
| :------------------------------- | :---: | :----: | :---------------: |
| DIUInt8Attr                  | 1B    | False  | name              |
| DIInt8Attr                   | 1B    | True   | name              |
| DIUInt16Attr                 | 2B    | False  | name              |
| DIInt16Attr                  | 2B    | True   | name              |
| DIUInt32Attr                 | 4B    | False  | name              |
| DIInt32Attr                  | 4B    | True   | name              |
| DIFloatAttr                  | 4B    | True   | name              |
| DIUInt64Attr                 | 8B    | False  | name              |
| DIInt64Attr                  | 8B    | True   | name              |
| DIDoubleAttr                 | 8B    | True   | name              |
| DIFixedLengthStrAttr         |  -    |    -   | name, size        |
| DIVariableLengthStrAttr ^1       |  -    |    -   | name              |
| DIFixedLengthBytesAttr           |  -    |    -   | name, size        |
| DIVariableLengthBytesAttr ^1     |  -    |    -   | name              |
| DISerialNumberAttr ^2            | 4B    |    -   | name              |
| DISignalStrengthAttr ^3          | 12B   |    -   | name              |
| DICondensedSignalStrengthAttr ^4 | 2B    |    -   | name              |
| DIListAttr ^5                    |  -    |    -   | name, class_name^5|
| DISerialNumberListAttr ^2        |  -    |    -   | name              |

> Notes:
> 1. This attribute must be the only one and the last one in the definition since its size is assumed to be the remaining data.
> 2. See `CiholasSerialNumber` class definition for more details.
> 3. See `UWBSignalStrength` class definition for more details.
> 4. See `UWBCondensedSignalStrength` class definition for more details.
> 5. This attribute requires a helper structure. The class name must be passed as an argument -- i.e., DIListAttr('image_list', Image)
> 6. In case it is impossible to define a CDP data item using the attributes listed above because of its structure. The data item class should override the `decode` and `encode` methods defined in the `CDPDataItem` class.

## Existing Helper Structures

| Helper Structure      | Data Item Type(s) |
| :-------------------- | :---------------: |
| BucketSettings        | 0x0114            |
| PinConfig             | 0x000D, 0x000E    |
| FullDeviceID          | 0x0125            |

## Adding a New Helper Structure

1. Add a `definition` class variable and define the structure's attributes using the same Data Item Attributes listed above.

2. At least, define both `__init__()` and `__str__()` methods. If a structure's `definition` uses `DISerialNumberAttr`, `DISignalStrengthAttr`, or `DICondensedSignalStrengthAtt`, make sure the structure's attribute is properly initialized in the constructor by creating an instance of the class associated with the attribute. For example:

```python
    class MyStructure:
    """My Structure Class Definition"""
    definition = [DISerialNumberAttr('serial_number'),
        DIUInt8Attr('interface_id')]

    def __init__(self, serial_number=0, interface_id=0):
        self.serial_number = CiholasSerialNumber(serial_number)  
        self.interface_id = interface_id

    def __str__(self):
        return "{}, {}".format(self.serial_number, self.interface_id)
```

See any of the existing helper structures for more details.
