# coding: utf-8
# Copyright (c) 2016, 2023, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.


from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class UserPhotos(object):
    """
    URLs of photos for the User
    """

    #: A constant which can be used with the type property of a UserPhotos.
    #: This constant has a value of "photo"
    TYPE_PHOTO = "photo"

    #: A constant which can be used with the type property of a UserPhotos.
    #: This constant has a value of "thumbnail"
    TYPE_THUMBNAIL = "thumbnail"

    def __init__(self, **kwargs):
        """
        Initializes a new UserPhotos object with values from keyword arguments.
        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param value:
            The value to assign to the value property of this UserPhotos.
        :type value: str

        :param display:
            The value to assign to the display property of this UserPhotos.
        :type display: str

        :param type:
            The value to assign to the type property of this UserPhotos.
            Allowed values for this property are: "photo", "thumbnail", 'UNKNOWN_ENUM_VALUE'.
            Any unrecognized values returned by a service will be mapped to 'UNKNOWN_ENUM_VALUE'.
        :type type: str

        :param primary:
            The value to assign to the primary property of this UserPhotos.
        :type primary: bool

        """
        self.swagger_types = {
            'value': 'str',
            'display': 'str',
            'type': 'str',
            'primary': 'bool'
        }

        self.attribute_map = {
            'value': 'value',
            'display': 'display',
            'type': 'type',
            'primary': 'primary'
        }

        self._value = None
        self._display = None
        self._type = None
        self._primary = None

    @property
    def value(self):
        """
        **[Required]** Gets the value of this UserPhotos.
        URL of a photo for the User

        **SCIM++ Properties:**
         - idcsSearchable: false
         - multiValued: false
         - mutability: readWrite
         - required: true
         - returned: default
         - type: reference
         - uniqueness: none


        :return: The value of this UserPhotos.
        :rtype: str
        """
        return self._value

    @value.setter
    def value(self, value):
        """
        Sets the value of this UserPhotos.
        URL of a photo for the User

        **SCIM++ Properties:**
         - idcsSearchable: false
         - multiValued: false
         - mutability: readWrite
         - required: true
         - returned: default
         - type: reference
         - uniqueness: none


        :param value: The value of this UserPhotos.
        :type: str
        """
        self._value = value

    @property
    def display(self):
        """
        Gets the display of this UserPhotos.
        A human readable name, primarily used for display purposes.

        **SCIM++ Properties:**
         - idcsSearchable: false
         - multiValued: false
         - mutability: readWrite
         - required: false
         - returned: default
         - type: string
         - uniqueness: none


        :return: The display of this UserPhotos.
        :rtype: str
        """
        return self._display

    @display.setter
    def display(self, display):
        """
        Sets the display of this UserPhotos.
        A human readable name, primarily used for display purposes.

        **SCIM++ Properties:**
         - idcsSearchable: false
         - multiValued: false
         - mutability: readWrite
         - required: false
         - returned: default
         - type: string
         - uniqueness: none


        :param display: The display of this UserPhotos.
        :type: str
        """
        self._display = display

    @property
    def type(self):
        """
        **[Required]** Gets the type of this UserPhotos.
        A label indicating the attribute's function; e.g., 'photo' or 'thumbnail'.

        **SCIM++ Properties:**
         - idcsSearchable: false
         - multiValued: false
         - mutability: readWrite
         - required: true
         - returned: default
         - type: string
         - uniqueness: none

        Allowed values for this property are: "photo", "thumbnail", 'UNKNOWN_ENUM_VALUE'.
        Any unrecognized values returned by a service will be mapped to 'UNKNOWN_ENUM_VALUE'.


        :return: The type of this UserPhotos.
        :rtype: str
        """
        return self._type

    @type.setter
    def type(self, type):
        """
        Sets the type of this UserPhotos.
        A label indicating the attribute's function; e.g., 'photo' or 'thumbnail'.

        **SCIM++ Properties:**
         - idcsSearchable: false
         - multiValued: false
         - mutability: readWrite
         - required: true
         - returned: default
         - type: string
         - uniqueness: none


        :param type: The type of this UserPhotos.
        :type: str
        """
        allowed_values = ["photo", "thumbnail"]
        if not value_allowed_none_or_none_sentinel(type, allowed_values):
            type = 'UNKNOWN_ENUM_VALUE'
        self._type = type

    @property
    def primary(self):
        """
        Gets the primary of this UserPhotos.
        A Boolean value indicating the 'primary' or preferred attribute value for this attribute, e.g., the preferred photo or thumbnail. The primary attribute value 'true' MUST appear no more than once.

        **SCIM++ Properties:**
         - idcsSearchable: false
         - multiValued: false
         - mutability: readWrite
         - required: false
         - returned: default
         - type: boolean
         - uniqueness: none


        :return: The primary of this UserPhotos.
        :rtype: bool
        """
        return self._primary

    @primary.setter
    def primary(self, primary):
        """
        Sets the primary of this UserPhotos.
        A Boolean value indicating the 'primary' or preferred attribute value for this attribute, e.g., the preferred photo or thumbnail. The primary attribute value 'true' MUST appear no more than once.

        **SCIM++ Properties:**
         - idcsSearchable: false
         - multiValued: false
         - mutability: readWrite
         - required: false
         - returned: default
         - type: boolean
         - uniqueness: none


        :param primary: The primary of this UserPhotos.
        :type: bool
        """
        self._primary = primary

    def __repr__(self):
        return formatted_flat_dict(self)

    def __eq__(self, other):
        if other is None:
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not self == other
