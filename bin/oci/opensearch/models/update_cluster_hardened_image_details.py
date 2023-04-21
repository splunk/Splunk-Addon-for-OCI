# coding: utf-8
# Copyright (c) 2016, 2023, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.


from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class UpdateClusterHardenedImageDetails(object):
    """
    Information about the cluster's hardened image.
    """

    def __init__(self, **kwargs):
        """
        Initializes a new UpdateClusterHardenedImageDetails object with values from keyword arguments.
        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param cluster_id:
            The value to assign to the cluster_id property of this UpdateClusterHardenedImageDetails.
        :type cluster_id: str

        """
        self.swagger_types = {
            'cluster_id': 'str'
        }

        self.attribute_map = {
            'cluster_id': 'clusterId'
        }

        self._cluster_id = None

    @property
    def cluster_id(self):
        """
        **[Required]** Gets the cluster_id of this UpdateClusterHardenedImageDetails.
        The OCID of the OpenSearch cluster.


        :return: The cluster_id of this UpdateClusterHardenedImageDetails.
        :rtype: str
        """
        return self._cluster_id

    @cluster_id.setter
    def cluster_id(self, cluster_id):
        """
        Sets the cluster_id of this UpdateClusterHardenedImageDetails.
        The OCID of the OpenSearch cluster.


        :param cluster_id: The cluster_id of this UpdateClusterHardenedImageDetails.
        :type: str
        """
        self._cluster_id = cluster_id

    def __repr__(self):
        return formatted_flat_dict(self)

    def __eq__(self, other):
        if other is None:
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not self == other
