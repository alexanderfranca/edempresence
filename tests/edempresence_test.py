import os
import unittest
from edempresence.edempresence import EdemPresence
from edempresence.edemcard import EdemCard
from edempresence.edemexternalfile import EdemExternalFile

class test_edempresence(unittest.TestCase):

    def setUp(self):

        card = EdemCard(enrollment=4324)
        external_file = EdemExternalFile(filepath='./record.txt')

        self.edem = EdemPresence(card=card, external_file=external_file)

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

    def test_check_if_date_file_exists(self):

        file_name = './1544393376-20181209.txt'

        self.edem.create_file(file_name)

        result = self.edem.date_file_exists(file_name)

        os.remove(file_name)

        self.assertTrue(type(result) is str)

    def test_record_presence(self):

        result = self.edem.record_presence()

        self.assertTrue('file' in result.keys())

        os.remove(result['file'])

    def test_generate_full_presence_record_has_enrollment(self):

        data = self.edem.generate_full_presence_record()

        self.assertTrue('enrollment' in data.keys())

    def test_generate_full_presence_record_write_data_into_file(self):

        data = self.edem.generate_full_presence_record()

        last_line = self.edem.write_external_presence_data(data)

        os.remove(self.edem.external_file.filepath)

        self.assertTrue(type(last_line) is str)

