# coding: utf-8
# Copyright (c) 2016, 2023, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.


from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class CreateSkillParameterDetails(object):
    """
    Properties that are required to create a Skill Parameter.
    """

    #: A constant which can be used with the type property of a CreateSkillParameterDetails.
    #: This constant has a value of "STRING"
    TYPE_STRING = "STRING"

    #: A constant which can be used with the type property of a CreateSkillParameterDetails.
    #: This constant has a value of "INTEGER"
    TYPE_INTEGER = "INTEGER"

    #: A constant which can be used with the type property of a CreateSkillParameterDetails.
    #: This constant has a value of "FLOAT"
    TYPE_FLOAT = "FLOAT"

    #: A constant which can be used with the type property of a CreateSkillParameterDetails.
    #: This constant has a value of "BOOLEAN"
    TYPE_BOOLEAN = "BOOLEAN"

    #: A constant which can be used with the type property of a CreateSkillParameterDetails.
    #: This constant has a value of "SECURE"
    TYPE_SECURE = "SECURE"

    def __init__(self, **kwargs):
        """
        Initializes a new CreateSkillParameterDetails object with values from keyword arguments.
        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param name:
            The value to assign to the name property of this CreateSkillParameterDetails.
        :type name: str

        :param display_name:
            The value to assign to the display_name property of this CreateSkillParameterDetails.
        :type display_name: str

        :param description:
            The value to assign to the description property of this CreateSkillParameterDetails.
        :type description: str

        :param type:
            The value to assign to the type property of this CreateSkillParameterDetails.
            Allowed values for this property are: "STRING", "INTEGER", "FLOAT", "BOOLEAN", "SECURE"
        :type type: str

        :param value:
            The value to assign to the value property of this CreateSkillParameterDetails.
        :type value: str

        """
        self.swagger_types = {
            'name': 'str',
            'display_name': 'str',
            'description': 'str',
            'type': 'str',
            'value': 'str'
        }

        self.attribute_map = {
            'name': 'name',
            'display_name': 'displayName',
            'description': 'description',
            'type': 'type',
            'value': 'value'
        }

        self._name = None
        self._display_name = None
        self._description = None
        self._type = None
        self._value = None

    @property
    def name(self):
        """
        **[Required]** Gets the name of this CreateSkillParameterDetails.
        The Parameter name.  This must be unique within the parent resource.


        :return: The name of this CreateSkillParameterDetails.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """
        Sets the name of this CreateSkillParameterDetails.
        The Parameter name.  This must be unique within the parent resource.


        :param name: The name of this CreateSkillParameterDetails.
        :type: str
        """
        self._name = name

    @property
    def display_name(self):
        """
        **[Required]** Gets the display_name of this CreateSkillParameterDetails.
        The display name for the Parameter.


        :return: The display_name of this CreateSkillParameterDetails.
        :rtype: str
        """
        return self._display_name

    @display_name.setter
    def display_name(self, display_name):
        """
        Sets the display_name of this CreateSkillParameterDetails.
        The display name for the Parameter.


        :param display_name: The display_name of this CreateSkillParameterDetails.
        :type: str
        """
        self._display_name = display_name

    @property
    def description(self):
        """
        Gets the description of this CreateSkillParameterDetails.
        A description of the Parameter.


        :return: The description of this CreateSkillParameterDetails.
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        """
        Sets the description of this CreateSkillParameterDetails.
        A description of the Parameter.


        :param description: The description of this CreateSkillParameterDetails.
        :type: str
        """
        self._description = description

    @property
    def type(self):
        """
        **[Required]** Gets the type of this CreateSkillParameterDetails.
        The value type.

        Allowed values for this property are: "STRING", "INTEGER", "FLOAT", "BOOLEAN", "SECURE"


        :return: The type of this CreateSkillParameterDetails.
        :rtype: str
        """
        return self._type

    @type.setter
    def type(self, type):
        """
        Sets the type of this CreateSkillParameterDetails.
        The value type.


        :param type: The type of this CreateSkillParameterDetails.
        :type: str
        """
        allowed_values = ["STRING", "INTEGER", "FLOAT", "BOOLEAN", "SECURE"]
        if not value_allowed_none_or_none_sentinel(type, allowed_values):
            raise ValueError(
                "Invalid value for `type`, must be None or one of {0}"
                .format(allowed_values)
            )
        self._type = type

    @property
    def value(self):
        """
        **[Required]** Gets the value of this CreateSkillParameterDetails.
        The current value.  The value will be interpreted based on the `type`.


        :return: The value of this CreateSkillParameterDetails.
        :rtype: str
        """
        return self._value

    @value.setter
    def value(self, value):
        """
        Sets the value of this CreateSkillParameterDetails.
        The current value.  The value will be interpreted based on the `type`.


        :param value: The value of this CreateSkillParameterDetails.
        :type: str
        """
        self._value = value

    def __repr__(self):
        return formatted_flat_dict(self)

    def __eq__(self, other):
        if other is None:
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not self == other
