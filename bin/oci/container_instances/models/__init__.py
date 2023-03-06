# coding: utf-8
# Copyright (c) 2016, 2023, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.

from __future__ import absolute_import

from .basic_image_pull_secret import BasicImagePullSecret
from .change_container_instance_compartment_details import ChangeContainerInstanceCompartmentDetails
from .container import Container
from .container_collection import ContainerCollection
from .container_command_health_check import ContainerCommandHealthCheck
from .container_config_file import ContainerConfigFile
from .container_config_file_volume import ContainerConfigFileVolume
from .container_dns_config import ContainerDnsConfig
from .container_empty_dir_volume import ContainerEmptyDirVolume
from .container_health_check import ContainerHealthCheck
from .container_http_health_check import ContainerHttpHealthCheck
from .container_instance import ContainerInstance
from .container_instance_collection import ContainerInstanceCollection
from .container_instance_container import ContainerInstanceContainer
from .container_instance_shape_collection import ContainerInstanceShapeCollection
from .container_instance_shape_config import ContainerInstanceShapeConfig
from .container_instance_shape_summary import ContainerInstanceShapeSummary
from .container_instance_summary import ContainerInstanceSummary
from .container_resource_config import ContainerResourceConfig
from .container_summary import ContainerSummary
from .container_tcp_health_check import ContainerTcpHealthCheck
from .container_vnic import ContainerVnic
from .container_volume import ContainerVolume
from .create_basic_image_pull_secret_details import CreateBasicImagePullSecretDetails
from .create_container_command_health_check_details import CreateContainerCommandHealthCheckDetails
from .create_container_config_file_volume_details import CreateContainerConfigFileVolumeDetails
from .create_container_details import CreateContainerDetails
from .create_container_dns_config_details import CreateContainerDnsConfigDetails
from .create_container_empty_dir_volume_details import CreateContainerEmptyDirVolumeDetails
from .create_container_health_check_details import CreateContainerHealthCheckDetails
from .create_container_http_health_check_details import CreateContainerHttpHealthCheckDetails
from .create_container_instance_details import CreateContainerInstanceDetails
from .create_container_instance_shape_config_details import CreateContainerInstanceShapeConfigDetails
from .create_container_resource_config_details import CreateContainerResourceConfigDetails
from .create_container_tcp_health_check_details import CreateContainerTcpHealthCheckDetails
from .create_container_vnic_details import CreateContainerVnicDetails
from .create_container_volume_details import CreateContainerVolumeDetails
from .create_image_pull_secret_details import CreateImagePullSecretDetails
from .create_vault_image_pull_secret_details import CreateVaultImagePullSecretDetails
from .create_volume_mount_details import CreateVolumeMountDetails
from .health_check_http_header import HealthCheckHttpHeader
from .image_pull_secret import ImagePullSecret
from .shape_memory_options import ShapeMemoryOptions
from .shape_networking_bandwidth_options import ShapeNetworkingBandwidthOptions
from .shape_ocpu_options import ShapeOcpuOptions
from .update_container_details import UpdateContainerDetails
from .update_container_instance_details import UpdateContainerInstanceDetails
from .vault_image_pull_secret import VaultImagePullSecret
from .volume_mount import VolumeMount
from .work_request import WorkRequest
from .work_request_error import WorkRequestError
from .work_request_error_collection import WorkRequestErrorCollection
from .work_request_log_entry import WorkRequestLogEntry
from .work_request_log_entry_collection import WorkRequestLogEntryCollection
from .work_request_resource import WorkRequestResource
from .work_request_summary import WorkRequestSummary
from .work_request_summary_collection import WorkRequestSummaryCollection

