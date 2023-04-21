# coding: utf-8
# Copyright (c) 2016, 2023, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.


from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class AddonVersions(object):
    """
    The properties that define a work request resource.
    """

    #: A constant which can be used with the status property of a AddonVersions.
    #: This constant has a value of "ACTIVE"
    STATUS_ACTIVE = "ACTIVE"

    #: A constant which can be used with the status property of a AddonVersions.
    #: This constant has a value of "DEPRECATED"
    STATUS_DEPRECATED = "DEPRECATED"

    #: A constant which can be used with the status property of a AddonVersions.
    #: This constant has a value of "PREVIEW"
    STATUS_PREVIEW = "PREVIEW"

    #: A constant which can be used with the status property of a AddonVersions.
    #: This constant has a value of "RECALLED"
    STATUS_RECALLED = "RECALLED"

    def __init__(self, **kwargs):
        """
        Initializes a new AddonVersions object with values from keyword arguments.
        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param status:
            The value to assign to the status property of this AddonVersions.
            Allowed values for this property are: "ACTIVE", "DEPRECATED", "PREVIEW", "RECALLED", 'UNKNOWN_ENUM_VALUE'.
            Any unrecognized values returned by a service will be mapped to 'UNKNOWN_ENUM_VALUE'.
        :type status: str

        :param version_number:
            The value to assign to the version_number property of this AddonVersions.
        :type version_number: str

        :param description:
            The value to assign to the description property of this AddonVersions.
        :type description: str

        :param kubernetes_version_filters:
            The value to assign to the kubernetes_version_filters property of this AddonVersions.
        :type kubernetes_version_filters: oci.container_engine.models.KubernetesVersionsFilters

        :param configurations:
            The value to assign to the configurations property of this AddonVersions.
        :type configurations: list[oci.container_engine.models.AddonVersionConfiguration]

        """
        self.swagger_types = {
            'status': 'str',
            'version_number': 'str',
            'description': 'str',
            'kubernetes_version_filters': 'KubernetesVersionsFilters',
            'configurations': 'list[AddonVersionConfiguration]'
        }

        self.attribute_map = {
            'status': 'status',
            'version_number': 'versionNumber',
            'description': 'description',
            'kubernetes_version_filters': 'kubernetesVersionFilters',
            'configurations': 'configurations'
        }

        self._status = None
        self._version_number = None
        self._description = None
        self._kubernetes_version_filters = None
        self._configurations = None

    @property
    def status(self):
        """
        Gets the status of this AddonVersions.
        Current state of the addon, only active will be visible to customer, visibility of versions in other status will be filtered  based on limits property.

        Allowed values for this property are: "ACTIVE", "DEPRECATED", "PREVIEW", "RECALLED", 'UNKNOWN_ENUM_VALUE'.
        Any unrecognized values returned by a service will be mapped to 'UNKNOWN_ENUM_VALUE'.


        :return: The status of this AddonVersions.
        :rtype: str
        """
        return self._status

    @status.setter
    def status(self, status):
        """
        Sets the status of this AddonVersions.
        Current state of the addon, only active will be visible to customer, visibility of versions in other status will be filtered  based on limits property.


        :param status: The status of this AddonVersions.
        :type: str
        """
        allowed_values = ["ACTIVE", "DEPRECATED", "PREVIEW", "RECALLED"]
        if not value_allowed_none_or_none_sentinel(status, allowed_values):
            status = 'UNKNOWN_ENUM_VALUE'
        self._status = status

    @property
    def version_number(self):
        """
        Gets the version_number of this AddonVersions.
        Version number, need be comparable within an addon.


        :return: The version_number of this AddonVersions.
        :rtype: str
        """
        return self._version_number

    @version_number.setter
    def version_number(self, version_number):
        """
        Sets the version_number of this AddonVersions.
        Version number, need be comparable within an addon.


        :param version_number: The version_number of this AddonVersions.
        :type: str
        """
        self._version_number = version_number

    @property
    def description(self):
        """
        Gets the description of this AddonVersions.
        Information about the addon version.


        :return: The description of this AddonVersions.
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        """
        Sets the description of this AddonVersions.
        Information about the addon version.


        :param description: The description of this AddonVersions.
        :type: str
        """
        self._description = description

    @property
    def kubernetes_version_filters(self):
        """
        Gets the kubernetes_version_filters of this AddonVersions.
        The range of kubernetes versions an addon can be configured.


        :return: The kubernetes_version_filters of this AddonVersions.
        :rtype: oci.container_engine.models.KubernetesVersionsFilters
        """
        return self._kubernetes_version_filters

    @kubernetes_version_filters.setter
    def kubernetes_version_filters(self, kubernetes_version_filters):
        """
        Sets the kubernetes_version_filters of this AddonVersions.
        The range of kubernetes versions an addon can be configured.


        :param kubernetes_version_filters: The kubernetes_version_filters of this AddonVersions.
        :type: oci.container_engine.models.KubernetesVersionsFilters
        """
        self._kubernetes_version_filters = kubernetes_version_filters

    @property
    def configurations(self):
        """
        Gets the configurations of this AddonVersions.
        Addon version configuration details.


        :return: The configurations of this AddonVersions.
        :rtype: list[oci.container_engine.models.AddonVersionConfiguration]
        """
        return self._configurations

    @configurations.setter
    def configurations(self, configurations):
        """
        Sets the configurations of this AddonVersions.
        Addon version configuration details.


        :param configurations: The configurations of this AddonVersions.
        :type: list[oci.container_engine.models.AddonVersionConfiguration]
        """
        self._configurations = configurations

    def __repr__(self):
        return formatted_flat_dict(self)

    def __eq__(self, other):
        if other is None:
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not self == other
