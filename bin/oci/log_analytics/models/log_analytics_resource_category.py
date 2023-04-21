# coding: utf-8
# Copyright (c) 2016, 2023, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.


from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class LogAnalyticsResourceCategory(object):
    """
    A resource and its category.
    """

    def __init__(self, **kwargs):
        """
        Initializes a new LogAnalyticsResourceCategory object with values from keyword arguments.
        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param resource_id:
            The value to assign to the resource_id property of this LogAnalyticsResourceCategory.
        :type resource_id: str

        :param resource_type:
            The value to assign to the resource_type property of this LogAnalyticsResourceCategory.
        :type resource_type: str

        :param category_name:
            The value to assign to the category_name property of this LogAnalyticsResourceCategory.
        :type category_name: str

        :param is_system:
            The value to assign to the is_system property of this LogAnalyticsResourceCategory.
        :type is_system: bool

        """
        self.swagger_types = {
            'resource_id': 'str',
            'resource_type': 'str',
            'category_name': 'str',
            'is_system': 'bool'
        }

        self.attribute_map = {
            'resource_id': 'resourceId',
            'resource_type': 'resourceType',
            'category_name': 'categoryName',
            'is_system': 'isSystem'
        }

        self._resource_id = None
        self._resource_type = None
        self._category_name = None
        self._is_system = None

    @property
    def resource_id(self):
        """
        Gets the resource_id of this LogAnalyticsResourceCategory.
        The unique identifier of the resource, usually a name or ocid.


        :return: The resource_id of this LogAnalyticsResourceCategory.
        :rtype: str
        """
        return self._resource_id

    @resource_id.setter
    def resource_id(self, resource_id):
        """
        Sets the resource_id of this LogAnalyticsResourceCategory.
        The unique identifier of the resource, usually a name or ocid.


        :param resource_id: The resource_id of this LogAnalyticsResourceCategory.
        :type: str
        """
        self._resource_id = resource_id

    @property
    def resource_type(self):
        """
        Gets the resource_type of this LogAnalyticsResourceCategory.
        The resource type.


        :return: The resource_type of this LogAnalyticsResourceCategory.
        :rtype: str
        """
        return self._resource_type

    @resource_type.setter
    def resource_type(self, resource_type):
        """
        Sets the resource_type of this LogAnalyticsResourceCategory.
        The resource type.


        :param resource_type: The resource_type of this LogAnalyticsResourceCategory.
        :type: str
        """
        self._resource_type = resource_type

    @property
    def category_name(self):
        """
        Gets the category_name of this LogAnalyticsResourceCategory.
        The category name to which this resource belongs.


        :return: The category_name of this LogAnalyticsResourceCategory.
        :rtype: str
        """
        return self._category_name

    @category_name.setter
    def category_name(self, category_name):
        """
        Sets the category_name of this LogAnalyticsResourceCategory.
        The category name to which this resource belongs.


        :param category_name: The category_name of this LogAnalyticsResourceCategory.
        :type: str
        """
        self._category_name = category_name

    @property
    def is_system(self):
        """
        Gets the is_system of this LogAnalyticsResourceCategory.
        The system flag. A value of false denotes a user-created category assignment.
        A value of true denotes an Oracle-defined category assignment.


        :return: The is_system of this LogAnalyticsResourceCategory.
        :rtype: bool
        """
        return self._is_system

    @is_system.setter
    def is_system(self, is_system):
        """
        Sets the is_system of this LogAnalyticsResourceCategory.
        The system flag. A value of false denotes a user-created category assignment.
        A value of true denotes an Oracle-defined category assignment.


        :param is_system: The is_system of this LogAnalyticsResourceCategory.
        :type: bool
        """
        self._is_system = is_system

    def __repr__(self):
        return formatted_flat_dict(self)

    def __eq__(self, other):
        if other is None:
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not self == other
