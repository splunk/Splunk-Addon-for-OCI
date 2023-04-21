# coding: utf-8
# Copyright (c) 2016, 2023, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.

from .external_db_system_discovery_connector import ExternalDbSystemDiscoveryConnector
from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class ExternalDbSystemDiscoveryMacsConnector(ExternalDbSystemDiscoveryConnector):
    """
    The details of an external DB system connector that uses the
    `Management Agent Cloud Service (MACS)`__
    to connect to an external DB system component.

    __ https://docs.cloud.oracle.com/iaas/management-agents/index.html
    """

    def __init__(self, **kwargs):
        """
        Initializes a new ExternalDbSystemDiscoveryMacsConnector object with values from keyword arguments. The default value of the :py:attr:`~oci.database_management.models.ExternalDbSystemDiscoveryMacsConnector.connector_type` attribute
        of this class is ``MACS`` and it should not be changed.
        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param connector_type:
            The value to assign to the connector_type property of this ExternalDbSystemDiscoveryMacsConnector.
            Allowed values for this property are: "MACS"
        :type connector_type: str

        :param display_name:
            The value to assign to the display_name property of this ExternalDbSystemDiscoveryMacsConnector.
        :type display_name: str

        :param connection_status:
            The value to assign to the connection_status property of this ExternalDbSystemDiscoveryMacsConnector.
        :type connection_status: str

        :param connection_failure_message:
            The value to assign to the connection_failure_message property of this ExternalDbSystemDiscoveryMacsConnector.
        :type connection_failure_message: str

        :param time_connection_status_last_updated:
            The value to assign to the time_connection_status_last_updated property of this ExternalDbSystemDiscoveryMacsConnector.
        :type time_connection_status_last_updated: datetime

        :param agent_id:
            The value to assign to the agent_id property of this ExternalDbSystemDiscoveryMacsConnector.
        :type agent_id: str

        :param connection_info:
            The value to assign to the connection_info property of this ExternalDbSystemDiscoveryMacsConnector.
        :type connection_info: oci.database_management.models.ExternalDbSystemConnectionInfo

        """
        self.swagger_types = {
            'connector_type': 'str',
            'display_name': 'str',
            'connection_status': 'str',
            'connection_failure_message': 'str',
            'time_connection_status_last_updated': 'datetime',
            'agent_id': 'str',
            'connection_info': 'ExternalDbSystemConnectionInfo'
        }

        self.attribute_map = {
            'connector_type': 'connectorType',
            'display_name': 'displayName',
            'connection_status': 'connectionStatus',
            'connection_failure_message': 'connectionFailureMessage',
            'time_connection_status_last_updated': 'timeConnectionStatusLastUpdated',
            'agent_id': 'agentId',
            'connection_info': 'connectionInfo'
        }

        self._connector_type = None
        self._display_name = None
        self._connection_status = None
        self._connection_failure_message = None
        self._time_connection_status_last_updated = None
        self._agent_id = None
        self._connection_info = None
        self._connector_type = 'MACS'

    @property
    def agent_id(self):
        """
        **[Required]** Gets the agent_id of this ExternalDbSystemDiscoveryMacsConnector.
        The `OCID`__ of the management agent
        used for the external DB system connector.

        __ https://docs.cloud.oracle.com/Content/General/Concepts/identifiers.htm


        :return: The agent_id of this ExternalDbSystemDiscoveryMacsConnector.
        :rtype: str
        """
        return self._agent_id

    @agent_id.setter
    def agent_id(self, agent_id):
        """
        Sets the agent_id of this ExternalDbSystemDiscoveryMacsConnector.
        The `OCID`__ of the management agent
        used for the external DB system connector.

        __ https://docs.cloud.oracle.com/Content/General/Concepts/identifiers.htm


        :param agent_id: The agent_id of this ExternalDbSystemDiscoveryMacsConnector.
        :type: str
        """
        self._agent_id = agent_id

    @property
    def connection_info(self):
        """
        Gets the connection_info of this ExternalDbSystemDiscoveryMacsConnector.

        :return: The connection_info of this ExternalDbSystemDiscoveryMacsConnector.
        :rtype: oci.database_management.models.ExternalDbSystemConnectionInfo
        """
        return self._connection_info

    @connection_info.setter
    def connection_info(self, connection_info):
        """
        Sets the connection_info of this ExternalDbSystemDiscoveryMacsConnector.

        :param connection_info: The connection_info of this ExternalDbSystemDiscoveryMacsConnector.
        :type: oci.database_management.models.ExternalDbSystemConnectionInfo
        """
        self._connection_info = connection_info

    def __repr__(self):
        return formatted_flat_dict(self)

    def __eq__(self, other):
        if other is None:
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not self == other
