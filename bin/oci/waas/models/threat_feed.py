# coding: utf-8
# Copyright (c) 2016, 2023, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.


from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class ThreatFeed(object):
    """
    The settings of the threat intelligence feed. You can block requests from IP addresses based on their reputations with various commercial and open source threat feeds.
    """

    #: A constant which can be used with the action property of a ThreatFeed.
    #: This constant has a value of "OFF"
    ACTION_OFF = "OFF"

    #: A constant which can be used with the action property of a ThreatFeed.
    #: This constant has a value of "DETECT"
    ACTION_DETECT = "DETECT"

    #: A constant which can be used with the action property of a ThreatFeed.
    #: This constant has a value of "BLOCK"
    ACTION_BLOCK = "BLOCK"

    def __init__(self, **kwargs):
        """
        Initializes a new ThreatFeed object with values from keyword arguments.
        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param key:
            The value to assign to the key property of this ThreatFeed.
        :type key: str

        :param name:
            The value to assign to the name property of this ThreatFeed.
        :type name: str

        :param action:
            The value to assign to the action property of this ThreatFeed.
            Allowed values for this property are: "OFF", "DETECT", "BLOCK", 'UNKNOWN_ENUM_VALUE'.
            Any unrecognized values returned by a service will be mapped to 'UNKNOWN_ENUM_VALUE'.
        :type action: str

        :param description:
            The value to assign to the description property of this ThreatFeed.
        :type description: str

        """
        self.swagger_types = {
            'key': 'str',
            'name': 'str',
            'action': 'str',
            'description': 'str'
        }

        self.attribute_map = {
            'key': 'key',
            'name': 'name',
            'action': 'action',
            'description': 'description'
        }

        self._key = None
        self._name = None
        self._action = None
        self._description = None

    @property
    def key(self):
        """
        Gets the key of this ThreatFeed.
        The unique key of the threat intelligence feed.


        :return: The key of this ThreatFeed.
        :rtype: str
        """
        return self._key

    @key.setter
    def key(self, key):
        """
        Sets the key of this ThreatFeed.
        The unique key of the threat intelligence feed.


        :param key: The key of this ThreatFeed.
        :type: str
        """
        self._key = key

    @property
    def name(self):
        """
        Gets the name of this ThreatFeed.
        The name of the threat intelligence feed.


        :return: The name of this ThreatFeed.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """
        Sets the name of this ThreatFeed.
        The name of the threat intelligence feed.


        :param name: The name of this ThreatFeed.
        :type: str
        """
        self._name = name

    @property
    def action(self):
        """
        Gets the action of this ThreatFeed.
        The action to take when traffic is flagged as malicious by data from the threat intelligence feed. If unspecified, defaults to `OFF`.

        Allowed values for this property are: "OFF", "DETECT", "BLOCK", 'UNKNOWN_ENUM_VALUE'.
        Any unrecognized values returned by a service will be mapped to 'UNKNOWN_ENUM_VALUE'.


        :return: The action of this ThreatFeed.
        :rtype: str
        """
        return self._action

    @action.setter
    def action(self, action):
        """
        Sets the action of this ThreatFeed.
        The action to take when traffic is flagged as malicious by data from the threat intelligence feed. If unspecified, defaults to `OFF`.


        :param action: The action of this ThreatFeed.
        :type: str
        """
        allowed_values = ["OFF", "DETECT", "BLOCK"]
        if not value_allowed_none_or_none_sentinel(action, allowed_values):
            action = 'UNKNOWN_ENUM_VALUE'
        self._action = action

    @property
    def description(self):
        """
        Gets the description of this ThreatFeed.
        The description of the threat intelligence feed.


        :return: The description of this ThreatFeed.
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        """
        Sets the description of this ThreatFeed.
        The description of the threat intelligence feed.


        :param description: The description of this ThreatFeed.
        :type: str
        """
        self._description = description

    def __repr__(self):
        return formatted_flat_dict(self)

    def __eq__(self, other):
        if other is None:
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not self == other
