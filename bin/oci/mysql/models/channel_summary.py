# coding: utf-8
# Copyright (c) 2016, 2023, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.


from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class ChannelSummary(object):
    """
    Summary of a Channel.
    """

    def __init__(self, **kwargs):
        """
        Initializes a new ChannelSummary object with values from keyword arguments.
        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param id:
            The value to assign to the id property of this ChannelSummary.
        :type id: str

        :param compartment_id:
            The value to assign to the compartment_id property of this ChannelSummary.
        :type compartment_id: str

        :param is_enabled:
            The value to assign to the is_enabled property of this ChannelSummary.
        :type is_enabled: bool

        :param source:
            The value to assign to the source property of this ChannelSummary.
        :type source: oci.mysql.models.ChannelSource

        :param target:
            The value to assign to the target property of this ChannelSummary.
        :type target: oci.mysql.models.ChannelTarget

        :param lifecycle_state:
            The value to assign to the lifecycle_state property of this ChannelSummary.
        :type lifecycle_state: str

        :param lifecycle_details:
            The value to assign to the lifecycle_details property of this ChannelSummary.
        :type lifecycle_details: str

        :param display_name:
            The value to assign to the display_name property of this ChannelSummary.
        :type display_name: str

        :param time_created:
            The value to assign to the time_created property of this ChannelSummary.
        :type time_created: datetime

        :param time_updated:
            The value to assign to the time_updated property of this ChannelSummary.
        :type time_updated: datetime

        :param freeform_tags:
            The value to assign to the freeform_tags property of this ChannelSummary.
        :type freeform_tags: dict(str, str)

        :param defined_tags:
            The value to assign to the defined_tags property of this ChannelSummary.
        :type defined_tags: dict(str, dict(str, object))

        """
        self.swagger_types = {
            'id': 'str',
            'compartment_id': 'str',
            'is_enabled': 'bool',
            'source': 'ChannelSource',
            'target': 'ChannelTarget',
            'lifecycle_state': 'str',
            'lifecycle_details': 'str',
            'display_name': 'str',
            'time_created': 'datetime',
            'time_updated': 'datetime',
            'freeform_tags': 'dict(str, str)',
            'defined_tags': 'dict(str, dict(str, object))'
        }

        self.attribute_map = {
            'id': 'id',
            'compartment_id': 'compartmentId',
            'is_enabled': 'isEnabled',
            'source': 'source',
            'target': 'target',
            'lifecycle_state': 'lifecycleState',
            'lifecycle_details': 'lifecycleDetails',
            'display_name': 'displayName',
            'time_created': 'timeCreated',
            'time_updated': 'timeUpdated',
            'freeform_tags': 'freeformTags',
            'defined_tags': 'definedTags'
        }

        self._id = None
        self._compartment_id = None
        self._is_enabled = None
        self._source = None
        self._target = None
        self._lifecycle_state = None
        self._lifecycle_details = None
        self._display_name = None
        self._time_created = None
        self._time_updated = None
        self._freeform_tags = None
        self._defined_tags = None

    @property
    def id(self):
        """
        **[Required]** Gets the id of this ChannelSummary.
        The OCID of the Channel.


        :return: The id of this ChannelSummary.
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """
        Sets the id of this ChannelSummary.
        The OCID of the Channel.


        :param id: The id of this ChannelSummary.
        :type: str
        """
        self._id = id

    @property
    def compartment_id(self):
        """
        **[Required]** Gets the compartment_id of this ChannelSummary.
        The OCID of the compartment.


        :return: The compartment_id of this ChannelSummary.
        :rtype: str
        """
        return self._compartment_id

    @compartment_id.setter
    def compartment_id(self, compartment_id):
        """
        Sets the compartment_id of this ChannelSummary.
        The OCID of the compartment.


        :param compartment_id: The compartment_id of this ChannelSummary.
        :type: str
        """
        self._compartment_id = compartment_id

    @property
    def is_enabled(self):
        """
        **[Required]** Gets the is_enabled of this ChannelSummary.
        Whether the Channel has been enabled by the user.


        :return: The is_enabled of this ChannelSummary.
        :rtype: bool
        """
        return self._is_enabled

    @is_enabled.setter
    def is_enabled(self, is_enabled):
        """
        Sets the is_enabled of this ChannelSummary.
        Whether the Channel has been enabled by the user.


        :param is_enabled: The is_enabled of this ChannelSummary.
        :type: bool
        """
        self._is_enabled = is_enabled

    @property
    def source(self):
        """
        **[Required]** Gets the source of this ChannelSummary.

        :return: The source of this ChannelSummary.
        :rtype: oci.mysql.models.ChannelSource
        """
        return self._source

    @source.setter
    def source(self, source):
        """
        Sets the source of this ChannelSummary.

        :param source: The source of this ChannelSummary.
        :type: oci.mysql.models.ChannelSource
        """
        self._source = source

    @property
    def target(self):
        """
        **[Required]** Gets the target of this ChannelSummary.

        :return: The target of this ChannelSummary.
        :rtype: oci.mysql.models.ChannelTarget
        """
        return self._target

    @target.setter
    def target(self, target):
        """
        Sets the target of this ChannelSummary.

        :param target: The target of this ChannelSummary.
        :type: oci.mysql.models.ChannelTarget
        """
        self._target = target

    @property
    def lifecycle_state(self):
        """
        **[Required]** Gets the lifecycle_state of this ChannelSummary.
        The state of the Channel.


        :return: The lifecycle_state of this ChannelSummary.
        :rtype: str
        """
        return self._lifecycle_state

    @lifecycle_state.setter
    def lifecycle_state(self, lifecycle_state):
        """
        Sets the lifecycle_state of this ChannelSummary.
        The state of the Channel.


        :param lifecycle_state: The lifecycle_state of this ChannelSummary.
        :type: str
        """
        self._lifecycle_state = lifecycle_state

    @property
    def lifecycle_details(self):
        """
        Gets the lifecycle_details of this ChannelSummary.
        A message describing the state of the Channel.


        :return: The lifecycle_details of this ChannelSummary.
        :rtype: str
        """
        return self._lifecycle_details

    @lifecycle_details.setter
    def lifecycle_details(self, lifecycle_details):
        """
        Sets the lifecycle_details of this ChannelSummary.
        A message describing the state of the Channel.


        :param lifecycle_details: The lifecycle_details of this ChannelSummary.
        :type: str
        """
        self._lifecycle_details = lifecycle_details

    @property
    def display_name(self):
        """
        **[Required]** Gets the display_name of this ChannelSummary.
        The user-friendly name for the Channel. It does not have to be unique.


        :return: The display_name of this ChannelSummary.
        :rtype: str
        """
        return self._display_name

    @display_name.setter
    def display_name(self, display_name):
        """
        Sets the display_name of this ChannelSummary.
        The user-friendly name for the Channel. It does not have to be unique.


        :param display_name: The display_name of this ChannelSummary.
        :type: str
        """
        self._display_name = display_name

    @property
    def time_created(self):
        """
        **[Required]** Gets the time_created of this ChannelSummary.
        The date and time the Channel was created, as described by `RFC 3339`__.

        __ https://tools.ietf.org/rfc/rfc3339


        :return: The time_created of this ChannelSummary.
        :rtype: datetime
        """
        return self._time_created

    @time_created.setter
    def time_created(self, time_created):
        """
        Sets the time_created of this ChannelSummary.
        The date and time the Channel was created, as described by `RFC 3339`__.

        __ https://tools.ietf.org/rfc/rfc3339


        :param time_created: The time_created of this ChannelSummary.
        :type: datetime
        """
        self._time_created = time_created

    @property
    def time_updated(self):
        """
        **[Required]** Gets the time_updated of this ChannelSummary.
        The time the Channel was last updated, as described by `RFC 3339`__.

        __ https://tools.ietf.org/rfc/rfc3339


        :return: The time_updated of this ChannelSummary.
        :rtype: datetime
        """
        return self._time_updated

    @time_updated.setter
    def time_updated(self, time_updated):
        """
        Sets the time_updated of this ChannelSummary.
        The time the Channel was last updated, as described by `RFC 3339`__.

        __ https://tools.ietf.org/rfc/rfc3339


        :param time_updated: The time_updated of this ChannelSummary.
        :type: datetime
        """
        self._time_updated = time_updated

    @property
    def freeform_tags(self):
        """
        Gets the freeform_tags of this ChannelSummary.
        Simple key-value pair applied without any predefined name, type or scope. Exists for cross-compatibility only.
        Example: `{\"bar-key\": \"value\"}`


        :return: The freeform_tags of this ChannelSummary.
        :rtype: dict(str, str)
        """
        return self._freeform_tags

    @freeform_tags.setter
    def freeform_tags(self, freeform_tags):
        """
        Sets the freeform_tags of this ChannelSummary.
        Simple key-value pair applied without any predefined name, type or scope. Exists for cross-compatibility only.
        Example: `{\"bar-key\": \"value\"}`


        :param freeform_tags: The freeform_tags of this ChannelSummary.
        :type: dict(str, str)
        """
        self._freeform_tags = freeform_tags

    @property
    def defined_tags(self):
        """
        Gets the defined_tags of this ChannelSummary.
        Usage of predefined tag keys. These predefined keys are scoped to namespaces.
        Example: `{\"foo-namespace\": {\"bar-key\": \"value\"}}`


        :return: The defined_tags of this ChannelSummary.
        :rtype: dict(str, dict(str, object))
        """
        return self._defined_tags

    @defined_tags.setter
    def defined_tags(self, defined_tags):
        """
        Sets the defined_tags of this ChannelSummary.
        Usage of predefined tag keys. These predefined keys are scoped to namespaces.
        Example: `{\"foo-namespace\": {\"bar-key\": \"value\"}}`


        :param defined_tags: The defined_tags of this ChannelSummary.
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
