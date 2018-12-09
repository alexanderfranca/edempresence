import time

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

