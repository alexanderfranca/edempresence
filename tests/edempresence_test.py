import unittest
from edempresence.edempresence import EdemPresence
from edempresence.edemcard import EdemCard

class test_edempresence(unittest.TestCase):

    def setUp(self):

        card = EdemCard(enrollment=4324)
        self.edem = EdemPresence(card)

    def test_check_timestamp_is_int(self):

        timestamp = self.edem.timestamp()

        self.assertTrue(type(timestamp) is int)

    def test_if_enrollment_number_is_integer(self):

        enrollment = self.edem.enrollment

        self.assertTrue(type(enrollment) is int)

    def test_method_if_enrollment_number_is_integer(self):

        result = self.edem.check_enrollment_is_number()

        self.assertTrue(result)
