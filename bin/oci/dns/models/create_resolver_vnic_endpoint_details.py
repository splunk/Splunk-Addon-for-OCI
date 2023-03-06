# coding: utf-8
# Copyright (c) 2016, 2023, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.

from .create_resolver_endpoint_details import CreateResolverEndpointDetails
from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class CreateResolverVnicEndpointDetails(CreateResolverEndpointDetails):
    """
    The body for defining a new resolver VNIC endpoint. Either isForwarding or isListening must be true, but not both.
    If isListening is true, a listeningAddress may be provided. If isForwarding is true, a forwardingAddress
    may be provided. When not provided, an address will be chosen automatically.

    **Warning:** Oracle recommends that you avoid using any confidential information when you supply string values using the API.
    """

    def __init__(self, **kwargs):
        """
        Initializes a new CreateResolverVnicEndpointDetails object with values from keyword arguments. The default value of the :py:attr:`~oci.dns.models.CreateResolverVnicEndpointDetails.endpoint_type` attribute
        of this class is ``VNIC`` and it should not be changed.
        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param name:
            The value to assign to the name property of this CreateResolverVnicEndpointDetails.
        :type name: str

        :param endpoint_type:
            The value to assign to the endpoint_type property of this CreateResolverVnicEndpointDetails.
            Allowed values for this property are: "VNIC"
        :type endpoint_type: str

        :param forwarding_address:
            The value to assign to the forwarding_address property of this CreateResolverVnicEndpointDetails.
        :type forwarding_address: str

        :param is_forwarding:
            The value to assign to the is_forwarding property of this CreateResolverVnicEndpointDetails.
        :type is_forwarding: bool

        :param is_listening:
            The value to assign to the is_listening property of this CreateResolverVnicEndpointDetails.
        :type is_listening: bool

        :param listening_address:
            The value to assign to the listening_address property of this CreateResolverVnicEndpointDetails.
        :type listening_address: str

        :param subnet_id:
            The value to assign to the subnet_id property of this CreateResolverVnicEndpointDetails.
        :type subnet_id: str

        :param nsg_ids:
            The value to assign to the nsg_ids property of this CreateResolverVnicEndpointDetails.
        :type nsg_ids: list[str]

        """
        self.swagger_types = {
            'name': 'str',
            'endpoint_type': 'str',
            'forwarding_address': 'str',
            'is_forwarding': 'bool',
            'is_listening': 'bool',
            'listening_address': 'str',
            'subnet_id': 'str',
            'nsg_ids': 'list[str]'
        }

        self.attribute_map = {
            'name': 'name',
            'endpoint_type': 'endpointType',
            'forwarding_address': 'forwardingAddress',
            'is_forwarding': 'isForwarding',
            'is_listening': 'isListening',
            'listening_address': 'listeningAddress',
            'subnet_id': 'subnetId',
            'nsg_ids': 'nsgIds'
        }

        self._name = None
        self._endpoint_type = None
        self._forwarding_address = None
        self._is_forwarding = None
        self._is_listening = None
        self._listening_address = None
        self._subnet_id = None
        self._nsg_ids = None
        self._endpoint_type = 'VNIC'

    @property
    def subnet_id(self):
        """
        **[Required]** Gets the subnet_id of this CreateResolverVnicEndpointDetails.
        The OCID of a subnet. Must be part of the VCN that the resolver is attached to.


        :return: The subnet_id of this CreateResolverVnicEndpointDetails.
        :rtype: str
        """
        return self._subnet_id

    @subnet_id.setter
    def subnet_id(self, subnet_id):
        """
        Sets the subnet_id of this CreateResolverVnicEndpointDetails.
        The OCID of a subnet. Must be part of the VCN that the resolver is attached to.


        :param subnet_id: The subnet_id of this CreateResolverVnicEndpointDetails.
        :type: str
        """
        self._subnet_id = subnet_id

    @property
    def nsg_ids(self):
        """
        Gets the nsg_ids of this CreateResolverVnicEndpointDetails.
        An array of network security group OCIDs for the resolver endpoint. These must be part of the VCN that the
        resolver endpoint is a part of.


        :return: The nsg_ids of this CreateResolverVnicEndpointDetails.
        :rtype: list[str]
        """
        return self._nsg_ids

    @nsg_ids.setter
    def nsg_ids(self, nsg_ids):
        """
        Sets the nsg_ids of this CreateResolverVnicEndpointDetails.
        An array of network security group OCIDs for the resolver endpoint. These must be part of the VCN that the
        resolver endpoint is a part of.


        :param nsg_ids: The nsg_ids of this CreateResolverVnicEndpointDetails.
        :type: list[str]
        """
        self._nsg_ids = nsg_ids

    def __repr__(self):
        return formatted_flat_dict(self)

    def __eq__(self, other):
        if other is None:
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not self == other
