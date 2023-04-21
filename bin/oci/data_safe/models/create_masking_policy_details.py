# coding: utf-8
# Copyright (c) 2016, 2023, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.


from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class CreateMaskingPolicyDetails(object):
    """
    Details to create a new masking policy. Use either a sensitive data model or a reference
    target database to create your masking policy.

    To use a sensitive data model as the source of masking columns, set the columnSource
    attribute to SENSITIVE_DATA_MODEL and provide the sensitiveDataModelId attribute. After
    creating a masking policy, you can use the AddMaskingColumnsFromSdm operation to automatically
    add all the columns from the associated sensitive data model. In this case, the target
    database associated with the sensitive data model is used for column and masking format validations.

    You can also create a masking policy without using a sensitive data model. In this case,
    you need to associate your masking policy with a target database by setting the columnSource
    attribute to TARGET and providing the targetId attribute. The specified target database is
    used for column and masking format validations.

    After creating a masking policy, you can use the CreateMaskingColumn or PatchMaskingColumns
    operation to manually add columns to the policy. You need to add the parent columns only,
    and it automatically adds the child columns (in referential relationship with the parent
    columns) from the associated sensitive data model or target database.
    """

    def __init__(self, **kwargs):
        """
        Initializes a new CreateMaskingPolicyDetails object with values from keyword arguments.
        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param display_name:
            The value to assign to the display_name property of this CreateMaskingPolicyDetails.
        :type display_name: str

        :param compartment_id:
            The value to assign to the compartment_id property of this CreateMaskingPolicyDetails.
        :type compartment_id: str

        :param description:
            The value to assign to the description property of this CreateMaskingPolicyDetails.
        :type description: str

        :param is_drop_temp_tables_enabled:
            The value to assign to the is_drop_temp_tables_enabled property of this CreateMaskingPolicyDetails.
        :type is_drop_temp_tables_enabled: bool

        :param is_redo_logging_enabled:
            The value to assign to the is_redo_logging_enabled property of this CreateMaskingPolicyDetails.
        :type is_redo_logging_enabled: bool

        :param is_refresh_stats_enabled:
            The value to assign to the is_refresh_stats_enabled property of this CreateMaskingPolicyDetails.
        :type is_refresh_stats_enabled: bool

        :param parallel_degree:
            The value to assign to the parallel_degree property of this CreateMaskingPolicyDetails.
        :type parallel_degree: str

        :param recompile:
            The value to assign to the recompile property of this CreateMaskingPolicyDetails.
        :type recompile: str

        :param pre_masking_script:
            The value to assign to the pre_masking_script property of this CreateMaskingPolicyDetails.
        :type pre_masking_script: str

        :param post_masking_script:
            The value to assign to the post_masking_script property of this CreateMaskingPolicyDetails.
        :type post_masking_script: str

        :param column_source:
            The value to assign to the column_source property of this CreateMaskingPolicyDetails.
        :type column_source: oci.data_safe.models.CreateColumnSourceDetails

        :param freeform_tags:
            The value to assign to the freeform_tags property of this CreateMaskingPolicyDetails.
        :type freeform_tags: dict(str, str)

        :param defined_tags:
            The value to assign to the defined_tags property of this CreateMaskingPolicyDetails.
        :type defined_tags: dict(str, dict(str, object))

        """
        self.swagger_types = {
            'display_name': 'str',
            'compartment_id': 'str',
            'description': 'str',
            'is_drop_temp_tables_enabled': 'bool',
            'is_redo_logging_enabled': 'bool',
            'is_refresh_stats_enabled': 'bool',
            'parallel_degree': 'str',
            'recompile': 'str',
            'pre_masking_script': 'str',
            'post_masking_script': 'str',
            'column_source': 'CreateColumnSourceDetails',
            'freeform_tags': 'dict(str, str)',
            'defined_tags': 'dict(str, dict(str, object))'
        }

        self.attribute_map = {
            'display_name': 'displayName',
            'compartment_id': 'compartmentId',
            'description': 'description',
            'is_drop_temp_tables_enabled': 'isDropTempTablesEnabled',
            'is_redo_logging_enabled': 'isRedoLoggingEnabled',
            'is_refresh_stats_enabled': 'isRefreshStatsEnabled',
            'parallel_degree': 'parallelDegree',
            'recompile': 'recompile',
            'pre_masking_script': 'preMaskingScript',
            'post_masking_script': 'postMaskingScript',
            'column_source': 'columnSource',
            'freeform_tags': 'freeformTags',
            'defined_tags': 'definedTags'
        }

        self._display_name = None
        self._compartment_id = None
        self._description = None
        self._is_drop_temp_tables_enabled = None
        self._is_redo_logging_enabled = None
        self._is_refresh_stats_enabled = None
        self._parallel_degree = None
        self._recompile = None
        self._pre_masking_script = None
        self._post_masking_script = None
        self._column_source = None
        self._freeform_tags = None
        self._defined_tags = None

    @property
    def display_name(self):
        """
        Gets the display_name of this CreateMaskingPolicyDetails.
        The display name of the masking policy. The name does not have to be unique, and it's changeable.


        :return: The display_name of this CreateMaskingPolicyDetails.
        :rtype: str
        """
        return self._display_name

    @display_name.setter
    def display_name(self, display_name):
        """
        Sets the display_name of this CreateMaskingPolicyDetails.
        The display name of the masking policy. The name does not have to be unique, and it's changeable.


        :param display_name: The display_name of this CreateMaskingPolicyDetails.
        :type: str
        """
        self._display_name = display_name

    @property
    def compartment_id(self):
        """
        **[Required]** Gets the compartment_id of this CreateMaskingPolicyDetails.
        The OCID of the compartment where the masking policy should be created.


        :return: The compartment_id of this CreateMaskingPolicyDetails.
        :rtype: str
        """
        return self._compartment_id

    @compartment_id.setter
    def compartment_id(self, compartment_id):
        """
        Sets the compartment_id of this CreateMaskingPolicyDetails.
        The OCID of the compartment where the masking policy should be created.


        :param compartment_id: The compartment_id of this CreateMaskingPolicyDetails.
        :type: str
        """
        self._compartment_id = compartment_id

    @property
    def description(self):
        """
        Gets the description of this CreateMaskingPolicyDetails.
        The description of the masking policy.


        :return: The description of this CreateMaskingPolicyDetails.
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        """
        Sets the description of this CreateMaskingPolicyDetails.
        The description of the masking policy.


        :param description: The description of this CreateMaskingPolicyDetails.
        :type: str
        """
        self._description = description

    @property
    def is_drop_temp_tables_enabled(self):
        """
        Gets the is_drop_temp_tables_enabled of this CreateMaskingPolicyDetails.
        Indicates if the temporary tables created during a masking operation should be dropped after masking. It's enabled by default.
        Set this attribute to false to preserve the temporary tables. Masking creates temporary tables that map the original sensitive
        data values to mask values. By default, these temporary tables are dropped after masking. But, in some cases, you may want
        to preserve this information to track how masking changed your data. Note that doing so compromises security. These tables
        must be dropped before the database is available for unprivileged users.


        :return: The is_drop_temp_tables_enabled of this CreateMaskingPolicyDetails.
        :rtype: bool
        """
        return self._is_drop_temp_tables_enabled

    @is_drop_temp_tables_enabled.setter
    def is_drop_temp_tables_enabled(self, is_drop_temp_tables_enabled):
        """
        Sets the is_drop_temp_tables_enabled of this CreateMaskingPolicyDetails.
        Indicates if the temporary tables created during a masking operation should be dropped after masking. It's enabled by default.
        Set this attribute to false to preserve the temporary tables. Masking creates temporary tables that map the original sensitive
        data values to mask values. By default, these temporary tables are dropped after masking. But, in some cases, you may want
        to preserve this information to track how masking changed your data. Note that doing so compromises security. These tables
        must be dropped before the database is available for unprivileged users.


        :param is_drop_temp_tables_enabled: The is_drop_temp_tables_enabled of this CreateMaskingPolicyDetails.
        :type: bool
        """
        self._is_drop_temp_tables_enabled = is_drop_temp_tables_enabled

    @property
    def is_redo_logging_enabled(self):
        """
        Gets the is_redo_logging_enabled of this CreateMaskingPolicyDetails.
        Indicates if redo logging is enabled during a masking operation. It's disabled by default. Set this attribute to true to
        enable redo logging. By default, masking disables redo logging and flashback logging to purge any original unmasked
        data from logs. However, in certain circumstances when you only want to test masking, rollback changes, and retry masking,
        you could enable logging and use a flashback database to retrieve the original unmasked data after it has been masked.


        :return: The is_redo_logging_enabled of this CreateMaskingPolicyDetails.
        :rtype: bool
        """
        return self._is_redo_logging_enabled

    @is_redo_logging_enabled.setter
    def is_redo_logging_enabled(self, is_redo_logging_enabled):
        """
        Sets the is_redo_logging_enabled of this CreateMaskingPolicyDetails.
        Indicates if redo logging is enabled during a masking operation. It's disabled by default. Set this attribute to true to
        enable redo logging. By default, masking disables redo logging and flashback logging to purge any original unmasked
        data from logs. However, in certain circumstances when you only want to test masking, rollback changes, and retry masking,
        you could enable logging and use a flashback database to retrieve the original unmasked data after it has been masked.


        :param is_redo_logging_enabled: The is_redo_logging_enabled of this CreateMaskingPolicyDetails.
        :type: bool
        """
        self._is_redo_logging_enabled = is_redo_logging_enabled

    @property
    def is_refresh_stats_enabled(self):
        """
        Gets the is_refresh_stats_enabled of this CreateMaskingPolicyDetails.
        Indicates if statistics gathering is enabled. It's enabled by default. Set this attribute to false to disable statistics
        gathering. The masking process gathers statistics on masked database tables after masking completes.


        :return: The is_refresh_stats_enabled of this CreateMaskingPolicyDetails.
        :rtype: bool
        """
        return self._is_refresh_stats_enabled

    @is_refresh_stats_enabled.setter
    def is_refresh_stats_enabled(self, is_refresh_stats_enabled):
        """
        Sets the is_refresh_stats_enabled of this CreateMaskingPolicyDetails.
        Indicates if statistics gathering is enabled. It's enabled by default. Set this attribute to false to disable statistics
        gathering. The masking process gathers statistics on masked database tables after masking completes.


        :param is_refresh_stats_enabled: The is_refresh_stats_enabled of this CreateMaskingPolicyDetails.
        :type: bool
        """
        self._is_refresh_stats_enabled = is_refresh_stats_enabled

    @property
    def parallel_degree(self):
        """
        Gets the parallel_degree of this CreateMaskingPolicyDetails.
        Specifies options to enable parallel execution when running data masking. Allowed values are 'NONE' (no parallelism),
        'DEFAULT' (the Oracle Database computes the optimum degree of parallelism) or an integer value to be used as the degree
        of parallelism. Parallel execution helps effectively use multiple CPUs and improve masking performance. Refer to the
        Oracle Database parallel execution framework when choosing an explicit degree of parallelism.


        :return: The parallel_degree of this CreateMaskingPolicyDetails.
        :rtype: str
        """
        return self._parallel_degree

    @parallel_degree.setter
    def parallel_degree(self, parallel_degree):
        """
        Sets the parallel_degree of this CreateMaskingPolicyDetails.
        Specifies options to enable parallel execution when running data masking. Allowed values are 'NONE' (no parallelism),
        'DEFAULT' (the Oracle Database computes the optimum degree of parallelism) or an integer value to be used as the degree
        of parallelism. Parallel execution helps effectively use multiple CPUs and improve masking performance. Refer to the
        Oracle Database parallel execution framework when choosing an explicit degree of parallelism.


        :param parallel_degree: The parallel_degree of this CreateMaskingPolicyDetails.
        :type: str
        """
        self._parallel_degree = parallel_degree

    @property
    def recompile(self):
        """
        Gets the recompile of this CreateMaskingPolicyDetails.
        Specifies how to recompile invalid objects post data masking. Allowed values are 'SERIAL' (recompile in serial),
        'PARALLEL' (recompile in parallel), 'NONE' (do not recompile). If it's set to PARALLEL, the value of parallelDegree
        attribute is used. Note that few objects may remain invalid even after recompiling once and you may have to further
        recompile manually using UTL_RECOMP package.


        :return: The recompile of this CreateMaskingPolicyDetails.
        :rtype: str
        """
        return self._recompile

    @recompile.setter
    def recompile(self, recompile):
        """
        Sets the recompile of this CreateMaskingPolicyDetails.
        Specifies how to recompile invalid objects post data masking. Allowed values are 'SERIAL' (recompile in serial),
        'PARALLEL' (recompile in parallel), 'NONE' (do not recompile). If it's set to PARALLEL, the value of parallelDegree
        attribute is used. Note that few objects may remain invalid even after recompiling once and you may have to further
        recompile manually using UTL_RECOMP package.


        :param recompile: The recompile of this CreateMaskingPolicyDetails.
        :type: str
        """
        self._recompile = recompile

    @property
    def pre_masking_script(self):
        """
        Gets the pre_masking_script of this CreateMaskingPolicyDetails.
        A pre-masking script, which can contain SQL and PL/SQL statements. It's executed before
        the core masking script generated using the masking policy. It's usually used to perform
        any preparation or prerequisite work before masking data.


        :return: The pre_masking_script of this CreateMaskingPolicyDetails.
        :rtype: str
        """
        return self._pre_masking_script

    @pre_masking_script.setter
    def pre_masking_script(self, pre_masking_script):
        """
        Sets the pre_masking_script of this CreateMaskingPolicyDetails.
        A pre-masking script, which can contain SQL and PL/SQL statements. It's executed before
        the core masking script generated using the masking policy. It's usually used to perform
        any preparation or prerequisite work before masking data.


        :param pre_masking_script: The pre_masking_script of this CreateMaskingPolicyDetails.
        :type: str
        """
        self._pre_masking_script = pre_masking_script

    @property
    def post_masking_script(self):
        """
        Gets the post_masking_script of this CreateMaskingPolicyDetails.
        A post-masking script, which can contain SQL and PL/SQL statements. It's executed after
        the core masking script generated using the masking policy. It's usually used to perform
        additional transformation or cleanup work after masking.


        :return: The post_masking_script of this CreateMaskingPolicyDetails.
        :rtype: str
        """
        return self._post_masking_script

    @post_masking_script.setter
    def post_masking_script(self, post_masking_script):
        """
        Sets the post_masking_script of this CreateMaskingPolicyDetails.
        A post-masking script, which can contain SQL and PL/SQL statements. It's executed after
        the core masking script generated using the masking policy. It's usually used to perform
        additional transformation or cleanup work after masking.


        :param post_masking_script: The post_masking_script of this CreateMaskingPolicyDetails.
        :type: str
        """
        self._post_masking_script = post_masking_script

    @property
    def column_source(self):
        """
        **[Required]** Gets the column_source of this CreateMaskingPolicyDetails.

        :return: The column_source of this CreateMaskingPolicyDetails.
        :rtype: oci.data_safe.models.CreateColumnSourceDetails
        """
        return self._column_source

    @column_source.setter
    def column_source(self, column_source):
        """
        Sets the column_source of this CreateMaskingPolicyDetails.

        :param column_source: The column_source of this CreateMaskingPolicyDetails.
        :type: oci.data_safe.models.CreateColumnSourceDetails
        """
        self._column_source = column_source

    @property
    def freeform_tags(self):
        """
        Gets the freeform_tags of this CreateMaskingPolicyDetails.
        Free-form tags for this resource. Each tag is a simple key-value pair with no predefined name, type, or namespace. For more information, see `Resource Tags`__

        Example: `{\"Department\": \"Finance\"}`

        __ https://docs.cloud.oracle.com/iaas/Content/General/Concepts/resourcetags.htm


        :return: The freeform_tags of this CreateMaskingPolicyDetails.
        :rtype: dict(str, str)
        """
        return self._freeform_tags

    @freeform_tags.setter
    def freeform_tags(self, freeform_tags):
        """
        Sets the freeform_tags of this CreateMaskingPolicyDetails.
        Free-form tags for this resource. Each tag is a simple key-value pair with no predefined name, type, or namespace. For more information, see `Resource Tags`__

        Example: `{\"Department\": \"Finance\"}`

        __ https://docs.cloud.oracle.com/iaas/Content/General/Concepts/resourcetags.htm


        :param freeform_tags: The freeform_tags of this CreateMaskingPolicyDetails.
        :type: dict(str, str)
        """
        self._freeform_tags = freeform_tags

    @property
    def defined_tags(self):
        """
        Gets the defined_tags of this CreateMaskingPolicyDetails.
        Defined tags for this resource. Each key is predefined and scoped to a namespace. For more information, see `Resource Tags`__

        Example: `{\"Operations\": {\"CostCenter\": \"42\"}}`

        __ https://docs.cloud.oracle.com/iaas/Content/General/Concepts/resourcetags.htm


        :return: The defined_tags of this CreateMaskingPolicyDetails.
        :rtype: dict(str, dict(str, object))
        """
        return self._defined_tags

    @defined_tags.setter
    def defined_tags(self, defined_tags):
        """
        Sets the defined_tags of this CreateMaskingPolicyDetails.
        Defined tags for this resource. Each key is predefined and scoped to a namespace. For more information, see `Resource Tags`__

        Example: `{\"Operations\": {\"CostCenter\": \"42\"}}`

        __ https://docs.cloud.oracle.com/iaas/Content/General/Concepts/resourcetags.htm


        :param defined_tags: The defined_tags of this CreateMaskingPolicyDetails.
        :type: dict(str, dict(str, object))
        """
        self._defined_tags = defined_tags

    def __repr__(self):
        return formatted_flat_dict(self)

    def __eq__(self, other):
        if other is None:
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not self == other
