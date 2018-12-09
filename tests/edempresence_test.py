import os
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

    def test_filename_has_twenty_and_three_digits(self):

        file_name = self.edem.filename()

        file_name_size = len(file_name)

        self.assertEqual(file_name_size, 23) 

    def test_if_filename_exists(self):

        file_name = self.edem.filename()

        self.edem.create_file(file_name)

        result = self.edem.filename_exists(file_name)

        os.remove(file_name)

        self.assertTrue(result)

    def test_strip_date_from_file_name(self):

        file_name = '/home/example/test/1544393376-20181209.txt'

        result = self.edem.strip_date_from_filename(file_name)

        self.assertEqual(result, '20181209')