# Maps type names to classes for container_instances services.
container_instances_type_mapping = {
    "BasicImagePullSecret": BasicImagePullSecret,
    "ChangeContainerInstanceCompartmentDetails": ChangeContainerInstanceCompartmentDetails,
    "Container": Container,
    "ContainerCollection": ContainerCollection,
    "ContainerCommandHealthCheck": ContainerCommandHealthCheck,
    "ContainerConfigFile": ContainerConfigFile,
    "ContainerConfigFileVolume": ContainerConfigFileVolume,
    "ContainerDnsConfig": ContainerDnsConfig,
    "ContainerEmptyDirVolume": ContainerEmptyDirVolume,
    "ContainerHealthCheck": ContainerHealthCheck,
    "ContainerHttpHealthCheck": ContainerHttpHealthCheck,
    "ContainerInstance": ContainerInstance,
    "ContainerInstanceCollection": ContainerInstanceCollection,
    "ContainerInstanceContainer": ContainerInstanceContainer,
    "ContainerInstanceShapeCollection": ContainerInstanceShapeCollection,
    "ContainerInstanceShapeConfig": ContainerInstanceShapeConfig,
    "ContainerInstanceShapeSummary": ContainerInstanceShapeSummary,
    "ContainerInstanceSummary": ContainerInstanceSummary,
    "ContainerResourceConfig": ContainerResourceConfig,
    "ContainerSummary": ContainerSummary,
    "ContainerTcpHealthCheck": ContainerTcpHealthCheck,
    "ContainerVnic": ContainerVnic,
    "ContainerVolume": ContainerVolume,
    "CreateBasicImagePullSecretDetails": CreateBasicImagePullSecretDetails,
    "CreateContainerCommandHealthCheckDetails": CreateContainerCommandHealthCheckDetails,
    "CreateContainerConfigFileVolumeDetails": CreateContainerConfigFileVolumeDetails,
    "CreateContainerDetails": CreateContainerDetails,
    "CreateContainerDnsConfigDetails": CreateContainerDnsConfigDetails,
    "CreateContainerEmptyDirVolumeDetails": CreateContainerEmptyDirVolumeDetails,
    "CreateContainerHealthCheckDetails": CreateContainerHealthCheckDetails,
    "CreateContainerHttpHealthCheckDetails": CreateContainerHttpHealthCheckDetails,
    "CreateContainerInstanceDetails": CreateContainerInstanceDetails,
    "CreateContainerInstanceShapeConfigDetails": CreateContainerInstanceShapeConfigDetails,
    "CreateContainerResourceConfigDetails": CreateContainerResourceConfigDetails,
    "CreateContainerTcpHealthCheckDetails": CreateContainerTcpHealthCheckDetails,
    "CreateContainerVnicDetails": CreateContainerVnicDetails,
    "CreateContainerVolumeDetails": CreateContainerVolumeDetails,
    "CreateImagePullSecretDetails": CreateImagePullSecretDetails,
    "CreateVaultImagePullSecretDetails": CreateVaultImagePullSecretDetails,
    "CreateVolumeMountDetails": CreateVolumeMountDetails,
    "HealthCheckHttpHeader": HealthCheckHttpHeader,
    "ImagePullSecret": ImagePullSecret,
    "ShapeMemoryOptions": ShapeMemoryOptions,
    "ShapeNetworkingBandwidthOptions": ShapeNetworkingBandwidthOptions,
    "ShapeOcpuOptions": ShapeOcpuOptions,
    "UpdateContainerDetails": UpdateContainerDetails,
    "UpdateContainerInstanceDetails": UpdateContainerInstanceDetails,
    "VaultImagePullSecret": VaultImagePullSecret,
    "VolumeMount": VolumeMount,
    "WorkRequest": WorkRequest,
    "WorkRequestError": WorkRequestError,
    "WorkRequestErrorCollection": WorkRequestErrorCollection,
    "WorkRequestLogEntry": WorkRequestLogEntry,
    "WorkRequestLogEntryCollection": WorkRequestLogEntryCollection,
    "WorkRequestResource": WorkRequestResource,
    "WorkRequestSummary": WorkRequestSummary,
    "WorkRequestSummaryCollection": WorkRequestSummaryCollection
}
