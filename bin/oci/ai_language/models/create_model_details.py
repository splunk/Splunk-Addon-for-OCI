# coding: utf-8
# Copyright (c) 2016, 2023, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.


from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class CreateModelDetails(object):
    """
    The information needed to train a new model
    """

    def __init__(self, **kwargs):
        """
        Initializes a new CreateModelDetails object with values from keyword arguments.
        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param display_name:
            The value to assign to the display_name property of this CreateModelDetails.
        :type display_name: str

        :param description:
            The value to assign to the description property of this CreateModelDetails.
        :type description: str

        :param compartment_id:
            The value to assign to the compartment_id property of this CreateModelDetails.
        :type compartment_id: str

        :param project_id:
            The value to assign to the project_id property of this CreateModelDetails.
        :type project_id: str

        :param model_details:
            The value to assign to the model_details property of this CreateModelDetails.
        :type model_details: oci.ai_language.models.ModelDetails

        :param training_dataset:
            The value to assign to the training_dataset property of this CreateModelDetails.
        :type training_dataset: oci.ai_language.models.DatasetDetails

        :param test_strategy:
            The value to assign to the test_strategy property of this CreateModelDetails.
        :type test_strategy: oci.ai_language.models.TestStrategy

        :param freeform_tags:
            The value to assign to the freeform_tags property of this CreateModelDetails.
        :type freeform_tags: dict(str, str)

        :param defined_tags:
            The value to assign to the defined_tags property of this CreateModelDetails.
        :type defined_tags: dict(str, dict(str, object))

        """
        self.swagger_types = {
            'display_name': 'str',
            'description': 'str',
            'compartment_id': 'str',
            'project_id': 'str',
            'model_details': 'ModelDetails',
            'training_dataset': 'DatasetDetails',
            'test_strategy': 'TestStrategy',
            'freeform_tags': 'dict(str, str)',
            'defined_tags': 'dict(str, dict(str, object))'
        }

        self.attribute_map = {
            'display_name': 'displayName',
            'description': 'description',
            'compartment_id': 'compartmentId',
            'project_id': 'projectId',
            'model_details': 'modelDetails',
            'training_dataset': 'trainingDataset',
            'test_strategy': 'testStrategy',
            'freeform_tags': 'freeformTags',
            'defined_tags': 'definedTags'
        }

        self._display_name = None
        self._description = None
        self._compartment_id = None
        self._project_id = None
        self._model_details = None
        self._training_dataset = None
        self._test_strategy = None
        self._freeform_tags = None
        self._defined_tags = None

    @property
    def display_name(self):
        """
        Gets the display_name of this CreateModelDetails.
        A user-friendly display name for the resource. It does not have to be unique and can be modified. Avoid entering confidential information.


        :return: The display_name of this CreateModelDetails.
        :rtype: str
        """
        return self._display_name

    @display_name.setter
    def display_name(self, display_name):
        """
        Sets the display_name of this CreateModelDetails.
        A user-friendly display name for the resource. It does not have to be unique and can be modified. Avoid entering confidential information.


        :param display_name: The display_name of this CreateModelDetails.
        :type: str
        """
        self._display_name = display_name

    @property
    def description(self):
        """
        Gets the description of this CreateModelDetails.
        A short description of the a model.


        :return: The description of this CreateModelDetails.
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        """
        Sets the description of this CreateModelDetails.
        A short description of the a model.


        :param description: The description of this CreateModelDetails.
        :type: str
        """
        self._description = description

    @property
    def compartment_id(self):
        """
        **[Required]** Gets the compartment_id of this CreateModelDetails.
        The `OCID`__  for the models compartment.

        __ https://docs.cloud.oracle.com/Content/General/Concepts/identifiers.htm


        :return: The compartment_id of this CreateModelDetails.
        :rtype: str
        """
        return self._compartment_id

    @compartment_id.setter
    def compartment_id(self, compartment_id):
        """
        Sets the compartment_id of this CreateModelDetails.
        The `OCID`__  for the models compartment.

        __ https://docs.cloud.oracle.com/Content/General/Concepts/identifiers.htm


        :param compartment_id: The compartment_id of this CreateModelDetails.
        :type: str
        """
        self._compartment_id = compartment_id

    @property
    def project_id(self):
        """
        **[Required]** Gets the project_id of this CreateModelDetails.
        The `OCID`__ of the project to associate with the model.

        __ https://docs.cloud.oracle.com/iaas/Content/General/Concepts/identifiers.htm


        :return: The project_id of this CreateModelDetails.
        :rtype: str
        """
        return self._project_id

    @project_id.setter
    def project_id(self, project_id):
        """
        Sets the project_id of this CreateModelDetails.
        The `OCID`__ of the project to associate with the model.

        __ https://docs.cloud.oracle.com/iaas/Content/General/Concepts/identifiers.htm


        :param project_id: The project_id of this CreateModelDetails.
        :type: str
        """
        self._project_id = project_id

    @property
    def model_details(self):
        """
        **[Required]** Gets the model_details of this CreateModelDetails.

        :return: The model_details of this CreateModelDetails.
        :rtype: oci.ai_language.models.ModelDetails
        """
        return self._model_details

    @model_details.setter
    def model_details(self, model_details):
        """
        Sets the model_details of this CreateModelDetails.

        :param model_details: The model_details of this CreateModelDetails.
        :type: oci.ai_language.models.ModelDetails
        """
        self._model_details = model_details

    @property
    def training_dataset(self):
        """
        **[Required]** Gets the training_dataset of this CreateModelDetails.

        :return: The training_dataset of this CreateModelDetails.
        :rtype: oci.ai_language.models.DatasetDetails
        """
        return self._training_dataset

    @training_dataset.setter
    def training_dataset(self, training_dataset):
        """
        Sets the training_dataset of this CreateModelDetails.

        :param training_dataset: The training_dataset of this CreateModelDetails.
        :type: oci.ai_language.models.DatasetDetails
        """
        self._training_dataset = training_dataset

    @property
    def test_strategy(self):
        """
        Gets the test_strategy of this CreateModelDetails.

        :return: The test_strategy of this CreateModelDetails.
        :rtype: oci.ai_language.models.TestStrategy
        """
        return self._test_strategy

    @test_strategy.setter
    def test_strategy(self, test_strategy):
        """
        Sets the test_strategy of this CreateModelDetails.

        :param test_strategy: The test_strategy of this CreateModelDetails.
        :type: oci.ai_language.models.TestStrategy
        """
        self._test_strategy = test_strategy

    @property
    def freeform_tags(self):
        """
        Gets the freeform_tags of this CreateModelDetails.
        Simple key-value pair that is applied without any predefined name, type or scope. Exists for cross-compatibility only.
        Example: `{\"bar-key\": \"value\"}`


        :return: The freeform_tags of this CreateModelDetails.
        :rtype: dict(str, str)
        """
        return self._freeform_tags

    @freeform_tags.setter
    def freeform_tags(self, freeform_tags):
        """
        Sets the freeform_tags of this CreateModelDetails.
        Simple key-value pair that is applied without any predefined name, type or scope. Exists for cross-compatibility only.
        Example: `{\"bar-key\": \"value\"}`


        :param freeform_tags: The freeform_tags of this CreateModelDetails.
        :type: dict(str, str)
        """
        self._freeform_tags = freeform_tags

    @property
    def defined_tags(self):
        """
        Gets the defined_tags of this CreateModelDetails.
        Defined tags for this resource. Each key is predefined and scoped to a namespace.
        Example: `{\"foo-namespace\": {\"bar-key\": \"value\"}}`


        :return: The defined_tags of this CreateModelDetails.
        :rtype: dict(str, dict(str, object))
        """
        return self._defined_tags

    @defined_tags.setter
    def defined_tags(self, defined_tags):
        """
        Sets the defined_tags of this CreateModelDetails.
        Defined tags for this resource. Each key is predefined and scoped to a namespace.
        Example: `{\"foo-namespace\": {\"bar-key\": \"value\"}}`


        :param defined_tags: The defined_tags of this CreateModelDetails.
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
