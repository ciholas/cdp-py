# Ciholas, Inc. - www.ciholas.com
# Licensed under: creativecommons.org/licenses/by/4.0
# pylint: disable=trailing-whitespace, too-few-public-methods

class CiholasSerialNumber:
    """Ciholas Serial Number Class Definition"""

    __slots__ = ('as_int', 'string')   #This saves 'some' memory for large lists, and increases speed a small amount

    def __init__(self, value=0):

        if   type(value) is int                 : self.as_int = value
        elif type(value) is float               : self.as_int = int(value)
        elif type(value) is str                 : self.as_int = int(         value.replace(":", ""), 16) 
        elif type(value) is bytes               : self.as_int = int(value.decode().replace(":", ""), 16)
        elif type(value) is CiholasSerialNumber : self.as_int = value.as_int
        else :
            raise TypeError("Invalid type for value argument.")

        self.string = None

    def __str__(self):

        if self.string is None :
            self.string = "{:02X}:{:02X}:{:04X}".format( (self.as_int >> 24)         ,
                                                         (self.as_int >> 16) &   0xff,
                                                         (self.as_int      ) & 0xffff)
        return self.string

    def __int__(self):
        return self.as_int

    def __format__(self, specifier) :
        if   any(element in specifier for element in 'xXdcfboeEg') : return f'{self.as_int:{   specifier}}' 
        elif         's' in specifier                              : return f'{self.__str__():{specifier}}'
        else                                                       : return    self.__str__()

    def __eq__(self, other):
        try                                : result = (self.as_int == other.as_int)
        except (TypeError, AttributeError) : result = (self.as_int == CiholasSerialNumber(other).as_int)
        return result

    def __lt__(self, other):
        try                                : result = (self.as_int <  other.as_int)
        except (TypeError, AttributeError) : result = (self.as_int <  CiholasSerialNumber(other).as_int)
        return result
  
    def __gt__(self, other):
        try                                : result = (self.as_int >  other.as_int)
        except (TypeError, AttributeError) : result = (self.as_int >  CiholasSerialNumber(other).as_int)
        return result
  
    def __le__(self, other):
        try                                : result = (self.as_int <= other.as_int)
        except (TypeError, AttributeError) : result = (self.as_int <= CiholasSerialNumber(other).as_int)
        return result 
  
    def __ge__(self, other):
        try                                : result = (self.as_int >= other.as_int)
        except (TypeError, AttributeError) : result = (self.as_int >= CiholasSerialNumber(other).as_int)
        return result 

    def __hash__(self):
        return hash(self.as_int)

    def __repr__(self):
        return self.__str__()