# coding: utf-8
# Copyright (c) 2016, 2023, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.


from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class UpdateDataGuardAssociationDetails(object):
    """
    The configuration details for updating a Data Guard association for a database.

    **Warning:** Oracle recommends that you avoid using any confidential information when you supply string values using the API.
    """

    #: A constant which can be used with the protection_mode property of a UpdateDataGuardAssociationDetails.
    #: This constant has a value of "MAXIMUM_AVAILABILITY"
    PROTECTION_MODE_MAXIMUM_AVAILABILITY = "MAXIMUM_AVAILABILITY"

    #: A constant which can be used with the protection_mode property of a UpdateDataGuardAssociationDetails.
    #: This constant has a value of "MAXIMUM_PERFORMANCE"
    PROTECTION_MODE_MAXIMUM_PERFORMANCE = "MAXIMUM_PERFORMANCE"

    #: A constant which can be used with the protection_mode property of a UpdateDataGuardAssociationDetails.
    #: This constant has a value of "MAXIMUM_PROTECTION"
    PROTECTION_MODE_MAXIMUM_PROTECTION = "MAXIMUM_PROTECTION"

    #: A constant which can be used with the transport_type property of a UpdateDataGuardAssociationDetails.
    #: This constant has a value of "SYNC"
    TRANSPORT_TYPE_SYNC = "SYNC"

    #: A constant which can be used with the transport_type property of a UpdateDataGuardAssociationDetails.
    #: This constant has a value of "ASYNC"
    TRANSPORT_TYPE_ASYNC = "ASYNC"

    #: A constant which can be used with the transport_type property of a UpdateDataGuardAssociationDetails.
    #: This constant has a value of "FASTSYNC"
    TRANSPORT_TYPE_FASTSYNC = "FASTSYNC"

    def __init__(self, **kwargs):
        """
        Initializes a new UpdateDataGuardAssociationDetails object with values from keyword arguments.
        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param database_admin_password:
            The value to assign to the database_admin_password property of this UpdateDataGuardAssociationDetails.
        :type database_admin_password: str

        :param protection_mode:
            The value to assign to the protection_mode property of this UpdateDataGuardAssociationDetails.
            Allowed values for this property are: "MAXIMUM_AVAILABILITY", "MAXIMUM_PERFORMANCE", "MAXIMUM_PROTECTION"
        :type protection_mode: str

        :param transport_type:
            The value to assign to the transport_type property of this UpdateDataGuardAssociationDetails.
            Allowed values for this property are: "SYNC", "ASYNC", "FASTSYNC"
        :type transport_type: str

        :param is_active_data_guard_enabled:
            The value to assign to the is_active_data_guard_enabled property of this UpdateDataGuardAssociationDetails.
        :type is_active_data_guard_enabled: bool

        """
        self.swagger_types = {
            'database_admin_password': 'str',
            'protection_mode': 'str',
            'transport_type': 'str',
            'is_active_data_guard_enabled': 'bool'
        }

        self.attribute_map = {
            'database_admin_password': 'databaseAdminPassword',
            'protection_mode': 'protectionMode',
            'transport_type': 'transportType',
            'is_active_data_guard_enabled': 'isActiveDataGuardEnabled'
        }

        self._database_admin_password = None
        self._protection_mode = None
        self._transport_type = None
        self._is_active_data_guard_enabled = None

    @property
    def database_admin_password(self):
        """
        Gets the database_admin_password of this UpdateDataGuardAssociationDetails.
        A strong password for the 'SYS', 'SYSTEM', and 'PDB Admin' users to apply during standby creation.

        The password must contain no fewer than nine characters and include:

        * At least two uppercase characters.

        * At least two lowercase characters.

        * At least two numeric characters.

        * At least two special characters. Valid special characters include \"_\", \"#\", and \"-\" only.

        **The password MUST be the same as the primary admin password.**


        :return: The database_admin_password of this UpdateDataGuardAssociationDetails.
        :rtype: str
        """
        return self._database_admin_password

    @database_admin_password.setter
    def database_admin_password(self, database_admin_password):
        """
        Sets the database_admin_password of this UpdateDataGuardAssociationDetails.
        A strong password for the 'SYS', 'SYSTEM', and 'PDB Admin' users to apply during standby creation.

        The password must contain no fewer than nine characters and include:

        * At least two uppercase characters.

        * At least two lowercase characters.

        * At least two numeric characters.

        * At least two special characters. Valid special characters include \"_\", \"#\", and \"-\" only.

        **The password MUST be the same as the primary admin password.**


        :param database_admin_password: The database_admin_password of this UpdateDataGuardAssociationDetails.
        :type: str
        """
        self._database_admin_password = database_admin_password

    @property
    def protection_mode(self):
        """
        Gets the protection_mode of this UpdateDataGuardAssociationDetails.
        The protection mode for the Data Guard association's primary and standby database. For more information, see
        `Oracle Data Guard Protection Modes`__
        in the Oracle Data Guard documentation.

        __ http://docs.oracle.com/database/122/SBYDB/oracle-data-guard-protection-modes.htm#SBYDB02000

        Allowed values for this property are: "MAXIMUM_AVAILABILITY", "MAXIMUM_PERFORMANCE", "MAXIMUM_PROTECTION"


        :return: The protection_mode of this UpdateDataGuardAssociationDetails.
        :rtype: str
        """
        return self._protection_mode

    @protection_mode.setter
    def protection_mode(self, protection_mode):
        """
        Sets the protection_mode of this UpdateDataGuardAssociationDetails.
        The protection mode for the Data Guard association's primary and standby database. For more information, see
        `Oracle Data Guard Protection Modes`__
        in the Oracle Data Guard documentation.

        __ http://docs.oracle.com/database/122/SBYDB/oracle-data-guard-protection-modes.htm#SBYDB02000


        :param protection_mode: The protection_mode of this UpdateDataGuardAssociationDetails.
        :type: str
        """
        allowed_values = ["MAXIMUM_AVAILABILITY", "MAXIMUM_PERFORMANCE", "MAXIMUM_PROTECTION"]
        if not value_allowed_none_or_none_sentinel(protection_mode, allowed_values):
            raise ValueError(
                "Invalid value for `protection_mode`, must be None or one of {0}"
                .format(allowed_values)
            )
        self._protection_mode = protection_mode

    @property
    def transport_type(self):
        """
        Gets the transport_type of this UpdateDataGuardAssociationDetails.
        The redo transport type to use for this Data Guard association.  Valid values depend on the specified 'protectionMode':
        * MAXIMUM_AVAILABILITY - Use SYNC or FASTSYNC
        * MAXIMUM_PERFORMANCE - Use ASYNC
        * MAXIMUM_PROTECTION - Use SYNC

        For more information, see
        `Redo Transport Services`__
        in the Oracle Data Guard documentation.

        __ http://docs.oracle.com/database/122/SBYDB/oracle-data-guard-redo-transport-services.htm#SBYDB00400

        Allowed values for this property are: "SYNC", "ASYNC", "FASTSYNC"


        :return: The transport_type of this UpdateDataGuardAssociationDetails.
        :rtype: str
        """
        return self._transport_type

    @transport_type.setter
    def transport_type(self, transport_type):
        """
        Sets the transport_type of this UpdateDataGuardAssociationDetails.
        The redo transport type to use for this Data Guard association.  Valid values depend on the specified 'protectionMode':
        * MAXIMUM_AVAILABILITY - Use SYNC or FASTSYNC
        * MAXIMUM_PERFORMANCE - Use ASYNC
        * MAXIMUM_PROTECTION - Use SYNC

        For more information, see
        `Redo Transport Services`__
        in the Oracle Data Guard documentation.

        __ http://docs.oracle.com/database/122/SBYDB/oracle-data-guard-redo-transport-services.htm#SBYDB00400


        :param transport_type: The transport_type of this UpdateDataGuardAssociationDetails.
        :type: str
        """
        allowed_values = ["SYNC", "ASYNC", "FASTSYNC"]
        if not value_allowed_none_or_none_sentinel(transport_type, allowed_values):
            raise ValueError(
                "Invalid value for `transport_type`, must be None or one of {0}"
                .format(allowed_values)
            )
        self._transport_type = transport_type

    @property
    def is_active_data_guard_enabled(self):
        """
        Gets the is_active_data_guard_enabled of this UpdateDataGuardAssociationDetails.
        True if active Data Guard is enabled. Update this parameter to change the Data Guard setting.


        :return: The is_active_data_guard_enabled of this UpdateDataGuardAssociationDetails.
        :rtype: bool
        """
        return self._is_active_data_guard_enabled

    @is_active_data_guard_enabled.setter
    def is_active_data_guard_enabled(self, is_active_data_guard_enabled):
        """
        Sets the is_active_data_guard_enabled of this UpdateDataGuardAssociationDetails.
        True if active Data Guard is enabled. Update this parameter to change the Data Guard setting.


        :param is_active_data_guard_enabled: The is_active_data_guard_enabled of this UpdateDataGuardAssociationDetails.
        :type: bool
        """
        self._is_active_data_guard_enabled = is_active_data_guard_enabled

    def __repr__(self):
        return formatted_flat_dict(self)

    def __eq__(self, other):
        if other is None:
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not self == other
