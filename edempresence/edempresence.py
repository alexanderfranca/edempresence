import time
import glob
from datetime import datetime
import os

class EdemPresence:
    """
    Deals with the whole student ID recording.
    """

    def __init__(self, card, external_file=None):
        self.enrollment = card.enrollment
        self.external_file = external_file

    def timestamp(self):
        """
        Return the timestamp in a integer format.

        Returns:
            (int): timestamp
        """

        return int(time.time())

    def check_enrollment_is_number(self):
        """
        Check if student enrollment ID is an integer number.

        Returns:
            (bol): True or False.
        """

        result = False

        if type(self.enrollment) is int:
            result = True

        return result

    def filename(self):
        """
        Generates a file name that will be used to store students presence for the day.

        Example: 1544391469-20081206.txt

        Returns:
            (str): file name. Format should be $timestamp-$year$month$day.txt.
        """

        timestamp = self.timestamp()
        day = datetime.fromtimestamp(timestamp).strftime("%d")
        month = datetime.fromtimestamp(timestamp).strftime("%m")
        year = datetime.fromtimestamp(timestamp).strftime("%Y")

        filename = str(timestamp) + '-' + str(year) + str(month) + str(day) + '.txt'

        return filename

    def create_file(self, file_name):
        """
        Create an empty file that'll store the students presence.

        Args:
            file_name(str): Full path for the file to be created.
        """

        open(file_name, 'a').close()

    def filename_exists(self, file_name):
        """
        Check if the file name for storing students presence already exists.

        Returns:
            (bol): True or False.
        """

        result = False

        if os.path.exists(file_name):
            result = True

        return result

    def strip_date_from_filename(self, file_name):
        """
        Returns only the date from the full path filename.

        Typical filenam have a full path and timestamp in its name.

        Returns:
            (str): the date from the full path filename. Example: '20180512' from something like '2342434423-20180512.txt'.
        """

        basename = os.path.basename(file_name)
        dirname = os.path.dirname(file_name)

        date_and_format = basename.split('-')
        date = date_and_format[1].split('.')

        return date[0]

    def date_file_exists(self, file_name):
        """
        Check if the file that has its date part in its name exists.

        Args:
            file_name(str): full file name path.

        Returns:
            (str): found file name. 
        """

        date = self.strip_date_from_filename(file_name)
        date = str(date) + '.txt'

        files = glob.glob('*' + date)

        result = None

        if len(files) > 0:
            result = files[0]

        return result

    def record_presence(self):
        """
        Record the student enrollment and timestamp to the destination record file.
        """

        result = {}

        filename = self.filename()

        date_file_name = self.strip_date_from_filename(filename)

        found_file = self.date_file_exists(filename)

        if not found_file:
            self.create_file(filename)
            found_file = filename

        with open(found_file, 'a') as record:
            timestamp = self.timestamp()
            record.write(str(self.enrollment) + ':' + str(timestamp) + "\n")
            result = { 'enrollment': self.enrollment, 'timestamp': timestamp, 'file': filename }

        return result

    def generate_full_presence_record(self):
        """
        Generate a full data structure containing all the data (for students presence) required by third part software.

        Returns:
            (dict): student presence data (enrollment, day, year, action etc).

        """

        timestamp = self.timestamp()
        day = datetime.fromtimestamp(timestamp).strftime("%d")
        month = datetime.fromtimestamp(timestamp).strftime("%m")
        year = datetime.fromtimestamp(timestamp).strftime("%Y")
        hour = datetime.fromtimestamp(timestamp).strftime("%H")
        minute = datetime.fromtimestamp(timestamp).strftime("%M")
        second = datetime.fromtimestamp(timestamp).strftime("%s")

        presence_data = { 'act': '01', 'day': day, 'month': month, 'year': year, 'hour': hour, 'minute': minute, 'second': second, 'enrollment': self.enrollment }

        return presence_data

    def write_external_presence_data(self, data):

        with open(self.external_file.filepath, 'a') as external_file:
            external_file.write(str(data['act']) + ',' + str(data['day']) + "," + str(data['month']) + "," + str(data['year']) + "," + str(data['hour']) + "," + str(data['minute']) + "," + str(data['second']) + "," + str(data['enrollment']) + "\n")


        with open(self.external_file.filepath) as external_file:
            lines = external_file.readlines()

        return lines[-1]


