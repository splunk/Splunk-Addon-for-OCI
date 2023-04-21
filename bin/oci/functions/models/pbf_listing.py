# coding: utf-8
# Copyright (c) 2016, 2023, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.


from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class PbfListing(object):
    """
    PbfListing resources provide details about the available PBFs for consumption by the user.
    This resource contains details about PBF's functionality, policies required, configuration parameters expected
    etc.
    """

    #: A constant which can be used with the lifecycle_state property of a PbfListing.
    #: This constant has a value of "ACTIVE"
    LIFECYCLE_STATE_ACTIVE = "ACTIVE"

    #: A constant which can be used with the lifecycle_state property of a PbfListing.
    #: This constant has a value of "INACTIVE"
    LIFECYCLE_STATE_INACTIVE = "INACTIVE"

    #: A constant which can be used with the lifecycle_state property of a PbfListing.
    #: This constant has a value of "DELETED"
    LIFECYCLE_STATE_DELETED = "DELETED"

    def __init__(self, **kwargs):
        """
        Initializes a new PbfListing object with values from keyword arguments.
        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param id:
            The value to assign to the id property of this PbfListing.
        :type id: str

        :param name:
            The value to assign to the name property of this PbfListing.
        :type name: str

        :param description:
            The value to assign to the description property of this PbfListing.
        :type description: str

        :param publisher_details:
            The value to assign to the publisher_details property of this PbfListing.
        :type publisher_details: oci.functions.models.PublisherDetails

        :param triggers:
            The value to assign to the triggers property of this PbfListing.
        :type triggers: list[oci.functions.models.Trigger]

        :param time_created:
            The value to assign to the time_created property of this PbfListing.
        :type time_created: datetime

        :param time_updated:
            The value to assign to the time_updated property of this PbfListing.
        :type time_updated: datetime

        :param lifecycle_state:
            The value to assign to the lifecycle_state property of this PbfListing.
            Allowed values for this property are: "ACTIVE", "INACTIVE", "DELETED", 'UNKNOWN_ENUM_VALUE'.
            Any unrecognized values returned by a service will be mapped to 'UNKNOWN_ENUM_VALUE'.
        :type lifecycle_state: str

        :param freeform_tags:
            The value to assign to the freeform_tags property of this PbfListing.
        :type freeform_tags: dict(str, str)

        :param defined_tags:
            The value to assign to the defined_tags property of this PbfListing.
        :type defined_tags: dict(str, dict(str, object))

        :param system_tags:
            The value to assign to the system_tags property of this PbfListing.
        :type system_tags: dict(str, dict(str, object))

        """
        self.swagger_types = {
            'id': 'str',
            'name': 'str',
            'description': 'str',
            'publisher_details': 'PublisherDetails',
            'triggers': 'list[Trigger]',
            'time_created': 'datetime',
            'time_updated': 'datetime',
            'lifecycle_state': 'str',
            'freeform_tags': 'dict(str, str)',
            'defined_tags': 'dict(str, dict(str, object))',
            'system_tags': 'dict(str, dict(str, object))'
        }

        self.attribute_map = {
            'id': 'id',
            'name': 'name',
            'description': 'description',
            'publisher_details': 'publisherDetails',
            'triggers': 'triggers',
            'time_created': 'timeCreated',
            'time_updated': 'timeUpdated',
            'lifecycle_state': 'lifecycleState',
            'freeform_tags': 'freeformTags',
            'defined_tags': 'definedTags',
            'system_tags': 'systemTags'
        }

        self._id = None
        self._name = None
        self._description = None
        self._publisher_details = None
        self._triggers = None
        self._time_created = None
        self._time_updated = None
        self._lifecycle_state = None
        self._freeform_tags = None
        self._defined_tags = None
        self._system_tags = None

    @property
    def id(self):
        """
        **[Required]** Gets the id of this PbfListing.
        Unique identifier that is immutable on creation.


        :return: The id of this PbfListing.
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """
        Sets the id of this PbfListing.
        Unique identifier that is immutable on creation.


        :param id: The id of this PbfListing.
        :type: str
        """
        self._id = id

    @property
    def name(self):
        """
        **[Required]** Gets the name of this PbfListing.
        A brief descriptive name for the PBF listing. The PBF listing name must be unique, and not match and existing
        PBF.


        :return: The name of this PbfListing.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """
        Sets the name of this PbfListing.
        A brief descriptive name for the PBF listing. The PBF listing name must be unique, and not match and existing
        PBF.


        :param name: The name of this PbfListing.
        :type: str
        """
        self._name = name

    @property
    def description(self):
        """
        **[Required]** Gets the description of this PbfListing.
        A short overview of the PBF Listing: the purpose of the PBF and and associated information.


        :return: The description of this PbfListing.
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        """
        Sets the description of this PbfListing.
        A short overview of the PBF Listing: the purpose of the PBF and and associated information.


        :param description: The description of this PbfListing.
        :type: str
        """
        self._description = description

    @property
    def publisher_details(self):
        """
        **[Required]** Gets the publisher_details of this PbfListing.

        :return: The publisher_details of this PbfListing.
        :rtype: oci.functions.models.PublisherDetails
        """
        return self._publisher_details

    @publisher_details.setter
    def publisher_details(self, publisher_details):
        """
        Sets the publisher_details of this PbfListing.

        :param publisher_details: The publisher_details of this PbfListing.
        :type: oci.functions.models.PublisherDetails
        """
        self._publisher_details = publisher_details

    @property
    def triggers(self):
        """
        Gets the triggers of this PbfListing.
        An array of Trigger. A list of triggers that may activate the PBF.


        :return: The triggers of this PbfListing.
        :rtype: list[oci.functions.models.Trigger]
        """
        return self._triggers

    @triggers.setter
    def triggers(self, triggers):
        """
        Sets the triggers of this PbfListing.
        An array of Trigger. A list of triggers that may activate the PBF.


        :param triggers: The triggers of this PbfListing.
        :type: list[oci.functions.models.Trigger]
        """
        self._triggers = triggers

    @property
    def time_created(self):
        """
        **[Required]** Gets the time_created of this PbfListing.
        The time the PbfListing was created. An RFC3339 formatted datetime string.


        :return: The time_created of this PbfListing.
        :rtype: datetime
        """
        return self._time_created

    @time_created.setter
    def time_created(self, time_created):
        """
        Sets the time_created of this PbfListing.
        The time the PbfListing was created. An RFC3339 formatted datetime string.


        :param time_created: The time_created of this PbfListing.
        :type: datetime
        """
        self._time_created = time_created

    @property
    def time_updated(self):
        """
        **[Required]** Gets the time_updated of this PbfListing.
        The last time the PbfListing was updated. An RFC3339 formatted datetime string.


        :return: The time_updated of this PbfListing.
        :rtype: datetime
        """
        return self._time_updated

    @time_updated.setter
    def time_updated(self, time_updated):
        """
        Sets the time_updated of this PbfListing.
        The last time the PbfListing was updated. An RFC3339 formatted datetime string.


        :param time_updated: The time_updated of this PbfListing.
        :type: datetime
        """
        self._time_updated = time_updated

    @property
    def lifecycle_state(self):
        """
        **[Required]** Gets the lifecycle_state of this PbfListing.
        The current state of the PBF resource.

        Allowed values for this property are: "ACTIVE", "INACTIVE", "DELETED", 'UNKNOWN_ENUM_VALUE'.
        Any unrecognized values returned by a service will be mapped to 'UNKNOWN_ENUM_VALUE'.


        :return: The lifecycle_state of this PbfListing.
        :rtype: str
        """
        return self._lifecycle_state

    @lifecycle_state.setter
    def lifecycle_state(self, lifecycle_state):
        """
        Sets the lifecycle_state of this PbfListing.
        The current state of the PBF resource.


        :param lifecycle_state: The lifecycle_state of this PbfListing.
        :type: str
        """
        allowed_values = ["ACTIVE", "INACTIVE", "DELETED"]
        if not value_allowed_none_or_none_sentinel(lifecycle_state, allowed_values):
            lifecycle_state = 'UNKNOWN_ENUM_VALUE'
        self._lifecycle_state = lifecycle_state

    @property
    def freeform_tags(self):
        """
        Gets the freeform_tags of this PbfListing.
        Simple key-value pair that is applied without any predefined name, type or scope. Exists for cross-compatibility only.
        Example: `{\"bar-key\": \"value\"}`


        :return: The freeform_tags of this PbfListing.
        :rtype: dict(str, str)
        """
        return self._freeform_tags

    @freeform_tags.setter
    def freeform_tags(self, freeform_tags):
        """
        Sets the freeform_tags of this PbfListing.
        Simple key-value pair that is applied without any predefined name, type or scope. Exists for cross-compatibility only.
        Example: `{\"bar-key\": \"value\"}`


        :param freeform_tags: The freeform_tags of this PbfListing.
        :type: dict(str, str)
        """
        self._freeform_tags = freeform_tags

    @property
    def defined_tags(self):
        """
        Gets the defined_tags of this PbfListing.
        Defined tags for this resource. Each key is predefined and scoped to a namespace.
        Example: `{\"foo-namespace\": {\"bar-key\": \"value\"}}`


        :return: The defined_tags of this PbfListing.
        :rtype: dict(str, dict(str, object))
        """
        return self._defined_tags

    @defined_tags.setter
    def defined_tags(self, defined_tags):
        """
        Sets the defined_tags of this PbfListing.
        Defined tags for this resource. Each key is predefined and scoped to a namespace.
        Example: `{\"foo-namespace\": {\"bar-key\": \"value\"}}`


        :param defined_tags: The defined_tags of this PbfListing.
        :type: dict(str, dict(str, object))
        """
        self._defined_tags = defined_tags

    @property
    def system_tags(self):
        """
        Gets the system_tags of this PbfListing.
        System tags for this resource. Each key is predefined and scoped to a namespace.
        Example: `{\"orcl-cloud\": {\"free-tier-retained\": \"true\"}}`


        :return: The system_tags of this PbfListing.
        :rtype: dict(str, dict(str, object))
        """
        return self._system_tags

    @system_tags.setter
    def system_tags(self, system_tags):
        """
        Sets the system_tags of this PbfListing.
        System tags for this resource. Each key is predefined and scoped to a namespace.
        Example: `{\"orcl-cloud\": {\"free-tier-retained\": \"true\"}}`


        :param system_tags: The system_tags of this PbfListing.
        :type: dict(str, dict(str, object))
        """
        self._system_tags = system_tags

    def __repr__(self):
        return formatted_flat_dict(self)

    def __eq__(self, other):
        if other is None:
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not self == other
