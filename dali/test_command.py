from . import command,address
import unittest

class TestCommands(unittest.TestCase):
    def test_roundtrip(self):
        "all two-byte sequences (a,b) survive command.from_bytes()"
        for a in xrange(0,256):
            for b in xrange(0,256):
                ts=(a,b)
                self.assertEqual(ts,command.from_bytes(ts).command)

    def test_unicode(self):
        "command objects return unicode from their __unicode__ method"
        for a in xrange(0,256):
            for b in xrange(0,256):
                ts=(a,b)
                self.assertTrue(
                    isinstance(command.from_bytes(ts).__unicode__(),unicode))

    def test_bad_command(self):
        "command.from_bytes() rejects invalid inputs"
        self.assertRaises(TypeError,command.from_bytes,1)
        self.assertRaises(ValueError,command.from_bytes,"test")
        self.assertRaises(ValueError,command.from_bytes,(256,0))
        self.assertRaises(ValueError,command.from_bytes,(0,256))
        self.assertRaises(ValueError,command.from_bytes,(-1,0))
        self.assertRaises(ValueError,command.from_bytes,(0,-1))

    def test_with_integer_destination(self):
        "commands accept integer destination"
        self.assertEqual(command.ArcPower(5,100).destination,address.Short(5))
        self.assertEqual(command.Off(5).destination,address.Short(5))
        self.assertRaises(ValueError,command.Off,-1)
        self.assertRaises(ValueError,command.Off,64)
        self.assertRaises(ValueError,command.Off,None)

if __name__=="__main__":
    unittest.main()
