# coding: utf-8
# Copyright (c) 2016, 2023, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.


from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class CompareContentResult(object):
    """
    The intraline diff result.
    """

    def __init__(self, **kwargs):
        """
        Initializes a new CompareContentResult object with values from keyword arguments.
        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param line_comparison_results:
            The value to assign to the line_comparison_results property of this CompareContentResult.
        :type line_comparison_results: list[oci.log_analytics.models.CompareLineResult]

        """
        self.swagger_types = {
            'line_comparison_results': 'list[CompareLineResult]'
        }

        self.attribute_map = {
            'line_comparison_results': 'lineComparisonResults'
        }

        self._line_comparison_results = None

    @property
    def line_comparison_results(self):
        """
        Gets the line_comparison_results of this CompareContentResult.
        An array of line comparison results.


        :return: The line_comparison_results of this CompareContentResult.
        :rtype: list[oci.log_analytics.models.CompareLineResult]
        """
        return self._line_comparison_results

    @line_comparison_results.setter
    def line_comparison_results(self, line_comparison_results):
        """
        Sets the line_comparison_results of this CompareContentResult.
        An array of line comparison results.


        :param line_comparison_results: The line_comparison_results of this CompareContentResult.
        :type: list[oci.log_analytics.models.CompareLineResult]
        """
        self._line_comparison_results = line_comparison_results

    def __repr__(self):
        return formatted_flat_dict(self)

    def __eq__(self, other):
        if other is None:
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not self == other
