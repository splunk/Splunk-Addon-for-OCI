# coding: utf-8
# Copyright (c) 2016, 2023, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.

from .create_session_target_resource_details import CreateSessionTargetResourceDetails
from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class CreateDynamicPortForwardingSessionTargetResourceDetails(CreateSessionTargetResourceDetails):
    """
    Details about a dynamic port forwarding session for a target subnet.
    """

    def __init__(self, **kwargs):
        """
        Initializes a new CreateDynamicPortForwardingSessionTargetResourceDetails object with values from keyword arguments. The default value of the :py:attr:`~oci.bastion.models.CreateDynamicPortForwardingSessionTargetResourceDetails.session_type` attribute
        of this class is ``DYNAMIC_PORT_FORWARDING`` and it should not be changed.
        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param session_type:
            The value to assign to the session_type property of this CreateDynamicPortForwardingSessionTargetResourceDetails.
            Allowed values for this property are: "MANAGED_SSH", "PORT_FORWARDING", "DYNAMIC_PORT_FORWARDING"
        :type session_type: str

        """
        self.swagger_types = {
            'session_type': 'str'
        }

        self.attribute_map = {
            'session_type': 'sessionType'
        }

        self._session_type = None
        self._session_type = 'DYNAMIC_PORT_FORWARDING'

    def __repr__(self):
        return formatted_flat_dict(self)

    def __eq__(self, other):
        if other is None:
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not self == other
