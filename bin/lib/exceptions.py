"""
This includes all exceptions defined for technology addon.
"""

from http.client import HTTPException


class ConnectivityException(Exception):
    """
    Exception raised for errors in the ping modular input.
    """


class ConnectivityExceptionFileNotFound(ConnectivityException):
    """
    Raised if the lookup file defined in the input is not found
    """

    def __init__(self, message):
        self.file = message
        ConnectivityException.__init__(self, 'Lookup file, %s , does not exist' % message)


class ConnectivityExceptionFieldNotFound(ConnectivityException):
    """
    Raised if the field specified for modular input is not found in the CSV header
    """

    def __init__(self, message):
        self.field = message
        ConnectivityException.__init__(self, 'Field, %s, does not match values in header' % message)


class ConnectivityPortValueError(ConnectivityException):
    """
    Raised if the field specified for modular input is not found in the CSV header
    """

    def __init__(self, message):
        self.port = message
        ConnectivityException.__init__(self, "Could not find your port: %s" % message)


class ConnectivitySocketCreation(ConnectivityException):
    """
    Raised if the field specified for modular input is not found in the CSV header
    """

    def __init__(self):
        ConnectivityException.__init__(self, "Network error - Problem creating socket")


class ConnectivityNameResolution(ConnectivityException):
    """
    Raised if the field specified for modular input is not found in the CSV header
    """

    def __init__(self, ip):
        ConnectivityException.__init__(self, "Problem resolving address: %s" % ip)


class ConnectivityNetworkError(ConnectivityException):
    """
    Raised if the field specified for modular input is not found in the CSV header
    """

    def __init__(self, message):
        ConnectivityException.__init__(self, "Connection error: %s" % message)


class ConnectivityParameterError(ConnectivityException):
    """
    Raised if the field specified for modular input is not found in the CSV header
    """

    def __init__(self, message):
        ConnectivityException.__init__(self, "Parameter Error" % message)
