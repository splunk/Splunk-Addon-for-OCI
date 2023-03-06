# coding: utf-8
# Copyright (c) 2016, 2023, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.


from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class IndicatorRelationship(object):
    """
    A relationship name and list of releated entities.
    """

    def __init__(self, **kwargs):
        """
        Initializes a new IndicatorRelationship object with values from keyword arguments.
        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param name:
            The value to assign to the name property of this IndicatorRelationship.
        :type name: str

        :param related_entity:
            The value to assign to the related_entity property of this IndicatorRelationship.
        :type related_entity: oci.threat_intelligence.models.EntityReference

        :param attribution:
            The value to assign to the attribution property of this IndicatorRelationship.
        :type attribution: list[oci.threat_intelligence.models.DataAttribution]

        """
        self.swagger_types = {
            'name': 'str',
            'related_entity': 'EntityReference',
            'attribution': 'list[DataAttribution]'
        }

        self.attribute_map = {
            'name': 'name',
            'related_entity': 'relatedEntity',
            'attribution': 'attribution'
        }

        self._name = None
        self._related_entity = None
        self._attribution = None

    @property
    def name(self):
        """
        **[Required]** Gets the name of this IndicatorRelationship.
        The name of the attribute.


        :return: The name of this IndicatorRelationship.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """
        Sets the name of this IndicatorRelationship.
        The name of the attribute.


        :param name: The name of this IndicatorRelationship.
        :type: str
        """
        self._name = name

    @property
    def related_entity(self):
        """
        **[Required]** Gets the related_entity of this IndicatorRelationship.

        :return: The related_entity of this IndicatorRelationship.
        :rtype: oci.threat_intelligence.models.EntityReference
        """
        return self._related_entity

    @related_entity.setter
    def related_entity(self, related_entity):
        """
        Sets the related_entity of this IndicatorRelationship.

        :param related_entity: The related_entity of this IndicatorRelationship.
        :type: oci.threat_intelligence.models.EntityReference
        """
        self._related_entity = related_entity

    @property
    def attribution(self):
        """
        **[Required]** Gets the attribution of this IndicatorRelationship.
        The array of attribution data that support this relationship.


        :return: The attribution of this IndicatorRelationship.
        :rtype: list[oci.threat_intelligence.models.DataAttribution]
        """
        return self._attribution

    @attribution.setter
    def attribution(self, attribution):
        """
        Sets the attribution of this IndicatorRelationship.
        The array of attribution data that support this relationship.


        :param attribution: The attribution of this IndicatorRelationship.
        :type: list[oci.threat_intelligence.models.DataAttribution]
        """
        self._attribution = attribution

    def __repr__(self):
        return formatted_flat_dict(self)

    def __eq__(self, other):
        if other is None:
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not self == other
