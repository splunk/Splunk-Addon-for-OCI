# coding: utf-8
# Copyright (c) 2016, 2023, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.


from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class InteractionSummary(object):
    """
    Summary of access request customer and operator conversation.
    """

    def __init__(self, **kwargs):
        """
        Initializes a new InteractionSummary object with values from keyword arguments.
        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param id:
            The value to assign to the id property of this InteractionSummary.
        :type id: str

        :param user_id:
            The value to assign to the user_id property of this InteractionSummary.
        :type user_id: str

        :param user_name:
            The value to assign to the user_name property of this InteractionSummary.
        :type user_name: str

        :param message:
            The value to assign to the message property of this InteractionSummary.
        :type message: str

        :param user_type:
            The value to assign to the user_type property of this InteractionSummary.
        :type user_type: str

        :param time_of_conversation:
            The value to assign to the time_of_conversation property of this InteractionSummary.
        :type time_of_conversation: datetime

        """
        self.swagger_types = {
            'id': 'str',
            'user_id': 'str',
            'user_name': 'str',
            'message': 'str',
            'user_type': 'str',
            'time_of_conversation': 'datetime'
        }

        self.attribute_map = {
            'id': 'id',
            'user_id': 'userId',
            'user_name': 'userName',
            'message': 'message',
            'user_type': 'userType',
            'time_of_conversation': 'timeOfConversation'
        }

        self._id = None
        self._user_id = None
        self._user_name = None
        self._message = None
        self._user_type = None
        self._time_of_conversation = None

    @property
    def id(self):
        """
        Gets the id of this InteractionSummary.
        The uniqueId of the message.


        :return: The id of this InteractionSummary.
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """
        Sets the id of this InteractionSummary.
        The uniqueId of the message.


        :param id: The id of this InteractionSummary.
        :type: str
        """
        self._id = id

    @property
    def user_id(self):
        """
        Gets the user_id of this InteractionSummary.
        customer or operator id who is part of this conversation.


        :return: The user_id of this InteractionSummary.
        :rtype: str
        """
        return self._user_id

    @user_id.setter
    def user_id(self, user_id):
        """
        Sets the user_id of this InteractionSummary.
        customer or operator id who is part of this conversation.


        :param user_id: The user_id of this InteractionSummary.
        :type: str
        """
        self._user_id = user_id

    @property
    def user_name(self):
        """
        Gets the user_name of this InteractionSummary.
        customer or operator Name who is part of this conversation.


        :return: The user_name of this InteractionSummary.
        :rtype: str
        """
        return self._user_name

    @user_name.setter
    def user_name(self, user_name):
        """
        Sets the user_name of this InteractionSummary.
        customer or operator Name who is part of this conversation.


        :param user_name: The user_name of this InteractionSummary.
        :type: str
        """
        self._user_name = user_name

    @property
    def message(self):
        """
        Gets the message of this InteractionSummary.
        contains the information exchanged between operator and customer.


        :return: The message of this InteractionSummary.
        :rtype: str
        """
        return self._message

    @message.setter
    def message(self, message):
        """
        Sets the message of this InteractionSummary.
        contains the information exchanged between operator and customer.


        :param message: The message of this InteractionSummary.
        :type: str
        """
        self._message = message

    @property
    def user_type(self):
        """
        Gets the user_type of this InteractionSummary.
        Whether the userConversation is an operator or customer.


        :return: The user_type of this InteractionSummary.
        :rtype: str
        """
        return self._user_type

    @user_type.setter
    def user_type(self, user_type):
        """
        Sets the user_type of this InteractionSummary.
        Whether the userConversation is an operator or customer.


        :param user_type: The user_type of this InteractionSummary.
        :type: str
        """
        self._user_type = user_type

    @property
    def time_of_conversation(self):
        """
        Gets the time_of_conversation of this InteractionSummary.
        Time when the conversation happened in `RFC 3339`__timestamp format. Example: '2020-05-22T21:10:29.600Z'

        __ https://tools.ietf.org/html/rfc3339


        :return: The time_of_conversation of this InteractionSummary.
        :rtype: datetime
        """
        return self._time_of_conversation

    @time_of_conversation.setter
    def time_of_conversation(self, time_of_conversation):
        """
        Sets the time_of_conversation of this InteractionSummary.
        Time when the conversation happened in `RFC 3339`__timestamp format. Example: '2020-05-22T21:10:29.600Z'

        __ https://tools.ietf.org/html/rfc3339


        :param time_of_conversation: The time_of_conversation of this InteractionSummary.
        :type: datetime
        """
        self._time_of_conversation = time_of_conversation

    def __repr__(self):
        return formatted_flat_dict(self)

    def __eq__(self, other):
        if other is None:
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not self == other
