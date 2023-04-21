# coding: utf-8
# Copyright (c) 2016, 2023, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.


from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class UpdateDatabaseToolsConnectionDetails(object):
    """
    The information to be updated.
    """

    #: A constant which can be used with the type property of a UpdateDatabaseToolsConnectionDetails.
    #: This constant has a value of "ORACLE_DATABASE"
    TYPE_ORACLE_DATABASE = "ORACLE_DATABASE"

    #: A constant which can be used with the type property of a UpdateDatabaseToolsConnectionDetails.
    #: This constant has a value of "MYSQL"
    TYPE_MYSQL = "MYSQL"

    def __init__(self, **kwargs):
        """
        Initializes a new UpdateDatabaseToolsConnectionDetails object with values from keyword arguments. This class has the following subclasses and if you are using this class as input
        to a service operations then you should favor using a subclass over the base class:

        * :class:`~oci.database_tools.models.UpdateDatabaseToolsConnectionMySqlDetails`
        * :class:`~oci.database_tools.models.UpdateDatabaseToolsConnectionOracleDatabaseDetails`

        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param display_name:
            The value to assign to the display_name property of this UpdateDatabaseToolsConnectionDetails.
        :type display_name: str

        :param defined_tags:
            The value to assign to the defined_tags property of this UpdateDatabaseToolsConnectionDetails.
        :type defined_tags: dict(str, dict(str, object))

        :param freeform_tags:
            The value to assign to the freeform_tags property of this UpdateDatabaseToolsConnectionDetails.
        :type freeform_tags: dict(str, str)

        :param type:
            The value to assign to the type property of this UpdateDatabaseToolsConnectionDetails.
            Allowed values for this property are: "ORACLE_DATABASE", "MYSQL"
        :type type: str

        """
        self.swagger_types = {
            'display_name': 'str',
            'defined_tags': 'dict(str, dict(str, object))',
            'freeform_tags': 'dict(str, str)',
            'type': 'str'
        }

        self.attribute_map = {
            'display_name': 'displayName',
            'defined_tags': 'definedTags',
            'freeform_tags': 'freeformTags',
            'type': 'type'
        }

        self._display_name = None
        self._defined_tags = None
        self._freeform_tags = None
        self._type = None

    @staticmethod
    def get_subtype(object_dictionary):
        """
        Given the hash representation of a subtype of this class,
        use the info in the hash to return the class of the subtype.
        """
        type = object_dictionary['type']

        if type == 'MYSQL':
            return 'UpdateDatabaseToolsConnectionMySqlDetails'

        if type == 'ORACLE_DATABASE':
            return 'UpdateDatabaseToolsConnectionOracleDatabaseDetails'
        else:
            return 'UpdateDatabaseToolsConnectionDetails'

    @property
    def display_name(self):
        """
        Gets the display_name of this UpdateDatabaseToolsConnectionDetails.
        A user-friendly name. Does not have to be unique, and it's changeable. Avoid entering confidential information.


        :return: The display_name of this UpdateDatabaseToolsConnectionDetails.
        :rtype: str
        """
        return self._display_name

    @display_name.setter
    def display_name(self, display_name):
        """
        Sets the display_name of this UpdateDatabaseToolsConnectionDetails.
        A user-friendly name. Does not have to be unique, and it's changeable. Avoid entering confidential information.


        :param display_name: The display_name of this UpdateDatabaseToolsConnectionDetails.
        :type: str
        """
        self._display_name = display_name

    @property
    def defined_tags(self):
        """
        Gets the defined_tags of this UpdateDatabaseToolsConnectionDetails.
        Defined tags for this resource. Each key is predefined and scoped to a namespace.
        Example: `{\"foo-namespace\": {\"bar-key\": \"value\"}}`


        :return: The defined_tags of this UpdateDatabaseToolsConnectionDetails.
        :rtype: dict(str, dict(str, object))
        """
        return self._defined_tags

    @defined_tags.setter
    def defined_tags(self, defined_tags):
        """
        Sets the defined_tags of this UpdateDatabaseToolsConnectionDetails.
        Defined tags for this resource. Each key is predefined and scoped to a namespace.
        Example: `{\"foo-namespace\": {\"bar-key\": \"value\"}}`


        :param defined_tags: The defined_tags of this UpdateDatabaseToolsConnectionDetails.
        :type: dict(str, dict(str, object))
        """
        self._defined_tags = defined_tags

    @property
    def freeform_tags(self):
        """
        Gets the freeform_tags of this UpdateDatabaseToolsConnectionDetails.
        Simple key-value pair that is applied without any predefined name, type or scope. Exists for cross-compatibility only.
        Example: `{\"bar-key\": \"value\"}`


        :return: The freeform_tags of this UpdateDatabaseToolsConnectionDetails.
        :rtype: dict(str, str)
        """
        return self._freeform_tags

    @freeform_tags.setter
    def freeform_tags(self, freeform_tags):
        """
        Sets the freeform_tags of this UpdateDatabaseToolsConnectionDetails.
        Simple key-value pair that is applied without any predefined name, type or scope. Exists for cross-compatibility only.
        Example: `{\"bar-key\": \"value\"}`


        :param freeform_tags: The freeform_tags of this UpdateDatabaseToolsConnectionDetails.
        :type: dict(str, str)
        """
        self._freeform_tags = freeform_tags

    @property
    def type(self):
        """
        **[Required]** Gets the type of this UpdateDatabaseToolsConnectionDetails.
        The `DatabaseToolsConnection` type.

        Allowed values for this property are: "ORACLE_DATABASE", "MYSQL"


        :return: The type of this UpdateDatabaseToolsConnectionDetails.
        :rtype: str
        """
        return self._type

    @type.setter
    def type(self, type):
        """
        Sets the type of this UpdateDatabaseToolsConnectionDetails.
        The `DatabaseToolsConnection` type.


        :param type: The type of this UpdateDatabaseToolsConnectionDetails.
        :type: str
        """
        allowed_values = ["ORACLE_DATABASE", "MYSQL"]
        if not value_allowed_none_or_none_sentinel(type, allowed_values):
            raise ValueError(
                "Invalid value for `type`, must be None or one of {0}"
                .format(allowed_values)
            )
        self._type = type

    def __repr__(self):
        return formatted_flat_dict(self)

    def __eq__(self, other):
        if other is None:
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not self == other
