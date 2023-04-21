# coding: utf-8
# Copyright (c) 2016, 2023, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.


from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class InvoiceLineSummary(object):
    """
    Product items of the invoice
    """

    def __init__(self, **kwargs):
        """
        Initializes a new InvoiceLineSummary object with values from keyword arguments.
        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param product:
            The value to assign to the product property of this InvoiceLineSummary.
        :type product: str

        :param order_no:
            The value to assign to the order_no property of this InvoiceLineSummary.
        :type order_no: str

        :param part_number:
            The value to assign to the part_number property of this InvoiceLineSummary.
        :type part_number: str

        :param time_start:
            The value to assign to the time_start property of this InvoiceLineSummary.
        :type time_start: datetime

        :param time_end:
            The value to assign to the time_end property of this InvoiceLineSummary.
        :type time_end: datetime

        :param quantity:
            The value to assign to the quantity property of this InvoiceLineSummary.
        :type quantity: float

        :param net_unit_price:
            The value to assign to the net_unit_price property of this InvoiceLineSummary.
        :type net_unit_price: float

        :param total_price:
            The value to assign to the total_price property of this InvoiceLineSummary.
        :type total_price: float

        :param currency:
            The value to assign to the currency property of this InvoiceLineSummary.
        :type currency: oci.osp_gateway.models.Currency

        """
        self.swagger_types = {
            'product': 'str',
            'order_no': 'str',
            'part_number': 'str',
            'time_start': 'datetime',
            'time_end': 'datetime',
            'quantity': 'float',
            'net_unit_price': 'float',
            'total_price': 'float',
            'currency': 'Currency'
        }

        self.attribute_map = {
            'product': 'product',
            'order_no': 'orderNo',
            'part_number': 'partNumber',
            'time_start': 'timeStart',
            'time_end': 'timeEnd',
            'quantity': 'quantity',
            'net_unit_price': 'netUnitPrice',
            'total_price': 'totalPrice',
            'currency': 'currency'
        }

        self._product = None
        self._order_no = None
        self._part_number = None
        self._time_start = None
        self._time_end = None
        self._quantity = None
        self._net_unit_price = None
        self._total_price = None
        self._currency = None

    @property
    def product(self):
        """
        **[Required]** Gets the product of this InvoiceLineSummary.
        Product of the item


        :return: The product of this InvoiceLineSummary.
        :rtype: str
        """
        return self._product

    @product.setter
    def product(self, product):
        """
        Sets the product of this InvoiceLineSummary.
        Product of the item


        :param product: The product of this InvoiceLineSummary.
        :type: str
        """
        self._product = product

    @property
    def order_no(self):
        """
        Gets the order_no of this InvoiceLineSummary.
        Product of the item


        :return: The order_no of this InvoiceLineSummary.
        :rtype: str
        """
        return self._order_no

    @order_no.setter
    def order_no(self, order_no):
        """
        Sets the order_no of this InvoiceLineSummary.
        Product of the item


        :param order_no: The order_no of this InvoiceLineSummary.
        :type: str
        """
        self._order_no = order_no

    @property
    def part_number(self):
        """
        Gets the part_number of this InvoiceLineSummary.
        Part number


        :return: The part_number of this InvoiceLineSummary.
        :rtype: str
        """
        return self._part_number

    @part_number.setter
    def part_number(self, part_number):
        """
        Sets the part_number of this InvoiceLineSummary.
        Part number


        :param part_number: The part_number of this InvoiceLineSummary.
        :type: str
        """
        self._part_number = part_number

    @property
    def time_start(self):
        """
        Gets the time_start of this InvoiceLineSummary.
        Start date


        :return: The time_start of this InvoiceLineSummary.
        :rtype: datetime
        """
        return self._time_start

    @time_start.setter
    def time_start(self, time_start):
        """
        Sets the time_start of this InvoiceLineSummary.
        Start date


        :param time_start: The time_start of this InvoiceLineSummary.
        :type: datetime
        """
        self._time_start = time_start

    @property
    def time_end(self):
        """
        Gets the time_end of this InvoiceLineSummary.
        End date


        :return: The time_end of this InvoiceLineSummary.
        :rtype: datetime
        """
        return self._time_end

    @time_end.setter
    def time_end(self, time_end):
        """
        Sets the time_end of this InvoiceLineSummary.
        End date


        :param time_end: The time_end of this InvoiceLineSummary.
        :type: datetime
        """
        self._time_end = time_end

    @property
    def quantity(self):
        """
        Gets the quantity of this InvoiceLineSummary.
        Quantity of the ordered product


        :return: The quantity of this InvoiceLineSummary.
        :rtype: float
        """
        return self._quantity

    @quantity.setter
    def quantity(self, quantity):
        """
        Sets the quantity of this InvoiceLineSummary.
        Quantity of the ordered product


        :param quantity: The quantity of this InvoiceLineSummary.
        :type: float
        """
        self._quantity = quantity

    @property
    def net_unit_price(self):
        """
        Gets the net_unit_price of this InvoiceLineSummary.
        Unit price of the ordered product


        :return: The net_unit_price of this InvoiceLineSummary.
        :rtype: float
        """
        return self._net_unit_price

    @net_unit_price.setter
    def net_unit_price(self, net_unit_price):
        """
        Sets the net_unit_price of this InvoiceLineSummary.
        Unit price of the ordered product


        :param net_unit_price: The net_unit_price of this InvoiceLineSummary.
        :type: float
        """
        self._net_unit_price = net_unit_price

    @property
    def total_price(self):
        """
        Gets the total_price of this InvoiceLineSummary.
        Total price of the ordered product (Net unit price x quantity)


        :return: The total_price of this InvoiceLineSummary.
        :rtype: float
        """
        return self._total_price

    @total_price.setter
    def total_price(self, total_price):
        """
        Sets the total_price of this InvoiceLineSummary.
        Total price of the ordered product (Net unit price x quantity)


        :param total_price: The total_price of this InvoiceLineSummary.
        :type: float
        """
        self._total_price = total_price

    @property
    def currency(self):
        """
        Gets the currency of this InvoiceLineSummary.

        :return: The currency of this InvoiceLineSummary.
        :rtype: oci.osp_gateway.models.Currency
        """
        return self._currency

    @currency.setter
    def currency(self, currency):
        """
        Sets the currency of this InvoiceLineSummary.

        :param currency: The currency of this InvoiceLineSummary.
        :type: oci.osp_gateway.models.Currency
        """
        self._currency = currency

    def __repr__(self):
        return formatted_flat_dict(self)

    def __eq__(self, other):
        if other is None:
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not self == other
