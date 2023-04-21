# coding: utf-8
# Copyright (c) 2016, 2023, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.


from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class ProfileSummary(object):
    """
    The summary of information about the user profiles. It includes details such as profile name, failed login attempts,
    sessions per user, inactive account time, password lock time, user created, target id, and the compartment id.
    """

    def __init__(self, **kwargs):
        """
        Initializes a new ProfileSummary object with values from keyword arguments.
        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param user_assessment_id:
            The value to assign to the user_assessment_id property of this ProfileSummary.
        :type user_assessment_id: str

        :param compartment_id:
            The value to assign to the compartment_id property of this ProfileSummary.
        :type compartment_id: str

        :param target_id:
            The value to assign to the target_id property of this ProfileSummary.
        :type target_id: str

        :param profile_name:
            The value to assign to the profile_name property of this ProfileSummary.
        :type profile_name: str

        :param user_count:
            The value to assign to the user_count property of this ProfileSummary.
        :type user_count: int

        :param failed_login_attempts:
            The value to assign to the failed_login_attempts property of this ProfileSummary.
        :type failed_login_attempts: str

        :param password_verification_function:
            The value to assign to the password_verification_function property of this ProfileSummary.
        :type password_verification_function: str

        :param sessions_per_user:
            The value to assign to the sessions_per_user property of this ProfileSummary.
        :type sessions_per_user: str

        :param inactive_account_time:
            The value to assign to the inactive_account_time property of this ProfileSummary.
        :type inactive_account_time: str

        :param password_lock_time:
            The value to assign to the password_lock_time property of this ProfileSummary.
        :type password_lock_time: str

        :param is_user_created:
            The value to assign to the is_user_created property of this ProfileSummary.
        :type is_user_created: bool

        :param freeform_tags:
            The value to assign to the freeform_tags property of this ProfileSummary.
        :type freeform_tags: dict(str, str)

        :param defined_tags:
            The value to assign to the defined_tags property of this ProfileSummary.
        :type defined_tags: dict(str, dict(str, object))

        """
        self.swagger_types = {
            'user_assessment_id': 'str',
            'compartment_id': 'str',
            'target_id': 'str',
            'profile_name': 'str',
            'user_count': 'int',
            'failed_login_attempts': 'str',
            'password_verification_function': 'str',
            'sessions_per_user': 'str',
            'inactive_account_time': 'str',
            'password_lock_time': 'str',
            'is_user_created': 'bool',
            'freeform_tags': 'dict(str, str)',
            'defined_tags': 'dict(str, dict(str, object))'
        }

        self.attribute_map = {
            'user_assessment_id': 'userAssessmentId',
            'compartment_id': 'compartmentId',
            'target_id': 'targetId',
            'profile_name': 'profileName',
            'user_count': 'userCount',
            'failed_login_attempts': 'failedLoginAttempts',
            'password_verification_function': 'passwordVerificationFunction',
            'sessions_per_user': 'sessionsPerUser',
            'inactive_account_time': 'inactiveAccountTime',
            'password_lock_time': 'passwordLockTime',
            'is_user_created': 'isUserCreated',
            'freeform_tags': 'freeformTags',
            'defined_tags': 'definedTags'
        }

        self._user_assessment_id = None
        self._compartment_id = None
        self._target_id = None
        self._profile_name = None
        self._user_count = None
        self._failed_login_attempts = None
        self._password_verification_function = None
        self._sessions_per_user = None
        self._inactive_account_time = None
        self._password_lock_time = None
        self._is_user_created = None
        self._freeform_tags = None
        self._defined_tags = None

    @property
    def user_assessment_id(self):
        """
        **[Required]** Gets the user_assessment_id of this ProfileSummary.
        The OCID of the latest user assessment corresponding to the target under consideration. A compartment
        type assessment can also be passed to profiles from all the targets from the corresponding compartment.


        :return: The user_assessment_id of this ProfileSummary.
        :rtype: str
        """
        return self._user_assessment_id

    @user_assessment_id.setter
    def user_assessment_id(self, user_assessment_id):
        """
        Sets the user_assessment_id of this ProfileSummary.
        The OCID of the latest user assessment corresponding to the target under consideration. A compartment
        type assessment can also be passed to profiles from all the targets from the corresponding compartment.


        :param user_assessment_id: The user_assessment_id of this ProfileSummary.
        :type: str
        """
        self._user_assessment_id = user_assessment_id

    @property
    def compartment_id(self):
        """
        **[Required]** Gets the compartment_id of this ProfileSummary.
        The OCID of the compartment that contains the user assessment.


        :return: The compartment_id of this ProfileSummary.
        :rtype: str
        """
        return self._compartment_id

    @compartment_id.setter
    def compartment_id(self, compartment_id):
        """
        Sets the compartment_id of this ProfileSummary.
        The OCID of the compartment that contains the user assessment.


        :param compartment_id: The compartment_id of this ProfileSummary.
        :type: str
        """
        self._compartment_id = compartment_id

    @property
    def target_id(self):
        """
        Gets the target_id of this ProfileSummary.
        The OCID of the target database.


        :return: The target_id of this ProfileSummary.
        :rtype: str
        """
        return self._target_id

    @target_id.setter
    def target_id(self, target_id):
        """
        Sets the target_id of this ProfileSummary.
        The OCID of the target database.


        :param target_id: The target_id of this ProfileSummary.
        :type: str
        """
        self._target_id = target_id

    @property
    def profile_name(self):
        """
        Gets the profile_name of this ProfileSummary.
        The name of the profile.


        :return: The profile_name of this ProfileSummary.
        :rtype: str
        """
        return self._profile_name

    @profile_name.setter
    def profile_name(self, profile_name):
        """
        Sets the profile_name of this ProfileSummary.
        The name of the profile.


        :param profile_name: The profile_name of this ProfileSummary.
        :type: str
        """
        self._profile_name = profile_name

    @property
    def user_count(self):
        """
        Gets the user_count of this ProfileSummary.
        The number of users having a given profile.


        :return: The user_count of this ProfileSummary.
        :rtype: int
        """
        return self._user_count

    @user_count.setter
    def user_count(self, user_count):
        """
        Sets the user_count of this ProfileSummary.
        The number of users having a given profile.


        :param user_count: The user_count of this ProfileSummary.
        :type: int
        """
        self._user_count = user_count

    @property
    def failed_login_attempts(self):
        """
        Gets the failed_login_attempts of this ProfileSummary.
        Maximum times the user is allowed in fail login before the user account is locked.


        :return: The failed_login_attempts of this ProfileSummary.
        :rtype: str
        """
        return self._failed_login_attempts

    @failed_login_attempts.setter
    def failed_login_attempts(self, failed_login_attempts):
        """
        Sets the failed_login_attempts of this ProfileSummary.
        Maximum times the user is allowed in fail login before the user account is locked.


        :param failed_login_attempts: The failed_login_attempts of this ProfileSummary.
        :type: str
        """
        self._failed_login_attempts = failed_login_attempts

    @property
    def password_verification_function(self):
        """
        Gets the password_verification_function of this ProfileSummary.
        PL/SQL that can be used for password verification.


        :return: The password_verification_function of this ProfileSummary.
        :rtype: str
        """
        return self._password_verification_function

    @password_verification_function.setter
    def password_verification_function(self, password_verification_function):
        """
        Sets the password_verification_function of this ProfileSummary.
        PL/SQL that can be used for password verification.


        :param password_verification_function: The password_verification_function of this ProfileSummary.
        :type: str
        """
        self._password_verification_function = password_verification_function

    @property
    def sessions_per_user(self):
        """
        Gets the sessions_per_user of this ProfileSummary.
        The maximum number of sessions a user is allowed to create.


        :return: The sessions_per_user of this ProfileSummary.
        :rtype: str
        """
        return self._sessions_per_user

    @sessions_per_user.setter
    def sessions_per_user(self, sessions_per_user):
        """
        Sets the sessions_per_user of this ProfileSummary.
        The maximum number of sessions a user is allowed to create.


        :param sessions_per_user: The sessions_per_user of this ProfileSummary.
        :type: str
        """
        self._sessions_per_user = sessions_per_user

    @property
    def inactive_account_time(self):
        """
        Gets the inactive_account_time of this ProfileSummary.
        The permitted periods of continuous inactive time during a session, expressed in minutes.
        Long-running queries and other operations are not subjected to this limit.


        :return: The inactive_account_time of this ProfileSummary.
        :rtype: str
        """
        return self._inactive_account_time

    @inactive_account_time.setter
    def inactive_account_time(self, inactive_account_time):
        """
        Sets the inactive_account_time of this ProfileSummary.
        The permitted periods of continuous inactive time during a session, expressed in minutes.
        Long-running queries and other operations are not subjected to this limit.


        :param inactive_account_time: The inactive_account_time of this ProfileSummary.
        :type: str
        """
        self._inactive_account_time = inactive_account_time

    @property
    def password_lock_time(self):
        """
        Gets the password_lock_time of this ProfileSummary.
        Number of days the user account remains locked after failed login


        :return: The password_lock_time of this ProfileSummary.
        :rtype: str
        """
        return self._password_lock_time

    @password_lock_time.setter
    def password_lock_time(self, password_lock_time):
        """
        Sets the password_lock_time of this ProfileSummary.
        Number of days the user account remains locked after failed login


        :param password_lock_time: The password_lock_time of this ProfileSummary.
        :type: str
        """
        self._password_lock_time = password_lock_time

    @property
    def is_user_created(self):
        """
        Gets the is_user_created of this ProfileSummary.
        Represents if the profile is created by user.


        :return: The is_user_created of this ProfileSummary.
        :rtype: bool
        """
        return self._is_user_created

    @is_user_created.setter
    def is_user_created(self, is_user_created):
        """
        Sets the is_user_created of this ProfileSummary.
        Represents if the profile is created by user.


        :param is_user_created: The is_user_created of this ProfileSummary.
        :type: bool
        """
        self._is_user_created = is_user_created

    @property
    def freeform_tags(self):
        """
        Gets the freeform_tags of this ProfileSummary.
        Free-form tags for this resource. Each tag is a simple key-value pair with no predefined name, type, or namespace. For more information, see `Resource Tags`__

        Example: `{\"Department\": \"Finance\"}`

        __ https://docs.cloud.oracle.com/iaas/Content/General/Concepts/resourcetags.htm


        :return: The freeform_tags of this ProfileSummary.
        :rtype: dict(str, str)
        """
        return self._freeform_tags

    @freeform_tags.setter
    def freeform_tags(self, freeform_tags):
        """
        Sets the freeform_tags of this ProfileSummary.
        Free-form tags for this resource. Each tag is a simple key-value pair with no predefined name, type, or namespace. For more information, see `Resource Tags`__

        Example: `{\"Department\": \"Finance\"}`

        __ https://docs.cloud.oracle.com/iaas/Content/General/Concepts/resourcetags.htm


        :param freeform_tags: The freeform_tags of this ProfileSummary.
        :type: dict(str, str)
        """
        self._freeform_tags = freeform_tags

    @property
    def defined_tags(self):
        """
        Gets the defined_tags of this ProfileSummary.
        Defined tags for this resource. Each key is predefined and scoped to a namespace. For more information, see `Resource Tags`__

        Example: `{\"Operations\": {\"CostCenter\": \"42\"}}`

        __ https://docs.cloud.oracle.com/iaas/Content/General/Concepts/resourcetags.htm


        :return: The defined_tags of this ProfileSummary.
        :rtype: dict(str, dict(str, object))
        """
        return self._defined_tags

    @defined_tags.setter
    def defined_tags(self, defined_tags):
        """
        Sets the defined_tags of this ProfileSummary.
        Defined tags for this resource. Each key is predefined and scoped to a namespace. For more information, see `Resource Tags`__

        Example: `{\"Operations\": {\"CostCenter\": \"42\"}}`

        __ https://docs.cloud.oracle.com/iaas/Content/General/Concepts/resourcetags.htm


        :param defined_tags: The defined_tags of this ProfileSummary.
        :type: dict(str, dict(str, object))
        """
        self._defined_tags = defined_tags

    def __repr__(self):
        return formatted_flat_dict(self)

    def __eq__(self, other):
        if other is None:
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not self == other
