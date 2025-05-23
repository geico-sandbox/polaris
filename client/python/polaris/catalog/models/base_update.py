#
# Licensed to the Apache Software Foundation (ASF) under one
# or more contributor license agreements.  See the NOTICE file
# distributed with this work for additional information
# regarding copyright ownership.  The ASF licenses this file
# to you under the Apache License, Version 2.0 (the
# "License"); you may not use this file except in compliance
# with the License.  You may obtain a copy of the License at
#
#   http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing,
# software distributed under the License is distributed on an
# "AS IS" BASIS, WITHOUT WARRANTIES OR CONDITIONS OF ANY
# KIND, either express or implied.  See the License for the
# specific language governing permissions and limitations
# under the License.
#

# coding: utf-8

"""
    Apache Iceberg REST Catalog API

    Defines the specification for the first version of the REST Catalog API. Implementations should ideally support both Iceberg table specs v1 and v2, with priority given to v2.

    The version of the OpenAPI document: 0.0.1
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


from __future__ import annotations
import pprint
import re  # noqa: F401
import json

from importlib import import_module
from pydantic import BaseModel, ConfigDict, StrictStr
from typing import Any, ClassVar, Dict, List, Union
from typing import Optional, Set
from typing_extensions import Self

from typing import TYPE_CHECKING
if TYPE_CHECKING:
    from polaris.catalog.models.add_schema_update import AddSchemaUpdate
    from polaris.catalog.models.add_snapshot_update import AddSnapshotUpdate
    from polaris.catalog.models.add_sort_order_update import AddSortOrderUpdate
    from polaris.catalog.models.add_partition_spec_update import AddPartitionSpecUpdate
    from polaris.catalog.models.add_view_version_update import AddViewVersionUpdate
    from polaris.catalog.models.assign_uuid_update import AssignUUIDUpdate
    from polaris.catalog.models.enable_row_lineage_update import EnableRowLineageUpdate
    from polaris.catalog.models.remove_partition_specs_update import RemovePartitionSpecsUpdate
    from polaris.catalog.models.remove_partition_statistics_update import RemovePartitionStatisticsUpdate
    from polaris.catalog.models.remove_properties_update import RemovePropertiesUpdate
    from polaris.catalog.models.remove_snapshot_ref_update import RemoveSnapshotRefUpdate
    from polaris.catalog.models.remove_snapshots_update import RemoveSnapshotsUpdate
    from polaris.catalog.models.remove_statistics_update import RemoveStatisticsUpdate
    from polaris.catalog.models.set_current_schema_update import SetCurrentSchemaUpdate
    from polaris.catalog.models.set_current_view_version_update import SetCurrentViewVersionUpdate
    from polaris.catalog.models.set_default_sort_order_update import SetDefaultSortOrderUpdate
    from polaris.catalog.models.set_default_spec_update import SetDefaultSpecUpdate
    from polaris.catalog.models.set_location_update import SetLocationUpdate
    from polaris.catalog.models.set_partition_statistics_update import SetPartitionStatisticsUpdate
    from polaris.catalog.models.set_properties_update import SetPropertiesUpdate
    from polaris.catalog.models.set_snapshot_ref_update import SetSnapshotRefUpdate
    from polaris.catalog.models.set_statistics_update import SetStatisticsUpdate
    from polaris.catalog.models.upgrade_format_version_update import UpgradeFormatVersionUpdate

class BaseUpdate(BaseModel):
    """
    BaseUpdate
    """ # noqa: E501
    action: StrictStr
    __properties: ClassVar[List[str]] = ["action"]

    model_config = ConfigDict(
        populate_by_name=True,
        validate_assignment=True,
        protected_namespaces=(),
    )


    # JSON field name that stores the object type
    __discriminator_property_name: ClassVar[str] = 'action'

    # discriminator mappings
    __discriminator_value_class_map: ClassVar[Dict[str, str]] = {
        'add-schema': 'AddSchemaUpdate','add-snapshot': 'AddSnapshotUpdate','add-sort-order': 'AddSortOrderUpdate','add-spec': 'AddPartitionSpecUpdate','add-view-version': 'AddViewVersionUpdate','assign-uuid': 'AssignUUIDUpdate','enable-row-lineage': 'EnableRowLineageUpdate','remove-partition-specs': 'RemovePartitionSpecsUpdate','remove-partition-statistics': 'RemovePartitionStatisticsUpdate','remove-properties': 'RemovePropertiesUpdate','remove-snapshot-ref': 'RemoveSnapshotRefUpdate','remove-snapshots': 'RemoveSnapshotsUpdate','remove-statistics': 'RemoveStatisticsUpdate','set-current-schema': 'SetCurrentSchemaUpdate','set-current-view-version': 'SetCurrentViewVersionUpdate','set-default-sort-order': 'SetDefaultSortOrderUpdate','set-default-spec': 'SetDefaultSpecUpdate','set-location': 'SetLocationUpdate','set-partition-statistics': 'SetPartitionStatisticsUpdate','set-properties': 'SetPropertiesUpdate','set-snapshot-ref': 'SetSnapshotRefUpdate','set-statistics': 'SetStatisticsUpdate','upgrade-format-version': 'UpgradeFormatVersionUpdate'
    }

    @classmethod
    def get_discriminator_value(cls, obj: Dict[str, Any]) -> Optional[str]:
        """Returns the discriminator value (object type) of the data"""
        discriminator_value = obj[cls.__discriminator_property_name]
        if discriminator_value:
            return cls.__discriminator_value_class_map.get(discriminator_value)
        else:
            return None

    def to_str(self) -> str:
        """Returns the string representation of the model using alias"""
        return pprint.pformat(self.model_dump(by_alias=True))

    def to_json(self) -> str:
        """Returns the JSON representation of the model using alias"""
        # TODO: pydantic v2: use .model_dump_json(by_alias=True, exclude_unset=True) instead
        return json.dumps(self.to_dict())

    @classmethod
    def from_json(cls, json_str: str) -> Optional[Union[AddSchemaUpdate, AddSnapshotUpdate, AddSortOrderUpdate, AddPartitionSpecUpdate, AddViewVersionUpdate, AssignUUIDUpdate, EnableRowLineageUpdate, RemovePartitionSpecsUpdate, RemovePartitionStatisticsUpdate, RemovePropertiesUpdate, RemoveSnapshotRefUpdate, RemoveSnapshotsUpdate, RemoveStatisticsUpdate, SetCurrentSchemaUpdate, SetCurrentViewVersionUpdate, SetDefaultSortOrderUpdate, SetDefaultSpecUpdate, SetLocationUpdate, SetPartitionStatisticsUpdate, SetPropertiesUpdate, SetSnapshotRefUpdate, SetStatisticsUpdate, UpgradeFormatVersionUpdate]]:
        """Create an instance of BaseUpdate from a JSON string"""
        return cls.from_dict(json.loads(json_str))

    def to_dict(self) -> Dict[str, Any]:
        """Return the dictionary representation of the model using alias.

        This has the following differences from calling pydantic's
        `self.model_dump(by_alias=True)`:

        * `None` is only added to the output dict for nullable fields that
          were set at model initialization. Other fields with value `None`
          are ignored.
        """
        excluded_fields: Set[str] = set([
        ])

        _dict = self.model_dump(
            by_alias=True,
            exclude=excluded_fields,
            exclude_none=True,
        )
        return _dict

    @classmethod
    def from_dict(cls, obj: Dict[str, Any]) -> Optional[Union[AddSchemaUpdate, AddSnapshotUpdate, AddSortOrderUpdate, AddPartitionSpecUpdate, AddViewVersionUpdate, AssignUUIDUpdate, EnableRowLineageUpdate, RemovePartitionSpecsUpdate, RemovePartitionStatisticsUpdate, RemovePropertiesUpdate, RemoveSnapshotRefUpdate, RemoveSnapshotsUpdate, RemoveStatisticsUpdate, SetCurrentSchemaUpdate, SetCurrentViewVersionUpdate, SetDefaultSortOrderUpdate, SetDefaultSpecUpdate, SetLocationUpdate, SetPartitionStatisticsUpdate, SetPropertiesUpdate, SetSnapshotRefUpdate, SetStatisticsUpdate, UpgradeFormatVersionUpdate]]:
        """Create an instance of BaseUpdate from a dict"""
        # look up the object type based on discriminator mapping
        object_type = cls.get_discriminator_value(obj)
        if object_type ==  'AddSchemaUpdate':
            return import_module("polaris.catalog.models.add_schema_update").AddSchemaUpdate.from_dict(obj)
        if object_type ==  'AddSnapshotUpdate':
            return import_module("polaris.catalog.models.add_snapshot_update").AddSnapshotUpdate.from_dict(obj)
        if object_type ==  'AddSortOrderUpdate':
            return import_module("polaris.catalog.models.add_sort_order_update").AddSortOrderUpdate.from_dict(obj)
        if object_type ==  'AddPartitionSpecUpdate':
            return import_module("polaris.catalog.models.add_partition_spec_update").AddPartitionSpecUpdate.from_dict(obj)
        if object_type ==  'AddViewVersionUpdate':
            return import_module("polaris.catalog.models.add_view_version_update").AddViewVersionUpdate.from_dict(obj)
        if object_type ==  'AssignUUIDUpdate':
            return import_module("polaris.catalog.models.assign_uuid_update").AssignUUIDUpdate.from_dict(obj)
        if object_type ==  'EnableRowLineageUpdate':
            return import_module("polaris.catalog.models.enable_row_lineage_update").EnableRowLineageUpdate.from_dict(obj)
        if object_type ==  'RemovePartitionSpecsUpdate':
            return import_module("polaris.catalog.models.remove_partition_specs_update").RemovePartitionSpecsUpdate.from_dict(obj)
        if object_type ==  'RemovePartitionStatisticsUpdate':
            return import_module("polaris.catalog.models.remove_partition_statistics_update").RemovePartitionStatisticsUpdate.from_dict(obj)
        if object_type ==  'RemovePropertiesUpdate':
            return import_module("polaris.catalog.models.remove_properties_update").RemovePropertiesUpdate.from_dict(obj)
        if object_type ==  'RemoveSnapshotRefUpdate':
            return import_module("polaris.catalog.models.remove_snapshot_ref_update").RemoveSnapshotRefUpdate.from_dict(obj)
        if object_type ==  'RemoveSnapshotsUpdate':
            return import_module("polaris.catalog.models.remove_snapshots_update").RemoveSnapshotsUpdate.from_dict(obj)
        if object_type ==  'RemoveStatisticsUpdate':
            return import_module("polaris.catalog.models.remove_statistics_update").RemoveStatisticsUpdate.from_dict(obj)
        if object_type ==  'SetCurrentSchemaUpdate':
            return import_module("polaris.catalog.models.set_current_schema_update").SetCurrentSchemaUpdate.from_dict(obj)
        if object_type ==  'SetCurrentViewVersionUpdate':
            return import_module("polaris.catalog.models.set_current_view_version_update").SetCurrentViewVersionUpdate.from_dict(obj)
        if object_type ==  'SetDefaultSortOrderUpdate':
            return import_module("polaris.catalog.models.set_default_sort_order_update").SetDefaultSortOrderUpdate.from_dict(obj)
        if object_type ==  'SetDefaultSpecUpdate':
            return import_module("polaris.catalog.models.set_default_spec_update").SetDefaultSpecUpdate.from_dict(obj)
        if object_type ==  'SetLocationUpdate':
            return import_module("polaris.catalog.models.set_location_update").SetLocationUpdate.from_dict(obj)
        if object_type ==  'SetPartitionStatisticsUpdate':
            return import_module("polaris.catalog.models.set_partition_statistics_update").SetPartitionStatisticsUpdate.from_dict(obj)
        if object_type ==  'SetPropertiesUpdate':
            return import_module("polaris.catalog.models.set_properties_update").SetPropertiesUpdate.from_dict(obj)
        if object_type ==  'SetSnapshotRefUpdate':
            return import_module("polaris.catalog.models.set_snapshot_ref_update").SetSnapshotRefUpdate.from_dict(obj)
        if object_type ==  'SetStatisticsUpdate':
            return import_module("polaris.catalog.models.set_statistics_update").SetStatisticsUpdate.from_dict(obj)
        if object_type ==  'UpgradeFormatVersionUpdate':
            return import_module("polaris.catalog.models.upgrade_format_version_update").UpgradeFormatVersionUpdate.from_dict(obj)

        raise ValueError("BaseUpdate failed to lookup discriminator value from " +
                            json.dumps(obj) + ". Discriminator property name: " + cls.__discriminator_property_name +
                            ", mapping: " + json.dumps(cls.__discriminator_value_class_map))


