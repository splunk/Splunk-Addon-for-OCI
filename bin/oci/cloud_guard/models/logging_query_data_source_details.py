# coding: utf-8
# Copyright (c) 2016, 2023, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.

from .data_source_details import DataSourceDetails
from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class LoggingQueryDataSourceDetails(DataSourceDetails):
    """
    The information about new Logging Query of type DataSource.
    """

    #: A constant which can be used with the operator property of a LoggingQueryDataSourceDetails.
    #: This constant has a value of "EQUAL"
    OPERATOR_EQUAL = "EQUAL"

    #: A constant which can be used with the operator property of a LoggingQueryDataSourceDetails.
    #: This constant has a value of "GREATER"
    OPERATOR_GREATER = "GREATER"

    #: A constant which can be used with the operator property of a LoggingQueryDataSourceDetails.
    #: This constant has a value of "GREATERTHANEQUALTO"
    OPERATOR_GREATERTHANEQUALTO = "GREATERTHANEQUALTO"

    #: A constant which can be used with the operator property of a LoggingQueryDataSourceDetails.
    #: This constant has a value of "LESS"
    OPERATOR_LESS = "LESS"

    #: A constant which can be used with the operator property of a LoggingQueryDataSourceDetails.
    #: This constant has a value of "LESSTHANEQUALTO"
    OPERATOR_LESSTHANEQUALTO = "LESSTHANEQUALTO"

    #: A constant which can be used with the logging_query_type property of a LoggingQueryDataSourceDetails.
    #: This constant has a value of "INSIGHT"
    LOGGING_QUERY_TYPE_INSIGHT = "INSIGHT"

    def __init__(self, **kwargs):
        """
        Initializes a new LoggingQueryDataSourceDetails object with values from keyword arguments. The default value of the :py:attr:`~oci.cloud_guard.models.LoggingQueryDataSourceDetails.data_source_feed_provider` attribute
        of this class is ``LOGGINGQUERY`` and it should not be changed.
        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param data_source_feed_provider:
            The value to assign to the data_source_feed_provider property of this LoggingQueryDataSourceDetails.
            Allowed values for this property are: "LOGGINGQUERY", 'UNKNOWN_ENUM_VALUE'.
            Any unrecognized values returned by a service will be mapped to 'UNKNOWN_ENUM_VALUE'.
        :type data_source_feed_provider: str

        :param regions:
            The value to assign to the regions property of this LoggingQueryDataSourceDetails.
        :type regions: list[str]

        :param query:
            The value to assign to the query property of this LoggingQueryDataSourceDetails.
        :type query: str

        :param interval_in_minutes:
            The value to assign to the interval_in_minutes property of this LoggingQueryDataSourceDetails.
        :type interval_in_minutes: int

        :param threshold:
            The value to assign to the threshold property of this LoggingQueryDataSourceDetails.
        :type threshold: int

        :param query_start_time:
            The value to assign to the query_start_time property of this LoggingQueryDataSourceDetails.
        :type query_start_time: oci.cloud_guard.models.ContinuousQueryStartPolicy

        :param operator:
            The value to assign to the operator property of this LoggingQueryDataSourceDetails.
            Allowed values for this property are: "EQUAL", "GREATER", "GREATERTHANEQUALTO", "LESS", "LESSTHANEQUALTO", 'UNKNOWN_ENUM_VALUE'.
            Any unrecognized values returned by a service will be mapped to 'UNKNOWN_ENUM_VALUE'.
        :type operator: str

        :param logging_query_type:
            The value to assign to the logging_query_type property of this LoggingQueryDataSourceDetails.
            Allowed values for this property are: "INSIGHT", 'UNKNOWN_ENUM_VALUE'.
            Any unrecognized values returned by a service will be mapped to 'UNKNOWN_ENUM_VALUE'.
        :type logging_query_type: str

        :param additional_entities_count:
            The value to assign to the additional_entities_count property of this LoggingQueryDataSourceDetails.
        :type additional_entities_count: int

        :param logging_query_details:
            The value to assign to the logging_query_details property of this LoggingQueryDataSourceDetails.
        :type logging_query_details: oci.cloud_guard.models.LoggingQueryDetails

        """
        self.swagger_types = {
            'data_source_feed_provider': 'str',
            'regions': 'list[str]',
            'query': 'str',
            'interval_in_minutes': 'int',
            'threshold': 'int',
            'query_start_time': 'ContinuousQueryStartPolicy',
            'operator': 'str',
            'logging_query_type': 'str',
            'additional_entities_count': 'int',
            'logging_query_details': 'LoggingQueryDetails'
        }

        self.attribute_map = {
            'data_source_feed_provider': 'dataSourceFeedProvider',
            'regions': 'regions',
            'query': 'query',
            'interval_in_minutes': 'intervalInMinutes',
            'threshold': 'threshold',
            'query_start_time': 'queryStartTime',
            'operator': 'operator',
            'logging_query_type': 'loggingQueryType',
            'additional_entities_count': 'additionalEntitiesCount',
            'logging_query_details': 'loggingQueryDetails'
        }

        self._data_source_feed_provider = None
        self._regions = None
        self._query = None
        self._interval_in_minutes = None
        self._threshold = None
        self._query_start_time = None
        self._operator = None
        self._logging_query_type = None
        self._additional_entities_count = None
        self._logging_query_details = None
        self._data_source_feed_provider = 'LOGGINGQUERY'

    @property
    def regions(self):
        """
        Gets the regions of this LoggingQueryDataSourceDetails.
        Logging Query regions


        :return: The regions of this LoggingQueryDataSourceDetails.
        :rtype: list[str]
        """
        return self._regions

    @regions.setter
    def regions(self, regions):
        """
        Sets the regions of this LoggingQueryDataSourceDetails.
        Logging Query regions


        :param regions: The regions of this LoggingQueryDataSourceDetails.
        :type: list[str]
        """
        self._regions = regions

    @property
    def query(self):
        """
        Gets the query of this LoggingQueryDataSourceDetails.
        The continuous query expression that is run periodically.


        :return: The query of this LoggingQueryDataSourceDetails.
        :rtype: str
        """
        return self._query

    @query.setter
    def query(self, query):
        """
        Sets the query of this LoggingQueryDataSourceDetails.
        The continuous query expression that is run periodically.


        :param query: The query of this LoggingQueryDataSourceDetails.
        :type: str
        """
        self._query = query

    @property
    def interval_in_minutes(self):
        """
        Gets the interval_in_minutes of this LoggingQueryDataSourceDetails.
        Interval in minutes that query is run periodically.


        :return: The interval_in_minutes of this LoggingQueryDataSourceDetails.
        :rtype: int
        """
        return self._interval_in_minutes

    @interval_in_minutes.setter
    def interval_in_minutes(self, interval_in_minutes):
        """
        Sets the interval_in_minutes of this LoggingQueryDataSourceDetails.
        Interval in minutes that query is run periodically.


        :param interval_in_minutes: The interval_in_minutes of this LoggingQueryDataSourceDetails.
        :type: int
        """
        self._interval_in_minutes = interval_in_minutes

    @property
    def threshold(self):
        """
        Gets the threshold of this LoggingQueryDataSourceDetails.
        The integer value that must be exceeded, fall below or equal to (depending on the operator), the query result to trigger an event.


        :return: The threshold of this LoggingQueryDataSourceDetails.
        :rtype: int
        """
        return self._threshold

    @threshold.setter
    def threshold(self, threshold):
        """
        Sets the threshold of this LoggingQueryDataSourceDetails.
        The integer value that must be exceeded, fall below or equal to (depending on the operator), the query result to trigger an event.


        :param threshold: The threshold of this LoggingQueryDataSourceDetails.
        :type: int
        """
        self._threshold = threshold

    @property
    def query_start_time(self):
        """
        Gets the query_start_time of this LoggingQueryDataSourceDetails.

        :return: The query_start_time of this LoggingQueryDataSourceDetails.
        :rtype: oci.cloud_guard.models.ContinuousQueryStartPolicy
        """
        return self._query_start_time

    @query_start_time.setter
    def query_start_time(self, query_start_time):
        """
        Sets the query_start_time of this LoggingQueryDataSourceDetails.

        :param query_start_time: The query_start_time of this LoggingQueryDataSourceDetails.
        :type: oci.cloud_guard.models.ContinuousQueryStartPolicy
        """
        self._query_start_time = query_start_time

    @property
    def operator(self):
        """
        Gets the operator of this LoggingQueryDataSourceDetails.
        Operator used in Data Soruce

        Allowed values for this property are: "EQUAL", "GREATER", "GREATERTHANEQUALTO", "LESS", "LESSTHANEQUALTO", 'UNKNOWN_ENUM_VALUE'.
        Any unrecognized values returned by a service will be mapped to 'UNKNOWN_ENUM_VALUE'.


        :return: The operator of this LoggingQueryDataSourceDetails.
        :rtype: str
        """
        return self._operator

    @operator.setter
    def operator(self, operator):
        """
        Sets the operator of this LoggingQueryDataSourceDetails.
        Operator used in Data Soruce


        :param operator: The operator of this LoggingQueryDataSourceDetails.
        :type: str
        """
        allowed_values = ["EQUAL", "GREATER", "GREATERTHANEQUALTO", "LESS", "LESSTHANEQUALTO"]
        if not value_allowed_none_or_none_sentinel(operator, allowed_values):
            operator = 'UNKNOWN_ENUM_VALUE'
        self._operator = operator

    @property
    def logging_query_type(self):
        """
        Gets the logging_query_type of this LoggingQueryDataSourceDetails.
        Logging query type for data source (Sighting/Insight)

        Allowed values for this property are: "INSIGHT", 'UNKNOWN_ENUM_VALUE'.
        Any unrecognized values returned by a service will be mapped to 'UNKNOWN_ENUM_VALUE'.


        :return: The logging_query_type of this LoggingQueryDataSourceDetails.
        :rtype: str
        """
        return self._logging_query_type

    @logging_query_type.setter
    def logging_query_type(self, logging_query_type):
        """
        Sets the logging_query_type of this LoggingQueryDataSourceDetails.
        Logging query type for data source (Sighting/Insight)


        :param logging_query_type: The logging_query_type of this LoggingQueryDataSourceDetails.
        :type: str
        """
        allowed_values = ["INSIGHT"]
        if not value_allowed_none_or_none_sentinel(logging_query_type, allowed_values):
            logging_query_type = 'UNKNOWN_ENUM_VALUE'
        self._logging_query_type = logging_query_type

    @property
    def additional_entities_count(self):
        """
        Gets the additional_entities_count of this LoggingQueryDataSourceDetails.
        The additional entities count used for data source query.


        :return: The additional_entities_count of this LoggingQueryDataSourceDetails.
        :rtype: int
        """
        return self._additional_entities_count

    @additional_entities_count.setter
    def additional_entities_count(self, additional_entities_count):
        """
        Sets the additional_entities_count of this LoggingQueryDataSourceDetails.
        The additional entities count used for data source query.


        :param additional_entities_count: The additional_entities_count of this LoggingQueryDataSourceDetails.
        :type: int
        """
        self._additional_entities_count = additional_entities_count

    @property
    def logging_query_details(self):
        """
        Gets the logging_query_details of this LoggingQueryDataSourceDetails.

        :return: The logging_query_details of this LoggingQueryDataSourceDetails.
        :rtype: oci.cloud_guard.models.LoggingQueryDetails
        """
        return self._logging_query_details

    @logging_query_details.setter
    def logging_query_details(self, logging_query_details):
        """
        Sets the logging_query_details of this LoggingQueryDataSourceDetails.

        :param logging_query_details: The logging_query_details of this LoggingQueryDataSourceDetails.
        :type: oci.cloud_guard.models.LoggingQueryDetails
        """
        self._logging_query_details = logging_query_details

    def __repr__(self):
        return formatted_flat_dict(self)

    def __eq__(self, other):
        if other is None:
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not self == other
