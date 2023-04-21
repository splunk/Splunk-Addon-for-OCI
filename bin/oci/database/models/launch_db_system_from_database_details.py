# coding: utf-8
# Copyright (c) 2016, 2023, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.

from .launch_db_system_base import LaunchDbSystemBase
from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class LaunchDbSystemFromDatabaseDetails(LaunchDbSystemBase):
    """
    Used for creating a new DB system from a database, including archived redo log data.
    """

    #: A constant which can be used with the database_edition property of a LaunchDbSystemFromDatabaseDetails.
    #: This constant has a value of "STANDARD_EDITION"
    DATABASE_EDITION_STANDARD_EDITION = "STANDARD_EDITION"

    #: A constant which can be used with the database_edition property of a LaunchDbSystemFromDatabaseDetails.
    #: This constant has a value of "ENTERPRISE_EDITION"
    DATABASE_EDITION_ENTERPRISE_EDITION = "ENTERPRISE_EDITION"

    #: A constant which can be used with the database_edition property of a LaunchDbSystemFromDatabaseDetails.
    #: This constant has a value of "ENTERPRISE_EDITION_HIGH_PERFORMANCE"
    DATABASE_EDITION_ENTERPRISE_EDITION_HIGH_PERFORMANCE = "ENTERPRISE_EDITION_HIGH_PERFORMANCE"

    #: A constant which can be used with the database_edition property of a LaunchDbSystemFromDatabaseDetails.
    #: This constant has a value of "ENTERPRISE_EDITION_EXTREME_PERFORMANCE"
    DATABASE_EDITION_ENTERPRISE_EDITION_EXTREME_PERFORMANCE = "ENTERPRISE_EDITION_EXTREME_PERFORMANCE"

    #: A constant which can be used with the disk_redundancy property of a LaunchDbSystemFromDatabaseDetails.
    #: This constant has a value of "HIGH"
    DISK_REDUNDANCY_HIGH = "HIGH"

    #: A constant which can be used with the disk_redundancy property of a LaunchDbSystemFromDatabaseDetails.
    #: This constant has a value of "NORMAL"
    DISK_REDUNDANCY_NORMAL = "NORMAL"

    #: A constant which can be used with the license_model property of a LaunchDbSystemFromDatabaseDetails.
    #: This constant has a value of "LICENSE_INCLUDED"
    LICENSE_MODEL_LICENSE_INCLUDED = "LICENSE_INCLUDED"

    #: A constant which can be used with the license_model property of a LaunchDbSystemFromDatabaseDetails.
    #: This constant has a value of "BRING_YOUR_OWN_LICENSE"
    LICENSE_MODEL_BRING_YOUR_OWN_LICENSE = "BRING_YOUR_OWN_LICENSE"

    def __init__(self, **kwargs):
        """
        Initializes a new LaunchDbSystemFromDatabaseDetails object with values from keyword arguments. The default value of the :py:attr:`~oci.database.models.LaunchDbSystemFromDatabaseDetails.source` attribute
        of this class is ``DATABASE`` and it should not be changed.
        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param compartment_id:
            The value to assign to the compartment_id property of this LaunchDbSystemFromDatabaseDetails.
        :type compartment_id: str

        :param fault_domains:
            The value to assign to the fault_domains property of this LaunchDbSystemFromDatabaseDetails.
        :type fault_domains: list[str]

        :param display_name:
            The value to assign to the display_name property of this LaunchDbSystemFromDatabaseDetails.
        :type display_name: str

        :param availability_domain:
            The value to assign to the availability_domain property of this LaunchDbSystemFromDatabaseDetails.
        :type availability_domain: str

        :param subnet_id:
            The value to assign to the subnet_id property of this LaunchDbSystemFromDatabaseDetails.
        :type subnet_id: str

        :param backup_subnet_id:
            The value to assign to the backup_subnet_id property of this LaunchDbSystemFromDatabaseDetails.
        :type backup_subnet_id: str

        :param nsg_ids:
            The value to assign to the nsg_ids property of this LaunchDbSystemFromDatabaseDetails.
        :type nsg_ids: list[str]

        :param backup_network_nsg_ids:
            The value to assign to the backup_network_nsg_ids property of this LaunchDbSystemFromDatabaseDetails.
        :type backup_network_nsg_ids: list[str]

        :param shape:
            The value to assign to the shape property of this LaunchDbSystemFromDatabaseDetails.
        :type shape: str

        :param time_zone:
            The value to assign to the time_zone property of this LaunchDbSystemFromDatabaseDetails.
        :type time_zone: str

        :param db_system_options:
            The value to assign to the db_system_options property of this LaunchDbSystemFromDatabaseDetails.
        :type db_system_options: oci.database.models.DbSystemOptions

        :param storage_volume_performance_mode:
            The value to assign to the storage_volume_performance_mode property of this LaunchDbSystemFromDatabaseDetails.
            Allowed values for this property are: "BALANCED", "HIGH_PERFORMANCE"
        :type storage_volume_performance_mode: str

        :param sparse_diskgroup:
            The value to assign to the sparse_diskgroup property of this LaunchDbSystemFromDatabaseDetails.
        :type sparse_diskgroup: bool

        :param ssh_public_keys:
            The value to assign to the ssh_public_keys property of this LaunchDbSystemFromDatabaseDetails.
        :type ssh_public_keys: list[str]

        :param hostname:
            The value to assign to the hostname property of this LaunchDbSystemFromDatabaseDetails.
        :type hostname: str

        :param domain:
            The value to assign to the domain property of this LaunchDbSystemFromDatabaseDetails.
        :type domain: str

        :param cpu_core_count:
            The value to assign to the cpu_core_count property of this LaunchDbSystemFromDatabaseDetails.
        :type cpu_core_count: int

        :param cluster_name:
            The value to assign to the cluster_name property of this LaunchDbSystemFromDatabaseDetails.
        :type cluster_name: str

        :param data_storage_percentage:
            The value to assign to the data_storage_percentage property of this LaunchDbSystemFromDatabaseDetails.
        :type data_storage_percentage: int

        :param initial_data_storage_size_in_gb:
            The value to assign to the initial_data_storage_size_in_gb property of this LaunchDbSystemFromDatabaseDetails.
        :type initial_data_storage_size_in_gb: int

        :param kms_key_id:
            The value to assign to the kms_key_id property of this LaunchDbSystemFromDatabaseDetails.
        :type kms_key_id: str

        :param kms_key_version_id:
            The value to assign to the kms_key_version_id property of this LaunchDbSystemFromDatabaseDetails.
        :type kms_key_version_id: str

        :param node_count:
            The value to assign to the node_count property of this LaunchDbSystemFromDatabaseDetails.
        :type node_count: int

        :param freeform_tags:
            The value to assign to the freeform_tags property of this LaunchDbSystemFromDatabaseDetails.
        :type freeform_tags: dict(str, str)

        :param defined_tags:
            The value to assign to the defined_tags property of this LaunchDbSystemFromDatabaseDetails.
        :type defined_tags: dict(str, dict(str, object))

        :param source:
            The value to assign to the source property of this LaunchDbSystemFromDatabaseDetails.
            Allowed values for this property are: "NONE", "DB_BACKUP", "DATABASE", "DB_SYSTEM"
        :type source: str

        :param private_ip:
            The value to assign to the private_ip property of this LaunchDbSystemFromDatabaseDetails.
        :type private_ip: str

        :param data_collection_options:
            The value to assign to the data_collection_options property of this LaunchDbSystemFromDatabaseDetails.
        :type data_collection_options: oci.database.models.DataCollectionOptions

        :param db_home:
            The value to assign to the db_home property of this LaunchDbSystemFromDatabaseDetails.
        :type db_home: oci.database.models.CreateDbHomeFromDatabaseDetails

        :param database_edition:
            The value to assign to the database_edition property of this LaunchDbSystemFromDatabaseDetails.
            Allowed values for this property are: "STANDARD_EDITION", "ENTERPRISE_EDITION", "ENTERPRISE_EDITION_HIGH_PERFORMANCE", "ENTERPRISE_EDITION_EXTREME_PERFORMANCE"
        :type database_edition: str

        :param disk_redundancy:
            The value to assign to the disk_redundancy property of this LaunchDbSystemFromDatabaseDetails.
            Allowed values for this property are: "HIGH", "NORMAL"
        :type disk_redundancy: str

        :param license_model:
            The value to assign to the license_model property of this LaunchDbSystemFromDatabaseDetails.
            Allowed values for this property are: "LICENSE_INCLUDED", "BRING_YOUR_OWN_LICENSE"
        :type license_model: str

        """
        self.swagger_types = {
            'compartment_id': 'str',
            'fault_domains': 'list[str]',
            'display_name': 'str',
            'availability_domain': 'str',
            'subnet_id': 'str',
            'backup_subnet_id': 'str',
            'nsg_ids': 'list[str]',
            'backup_network_nsg_ids': 'list[str]',
            'shape': 'str',
            'time_zone': 'str',
            'db_system_options': 'DbSystemOptions',
            'storage_volume_performance_mode': 'str',
            'sparse_diskgroup': 'bool',
            'ssh_public_keys': 'list[str]',
            'hostname': 'str',
            'domain': 'str',
            'cpu_core_count': 'int',
            'cluster_name': 'str',
            'data_storage_percentage': 'int',
            'initial_data_storage_size_in_gb': 'int',
            'kms_key_id': 'str',
            'kms_key_version_id': 'str',
            'node_count': 'int',
            'freeform_tags': 'dict(str, str)',
            'defined_tags': 'dict(str, dict(str, object))',
            'source': 'str',
            'private_ip': 'str',
            'data_collection_options': 'DataCollectionOptions',
            'db_home': 'CreateDbHomeFromDatabaseDetails',
            'database_edition': 'str',
            'disk_redundancy': 'str',
            'license_model': 'str'
        }

        self.attribute_map = {
            'compartment_id': 'compartmentId',
            'fault_domains': 'faultDomains',
            'display_name': 'displayName',
            'availability_domain': 'availabilityDomain',
            'subnet_id': 'subnetId',
            'backup_subnet_id': 'backupSubnetId',
            'nsg_ids': 'nsgIds',
            'backup_network_nsg_ids': 'backupNetworkNsgIds',
            'shape': 'shape',
            'time_zone': 'timeZone',
            'db_system_options': 'dbSystemOptions',
            'storage_volume_performance_mode': 'storageVolumePerformanceMode',
            'sparse_diskgroup': 'sparseDiskgroup',
            'ssh_public_keys': 'sshPublicKeys',
            'hostname': 'hostname',
            'domain': 'domain',
            'cpu_core_count': 'cpuCoreCount',
            'cluster_name': 'clusterName',
            'data_storage_percentage': 'dataStoragePercentage',
            'initial_data_storage_size_in_gb': 'initialDataStorageSizeInGB',
            'kms_key_id': 'kmsKeyId',
            'kms_key_version_id': 'kmsKeyVersionId',
            'node_count': 'nodeCount',
            'freeform_tags': 'freeformTags',
            'defined_tags': 'definedTags',
            'source': 'source',
            'private_ip': 'privateIp',
            'data_collection_options': 'dataCollectionOptions',
            'db_home': 'dbHome',
            'database_edition': 'databaseEdition',
            'disk_redundancy': 'diskRedundancy',
            'license_model': 'licenseModel'
        }

        self._compartment_id = None
        self._fault_domains = None
        self._display_name = None
        self._availability_domain = None
        self._subnet_id = None
        self._backup_subnet_id = None
        self._nsg_ids = None
        self._backup_network_nsg_ids = None
        self._shape = None
        self._time_zone = None
        self._db_system_options = None
        self._storage_volume_performance_mode = None
        self._sparse_diskgroup = None
        self._ssh_public_keys = None
        self._hostname = None
        self._domain = None
        self._cpu_core_count = None
        self._cluster_name = None
        self._data_storage_percentage = None
        self._initial_data_storage_size_in_gb = None
        self._kms_key_id = None
        self._kms_key_version_id = None
        self._node_count = None
        self._freeform_tags = None
        self._defined_tags = None
        self._source = None
        self._private_ip = None
        self._data_collection_options = None
        self._db_home = None
        self._database_edition = None
        self._disk_redundancy = None
        self._license_model = None
        self._source = 'DATABASE'

    @property
    def db_home(self):
        """
        **[Required]** Gets the db_home of this LaunchDbSystemFromDatabaseDetails.

        :return: The db_home of this LaunchDbSystemFromDatabaseDetails.
        :rtype: oci.database.models.CreateDbHomeFromDatabaseDetails
        """
        return self._db_home

    @db_home.setter
    def db_home(self, db_home):
        """
        Sets the db_home of this LaunchDbSystemFromDatabaseDetails.

        :param db_home: The db_home of this LaunchDbSystemFromDatabaseDetails.
        :type: oci.database.models.CreateDbHomeFromDatabaseDetails
        """
        self._db_home = db_home

    @property
    def database_edition(self):
        """
        **[Required]** Gets the database_edition of this LaunchDbSystemFromDatabaseDetails.
        The Oracle Database Edition that applies to all the databases on the DB system.
        Exadata DB systems and 2-node RAC DB systems require ENTERPRISE_EDITION_EXTREME_PERFORMANCE.

        Allowed values for this property are: "STANDARD_EDITION", "ENTERPRISE_EDITION", "ENTERPRISE_EDITION_HIGH_PERFORMANCE", "ENTERPRISE_EDITION_EXTREME_PERFORMANCE"


        :return: The database_edition of this LaunchDbSystemFromDatabaseDetails.
        :rtype: str
        """
        return self._database_edition

    @database_edition.setter
    def database_edition(self, database_edition):
        """
        Sets the database_edition of this LaunchDbSystemFromDatabaseDetails.
        The Oracle Database Edition that applies to all the databases on the DB system.
        Exadata DB systems and 2-node RAC DB systems require ENTERPRISE_EDITION_EXTREME_PERFORMANCE.


        :param database_edition: The database_edition of this LaunchDbSystemFromDatabaseDetails.
        :type: str
        """
        allowed_values = ["STANDARD_EDITION", "ENTERPRISE_EDITION", "ENTERPRISE_EDITION_HIGH_PERFORMANCE", "ENTERPRISE_EDITION_EXTREME_PERFORMANCE"]
        if not value_allowed_none_or_none_sentinel(database_edition, allowed_values):
            raise ValueError(
                "Invalid value for `database_edition`, must be None or one of {0}"
                .format(allowed_values)
            )
        self._database_edition = database_edition

    @property
    def disk_redundancy(self):
        """
        Gets the disk_redundancy of this LaunchDbSystemFromDatabaseDetails.
        The type of redundancy configured for the DB system.
        NORMAL 2-way redundancy, recommended for test and development systems.
        HIGH is 3-way redundancy, recommended for production systems.

        Allowed values for this property are: "HIGH", "NORMAL"


        :return: The disk_redundancy of this LaunchDbSystemFromDatabaseDetails.
        :rtype: str
        """
        return self._disk_redundancy

    @disk_redundancy.setter
    def disk_redundancy(self, disk_redundancy):
        """
        Sets the disk_redundancy of this LaunchDbSystemFromDatabaseDetails.
        The type of redundancy configured for the DB system.
        NORMAL 2-way redundancy, recommended for test and development systems.
        HIGH is 3-way redundancy, recommended for production systems.


        :param disk_redundancy: The disk_redundancy of this LaunchDbSystemFromDatabaseDetails.
        :type: str
        """
        allowed_values = ["HIGH", "NORMAL"]
        if not value_allowed_none_or_none_sentinel(disk_redundancy, allowed_values):
            raise ValueError(
                "Invalid value for `disk_redundancy`, must be None or one of {0}"
                .format(allowed_values)
            )
        self._disk_redundancy = disk_redundancy

    @property
    def license_model(self):
        """
        Gets the license_model of this LaunchDbSystemFromDatabaseDetails.
        The Oracle license model that applies to all the databases on the DB system. The default is LICENSE_INCLUDED.

        Allowed values for this property are: "LICENSE_INCLUDED", "BRING_YOUR_OWN_LICENSE"


        :return: The license_model of this LaunchDbSystemFromDatabaseDetails.
        :rtype: str
        """
        return self._license_model

    @license_model.setter
    def license_model(self, license_model):
        """
        Sets the license_model of this LaunchDbSystemFromDatabaseDetails.
        The Oracle license model that applies to all the databases on the DB system. The default is LICENSE_INCLUDED.


        :param license_model: The license_model of this LaunchDbSystemFromDatabaseDetails.
        :type: str
        """
        allowed_values = ["LICENSE_INCLUDED", "BRING_YOUR_OWN_LICENSE"]
        if not value_allowed_none_or_none_sentinel(license_model, allowed_values):
            raise ValueError(
                "Invalid value for `license_model`, must be None or one of {0}"
                .format(allowed_values)
            )
        self._license_model = license_model

    def __repr__(self):
        return formatted_flat_dict(self)

    def __eq__(self, other):
        if other is None:
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not self == other
