# coding: utf-8
# Copyright (c) 2016, 2023, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.


from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class ForwardedRoutingActionDetails(object):
    """
    Defines details for the forwarded routing action.
    """

    def __init__(self, **kwargs):
        """
        Initializes a new ForwardedRoutingActionDetails object with values from keyword arguments.
        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param is_restricted_or_partial:
            The value to assign to the is_restricted_or_partial property of this ForwardedRoutingActionDetails.
        :type is_restricted_or_partial: bool

        :param forwarded_routing_configuration:
            The value to assign to the forwarded_routing_configuration property of this ForwardedRoutingActionDetails.
        :type forwarded_routing_configuration: oci.vn_monitoring.models.ForwardedRoutingConfiguration

        """
        self.swagger_types = {
            'is_restricted_or_partial': 'bool',
            'forwarded_routing_configuration': 'ForwardedRoutingConfiguration'
        }

        self.attribute_map = {
            'is_restricted_or_partial': 'isRestrictedOrPartial',
            'forwarded_routing_configuration': 'forwardedRoutingConfiguration'
        }

        self._is_restricted_or_partial = None
        self._forwarded_routing_configuration = None

    @property
    def is_restricted_or_partial(self):
        """
        **[Required]** Gets the is_restricted_or_partial of this ForwardedRoutingActionDetails.
        If true, the forwarded routing configuration details are incomplete.


        :return: The is_restricted_or_partial of this ForwardedRoutingActionDetails.
        :rtype: bool
        """
        return self._is_restricted_or_partial

    @is_restricted_or_partial.setter
    def is_restricted_or_partial(self, is_restricted_or_partial):
        """
        Sets the is_restricted_or_partial of this ForwardedRoutingActionDetails.
        If true, the forwarded routing configuration details are incomplete.


        :param is_restricted_or_partial: The is_restricted_or_partial of this ForwardedRoutingActionDetails.
        :type: bool
        """
        self._is_restricted_or_partial = is_restricted_or_partial

    @property
    def forwarded_routing_configuration(self):
        """
        Gets the forwarded_routing_configuration of this ForwardedRoutingActionDetails.

        :return: The forwarded_routing_configuration of this ForwardedRoutingActionDetails.
        :rtype: oci.vn_monitoring.models.ForwardedRoutingConfiguration
        """
        return self._forwarded_routing_configuration

    @forwarded_routing_configuration.setter
    def forwarded_routing_configuration(self, forwarded_routing_configuration):
        """
        Sets the forwarded_routing_configuration of this ForwardedRoutingActionDetails.

        :param forwarded_routing_configuration: The forwarded_routing_configuration of this ForwardedRoutingActionDetails.
        :type: oci.vn_monitoring.models.ForwardedRoutingConfiguration
        """
        self._forwarded_routing_configuration = forwarded_routing_configuration

    def __repr__(self):
        return formatted_flat_dict(self)

    def __eq__(self, other):
        if other is None:
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not self == other
