# Ciholas, Inc. - www.ciholas.com
# Licensed under: creativecommons.org/licenses/by/4.0
# pylint: disable=trailing-whitespace, too-few-public-methods

class CiholasSerialNumber(int):
    """Ciholas Serial Number Class Definition"""

    def __new__(cls, value=0):
        value_as_int = 0
        if isinstance(value, int):
            value_as_int = int(value)
        elif isinstance(value, str):
            value_as_int = (int)(value.replace(":", ""), 16)
        else:
            raise ValueError("Invalid type for Ciholas Serial Number")
        obj = int.__new__(cls, value_as_int)
        obj.as_int = value_as_int
        obj.string = "{:02x}:{:02x}:{:04x}".format(obj.as_int >> 24,
                                                    (obj.as_int >> 16) & 0xff,
                                                    obj.as_int & 0xffff).upper()
        return obj

    def __int__(self):
        return self.as_int

    def __str__(self):
        return self.string

    def __eq__(self, other):
        if isinstance(other, int):
            return self.__int__() == other
        if isinstance(other, str):
            # Other must be of the form 'XX:XX:XXXX'
            return self.__str__() == other
        return False

    def __hash__(self):
        return hash(self.__int__())

    def __repr__(self):
        return self.__str__()
