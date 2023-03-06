# coding: utf-8
# Copyright (c) 2016, 2023, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.

from .purge_web_app_acceleration_cache_details import PurgeWebAppAccelerationCacheDetails
from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class PurgeEntireWebAppAccelerationCacheDetails(PurgeWebAppAccelerationCacheDetails):
    """
    Clears all resources from the cache of the WebAppAcceleration.
    """

    def __init__(self, **kwargs):
        """
        Initializes a new PurgeEntireWebAppAccelerationCacheDetails object with values from keyword arguments. The default value of the :py:attr:`~oci.waa.models.PurgeEntireWebAppAccelerationCacheDetails.purge_type` attribute
        of this class is ``ENTIRE_CACHE`` and it should not be changed.
        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param purge_type:
            The value to assign to the purge_type property of this PurgeEntireWebAppAccelerationCacheDetails.
            Allowed values for this property are: "ENTIRE_CACHE"
        :type purge_type: str

        """
        self.swagger_types = {
            'purge_type': 'str'
        }

        self.attribute_map = {
            'purge_type': 'purgeType'
        }

        self._purge_type = None
        self._purge_type = 'ENTIRE_CACHE'

    def __repr__(self):
        return formatted_flat_dict(self)

    def __eq__(self, other):
        if other is None:
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not self == other
