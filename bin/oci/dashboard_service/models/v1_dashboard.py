# coding: utf-8
# Copyright (c) 2016, 2023, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.

from .dashboard import Dashboard
from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class V1Dashboard(Dashboard):
    """
    A version 1 dashboard.
    The interpretation of the `config` and `widgets` fields depends on the runtime behavior of the Oracle Cloud Infrastructure Console.
    The sum of the `config` and `widget` fields JSON text representation cannot exceed 200 KB.
    """

    def __init__(self, **kwargs):
        """
        Initializes a new V1Dashboard object with values from keyword arguments. The default value of the :py:attr:`~oci.dashboard_service.models.V1Dashboard.schema_version` attribute
        of this class is ``V1`` and it should not be changed.
        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param id:
            The value to assign to the id property of this V1Dashboard.
        :type id: str

        :param dashboard_group_id:
            The value to assign to the dashboard_group_id property of this V1Dashboard.
        :type dashboard_group_id: str

        :param display_name:
            The value to assign to the display_name property of this V1Dashboard.
        :type display_name: str

        :param description:
            The value to assign to the description property of this V1Dashboard.
        :type description: str

        :param compartment_id:
            The value to assign to the compartment_id property of this V1Dashboard.
        :type compartment_id: str

        :param schema_version:
            The value to assign to the schema_version property of this V1Dashboard.
            Allowed values for this property are: "V1"
        :type schema_version: str

        :param time_created:
            The value to assign to the time_created property of this V1Dashboard.
        :type time_created: datetime

        :param time_updated:
            The value to assign to the time_updated property of this V1Dashboard.
        :type time_updated: datetime

        :param lifecycle_state:
            The value to assign to the lifecycle_state property of this V1Dashboard.
            Allowed values for this property are: "CREATING", "UPDATING", "ACTIVE", "DELETING", "DELETED", "FAILED"
        :type lifecycle_state: str

        :param freeform_tags:
            The value to assign to the freeform_tags property of this V1Dashboard.
        :type freeform_tags: dict(str, str)

        :param defined_tags:
            The value to assign to the defined_tags property of this V1Dashboard.
        :type defined_tags: dict(str, dict(str, object))

        :param system_tags:
            The value to assign to the system_tags property of this V1Dashboard.
        :type system_tags: dict(str, dict(str, object))

        :param config:
            The value to assign to the config property of this V1Dashboard.
        :type config: object

        :param widgets:
            The value to assign to the widgets property of this V1Dashboard.
        :type widgets: list[object]

        """
        self.swagger_types = {
            'id': 'str',
            'dashboard_group_id': 'str',
            'display_name': 'str',
            'description': 'str',
            'compartment_id': 'str',
            'schema_version': 'str',
            'time_created': 'datetime',
            'time_updated': 'datetime',
            'lifecycle_state': 'str',
            'freeform_tags': 'dict(str, str)',
            'defined_tags': 'dict(str, dict(str, object))',
            'system_tags': 'dict(str, dict(str, object))',
            'config': 'object',
            'widgets': 'list[object]'
        }

        self.attribute_map = {
            'id': 'id',
            'dashboard_group_id': 'dashboardGroupId',
            'display_name': 'displayName',
            'description': 'description',
            'compartment_id': 'compartmentId',
            'schema_version': 'schemaVersion',
            'time_created': 'timeCreated',
            'time_updated': 'timeUpdated',
            'lifecycle_state': 'lifecycleState',
            'freeform_tags': 'freeformTags',
            'defined_tags': 'definedTags',
            'system_tags': 'systemTags',
            'config': 'config',
            'widgets': 'widgets'
        }

        self._id = None
        self._dashboard_group_id = None
        self._display_name = None
        self._description = None
        self._compartment_id = None
        self._schema_version = None
        self._time_created = None
        self._time_updated = None
        self._lifecycle_state = None
        self._freeform_tags = None
        self._defined_tags = None
        self._system_tags = None
        self._config = None
        self._widgets = None
        self._schema_version = 'V1'

    @property
    def config(self):
        """
        Gets the config of this V1Dashboard.
        The dashboard configuration. For example, the layout and widget placement.


        :return: The config of this V1Dashboard.
        :rtype: object
        """
        return self._config

    @config.setter
    def config(self, config):
        """
        Sets the config of this V1Dashboard.
        The dashboard configuration. For example, the layout and widget placement.


        :param config: The config of this V1Dashboard.
        :type: object
        """
        self._config = config

    @property
    def widgets(self):
        """
        **[Required]** Gets the widgets of this V1Dashboard.
        The visualization building blocks of the dashboard.


        :return: The widgets of this V1Dashboard.
        :rtype: list[object]
        """
        return self._widgets

    @widgets.setter
    def widgets(self, widgets):
        """
        Sets the widgets of this V1Dashboard.
        The visualization building blocks of the dashboard.


        :param widgets: The widgets of this V1Dashboard.
        :type: list[object]
        """
        self._widgets = widgets

    def __repr__(self):
        return formatted_flat_dict(self)

    def __eq__(self, other):
        if other is None:
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not self == other
