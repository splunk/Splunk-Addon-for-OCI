# coding: utf-8
# Copyright (c) 2016, 2023, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.


from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class Operator(object):
    """
    An operator defines some data integration semantics in a data flow. It may be reading/writing data or transforming the data.
    """

    #: A constant which can be used with the model_type property of a Operator.
    #: This constant has a value of "SOURCE_OPERATOR"
    MODEL_TYPE_SOURCE_OPERATOR = "SOURCE_OPERATOR"

    #: A constant which can be used with the model_type property of a Operator.
    #: This constant has a value of "FILTER_OPERATOR"
    MODEL_TYPE_FILTER_OPERATOR = "FILTER_OPERATOR"

    #: A constant which can be used with the model_type property of a Operator.
    #: This constant has a value of "JOINER_OPERATOR"
    MODEL_TYPE_JOINER_OPERATOR = "JOINER_OPERATOR"

    #: A constant which can be used with the model_type property of a Operator.
    #: This constant has a value of "AGGREGATOR_OPERATOR"
    MODEL_TYPE_AGGREGATOR_OPERATOR = "AGGREGATOR_OPERATOR"

    #: A constant which can be used with the model_type property of a Operator.
    #: This constant has a value of "PROJECTION_OPERATOR"
    MODEL_TYPE_PROJECTION_OPERATOR = "PROJECTION_OPERATOR"

    #: A constant which can be used with the model_type property of a Operator.
    #: This constant has a value of "TARGET_OPERATOR"
    MODEL_TYPE_TARGET_OPERATOR = "TARGET_OPERATOR"

    #: A constant which can be used with the model_type property of a Operator.
    #: This constant has a value of "FLATTEN_OPERATOR"
    MODEL_TYPE_FLATTEN_OPERATOR = "FLATTEN_OPERATOR"

    #: A constant which can be used with the model_type property of a Operator.
    #: This constant has a value of "DISTINCT_OPERATOR"
    MODEL_TYPE_DISTINCT_OPERATOR = "DISTINCT_OPERATOR"

    #: A constant which can be used with the model_type property of a Operator.
    #: This constant has a value of "SORT_OPERATOR"
    MODEL_TYPE_SORT_OPERATOR = "SORT_OPERATOR"

    #: A constant which can be used with the model_type property of a Operator.
    #: This constant has a value of "UNION_OPERATOR"
    MODEL_TYPE_UNION_OPERATOR = "UNION_OPERATOR"

    #: A constant which can be used with the model_type property of a Operator.
    #: This constant has a value of "INTERSECT_OPERATOR"
    MODEL_TYPE_INTERSECT_OPERATOR = "INTERSECT_OPERATOR"

    #: A constant which can be used with the model_type property of a Operator.
    #: This constant has a value of "MINUS_OPERATOR"
    MODEL_TYPE_MINUS_OPERATOR = "MINUS_OPERATOR"

    #: A constant which can be used with the model_type property of a Operator.
    #: This constant has a value of "MERGE_OPERATOR"
    MODEL_TYPE_MERGE_OPERATOR = "MERGE_OPERATOR"

    #: A constant which can be used with the model_type property of a Operator.
    #: This constant has a value of "FUNCTION_OPERATOR"
    MODEL_TYPE_FUNCTION_OPERATOR = "FUNCTION_OPERATOR"

    #: A constant which can be used with the model_type property of a Operator.
    #: This constant has a value of "SPLIT_OPERATOR"
    MODEL_TYPE_SPLIT_OPERATOR = "SPLIT_OPERATOR"

    #: A constant which can be used with the model_type property of a Operator.
    #: This constant has a value of "START_OPERATOR"
    MODEL_TYPE_START_OPERATOR = "START_OPERATOR"

    #: A constant which can be used with the model_type property of a Operator.
    #: This constant has a value of "END_OPERATOR"
    MODEL_TYPE_END_OPERATOR = "END_OPERATOR"

    #: A constant which can be used with the model_type property of a Operator.
    #: This constant has a value of "PIPELINE_OPERATOR"
    MODEL_TYPE_PIPELINE_OPERATOR = "PIPELINE_OPERATOR"

    #: A constant which can be used with the model_type property of a Operator.
    #: This constant has a value of "DECISION_OPERATOR"
    MODEL_TYPE_DECISION_OPERATOR = "DECISION_OPERATOR"

    #: A constant which can be used with the model_type property of a Operator.
    #: This constant has a value of "TASK_OPERATOR"
    MODEL_TYPE_TASK_OPERATOR = "TASK_OPERATOR"

    #: A constant which can be used with the model_type property of a Operator.
    #: This constant has a value of "EXPRESSION_OPERATOR"
    MODEL_TYPE_EXPRESSION_OPERATOR = "EXPRESSION_OPERATOR"

    #: A constant which can be used with the model_type property of a Operator.
    #: This constant has a value of "LOOKUP_OPERATOR"
    MODEL_TYPE_LOOKUP_OPERATOR = "LOOKUP_OPERATOR"

    #: A constant which can be used with the model_type property of a Operator.
    #: This constant has a value of "PIVOT_OPERATOR"
    MODEL_TYPE_PIVOT_OPERATOR = "PIVOT_OPERATOR"

    def __init__(self, **kwargs):
        """
        Initializes a new Operator object with values from keyword arguments. This class has the following subclasses and if you are using this class as input
        to a service operations then you should favor using a subclass over the base class:

        * :class:`~oci.data_integration.models.Joiner`
        * :class:`~oci.data_integration.models.TaskOperator`
        * :class:`~oci.data_integration.models.Flatten`
        * :class:`~oci.data_integration.models.Aggregator`
        * :class:`~oci.data_integration.models.SortOper`
        * :class:`~oci.data_integration.models.Projection`
        * :class:`~oci.data_integration.models.EndOperator`
        * :class:`~oci.data_integration.models.Source`
        * :class:`~oci.data_integration.models.Union`
        * :class:`~oci.data_integration.models.ExpressionOperator`
        * :class:`~oci.data_integration.models.Function`
        * :class:`~oci.data_integration.models.DecisionOperator`
        * :class:`~oci.data_integration.models.Intersect`
        * :class:`~oci.data_integration.models.Target`
        * :class:`~oci.data_integration.models.Distinct`
        * :class:`~oci.data_integration.models.Filter`
        * :class:`~oci.data_integration.models.Lookup`
        * :class:`~oci.data_integration.models.Pivot`
        * :class:`~oci.data_integration.models.StartOperator`
        * :class:`~oci.data_integration.models.MergeOperator`
        * :class:`~oci.data_integration.models.Split`
        * :class:`~oci.data_integration.models.Minus`

        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param model_type:
            The value to assign to the model_type property of this Operator.
            Allowed values for this property are: "SOURCE_OPERATOR", "FILTER_OPERATOR", "JOINER_OPERATOR", "AGGREGATOR_OPERATOR", "PROJECTION_OPERATOR", "TARGET_OPERATOR", "FLATTEN_OPERATOR", "DISTINCT_OPERATOR", "SORT_OPERATOR", "UNION_OPERATOR", "INTERSECT_OPERATOR", "MINUS_OPERATOR", "MERGE_OPERATOR", "FUNCTION_OPERATOR", "SPLIT_OPERATOR", "START_OPERATOR", "END_OPERATOR", "PIPELINE_OPERATOR", "DECISION_OPERATOR", "TASK_OPERATOR", "EXPRESSION_OPERATOR", "LOOKUP_OPERATOR", "PIVOT_OPERATOR", 'UNKNOWN_ENUM_VALUE'.
            Any unrecognized values returned by a service will be mapped to 'UNKNOWN_ENUM_VALUE'.
        :type model_type: str

        :param key:
            The value to assign to the key property of this Operator.
        :type key: str

        :param model_version:
            The value to assign to the model_version property of this Operator.
        :type model_version: str

        :param parent_ref:
            The value to assign to the parent_ref property of this Operator.
        :type parent_ref: oci.data_integration.models.ParentReference

        :param name:
            The value to assign to the name property of this Operator.
        :type name: str

        :param description:
            The value to assign to the description property of this Operator.
        :type description: str

        :param object_version:
            The value to assign to the object_version property of this Operator.
        :type object_version: int

        :param input_ports:
            The value to assign to the input_ports property of this Operator.
        :type input_ports: list[oci.data_integration.models.InputPort]

        :param output_ports:
            The value to assign to the output_ports property of this Operator.
        :type output_ports: list[oci.data_integration.models.TypedObject]

        :param object_status:
            The value to assign to the object_status property of this Operator.
        :type object_status: int

        :param identifier:
            The value to assign to the identifier property of this Operator.
        :type identifier: str

        :param parameters:
            The value to assign to the parameters property of this Operator.
        :type parameters: list[oci.data_integration.models.Parameter]

        :param op_config_values:
            The value to assign to the op_config_values property of this Operator.
        :type op_config_values: oci.data_integration.models.ConfigValues

        """
        self.swagger_types = {
            'model_type': 'str',
            'key': 'str',
            'model_version': 'str',
            'parent_ref': 'ParentReference',
            'name': 'str',
            'description': 'str',
            'object_version': 'int',
            'input_ports': 'list[InputPort]',
            'output_ports': 'list[TypedObject]',
            'object_status': 'int',
            'identifier': 'str',
            'parameters': 'list[Parameter]',
            'op_config_values': 'ConfigValues'
        }

        self.attribute_map = {
            'model_type': 'modelType',
            'key': 'key',
            'model_version': 'modelVersion',
            'parent_ref': 'parentRef',
            'name': 'name',
            'description': 'description',
            'object_version': 'objectVersion',
            'input_ports': 'inputPorts',
            'output_ports': 'outputPorts',
            'object_status': 'objectStatus',
            'identifier': 'identifier',
            'parameters': 'parameters',
            'op_config_values': 'opConfigValues'
        }

        self._model_type = None
        self._key = None
        self._model_version = None
        self._parent_ref = None
        self._name = None
        self._description = None
        self._object_version = None
        self._input_ports = None
        self._output_ports = None
        self._object_status = None
        self._identifier = None
        self._parameters = None
        self._op_config_values = None

    @staticmethod
    def get_subtype(object_dictionary):
        """
        Given the hash representation of a subtype of this class,
        use the info in the hash to return the class of the subtype.
        """
        type = object_dictionary['modelType']

        if type == 'JOINER_OPERATOR':
            return 'Joiner'

        if type == 'TASK_OPERATOR':
            return 'TaskOperator'

        if type == 'FLATTEN_OPERATOR':
            return 'Flatten'

        if type == 'AGGREGATOR_OPERATOR':
            return 'Aggregator'

        if type == 'SORT_OPERATOR':
            return 'SortOper'

        if type == 'PROJECTION_OPERATOR':
            return 'Projection'

        if type == 'END_OPERATOR':
            return 'EndOperator'

        if type == 'SOURCE_OPERATOR':
            return 'Source'

        if type == 'UNION_OPERATOR':
            return 'Union'

        if type == 'EXPRESSION_OPERATOR':
            return 'ExpressionOperator'

        if type == 'FUNCTION_OPERATOR':
            return 'Function'

        if type == 'DECISION_OPERATOR':
            return 'DecisionOperator'

        if type == 'INTERSECT_OPERATOR':
            return 'Intersect'

        if type == 'TARGET_OPERATOR':
            return 'Target'

        if type == 'DISTINCT_OPERATOR':
            return 'Distinct'

        if type == 'FILTER_OPERATOR':
            return 'Filter'

        if type == 'LOOKUP_OPERATOR':
            return 'Lookup'

        if type == 'PIVOT_OPERATOR':
            return 'Pivot'

        if type == 'START_OPERATOR':
            return 'StartOperator'

        if type == 'MERGE_OPERATOR':
            return 'MergeOperator'

        if type == 'SPLIT_OPERATOR':
            return 'Split'

        if type == 'MINUS_OPERATOR':
            return 'Minus'
        else:
            return 'Operator'

    @property
    def model_type(self):
        """
        **[Required]** Gets the model_type of this Operator.
        The model type of the operator.

        Allowed values for this property are: "SOURCE_OPERATOR", "FILTER_OPERATOR", "JOINER_OPERATOR", "AGGREGATOR_OPERATOR", "PROJECTION_OPERATOR", "TARGET_OPERATOR", "FLATTEN_OPERATOR", "DISTINCT_OPERATOR", "SORT_OPERATOR", "UNION_OPERATOR", "INTERSECT_OPERATOR", "MINUS_OPERATOR", "MERGE_OPERATOR", "FUNCTION_OPERATOR", "SPLIT_OPERATOR", "START_OPERATOR", "END_OPERATOR", "PIPELINE_OPERATOR", "DECISION_OPERATOR", "TASK_OPERATOR", "EXPRESSION_OPERATOR", "LOOKUP_OPERATOR", "PIVOT_OPERATOR", 'UNKNOWN_ENUM_VALUE'.
        Any unrecognized values returned by a service will be mapped to 'UNKNOWN_ENUM_VALUE'.


        :return: The model_type of this Operator.
        :rtype: str
        """
        return self._model_type

    @model_type.setter
    def model_type(self, model_type):
        """
        Sets the model_type of this Operator.
        The model type of the operator.


        :param model_type: The model_type of this Operator.
        :type: str
        """
        allowed_values = ["SOURCE_OPERATOR", "FILTER_OPERATOR", "JOINER_OPERATOR", "AGGREGATOR_OPERATOR", "PROJECTION_OPERATOR", "TARGET_OPERATOR", "FLATTEN_OPERATOR", "DISTINCT_OPERATOR", "SORT_OPERATOR", "UNION_OPERATOR", "INTERSECT_OPERATOR", "MINUS_OPERATOR", "MERGE_OPERATOR", "FUNCTION_OPERATOR", "SPLIT_OPERATOR", "START_OPERATOR", "END_OPERATOR", "PIPELINE_OPERATOR", "DECISION_OPERATOR", "TASK_OPERATOR", "EXPRESSION_OPERATOR", "LOOKUP_OPERATOR", "PIVOT_OPERATOR"]
        if not value_allowed_none_or_none_sentinel(model_type, allowed_values):
            model_type = 'UNKNOWN_ENUM_VALUE'
        self._model_type = model_type

    @property
    def key(self):
        """
        Gets the key of this Operator.
        The key of the object.


        :return: The key of this Operator.
        :rtype: str
        """
        return self._key

    @key.setter
    def key(self, key):
        """
        Sets the key of this Operator.
        The key of the object.


        :param key: The key of this Operator.
        :type: str
        """
        self._key = key

    @property
    def model_version(self):
        """
        Gets the model_version of this Operator.
        The model version of an object.


        :return: The model_version of this Operator.
        :rtype: str
        """
        return self._model_version

    @model_version.setter
    def model_version(self, model_version):
        """
        Sets the model_version of this Operator.
        The model version of an object.


        :param model_version: The model_version of this Operator.
        :type: str
        """
        self._model_version = model_version

    @property
    def parent_ref(self):
        """
        Gets the parent_ref of this Operator.

        :return: The parent_ref of this Operator.
        :rtype: oci.data_integration.models.ParentReference
        """
        return self._parent_ref

    @parent_ref.setter
    def parent_ref(self, parent_ref):
        """
        Sets the parent_ref of this Operator.

        :param parent_ref: The parent_ref of this Operator.
        :type: oci.data_integration.models.ParentReference
        """
        self._parent_ref = parent_ref

    @property
    def name(self):
        """
        Gets the name of this Operator.
        Free form text without any restriction on permitted characters. Name can have letters, numbers, and special characters. The value is editable and is restricted to 1000 characters.


        :return: The name of this Operator.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """
        Sets the name of this Operator.
        Free form text without any restriction on permitted characters. Name can have letters, numbers, and special characters. The value is editable and is restricted to 1000 characters.


        :param name: The name of this Operator.
        :type: str
        """
        self._name = name

    @property
    def description(self):
        """
        Gets the description of this Operator.
        Details about the operator.


        :return: The description of this Operator.
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        """
        Sets the description of this Operator.
        Details about the operator.


        :param description: The description of this Operator.
        :type: str
        """
        self._description = description

    @property
    def object_version(self):
        """
        Gets the object_version of this Operator.
        The version of the object that is used to track changes in the object instance.


        :return: The object_version of this Operator.
        :rtype: int
        """
        return self._object_version

    @object_version.setter
    def object_version(self, object_version):
        """
        Sets the object_version of this Operator.
        The version of the object that is used to track changes in the object instance.


        :param object_version: The object_version of this Operator.
        :type: int
        """
        self._object_version = object_version

    @property
    def input_ports(self):
        """
        Gets the input_ports of this Operator.
        An array of input ports.


        :return: The input_ports of this Operator.
        :rtype: list[oci.data_integration.models.InputPort]
        """
        return self._input_ports

    @input_ports.setter
    def input_ports(self, input_ports):
        """
        Sets the input_ports of this Operator.
        An array of input ports.


        :param input_ports: The input_ports of this Operator.
        :type: list[oci.data_integration.models.InputPort]
        """
        self._input_ports = input_ports

    @property
    def output_ports(self):
        """
        Gets the output_ports of this Operator.
        An array of output ports.


        :return: The output_ports of this Operator.
        :rtype: list[oci.data_integration.models.TypedObject]
        """
        return self._output_ports

    @output_ports.setter
    def output_ports(self, output_ports):
        """
        Sets the output_ports of this Operator.
        An array of output ports.


        :param output_ports: The output_ports of this Operator.
        :type: list[oci.data_integration.models.TypedObject]
        """
        self._output_ports = output_ports

    @property
    def object_status(self):
        """
        Gets the object_status of this Operator.
        The status of an object that can be set to value 1 for shallow references across objects, other values reserved.


        :return: The object_status of this Operator.
        :rtype: int
        """
        return self._object_status

    @object_status.setter
    def object_status(self, object_status):
        """
        Sets the object_status of this Operator.
        The status of an object that can be set to value 1 for shallow references across objects, other values reserved.


        :param object_status: The object_status of this Operator.
        :type: int
        """
        self._object_status = object_status

    @property
    def identifier(self):
        """
        Gets the identifier of this Operator.
        Value can only contain upper case letters, underscore, and numbers. It should begin with upper case letter or underscore. The value can be modified.


        :return: The identifier of this Operator.
        :rtype: str
        """
        return self._identifier

    @identifier.setter
    def identifier(self, identifier):
        """
        Sets the identifier of this Operator.
        Value can only contain upper case letters, underscore, and numbers. It should begin with upper case letter or underscore. The value can be modified.


        :param identifier: The identifier of this Operator.
        :type: str
        """
        self._identifier = identifier

    @property
    def parameters(self):
        """
        Gets the parameters of this Operator.
        An array of parameters used in the data flow.


        :return: The parameters of this Operator.
        :rtype: list[oci.data_integration.models.Parameter]
        """
        return self._parameters

    @parameters.setter
    def parameters(self, parameters):
        """
        Sets the parameters of this Operator.
        An array of parameters used in the data flow.


        :param parameters: The parameters of this Operator.
        :type: list[oci.data_integration.models.Parameter]
        """
        self._parameters = parameters

    @property
    def op_config_values(self):
        """
        Gets the op_config_values of this Operator.

        :return: The op_config_values of this Operator.
        :rtype: oci.data_integration.models.ConfigValues
        """
        return self._op_config_values

    @op_config_values.setter
    def op_config_values(self, op_config_values):
        """
        Sets the op_config_values of this Operator.

        :param op_config_values: The op_config_values of this Operator.
        :type: oci.data_integration.models.ConfigValues
        """
        self._op_config_values = op_config_values

    def __repr__(self):
        return formatted_flat_dict(self)

    def __eq__(self, other):
        if other is None:
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not self == other
