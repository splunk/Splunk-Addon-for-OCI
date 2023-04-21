# coding: utf-8
# Copyright (c) 2016, 2023, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.

from .input_details import InputDetails
from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class EmbeddedInputDetails(InputDetails):
    """
    The request body when byte data is provided in detect call, which is Base64 encoded.
    The default type of the data is CSV and can be JSON by setting the 'contentType'.
    """

    #: A constant which can be used with the content_type property of a EmbeddedInputDetails.
    #: This constant has a value of "CSV"
    CONTENT_TYPE_CSV = "CSV"

    #: A constant which can be used with the content_type property of a EmbeddedInputDetails.
    #: This constant has a value of "JSON"
    CONTENT_TYPE_JSON = "JSON"

    def __init__(self, **kwargs):
        """
        Initializes a new EmbeddedInputDetails object with values from keyword arguments. The default value of the :py:attr:`~oci.ai_anomaly_detection.models.EmbeddedInputDetails.input_type` attribute
        of this class is ``BASE64_ENCODED`` and it should not be changed.
        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param input_type:
            The value to assign to the input_type property of this EmbeddedInputDetails.
            Allowed values for this property are: "INLINE", "BASE64_ENCODED", "OBJECT_LIST"
        :type input_type: str

        :param content_type:
            The value to assign to the content_type property of this EmbeddedInputDetails.
            Allowed values for this property are: "CSV", "JSON"
        :type content_type: str

        :param content:
            The value to assign to the content property of this EmbeddedInputDetails.
        :type content: str

        """
        self.swagger_types = {
            'input_type': 'str',
            'content_type': 'str',
            'content': 'str'
        }

        self.attribute_map = {
            'input_type': 'inputType',
            'content_type': 'contentType',
            'content': 'content'
        }

        self._input_type = None
        self._content_type = None
        self._content = None
        self._input_type = 'BASE64_ENCODED'

    @property
    def content_type(self):
        """
        **[Required]** Gets the content_type of this EmbeddedInputDetails.
        Allowed values for this property are: "CSV", "JSON"


        :return: The content_type of this EmbeddedInputDetails.
        :rtype: str
        """
        return self._content_type

    @content_type.setter
    def content_type(self, content_type):
        """
        Sets the content_type of this EmbeddedInputDetails.

        :param content_type: The content_type of this EmbeddedInputDetails.
        :type: str
        """
        allowed_values = ["CSV", "JSON"]
        if not value_allowed_none_or_none_sentinel(content_type, allowed_values):
            raise ValueError(
                "Invalid value for `content_type`, must be None or one of {0}"
                .format(allowed_values)
            )
        self._content_type = content_type

    @property
    def content(self):
        """
        **[Required]** Gets the content of this EmbeddedInputDetails.

        :return: The content of this EmbeddedInputDetails.
        :rtype: str
        """
        return self._content

    @content.setter
    def content(self, content):
        """
        Sets the content of this EmbeddedInputDetails.

        :param content: The content of this EmbeddedInputDetails.
        :type: str
        """
        self._content = content

    def __repr__(self):
        return formatted_flat_dict(self)

    def __eq__(self, other):
        if other is None:
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not self == other
