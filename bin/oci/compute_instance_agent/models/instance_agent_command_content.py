# coding: utf-8
# Copyright (c) 2016, 2023, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.


from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class InstanceAgentCommandContent(object):
    """
    The contents of the command.
    """

    def __init__(self, **kwargs):
        """
        Initializes a new InstanceAgentCommandContent object with values from keyword arguments.
        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param source:
            The value to assign to the source property of this InstanceAgentCommandContent.
        :type source: oci.compute_instance_agent.models.InstanceAgentCommandSourceDetails

        :param output:
            The value to assign to the output property of this InstanceAgentCommandContent.
        :type output: oci.compute_instance_agent.models.InstanceAgentCommandOutputDetails

        """
        self.swagger_types = {
            'source': 'InstanceAgentCommandSourceDetails',
            'output': 'InstanceAgentCommandOutputDetails'
        }

        self.attribute_map = {
            'source': 'source',
            'output': 'output'
        }

        self._source = None
        self._output = None

    @property
    def source(self):
        """
        **[Required]** Gets the source of this InstanceAgentCommandContent.
        The source of the command.


        :return: The source of this InstanceAgentCommandContent.
        :rtype: oci.compute_instance_agent.models.InstanceAgentCommandSourceDetails
        """
        return self._source

    @source.setter
    def source(self, source):
        """
        Sets the source of this InstanceAgentCommandContent.
        The source of the command.


        :param source: The source of this InstanceAgentCommandContent.
        :type: oci.compute_instance_agent.models.InstanceAgentCommandSourceDetails
        """
        self._source = source

    @property
    def output(self):
        """
        Gets the output of this InstanceAgentCommandContent.
        The output destination for the command.


        :return: The output of this InstanceAgentCommandContent.
        :rtype: oci.compute_instance_agent.models.InstanceAgentCommandOutputDetails
        """
        return self._output

    @output.setter
    def output(self, output):
        """
        Sets the output of this InstanceAgentCommandContent.
        The output destination for the command.


        :param output: The output of this InstanceAgentCommandContent.
        :type: oci.compute_instance_agent.models.InstanceAgentCommandOutputDetails
        """
        self._output = output

    def __repr__(self):
        return formatted_flat_dict(self)

    def __eq__(self, other):
        if other is None:
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not self == other
