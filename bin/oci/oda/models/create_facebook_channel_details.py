# coding: utf-8
# Copyright (c) 2016, 2023, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.

from .create_channel_details import CreateChannelDetails
from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class CreateFacebookChannelDetails(CreateChannelDetails):
    """
    Properties required to create a Facebook channel.
    """

    def __init__(self, **kwargs):
        """
        Initializes a new CreateFacebookChannelDetails object with values from keyword arguments. The default value of the :py:attr:`~oci.oda.models.CreateFacebookChannelDetails.type` attribute
        of this class is ``FACEBOOK`` and it should not be changed.
        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param name:
            The value to assign to the name property of this CreateFacebookChannelDetails.
        :type name: str

        :param description:
            The value to assign to the description property of this CreateFacebookChannelDetails.
        :type description: str

        :param type:
            The value to assign to the type property of this CreateFacebookChannelDetails.
            Allowed values for this property are: "ANDROID", "APPEVENT", "APPLICATION", "CORTANA", "FACEBOOK", "IOS", "MSTEAMS", "OSS", "OSVC", "SERVICECLOUD", "SLACK", "TEST", "TWILIO", "WEB", "WEBHOOK"
        :type type: str

        :param session_expiry_duration_in_milliseconds:
            The value to assign to the session_expiry_duration_in_milliseconds property of this CreateFacebookChannelDetails.
        :type session_expiry_duration_in_milliseconds: int

        :param freeform_tags:
            The value to assign to the freeform_tags property of this CreateFacebookChannelDetails.
        :type freeform_tags: dict(str, str)

        :param defined_tags:
            The value to assign to the defined_tags property of this CreateFacebookChannelDetails.
        :type defined_tags: dict(str, dict(str, object))

        :param app_secret:
            The value to assign to the app_secret property of this CreateFacebookChannelDetails.
        :type app_secret: str

        :param page_access_token:
            The value to assign to the page_access_token property of this CreateFacebookChannelDetails.
        :type page_access_token: str

        :param bot_id:
            The value to assign to the bot_id property of this CreateFacebookChannelDetails.
        :type bot_id: str

        """
        self.swagger_types = {
            'name': 'str',
            'description': 'str',
            'type': 'str',
            'session_expiry_duration_in_milliseconds': 'int',
            'freeform_tags': 'dict(str, str)',
            'defined_tags': 'dict(str, dict(str, object))',
            'app_secret': 'str',
            'page_access_token': 'str',
            'bot_id': 'str'
        }

        self.attribute_map = {
            'name': 'name',
            'description': 'description',
            'type': 'type',
            'session_expiry_duration_in_milliseconds': 'sessionExpiryDurationInMilliseconds',
            'freeform_tags': 'freeformTags',
            'defined_tags': 'definedTags',
            'app_secret': 'appSecret',
            'page_access_token': 'pageAccessToken',
            'bot_id': 'botId'
        }

        self._name = None
        self._description = None
        self._type = None
        self._session_expiry_duration_in_milliseconds = None
        self._freeform_tags = None
        self._defined_tags = None
        self._app_secret = None
        self._page_access_token = None
        self._bot_id = None
        self._type = 'FACEBOOK'

    @property
    def app_secret(self):
        """
        **[Required]** Gets the app_secret of this CreateFacebookChannelDetails.
        The app secret for your Facebook app.


        :return: The app_secret of this CreateFacebookChannelDetails.
        :rtype: str
        """
        return self._app_secret

    @app_secret.setter
    def app_secret(self, app_secret):
        """
        Sets the app_secret of this CreateFacebookChannelDetails.
        The app secret for your Facebook app.


        :param app_secret: The app_secret of this CreateFacebookChannelDetails.
        :type: str
        """
        self._app_secret = app_secret

    @property
    def page_access_token(self):
        """
        **[Required]** Gets the page_access_token of this CreateFacebookChannelDetails.
        The page access token that you generated for your Facebook page.


        :return: The page_access_token of this CreateFacebookChannelDetails.
        :rtype: str
        """
        return self._page_access_token

    @page_access_token.setter
    def page_access_token(self, page_access_token):
        """
        Sets the page_access_token of this CreateFacebookChannelDetails.
        The page access token that you generated for your Facebook page.


        :param page_access_token: The page_access_token of this CreateFacebookChannelDetails.
        :type: str
        """
        self._page_access_token = page_access_token

    @property
    def bot_id(self):
        """
        Gets the bot_id of this CreateFacebookChannelDetails.
        The ID of the Skill or Digital Assistant that the Channel is routed to.


        :return: The bot_id of this CreateFacebookChannelDetails.
        :rtype: str
        """
        return self._bot_id

    @bot_id.setter
    def bot_id(self, bot_id):
        """
        Sets the bot_id of this CreateFacebookChannelDetails.
        The ID of the Skill or Digital Assistant that the Channel is routed to.


        :param bot_id: The bot_id of this CreateFacebookChannelDetails.
        :type: str
        """
        self._bot_id = bot_id

    def __repr__(self):
        return formatted_flat_dict(self)

    def __eq__(self, other):
        if other is None:
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not self == other
