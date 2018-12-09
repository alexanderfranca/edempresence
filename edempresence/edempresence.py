import time
from datetime import datetime

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
