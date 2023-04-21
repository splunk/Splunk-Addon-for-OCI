# coding: utf-8
# Copyright (c) 2016, 2023, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.


from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class UserExtLocked(object):
    """
    A complex attribute that indicates an account is locked (blocking new sessions)

    **SCIM++ Properties:**
    - idcsCsvAttributeNameMappings: [[columnHeaderName:Locked, mapsTo:locked.on], [columnHeaderName:Locked Reason, mapsTo:locked.reason], [columnHeaderName:Locked Date, mapsTo:locked.lockDate]]
    - idcsSearchable: false
    - idcsAllowUpdatesInReadOnlyMode: true
    - multiValued: false
    - mutability: readWrite
    - required: false
    - returned: default
    - type: complex
    - uniqueness: none
    """

    def __init__(self, **kwargs):
        """
        Initializes a new UserExtLocked object with values from keyword arguments.
        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param reason:
            The value to assign to the reason property of this UserExtLocked.
        :type reason: int

        :param on:
            The value to assign to the on property of this UserExtLocked.
        :type on: bool

        :param lock_date:
            The value to assign to the lock_date property of this UserExtLocked.
        :type lock_date: str

        :param expired:
            The value to assign to the expired property of this UserExtLocked.
        :type expired: bool

        """
        self.swagger_types = {
            'reason': 'int',
            'on': 'bool',
            'lock_date': 'str',
            'expired': 'bool'
        }

        self.attribute_map = {
            'reason': 'reason',
            'on': 'on',
            'lock_date': 'lockDate',
            'expired': 'expired'
        }

        self._reason = None
        self._on = None
        self._lock_date = None
        self._expired = None

    @property
    def reason(self):
        """
        Gets the reason of this UserExtLocked.
        Indicates the reason for locking. Valid values are: 0 - failed password login attempts, 1 - admin lock, 2 - failed reset password attempts, 3 - failed MFA login attempts, 4 - failed MFA login attempts for federated user, 5 - failed Database login attempts

        **SCIM++ Properties:**
         - idcsSearchable: false
         - multiValued: false
         - mutability: readWrite
         - required: false
         - returned: default
         - type: integer
         - uniqueness: none


        :return: The reason of this UserExtLocked.
        :rtype: int
        """
        return self._reason

    @reason.setter
    def reason(self, reason):
        """
        Sets the reason of this UserExtLocked.
        Indicates the reason for locking. Valid values are: 0 - failed password login attempts, 1 - admin lock, 2 - failed reset password attempts, 3 - failed MFA login attempts, 4 - failed MFA login attempts for federated user, 5 - failed Database login attempts

        **SCIM++ Properties:**
         - idcsSearchable: false
         - multiValued: false
         - mutability: readWrite
         - required: false
         - returned: default
         - type: integer
         - uniqueness: none


        :param reason: The reason of this UserExtLocked.
        :type: int
        """
        self._reason = reason

    @property
    def on(self):
        """
        Gets the on of this UserExtLocked.
        Indicates tat the account is locked

        **SCIM++ Properties:**
         - caseExact: false
         - idcsSearchable: true
         - multiValued: false
         - mutability: readWrite
         - required: false
         - returned: default
         - type: boolean
         - uniqueness: none


        :return: The on of this UserExtLocked.
        :rtype: bool
        """
        return self._on

    @on.setter
    def on(self, on):
        """
        Sets the on of this UserExtLocked.
        Indicates tat the account is locked

        **SCIM++ Properties:**
         - caseExact: false
         - idcsSearchable: true
         - multiValued: false
         - mutability: readWrite
         - required: false
         - returned: default
         - type: boolean
         - uniqueness: none


        :param on: The on of this UserExtLocked.
        :type: bool
        """
        self._on = on

    @property
    def lock_date(self):
        """
        Gets the lock_date of this UserExtLocked.
        The date and time that the current resource was locked

        **SCIM++ Properties:**
         - idcsSearchable: false
         - multiValued: false
         - mutability: readWrite
         - required: false
         - returned: default
         - type: dateTime
         - uniqueness: none


        :return: The lock_date of this UserExtLocked.
        :rtype: str
        """
        return self._lock_date

    @lock_date.setter
    def lock_date(self, lock_date):
        """
        Sets the lock_date of this UserExtLocked.
        The date and time that the current resource was locked

        **SCIM++ Properties:**
         - idcsSearchable: false
         - multiValued: false
         - mutability: readWrite
         - required: false
         - returned: default
         - type: dateTime
         - uniqueness: none


        :param lock_date: The lock_date of this UserExtLocked.
        :type: str
        """
        self._lock_date = lock_date

    @property
    def expired(self):
        """
        Gets the expired of this UserExtLocked.
        Indicates whether user password is expired. If this value is false, password expiry will still be evaluated during user login.

        **Added In:** 20.1.3

        **SCIM++ Properties:**
         - caseExact: false
         - idcsSearchable: false
         - multiValued: false
         - mutability: readWrite
         - required: false
         - returned: request
         - type: boolean
         - uniqueness: none


        :return: The expired of this UserExtLocked.
        :rtype: bool
        """
        return self._expired

    @expired.setter
    def expired(self, expired):
        """
        Sets the expired of this UserExtLocked.
        Indicates whether user password is expired. If this value is false, password expiry will still be evaluated during user login.

        **Added In:** 20.1.3

        **SCIM++ Properties:**
         - caseExact: false
         - idcsSearchable: false
         - multiValued: false
         - mutability: readWrite
         - required: false
         - returned: request
         - type: boolean
         - uniqueness: none


        :param expired: The expired of this UserExtLocked.
        :type: bool
        """
        self._expired = expired

    def __repr__(self):
        return formatted_flat_dict(self)

    def __eq__(self, other):
        if other is None:
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not self == other
