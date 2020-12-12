class Error(Exception):
    """
    Base class for errors
    """
    pass


class TooLittleMoneyError(Error):
    """
    Error to be raised when money's insufficient
    """
    pass