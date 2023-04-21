# coding: utf-8
# Copyright (c) 2016, 2023, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.

from .create_backup_destination_details import CreateBackupDestinationDetails
from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class CreateNFSBackupDestinationDetails(CreateBackupDestinationDetails):
    """
    Used for creating NFS backup destinations.
    """

    def __init__(self, **kwargs):
        """
        Initializes a new CreateNFSBackupDestinationDetails object with values from keyword arguments. The default value of the :py:attr:`~oci.database.models.CreateNFSBackupDestinationDetails.type` attribute
        of this class is ``NFS`` and it should not be changed.
        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param display_name:
            The value to assign to the display_name property of this CreateNFSBackupDestinationDetails.
        :type display_name: str

        :param compartment_id:
            The value to assign to the compartment_id property of this CreateNFSBackupDestinationDetails.
        :type compartment_id: str

        :param type:
            The value to assign to the type property of this CreateNFSBackupDestinationDetails.
            Allowed values for this property are: "NFS", "RECOVERY_APPLIANCE"
        :type type: str

        :param freeform_tags:
            The value to assign to the freeform_tags property of this CreateNFSBackupDestinationDetails.
        :type freeform_tags: dict(str, str)

        :param defined_tags:
            The value to assign to the defined_tags property of this CreateNFSBackupDestinationDetails.
        :type defined_tags: dict(str, dict(str, object))

        :param local_mount_point_path:
            The value to assign to the local_mount_point_path property of this CreateNFSBackupDestinationDetails.
        :type local_mount_point_path: str

        :param mount_type_details:
            The value to assign to the mount_type_details property of this CreateNFSBackupDestinationDetails.
        :type mount_type_details: oci.database.models.MountTypeDetails

        """
        self.swagger_types = {
            'display_name': 'str',
            'compartment_id': 'str',
            'type': 'str',
            'freeform_tags': 'dict(str, str)',
            'defined_tags': 'dict(str, dict(str, object))',
            'local_mount_point_path': 'str',
            'mount_type_details': 'MountTypeDetails'
        }

        self.attribute_map = {
            'display_name': 'displayName',
            'compartment_id': 'compartmentId',
            'type': 'type',
            'freeform_tags': 'freeformTags',
            'defined_tags': 'definedTags',
            'local_mount_point_path': 'localMountPointPath',
            'mount_type_details': 'mountTypeDetails'
        }

        self._display_name = None
        self._compartment_id = None
        self._type = None
        self._freeform_tags = None
        self._defined_tags = None
        self._local_mount_point_path = None
        self._mount_type_details = None
        self._type = 'NFS'

    @property
    def local_mount_point_path(self):
        """
        Gets the local_mount_point_path of this CreateNFSBackupDestinationDetails.
        **Deprecated.** The local directory path on each VM cluster node where the NFS server location is mounted. The local directory path and the NFS server location must each be the same across all of the VM cluster nodes. Ensure that the NFS mount is maintained continuously on all of the VM cluster nodes.
        This field is deprecated. Use the mountTypeDetails field instead to specify the mount type for NFS.


        :return: The local_mount_point_path of this CreateNFSBackupDestinationDetails.
        :rtype: str
        """
        return self._local_mount_point_path

    @local_mount_point_path.setter
    def local_mount_point_path(self, local_mount_point_path):
        """
        Sets the local_mount_point_path of this CreateNFSBackupDestinationDetails.
        **Deprecated.** The local directory path on each VM cluster node where the NFS server location is mounted. The local directory path and the NFS server location must each be the same across all of the VM cluster nodes. Ensure that the NFS mount is maintained continuously on all of the VM cluster nodes.
        This field is deprecated. Use the mountTypeDetails field instead to specify the mount type for NFS.


        :param local_mount_point_path: The local_mount_point_path of this CreateNFSBackupDestinationDetails.
        :type: str
        """
        self._local_mount_point_path = local_mount_point_path

    @property
    def mount_type_details(self):
        """
        Gets the mount_type_details of this CreateNFSBackupDestinationDetails.

        :return: The mount_type_details of this CreateNFSBackupDestinationDetails.
        :rtype: oci.database.models.MountTypeDetails
        """
        return self._mount_type_details

    @mount_type_details.setter
    def mount_type_details(self, mount_type_details):
        """
        Sets the mount_type_details of this CreateNFSBackupDestinationDetails.

        :param mount_type_details: The mount_type_details of this CreateNFSBackupDestinationDetails.
        :type: oci.database.models.MountTypeDetails
        """
        self._mount_type_details = mount_type_details

    def __repr__(self):
        return formatted_flat_dict(self)

    def __eq__(self, other):
        if other is None:
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not self == other
