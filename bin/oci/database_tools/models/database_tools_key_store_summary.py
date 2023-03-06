# coding: utf-8
# Copyright (c) 2016, 2023, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.


from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class DatabaseToolsKeyStoreSummary(object):
    """
    The key store secrets.
    """

    #: A constant which can be used with the key_store_type property of a DatabaseToolsKeyStoreSummary.
    #: This constant has a value of "JAVA_KEY_STORE"
    KEY_STORE_TYPE_JAVA_KEY_STORE = "JAVA_KEY_STORE"

    #: A constant which can be used with the key_store_type property of a DatabaseToolsKeyStoreSummary.
    #: This constant has a value of "JAVA_TRUST_STORE"
    KEY_STORE_TYPE_JAVA_TRUST_STORE = "JAVA_TRUST_STORE"

    #: A constant which can be used with the key_store_type property of a DatabaseToolsKeyStoreSummary.
    #: This constant has a value of "PKCS12"
    KEY_STORE_TYPE_PKCS12 = "PKCS12"

    #: A constant which can be used with the key_store_type property of a DatabaseToolsKeyStoreSummary.
    #: This constant has a value of "SSO"
    KEY_STORE_TYPE_SSO = "SSO"

    def __init__(self, **kwargs):
        """
        Initializes a new DatabaseToolsKeyStoreSummary object with values from keyword arguments.
        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param key_store_type:
            The value to assign to the key_store_type property of this DatabaseToolsKeyStoreSummary.
            Allowed values for this property are: "JAVA_KEY_STORE", "JAVA_TRUST_STORE", "PKCS12", "SSO", 'UNKNOWN_ENUM_VALUE'.
            Any unrecognized values returned by a service will be mapped to 'UNKNOWN_ENUM_VALUE'.
        :type key_store_type: str

        :param key_store_content:
            The value to assign to the key_store_content property of this DatabaseToolsKeyStoreSummary.
        :type key_store_content: oci.database_tools.models.DatabaseToolsKeyStoreContentSummary

        :param key_store_password:
            The value to assign to the key_store_password property of this DatabaseToolsKeyStoreSummary.
        :type key_store_password: oci.database_tools.models.DatabaseToolsKeyStorePasswordSummary

        """
        self.swagger_types = {
            'key_store_type': 'str',
            'key_store_content': 'DatabaseToolsKeyStoreContentSummary',
            'key_store_password': 'DatabaseToolsKeyStorePasswordSummary'
        }

        self.attribute_map = {
            'key_store_type': 'keyStoreType',
            'key_store_content': 'keyStoreContent',
            'key_store_password': 'keyStorePassword'
        }

        self._key_store_type = None
        self._key_store_content = None
        self._key_store_password = None

    @property
    def key_store_type(self):
        """
        Gets the key_store_type of this DatabaseToolsKeyStoreSummary.
        The key store type.

        Allowed values for this property are: "JAVA_KEY_STORE", "JAVA_TRUST_STORE", "PKCS12", "SSO", 'UNKNOWN_ENUM_VALUE'.
        Any unrecognized values returned by a service will be mapped to 'UNKNOWN_ENUM_VALUE'.


        :return: The key_store_type of this DatabaseToolsKeyStoreSummary.
        :rtype: str
        """
        return self._key_store_type

    @key_store_type.setter
    def key_store_type(self, key_store_type):
        """
        Sets the key_store_type of this DatabaseToolsKeyStoreSummary.
        The key store type.


        :param key_store_type: The key_store_type of this DatabaseToolsKeyStoreSummary.
        :type: str
        """
        allowed_values = ["JAVA_KEY_STORE", "JAVA_TRUST_STORE", "PKCS12", "SSO"]
        if not value_allowed_none_or_none_sentinel(key_store_type, allowed_values):
            key_store_type = 'UNKNOWN_ENUM_VALUE'
        self._key_store_type = key_store_type

    @property
    def key_store_content(self):
        """
        Gets the key_store_content of this DatabaseToolsKeyStoreSummary.

        :return: The key_store_content of this DatabaseToolsKeyStoreSummary.
        :rtype: oci.database_tools.models.DatabaseToolsKeyStoreContentSummary
        """
        return self._key_store_content

    @key_store_content.setter
    def key_store_content(self, key_store_content):
        """
        Sets the key_store_content of this DatabaseToolsKeyStoreSummary.

        :param key_store_content: The key_store_content of this DatabaseToolsKeyStoreSummary.
        :type: oci.database_tools.models.DatabaseToolsKeyStoreContentSummary
        """
        self._key_store_content = key_store_content

    @property
    def key_store_password(self):
        """
        Gets the key_store_password of this DatabaseToolsKeyStoreSummary.

        :return: The key_store_password of this DatabaseToolsKeyStoreSummary.
        :rtype: oci.database_tools.models.DatabaseToolsKeyStorePasswordSummary
        """
        return self._key_store_password

    @key_store_password.setter
    def key_store_password(self, key_store_password):
        """
        Sets the key_store_password of this DatabaseToolsKeyStoreSummary.

        :param key_store_password: The key_store_password of this DatabaseToolsKeyStoreSummary.
        :type: oci.database_tools.models.DatabaseToolsKeyStorePasswordSummary
        """
        self._key_store_password = key_store_password

    def __repr__(self):
        return formatted_flat_dict(self)

    def __eq__(self, other):
        if other is None:
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not self == other
