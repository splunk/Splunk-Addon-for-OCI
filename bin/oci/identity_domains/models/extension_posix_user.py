# coding: utf-8
# Copyright (c) 2016, 2023, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.


from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class ExtensionPosixUser(object):
    """
    POSIX User extension
    """

    def __init__(self, **kwargs):
        """
        Initializes a new ExtensionPosixUser object with values from keyword arguments.
        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param uid_number:
            The value to assign to the uid_number property of this ExtensionPosixUser.
        :type uid_number: int

        :param gid_number:
            The value to assign to the gid_number property of this ExtensionPosixUser.
        :type gid_number: int

        :param gecos:
            The value to assign to the gecos property of this ExtensionPosixUser.
        :type gecos: str

        :param home_directory:
            The value to assign to the home_directory property of this ExtensionPosixUser.
        :type home_directory: str

        :param login_shell:
            The value to assign to the login_shell property of this ExtensionPosixUser.
        :type login_shell: str

        """
        self.swagger_types = {
            'uid_number': 'int',
            'gid_number': 'int',
            'gecos': 'str',
            'home_directory': 'str',
            'login_shell': 'str'
        }

        self.attribute_map = {
            'uid_number': 'uidNumber',
            'gid_number': 'gidNumber',
            'gecos': 'gecos',
            'home_directory': 'homeDirectory',
            'login_shell': 'loginShell'
        }

        self._uid_number = None
        self._gid_number = None
        self._gecos = None
        self._home_directory = None
        self._login_shell = None

    @property
    def uid_number(self):
        """
        Gets the uid_number of this ExtensionPosixUser.
        Integer uniquely identifying a user in a POSIX administrative domain

        **SCIM++ Properties:**
         - idcsSearchable: true
         - multiValued: false
         - mutability: readWrite
         - required: false
         - returned: request
         - type: integer
         - uniqueness: server


        :return: The uid_number of this ExtensionPosixUser.
        :rtype: int
        """
        return self._uid_number

    @uid_number.setter
    def uid_number(self, uid_number):
        """
        Sets the uid_number of this ExtensionPosixUser.
        Integer uniquely identifying a user in a POSIX administrative domain

        **SCIM++ Properties:**
         - idcsSearchable: true
         - multiValued: false
         - mutability: readWrite
         - required: false
         - returned: request
         - type: integer
         - uniqueness: server


        :param uid_number: The uid_number of this ExtensionPosixUser.
        :type: int
        """
        self._uid_number = uid_number

    @property
    def gid_number(self):
        """
        Gets the gid_number of this ExtensionPosixUser.
        Primary Group identifier of the POSIX user

        **SCIM++ Properties:**
         - idcsSearchable: true
         - multiValued: false
         - mutability: readWrite
         - required: false
         - returned: request
         - type: integer
         - uniqueness: none


        :return: The gid_number of this ExtensionPosixUser.
        :rtype: int
        """
        return self._gid_number

    @gid_number.setter
    def gid_number(self, gid_number):
        """
        Sets the gid_number of this ExtensionPosixUser.
        Primary Group identifier of the POSIX user

        **SCIM++ Properties:**
         - idcsSearchable: true
         - multiValued: false
         - mutability: readWrite
         - required: false
         - returned: request
         - type: integer
         - uniqueness: none


        :param gid_number: The gid_number of this ExtensionPosixUser.
        :type: int
        """
        self._gid_number = gid_number

    @property
    def gecos(self):
        """
        Gets the gecos of this ExtensionPosixUser.
        General information about the POSIX account such as their real name and phone number

        **SCIM++ Properties:**
         - caseExact: false
         - multiValued: false
         - mutability: readWrite
         - required: false
         - returned: request
         - type: string
         - uniqueness: none


        :return: The gecos of this ExtensionPosixUser.
        :rtype: str
        """
        return self._gecos

    @gecos.setter
    def gecos(self, gecos):
        """
        Sets the gecos of this ExtensionPosixUser.
        General information about the POSIX account such as their real name and phone number

        **SCIM++ Properties:**
         - caseExact: false
         - multiValued: false
         - mutability: readWrite
         - required: false
         - returned: request
         - type: string
         - uniqueness: none


        :param gecos: The gecos of this ExtensionPosixUser.
        :type: str
        """
        self._gecos = gecos

    @property
    def home_directory(self):
        """
        Gets the home_directory of this ExtensionPosixUser.
        The absolute path to the home directory of the POSIX account

        **SCIM++ Properties:**
         - caseExact: true
         - multiValued: false
         - mutability: readWrite
         - required: false
         - returned: request
         - type: string
         - uniqueness: none


        :return: The home_directory of this ExtensionPosixUser.
        :rtype: str
        """
        return self._home_directory

    @home_directory.setter
    def home_directory(self, home_directory):
        """
        Sets the home_directory of this ExtensionPosixUser.
        The absolute path to the home directory of the POSIX account

        **SCIM++ Properties:**
         - caseExact: true
         - multiValued: false
         - mutability: readWrite
         - required: false
         - returned: request
         - type: string
         - uniqueness: none


        :param home_directory: The home_directory of this ExtensionPosixUser.
        :type: str
        """
        self._home_directory = home_directory

    @property
    def login_shell(self):
        """
        Gets the login_shell of this ExtensionPosixUser.
        The path to the login shell of the POSIX account

        **SCIM++ Properties:**
         - caseExact: true
         - multiValued: false
         - mutability: readWrite
         - required: false
         - returned: request
         - type: string
         - uniqueness: none


        :return: The login_shell of this ExtensionPosixUser.
        :rtype: str
        """
        return self._login_shell

    @login_shell.setter
    def login_shell(self, login_shell):
        """
        Sets the login_shell of this ExtensionPosixUser.
        The path to the login shell of the POSIX account

        **SCIM++ Properties:**
         - caseExact: true
         - multiValued: false
         - mutability: readWrite
         - required: false
         - returned: request
         - type: string
         - uniqueness: none


        :param login_shell: The login_shell of this ExtensionPosixUser.
        :type: str
        """
        self._login_shell = login_shell

    def __repr__(self):
        return formatted_flat_dict(self)

    def __eq__(self, other):
        if other is None:
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not self == other
