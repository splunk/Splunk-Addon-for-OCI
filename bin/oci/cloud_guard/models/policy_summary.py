# coding: utf-8
# Copyright (c) 2016, 2023, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.


from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class PolicySummary(object):
    """
    Global policy statement
    """

    def __init__(self, **kwargs):
        """
        Initializes a new PolicySummary object with values from keyword arguments.
        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param policy:
            The value to assign to the policy property of this PolicySummary.
        :type policy: str

        """
        self.swagger_types = {
            'policy': 'str'
        }

        self.attribute_map = {
            'policy': 'policy'
        }

        self._policy = None

    @property
    def policy(self):
        """
        **[Required]** Gets the policy of this PolicySummary.
        Global policy statement


        :return: The policy of this PolicySummary.
        :rtype: str
        """
        return self._policy

    @policy.setter
    def policy(self, policy):
        """
        Sets the policy of this PolicySummary.
        Global policy statement


        :param policy: The policy of this PolicySummary.
        :type: str
        """
        self._policy = policy

    def __repr__(self):
        return formatted_flat_dict(self)

    def __eq__(self, other):
        if other is None:
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not self == other
