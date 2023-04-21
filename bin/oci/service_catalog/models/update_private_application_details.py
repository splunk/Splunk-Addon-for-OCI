# coding: utf-8
# Copyright (c) 2016, 2023, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.


from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class UpdatePrivateApplicationDetails(object):
    """
    The model for the parameters needed to update a private application.
    """

    def __init__(self, **kwargs):
        """
        Initializes a new UpdatePrivateApplicationDetails object with values from keyword arguments.
        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param display_name:
            The value to assign to the display_name property of this UpdatePrivateApplicationDetails.
        :type display_name: str

        :param short_description:
            The value to assign to the short_description property of this UpdatePrivateApplicationDetails.
        :type short_description: str

        :param long_description:
            The value to assign to the long_description property of this UpdatePrivateApplicationDetails.
        :type long_description: str

        :param logo_file_base64_encoded:
            The value to assign to the logo_file_base64_encoded property of this UpdatePrivateApplicationDetails.
        :type logo_file_base64_encoded: str

        :param defined_tags:
            The value to assign to the defined_tags property of this UpdatePrivateApplicationDetails.
        :type defined_tags: dict(str, dict(str, object))

        :param freeform_tags:
            The value to assign to the freeform_tags property of this UpdatePrivateApplicationDetails.
        :type freeform_tags: dict(str, str)

        """
        self.swagger_types = {
            'display_name': 'str',
            'short_description': 'str',
            'long_description': 'str',
            'logo_file_base64_encoded': 'str',
            'defined_tags': 'dict(str, dict(str, object))',
            'freeform_tags': 'dict(str, str)'
        }

        self.attribute_map = {
            'display_name': 'displayName',
            'short_description': 'shortDescription',
            'long_description': 'longDescription',
            'logo_file_base64_encoded': 'logoFileBase64Encoded',
            'defined_tags': 'definedTags',
            'freeform_tags': 'freeformTags'
        }

        self._display_name = None
        self._short_description = None
        self._long_description = None
        self._logo_file_base64_encoded = None
        self._defined_tags = None
        self._freeform_tags = None

    @property
    def display_name(self):
        """
        Gets the display_name of this UpdatePrivateApplicationDetails.
        The name of the private application.


        :return: The display_name of this UpdatePrivateApplicationDetails.
        :rtype: str
        """
        return self._display_name

    @display_name.setter
    def display_name(self, display_name):
        """
        Sets the display_name of this UpdatePrivateApplicationDetails.
        The name of the private application.


        :param display_name: The display_name of this UpdatePrivateApplicationDetails.
        :type: str
        """
        self._display_name = display_name

    @property
    def short_description(self):
        """
        Gets the short_description of this UpdatePrivateApplicationDetails.
        A short description of the private application.


        :return: The short_description of this UpdatePrivateApplicationDetails.
        :rtype: str
        """
        return self._short_description

    @short_description.setter
    def short_description(self, short_description):
        """
        Sets the short_description of this UpdatePrivateApplicationDetails.
        A short description of the private application.


        :param short_description: The short_description of this UpdatePrivateApplicationDetails.
        :type: str
        """
        self._short_description = short_description

    @property
    def long_description(self):
        """
        Gets the long_description of this UpdatePrivateApplicationDetails.
        A long description of the private application.


        :return: The long_description of this UpdatePrivateApplicationDetails.
        :rtype: str
        """
        return self._long_description

    @long_description.setter
    def long_description(self, long_description):
        """
        Sets the long_description of this UpdatePrivateApplicationDetails.
        A long description of the private application.


        :param long_description: The long_description of this UpdatePrivateApplicationDetails.
        :type: str
        """
        self._long_description = long_description

    @property
    def logo_file_base64_encoded(self):
        """
        Gets the logo_file_base64_encoded of this UpdatePrivateApplicationDetails.
        Base64-encoded logo to use as the private application icon.
        Template icon file requirements: PNG format, 50 KB maximum, 130 x 130 pixels.


        :return: The logo_file_base64_encoded of this UpdatePrivateApplicationDetails.
        :rtype: str
        """
        return self._logo_file_base64_encoded

    @logo_file_base64_encoded.setter
    def logo_file_base64_encoded(self, logo_file_base64_encoded):
        """
        Sets the logo_file_base64_encoded of this UpdatePrivateApplicationDetails.
        Base64-encoded logo to use as the private application icon.
        Template icon file requirements: PNG format, 50 KB maximum, 130 x 130 pixels.


        :param logo_file_base64_encoded: The logo_file_base64_encoded of this UpdatePrivateApplicationDetails.
        :type: str
        """
        self._logo_file_base64_encoded = logo_file_base64_encoded

    @property
    def defined_tags(self):
        """
        Gets the defined_tags of this UpdatePrivateApplicationDetails.
        Defined tags for this resource. Each key is predefined and scoped to a namespace.
        Example: `{\"foo-namespace\": {\"bar-key\": \"value\"}}`


        :return: The defined_tags of this UpdatePrivateApplicationDetails.
        :rtype: dict(str, dict(str, object))
        """
        return self._defined_tags

    @defined_tags.setter
    def defined_tags(self, defined_tags):
        """
        Sets the defined_tags of this UpdatePrivateApplicationDetails.
        Defined tags for this resource. Each key is predefined and scoped to a namespace.
        Example: `{\"foo-namespace\": {\"bar-key\": \"value\"}}`


        :param defined_tags: The defined_tags of this UpdatePrivateApplicationDetails.
        :type: dict(str, dict(str, object))
        """
        self._defined_tags = defined_tags

    @property
    def freeform_tags(self):
        """
        Gets the freeform_tags of this UpdatePrivateApplicationDetails.
        Simple key-value pair that is applied without any predefined name, type or scope. Exists for cross-compatibility only.
        Example: `{\"bar-key\": \"value\"}`


        :return: The freeform_tags of this UpdatePrivateApplicationDetails.
        :rtype: dict(str, str)
        """
        return self._freeform_tags

    @freeform_tags.setter
    def freeform_tags(self, freeform_tags):
        """
        Sets the freeform_tags of this UpdatePrivateApplicationDetails.
        Simple key-value pair that is applied without any predefined name, type or scope. Exists for cross-compatibility only.
        Example: `{\"bar-key\": \"value\"}`


        :param freeform_tags: The freeform_tags of this UpdatePrivateApplicationDetails.
        :type: dict(str, str)
        """
        self._freeform_tags = freeform_tags

    def __repr__(self):
        return formatted_flat_dict(self)

    def __eq__(self, other):
        if other is None:
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not self == other
