# coding: utf-8
# Copyright (c) 2016, 2023, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.


from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class RegionStatusDetail(object):
    """
    Status of Region query replication.
    """

    #: A constant which can be used with the status property of a RegionStatusDetail.
    #: This constant has a value of "PROVISIONING"
    STATUS_PROVISIONING = "PROVISIONING"

    #: A constant which can be used with the status property of a RegionStatusDetail.
    #: This constant has a value of "FAILED"
    STATUS_FAILED = "FAILED"

    #: A constant which can be used with the status property of a RegionStatusDetail.
    #: This constant has a value of "SUCCEEDED"
    STATUS_SUCCEEDED = "SUCCEEDED"

    def __init__(self, **kwargs):
        """
        Initializes a new RegionStatusDetail object with values from keyword arguments.
        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param region:
            The value to assign to the region property of this RegionStatusDetail.
        :type region: str

        :param status:
            The value to assign to the status property of this RegionStatusDetail.
            Allowed values for this property are: "PROVISIONING", "FAILED", "SUCCEEDED", 'UNKNOWN_ENUM_VALUE'.
            Any unrecognized values returned by a service will be mapped to 'UNKNOWN_ENUM_VALUE'.
        :type status: str

        """
        self.swagger_types = {
            'region': 'str',
            'status': 'str'
        }

        self.attribute_map = {
            'region': 'region',
            'status': 'status'
        }

        self._region = None
        self._status = None

    @property
    def region(self):
        """
        **[Required]** Gets the region of this RegionStatusDetail.
        Data Source replication region.


        :return: The region of this RegionStatusDetail.
        :rtype: str
        """
        return self._region

    @region.setter
    def region(self, region):
        """
        Sets the region of this RegionStatusDetail.
        Data Source replication region.


        :param region: The region of this RegionStatusDetail.
        :type: str
        """
        self._region = region

    @property
    def status(self):
        """
        **[Required]** Gets the status of this RegionStatusDetail.
        Data Source replication region status.

        Allowed values for this property are: "PROVISIONING", "FAILED", "SUCCEEDED", 'UNKNOWN_ENUM_VALUE'.
        Any unrecognized values returned by a service will be mapped to 'UNKNOWN_ENUM_VALUE'.


        :return: The status of this RegionStatusDetail.
        :rtype: str
        """
        return self._status

    @status.setter
    def status(self, status):
        """
        Sets the status of this RegionStatusDetail.
        Data Source replication region status.


        :param status: The status of this RegionStatusDetail.
        :type: str
        """
        allowed_values = ["PROVISIONING", "FAILED", "SUCCEEDED"]
        if not value_allowed_none_or_none_sentinel(status, allowed_values):
            status = 'UNKNOWN_ENUM_VALUE'
        self._status = status

    def __repr__(self):
        return formatted_flat_dict(self)

    def __eq__(self, other):
        if other is None:
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not self == other
