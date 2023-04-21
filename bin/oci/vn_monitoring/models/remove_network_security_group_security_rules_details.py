# coding: utf-8
# Copyright (c) 2016, 2023, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.


from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class RemoveNetworkSecurityGroupSecurityRulesDetails(object):
    """
    RemoveNetworkSecurityGroupSecurityRulesDetails model.
    """

    def __init__(self, **kwargs):
        """
        Initializes a new RemoveNetworkSecurityGroupSecurityRulesDetails object with values from keyword arguments.
        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param security_rule_ids:
            The value to assign to the security_rule_ids property of this RemoveNetworkSecurityGroupSecurityRulesDetails.
        :type security_rule_ids: list[str]

        """
        self.swagger_types = {
            'security_rule_ids': 'list[str]'
        }

        self.attribute_map = {
            'security_rule_ids': 'securityRuleIds'
        }

        self._security_rule_ids = None

    @property
    def security_rule_ids(self):
        """
        Gets the security_rule_ids of this RemoveNetworkSecurityGroupSecurityRulesDetails.
        The Oracle-assigned ID of each :class:`SecurityRule` to be deleted.


        :return: The security_rule_ids of this RemoveNetworkSecurityGroupSecurityRulesDetails.
        :rtype: list[str]
        """
        return self._security_rule_ids

    @security_rule_ids.setter
    def security_rule_ids(self, security_rule_ids):
        """
        Sets the security_rule_ids of this RemoveNetworkSecurityGroupSecurityRulesDetails.
        The Oracle-assigned ID of each :class:`SecurityRule` to be deleted.


        :param security_rule_ids: The security_rule_ids of this RemoveNetworkSecurityGroupSecurityRulesDetails.
        :type: list[str]
        """
        self._security_rule_ids = security_rule_ids

    def __repr__(self):
        return formatted_flat_dict(self)

    def __eq__(self, other):
        if other is None:
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not self == other
