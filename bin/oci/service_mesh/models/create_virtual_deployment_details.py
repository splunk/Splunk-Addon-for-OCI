# coding: utf-8
# Copyright (c) 2016, 2023, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.


from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class CreateVirtualDeploymentDetails(object):
    """
    The information about a new VirtualDeployment.
    """

    def __init__(self, **kwargs):
        """
        Initializes a new CreateVirtualDeploymentDetails object with values from keyword arguments.
        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param virtual_service_id:
            The value to assign to the virtual_service_id property of this CreateVirtualDeploymentDetails.
        :type virtual_service_id: str

        :param name:
            The value to assign to the name property of this CreateVirtualDeploymentDetails.
        :type name: str

        :param description:
            The value to assign to the description property of this CreateVirtualDeploymentDetails.
        :type description: str

        :param service_discovery:
            The value to assign to the service_discovery property of this CreateVirtualDeploymentDetails.
        :type service_discovery: oci.service_mesh.models.ServiceDiscoveryConfiguration

        :param listeners:
            The value to assign to the listeners property of this CreateVirtualDeploymentDetails.
        :type listeners: list[oci.service_mesh.models.VirtualDeploymentListener]

        :param access_logging:
            The value to assign to the access_logging property of this CreateVirtualDeploymentDetails.
        :type access_logging: oci.service_mesh.models.AccessLoggingConfiguration

        :param compartment_id:
            The value to assign to the compartment_id property of this CreateVirtualDeploymentDetails.
        :type compartment_id: str

        :param freeform_tags:
            The value to assign to the freeform_tags property of this CreateVirtualDeploymentDetails.
        :type freeform_tags: dict(str, str)

        :param defined_tags:
            The value to assign to the defined_tags property of this CreateVirtualDeploymentDetails.
        :type defined_tags: dict(str, dict(str, object))

        """
        self.swagger_types = {
            'virtual_service_id': 'str',
            'name': 'str',
            'description': 'str',
            'service_discovery': 'ServiceDiscoveryConfiguration',
            'listeners': 'list[VirtualDeploymentListener]',
            'access_logging': 'AccessLoggingConfiguration',
            'compartment_id': 'str',
            'freeform_tags': 'dict(str, str)',
            'defined_tags': 'dict(str, dict(str, object))'
        }

        self.attribute_map = {
            'virtual_service_id': 'virtualServiceId',
            'name': 'name',
            'description': 'description',
            'service_discovery': 'serviceDiscovery',
            'listeners': 'listeners',
            'access_logging': 'accessLogging',
            'compartment_id': 'compartmentId',
            'freeform_tags': 'freeformTags',
            'defined_tags': 'definedTags'
        }

        self._virtual_service_id = None
        self._name = None
        self._description = None
        self._service_discovery = None
        self._listeners = None
        self._access_logging = None
        self._compartment_id = None
        self._freeform_tags = None
        self._defined_tags = None

    @property
    def virtual_service_id(self):
        """
        **[Required]** Gets the virtual_service_id of this CreateVirtualDeploymentDetails.
        The OCID of the service mesh in which this access policy is created.


        :return: The virtual_service_id of this CreateVirtualDeploymentDetails.
        :rtype: str
        """
        return self._virtual_service_id

    @virtual_service_id.setter
    def virtual_service_id(self, virtual_service_id):
        """
        Sets the virtual_service_id of this CreateVirtualDeploymentDetails.
        The OCID of the service mesh in which this access policy is created.


        :param virtual_service_id: The virtual_service_id of this CreateVirtualDeploymentDetails.
        :type: str
        """
        self._virtual_service_id = virtual_service_id

    @property
    def name(self):
        """
        **[Required]** Gets the name of this CreateVirtualDeploymentDetails.
        A user-friendly name. The name must be unique within the same virtual service and cannot be changed after creation.
        Avoid entering confidential information.

        Example: `My unique resource name`


        :return: The name of this CreateVirtualDeploymentDetails.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """
        Sets the name of this CreateVirtualDeploymentDetails.
        A user-friendly name. The name must be unique within the same virtual service and cannot be changed after creation.
        Avoid entering confidential information.

        Example: `My unique resource name`


        :param name: The name of this CreateVirtualDeploymentDetails.
        :type: str
        """
        self._name = name

    @property
    def description(self):
        """
        Gets the description of this CreateVirtualDeploymentDetails.
        Description of the resource. It can be changed after creation.
        Avoid entering confidential information.

        Example: `This is my new resource`


        :return: The description of this CreateVirtualDeploymentDetails.
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        """
        Sets the description of this CreateVirtualDeploymentDetails.
        Description of the resource. It can be changed after creation.
        Avoid entering confidential information.

        Example: `This is my new resource`


        :param description: The description of this CreateVirtualDeploymentDetails.
        :type: str
        """
        self._description = description

    @property
    def service_discovery(self):
        """
        Gets the service_discovery of this CreateVirtualDeploymentDetails.

        :return: The service_discovery of this CreateVirtualDeploymentDetails.
        :rtype: oci.service_mesh.models.ServiceDiscoveryConfiguration
        """
        return self._service_discovery

    @service_discovery.setter
    def service_discovery(self, service_discovery):
        """
        Sets the service_discovery of this CreateVirtualDeploymentDetails.

        :param service_discovery: The service_discovery of this CreateVirtualDeploymentDetails.
        :type: oci.service_mesh.models.ServiceDiscoveryConfiguration
        """
        self._service_discovery = service_discovery

    @property
    def listeners(self):
        """
        Gets the listeners of this CreateVirtualDeploymentDetails.
        The listeners for the virtual deployment.


        :return: The listeners of this CreateVirtualDeploymentDetails.
        :rtype: list[oci.service_mesh.models.VirtualDeploymentListener]
        """
        return self._listeners

    @listeners.setter
    def listeners(self, listeners):
        """
        Sets the listeners of this CreateVirtualDeploymentDetails.
        The listeners for the virtual deployment.


        :param listeners: The listeners of this CreateVirtualDeploymentDetails.
        :type: list[oci.service_mesh.models.VirtualDeploymentListener]
        """
        self._listeners = listeners

    @property
    def access_logging(self):
        """
        Gets the access_logging of this CreateVirtualDeploymentDetails.

        :return: The access_logging of this CreateVirtualDeploymentDetails.
        :rtype: oci.service_mesh.models.AccessLoggingConfiguration
        """
        return self._access_logging

    @access_logging.setter
    def access_logging(self, access_logging):
        """
        Sets the access_logging of this CreateVirtualDeploymentDetails.

        :param access_logging: The access_logging of this CreateVirtualDeploymentDetails.
        :type: oci.service_mesh.models.AccessLoggingConfiguration
        """
        self._access_logging = access_logging

    @property
    def compartment_id(self):
        """
        **[Required]** Gets the compartment_id of this CreateVirtualDeploymentDetails.
        The `OCID`__ of the compartment.

        __ https://docs.cloud.oracle.com/Content/General/Concepts/identifiers.htm


        :return: The compartment_id of this CreateVirtualDeploymentDetails.
        :rtype: str
        """
        return self._compartment_id

    @compartment_id.setter
    def compartment_id(self, compartment_id):
        """
        Sets the compartment_id of this CreateVirtualDeploymentDetails.
        The `OCID`__ of the compartment.

        __ https://docs.cloud.oracle.com/Content/General/Concepts/identifiers.htm


        :param compartment_id: The compartment_id of this CreateVirtualDeploymentDetails.
        :type: str
        """
        self._compartment_id = compartment_id

    @property
    def freeform_tags(self):
        """
        Gets the freeform_tags of this CreateVirtualDeploymentDetails.
        Simple key-value pair that is applied without any predefined name, type or scope. Exists for cross-compatibility only.
        Example: `{\"bar-key\": \"value\"}`


        :return: The freeform_tags of this CreateVirtualDeploymentDetails.
        :rtype: dict(str, str)
        """
        return self._freeform_tags

    @freeform_tags.setter
    def freeform_tags(self, freeform_tags):
        """
        Sets the freeform_tags of this CreateVirtualDeploymentDetails.
        Simple key-value pair that is applied without any predefined name, type or scope. Exists for cross-compatibility only.
        Example: `{\"bar-key\": \"value\"}`


        :param freeform_tags: The freeform_tags of this CreateVirtualDeploymentDetails.
        :type: dict(str, str)
        """
        self._freeform_tags = freeform_tags

    @property
    def defined_tags(self):
        """
        Gets the defined_tags of this CreateVirtualDeploymentDetails.
        Defined tags for this resource. Each key is predefined and scoped to a namespace.
        Example: `{\"foo-namespace\": {\"bar-key\": \"value\"}}`


        :return: The defined_tags of this CreateVirtualDeploymentDetails.
        :rtype: dict(str, dict(str, object))
        """
        return self._defined_tags

    @defined_tags.setter
    def defined_tags(self, defined_tags):
        """
        Sets the defined_tags of this CreateVirtualDeploymentDetails.
        Defined tags for this resource. Each key is predefined and scoped to a namespace.
        Example: `{\"foo-namespace\": {\"bar-key\": \"value\"}}`


        :param defined_tags: The defined_tags of this CreateVirtualDeploymentDetails.
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
