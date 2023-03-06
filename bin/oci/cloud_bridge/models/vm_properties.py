# coding: utf-8
# Copyright (c) 2016, 2023, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.


from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class VmProperties(object):
    """
    Virtual machine related properties.
    """

    def __init__(self, **kwargs):
        """
        Initializes a new VmProperties object with values from keyword arguments.
        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param hypervisor_vendor:
            The value to assign to the hypervisor_vendor property of this VmProperties.
        :type hypervisor_vendor: str

        :param hypervisor_version:
            The value to assign to the hypervisor_version property of this VmProperties.
        :type hypervisor_version: str

        :param hypervisor_host:
            The value to assign to the hypervisor_host property of this VmProperties.
        :type hypervisor_host: str

        """
        self.swagger_types = {
            'hypervisor_vendor': 'str',
            'hypervisor_version': 'str',
            'hypervisor_host': 'str'
        }

        self.attribute_map = {
            'hypervisor_vendor': 'hypervisorVendor',
            'hypervisor_version': 'hypervisorVersion',
            'hypervisor_host': 'hypervisorHost'
        }

        self._hypervisor_vendor = None
        self._hypervisor_version = None
        self._hypervisor_host = None

    @property
    def hypervisor_vendor(self):
        """
        Gets the hypervisor_vendor of this VmProperties.
        Hypervisor vendor.


        :return: The hypervisor_vendor of this VmProperties.
        :rtype: str
        """
        return self._hypervisor_vendor

    @hypervisor_vendor.setter
    def hypervisor_vendor(self, hypervisor_vendor):
        """
        Sets the hypervisor_vendor of this VmProperties.
        Hypervisor vendor.


        :param hypervisor_vendor: The hypervisor_vendor of this VmProperties.
        :type: str
        """
        self._hypervisor_vendor = hypervisor_vendor

    @property
    def hypervisor_version(self):
        """
        Gets the hypervisor_version of this VmProperties.
        Hypervisor version.


        :return: The hypervisor_version of this VmProperties.
        :rtype: str
        """
        return self._hypervisor_version

    @hypervisor_version.setter
    def hypervisor_version(self, hypervisor_version):
        """
        Sets the hypervisor_version of this VmProperties.
        Hypervisor version.


        :param hypervisor_version: The hypervisor_version of this VmProperties.
        :type: str
        """
        self._hypervisor_version = hypervisor_version

    @property
    def hypervisor_host(self):
        """
        Gets the hypervisor_host of this VmProperties.
        Host name/IP address of VM on which the host is running.


        :return: The hypervisor_host of this VmProperties.
        :rtype: str
        """
        return self._hypervisor_host

    @hypervisor_host.setter
    def hypervisor_host(self, hypervisor_host):
        """
        Sets the hypervisor_host of this VmProperties.
        Host name/IP address of VM on which the host is running.


        :param hypervisor_host: The hypervisor_host of this VmProperties.
        :type: str
        """
        self._hypervisor_host = hypervisor_host

    def __repr__(self):
        return formatted_flat_dict(self)

    def __eq__(self, other):
        if other is None:
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not self == other
