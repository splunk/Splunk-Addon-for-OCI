# coding: utf-8
# Copyright (c) 2016, 2023, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.


from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class DataSourceEventSummary(object):
    """
    The information about Event details of DataSource.
    """

    #: A constant which can be used with the status property of a DataSourceEventSummary.
    #: This constant has a value of "SUCCESS"
    STATUS_SUCCESS = "SUCCESS"

    #: A constant which can be used with the status property of a DataSourceEventSummary.
    #: This constant has a value of "FAILURE"
    STATUS_FAILURE = "FAILURE"

    def __init__(self, **kwargs):
        """
        Initializes a new DataSourceEventSummary object with values from keyword arguments.
        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param region:
            The value to assign to the region property of this DataSourceEventSummary.
        :type region: str

        :param event_date:
            The value to assign to the event_date property of this DataSourceEventSummary.
        :type event_date: datetime

        :param data_source_id:
            The value to assign to the data_source_id property of this DataSourceEventSummary.
        :type data_source_id: str

        :param time_created:
            The value to assign to the time_created property of this DataSourceEventSummary.
        :type time_created: datetime

        :param status:
            The value to assign to the status property of this DataSourceEventSummary.
            Allowed values for this property are: "SUCCESS", "FAILURE", 'UNKNOWN_ENUM_VALUE'.
            Any unrecognized values returned by a service will be mapped to 'UNKNOWN_ENUM_VALUE'.
        :type status: str

        :param comments:
            The value to assign to the comments property of this DataSourceEventSummary.
        :type comments: str

        :param event_info:
            The value to assign to the event_info property of this DataSourceEventSummary.
        :type event_info: oci.cloud_guard.models.DataSourceEventInfo

        """
        self.swagger_types = {
            'region': 'str',
            'event_date': 'datetime',
            'data_source_id': 'str',
            'time_created': 'datetime',
            'status': 'str',
            'comments': 'str',
            'event_info': 'DataSourceEventInfo'
        }

        self.attribute_map = {
            'region': 'region',
            'event_date': 'eventDate',
            'data_source_id': 'dataSourceId',
            'time_created': 'timeCreated',
            'status': 'status',
            'comments': 'comments',
            'event_info': 'eventInfo'
        }

        self._region = None
        self._event_date = None
        self._data_source_id = None
        self._time_created = None
        self._status = None
        self._comments = None
        self._event_info = None

    @property
    def region(self):
        """
        **[Required]** Gets the region of this DataSourceEventSummary.
        Data source event region


        :return: The region of this DataSourceEventSummary.
        :rtype: str
        """
        return self._region

    @region.setter
    def region(self, region):
        """
        Sets the region of this DataSourceEventSummary.
        Data source event region


        :param region: The region of this DataSourceEventSummary.
        :type: str
        """
        self._region = region

    @property
    def event_date(self):
        """
        **[Required]** Gets the event_date of this DataSourceEventSummary.
        Data source event date time


        :return: The event_date of this DataSourceEventSummary.
        :rtype: datetime
        """
        return self._event_date

    @event_date.setter
    def event_date(self, event_date):
        """
        Sets the event_date of this DataSourceEventSummary.
        Data source event date time


        :param event_date: The event_date of this DataSourceEventSummary.
        :type: datetime
        """
        self._event_date = event_date

    @property
    def data_source_id(self):
        """
        **[Required]** Gets the data_source_id of this DataSourceEventSummary.
        Attached data Source


        :return: The data_source_id of this DataSourceEventSummary.
        :rtype: str
        """
        return self._data_source_id

    @data_source_id.setter
    def data_source_id(self, data_source_id):
        """
        Sets the data_source_id of this DataSourceEventSummary.
        Attached data Source


        :param data_source_id: The data_source_id of this DataSourceEventSummary.
        :type: str
        """
        self._data_source_id = data_source_id

    @property
    def time_created(self):
        """
        **[Required]** Gets the time_created of this DataSourceEventSummary.
        Data source event created time


        :return: The time_created of this DataSourceEventSummary.
        :rtype: datetime
        """
        return self._time_created

    @time_created.setter
    def time_created(self, time_created):
        """
        Sets the time_created of this DataSourceEventSummary.
        Data source event created time


        :param time_created: The time_created of this DataSourceEventSummary.
        :type: datetime
        """
        self._time_created = time_created

    @property
    def status(self):
        """
        Gets the status of this DataSourceEventSummary.
        Current data source event info status

        Allowed values for this property are: "SUCCESS", "FAILURE", 'UNKNOWN_ENUM_VALUE'.
        Any unrecognized values returned by a service will be mapped to 'UNKNOWN_ENUM_VALUE'.


        :return: The status of this DataSourceEventSummary.
        :rtype: str
        """
        return self._status

    @status.setter
    def status(self, status):
        """
        Sets the status of this DataSourceEventSummary.
        Current data source event info status


        :param status: The status of this DataSourceEventSummary.
        :type: str
        """
        allowed_values = ["SUCCESS", "FAILURE"]
        if not value_allowed_none_or_none_sentinel(status, allowed_values):
            status = 'UNKNOWN_ENUM_VALUE'
        self._status = status

    @property
    def comments(self):
        """
        Gets the comments of this DataSourceEventSummary.
        Data source event comments


        :return: The comments of this DataSourceEventSummary.
        :rtype: str
        """
        return self._comments

    @comments.setter
    def comments(self, comments):
        """
        Sets the comments of this DataSourceEventSummary.
        Data source event comments


        :param comments: The comments of this DataSourceEventSummary.
        :type: str
        """
        self._comments = comments

    @property
    def event_info(self):
        """
        **[Required]** Gets the event_info of this DataSourceEventSummary.

        :return: The event_info of this DataSourceEventSummary.
        :rtype: oci.cloud_guard.models.DataSourceEventInfo
        """
        return self._event_info

    @event_info.setter
    def event_info(self, event_info):
        """
        Sets the event_info of this DataSourceEventSummary.

        :param event_info: The event_info of this DataSourceEventSummary.
        :type: oci.cloud_guard.models.DataSourceEventInfo
        """
        self._event_info = event_info

    def __repr__(self):
        return formatted_flat_dict(self)

    def __eq__(self, other):
        if other is None:
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not self == other
