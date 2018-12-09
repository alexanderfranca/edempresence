import unittest
from edempresence.edempresence import EdemPresence

class test_edempresence(unittest.TestCase):

    def setUp(self):

        self.edem = EdemPresence()


    def test_check_timestamp_is_int(self):

        timestamp = self.edem.timestamp()

        self.assertEqual(type(timestamp) is int)
