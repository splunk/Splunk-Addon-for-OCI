# coding: utf-8
# Copyright (c) 2016, 2023, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.

from __future__ import absolute_import

from .configuration import Configuration
from .configuration_aggregation import ConfigurationAggregation
from .cost_analysis_ui import CostAnalysisUI
from .create_custom_table_details import CreateCustomTableDetails
from .create_query_details import CreateQueryDetails
from .create_schedule_details import CreateScheduleDetails
from .custom_table import CustomTable
from .custom_table_collection import CustomTableCollection
from .custom_table_summary import CustomTableSummary
from .date_range import DateRange
from .dimension import Dimension
from .dynamic_date_range import DynamicDateRange
from .filter import Filter
from .forecast import Forecast
from .object_storage_location import ObjectStorageLocation
from .query import Query
from .query_collection import QueryCollection
from .query_definition import QueryDefinition
from .query_properties import QueryProperties
from .query_summary import QuerySummary
from .report_query import ReportQuery
from .request_summarized_usages_details import RequestSummarizedUsagesDetails
from .result_location import ResultLocation
from .saved_custom_table import SavedCustomTable
from .schedule import Schedule
from .schedule_collection import ScheduleCollection
from .schedule_summary import ScheduleSummary
from .scheduled_run import ScheduledRun
from .scheduled_run_collection import ScheduledRunCollection
from .scheduled_run_summary import ScheduledRunSummary
from .static_date_range import StaticDateRange
from .tag import Tag
from .update_custom_table_details import UpdateCustomTableDetails
from .update_query_details import UpdateQueryDetails
from .update_schedule_details import UpdateScheduleDetails
from .usage_aggregation import UsageAggregation
from .usage_summary import UsageSummary

# Maps type names to classes for usage_api services.
usage_api_type_mapping = {
    "Configuration": Configuration,
    "ConfigurationAggregation": ConfigurationAggregation,
    "CostAnalysisUI": CostAnalysisUI,
    "CreateCustomTableDetails": CreateCustomTableDetails,
    "CreateQueryDetails": CreateQueryDetails,
    "CreateScheduleDetails": CreateScheduleDetails,
    "CustomTable": CustomTable,
    "CustomTableCollection": CustomTableCollection,
    "CustomTableSummary": CustomTableSummary,
    "DateRange": DateRange,
    "Dimension": Dimension,
    "DynamicDateRange": DynamicDateRange,
    "Filter": Filter,
    "Forecast": Forecast,
    "ObjectStorageLocation": ObjectStorageLocation,
    "Query": Query,
    "QueryCollection": QueryCollection,
    "QueryDefinition": QueryDefinition,
    "QueryProperties": QueryProperties,
    "QuerySummary": QuerySummary,
    "ReportQuery": ReportQuery,
    "RequestSummarizedUsagesDetails": RequestSummarizedUsagesDetails,
    "ResultLocation": ResultLocation,
    "SavedCustomTable": SavedCustomTable,
    "Schedule": Schedule,
    "ScheduleCollection": ScheduleCollection,
    "ScheduleSummary": ScheduleSummary,
    "ScheduledRun": ScheduledRun,
    "ScheduledRunCollection": ScheduledRunCollection,
    "ScheduledRunSummary": ScheduledRunSummary,
    "StaticDateRange": StaticDateRange,
    "Tag": Tag,
    "UpdateCustomTableDetails": UpdateCustomTableDetails,
    "UpdateQueryDetails": UpdateQueryDetails,
    "UpdateScheduleDetails": UpdateScheduleDetails,
    "UsageAggregation": UsageAggregation,
    "UsageSummary": UsageSummary
}
