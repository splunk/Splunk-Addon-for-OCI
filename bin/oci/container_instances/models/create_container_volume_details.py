# coding: utf-8
# Copyright (c) 2016, 2023, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.


from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class CreateContainerVolumeDetails(object):
    """
    A Volume represents a directory with data that is accessible across multiple containers in a
    ContainerInstance.
    """

    #: A constant which can be used with the volume_type property of a CreateContainerVolumeDetails.
    #: This constant has a value of "EMPTYDIR"
    VOLUME_TYPE_EMPTYDIR = "EMPTYDIR"

    #: A constant which can be used with the volume_type property of a CreateContainerVolumeDetails.
    #: This constant has a value of "CONFIGFILE"
    VOLUME_TYPE_CONFIGFILE = "CONFIGFILE"

    def __init__(self, **kwargs):
        """
        Initializes a new CreateContainerVolumeDetails object with values from keyword arguments. This class has the following subclasses and if you are using this class as input
        to a service operations then you should favor using a subclass over the base class:

        * :class:`~oci.container_instances.models.CreateContainerConfigFileVolumeDetails`
        * :class:`~oci.container_instances.models.CreateContainerEmptyDirVolumeDetails`

        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param name:
            The value to assign to the name property of this CreateContainerVolumeDetails.
        :type name: str

        :param volume_type:
            The value to assign to the volume_type property of this CreateContainerVolumeDetails.
            Allowed values for this property are: "EMPTYDIR", "CONFIGFILE"
        :type volume_type: str

        """
        self.swagger_types = {
            'name': 'str',
            'volume_type': 'str'
        }

        self.attribute_map = {
            'name': 'name',
            'volume_type': 'volumeType'
        }

        self._name = None
        self._volume_type = None

    @staticmethod
    def get_subtype(object_dictionary):
        """
        Given the hash representation of a subtype of this class,
        use the info in the hash to return the class of the subtype.
        """
        type = object_dictionary['volumeType']

        if type == 'CONFIGFILE':
            return 'CreateContainerConfigFileVolumeDetails'

        if type == 'EMPTYDIR':
            return 'CreateContainerEmptyDirVolumeDetails'
        else:
            return 'CreateContainerVolumeDetails'

    @property
    def name(self):
        """
        **[Required]** Gets the name of this CreateContainerVolumeDetails.
        The name of the volume. This has be unique cross single ContainerInstance.


        :return: The name of this CreateContainerVolumeDetails.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """
        Sets the name of this CreateContainerVolumeDetails.
        The name of the volume. This has be unique cross single ContainerInstance.


        :param name: The name of this CreateContainerVolumeDetails.
        :type: str
        """
        self._name = name

    @property
    def volume_type(self):
        """
        **[Required]** Gets the volume_type of this CreateContainerVolumeDetails.
        The type of volume.

        Allowed values for this property are: "EMPTYDIR", "CONFIGFILE"


        :return: The volume_type of this CreateContainerVolumeDetails.
        :rtype: str
        """
        return self._volume_type

    @volume_type.setter
    def volume_type(self, volume_type):
        """
        Sets the volume_type of this CreateContainerVolumeDetails.
        The type of volume.


        :param volume_type: The volume_type of this CreateContainerVolumeDetails.
        :type: str
        """
        allowed_values = ["EMPTYDIR", "CONFIGFILE"]
        if not value_allowed_none_or_none_sentinel(volume_type, allowed_values):
            raise ValueError(
                "Invalid value for `volume_type`, must be None or one of {0}"
                .format(allowed_values)
            )
        self._volume_type = volume_type

    def __repr__(self):
        return formatted_flat_dict(self)

    def __eq__(self, other):
        if other is None:
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not self == other
