# coding: utf-8
# Copyright (c) 2016, 2023, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.


from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class ReportQuery(object):
    """
    The request of the generated Cost Analysis report.
    """

    #: A constant which can be used with the granularity property of a ReportQuery.
    #: This constant has a value of "HOURLY"
    GRANULARITY_HOURLY = "HOURLY"

    #: A constant which can be used with the granularity property of a ReportQuery.
    #: This constant has a value of "DAILY"
    GRANULARITY_DAILY = "DAILY"

    #: A constant which can be used with the granularity property of a ReportQuery.
    #: This constant has a value of "MONTHLY"
    GRANULARITY_MONTHLY = "MONTHLY"

    #: A constant which can be used with the granularity property of a ReportQuery.
    #: This constant has a value of "TOTAL"
    GRANULARITY_TOTAL = "TOTAL"

    #: A constant which can be used with the query_type property of a ReportQuery.
    #: This constant has a value of "USAGE"
    QUERY_TYPE_USAGE = "USAGE"

    #: A constant which can be used with the query_type property of a ReportQuery.
    #: This constant has a value of "COST"
    QUERY_TYPE_COST = "COST"

    #: A constant which can be used with the query_type property of a ReportQuery.
    #: This constant has a value of "CREDIT"
    QUERY_TYPE_CREDIT = "CREDIT"

    #: A constant which can be used with the query_type property of a ReportQuery.
    #: This constant has a value of "EXPIREDCREDIT"
    QUERY_TYPE_EXPIREDCREDIT = "EXPIREDCREDIT"

    #: A constant which can be used with the query_type property of a ReportQuery.
    #: This constant has a value of "ALLCREDIT"
    QUERY_TYPE_ALLCREDIT = "ALLCREDIT"

    #: A constant which can be used with the date_range_name property of a ReportQuery.
    #: This constant has a value of "LAST_SEVEN_DAYS"
    DATE_RANGE_NAME_LAST_SEVEN_DAYS = "LAST_SEVEN_DAYS"

    #: A constant which can be used with the date_range_name property of a ReportQuery.
    #: This constant has a value of "LAST_TEN_DAYS"
    DATE_RANGE_NAME_LAST_TEN_DAYS = "LAST_TEN_DAYS"

    #: A constant which can be used with the date_range_name property of a ReportQuery.
    #: This constant has a value of "MTD"
    DATE_RANGE_NAME_MTD = "MTD"

    #: A constant which can be used with the date_range_name property of a ReportQuery.
    #: This constant has a value of "LAST_TWO_MONTHS"
    DATE_RANGE_NAME_LAST_TWO_MONTHS = "LAST_TWO_MONTHS"

    #: A constant which can be used with the date_range_name property of a ReportQuery.
    #: This constant has a value of "LAST_THREE_MONTHS"
    DATE_RANGE_NAME_LAST_THREE_MONTHS = "LAST_THREE_MONTHS"

    #: A constant which can be used with the date_range_name property of a ReportQuery.
    #: This constant has a value of "ALL"
    DATE_RANGE_NAME_ALL = "ALL"

    #: A constant which can be used with the date_range_name property of a ReportQuery.
    #: This constant has a value of "LAST_SIX_MONTHS"
    DATE_RANGE_NAME_LAST_SIX_MONTHS = "LAST_SIX_MONTHS"

    #: A constant which can be used with the date_range_name property of a ReportQuery.
    #: This constant has a value of "LAST_ONE_YEAR"
    DATE_RANGE_NAME_LAST_ONE_YEAR = "LAST_ONE_YEAR"

    #: A constant which can be used with the date_range_name property of a ReportQuery.
    #: This constant has a value of "YTD"
    DATE_RANGE_NAME_YTD = "YTD"

    #: A constant which can be used with the date_range_name property of a ReportQuery.
    #: This constant has a value of "CUSTOM"
    DATE_RANGE_NAME_CUSTOM = "CUSTOM"

    def __init__(self, **kwargs):
        """
        Initializes a new ReportQuery object with values from keyword arguments.
        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param tenant_id:
            The value to assign to the tenant_id property of this ReportQuery.
        :type tenant_id: str

        :param time_usage_started:
            The value to assign to the time_usage_started property of this ReportQuery.
        :type time_usage_started: datetime

        :param time_usage_ended:
            The value to assign to the time_usage_ended property of this ReportQuery.
        :type time_usage_ended: datetime

        :param granularity:
            The value to assign to the granularity property of this ReportQuery.
            Allowed values for this property are: "HOURLY", "DAILY", "MONTHLY", "TOTAL", 'UNKNOWN_ENUM_VALUE'.
            Any unrecognized values returned by a service will be mapped to 'UNKNOWN_ENUM_VALUE'.
        :type granularity: str

        :param is_aggregate_by_time:
            The value to assign to the is_aggregate_by_time property of this ReportQuery.
        :type is_aggregate_by_time: bool

        :param forecast:
            The value to assign to the forecast property of this ReportQuery.
        :type forecast: oci.usage_api.models.Forecast

        :param query_type:
            The value to assign to the query_type property of this ReportQuery.
            Allowed values for this property are: "USAGE", "COST", "CREDIT", "EXPIREDCREDIT", "ALLCREDIT", 'UNKNOWN_ENUM_VALUE'.
            Any unrecognized values returned by a service will be mapped to 'UNKNOWN_ENUM_VALUE'.
        :type query_type: str

        :param group_by:
            The value to assign to the group_by property of this ReportQuery.
        :type group_by: list[str]

        :param group_by_tag:
            The value to assign to the group_by_tag property of this ReportQuery.
        :type group_by_tag: list[oci.usage_api.models.Tag]

        :param compartment_depth:
            The value to assign to the compartment_depth property of this ReportQuery.
        :type compartment_depth: float

        :param filter:
            The value to assign to the filter property of this ReportQuery.
        :type filter: oci.usage_api.models.Filter

        :param date_range_name:
            The value to assign to the date_range_name property of this ReportQuery.
            Allowed values for this property are: "LAST_SEVEN_DAYS", "LAST_TEN_DAYS", "MTD", "LAST_TWO_MONTHS", "LAST_THREE_MONTHS", "ALL", "LAST_SIX_MONTHS", "LAST_ONE_YEAR", "YTD", "CUSTOM", 'UNKNOWN_ENUM_VALUE'.
            Any unrecognized values returned by a service will be mapped to 'UNKNOWN_ENUM_VALUE'.
        :type date_range_name: str

        """
        self.swagger_types = {
            'tenant_id': 'str',
            'time_usage_started': 'datetime',
            'time_usage_ended': 'datetime',
            'granularity': 'str',
            'is_aggregate_by_time': 'bool',
            'forecast': 'Forecast',
            'query_type': 'str',
            'group_by': 'list[str]',
            'group_by_tag': 'list[Tag]',
            'compartment_depth': 'float',
            'filter': 'Filter',
            'date_range_name': 'str'
        }

        self.attribute_map = {
            'tenant_id': 'tenantId',
            'time_usage_started': 'timeUsageStarted',
            'time_usage_ended': 'timeUsageEnded',
            'granularity': 'granularity',
            'is_aggregate_by_time': 'isAggregateByTime',
            'forecast': 'forecast',
            'query_type': 'queryType',
            'group_by': 'groupBy',
            'group_by_tag': 'groupByTag',
            'compartment_depth': 'compartmentDepth',
            'filter': 'filter',
            'date_range_name': 'dateRangeName'
        }

        self._tenant_id = None
        self._time_usage_started = None
        self._time_usage_ended = None
        self._granularity = None
        self._is_aggregate_by_time = None
        self._forecast = None
        self._query_type = None
        self._group_by = None
        self._group_by_tag = None
        self._compartment_depth = None
        self._filter = None
        self._date_range_name = None

    @property
    def tenant_id(self):
        """
        **[Required]** Gets the tenant_id of this ReportQuery.
        Tenant ID.


        :return: The tenant_id of this ReportQuery.
        :rtype: str
        """
        return self._tenant_id

    @tenant_id.setter
    def tenant_id(self, tenant_id):
        """
        Sets the tenant_id of this ReportQuery.
        Tenant ID.


        :param tenant_id: The tenant_id of this ReportQuery.
        :type: str
        """
        self._tenant_id = tenant_id

    @property
    def time_usage_started(self):
        """
        Gets the time_usage_started of this ReportQuery.
        The usage start time.


        :return: The time_usage_started of this ReportQuery.
        :rtype: datetime
        """
        return self._time_usage_started

    @time_usage_started.setter
    def time_usage_started(self, time_usage_started):
        """
        Sets the time_usage_started of this ReportQuery.
        The usage start time.


        :param time_usage_started: The time_usage_started of this ReportQuery.
        :type: datetime
        """
        self._time_usage_started = time_usage_started

    @property
    def time_usage_ended(self):
        """
        Gets the time_usage_ended of this ReportQuery.
        The usage end time.


        :return: The time_usage_ended of this ReportQuery.
        :rtype: datetime
        """
        return self._time_usage_ended

    @time_usage_ended.setter
    def time_usage_ended(self, time_usage_ended):
        """
        Sets the time_usage_ended of this ReportQuery.
        The usage end time.


        :param time_usage_ended: The time_usage_ended of this ReportQuery.
        :type: datetime
        """
        self._time_usage_ended = time_usage_ended

    @property
    def granularity(self):
        """
        **[Required]** Gets the granularity of this ReportQuery.
        The usage granularity.
        HOURLY - Hourly data aggregation.
        DAILY - Daily data aggregation.
        MONTHLY - Monthly data aggregation.
        TOTAL - Not yet supported.

        Allowed values for this property are: "HOURLY", "DAILY", "MONTHLY", "TOTAL", 'UNKNOWN_ENUM_VALUE'.
        Any unrecognized values returned by a service will be mapped to 'UNKNOWN_ENUM_VALUE'.


        :return: The granularity of this ReportQuery.
        :rtype: str
        """
        return self._granularity

    @granularity.setter
    def granularity(self, granularity):
        """
        Sets the granularity of this ReportQuery.
        The usage granularity.
        HOURLY - Hourly data aggregation.
        DAILY - Daily data aggregation.
        MONTHLY - Monthly data aggregation.
        TOTAL - Not yet supported.


        :param granularity: The granularity of this ReportQuery.
        :type: str
        """
        allowed_values = ["HOURLY", "DAILY", "MONTHLY", "TOTAL"]
        if not value_allowed_none_or_none_sentinel(granularity, allowed_values):
            granularity = 'UNKNOWN_ENUM_VALUE'
        self._granularity = granularity

    @property
    def is_aggregate_by_time(self):
        """
        Gets the is_aggregate_by_time of this ReportQuery.
        Whether aggregated by time. If isAggregateByTime is true, all usage/cost over the query time period will be added up.


        :return: The is_aggregate_by_time of this ReportQuery.
        :rtype: bool
        """
        return self._is_aggregate_by_time

    @is_aggregate_by_time.setter
    def is_aggregate_by_time(self, is_aggregate_by_time):
        """
        Sets the is_aggregate_by_time of this ReportQuery.
        Whether aggregated by time. If isAggregateByTime is true, all usage/cost over the query time period will be added up.


        :param is_aggregate_by_time: The is_aggregate_by_time of this ReportQuery.
        :type: bool
        """
        self._is_aggregate_by_time = is_aggregate_by_time

    @property
    def forecast(self):
        """
        Gets the forecast of this ReportQuery.

        :return: The forecast of this ReportQuery.
        :rtype: oci.usage_api.models.Forecast
        """
        return self._forecast

    @forecast.setter
    def forecast(self, forecast):
        """
        Sets the forecast of this ReportQuery.

        :param forecast: The forecast of this ReportQuery.
        :type: oci.usage_api.models.Forecast
        """
        self._forecast = forecast

    @property
    def query_type(self):
        """
        Gets the query_type of this ReportQuery.
        The query usage type. COST by default if it is missing.
        Usage - Query the usage data.
        Cost - Query the cost/billing data.
        Credit - Query the credit adjustments data.
        ExpiredCredit - Query the expired credits data
        AllCredit - Query the credit adjustments and expired credit

        Allowed values for this property are: "USAGE", "COST", "CREDIT", "EXPIREDCREDIT", "ALLCREDIT", 'UNKNOWN_ENUM_VALUE'.
        Any unrecognized values returned by a service will be mapped to 'UNKNOWN_ENUM_VALUE'.


        :return: The query_type of this ReportQuery.
        :rtype: str
        """
        return self._query_type

    @query_type.setter
    def query_type(self, query_type):
        """
        Sets the query_type of this ReportQuery.
        The query usage type. COST by default if it is missing.
        Usage - Query the usage data.
        Cost - Query the cost/billing data.
        Credit - Query the credit adjustments data.
        ExpiredCredit - Query the expired credits data
        AllCredit - Query the credit adjustments and expired credit


        :param query_type: The query_type of this ReportQuery.
        :type: str
        """
        allowed_values = ["USAGE", "COST", "CREDIT", "EXPIREDCREDIT", "ALLCREDIT"]
        if not value_allowed_none_or_none_sentinel(query_type, allowed_values):
            query_type = 'UNKNOWN_ENUM_VALUE'
        self._query_type = query_type

    @property
    def group_by(self):
        """
        Gets the group_by of this ReportQuery.
        Aggregate the result by.
        example:
          `[\"tagNamespace\", \"tagKey\", \"tagValue\", \"service\", \"skuName\", \"skuPartNumber\", \"unit\",
            \"compartmentName\", \"compartmentPath\", \"compartmentId\", \"platform\", \"region\", \"logicalAd\",
            \"resourceId\", \"tenantId\", \"tenantName\"]`


        :return: The group_by of this ReportQuery.
        :rtype: list[str]
        """
        return self._group_by

    @group_by.setter
    def group_by(self, group_by):
        """
        Sets the group_by of this ReportQuery.
        Aggregate the result by.
        example:
          `[\"tagNamespace\", \"tagKey\", \"tagValue\", \"service\", \"skuName\", \"skuPartNumber\", \"unit\",
            \"compartmentName\", \"compartmentPath\", \"compartmentId\", \"platform\", \"region\", \"logicalAd\",
            \"resourceId\", \"tenantId\", \"tenantName\"]`


        :param group_by: The group_by of this ReportQuery.
        :type: list[str]
        """
        self._group_by = group_by

    @property
    def group_by_tag(self):
        """
        Gets the group_by_tag of this ReportQuery.
        GroupBy a specific tagKey. Provide the tagNamespace and tagKey in the tag object. Only supports one tag in the list.
        For example:
          `[{\"namespace\":\"oracle\", \"key\":\"createdBy\"]`


        :return: The group_by_tag of this ReportQuery.
        :rtype: list[oci.usage_api.models.Tag]
        """
        return self._group_by_tag

    @group_by_tag.setter
    def group_by_tag(self, group_by_tag):
        """
        Sets the group_by_tag of this ReportQuery.
        GroupBy a specific tagKey. Provide the tagNamespace and tagKey in the tag object. Only supports one tag in the list.
        For example:
          `[{\"namespace\":\"oracle\", \"key\":\"createdBy\"]`


        :param group_by_tag: The group_by_tag of this ReportQuery.
        :type: list[oci.usage_api.models.Tag]
        """
        self._group_by_tag = group_by_tag

    @property
    def compartment_depth(self):
        """
        Gets the compartment_depth of this ReportQuery.
        The compartment depth level.


        :return: The compartment_depth of this ReportQuery.
        :rtype: float
        """
        return self._compartment_depth

    @compartment_depth.setter
    def compartment_depth(self, compartment_depth):
        """
        Sets the compartment_depth of this ReportQuery.
        The compartment depth level.


        :param compartment_depth: The compartment_depth of this ReportQuery.
        :type: float
        """
        self._compartment_depth = compartment_depth

    @property
    def filter(self):
        """
        Gets the filter of this ReportQuery.

        :return: The filter of this ReportQuery.
        :rtype: oci.usage_api.models.Filter
        """
        return self._filter

    @filter.setter
    def filter(self, filter):
        """
        Sets the filter of this ReportQuery.

        :param filter: The filter of this ReportQuery.
        :type: oci.usage_api.models.Filter
        """
        self._filter = filter

    @property
    def date_range_name(self):
        """
        Gets the date_range_name of this ReportQuery.
        The UI date range, for example, LAST_THREE_MONTHS. Conflicts with timeUsageStarted and timeUsageEnded.

        Allowed values for this property are: "LAST_SEVEN_DAYS", "LAST_TEN_DAYS", "MTD", "LAST_TWO_MONTHS", "LAST_THREE_MONTHS", "ALL", "LAST_SIX_MONTHS", "LAST_ONE_YEAR", "YTD", "CUSTOM", 'UNKNOWN_ENUM_VALUE'.
        Any unrecognized values returned by a service will be mapped to 'UNKNOWN_ENUM_VALUE'.


        :return: The date_range_name of this ReportQuery.
        :rtype: str
        """
        return self._date_range_name

    @date_range_name.setter
    def date_range_name(self, date_range_name):
        """
        Sets the date_range_name of this ReportQuery.
        The UI date range, for example, LAST_THREE_MONTHS. Conflicts with timeUsageStarted and timeUsageEnded.


        :param date_range_name: The date_range_name of this ReportQuery.
        :type: str
        """
        allowed_values = ["LAST_SEVEN_DAYS", "LAST_TEN_DAYS", "MTD", "LAST_TWO_MONTHS", "LAST_THREE_MONTHS", "ALL", "LAST_SIX_MONTHS", "LAST_ONE_YEAR", "YTD", "CUSTOM"]
        if not value_allowed_none_or_none_sentinel(date_range_name, allowed_values):
            date_range_name = 'UNKNOWN_ENUM_VALUE'
        self._date_range_name = date_range_name

    def __repr__(self):
        return formatted_flat_dict(self)

    def __eq__(self, other):
        if other is None:
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not self == other
