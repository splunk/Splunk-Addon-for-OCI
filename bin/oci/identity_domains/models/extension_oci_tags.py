# coding: utf-8
# Copyright (c) 2016, 2023, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.


from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class ExtensionOCITags(object):
    """
    OCI Tags.
    """

    def __init__(self, **kwargs):
        """
        Initializes a new ExtensionOCITags object with values from keyword arguments.
        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param freeform_tags:
            The value to assign to the freeform_tags property of this ExtensionOCITags.
        :type freeform_tags: list[oci.identity_domains.models.FreeformTags]

        :param defined_tags:
            The value to assign to the defined_tags property of this ExtensionOCITags.
        :type defined_tags: list[oci.identity_domains.models.DefinedTags]

        :param tag_slug:
            The value to assign to the tag_slug property of this ExtensionOCITags.
        :type tag_slug: object

        """
        self.swagger_types = {
            'freeform_tags': 'list[FreeformTags]',
            'defined_tags': 'list[DefinedTags]',
            'tag_slug': 'object'
        }

        self.attribute_map = {
            'freeform_tags': 'freeformTags',
            'defined_tags': 'definedTags',
            'tag_slug': 'tagSlug'
        }

        self._freeform_tags = None
        self._defined_tags = None
        self._tag_slug = None

    @property
    def freeform_tags(self):
        """
        Gets the freeform_tags of this ExtensionOCITags.
        OCI Freeform Tags

        **Added In:** 2011192329

        **SCIM++ Properties:**
         - idcsCompositeKey: [key, value]
         - idcsSearchable: true
         - type: complex
         - required: false
         - mutability: readWrite
         - returned: default
         - multiValued: true


        :return: The freeform_tags of this ExtensionOCITags.
        :rtype: list[oci.identity_domains.models.FreeformTags]
        """
        return self._freeform_tags

    @freeform_tags.setter
    def freeform_tags(self, freeform_tags):
        """
        Sets the freeform_tags of this ExtensionOCITags.
        OCI Freeform Tags

        **Added In:** 2011192329

        **SCIM++ Properties:**
         - idcsCompositeKey: [key, value]
         - idcsSearchable: true
         - type: complex
         - required: false
         - mutability: readWrite
         - returned: default
         - multiValued: true


        :param freeform_tags: The freeform_tags of this ExtensionOCITags.
        :type: list[oci.identity_domains.models.FreeformTags]
        """
        self._freeform_tags = freeform_tags

    @property
    def defined_tags(self):
        """
        Gets the defined_tags of this ExtensionOCITags.
        OCI Defined Tags

        **Added In:** 2011192329

        **SCIM++ Properties:**
         - idcsCompositeKey: [namespace, key, value]
         - type: complex
         - idcsSearchable: true
         - required: false
         - mutability: readWrite
         - multiValued: true
         - returned: default


        :return: The defined_tags of this ExtensionOCITags.
        :rtype: list[oci.identity_domains.models.DefinedTags]
        """
        return self._defined_tags

    @defined_tags.setter
    def defined_tags(self, defined_tags):
        """
        Sets the defined_tags of this ExtensionOCITags.
        OCI Defined Tags

        **Added In:** 2011192329

        **SCIM++ Properties:**
         - idcsCompositeKey: [namespace, key, value]
         - type: complex
         - idcsSearchable: true
         - required: false
         - mutability: readWrite
         - multiValued: true
         - returned: default


        :param defined_tags: The defined_tags of this ExtensionOCITags.
        :type: list[oci.identity_domains.models.DefinedTags]
        """
        self._defined_tags = defined_tags

    @property
    def tag_slug(self):
        """
        Gets the tag_slug of this ExtensionOCITags.
        OCI Tag slug

        **Added In:** 2011192329

        **SCIM++ Properties:**
         - type: binary
         - mutability: readOnly
         - returned: request


        :return: The tag_slug of this ExtensionOCITags.
        :rtype: object
        """
        return self._tag_slug

    @tag_slug.setter
    def tag_slug(self, tag_slug):
        """
        Sets the tag_slug of this ExtensionOCITags.
        OCI Tag slug

        **Added In:** 2011192329

        **SCIM++ Properties:**
         - type: binary
         - mutability: readOnly
         - returned: request


        :param tag_slug: The tag_slug of this ExtensionOCITags.
        :type: object
        """
        self._tag_slug = tag_slug

    def __repr__(self):
        return formatted_flat_dict(self)

    def __eq__(self, other):
        if other is None:
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not self == other
