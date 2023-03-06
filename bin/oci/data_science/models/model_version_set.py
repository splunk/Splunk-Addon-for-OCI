# coding: utf-8
# Copyright (c) 2016, 2023, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.


from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class ModelVersionSet(object):
    """
    A model version set to associate different versions of machine learning models.
    """

    #: A constant which can be used with the lifecycle_state property of a ModelVersionSet.
    #: This constant has a value of "ACTIVE"
    LIFECYCLE_STATE_ACTIVE = "ACTIVE"

    #: A constant which can be used with the lifecycle_state property of a ModelVersionSet.
    #: This constant has a value of "DELETING"
    LIFECYCLE_STATE_DELETING = "DELETING"

    #: A constant which can be used with the lifecycle_state property of a ModelVersionSet.
    #: This constant has a value of "DELETED"
    LIFECYCLE_STATE_DELETED = "DELETED"

    #: A constant which can be used with the lifecycle_state property of a ModelVersionSet.
    #: This constant has a value of "FAILED"
    LIFECYCLE_STATE_FAILED = "FAILED"

    def __init__(self, **kwargs):
        """
        Initializes a new ModelVersionSet object with values from keyword arguments.
        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param id:
            The value to assign to the id property of this ModelVersionSet.
        :type id: str

        :param compartment_id:
            The value to assign to the compartment_id property of this ModelVersionSet.
        :type compartment_id: str

        :param project_id:
            The value to assign to the project_id property of this ModelVersionSet.
        :type project_id: str

        :param name:
            The value to assign to the name property of this ModelVersionSet.
        :type name: str

        :param description:
            The value to assign to the description property of this ModelVersionSet.
        :type description: str

        :param lifecycle_state:
            The value to assign to the lifecycle_state property of this ModelVersionSet.
            Allowed values for this property are: "ACTIVE", "DELETING", "DELETED", "FAILED", 'UNKNOWN_ENUM_VALUE'.
            Any unrecognized values returned by a service will be mapped to 'UNKNOWN_ENUM_VALUE'.
        :type lifecycle_state: str

        :param time_created:
            The value to assign to the time_created property of this ModelVersionSet.
        :type time_created: datetime

        :param time_updated:
            The value to assign to the time_updated property of this ModelVersionSet.
        :type time_updated: datetime

        :param created_by:
            The value to assign to the created_by property of this ModelVersionSet.
        :type created_by: str

        :param freeform_tags:
            The value to assign to the freeform_tags property of this ModelVersionSet.
        :type freeform_tags: dict(str, str)

        :param defined_tags:
            The value to assign to the defined_tags property of this ModelVersionSet.
        :type defined_tags: dict(str, dict(str, object))

        """
        self.swagger_types = {
            'id': 'str',
            'compartment_id': 'str',
            'project_id': 'str',
            'name': 'str',
            'description': 'str',
            'lifecycle_state': 'str',
            'time_created': 'datetime',
            'time_updated': 'datetime',
            'created_by': 'str',
            'freeform_tags': 'dict(str, str)',
            'defined_tags': 'dict(str, dict(str, object))'
        }

        self.attribute_map = {
            'id': 'id',
            'compartment_id': 'compartmentId',
            'project_id': 'projectId',
            'name': 'name',
            'description': 'description',
            'lifecycle_state': 'lifecycleState',
            'time_created': 'timeCreated',
            'time_updated': 'timeUpdated',
            'created_by': 'createdBy',
            'freeform_tags': 'freeformTags',
            'defined_tags': 'definedTags'
        }

        self._id = None
        self._compartment_id = None
        self._project_id = None
        self._name = None
        self._description = None
        self._lifecycle_state = None
        self._time_created = None
        self._time_updated = None
        self._created_by = None
        self._freeform_tags = None
        self._defined_tags = None

    @property
    def id(self):
        """
        **[Required]** Gets the id of this ModelVersionSet.
        The `OCID`__ of the model version set.

        __ https://docs.cloud.oracle.com/iaas/Content/General/Concepts/identifiers.htm


        :return: The id of this ModelVersionSet.
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """
        Sets the id of this ModelVersionSet.
        The `OCID`__ of the model version set.

        __ https://docs.cloud.oracle.com/iaas/Content/General/Concepts/identifiers.htm


        :param id: The id of this ModelVersionSet.
        :type: str
        """
        self._id = id

    @property
    def compartment_id(self):
        """
        **[Required]** Gets the compartment_id of this ModelVersionSet.
        The `OCID`__ of the model version set compartment.

        __ https://docs.cloud.oracle.com/iaas/Content/General/Concepts/identifiers.htm


        :return: The compartment_id of this ModelVersionSet.
        :rtype: str
        """
        return self._compartment_id

    @compartment_id.setter
    def compartment_id(self, compartment_id):
        """
        Sets the compartment_id of this ModelVersionSet.
        The `OCID`__ of the model version set compartment.

        __ https://docs.cloud.oracle.com/iaas/Content/General/Concepts/identifiers.htm


        :param compartment_id: The compartment_id of this ModelVersionSet.
        :type: str
        """
        self._compartment_id = compartment_id

    @property
    def project_id(self):
        """
        **[Required]** Gets the project_id of this ModelVersionSet.
        The `OCID`__ of the project associated with the model version set.

        __ https://docs.cloud.oracle.com/iaas/Content/General/Concepts/identifiers.htm


        :return: The project_id of this ModelVersionSet.
        :rtype: str
        """
        return self._project_id

    @project_id.setter
    def project_id(self, project_id):
        """
        Sets the project_id of this ModelVersionSet.
        The `OCID`__ of the project associated with the model version set.

        __ https://docs.cloud.oracle.com/iaas/Content/General/Concepts/identifiers.htm


        :param project_id: The project_id of this ModelVersionSet.
        :type: str
        """
        self._project_id = project_id

    @property
    def name(self):
        """
        **[Required]** Gets the name of this ModelVersionSet.
        A user-friendly name for the resource.


        :return: The name of this ModelVersionSet.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """
        Sets the name of this ModelVersionSet.
        A user-friendly name for the resource.


        :param name: The name of this ModelVersionSet.
        :type: str
        """
        self._name = name

    @property
    def description(self):
        """
        **[Required]** Gets the description of this ModelVersionSet.
        A short description of the model version set.


        :return: The description of this ModelVersionSet.
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        """
        Sets the description of this ModelVersionSet.
        A short description of the model version set.


        :param description: The description of this ModelVersionSet.
        :type: str
        """
        self._description = description

    @property
    def lifecycle_state(self):
        """
        **[Required]** Gets the lifecycle_state of this ModelVersionSet.
        The state of the model version set.

        Allowed values for this property are: "ACTIVE", "DELETING", "DELETED", "FAILED", 'UNKNOWN_ENUM_VALUE'.
        Any unrecognized values returned by a service will be mapped to 'UNKNOWN_ENUM_VALUE'.


        :return: The lifecycle_state of this ModelVersionSet.
        :rtype: str
        """
        return self._lifecycle_state

    @lifecycle_state.setter
    def lifecycle_state(self, lifecycle_state):
        """
        Sets the lifecycle_state of this ModelVersionSet.
        The state of the model version set.


        :param lifecycle_state: The lifecycle_state of this ModelVersionSet.
        :type: str
        """
        allowed_values = ["ACTIVE", "DELETING", "DELETED", "FAILED"]
        if not value_allowed_none_or_none_sentinel(lifecycle_state, allowed_values):
            lifecycle_state = 'UNKNOWN_ENUM_VALUE'
        self._lifecycle_state = lifecycle_state

    @property
    def time_created(self):
        """
        **[Required]** Gets the time_created of this ModelVersionSet.
        The date and time that the resource was created in the timestamp format defined by `RFC3339`__.
        Example: 2019-08-25T21:10:29.41Z

        __ https://tools.ietf.org/html/rfc3339


        :return: The time_created of this ModelVersionSet.
        :rtype: datetime
        """
        return self._time_created

    @time_created.setter
    def time_created(self, time_created):
        """
        Sets the time_created of this ModelVersionSet.
        The date and time that the resource was created in the timestamp format defined by `RFC3339`__.
        Example: 2019-08-25T21:10:29.41Z

        __ https://tools.ietf.org/html/rfc3339


        :param time_created: The time_created of this ModelVersionSet.
        :type: datetime
        """
        self._time_created = time_created

    @property
    def time_updated(self):
        """
        **[Required]** Gets the time_updated of this ModelVersionSet.
        The date and time that the resource was created in the timestamp format defined by `RFC3339`__.
        Example: 2019-08-25T21:10:29.41Z

        __ https://tools.ietf.org/html/rfc3339


        :return: The time_updated of this ModelVersionSet.
        :rtype: datetime
        """
        return self._time_updated

    @time_updated.setter
    def time_updated(self, time_updated):
        """
        Sets the time_updated of this ModelVersionSet.
        The date and time that the resource was created in the timestamp format defined by `RFC3339`__.
        Example: 2019-08-25T21:10:29.41Z

        __ https://tools.ietf.org/html/rfc3339


        :param time_updated: The time_updated of this ModelVersionSet.
        :type: datetime
        """
        self._time_updated = time_updated

    @property
    def created_by(self):
        """
        **[Required]** Gets the created_by of this ModelVersionSet.
        The `OCID`__ of the user who created the model version set.

        __ https://docs.cloud.oracle.com/iaas/Content/General/Concepts/identifiers.htm


        :return: The created_by of this ModelVersionSet.
        :rtype: str
        """
        return self._created_by

    @created_by.setter
    def created_by(self, created_by):
        """
        Sets the created_by of this ModelVersionSet.
        The `OCID`__ of the user who created the model version set.

        __ https://docs.cloud.oracle.com/iaas/Content/General/Concepts/identifiers.htm


        :param created_by: The created_by of this ModelVersionSet.
        :type: str
        """
        self._created_by = created_by

    @property
    def freeform_tags(self):
        """
        Gets the freeform_tags of this ModelVersionSet.
        Free-form tags for this resource. Each tag is a simple key-value pair with no predefined name, type, or namespace. See `Resource Tags`__.
        Example: `{\"Department\": \"Finance\"}`

        __ https://docs.cloud.oracle.com/Content/General/Concepts/resourcetags.htm


        :return: The freeform_tags of this ModelVersionSet.
        :rtype: dict(str, str)
        """
        return self._freeform_tags

    @freeform_tags.setter
    def freeform_tags(self, freeform_tags):
        """
        Sets the freeform_tags of this ModelVersionSet.
        Free-form tags for this resource. Each tag is a simple key-value pair with no predefined name, type, or namespace. See `Resource Tags`__.
        Example: `{\"Department\": \"Finance\"}`

        __ https://docs.cloud.oracle.com/Content/General/Concepts/resourcetags.htm


        :param freeform_tags: The freeform_tags of this ModelVersionSet.
        :type: dict(str, str)
        """
        self._freeform_tags = freeform_tags

    @property
    def defined_tags(self):
        """
        Gets the defined_tags of this ModelVersionSet.
        Defined tags for this resource. Each key is predefined and scoped to a namespace. See `Resource Tags`__.
        Example: `{\"Operations\": {\"CostCenter\": \"42\"}}`

        __ https://docs.cloud.oracle.com/Content/General/Concepts/resourcetags.htm


        :return: The defined_tags of this ModelVersionSet.
        :rtype: dict(str, dict(str, object))
        """
        return self._defined_tags

    @defined_tags.setter
    def defined_tags(self, defined_tags):
        """
        Sets the defined_tags of this ModelVersionSet.
        Defined tags for this resource. Each key is predefined and scoped to a namespace. See `Resource Tags`__.
        Example: `{\"Operations\": {\"CostCenter\": \"42\"}}`

        __ https://docs.cloud.oracle.com/Content/General/Concepts/resourcetags.htm


        :param defined_tags: The defined_tags of this ModelVersionSet.
        :type: dict(str, dict(str, object))
        """
        self._defined_tags = defined_tags

    def __repr__(self):
        return formatted_flat_dict(self)

    def __eq__(self, other):
        if other is None:
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not self == other
