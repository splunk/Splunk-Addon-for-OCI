# coding: utf-8
# Copyright (c) 2016, 2023, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.


from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class AuthenticationFactorSettingsClientAppSettings(object):
    """
    Settings related to compliance, Personal Identification Number (PIN) policy, and so on

    **SCIM++ Properties:**
    - idcsSearchable: false
    - multiValued: false
    - mutability: readWrite
    - required: true
    - returned: default
    - type: complex
    - uniqueness: none
    """

    #: A constant which can be used with the request_signing_algo property of a AuthenticationFactorSettingsClientAppSettings.
    #: This constant has a value of "SHA256withRSA"
    REQUEST_SIGNING_ALGO_SHA256WITH_RSA = "SHA256withRSA"

    #: A constant which can be used with the request_signing_algo property of a AuthenticationFactorSettingsClientAppSettings.
    #: This constant has a value of "SHA384withRSA"
    REQUEST_SIGNING_ALGO_SHA384WITH_RSA = "SHA384withRSA"

    #: A constant which can be used with the request_signing_algo property of a AuthenticationFactorSettingsClientAppSettings.
    #: This constant has a value of "SHA512withRSA"
    REQUEST_SIGNING_ALGO_SHA512WITH_RSA = "SHA512withRSA"

    #: A constant which can be used with the shared_secret_encoding property of a AuthenticationFactorSettingsClientAppSettings.
    #: This constant has a value of "Base32"
    SHARED_SECRET_ENCODING_BASE32 = "Base32"

    #: A constant which can be used with the shared_secret_encoding property of a AuthenticationFactorSettingsClientAppSettings.
    #: This constant has a value of "Base64"
    SHARED_SECRET_ENCODING_BASE64 = "Base64"

    def __init__(self, **kwargs):
        """
        Initializes a new AuthenticationFactorSettingsClientAppSettings object with values from keyword arguments.
        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param min_pin_length:
            The value to assign to the min_pin_length property of this AuthenticationFactorSettingsClientAppSettings.
        :type min_pin_length: int

        :param max_failures_before_warning:
            The value to assign to the max_failures_before_warning property of this AuthenticationFactorSettingsClientAppSettings.
        :type max_failures_before_warning: int

        :param max_failures_before_lockout:
            The value to assign to the max_failures_before_lockout property of this AuthenticationFactorSettingsClientAppSettings.
        :type max_failures_before_lockout: int

        :param initial_lockout_period_in_secs:
            The value to assign to the initial_lockout_period_in_secs property of this AuthenticationFactorSettingsClientAppSettings.
        :type initial_lockout_period_in_secs: int

        :param lockout_escalation_pattern:
            The value to assign to the lockout_escalation_pattern property of this AuthenticationFactorSettingsClientAppSettings.
        :type lockout_escalation_pattern: str

        :param max_lockout_interval_in_secs:
            The value to assign to the max_lockout_interval_in_secs property of this AuthenticationFactorSettingsClientAppSettings.
        :type max_lockout_interval_in_secs: int

        :param request_signing_algo:
            The value to assign to the request_signing_algo property of this AuthenticationFactorSettingsClientAppSettings.
            Allowed values for this property are: "SHA256withRSA", "SHA384withRSA", "SHA512withRSA", 'UNKNOWN_ENUM_VALUE'.
            Any unrecognized values returned by a service will be mapped to 'UNKNOWN_ENUM_VALUE'.
        :type request_signing_algo: str

        :param policy_update_freq_in_days:
            The value to assign to the policy_update_freq_in_days property of this AuthenticationFactorSettingsClientAppSettings.
        :type policy_update_freq_in_days: int

        :param key_pair_length:
            The value to assign to the key_pair_length property of this AuthenticationFactorSettingsClientAppSettings.
        :type key_pair_length: int

        :param device_protection_policy:
            The value to assign to the device_protection_policy property of this AuthenticationFactorSettingsClientAppSettings.
        :type device_protection_policy: str

        :param unlock_app_for_each_request_enabled:
            The value to assign to the unlock_app_for_each_request_enabled property of this AuthenticationFactorSettingsClientAppSettings.
        :type unlock_app_for_each_request_enabled: bool

        :param unlock_on_app_start_enabled:
            The value to assign to the unlock_on_app_start_enabled property of this AuthenticationFactorSettingsClientAppSettings.
        :type unlock_on_app_start_enabled: bool

        :param unlock_app_interval_in_secs:
            The value to assign to the unlock_app_interval_in_secs property of this AuthenticationFactorSettingsClientAppSettings.
        :type unlock_app_interval_in_secs: int

        :param shared_secret_encoding:
            The value to assign to the shared_secret_encoding property of this AuthenticationFactorSettingsClientAppSettings.
            Allowed values for this property are: "Base32", "Base64", 'UNKNOWN_ENUM_VALUE'.
            Any unrecognized values returned by a service will be mapped to 'UNKNOWN_ENUM_VALUE'.
        :type shared_secret_encoding: str

        :param unlock_on_app_foreground_enabled:
            The value to assign to the unlock_on_app_foreground_enabled property of this AuthenticationFactorSettingsClientAppSettings.
        :type unlock_on_app_foreground_enabled: bool

        """
        self.swagger_types = {
            'min_pin_length': 'int',
            'max_failures_before_warning': 'int',
            'max_failures_before_lockout': 'int',
            'initial_lockout_period_in_secs': 'int',
            'lockout_escalation_pattern': 'str',
            'max_lockout_interval_in_secs': 'int',
            'request_signing_algo': 'str',
            'policy_update_freq_in_days': 'int',
            'key_pair_length': 'int',
            'device_protection_policy': 'str',
            'unlock_app_for_each_request_enabled': 'bool',
            'unlock_on_app_start_enabled': 'bool',
            'unlock_app_interval_in_secs': 'int',
            'shared_secret_encoding': 'str',
            'unlock_on_app_foreground_enabled': 'bool'
        }

        self.attribute_map = {
            'min_pin_length': 'minPinLength',
            'max_failures_before_warning': 'maxFailuresBeforeWarning',
            'max_failures_before_lockout': 'maxFailuresBeforeLockout',
            'initial_lockout_period_in_secs': 'initialLockoutPeriodInSecs',
            'lockout_escalation_pattern': 'lockoutEscalationPattern',
            'max_lockout_interval_in_secs': 'maxLockoutIntervalInSecs',
            'request_signing_algo': 'requestSigningAlgo',
            'policy_update_freq_in_days': 'policyUpdateFreqInDays',
            'key_pair_length': 'keyPairLength',
            'device_protection_policy': 'deviceProtectionPolicy',
            'unlock_app_for_each_request_enabled': 'unlockAppForEachRequestEnabled',
            'unlock_on_app_start_enabled': 'unlockOnAppStartEnabled',
            'unlock_app_interval_in_secs': 'unlockAppIntervalInSecs',
            'shared_secret_encoding': 'sharedSecretEncoding',
            'unlock_on_app_foreground_enabled': 'unlockOnAppForegroundEnabled'
        }

        self._min_pin_length = None
        self._max_failures_before_warning = None
        self._max_failures_before_lockout = None
        self._initial_lockout_period_in_secs = None
        self._lockout_escalation_pattern = None
        self._max_lockout_interval_in_secs = None
        self._request_signing_algo = None
        self._policy_update_freq_in_days = None
        self._key_pair_length = None
        self._device_protection_policy = None
        self._unlock_app_for_each_request_enabled = None
        self._unlock_on_app_start_enabled = None
        self._unlock_app_interval_in_secs = None
        self._shared_secret_encoding = None
        self._unlock_on_app_foreground_enabled = None

    @property
    def min_pin_length(self):
        """
        **[Required]** Gets the min_pin_length of this AuthenticationFactorSettingsClientAppSettings.
        Minimum length of the Personal Identification Number (PIN)

        **SCIM++ Properties:**
         - idcsMaxValue: 10
         - idcsMinValue: 6
         - idcsSearchable: false
         - multiValued: false
         - mutability: readWrite
         - required: true
         - returned: default
         - type: integer
         - uniqueness: none


        :return: The min_pin_length of this AuthenticationFactorSettingsClientAppSettings.
        :rtype: int
        """
        return self._min_pin_length

    @min_pin_length.setter
    def min_pin_length(self, min_pin_length):
        """
        Sets the min_pin_length of this AuthenticationFactorSettingsClientAppSettings.
        Minimum length of the Personal Identification Number (PIN)

        **SCIM++ Properties:**
         - idcsMaxValue: 10
         - idcsMinValue: 6
         - idcsSearchable: false
         - multiValued: false
         - mutability: readWrite
         - required: true
         - returned: default
         - type: integer
         - uniqueness: none


        :param min_pin_length: The min_pin_length of this AuthenticationFactorSettingsClientAppSettings.
        :type: int
        """
        self._min_pin_length = min_pin_length

    @property
    def max_failures_before_warning(self):
        """
        **[Required]** Gets the max_failures_before_warning of this AuthenticationFactorSettingsClientAppSettings.
        The maximum number of login failures that the system will allow before raising a warning and sending an alert via email

        **SCIM++ Properties:**
         - idcsMaxValue: 10
         - idcsMinValue: 0
         - idcsSearchable: false
         - multiValued: false
         - mutability: readWrite
         - required: true
         - returned: default
         - type: integer
         - uniqueness: none


        :return: The max_failures_before_warning of this AuthenticationFactorSettingsClientAppSettings.
        :rtype: int
        """
        return self._max_failures_before_warning

    @max_failures_before_warning.setter
    def max_failures_before_warning(self, max_failures_before_warning):
        """
        Sets the max_failures_before_warning of this AuthenticationFactorSettingsClientAppSettings.
        The maximum number of login failures that the system will allow before raising a warning and sending an alert via email

        **SCIM++ Properties:**
         - idcsMaxValue: 10
         - idcsMinValue: 0
         - idcsSearchable: false
         - multiValued: false
         - mutability: readWrite
         - required: true
         - returned: default
         - type: integer
         - uniqueness: none


        :param max_failures_before_warning: The max_failures_before_warning of this AuthenticationFactorSettingsClientAppSettings.
        :type: int
        """
        self._max_failures_before_warning = max_failures_before_warning

    @property
    def max_failures_before_lockout(self):
        """
        **[Required]** Gets the max_failures_before_lockout of this AuthenticationFactorSettingsClientAppSettings.
        The maximum number of times that a particular user can fail to login before the system locks that user out of the service

        **SCIM++ Properties:**
         - idcsMaxValue: 10
         - idcsMinValue: 5
         - idcsSearchable: false
         - multiValued: false
         - mutability: readWrite
         - required: true
         - returned: default
         - type: integer
         - uniqueness: none


        :return: The max_failures_before_lockout of this AuthenticationFactorSettingsClientAppSettings.
        :rtype: int
        """
        return self._max_failures_before_lockout

    @max_failures_before_lockout.setter
    def max_failures_before_lockout(self, max_failures_before_lockout):
        """
        Sets the max_failures_before_lockout of this AuthenticationFactorSettingsClientAppSettings.
        The maximum number of times that a particular user can fail to login before the system locks that user out of the service

        **SCIM++ Properties:**
         - idcsMaxValue: 10
         - idcsMinValue: 5
         - idcsSearchable: false
         - multiValued: false
         - mutability: readWrite
         - required: true
         - returned: default
         - type: integer
         - uniqueness: none


        :param max_failures_before_lockout: The max_failures_before_lockout of this AuthenticationFactorSettingsClientAppSettings.
        :type: int
        """
        self._max_failures_before_lockout = max_failures_before_lockout

    @property
    def initial_lockout_period_in_secs(self):
        """
        **[Required]** Gets the initial_lockout_period_in_secs of this AuthenticationFactorSettingsClientAppSettings.
        The period of time in seconds that the system will lock a user out of the service after that user exceeds the maximum number of login failures

        **SCIM++ Properties:**
         - idcsMaxValue: 86400
         - idcsMinValue: 30
         - idcsSearchable: false
         - multiValued: false
         - mutability: readWrite
         - required: true
         - returned: default
         - type: integer
         - uniqueness: none


        :return: The initial_lockout_period_in_secs of this AuthenticationFactorSettingsClientAppSettings.
        :rtype: int
        """
        return self._initial_lockout_period_in_secs

    @initial_lockout_period_in_secs.setter
    def initial_lockout_period_in_secs(self, initial_lockout_period_in_secs):
        """
        Sets the initial_lockout_period_in_secs of this AuthenticationFactorSettingsClientAppSettings.
        The period of time in seconds that the system will lock a user out of the service after that user exceeds the maximum number of login failures

        **SCIM++ Properties:**
         - idcsMaxValue: 86400
         - idcsMinValue: 30
         - idcsSearchable: false
         - multiValued: false
         - mutability: readWrite
         - required: true
         - returned: default
         - type: integer
         - uniqueness: none


        :param initial_lockout_period_in_secs: The initial_lockout_period_in_secs of this AuthenticationFactorSettingsClientAppSettings.
        :type: int
        """
        self._initial_lockout_period_in_secs = initial_lockout_period_in_secs

    @property
    def lockout_escalation_pattern(self):
        """
        **[Required]** Gets the lockout_escalation_pattern of this AuthenticationFactorSettingsClientAppSettings.
        The pattern of escalation that the system follows, in locking a particular user out of the service.

        **SCIM++ Properties:**
         - idcsCanonicalValueSourceFilter: attrName eq \"lockoutEscalationPattern\" and attrValues.value eq \"$(lockoutEscalationPattern)\"
         - idcsCanonicalValueSourceResourceType: AllowedValue
         - idcsSearchable: false
         - multiValued: false
         - mutability: readWrite
         - required: true
         - returned: default
         - type: string
         - uniqueness: none


        :return: The lockout_escalation_pattern of this AuthenticationFactorSettingsClientAppSettings.
        :rtype: str
        """
        return self._lockout_escalation_pattern

    @lockout_escalation_pattern.setter
    def lockout_escalation_pattern(self, lockout_escalation_pattern):
        """
        Sets the lockout_escalation_pattern of this AuthenticationFactorSettingsClientAppSettings.
        The pattern of escalation that the system follows, in locking a particular user out of the service.

        **SCIM++ Properties:**
         - idcsCanonicalValueSourceFilter: attrName eq \"lockoutEscalationPattern\" and attrValues.value eq \"$(lockoutEscalationPattern)\"
         - idcsCanonicalValueSourceResourceType: AllowedValue
         - idcsSearchable: false
         - multiValued: false
         - mutability: readWrite
         - required: true
         - returned: default
         - type: string
         - uniqueness: none


        :param lockout_escalation_pattern: The lockout_escalation_pattern of this AuthenticationFactorSettingsClientAppSettings.
        :type: str
        """
        self._lockout_escalation_pattern = lockout_escalation_pattern

    @property
    def max_lockout_interval_in_secs(self):
        """
        **[Required]** Gets the max_lockout_interval_in_secs of this AuthenticationFactorSettingsClientAppSettings.
        The maximum period of time that the system will lock a particular user out of the service regardless of what the configured pattern of escalation would otherwise dictate

        **SCIM++ Properties:**
         - idcsMaxValue: 86400
         - idcsMinValue: 30
         - idcsSearchable: false
         - multiValued: false
         - mutability: readWrite
         - required: true
         - returned: default
         - type: integer
         - uniqueness: none


        :return: The max_lockout_interval_in_secs of this AuthenticationFactorSettingsClientAppSettings.
        :rtype: int
        """
        return self._max_lockout_interval_in_secs

    @max_lockout_interval_in_secs.setter
    def max_lockout_interval_in_secs(self, max_lockout_interval_in_secs):
        """
        Sets the max_lockout_interval_in_secs of this AuthenticationFactorSettingsClientAppSettings.
        The maximum period of time that the system will lock a particular user out of the service regardless of what the configured pattern of escalation would otherwise dictate

        **SCIM++ Properties:**
         - idcsMaxValue: 86400
         - idcsMinValue: 30
         - idcsSearchable: false
         - multiValued: false
         - mutability: readWrite
         - required: true
         - returned: default
         - type: integer
         - uniqueness: none


        :param max_lockout_interval_in_secs: The max_lockout_interval_in_secs of this AuthenticationFactorSettingsClientAppSettings.
        :type: int
        """
        self._max_lockout_interval_in_secs = max_lockout_interval_in_secs

    @property
    def request_signing_algo(self):
        """
        **[Required]** Gets the request_signing_algo of this AuthenticationFactorSettingsClientAppSettings.
        Indicates which algorithm the system will use to sign requests

        **SCIM++ Properties:**
         - idcsSearchable: false
         - multiValued: false
         - mutability: readWrite
         - required: true
         - returned: default
         - type: string
         - uniqueness: none

        Allowed values for this property are: "SHA256withRSA", "SHA384withRSA", "SHA512withRSA", 'UNKNOWN_ENUM_VALUE'.
        Any unrecognized values returned by a service will be mapped to 'UNKNOWN_ENUM_VALUE'.


        :return: The request_signing_algo of this AuthenticationFactorSettingsClientAppSettings.
        :rtype: str
        """
        return self._request_signing_algo

    @request_signing_algo.setter
    def request_signing_algo(self, request_signing_algo):
        """
        Sets the request_signing_algo of this AuthenticationFactorSettingsClientAppSettings.
        Indicates which algorithm the system will use to sign requests

        **SCIM++ Properties:**
         - idcsSearchable: false
         - multiValued: false
         - mutability: readWrite
         - required: true
         - returned: default
         - type: string
         - uniqueness: none


        :param request_signing_algo: The request_signing_algo of this AuthenticationFactorSettingsClientAppSettings.
        :type: str
        """
        allowed_values = ["SHA256withRSA", "SHA384withRSA", "SHA512withRSA"]
        if not value_allowed_none_or_none_sentinel(request_signing_algo, allowed_values):
            request_signing_algo = 'UNKNOWN_ENUM_VALUE'
        self._request_signing_algo = request_signing_algo

    @property
    def policy_update_freq_in_days(self):
        """
        **[Required]** Gets the policy_update_freq_in_days of this AuthenticationFactorSettingsClientAppSettings.
        The period of time in days after which a client should refresh its policy by re-reading that policy from the server

        **SCIM++ Properties:**
         - idcsMaxValue: 999
         - idcsMinValue: 1
         - idcsSearchable: false
         - multiValued: false
         - mutability: readWrite
         - required: true
         - returned: default
         - type: integer
         - uniqueness: none


        :return: The policy_update_freq_in_days of this AuthenticationFactorSettingsClientAppSettings.
        :rtype: int
        """
        return self._policy_update_freq_in_days

    @policy_update_freq_in_days.setter
    def policy_update_freq_in_days(self, policy_update_freq_in_days):
        """
        Sets the policy_update_freq_in_days of this AuthenticationFactorSettingsClientAppSettings.
        The period of time in days after which a client should refresh its policy by re-reading that policy from the server

        **SCIM++ Properties:**
         - idcsMaxValue: 999
         - idcsMinValue: 1
         - idcsSearchable: false
         - multiValued: false
         - mutability: readWrite
         - required: true
         - returned: default
         - type: integer
         - uniqueness: none


        :param policy_update_freq_in_days: The policy_update_freq_in_days of this AuthenticationFactorSettingsClientAppSettings.
        :type: int
        """
        self._policy_update_freq_in_days = policy_update_freq_in_days

    @property
    def key_pair_length(self):
        """
        **[Required]** Gets the key_pair_length of this AuthenticationFactorSettingsClientAppSettings.
        The size of the key that the system uses to generate the public-private key pair

        **SCIM++ Properties:**
         - idcsMaxValue: 4000
         - idcsMinValue: 32
         - idcsSearchable: false
         - multiValued: false
         - mutability: readWrite
         - required: true
         - returned: default
         - type: integer
         - uniqueness: none


        :return: The key_pair_length of this AuthenticationFactorSettingsClientAppSettings.
        :rtype: int
        """
        return self._key_pair_length

    @key_pair_length.setter
    def key_pair_length(self, key_pair_length):
        """
        Sets the key_pair_length of this AuthenticationFactorSettingsClientAppSettings.
        The size of the key that the system uses to generate the public-private key pair

        **SCIM++ Properties:**
         - idcsMaxValue: 4000
         - idcsMinValue: 32
         - idcsSearchable: false
         - multiValued: false
         - mutability: readWrite
         - required: true
         - returned: default
         - type: integer
         - uniqueness: none


        :param key_pair_length: The key_pair_length of this AuthenticationFactorSettingsClientAppSettings.
        :type: int
        """
        self._key_pair_length = key_pair_length

    @property
    def device_protection_policy(self):
        """
        **[Required]** Gets the device_protection_policy of this AuthenticationFactorSettingsClientAppSettings.
        Indicates what protection policy that the system applies on a device. By default, the value is NONE, which indicates that the system applies no protection policy. A value of APP_PIN indicates that the system requires a Personal Identification Number (PIN). A value of DEVICE_BIOMETRIC_OR_APP_PIN indicates that either a PIN or a biometric authentication factor is required.

        **SCIM++ Properties:**
         - idcsCanonicalValueSourceFilter: attrName eq \"deviceProtectionPolicy\" and attrValues.value eq \"$(deviceProtectionPolicy)\"
         - idcsCanonicalValueSourceResourceType: AllowedValue
         - idcsSearchable: false
         - multiValued: false
         - mutability: readWrite
         - required: true
         - returned: default
         - type: string
         - uniqueness: none


        :return: The device_protection_policy of this AuthenticationFactorSettingsClientAppSettings.
        :rtype: str
        """
        return self._device_protection_policy

    @device_protection_policy.setter
    def device_protection_policy(self, device_protection_policy):
        """
        Sets the device_protection_policy of this AuthenticationFactorSettingsClientAppSettings.
        Indicates what protection policy that the system applies on a device. By default, the value is NONE, which indicates that the system applies no protection policy. A value of APP_PIN indicates that the system requires a Personal Identification Number (PIN). A value of DEVICE_BIOMETRIC_OR_APP_PIN indicates that either a PIN or a biometric authentication factor is required.

        **SCIM++ Properties:**
         - idcsCanonicalValueSourceFilter: attrName eq \"deviceProtectionPolicy\" and attrValues.value eq \"$(deviceProtectionPolicy)\"
         - idcsCanonicalValueSourceResourceType: AllowedValue
         - idcsSearchable: false
         - multiValued: false
         - mutability: readWrite
         - required: true
         - returned: default
         - type: string
         - uniqueness: none


        :param device_protection_policy: The device_protection_policy of this AuthenticationFactorSettingsClientAppSettings.
        :type: str
        """
        self._device_protection_policy = device_protection_policy

    @property
    def unlock_app_for_each_request_enabled(self):
        """
        **[Required]** Gets the unlock_app_for_each_request_enabled of this AuthenticationFactorSettingsClientAppSettings.
        If true, indicates that the system should require the user to unlock the client app for each request. In order to unlock the App, the user must supply a Personal Identification Number (PIN) or a biometric authentication-factor.

        **SCIM++ Properties:**
         - idcsSearchable: false
         - multiValued: false
         - mutability: readWrite
         - required: true
         - returned: default
         - type: boolean
         - uniqueness: none


        :return: The unlock_app_for_each_request_enabled of this AuthenticationFactorSettingsClientAppSettings.
        :rtype: bool
        """
        return self._unlock_app_for_each_request_enabled

    @unlock_app_for_each_request_enabled.setter
    def unlock_app_for_each_request_enabled(self, unlock_app_for_each_request_enabled):
        """
        Sets the unlock_app_for_each_request_enabled of this AuthenticationFactorSettingsClientAppSettings.
        If true, indicates that the system should require the user to unlock the client app for each request. In order to unlock the App, the user must supply a Personal Identification Number (PIN) or a biometric authentication-factor.

        **SCIM++ Properties:**
         - idcsSearchable: false
         - multiValued: false
         - mutability: readWrite
         - required: true
         - returned: default
         - type: boolean
         - uniqueness: none


        :param unlock_app_for_each_request_enabled: The unlock_app_for_each_request_enabled of this AuthenticationFactorSettingsClientAppSettings.
        :type: bool
        """
        self._unlock_app_for_each_request_enabled = unlock_app_for_each_request_enabled

    @property
    def unlock_on_app_start_enabled(self):
        """
        **[Required]** Gets the unlock_on_app_start_enabled of this AuthenticationFactorSettingsClientAppSettings.
        If true, indicates that the system should require the user to unlock the client App whenever the App is started. In order to unlock the App, the user must supply a Personal Identification Number (PIN) or a biometric authentication-factor.

        **SCIM++ Properties:**
         - idcsSearchable: false
         - multiValued: false
         - mutability: readWrite
         - required: true
         - returned: default
         - type: boolean
         - uniqueness: none


        :return: The unlock_on_app_start_enabled of this AuthenticationFactorSettingsClientAppSettings.
        :rtype: bool
        """
        return self._unlock_on_app_start_enabled

    @unlock_on_app_start_enabled.setter
    def unlock_on_app_start_enabled(self, unlock_on_app_start_enabled):
        """
        Sets the unlock_on_app_start_enabled of this AuthenticationFactorSettingsClientAppSettings.
        If true, indicates that the system should require the user to unlock the client App whenever the App is started. In order to unlock the App, the user must supply a Personal Identification Number (PIN) or a biometric authentication-factor.

        **SCIM++ Properties:**
         - idcsSearchable: false
         - multiValued: false
         - mutability: readWrite
         - required: true
         - returned: default
         - type: boolean
         - uniqueness: none


        :param unlock_on_app_start_enabled: The unlock_on_app_start_enabled of this AuthenticationFactorSettingsClientAppSettings.
        :type: bool
        """
        self._unlock_on_app_start_enabled = unlock_on_app_start_enabled

    @property
    def unlock_app_interval_in_secs(self):
        """
        **[Required]** Gets the unlock_app_interval_in_secs of this AuthenticationFactorSettingsClientAppSettings.
        Specifies the period of time in seconds after which the client App should require the user to unlock the App. In order to unlock the App, the user must supply a Personal Identification Number (PIN) or a biometric authentication-factor. A value of zero means that it is disabled.

        **SCIM++ Properties:**
         - idcsMaxValue: 9999999
         - idcsMinValue: 0
         - idcsSearchable: false
         - multiValued: false
         - mutability: readWrite
         - required: true
         - returned: default
         - type: integer
         - uniqueness: none


        :return: The unlock_app_interval_in_secs of this AuthenticationFactorSettingsClientAppSettings.
        :rtype: int
        """
        return self._unlock_app_interval_in_secs

    @unlock_app_interval_in_secs.setter
    def unlock_app_interval_in_secs(self, unlock_app_interval_in_secs):
        """
        Sets the unlock_app_interval_in_secs of this AuthenticationFactorSettingsClientAppSettings.
        Specifies the period of time in seconds after which the client App should require the user to unlock the App. In order to unlock the App, the user must supply a Personal Identification Number (PIN) or a biometric authentication-factor. A value of zero means that it is disabled.

        **SCIM++ Properties:**
         - idcsMaxValue: 9999999
         - idcsMinValue: 0
         - idcsSearchable: false
         - multiValued: false
         - mutability: readWrite
         - required: true
         - returned: default
         - type: integer
         - uniqueness: none


        :param unlock_app_interval_in_secs: The unlock_app_interval_in_secs of this AuthenticationFactorSettingsClientAppSettings.
        :type: int
        """
        self._unlock_app_interval_in_secs = unlock_app_interval_in_secs

    @property
    def shared_secret_encoding(self):
        """
        **[Required]** Gets the shared_secret_encoding of this AuthenticationFactorSettingsClientAppSettings.
        Indicates the type of encoding that the system should use to generate a shared secret

        **SCIM++ Properties:**
         - idcsSearchable: false
         - multiValued: false
         - mutability: readWrite
         - required: true
         - returned: default
         - type: string
         - uniqueness: none

        Allowed values for this property are: "Base32", "Base64", 'UNKNOWN_ENUM_VALUE'.
        Any unrecognized values returned by a service will be mapped to 'UNKNOWN_ENUM_VALUE'.


        :return: The shared_secret_encoding of this AuthenticationFactorSettingsClientAppSettings.
        :rtype: str
        """
        return self._shared_secret_encoding

    @shared_secret_encoding.setter
    def shared_secret_encoding(self, shared_secret_encoding):
        """
        Sets the shared_secret_encoding of this AuthenticationFactorSettingsClientAppSettings.
        Indicates the type of encoding that the system should use to generate a shared secret

        **SCIM++ Properties:**
         - idcsSearchable: false
         - multiValued: false
         - mutability: readWrite
         - required: true
         - returned: default
         - type: string
         - uniqueness: none


        :param shared_secret_encoding: The shared_secret_encoding of this AuthenticationFactorSettingsClientAppSettings.
        :type: str
        """
        allowed_values = ["Base32", "Base64"]
        if not value_allowed_none_or_none_sentinel(shared_secret_encoding, allowed_values):
            shared_secret_encoding = 'UNKNOWN_ENUM_VALUE'
        self._shared_secret_encoding = shared_secret_encoding

    @property
    def unlock_on_app_foreground_enabled(self):
        """
        **[Required]** Gets the unlock_on_app_foreground_enabled of this AuthenticationFactorSettingsClientAppSettings.
        If true, indicates that the system should require the user to unlock the client App, when the client App comes to the foreground in the display of the device. In order to unlock the App, the user must supply a Personal Identification Number (PIN) or a biometric authentication-factor.

        **SCIM++ Properties:**
         - idcsSearchable: false
         - multiValued: false
         - mutability: readWrite
         - required: true
         - returned: default
         - type: boolean
         - uniqueness: none


        :return: The unlock_on_app_foreground_enabled of this AuthenticationFactorSettingsClientAppSettings.
        :rtype: bool
        """
        return self._unlock_on_app_foreground_enabled

    @unlock_on_app_foreground_enabled.setter
    def unlock_on_app_foreground_enabled(self, unlock_on_app_foreground_enabled):
        """
        Sets the unlock_on_app_foreground_enabled of this AuthenticationFactorSettingsClientAppSettings.
        If true, indicates that the system should require the user to unlock the client App, when the client App comes to the foreground in the display of the device. In order to unlock the App, the user must supply a Personal Identification Number (PIN) or a biometric authentication-factor.

        **SCIM++ Properties:**
         - idcsSearchable: false
         - multiValued: false
         - mutability: readWrite
         - required: true
         - returned: default
         - type: boolean
         - uniqueness: none


        :param unlock_on_app_foreground_enabled: The unlock_on_app_foreground_enabled of this AuthenticationFactorSettingsClientAppSettings.
        :type: bool
        """
        self._unlock_on_app_foreground_enabled = unlock_on_app_foreground_enabled

    def __repr__(self):
        return formatted_flat_dict(self)

    def __eq__(self, other):
        if other is None:
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not self == other
