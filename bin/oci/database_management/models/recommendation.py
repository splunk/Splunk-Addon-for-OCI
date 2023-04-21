# coding: utf-8
# Copyright (c) 2016, 2023, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.


from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class Recommendation(object):
    """
    The details of the Optimizer Statistics Advisor findings and recommendations.
    """

    def __init__(self, **kwargs):
        """
        Initializes a new Recommendation object with values from keyword arguments.
        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param message:
            The value to assign to the message property of this Recommendation.
        :type message: str

        :param example:
            The value to assign to the example property of this Recommendation.
        :type example: oci.database_management.models.RecommendationExample

        :param rationales:
            The value to assign to the rationales property of this Recommendation.
        :type rationales: list[oci.database_management.models.RecommendationRationale]

        """
        self.swagger_types = {
            'message': 'str',
            'example': 'RecommendationExample',
            'rationales': 'list[RecommendationRationale]'
        }

        self.attribute_map = {
            'message': 'message',
            'example': 'example',
            'rationales': 'rationales'
        }

        self._message = None
        self._example = None
        self._rationales = None

    @property
    def message(self):
        """
        **[Required]** Gets the message of this Recommendation.
        An overview of the Optimizer Statistics Advisor recommendation.


        :return: The message of this Recommendation.
        :rtype: str
        """
        return self._message

    @message.setter
    def message(self, message):
        """
        Sets the message of this Recommendation.
        An overview of the Optimizer Statistics Advisor recommendation.


        :param message: The message of this Recommendation.
        :type: str
        """
        self._message = message

    @property
    def example(self):
        """
        Gets the example of this Recommendation.

        :return: The example of this Recommendation.
        :rtype: oci.database_management.models.RecommendationExample
        """
        return self._example

    @example.setter
    def example(self, example):
        """
        Sets the example of this Recommendation.

        :param example: The example of this Recommendation.
        :type: oci.database_management.models.RecommendationExample
        """
        self._example = example

    @property
    def rationales(self):
        """
        Gets the rationales of this Recommendation.
        The rationale of the recommendation.


        :return: The rationales of this Recommendation.
        :rtype: list[oci.database_management.models.RecommendationRationale]
        """
        return self._rationales

    @rationales.setter
    def rationales(self, rationales):
        """
        Sets the rationales of this Recommendation.
        The rationale of the recommendation.


        :param rationales: The rationales of this Recommendation.
        :type: list[oci.database_management.models.RecommendationRationale]
        """
        self._rationales = rationales

    def __repr__(self):
        return formatted_flat_dict(self)

    def __eq__(self, other):
        if other is None:
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not self == other
