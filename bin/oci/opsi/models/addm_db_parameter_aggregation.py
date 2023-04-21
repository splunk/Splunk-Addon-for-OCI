# coding: utf-8
# Copyright (c) 2016, 2023, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.


from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class AddmDbParameterAggregation(object):
    """
    Summarizes change history for specific database parameter
    """

    def __init__(self, **kwargs):
        """
        Initializes a new AddmDbParameterAggregation object with values from keyword arguments.
        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param id:
            The value to assign to the id property of this AddmDbParameterAggregation.
        :type id: str

        :param name:
            The value to assign to the name property of this AddmDbParameterAggregation.
        :type name: str

        :param inst_num:
            The value to assign to the inst_num property of this AddmDbParameterAggregation.
        :type inst_num: int

        :param default_value:
            The value to assign to the default_value property of this AddmDbParameterAggregation.
        :type default_value: str

        :param begin_value:
            The value to assign to the begin_value property of this AddmDbParameterAggregation.
        :type begin_value: str

        :param end_value:
            The value to assign to the end_value property of this AddmDbParameterAggregation.
        :type end_value: str

        :param is_changed:
            The value to assign to the is_changed property of this AddmDbParameterAggregation.
        :type is_changed: bool

        :param is_default:
            The value to assign to the is_default property of this AddmDbParameterAggregation.
        :type is_default: bool

        :param value_modified:
            The value to assign to the value_modified property of this AddmDbParameterAggregation.
        :type value_modified: str

        :param is_high_impact:
            The value to assign to the is_high_impact property of this AddmDbParameterAggregation.
        :type is_high_impact: bool

        """
        self.swagger_types = {
            'id': 'str',
            'name': 'str',
            'inst_num': 'int',
            'default_value': 'str',
            'begin_value': 'str',
            'end_value': 'str',
            'is_changed': 'bool',
            'is_default': 'bool',
            'value_modified': 'str',
            'is_high_impact': 'bool'
        }

        self.attribute_map = {
            'id': 'id',
            'name': 'name',
            'inst_num': 'instNum',
            'default_value': 'defaultValue',
            'begin_value': 'beginValue',
            'end_value': 'endValue',
            'is_changed': 'isChanged',
            'is_default': 'isDefault',
            'value_modified': 'valueModified',
            'is_high_impact': 'isHighImpact'
        }

        self._id = None
        self._name = None
        self._inst_num = None
        self._default_value = None
        self._begin_value = None
        self._end_value = None
        self._is_changed = None
        self._is_default = None
        self._value_modified = None
        self._is_high_impact = None

    @property
    def id(self):
        """
        **[Required]** Gets the id of this AddmDbParameterAggregation.
        The `OCID`__ of the Database insight.

        __ https://docs.cloud.oracle.com/iaas/Content/General/Concepts/identifiers.htm


        :return: The id of this AddmDbParameterAggregation.
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """
        Sets the id of this AddmDbParameterAggregation.
        The `OCID`__ of the Database insight.

        __ https://docs.cloud.oracle.com/iaas/Content/General/Concepts/identifiers.htm


        :param id: The id of this AddmDbParameterAggregation.
        :type: str
        """
        self._id = id

    @property
    def name(self):
        """
        **[Required]** Gets the name of this AddmDbParameterAggregation.
        Name of  parameter


        :return: The name of this AddmDbParameterAggregation.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """
        Sets the name of this AddmDbParameterAggregation.
        Name of  parameter


        :param name: The name of this AddmDbParameterAggregation.
        :type: str
        """
        self._name = name

    @property
    def inst_num(self):
        """
        Gets the inst_num of this AddmDbParameterAggregation.
        Number of database instance


        :return: The inst_num of this AddmDbParameterAggregation.
        :rtype: int
        """
        return self._inst_num

    @inst_num.setter
    def inst_num(self, inst_num):
        """
        Sets the inst_num of this AddmDbParameterAggregation.
        Number of database instance


        :param inst_num: The inst_num of this AddmDbParameterAggregation.
        :type: int
        """
        self._inst_num = inst_num

    @property
    def default_value(self):
        """
        Gets the default_value of this AddmDbParameterAggregation.
        Parameter default value


        :return: The default_value of this AddmDbParameterAggregation.
        :rtype: str
        """
        return self._default_value

    @default_value.setter
    def default_value(self, default_value):
        """
        Sets the default_value of this AddmDbParameterAggregation.
        Parameter default value


        :param default_value: The default_value of this AddmDbParameterAggregation.
        :type: str
        """
        self._default_value = default_value

    @property
    def begin_value(self):
        """
        Gets the begin_value of this AddmDbParameterAggregation.
        Parameter value when time period began


        :return: The begin_value of this AddmDbParameterAggregation.
        :rtype: str
        """
        return self._begin_value

    @begin_value.setter
    def begin_value(self, begin_value):
        """
        Sets the begin_value of this AddmDbParameterAggregation.
        Parameter value when time period began


        :param begin_value: The begin_value of this AddmDbParameterAggregation.
        :type: str
        """
        self._begin_value = begin_value

    @property
    def end_value(self):
        """
        Gets the end_value of this AddmDbParameterAggregation.
        Parameter value when time period ended


        :return: The end_value of this AddmDbParameterAggregation.
        :rtype: str
        """
        return self._end_value

    @end_value.setter
    def end_value(self, end_value):
        """
        Sets the end_value of this AddmDbParameterAggregation.
        Parameter value when time period ended


        :param end_value: The end_value of this AddmDbParameterAggregation.
        :type: str
        """
        self._end_value = end_value

    @property
    def is_changed(self):
        """
        **[Required]** Gets the is_changed of this AddmDbParameterAggregation.
        Indicates whether the parameter's value changed during the selected time range (TRUE) or
        did not change during the selected time range (FALSE)


        :return: The is_changed of this AddmDbParameterAggregation.
        :rtype: bool
        """
        return self._is_changed

    @is_changed.setter
    def is_changed(self, is_changed):
        """
        Sets the is_changed of this AddmDbParameterAggregation.
        Indicates whether the parameter's value changed during the selected time range (TRUE) or
        did not change during the selected time range (FALSE)


        :param is_changed: The is_changed of this AddmDbParameterAggregation.
        :type: bool
        """
        self._is_changed = is_changed

    @property
    def is_default(self):
        """
        Gets the is_default of this AddmDbParameterAggregation.
        Indicates whether the parameter's end value was set to the default value (TRUE) or was
        specified in the parameter file (FALSE)


        :return: The is_default of this AddmDbParameterAggregation.
        :rtype: bool
        """
        return self._is_default

    @is_default.setter
    def is_default(self, is_default):
        """
        Sets the is_default of this AddmDbParameterAggregation.
        Indicates whether the parameter's end value was set to the default value (TRUE) or was
        specified in the parameter file (FALSE)


        :param is_default: The is_default of this AddmDbParameterAggregation.
        :type: bool
        """
        self._is_default = is_default

    @property
    def value_modified(self):
        """
        Gets the value_modified of this AddmDbParameterAggregation.
        Indicates whether the parameter has been modified after instance starup
        MODIFIED - Parameter has been modified with ALTER SESSION
        SYSTEM_MOD - Parameter has been modified with ALTER SYSTEM
        FALSE - Parameter has not been modified after instance starup


        :return: The value_modified of this AddmDbParameterAggregation.
        :rtype: str
        """
        return self._value_modified

    @value_modified.setter
    def value_modified(self, value_modified):
        """
        Sets the value_modified of this AddmDbParameterAggregation.
        Indicates whether the parameter has been modified after instance starup
        MODIFIED - Parameter has been modified with ALTER SESSION
        SYSTEM_MOD - Parameter has been modified with ALTER SYSTEM
        FALSE - Parameter has not been modified after instance starup


        :param value_modified: The value_modified of this AddmDbParameterAggregation.
        :type: str
        """
        self._value_modified = value_modified

    @property
    def is_high_impact(self):
        """
        Gets the is_high_impact of this AddmDbParameterAggregation.
        Indicates whether the parameter is a high impact parameter (TRUE) or not (FALSE)


        :return: The is_high_impact of this AddmDbParameterAggregation.
        :rtype: bool
        """
        return self._is_high_impact

    @is_high_impact.setter
    def is_high_impact(self, is_high_impact):
        """
        Sets the is_high_impact of this AddmDbParameterAggregation.
        Indicates whether the parameter is a high impact parameter (TRUE) or not (FALSE)


        :param is_high_impact: The is_high_impact of this AddmDbParameterAggregation.
        :type: bool
        """
        self._is_high_impact = is_high_impact

    def __repr__(self):
        return formatted_flat_dict(self)

    def __eq__(self, other):
        if other is None:
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not self == other
