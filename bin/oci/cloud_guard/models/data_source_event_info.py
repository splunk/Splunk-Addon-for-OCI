# coding: utf-8
# Copyright (c) 2016, 2023, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.


from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class DataSourceEventInfo(object):
    """
    Event info of a data source.
    """

    #: A constant which can be used with the data_source_feed_provider property of a DataSourceEventInfo.
    #: This constant has a value of "LOGGINGQUERY"
    DATA_SOURCE_FEED_PROVIDER_LOGGINGQUERY = "LOGGINGQUERY"

    def __init__(self, **kwargs):
        """
        Initializes a new DataSourceEventInfo object with values from keyword arguments. This class has the following subclasses and if you are using this class as input
        to a service operations then you should favor using a subclass over the base class:

        * :class:`~oci.cloud_guard.models.LoggingEventInfo`

        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param data_source_feed_provider:
            The value to assign to the data_source_feed_provider property of this DataSourceEventInfo.
            Allowed values for this property are: "LOGGINGQUERY", 'UNKNOWN_ENUM_VALUE'.
            Any unrecognized values returned by a service will be mapped to 'UNKNOWN_ENUM_VALUE'.
        :type data_source_feed_provider: str

        """
        self.swagger_types = {
            'data_source_feed_provider': 'str'
        }

        self.attribute_map = {
            'data_source_feed_provider': 'dataSourceFeedProvider'
        }

        self._data_source_feed_provider = None

    @staticmethod
    def get_subtype(object_dictionary):
        """
        Given the hash representation of a subtype of this class,
        use the info in the hash to return the class of the subtype.
        """
        type = object_dictionary['dataSourceFeedProvider']

        if type == 'LOGGINGQUERY':
            return 'LoggingEventInfo'
        else:
            return 'DataSourceEventInfo'

    @property
    def data_source_feed_provider(self):
        """
        **[Required]** Gets the data_source_feed_provider of this DataSourceEventInfo.
        Possible type of dataSourceFeed Provider(LoggingQuery)

        Allowed values for this property are: "LOGGINGQUERY", 'UNKNOWN_ENUM_VALUE'.
        Any unrecognized values returned by a service will be mapped to 'UNKNOWN_ENUM_VALUE'.


        :return: The data_source_feed_provider of this DataSourceEventInfo.
        :rtype: str
        """
        return self._data_source_feed_provider

    @data_source_feed_provider.setter
    def data_source_feed_provider(self, data_source_feed_provider):
        """
        Sets the data_source_feed_provider of this DataSourceEventInfo.
        Possible type of dataSourceFeed Provider(LoggingQuery)


        :param data_source_feed_provider: The data_source_feed_provider of this DataSourceEventInfo.
        :type: str
        """
        allowed_values = ["LOGGINGQUERY"]
        if not value_allowed_none_or_none_sentinel(data_source_feed_provider, allowed_values):
            data_source_feed_provider = 'UNKNOWN_ENUM_VALUE'
        self._data_source_feed_provider = data_source_feed_provider

    def __repr__(self):
        return formatted_flat_dict(self)

    def __eq__(self, other):
        if other is None:
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not self == other
