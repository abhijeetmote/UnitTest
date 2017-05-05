# =============================================================================
# $Id: Exp $
# =============================================================================
# Module: package.sub_package
# =============================================================================


# =============================================================================
# IMPORTS
# =============================================================================

# Standard imports
import time
import datetime
import calendar
import pdb

class Date(object):
    """Date representing the additional date utils.

    Example:

        >>> from Date import Date
        >>> Date_obj = Date("20150807211315")
        >>> Date_obj.get_epoch()
        1438981995
    """
    def __init__(self, date_time_str, dt_frmt="%Y%m%d%H%M%S"):
        import pdb 
        pdb.set_trace()
        self.date_time = datetime.datetime.strptime(date_time_str,dt_frmt)
        self.date_format = dt_frmt
        self._set_properties()

    def _set_properties(self):
        """ This function handles setting of properties for Date class and
        this function is not part of API.

        Args: self :- Date class object
        Raises: N/A
        returns: None
        """
        self.epoch = calendar.timegm(self.date_time.timetuple())
        self.year = self.date_time.year
        self.month = self.date_time.month
        self.day = self.date_time.strftime("%A")
        self.time_str = self.date_time.strftime("%H:%M:%S")
        self.date_yyyymmdd = self.date_time.strftime("%Y%m%d")

    def set_date_time(self, date_time_str, dt_frmt="%Y%m%d%H%M%S"):
        """This function sets date_time attribute of Date class
        which affects the other properties of Date class.

        Args: date_time_str :- String representing date time
              dt_frmt :- String representing format of date time
        Raises: N/A
        returns: None
        """
        self.date_time = datetime.datetime.strptime(date_time_str,dt_frmt)
        self._set_properties()

    def set_epoch(self, epoch_time):
        """This function sets date_time attribute of Date class
        which affects the other properties of Date class.

        Args:  epoch_time:- String or Int representing epoch time
        Raises: N/A
        returns: None
        """
        self.date_time = datetime.datetime.fromtimestamp(int(epoch_time))
        self._set_properties()

    def get_epoch(self):
        """This function returns epoch time.

        Args:  None
        Raises: N/A
        returns: Epoch time (Integer)
        """
        return self.epoch

    def get_date_format(self):
        """This function returns epoch time.

        Args:  None
        Raises: N/A
        returns: date format (String)"""
        return self.date_format

    def get_year(self):
        """This function returns year.

        Args:  None
        Raises: N/A
        returns: year (Integer)"""
        return self.year

    def get_month(self):
        """This function returns month.

        Args:  None
        Raises: N/A
        returns: Month (Integer)"""
        return self.month

    def get_day(self):
        """This function returns day.

        Args:  None
        Raises: N/A
        returns: Day (String) e.g Wednesday"""
        return self.day

    def get_time_str(self):
        """This function returns time in string.
        Args:  None
        Raises: N/A
        returns: time (String) e.g '11:03:18' """
        return self.time_str

    def get_date_yyyymmdd(self):
        """This function returns date in string.
        Args:  None
        Raises: N/A
        returns: date (String) e.g '20150827' """
        return self.date_yyyymmdd


if __name__ == '__main__':
    Date_obj = Date("20150807211315")
    print Date_obj.get_epoch()
