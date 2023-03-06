# coding: utf-8
# Copyright (c) 2016, 2023, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.


from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class ComputeInstanceGroupRolloutPolicy(object):
    """
    Specifies the rollout policy for compute instance group stages.
    """

    #: A constant which can be used with the policy_type property of a ComputeInstanceGroupRolloutPolicy.
    #: This constant has a value of "COMPUTE_INSTANCE_GROUP_LINEAR_ROLLOUT_POLICY_BY_COUNT"
    POLICY_TYPE_COMPUTE_INSTANCE_GROUP_LINEAR_ROLLOUT_POLICY_BY_COUNT = "COMPUTE_INSTANCE_GROUP_LINEAR_ROLLOUT_POLICY_BY_COUNT"

    #: A constant which can be used with the policy_type property of a ComputeInstanceGroupRolloutPolicy.
    #: This constant has a value of "COMPUTE_INSTANCE_GROUP_LINEAR_ROLLOUT_POLICY_BY_PERCENTAGE"
    POLICY_TYPE_COMPUTE_INSTANCE_GROUP_LINEAR_ROLLOUT_POLICY_BY_PERCENTAGE = "COMPUTE_INSTANCE_GROUP_LINEAR_ROLLOUT_POLICY_BY_PERCENTAGE"

    def __init__(self, **kwargs):
        """
        Initializes a new ComputeInstanceGroupRolloutPolicy object with values from keyword arguments. This class has the following subclasses and if you are using this class as input
        to a service operations then you should favor using a subclass over the base class:

        * :class:`~oci.devops.models.ComputeInstanceGroupLinearRolloutPolicyByPercentage`
        * :class:`~oci.devops.models.ComputeInstanceGroupLinearRolloutPolicyByCount`

        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param policy_type:
            The value to assign to the policy_type property of this ComputeInstanceGroupRolloutPolicy.
            Allowed values for this property are: "COMPUTE_INSTANCE_GROUP_LINEAR_ROLLOUT_POLICY_BY_COUNT", "COMPUTE_INSTANCE_GROUP_LINEAR_ROLLOUT_POLICY_BY_PERCENTAGE", 'UNKNOWN_ENUM_VALUE'.
            Any unrecognized values returned by a service will be mapped to 'UNKNOWN_ENUM_VALUE'.
        :type policy_type: str

        :param batch_delay_in_seconds:
            The value to assign to the batch_delay_in_seconds property of this ComputeInstanceGroupRolloutPolicy.
        :type batch_delay_in_seconds: int

        """
        self.swagger_types = {
            'policy_type': 'str',
            'batch_delay_in_seconds': 'int'
        }

        self.attribute_map = {
            'policy_type': 'policyType',
            'batch_delay_in_seconds': 'batchDelayInSeconds'
        }

        self._policy_type = None
        self._batch_delay_in_seconds = None

    @staticmethod
    def get_subtype(object_dictionary):
        """
        Given the hash representation of a subtype of this class,
        use the info in the hash to return the class of the subtype.
        """
        type = object_dictionary['policyType']

        if type == 'COMPUTE_INSTANCE_GROUP_LINEAR_ROLLOUT_POLICY_BY_PERCENTAGE':
            return 'ComputeInstanceGroupLinearRolloutPolicyByPercentage'

        if type == 'COMPUTE_INSTANCE_GROUP_LINEAR_ROLLOUT_POLICY_BY_COUNT':
            return 'ComputeInstanceGroupLinearRolloutPolicyByCount'
        else:
            return 'ComputeInstanceGroupRolloutPolicy'

    @property
    def policy_type(self):
        """
        **[Required]** Gets the policy_type of this ComputeInstanceGroupRolloutPolicy.
        The type of policy used for rolling out a deployment stage.

        Allowed values for this property are: "COMPUTE_INSTANCE_GROUP_LINEAR_ROLLOUT_POLICY_BY_COUNT", "COMPUTE_INSTANCE_GROUP_LINEAR_ROLLOUT_POLICY_BY_PERCENTAGE", 'UNKNOWN_ENUM_VALUE'.
        Any unrecognized values returned by a service will be mapped to 'UNKNOWN_ENUM_VALUE'.


        :return: The policy_type of this ComputeInstanceGroupRolloutPolicy.
        :rtype: str
        """
        return self._policy_type

    @policy_type.setter
    def policy_type(self, policy_type):
        """
        Sets the policy_type of this ComputeInstanceGroupRolloutPolicy.
        The type of policy used for rolling out a deployment stage.


        :param policy_type: The policy_type of this ComputeInstanceGroupRolloutPolicy.
        :type: str
        """
        allowed_values = ["COMPUTE_INSTANCE_GROUP_LINEAR_ROLLOUT_POLICY_BY_COUNT", "COMPUTE_INSTANCE_GROUP_LINEAR_ROLLOUT_POLICY_BY_PERCENTAGE"]
        if not value_allowed_none_or_none_sentinel(policy_type, allowed_values):
            policy_type = 'UNKNOWN_ENUM_VALUE'
        self._policy_type = policy_type

    @property
    def batch_delay_in_seconds(self):
        """
        Gets the batch_delay_in_seconds of this ComputeInstanceGroupRolloutPolicy.
        The duration of delay between batch rollout. The default delay is 1 minute.


        :return: The batch_delay_in_seconds of this ComputeInstanceGroupRolloutPolicy.
        :rtype: int
        """
        return self._batch_delay_in_seconds

    @batch_delay_in_seconds.setter
    def batch_delay_in_seconds(self, batch_delay_in_seconds):
        """
        Sets the batch_delay_in_seconds of this ComputeInstanceGroupRolloutPolicy.
        The duration of delay between batch rollout. The default delay is 1 minute.


        :param batch_delay_in_seconds: The batch_delay_in_seconds of this ComputeInstanceGroupRolloutPolicy.
        :type: int
        """
        self._batch_delay_in_seconds = batch_delay_in_seconds

    def __repr__(self):
        return formatted_flat_dict(self)

    def __eq__(self, other):
        if other is None:
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not self == other
