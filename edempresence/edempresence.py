import time
from datetime import datetime
import os

class EdemPresence:
    """
    Deals with the whole student ID recording.
    """

    def __init__(self, card):
        self.enrollment = card.enrollment

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

        basename = os.path.basename(file_name)
        dirname = os.path.dirname(file_name)

        date_and_format = basename.split('-')
        date = date_and_format[1].split('.')

        return date[0]
