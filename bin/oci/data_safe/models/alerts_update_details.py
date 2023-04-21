# coding: utf-8
# Copyright (c) 2016, 2023, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.


from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class AlertsUpdateDetails(object):
    """
    The details to update alerts in the specified compartment.
    """

    #: A constant which can be used with the status property of a AlertsUpdateDetails.
    #: This constant has a value of "OPEN"
    STATUS_OPEN = "OPEN"

    #: A constant which can be used with the status property of a AlertsUpdateDetails.
    #: This constant has a value of "CLOSED"
    STATUS_CLOSED = "CLOSED"

    def __init__(self, **kwargs):
        """
        Initializes a new AlertsUpdateDetails object with values from keyword arguments.
        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param status:
            The value to assign to the status property of this AlertsUpdateDetails.
            Allowed values for this property are: "OPEN", "CLOSED"
        :type status: str

        :param compartment_id:
            The value to assign to the compartment_id property of this AlertsUpdateDetails.
        :type compartment_id: str

        :param target_id:
            The value to assign to the target_id property of this AlertsUpdateDetails.
        :type target_id: str

        """
        self.swagger_types = {
            'status': 'str',
            'compartment_id': 'str',
            'target_id': 'str'
        }

        self.attribute_map = {
            'status': 'status',
            'compartment_id': 'compartmentId',
            'target_id': 'targetId'
        }

        self._status = None
        self._compartment_id = None
        self._target_id = None

    @property
    def status(self):
        """
        **[Required]** Gets the status of this AlertsUpdateDetails.
        The status of the alert.

        Allowed values for this property are: "OPEN", "CLOSED"


        :return: The status of this AlertsUpdateDetails.
        :rtype: str
        """
        return self._status

    @status.setter
    def status(self, status):
        """
        Sets the status of this AlertsUpdateDetails.
        The status of the alert.


        :param status: The status of this AlertsUpdateDetails.
        :type: str
        """
        allowed_values = ["OPEN", "CLOSED"]
        if not value_allowed_none_or_none_sentinel(status, allowed_values):
            raise ValueError(
                "Invalid value for `status`, must be None or one of {0}"
                .format(allowed_values)
            )
        self._status = status

    @property
    def compartment_id(self):
        """
        **[Required]** Gets the compartment_id of this AlertsUpdateDetails.
        The OCID of the compartment that contains the alerts.


        :return: The compartment_id of this AlertsUpdateDetails.
        :rtype: str
        """
        return self._compartment_id

    @compartment_id.setter
    def compartment_id(self, compartment_id):
        """
        Sets the compartment_id of this AlertsUpdateDetails.
        The OCID of the compartment that contains the alerts.


        :param compartment_id: The compartment_id of this AlertsUpdateDetails.
        :type: str
        """
        self._compartment_id = compartment_id

    @property
    def target_id(self):
        """
        Gets the target_id of this AlertsUpdateDetails.
        The OCID of the target database associated with the alerts.


        :return: The target_id of this AlertsUpdateDetails.
        :rtype: str
        """
        return self._target_id

    @target_id.setter
    def target_id(self, target_id):
        """
        Sets the target_id of this AlertsUpdateDetails.
        The OCID of the target database associated with the alerts.


        :param target_id: The target_id of this AlertsUpdateDetails.
        :type: str
        """
        self._target_id = target_id

    def __repr__(self):
        return formatted_flat_dict(self)

    def __eq__(self, other):
        if other is None:
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not self == other
