import math


class Bits:
    def __init__(self,
                 value,
                 byteorder='little',
                 strbase=10):
        accepted_types = (
            Bits,
            bytes,
            str,
            int
        )

        if not isinstance(value, accepted_types):
            raise TypeError(' '.join([
                'Expected one of types',
                ','.join([str(at) for at in accepted_types]),
                'for value'
            ]))

        if not isinstance(byteorder, str):
            raise TypeError('Expected ' + str(str) + ' for byteorder')
        else:
            byteorder = byteorder.lower()
        if byteorder not in ('little', 'big'):
            raise ValueError(' '.join([
                'Expected one of',
                '\'little\' or \'big\'',
                'for byteorder'
            ]))
        self.__byteorder = byteorder

        if not isinstance(strbase, int):
            raise TypeError('Expected ' + str(int) + ' for strbase')
        self.__strbase = strbase

        if isinstance(value, Bits):
            self.__int = value.__int
        elif isinstance(value, str):
            self.__int = int(value, strbase)
        elif isinstance(value, int):
            self.__int = value
        elif isinstance(value, bytes):
            self.__int = int.from_bytes(value, byteorder, signed=True)

    @property
    def byteorder(self):
        return self.__byteorder

    @byteorder.setter
    def byteorder(self, val):
        if isinstance(val, str):
            self.__byteorder = val
        else:
            raise TypeError('Expected {}'.format(str(str)))

    @property
    def strbase(self):
        return self.__strbase

    @strbase.setter
    def strbase(self, val):
        if isinstance(val, int):
            self.__strbase = val
        else:
            raise TypeError('Expected {}'.format(str(int)))

    def __and__(self, other):
        if not isinstance(other, Bits):
            raise NotImplemented
        return Bits(self.__int & other.__int)

    def __or__(self, other):
        if not isinstance(other, Bits):
            raise NotImplemented
        return Bits(self.__int | other.__int)

    def __xor__(self, other):
        if not isinstance(other, Bits):
            raise NotImplemented
        return Bits(self.__int ^ other.__int)

    def __eq__(self, other):
        if not isinstance(other, Bits):
            raise NotImplemented
        return self.__int == other.__int

    def __ne__(self, other):
        if not isinstance(other, Bits):
            raise NotImplemented
        return self.__int != other.__int

    def __invert__(self):
        return Bits(~self.__int)

    def __index__(self):
        return self.__int

    def __lshift__(self, other):
        if not isinstance(other, int):
            raise NotImplemented
        return Bits(self.__int << other)

    def __rshift__(self, other):
        if not isinstance(other, int):
            raise NotImplemented
        return Bits(self.__int >> other)

    def __add__(self, other):
        if not isinstance(other, Bits):
            raise NotImplemented
        return Bits(self | (other << (len(bytes(self)) * 8)))

    def __int__(self):
        return self.__int

    def __str__(self):
        return str(self.__int)

    def __bytes__(self):
        length = int(math.ceil(self.__int.bit_length()/8))
        return self.__int.to_bytes(length, self.__byteorder, signed=True)

    def __repr__(self):
        return 'Bits({}, byteorder=\'{}\', strbase={})'.format(int(self),
                                                               self.__byteorder,
                                                               self.__strbase)
