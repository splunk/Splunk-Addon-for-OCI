# coding: utf-8
# Copyright (c) 2016, 2023, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.


from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class GenerateDiscoveryReportForDownloadDetails(object):
    """
    Details to generate a downloadable discovery report.
    """

    #: A constant which can be used with the report_format property of a GenerateDiscoveryReportForDownloadDetails.
    #: This constant has a value of "PDF"
    REPORT_FORMAT_PDF = "PDF"

    #: A constant which can be used with the report_format property of a GenerateDiscoveryReportForDownloadDetails.
    #: This constant has a value of "XLS"
    REPORT_FORMAT_XLS = "XLS"

    def __init__(self, **kwargs):
        """
        Initializes a new GenerateDiscoveryReportForDownloadDetails object with values from keyword arguments.
        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param discovery_job_id:
            The value to assign to the discovery_job_id property of this GenerateDiscoveryReportForDownloadDetails.
        :type discovery_job_id: str

        :param report_format:
            The value to assign to the report_format property of this GenerateDiscoveryReportForDownloadDetails.
            Allowed values for this property are: "PDF", "XLS"
        :type report_format: str

        """
        self.swagger_types = {
            'discovery_job_id': 'str',
            'report_format': 'str'
        }

        self.attribute_map = {
            'discovery_job_id': 'discoveryJobId',
            'report_format': 'reportFormat'
        }

        self._discovery_job_id = None
        self._report_format = None

    @property
    def discovery_job_id(self):
        """
        Gets the discovery_job_id of this GenerateDiscoveryReportForDownloadDetails.
        The OCID of the discovery job.


        :return: The discovery_job_id of this GenerateDiscoveryReportForDownloadDetails.
        :rtype: str
        """
        return self._discovery_job_id

    @discovery_job_id.setter
    def discovery_job_id(self, discovery_job_id):
        """
        Sets the discovery_job_id of this GenerateDiscoveryReportForDownloadDetails.
        The OCID of the discovery job.


        :param discovery_job_id: The discovery_job_id of this GenerateDiscoveryReportForDownloadDetails.
        :type: str
        """
        self._discovery_job_id = discovery_job_id

    @property
    def report_format(self):
        """
        **[Required]** Gets the report_format of this GenerateDiscoveryReportForDownloadDetails.
        Format of the report.

        Allowed values for this property are: "PDF", "XLS"


        :return: The report_format of this GenerateDiscoveryReportForDownloadDetails.
        :rtype: str
        """
        return self._report_format

    @report_format.setter
    def report_format(self, report_format):
        """
        Sets the report_format of this GenerateDiscoveryReportForDownloadDetails.
        Format of the report.


        :param report_format: The report_format of this GenerateDiscoveryReportForDownloadDetails.
        :type: str
        """
        allowed_values = ["PDF", "XLS"]
        if not value_allowed_none_or_none_sentinel(report_format, allowed_values):
            raise ValueError(
                "Invalid value for `report_format`, must be None or one of {0}"
                .format(allowed_values)
            )
        self._report_format = report_format

    def __repr__(self):
        return formatted_flat_dict(self)

    def __eq__(self, other):
        if other is None:
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not self == other
