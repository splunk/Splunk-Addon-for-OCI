# coding: utf-8
# Copyright (c) 2016, 2023, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.


from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class CreateRoverNodeDetails(object):
    """
    The information required to create a RoverNode.
    """

    #: A constant which can be used with the shipping_preference property of a CreateRoverNodeDetails.
    #: This constant has a value of "ORACLE_SHIPPED"
    SHIPPING_PREFERENCE_ORACLE_SHIPPED = "ORACLE_SHIPPED"

    #: A constant which can be used with the shipping_preference property of a CreateRoverNodeDetails.
    #: This constant has a value of "CUSTOMER_PICKUP"
    SHIPPING_PREFERENCE_CUSTOMER_PICKUP = "CUSTOMER_PICKUP"

    #: A constant which can be used with the lifecycle_state property of a CreateRoverNodeDetails.
    #: This constant has a value of "CREATING"
    LIFECYCLE_STATE_CREATING = "CREATING"

    #: A constant which can be used with the lifecycle_state property of a CreateRoverNodeDetails.
    #: This constant has a value of "UPDATING"
    LIFECYCLE_STATE_UPDATING = "UPDATING"

    #: A constant which can be used with the lifecycle_state property of a CreateRoverNodeDetails.
    #: This constant has a value of "ACTIVE"
    LIFECYCLE_STATE_ACTIVE = "ACTIVE"

    #: A constant which can be used with the lifecycle_state property of a CreateRoverNodeDetails.
    #: This constant has a value of "DELETING"
    LIFECYCLE_STATE_DELETING = "DELETING"

    #: A constant which can be used with the lifecycle_state property of a CreateRoverNodeDetails.
    #: This constant has a value of "DELETED"
    LIFECYCLE_STATE_DELETED = "DELETED"

    #: A constant which can be used with the lifecycle_state property of a CreateRoverNodeDetails.
    #: This constant has a value of "FAILED"
    LIFECYCLE_STATE_FAILED = "FAILED"

    #: A constant which can be used with the enclosure_type property of a CreateRoverNodeDetails.
    #: This constant has a value of "RUGGADIZED"
    ENCLOSURE_TYPE_RUGGADIZED = "RUGGADIZED"

    #: A constant which can be used with the enclosure_type property of a CreateRoverNodeDetails.
    #: This constant has a value of "NON_RUGGADIZED"
    ENCLOSURE_TYPE_NON_RUGGADIZED = "NON_RUGGADIZED"

    def __init__(self, **kwargs):
        """
        Initializes a new CreateRoverNodeDetails object with values from keyword arguments.
        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param display_name:
            The value to assign to the display_name property of this CreateRoverNodeDetails.
        :type display_name: str

        :param compartment_id:
            The value to assign to the compartment_id property of this CreateRoverNodeDetails.
        :type compartment_id: str

        :param shape:
            The value to assign to the shape property of this CreateRoverNodeDetails.
        :type shape: str

        :param customer_shipping_address:
            The value to assign to the customer_shipping_address property of this CreateRoverNodeDetails.
        :type customer_shipping_address: oci.rover.models.ShippingAddress

        :param node_workloads:
            The value to assign to the node_workloads property of this CreateRoverNodeDetails.
        :type node_workloads: list[oci.rover.models.RoverWorkload]

        :param super_user_password:
            The value to assign to the super_user_password property of this CreateRoverNodeDetails.
        :type super_user_password: str

        :param unlock_passphrase:
            The value to assign to the unlock_passphrase property of this CreateRoverNodeDetails.
        :type unlock_passphrase: str

        :param point_of_contact:
            The value to assign to the point_of_contact property of this CreateRoverNodeDetails.
        :type point_of_contact: str

        :param point_of_contact_phone_number:
            The value to assign to the point_of_contact_phone_number property of this CreateRoverNodeDetails.
        :type point_of_contact_phone_number: str

        :param shipping_preference:
            The value to assign to the shipping_preference property of this CreateRoverNodeDetails.
            Allowed values for this property are: "ORACLE_SHIPPED", "CUSTOMER_PICKUP"
        :type shipping_preference: str

        :param shipping_vendor:
            The value to assign to the shipping_vendor property of this CreateRoverNodeDetails.
        :type shipping_vendor: str

        :param time_pickup_expected:
            The value to assign to the time_pickup_expected property of this CreateRoverNodeDetails.
        :type time_pickup_expected: datetime

        :param public_key:
            The value to assign to the public_key property of this CreateRoverNodeDetails.
        :type public_key: str

        :param time_return_window_starts:
            The value to assign to the time_return_window_starts property of this CreateRoverNodeDetails.
        :type time_return_window_starts: datetime

        :param time_return_window_ends:
            The value to assign to the time_return_window_ends property of this CreateRoverNodeDetails.
        :type time_return_window_ends: datetime

        :param lifecycle_state:
            The value to assign to the lifecycle_state property of this CreateRoverNodeDetails.
            Allowed values for this property are: "CREATING", "UPDATING", "ACTIVE", "DELETING", "DELETED", "FAILED"
        :type lifecycle_state: str

        :param enclosure_type:
            The value to assign to the enclosure_type property of this CreateRoverNodeDetails.
            Allowed values for this property are: "RUGGADIZED", "NON_RUGGADIZED"
        :type enclosure_type: str

        :param lifecycle_state_details:
            The value to assign to the lifecycle_state_details property of this CreateRoverNodeDetails.
        :type lifecycle_state_details: str

        :param serial_number:
            The value to assign to the serial_number property of this CreateRoverNodeDetails.
        :type serial_number: str

        :param oracle_shipping_tracking_url:
            The value to assign to the oracle_shipping_tracking_url property of this CreateRoverNodeDetails.
        :type oracle_shipping_tracking_url: str

        :param is_import_requested:
            The value to assign to the is_import_requested property of this CreateRoverNodeDetails.
        :type is_import_requested: bool

        :param import_compartment_id:
            The value to assign to the import_compartment_id property of this CreateRoverNodeDetails.
        :type import_compartment_id: str

        :param import_file_bucket:
            The value to assign to the import_file_bucket property of this CreateRoverNodeDetails.
        :type import_file_bucket: str

        :param data_validation_code:
            The value to assign to the data_validation_code property of this CreateRoverNodeDetails.
        :type data_validation_code: str

        :param master_key_id:
            The value to assign to the master_key_id property of this CreateRoverNodeDetails.
        :type master_key_id: str

        :param freeform_tags:
            The value to assign to the freeform_tags property of this CreateRoverNodeDetails.
        :type freeform_tags: dict(str, str)

        :param defined_tags:
            The value to assign to the defined_tags property of this CreateRoverNodeDetails.
        :type defined_tags: dict(str, dict(str, object))

        :param system_tags:
            The value to assign to the system_tags property of this CreateRoverNodeDetails.
        :type system_tags: dict(str, dict(str, object))

        """
        self.swagger_types = {
            'display_name': 'str',
            'compartment_id': 'str',
            'shape': 'str',
            'customer_shipping_address': 'ShippingAddress',
            'node_workloads': 'list[RoverWorkload]',
            'super_user_password': 'str',
            'unlock_passphrase': 'str',
            'point_of_contact': 'str',
            'point_of_contact_phone_number': 'str',
            'shipping_preference': 'str',
            'shipping_vendor': 'str',
            'time_pickup_expected': 'datetime',
            'public_key': 'str',
            'time_return_window_starts': 'datetime',
            'time_return_window_ends': 'datetime',
            'lifecycle_state': 'str',
            'enclosure_type': 'str',
            'lifecycle_state_details': 'str',
            'serial_number': 'str',
            'oracle_shipping_tracking_url': 'str',
            'is_import_requested': 'bool',
            'import_compartment_id': 'str',
            'import_file_bucket': 'str',
            'data_validation_code': 'str',
            'master_key_id': 'str',
            'freeform_tags': 'dict(str, str)',
            'defined_tags': 'dict(str, dict(str, object))',
            'system_tags': 'dict(str, dict(str, object))'
        }

        self.attribute_map = {
            'display_name': 'displayName',
            'compartment_id': 'compartmentId',
            'shape': 'shape',
            'customer_shipping_address': 'customerShippingAddress',
            'node_workloads': 'nodeWorkloads',
            'super_user_password': 'superUserPassword',
            'unlock_passphrase': 'unlockPassphrase',
            'point_of_contact': 'pointOfContact',
            'point_of_contact_phone_number': 'pointOfContactPhoneNumber',
            'shipping_preference': 'shippingPreference',
            'shipping_vendor': 'shippingVendor',
            'time_pickup_expected': 'timePickupExpected',
            'public_key': 'publicKey',
            'time_return_window_starts': 'timeReturnWindowStarts',
            'time_return_window_ends': 'timeReturnWindowEnds',
            'lifecycle_state': 'lifecycleState',
            'enclosure_type': 'enclosureType',
            'lifecycle_state_details': 'lifecycleStateDetails',
            'serial_number': 'serialNumber',
            'oracle_shipping_tracking_url': 'oracleShippingTrackingUrl',
            'is_import_requested': 'isImportRequested',
            'import_compartment_id': 'importCompartmentId',
            'import_file_bucket': 'importFileBucket',
            'data_validation_code': 'dataValidationCode',
            'master_key_id': 'masterKeyId',
            'freeform_tags': 'freeformTags',
            'defined_tags': 'definedTags',
            'system_tags': 'systemTags'
        }

        self._display_name = None
        self._compartment_id = None
        self._shape = None
        self._customer_shipping_address = None
        self._node_workloads = None
        self._super_user_password = None
        self._unlock_passphrase = None
        self._point_of_contact = None
        self._point_of_contact_phone_number = None
        self._shipping_preference = None
        self._shipping_vendor = None
        self._time_pickup_expected = None
        self._public_key = None
        self._time_return_window_starts = None
        self._time_return_window_ends = None
        self._lifecycle_state = None
        self._enclosure_type = None
        self._lifecycle_state_details = None
        self._serial_number = None
        self._oracle_shipping_tracking_url = None
        self._is_import_requested = None
        self._import_compartment_id = None
        self._import_file_bucket = None
        self._data_validation_code = None
        self._master_key_id = None
        self._freeform_tags = None
        self._defined_tags = None
        self._system_tags = None

    @property
    def display_name(self):
        """
        **[Required]** Gets the display_name of this CreateRoverNodeDetails.
        A user-friendly name. Does not have to be unique, and it's changeable. Avoid entering confidential information.


        :return: The display_name of this CreateRoverNodeDetails.
        :rtype: str
        """
        return self._display_name

    @display_name.setter
    def display_name(self, display_name):
        """
        Sets the display_name of this CreateRoverNodeDetails.
        A user-friendly name. Does not have to be unique, and it's changeable. Avoid entering confidential information.


        :param display_name: The display_name of this CreateRoverNodeDetails.
        :type: str
        """
        self._display_name = display_name

    @property
    def compartment_id(self):
        """
        **[Required]** Gets the compartment_id of this CreateRoverNodeDetails.
        The OCID of the compartment containing the RoverNode.


        :return: The compartment_id of this CreateRoverNodeDetails.
        :rtype: str
        """
        return self._compartment_id

    @compartment_id.setter
    def compartment_id(self, compartment_id):
        """
        Sets the compartment_id of this CreateRoverNodeDetails.
        The OCID of the compartment containing the RoverNode.


        :param compartment_id: The compartment_id of this CreateRoverNodeDetails.
        :type: str
        """
        self._compartment_id = compartment_id

    @property
    def shape(self):
        """
        Gets the shape of this CreateRoverNodeDetails.
        The shape of the node.


        :return: The shape of this CreateRoverNodeDetails.
        :rtype: str
        """
        return self._shape

    @shape.setter
    def shape(self, shape):
        """
        Sets the shape of this CreateRoverNodeDetails.
        The shape of the node.


        :param shape: The shape of this CreateRoverNodeDetails.
        :type: str
        """
        self._shape = shape

    @property
    def customer_shipping_address(self):
        """
        Gets the customer_shipping_address of this CreateRoverNodeDetails.

        :return: The customer_shipping_address of this CreateRoverNodeDetails.
        :rtype: oci.rover.models.ShippingAddress
        """
        return self._customer_shipping_address

    @customer_shipping_address.setter
    def customer_shipping_address(self, customer_shipping_address):
        """
        Sets the customer_shipping_address of this CreateRoverNodeDetails.

        :param customer_shipping_address: The customer_shipping_address of this CreateRoverNodeDetails.
        :type: oci.rover.models.ShippingAddress
        """
        self._customer_shipping_address = customer_shipping_address

    @property
    def node_workloads(self):
        """
        Gets the node_workloads of this CreateRoverNodeDetails.
        List of existing workloads that should be provisioned on the node.


        :return: The node_workloads of this CreateRoverNodeDetails.
        :rtype: list[oci.rover.models.RoverWorkload]
        """
        return self._node_workloads

    @node_workloads.setter
    def node_workloads(self, node_workloads):
        """
        Sets the node_workloads of this CreateRoverNodeDetails.
        List of existing workloads that should be provisioned on the node.


        :param node_workloads: The node_workloads of this CreateRoverNodeDetails.
        :type: list[oci.rover.models.RoverWorkload]
        """
        self._node_workloads = node_workloads

    @property
    def super_user_password(self):
        """
        Gets the super_user_password of this CreateRoverNodeDetails.
        Root password for the rover node.


        :return: The super_user_password of this CreateRoverNodeDetails.
        :rtype: str
        """
        return self._super_user_password

    @super_user_password.setter
    def super_user_password(self, super_user_password):
        """
        Sets the super_user_password of this CreateRoverNodeDetails.
        Root password for the rover node.


        :param super_user_password: The super_user_password of this CreateRoverNodeDetails.
        :type: str
        """
        self._super_user_password = super_user_password

    @property
    def unlock_passphrase(self):
        """
        Gets the unlock_passphrase of this CreateRoverNodeDetails.
        Passphrase to unlock the rover node.


        :return: The unlock_passphrase of this CreateRoverNodeDetails.
        :rtype: str
        """
        return self._unlock_passphrase

    @unlock_passphrase.setter
    def unlock_passphrase(self, unlock_passphrase):
        """
        Sets the unlock_passphrase of this CreateRoverNodeDetails.
        Passphrase to unlock the rover node.


        :param unlock_passphrase: The unlock_passphrase of this CreateRoverNodeDetails.
        :type: str
        """
        self._unlock_passphrase = unlock_passphrase

    @property
    def point_of_contact(self):
        """
        Gets the point_of_contact of this CreateRoverNodeDetails.
        Name of point of contact for this order if customer is picking up.


        :return: The point_of_contact of this CreateRoverNodeDetails.
        :rtype: str
        """
        return self._point_of_contact

    @point_of_contact.setter
    def point_of_contact(self, point_of_contact):
        """
        Sets the point_of_contact of this CreateRoverNodeDetails.
        Name of point of contact for this order if customer is picking up.


        :param point_of_contact: The point_of_contact of this CreateRoverNodeDetails.
        :type: str
        """
        self._point_of_contact = point_of_contact

    @property
    def point_of_contact_phone_number(self):
        """
        Gets the point_of_contact_phone_number of this CreateRoverNodeDetails.
        Phone number of point of contact for this order if customer is picking up.


        :return: The point_of_contact_phone_number of this CreateRoverNodeDetails.
        :rtype: str
        """
        return self._point_of_contact_phone_number

    @point_of_contact_phone_number.setter
    def point_of_contact_phone_number(self, point_of_contact_phone_number):
        """
        Sets the point_of_contact_phone_number of this CreateRoverNodeDetails.
        Phone number of point of contact for this order if customer is picking up.


        :param point_of_contact_phone_number: The point_of_contact_phone_number of this CreateRoverNodeDetails.
        :type: str
        """
        self._point_of_contact_phone_number = point_of_contact_phone_number

    @property
    def shipping_preference(self):
        """
        Gets the shipping_preference of this CreateRoverNodeDetails.
        Preference for device delivery.

        Allowed values for this property are: "ORACLE_SHIPPED", "CUSTOMER_PICKUP"


        :return: The shipping_preference of this CreateRoverNodeDetails.
        :rtype: str
        """
        return self._shipping_preference

    @shipping_preference.setter
    def shipping_preference(self, shipping_preference):
        """
        Sets the shipping_preference of this CreateRoverNodeDetails.
        Preference for device delivery.


        :param shipping_preference: The shipping_preference of this CreateRoverNodeDetails.
        :type: str
        """
        allowed_values = ["ORACLE_SHIPPED", "CUSTOMER_PICKUP"]
        if not value_allowed_none_or_none_sentinel(shipping_preference, allowed_values):
            raise ValueError(
                "Invalid value for `shipping_preference`, must be None or one of {0}"
                .format(allowed_values)
            )
        self._shipping_preference = shipping_preference

    @property
    def shipping_vendor(self):
        """
        Gets the shipping_vendor of this CreateRoverNodeDetails.
        Shipping vendor of choice for orace to customer shipping.


        :return: The shipping_vendor of this CreateRoverNodeDetails.
        :rtype: str
        """
        return self._shipping_vendor

    @shipping_vendor.setter
    def shipping_vendor(self, shipping_vendor):
        """
        Sets the shipping_vendor of this CreateRoverNodeDetails.
        Shipping vendor of choice for orace to customer shipping.


        :param shipping_vendor: The shipping_vendor of this CreateRoverNodeDetails.
        :type: str
        """
        self._shipping_vendor = shipping_vendor

    @property
    def time_pickup_expected(self):
        """
        Gets the time_pickup_expected of this CreateRoverNodeDetails.
        Expected date when customer wants to pickup the device if they chose customer pickup.


        :return: The time_pickup_expected of this CreateRoverNodeDetails.
        :rtype: datetime
        """
        return self._time_pickup_expected

    @time_pickup_expected.setter
    def time_pickup_expected(self, time_pickup_expected):
        """
        Sets the time_pickup_expected of this CreateRoverNodeDetails.
        Expected date when customer wants to pickup the device if they chose customer pickup.


        :param time_pickup_expected: The time_pickup_expected of this CreateRoverNodeDetails.
        :type: datetime
        """
        self._time_pickup_expected = time_pickup_expected

    @property
    def public_key(self):
        """
        Gets the public_key of this CreateRoverNodeDetails.
        The public key of the resource principal


        :return: The public_key of this CreateRoverNodeDetails.
        :rtype: str
        """
        return self._public_key

    @public_key.setter
    def public_key(self, public_key):
        """
        Sets the public_key of this CreateRoverNodeDetails.
        The public key of the resource principal


        :param public_key: The public_key of this CreateRoverNodeDetails.
        :type: str
        """
        self._public_key = public_key

    @property
    def time_return_window_starts(self):
        """
        Gets the time_return_window_starts of this CreateRoverNodeDetails.
        Start time for the window to pickup the device from customer.


        :return: The time_return_window_starts of this CreateRoverNodeDetails.
        :rtype: datetime
        """
        return self._time_return_window_starts

    @time_return_window_starts.setter
    def time_return_window_starts(self, time_return_window_starts):
        """
        Sets the time_return_window_starts of this CreateRoverNodeDetails.
        Start time for the window to pickup the device from customer.


        :param time_return_window_starts: The time_return_window_starts of this CreateRoverNodeDetails.
        :type: datetime
        """
        self._time_return_window_starts = time_return_window_starts

    @property
    def time_return_window_ends(self):
        """
        Gets the time_return_window_ends of this CreateRoverNodeDetails.
        End time for the window to pickup the device from customer.


        :return: The time_return_window_ends of this CreateRoverNodeDetails.
        :rtype: datetime
        """
        return self._time_return_window_ends

    @time_return_window_ends.setter
    def time_return_window_ends(self, time_return_window_ends):
        """
        Sets the time_return_window_ends of this CreateRoverNodeDetails.
        End time for the window to pickup the device from customer.


        :param time_return_window_ends: The time_return_window_ends of this CreateRoverNodeDetails.
        :type: datetime
        """
        self._time_return_window_ends = time_return_window_ends

    @property
    def lifecycle_state(self):
        """
        Gets the lifecycle_state of this CreateRoverNodeDetails.
        The current state of the RoverNode.

        Allowed values for this property are: "CREATING", "UPDATING", "ACTIVE", "DELETING", "DELETED", "FAILED"


        :return: The lifecycle_state of this CreateRoverNodeDetails.
        :rtype: str
        """
        return self._lifecycle_state

    @lifecycle_state.setter
    def lifecycle_state(self, lifecycle_state):
        """
        Sets the lifecycle_state of this CreateRoverNodeDetails.
        The current state of the RoverNode.


        :param lifecycle_state: The lifecycle_state of this CreateRoverNodeDetails.
        :type: str
        """
        allowed_values = ["CREATING", "UPDATING", "ACTIVE", "DELETING", "DELETED", "FAILED"]
        if not value_allowed_none_or_none_sentinel(lifecycle_state, allowed_values):
            raise ValueError(
                "Invalid value for `lifecycle_state`, must be None or one of {0}"
                .format(allowed_values)
            )
        self._lifecycle_state = lifecycle_state

    @property
    def enclosure_type(self):
        """
        Gets the enclosure_type of this CreateRoverNodeDetails.
        The type of enclosure rover nodes in this cluster are shipped in.

        Allowed values for this property are: "RUGGADIZED", "NON_RUGGADIZED"


        :return: The enclosure_type of this CreateRoverNodeDetails.
        :rtype: str
        """
        return self._enclosure_type

    @enclosure_type.setter
    def enclosure_type(self, enclosure_type):
        """
        Sets the enclosure_type of this CreateRoverNodeDetails.
        The type of enclosure rover nodes in this cluster are shipped in.


        :param enclosure_type: The enclosure_type of this CreateRoverNodeDetails.
        :type: str
        """
        allowed_values = ["RUGGADIZED", "NON_RUGGADIZED"]
        if not value_allowed_none_or_none_sentinel(enclosure_type, allowed_values):
            raise ValueError(
                "Invalid value for `enclosure_type`, must be None or one of {0}"
                .format(allowed_values)
            )
        self._enclosure_type = enclosure_type

    @property
    def lifecycle_state_details(self):
        """
        Gets the lifecycle_state_details of this CreateRoverNodeDetails.
        A property that can contain details on the lifecycle.


        :return: The lifecycle_state_details of this CreateRoverNodeDetails.
        :rtype: str
        """
        return self._lifecycle_state_details

    @lifecycle_state_details.setter
    def lifecycle_state_details(self, lifecycle_state_details):
        """
        Sets the lifecycle_state_details of this CreateRoverNodeDetails.
        A property that can contain details on the lifecycle.


        :param lifecycle_state_details: The lifecycle_state_details of this CreateRoverNodeDetails.
        :type: str
        """
        self._lifecycle_state_details = lifecycle_state_details

    @property
    def serial_number(self):
        """
        Gets the serial_number of this CreateRoverNodeDetails.
        Serial number of the node.


        :return: The serial_number of this CreateRoverNodeDetails.
        :rtype: str
        """
        return self._serial_number

    @serial_number.setter
    def serial_number(self, serial_number):
        """
        Sets the serial_number of this CreateRoverNodeDetails.
        Serial number of the node.


        :param serial_number: The serial_number of this CreateRoverNodeDetails.
        :type: str
        """
        self._serial_number = serial_number

    @property
    def oracle_shipping_tracking_url(self):
        """
        Gets the oracle_shipping_tracking_url of this CreateRoverNodeDetails.
        Tracking Url for the shipped FmsRoverNode.


        :return: The oracle_shipping_tracking_url of this CreateRoverNodeDetails.
        :rtype: str
        """
        return self._oracle_shipping_tracking_url

    @oracle_shipping_tracking_url.setter
    def oracle_shipping_tracking_url(self, oracle_shipping_tracking_url):
        """
        Sets the oracle_shipping_tracking_url of this CreateRoverNodeDetails.
        Tracking Url for the shipped FmsRoverNode.


        :param oracle_shipping_tracking_url: The oracle_shipping_tracking_url of this CreateRoverNodeDetails.
        :type: str
        """
        self._oracle_shipping_tracking_url = oracle_shipping_tracking_url

    @property
    def is_import_requested(self):
        """
        Gets the is_import_requested of this CreateRoverNodeDetails.
        The flag indicating that customer requests data to be imported to OCI upon Rover node return.


        :return: The is_import_requested of this CreateRoverNodeDetails.
        :rtype: bool
        """
        return self._is_import_requested

    @is_import_requested.setter
    def is_import_requested(self, is_import_requested):
        """
        Sets the is_import_requested of this CreateRoverNodeDetails.
        The flag indicating that customer requests data to be imported to OCI upon Rover node return.


        :param is_import_requested: The is_import_requested of this CreateRoverNodeDetails.
        :type: bool
        """
        self._is_import_requested = is_import_requested

    @property
    def import_compartment_id(self):
        """
        Gets the import_compartment_id of this CreateRoverNodeDetails.
        An OCID of a compartment where data will be imported to upon Rover node return.


        :return: The import_compartment_id of this CreateRoverNodeDetails.
        :rtype: str
        """
        return self._import_compartment_id

    @import_compartment_id.setter
    def import_compartment_id(self, import_compartment_id):
        """
        Sets the import_compartment_id of this CreateRoverNodeDetails.
        An OCID of a compartment where data will be imported to upon Rover node return.


        :param import_compartment_id: The import_compartment_id of this CreateRoverNodeDetails.
        :type: str
        """
        self._import_compartment_id = import_compartment_id

    @property
    def import_file_bucket(self):
        """
        Gets the import_file_bucket of this CreateRoverNodeDetails.
        Name of a bucket where files from NFS share will be imported to upon Rover node return.


        :return: The import_file_bucket of this CreateRoverNodeDetails.
        :rtype: str
        """
        return self._import_file_bucket

    @import_file_bucket.setter
    def import_file_bucket(self, import_file_bucket):
        """
        Sets the import_file_bucket of this CreateRoverNodeDetails.
        Name of a bucket where files from NFS share will be imported to upon Rover node return.


        :param import_file_bucket: The import_file_bucket of this CreateRoverNodeDetails.
        :type: str
        """
        self._import_file_bucket = import_file_bucket

    @property
    def data_validation_code(self):
        """
        Gets the data_validation_code of this CreateRoverNodeDetails.
        Validation code returned by data validation tool. Required for return shipping label generation if data import was requested.


        :return: The data_validation_code of this CreateRoverNodeDetails.
        :rtype: str
        """
        return self._data_validation_code

    @data_validation_code.setter
    def data_validation_code(self, data_validation_code):
        """
        Sets the data_validation_code of this CreateRoverNodeDetails.
        Validation code returned by data validation tool. Required for return shipping label generation if data import was requested.


        :param data_validation_code: The data_validation_code of this CreateRoverNodeDetails.
        :type: str
        """
        self._data_validation_code = data_validation_code

    @property
    def master_key_id(self):
        """
        Gets the master_key_id of this CreateRoverNodeDetails.
        Customer provided master key ID to encrypt secret information. If not provided, Rover's master key will be used for encryption.


        :return: The master_key_id of this CreateRoverNodeDetails.
        :rtype: str
        """
        return self._master_key_id

    @master_key_id.setter
    def master_key_id(self, master_key_id):
        """
        Sets the master_key_id of this CreateRoverNodeDetails.
        Customer provided master key ID to encrypt secret information. If not provided, Rover's master key will be used for encryption.


        :param master_key_id: The master_key_id of this CreateRoverNodeDetails.
        :type: str
        """
        self._master_key_id = master_key_id

    @property
    def freeform_tags(self):
        """
        Gets the freeform_tags of this CreateRoverNodeDetails.
        The freeform tags associated with this resource, if any. Each tag is a simple key-value pair with no
        predefined name, type, or namespace. For more information, see `Resource Tags`__.
        Example: `{\"Department\": \"Finance\"}`

        __ https://docs.cloud.oracle.com/iaas/Content/General/Concepts/resourcetags.htm


        :return: The freeform_tags of this CreateRoverNodeDetails.
        :rtype: dict(str, str)
        """
        return self._freeform_tags

    @freeform_tags.setter
    def freeform_tags(self, freeform_tags):
        """
        Sets the freeform_tags of this CreateRoverNodeDetails.
        The freeform tags associated with this resource, if any. Each tag is a simple key-value pair with no
        predefined name, type, or namespace. For more information, see `Resource Tags`__.
        Example: `{\"Department\": \"Finance\"}`

        __ https://docs.cloud.oracle.com/iaas/Content/General/Concepts/resourcetags.htm


        :param freeform_tags: The freeform_tags of this CreateRoverNodeDetails.
        :type: dict(str, str)
        """
        self._freeform_tags = freeform_tags

    @property
    def defined_tags(self):
        """
        Gets the defined_tags of this CreateRoverNodeDetails.
        The defined tags associated with this resource, if any. Each key is predefined and scoped to namespaces.
        For more information, see `Resource Tags`__.
        Example: `{\"Operations\": {\"CostCenter\": \"42\"}}`

        __ https://docs.cloud.oracle.com/iaas/Content/General/Concepts/resourcetags.htm


        :return: The defined_tags of this CreateRoverNodeDetails.
        :rtype: dict(str, dict(str, object))
        """
        return self._defined_tags

    @defined_tags.setter
    def defined_tags(self, defined_tags):
        """
        Sets the defined_tags of this CreateRoverNodeDetails.
        The defined tags associated with this resource, if any. Each key is predefined and scoped to namespaces.
        For more information, see `Resource Tags`__.
        Example: `{\"Operations\": {\"CostCenter\": \"42\"}}`

        __ https://docs.cloud.oracle.com/iaas/Content/General/Concepts/resourcetags.htm


        :param defined_tags: The defined_tags of this CreateRoverNodeDetails.
        :type: dict(str, dict(str, object))
        """
        self._defined_tags = defined_tags

    @property
    def system_tags(self):
        """
        Gets the system_tags of this CreateRoverNodeDetails.
        The system tags associated with this resource, if any. The system tags are set by Oracle cloud infrastructure services. Each key is predefined and scoped to namespaces.
        For more information, see `Resource Tags`__.
        Example: `{orcl-cloud: {free-tier-retain: true}}`

        __ https://docs.cloud.oracle.com/iaas/Content/General/Concepts/resourcetags.htm


        :return: The system_tags of this CreateRoverNodeDetails.
        :rtype: dict(str, dict(str, object))
        """
        return self._system_tags

    @system_tags.setter
    def system_tags(self, system_tags):
        """
        Sets the system_tags of this CreateRoverNodeDetails.
        The system tags associated with this resource, if any. The system tags are set by Oracle cloud infrastructure services. Each key is predefined and scoped to namespaces.
        For more information, see `Resource Tags`__.
        Example: `{orcl-cloud: {free-tier-retain: true}}`

        __ https://docs.cloud.oracle.com/iaas/Content/General/Concepts/resourcetags.htm


        :param system_tags: The system_tags of this CreateRoverNodeDetails.
        :type: dict(str, dict(str, object))
        """
        self._system_tags = system_tags

    def __repr__(self):
        return formatted_flat_dict(self)

    def __eq__(self, other):
        if other is None:
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not self == other
