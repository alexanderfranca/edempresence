import unittest
from edempresence.edempresence import EdemPresence
from edempresence.edemcard import EdemCard

class test_edempresence(unittest.TestCase):

    def setUp(self):

        card = EdemCard(enrollment='0004324')
        self.edem = EdemPresence(card)

    def test_check_timestamp_is_int(self):

        timestamp = self.edem.timestamp()

        self.assertTrue(type(timestamp) is int)

    def test_if_enrollment_number_is_integer(self):

        self.data1 = EdemCard(enrollment=4345)

        enrollment = self.data1.enrollment

        self.assertTrue(type(enrollment) is int)

    def test_if_enrollment_number_is_not_integer(self):

        self.data1 = EdemCard(enrollment='not_a_number')

        enrollment = self.data1.enrollment

        self.assertFalse(type(enrollment) is int)
