# coding: utf-8
# Copyright (c) 2016, 2023, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.


from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class UserExtSyncedFromApp(object):
    """
    Managed App or an Identity Source from where the user is synced. If enabled, this Managed App or Identity Source can be used for performing delegated authentication.

    **Added In:** 18.2.6

    **SCIM++ Properties:**
    - idcsCompositeKey: [value]
    - idcsSearchable: true
    - multiValued: false
    - mutability: readOnly
    - required: false
    - returned: default
    - type: complex
    - uniqueness: none
    """

    #: A constant which can be used with the type property of a UserExtSyncedFromApp.
    #: This constant has a value of "IdentitySource"
    TYPE_IDENTITY_SOURCE = "IdentitySource"

    #: A constant which can be used with the type property of a UserExtSyncedFromApp.
    #: This constant has a value of "App"
    TYPE_APP = "App"

    #: A constant which can be used with the type property of a UserExtSyncedFromApp.
    #: This constant has a value of "IdentityProvider"
    TYPE_IDENTITY_PROVIDER = "IdentityProvider"

    def __init__(self, **kwargs):
        """
        Initializes a new UserExtSyncedFromApp object with values from keyword arguments.
        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param value:
            The value to assign to the value property of this UserExtSyncedFromApp.
        :type value: str

        :param type:
            The value to assign to the type property of this UserExtSyncedFromApp.
            Allowed values for this property are: "IdentitySource", "App", "IdentityProvider", 'UNKNOWN_ENUM_VALUE'.
            Any unrecognized values returned by a service will be mapped to 'UNKNOWN_ENUM_VALUE'.
        :type type: str

        :param ref:
            The value to assign to the ref property of this UserExtSyncedFromApp.
        :type ref: str

        :param display:
            The value to assign to the display property of this UserExtSyncedFromApp.
        :type display: str

        """
        self.swagger_types = {
            'value': 'str',
            'type': 'str',
            'ref': 'str',
            'display': 'str'
        }

        self.attribute_map = {
            'value': 'value',
            'type': 'type',
            'ref': '$ref',
            'display': 'display'
        }

        self._value = None
        self._type = None
        self._ref = None
        self._display = None

    @property
    def value(self):
        """
        **[Required]** Gets the value of this UserExtSyncedFromApp.
        App identifier

        **Added In:** 18.2.6

        **SCIM++ Properties:**
         - caseExact: true
         - idcsSearchable: true
         - multiValued: false
         - mutability: readWrite
         - required: true
         - returned: default
         - type: string
         - uniqueness: none


        :return: The value of this UserExtSyncedFromApp.
        :rtype: str
        """
        return self._value

    @value.setter
    def value(self, value):
        """
        Sets the value of this UserExtSyncedFromApp.
        App identifier

        **Added In:** 18.2.6

        **SCIM++ Properties:**
         - caseExact: true
         - idcsSearchable: true
         - multiValued: false
         - mutability: readWrite
         - required: true
         - returned: default
         - type: string
         - uniqueness: none


        :param value: The value of this UserExtSyncedFromApp.
        :type: str
        """
        self._value = value

    @property
    def type(self):
        """
        **[Required]** Gets the type of this UserExtSyncedFromApp.
        A label that indicates whether this is an App or IdentitySource.

        **Added In:** 18.2.6

        **SCIM++ Properties:**
         - idcsDefaultValue: IdentitySource
         - idcsSearchable: false
         - multiValued: false
         - mutability: immutable
         - required: true
         - returned: default
         - type: string
         - uniqueness: none

        Allowed values for this property are: "IdentitySource", "App", "IdentityProvider", 'UNKNOWN_ENUM_VALUE'.
        Any unrecognized values returned by a service will be mapped to 'UNKNOWN_ENUM_VALUE'.


        :return: The type of this UserExtSyncedFromApp.
        :rtype: str
        """
        return self._type

    @type.setter
    def type(self, type):
        """
        Sets the type of this UserExtSyncedFromApp.
        A label that indicates whether this is an App or IdentitySource.

        **Added In:** 18.2.6

        **SCIM++ Properties:**
         - idcsDefaultValue: IdentitySource
         - idcsSearchable: false
         - multiValued: false
         - mutability: immutable
         - required: true
         - returned: default
         - type: string
         - uniqueness: none


        :param type: The type of this UserExtSyncedFromApp.
        :type: str
        """
        allowed_values = ["IdentitySource", "App", "IdentityProvider"]
        if not value_allowed_none_or_none_sentinel(type, allowed_values):
            type = 'UNKNOWN_ENUM_VALUE'
        self._type = type

    @property
    def ref(self):
        """
        Gets the ref of this UserExtSyncedFromApp.
        App URI

        **Added In:** 18.2.6

        **SCIM++ Properties:**
         - idcsSearchable: false
         - multiValued: false
         - mutability: readOnly
         - required: false
         - returned: default
         - type: reference
         - uniqueness: none


        :return: The ref of this UserExtSyncedFromApp.
        :rtype: str
        """
        return self._ref

    @ref.setter
    def ref(self, ref):
        """
        Sets the ref of this UserExtSyncedFromApp.
        App URI

        **Added In:** 18.2.6

        **SCIM++ Properties:**
         - idcsSearchable: false
         - multiValued: false
         - mutability: readOnly
         - required: false
         - returned: default
         - type: reference
         - uniqueness: none


        :param ref: The ref of this UserExtSyncedFromApp.
        :type: str
        """
        self._ref = ref

    @property
    def display(self):
        """
        Gets the display of this UserExtSyncedFromApp.
        App Display Name

        **Added In:** 18.2.6

        **SCIM++ Properties:**
         - caseExact: true
         - idcsSearchable: true
         - multiValued: false
         - mutability: readOnly
         - required: false
         - returned: default
         - type: string
         - uniqueness: none


        :return: The display of this UserExtSyncedFromApp.
        :rtype: str
        """
        return self._display

    @display.setter
    def display(self, display):
        """
        Sets the display of this UserExtSyncedFromApp.
        App Display Name

        **Added In:** 18.2.6

        **SCIM++ Properties:**
         - caseExact: true
         - idcsSearchable: true
         - multiValued: false
         - mutability: readOnly
         - required: false
         - returned: default
         - type: string
         - uniqueness: none


        :param display: The display of this UserExtSyncedFromApp.
        :type: str
        """
        self._display = display

    def __repr__(self):
        return formatted_flat_dict(self)

    def __eq__(self, other):
        if other is None:
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not self == other
