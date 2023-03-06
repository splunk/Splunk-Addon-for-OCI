# coding: utf-8
# Copyright (c) 2016, 2023, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.


from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class CreateOperationsInsightsPrivateEndpointDetails(object):
    """
    The details used to create a new Operation Insights private endpoint.
    """

    def __init__(self, **kwargs):
        """
        Initializes a new CreateOperationsInsightsPrivateEndpointDetails object with values from keyword arguments.
        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param display_name:
            The value to assign to the display_name property of this CreateOperationsInsightsPrivateEndpointDetails.
        :type display_name: str

        :param compartment_id:
            The value to assign to the compartment_id property of this CreateOperationsInsightsPrivateEndpointDetails.
        :type compartment_id: str

        :param vcn_id:
            The value to assign to the vcn_id property of this CreateOperationsInsightsPrivateEndpointDetails.
        :type vcn_id: str

        :param subnet_id:
            The value to assign to the subnet_id property of this CreateOperationsInsightsPrivateEndpointDetails.
        :type subnet_id: str

        :param is_used_for_rac_dbs:
            The value to assign to the is_used_for_rac_dbs property of this CreateOperationsInsightsPrivateEndpointDetails.
        :type is_used_for_rac_dbs: bool

        :param description:
            The value to assign to the description property of this CreateOperationsInsightsPrivateEndpointDetails.
        :type description: str

        :param nsg_ids:
            The value to assign to the nsg_ids property of this CreateOperationsInsightsPrivateEndpointDetails.
        :type nsg_ids: list[str]

        :param freeform_tags:
            The value to assign to the freeform_tags property of this CreateOperationsInsightsPrivateEndpointDetails.
        :type freeform_tags: dict(str, str)

        :param defined_tags:
            The value to assign to the defined_tags property of this CreateOperationsInsightsPrivateEndpointDetails.
        :type defined_tags: dict(str, dict(str, object))

        """
        self.swagger_types = {
            'display_name': 'str',
            'compartment_id': 'str',
            'vcn_id': 'str',
            'subnet_id': 'str',
            'is_used_for_rac_dbs': 'bool',
            'description': 'str',
            'nsg_ids': 'list[str]',
            'freeform_tags': 'dict(str, str)',
            'defined_tags': 'dict(str, dict(str, object))'
        }

        self.attribute_map = {
            'display_name': 'displayName',
            'compartment_id': 'compartmentId',
            'vcn_id': 'vcnId',
            'subnet_id': 'subnetId',
            'is_used_for_rac_dbs': 'isUsedForRacDbs',
            'description': 'description',
            'nsg_ids': 'nsgIds',
            'freeform_tags': 'freeformTags',
            'defined_tags': 'definedTags'
        }

        self._display_name = None
        self._compartment_id = None
        self._vcn_id = None
        self._subnet_id = None
        self._is_used_for_rac_dbs = None
        self._description = None
        self._nsg_ids = None
        self._freeform_tags = None
        self._defined_tags = None

    @property
    def display_name(self):
        """
        **[Required]** Gets the display_name of this CreateOperationsInsightsPrivateEndpointDetails.
        The display name for the private endpoint. It is changeable.


        :return: The display_name of this CreateOperationsInsightsPrivateEndpointDetails.
        :rtype: str
        """
        return self._display_name

    @display_name.setter
    def display_name(self, display_name):
        """
        Sets the display_name of this CreateOperationsInsightsPrivateEndpointDetails.
        The display name for the private endpoint. It is changeable.


        :param display_name: The display_name of this CreateOperationsInsightsPrivateEndpointDetails.
        :type: str
        """
        self._display_name = display_name

    @property
    def compartment_id(self):
        """
        **[Required]** Gets the compartment_id of this CreateOperationsInsightsPrivateEndpointDetails.
        The compartment `OCID`__ of the Private service accessed database.

        __ https://docs.cloud.oracle.com/iaas/Content/General/Concepts/identifiers.htm


        :return: The compartment_id of this CreateOperationsInsightsPrivateEndpointDetails.
        :rtype: str
        """
        return self._compartment_id

    @compartment_id.setter
    def compartment_id(self, compartment_id):
        """
        Sets the compartment_id of this CreateOperationsInsightsPrivateEndpointDetails.
        The compartment `OCID`__ of the Private service accessed database.

        __ https://docs.cloud.oracle.com/iaas/Content/General/Concepts/identifiers.htm


        :param compartment_id: The compartment_id of this CreateOperationsInsightsPrivateEndpointDetails.
        :type: str
        """
        self._compartment_id = compartment_id

    @property
    def vcn_id(self):
        """
        **[Required]** Gets the vcn_id of this CreateOperationsInsightsPrivateEndpointDetails.
        The VCN `OCID`__ of the Private service accessed database.

        __ https://docs.cloud.oracle.com/iaas/Content/General/Concepts/identifiers.htm


        :return: The vcn_id of this CreateOperationsInsightsPrivateEndpointDetails.
        :rtype: str
        """
        return self._vcn_id

    @vcn_id.setter
    def vcn_id(self, vcn_id):
        """
        Sets the vcn_id of this CreateOperationsInsightsPrivateEndpointDetails.
        The VCN `OCID`__ of the Private service accessed database.

        __ https://docs.cloud.oracle.com/iaas/Content/General/Concepts/identifiers.htm


        :param vcn_id: The vcn_id of this CreateOperationsInsightsPrivateEndpointDetails.
        :type: str
        """
        self._vcn_id = vcn_id

    @property
    def subnet_id(self):
        """
        **[Required]** Gets the subnet_id of this CreateOperationsInsightsPrivateEndpointDetails.
        The Subnet `OCID`__ of the Private service accessed database.

        __ https://docs.cloud.oracle.com/iaas/Content/General/Concepts/identifiers.htm


        :return: The subnet_id of this CreateOperationsInsightsPrivateEndpointDetails.
        :rtype: str
        """
        return self._subnet_id

    @subnet_id.setter
    def subnet_id(self, subnet_id):
        """
        Sets the subnet_id of this CreateOperationsInsightsPrivateEndpointDetails.
        The Subnet `OCID`__ of the Private service accessed database.

        __ https://docs.cloud.oracle.com/iaas/Content/General/Concepts/identifiers.htm


        :param subnet_id: The subnet_id of this CreateOperationsInsightsPrivateEndpointDetails.
        :type: str
        """
        self._subnet_id = subnet_id

    @property
    def is_used_for_rac_dbs(self):
        """
        **[Required]** Gets the is_used_for_rac_dbs of this CreateOperationsInsightsPrivateEndpointDetails.
        The flag to identify if private endpoint is used for rac database or not


        :return: The is_used_for_rac_dbs of this CreateOperationsInsightsPrivateEndpointDetails.
        :rtype: bool
        """
        return self._is_used_for_rac_dbs

    @is_used_for_rac_dbs.setter
    def is_used_for_rac_dbs(self, is_used_for_rac_dbs):
        """
        Sets the is_used_for_rac_dbs of this CreateOperationsInsightsPrivateEndpointDetails.
        The flag to identify if private endpoint is used for rac database or not


        :param is_used_for_rac_dbs: The is_used_for_rac_dbs of this CreateOperationsInsightsPrivateEndpointDetails.
        :type: bool
        """
        self._is_used_for_rac_dbs = is_used_for_rac_dbs

    @property
    def description(self):
        """
        Gets the description of this CreateOperationsInsightsPrivateEndpointDetails.
        The description of the private endpoint.


        :return: The description of this CreateOperationsInsightsPrivateEndpointDetails.
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        """
        Sets the description of this CreateOperationsInsightsPrivateEndpointDetails.
        The description of the private endpoint.


        :param description: The description of this CreateOperationsInsightsPrivateEndpointDetails.
        :type: str
        """
        self._description = description

    @property
    def nsg_ids(self):
        """
        Gets the nsg_ids of this CreateOperationsInsightsPrivateEndpointDetails.
        The `OCID`__ of the network security groups that the private endpoint belongs to.

        __ https://docs.cloud.oracle.com/iaas/Content/General/Concepts/identifiers.htm


        :return: The nsg_ids of this CreateOperationsInsightsPrivateEndpointDetails.
        :rtype: list[str]
        """
        return self._nsg_ids

    @nsg_ids.setter
    def nsg_ids(self, nsg_ids):
        """
        Sets the nsg_ids of this CreateOperationsInsightsPrivateEndpointDetails.
        The `OCID`__ of the network security groups that the private endpoint belongs to.

        __ https://docs.cloud.oracle.com/iaas/Content/General/Concepts/identifiers.htm


        :param nsg_ids: The nsg_ids of this CreateOperationsInsightsPrivateEndpointDetails.
        :type: list[str]
        """
        self._nsg_ids = nsg_ids

    @property
    def freeform_tags(self):
        """
        Gets the freeform_tags of this CreateOperationsInsightsPrivateEndpointDetails.
        Simple key-value pair that is applied without any predefined name, type or scope. Exists for cross-compatibility only.
        Example: `{\"bar-key\": \"value\"}`


        :return: The freeform_tags of this CreateOperationsInsightsPrivateEndpointDetails.
        :rtype: dict(str, str)
        """
        return self._freeform_tags

    @freeform_tags.setter
    def freeform_tags(self, freeform_tags):
        """
        Sets the freeform_tags of this CreateOperationsInsightsPrivateEndpointDetails.
        Simple key-value pair that is applied without any predefined name, type or scope. Exists for cross-compatibility only.
        Example: `{\"bar-key\": \"value\"}`


        :param freeform_tags: The freeform_tags of this CreateOperationsInsightsPrivateEndpointDetails.
        :type: dict(str, str)
        """
        self._freeform_tags = freeform_tags

    @property
    def defined_tags(self):
        """
        Gets the defined_tags of this CreateOperationsInsightsPrivateEndpointDetails.
        Defined tags for this resource. Each key is predefined and scoped to a namespace.
        Example: `{\"foo-namespace\": {\"bar-key\": \"value\"}}`


        :return: The defined_tags of this CreateOperationsInsightsPrivateEndpointDetails.
        :rtype: dict(str, dict(str, object))
        """
        return self._defined_tags

    @defined_tags.setter
    def defined_tags(self, defined_tags):
        """
        Sets the defined_tags of this CreateOperationsInsightsPrivateEndpointDetails.
        Defined tags for this resource. Each key is predefined and scoped to a namespace.
        Example: `{\"foo-namespace\": {\"bar-key\": \"value\"}}`


        :param defined_tags: The defined_tags of this CreateOperationsInsightsPrivateEndpointDetails.
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
