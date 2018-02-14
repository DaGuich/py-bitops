import unittest
from bitops import Bits


class TestBits(unittest.TestCase):
    def test_construct(self):
        self.assertEqual(Bits(12), Bits('12'))
        self.assertEqual(Bits(12), Bits('C', strbase=16))
        self.assertEqual(Bits(12), Bits(b'\x0C', 'big'))
        self.assertEqual(Bits(256), Bits(b'\x01\x00', 'big'))
        self.assertEqual(Bits(256), Bits(b'\x00\x01', 'little'))
        self.assertEqual(Bits(256), Bits(Bits(256)))

        with self.assertRaises(TypeError):
            x = Bits(12.5)

        with self.assertRaises(TypeError):
            x = Bits(8, byteorder=5)

        with self.assertRaises(ValueError):
            x = Bits(8, byteorder='failure')

        with self.assertRaises(TypeError):
            x = Bits(9, strbase='failure')

    def test_int(self):
        o = Bits(5)
        self.assertEqual(int(o), 5)

    def test_str(self):
        o = Bits(5)
        self.assertEqual(str(o), '5')

    def test_bytes(self):
        o = Bits(5)
        self.assertEqual(bytes(o), b'\x05')

    def test_hex(self):
        o = Bits(5)
        self.assertEqual(hex(o), '0x5')

    def test_concat(self):
        a = Bits(b'\x0a')
        b = Bits(b'\x09')
        self.assertEqual(Bits(b'\x0a\x09'), a + b)
        self.assertEqual(Bits(b'\x09\x0a'), b + a)

        c = Bits(b'\x12\x34')
        self.assertEqual(Bits(b'\x0a\x12\x34'), a + c)
        self.assertEqual(Bits(b'\x12\x34\x0a'), c + a)

    def test_unary(self):
        a = Bits(7)
        b = Bits(3)

        self.assertEqual(Bits(3), a & b)
        self.assertEqual(Bits(7), a | b)
        self.assertEqual(Bits(4), a ^ b)

    def test_invert(self):
        self.assertEqual(Bits(b'\x00'), ~Bits(b'\xFF'))
        self.assertEqual(Bits(b'\x0F'), ~Bits(b'\xF0'))
        self.assertEqual(Bits(b'\x00\xFF'), ~Bits(b'\xFF\x00'))
        self.assertEqual(Bits(b'\xAA'), ~Bits(b'\x55'))

    def test_repr(self):
        o = Bits(3)
        r = 'Bits(3, byteorder=\'little\', strbase=10)'
        self.assertEqual(r, repr(o))

        o.byteorder = 'big'
        r = 'Bits(3, byteorder=\'big\', strbase=10)'
        self.assertEqual(r, repr(o))

        o.strbase = 2
        r = 'Bits(3, byteorder=\'big\', strbase=2)'
        self.assertEqual(r, repr(o))

    def test_properties(self):
        o = Bits(3)

        with self.assertRaises(TypeError):
            o.strbase = 'abc'

        with self.assertRaises(TypeError):
            o.byteorder = 4

        o.byteorder = 'little'
        self.assertEqual(o.byteorder, 'little')

        o.strbase = 16
        self.assertEqual(o.strbase, 16)

    def test_eq_ne(self):
        self.assertTrue(Bits(2) == Bits(2))
        self.assertTrue(Bits(2) != Bits(3))
        self.assertFalse(Bits(2) == Bits(3))
        self.assertFalse(Bits(2) != Bits(2))

    def test_shift(self):
        o = Bits(2)

        self.assertEqual(Bits(4), o << 1)
        self.assertEqual(Bits(1), o >> 1)

    def test_not_implemented(self):
        o = Bits(12)

        with self.assertRaises(TypeError):
            o & 4

        with self.assertRaises(TypeError):
            o ^ 4

        with self.assertRaises(TypeError):
            o | 4

        with self.assertRaises(TypeError):
            o == 4

        with self.assertRaises(TypeError):
            o != 4

        with self.assertRaises(TypeError):
            o << 'a'

        with self.assertRaises(TypeError):
            o >> 'a'

        with self.assertRaises(TypeError):
            o + 5

