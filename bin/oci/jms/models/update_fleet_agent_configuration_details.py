# coding: utf-8
# Copyright (c) 2016, 2023, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.


from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class UpdateFleetAgentConfigurationDetails(object):
    """
    Attributes to update a Fleet Agent Configuration.
    """

    def __init__(self, **kwargs):
        """
        Initializes a new UpdateFleetAgentConfigurationDetails object with values from keyword arguments.
        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param jre_scan_frequency_in_minutes:
            The value to assign to the jre_scan_frequency_in_minutes property of this UpdateFleetAgentConfigurationDetails.
        :type jre_scan_frequency_in_minutes: int

        :param java_usage_tracker_processing_frequency_in_minutes:
            The value to assign to the java_usage_tracker_processing_frequency_in_minutes property of this UpdateFleetAgentConfigurationDetails.
        :type java_usage_tracker_processing_frequency_in_minutes: int

        :param work_request_validity_period_in_days:
            The value to assign to the work_request_validity_period_in_days property of this UpdateFleetAgentConfigurationDetails.
        :type work_request_validity_period_in_days: int

        :param agent_polling_interval_in_minutes:
            The value to assign to the agent_polling_interval_in_minutes property of this UpdateFleetAgentConfigurationDetails.
        :type agent_polling_interval_in_minutes: int

        :param linux_configuration:
            The value to assign to the linux_configuration property of this UpdateFleetAgentConfigurationDetails.
        :type linux_configuration: oci.jms.models.FleetAgentOsConfiguration

        :param windows_configuration:
            The value to assign to the windows_configuration property of this UpdateFleetAgentConfigurationDetails.
        :type windows_configuration: oci.jms.models.FleetAgentOsConfiguration

        """
        self.swagger_types = {
            'jre_scan_frequency_in_minutes': 'int',
            'java_usage_tracker_processing_frequency_in_minutes': 'int',
            'work_request_validity_period_in_days': 'int',
            'agent_polling_interval_in_minutes': 'int',
            'linux_configuration': 'FleetAgentOsConfiguration',
            'windows_configuration': 'FleetAgentOsConfiguration'
        }

        self.attribute_map = {
            'jre_scan_frequency_in_minutes': 'jreScanFrequencyInMinutes',
            'java_usage_tracker_processing_frequency_in_minutes': 'javaUsageTrackerProcessingFrequencyInMinutes',
            'work_request_validity_period_in_days': 'workRequestValidityPeriodInDays',
            'agent_polling_interval_in_minutes': 'agentPollingIntervalInMinutes',
            'linux_configuration': 'linuxConfiguration',
            'windows_configuration': 'windowsConfiguration'
        }

        self._jre_scan_frequency_in_minutes = None
        self._java_usage_tracker_processing_frequency_in_minutes = None
        self._work_request_validity_period_in_days = None
        self._agent_polling_interval_in_minutes = None
        self._linux_configuration = None
        self._windows_configuration = None

    @property
    def jre_scan_frequency_in_minutes(self):
        """
        Gets the jre_scan_frequency_in_minutes of this UpdateFleetAgentConfigurationDetails.
        The frequency (in minutes) of JRE scanning. (That is, how often should JMS scan for JRE installations.)


        :return: The jre_scan_frequency_in_minutes of this UpdateFleetAgentConfigurationDetails.
        :rtype: int
        """
        return self._jre_scan_frequency_in_minutes

    @jre_scan_frequency_in_minutes.setter
    def jre_scan_frequency_in_minutes(self, jre_scan_frequency_in_minutes):
        """
        Sets the jre_scan_frequency_in_minutes of this UpdateFleetAgentConfigurationDetails.
        The frequency (in minutes) of JRE scanning. (That is, how often should JMS scan for JRE installations.)


        :param jre_scan_frequency_in_minutes: The jre_scan_frequency_in_minutes of this UpdateFleetAgentConfigurationDetails.
        :type: int
        """
        self._jre_scan_frequency_in_minutes = jre_scan_frequency_in_minutes

    @property
    def java_usage_tracker_processing_frequency_in_minutes(self):
        """
        Gets the java_usage_tracker_processing_frequency_in_minutes of this UpdateFleetAgentConfigurationDetails.
        The frequency (in minutes) of Java Usage Tracker processing. (That is, how often should JMS process data from the Java Usage Tracker.)


        :return: The java_usage_tracker_processing_frequency_in_minutes of this UpdateFleetAgentConfigurationDetails.
        :rtype: int
        """
        return self._java_usage_tracker_processing_frequency_in_minutes

    @java_usage_tracker_processing_frequency_in_minutes.setter
    def java_usage_tracker_processing_frequency_in_minutes(self, java_usage_tracker_processing_frequency_in_minutes):
        """
        Sets the java_usage_tracker_processing_frequency_in_minutes of this UpdateFleetAgentConfigurationDetails.
        The frequency (in minutes) of Java Usage Tracker processing. (That is, how often should JMS process data from the Java Usage Tracker.)


        :param java_usage_tracker_processing_frequency_in_minutes: The java_usage_tracker_processing_frequency_in_minutes of this UpdateFleetAgentConfigurationDetails.
        :type: int
        """
        self._java_usage_tracker_processing_frequency_in_minutes = java_usage_tracker_processing_frequency_in_minutes

    @property
    def work_request_validity_period_in_days(self):
        """
        Gets the work_request_validity_period_in_days of this UpdateFleetAgentConfigurationDetails.
        The validity period in days for work requests.


        :return: The work_request_validity_period_in_days of this UpdateFleetAgentConfigurationDetails.
        :rtype: int
        """
        return self._work_request_validity_period_in_days

    @work_request_validity_period_in_days.setter
    def work_request_validity_period_in_days(self, work_request_validity_period_in_days):
        """
        Sets the work_request_validity_period_in_days of this UpdateFleetAgentConfigurationDetails.
        The validity period in days for work requests.


        :param work_request_validity_period_in_days: The work_request_validity_period_in_days of this UpdateFleetAgentConfigurationDetails.
        :type: int
        """
        self._work_request_validity_period_in_days = work_request_validity_period_in_days

    @property
    def agent_polling_interval_in_minutes(self):
        """
        Gets the agent_polling_interval_in_minutes of this UpdateFleetAgentConfigurationDetails.
        Agent polling interval in minutes


        :return: The agent_polling_interval_in_minutes of this UpdateFleetAgentConfigurationDetails.
        :rtype: int
        """
        return self._agent_polling_interval_in_minutes

    @agent_polling_interval_in_minutes.setter
    def agent_polling_interval_in_minutes(self, agent_polling_interval_in_minutes):
        """
        Sets the agent_polling_interval_in_minutes of this UpdateFleetAgentConfigurationDetails.
        Agent polling interval in minutes


        :param agent_polling_interval_in_minutes: The agent_polling_interval_in_minutes of this UpdateFleetAgentConfigurationDetails.
        :type: int
        """
        self._agent_polling_interval_in_minutes = agent_polling_interval_in_minutes

    @property
    def linux_configuration(self):
        """
        Gets the linux_configuration of this UpdateFleetAgentConfigurationDetails.

        :return: The linux_configuration of this UpdateFleetAgentConfigurationDetails.
        :rtype: oci.jms.models.FleetAgentOsConfiguration
        """
        return self._linux_configuration

    @linux_configuration.setter
    def linux_configuration(self, linux_configuration):
        """
        Sets the linux_configuration of this UpdateFleetAgentConfigurationDetails.

        :param linux_configuration: The linux_configuration of this UpdateFleetAgentConfigurationDetails.
        :type: oci.jms.models.FleetAgentOsConfiguration
        """
        self._linux_configuration = linux_configuration

    @property
    def windows_configuration(self):
        """
        Gets the windows_configuration of this UpdateFleetAgentConfigurationDetails.

        :return: The windows_configuration of this UpdateFleetAgentConfigurationDetails.
        :rtype: oci.jms.models.FleetAgentOsConfiguration
        """
        return self._windows_configuration

    @windows_configuration.setter
    def windows_configuration(self, windows_configuration):
        """
        Sets the windows_configuration of this UpdateFleetAgentConfigurationDetails.

        :param windows_configuration: The windows_configuration of this UpdateFleetAgentConfigurationDetails.
        :type: oci.jms.models.FleetAgentOsConfiguration
        """
        self._windows_configuration = windows_configuration

    def __repr__(self):
        return formatted_flat_dict(self)

    def __eq__(self, other):
        if other is None:
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not self == other
