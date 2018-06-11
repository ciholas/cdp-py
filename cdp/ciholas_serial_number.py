# pylint: disable=trailing-whitespace, too-few-public-methods

class CiholasSerialNumber():
    """Ciholas Serial Number Class Definition"""
    
    def __init__(self, value=0):
        if isinstance(value, str):
            self.as_int = (int)(value.replace(":", ""), 16)
        elif isinstance(value, int):
            self.as_int = value
        else:
            print("Invalid type for Ciholas Serial Number")
            exit(1)
        self.string = "{:02x}:{:02x}:{:04x}".format(self.as_int >> 24, 
                                                    (self.as_int >> 16) & 0xff, 
                                                    self.as_int & 0xffff).upper()

    def __str__(self):
        return self.string

    def __eq__(self, other):
        if isinstance(other, CiholasSerialNumber):
            return self.as_int == other.as_int
        if isinstance(other, int):
            return self.as_int == other
        if isinstance(other, str):
            # Other must be of the form 'XX:XX:XXXX'
            return self.string == other
        return False

    def __hash__(self):
        return hash(self.as_int)

    def __repr__(self):
        return self.__str__()
