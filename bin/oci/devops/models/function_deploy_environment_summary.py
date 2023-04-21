# coding: utf-8
# Copyright (c) 2016, 2023, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.

from .deploy_environment_summary import DeployEnvironmentSummary
from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class FunctionDeployEnvironmentSummary(DeployEnvironmentSummary):
    """
    Specifies the Function environment.
    """

    def __init__(self, **kwargs):
        """
        Initializes a new FunctionDeployEnvironmentSummary object with values from keyword arguments. The default value of the :py:attr:`~oci.devops.models.FunctionDeployEnvironmentSummary.deploy_environment_type` attribute
        of this class is ``FUNCTION`` and it should not be changed.
        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param id:
            The value to assign to the id property of this FunctionDeployEnvironmentSummary.
        :type id: str

        :param description:
            The value to assign to the description property of this FunctionDeployEnvironmentSummary.
        :type description: str

        :param display_name:
            The value to assign to the display_name property of this FunctionDeployEnvironmentSummary.
        :type display_name: str

        :param project_id:
            The value to assign to the project_id property of this FunctionDeployEnvironmentSummary.
        :type project_id: str

        :param compartment_id:
            The value to assign to the compartment_id property of this FunctionDeployEnvironmentSummary.
        :type compartment_id: str

        :param deploy_environment_type:
            The value to assign to the deploy_environment_type property of this FunctionDeployEnvironmentSummary.
        :type deploy_environment_type: str

        :param time_created:
            The value to assign to the time_created property of this FunctionDeployEnvironmentSummary.
        :type time_created: datetime

        :param time_updated:
            The value to assign to the time_updated property of this FunctionDeployEnvironmentSummary.
        :type time_updated: datetime

        :param lifecycle_state:
            The value to assign to the lifecycle_state property of this FunctionDeployEnvironmentSummary.
        :type lifecycle_state: str

        :param lifecycle_details:
            The value to assign to the lifecycle_details property of this FunctionDeployEnvironmentSummary.
        :type lifecycle_details: str

        :param freeform_tags:
            The value to assign to the freeform_tags property of this FunctionDeployEnvironmentSummary.
        :type freeform_tags: dict(str, str)

        :param defined_tags:
            The value to assign to the defined_tags property of this FunctionDeployEnvironmentSummary.
        :type defined_tags: dict(str, dict(str, object))

        :param system_tags:
            The value to assign to the system_tags property of this FunctionDeployEnvironmentSummary.
        :type system_tags: dict(str, dict(str, object))

        :param function_id:
            The value to assign to the function_id property of this FunctionDeployEnvironmentSummary.
        :type function_id: str

        """
        self.swagger_types = {
            'id': 'str',
            'description': 'str',
            'display_name': 'str',
            'project_id': 'str',
            'compartment_id': 'str',
            'deploy_environment_type': 'str',
            'time_created': 'datetime',
            'time_updated': 'datetime',
            'lifecycle_state': 'str',
            'lifecycle_details': 'str',
            'freeform_tags': 'dict(str, str)',
            'defined_tags': 'dict(str, dict(str, object))',
            'system_tags': 'dict(str, dict(str, object))',
            'function_id': 'str'
        }

        self.attribute_map = {
            'id': 'id',
            'description': 'description',
            'display_name': 'displayName',
            'project_id': 'projectId',
            'compartment_id': 'compartmentId',
            'deploy_environment_type': 'deployEnvironmentType',
            'time_created': 'timeCreated',
            'time_updated': 'timeUpdated',
            'lifecycle_state': 'lifecycleState',
            'lifecycle_details': 'lifecycleDetails',
            'freeform_tags': 'freeformTags',
            'defined_tags': 'definedTags',
            'system_tags': 'systemTags',
            'function_id': 'functionId'
        }

        self._id = None
        self._description = None
        self._display_name = None
        self._project_id = None
        self._compartment_id = None
        self._deploy_environment_type = None
        self._time_created = None
        self._time_updated = None
        self._lifecycle_state = None
        self._lifecycle_details = None
        self._freeform_tags = None
        self._defined_tags = None
        self._system_tags = None
        self._function_id = None
        self._deploy_environment_type = 'FUNCTION'

    @property
    def function_id(self):
        """
        **[Required]** Gets the function_id of this FunctionDeployEnvironmentSummary.
        The OCID of the Function.


        :return: The function_id of this FunctionDeployEnvironmentSummary.
        :rtype: str
        """
        return self._function_id

    @function_id.setter
    def function_id(self, function_id):
        """
        Sets the function_id of this FunctionDeployEnvironmentSummary.
        The OCID of the Function.


        :param function_id: The function_id of this FunctionDeployEnvironmentSummary.
        :type: str
        """
        self._function_id = function_id

    def __repr__(self):
        return formatted_flat_dict(self)

    def __eq__(self, other):
        if other is None:
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not self == other
