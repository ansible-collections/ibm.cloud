# coding: utf-8

# (C) Copyright IBM Corp. 2022.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#      http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

from __future__ import (absolute_import, division, print_function)
__metaclass__ = type


DOCUMENTATION = r'''
---
module: ibm_cm_offering_instance
short_description: Manage ibm_cm_offering_instance resources.
author: Kavya Handadi (@kavya498)
version_added: "1.0.0"
description:
    - This module creates, updates, or deletes a ibm_cm_offering_instance.
    - By default the module will look for an existing ibm_cm_offering_instance.
requirements:
    - "CatalogManagementV1"
options:
    kind_format:
        description:
            - the format this instance has (helm, operator, ova...).
        type: str
    install_plan:
        description: |
            Type of install plan (also known as approval strategy) for operator subscriptions.
            Can be either automatic, which automatically upgrades operators to the latest in a channel,
            or manual, which requires approval on the cluster.
        type: str
    metadata:
        description:
            - Map of metadata values for this offering instance.
        type: dict
    cluster_region:
        description:
            - Cluster region (e.g., us-south).
        type: str
    resource_group_id:
        description:
            - Id of the resource group to provision the offering instance into.
        type: str
    rev:
        description:
            - Cloudant revision.
        type: str
    channel:
        description:
            - Channel to pin the operator subscription to.
        type: str
    label:
        description:
            - the label for this instance.
        type: str
    offering_id:
        description:
            - Offering ID this instance was created from.
        type: str
    version:
        description:
            - The version this instance was installed from (not version id).
        type: str
    url:
        description:
            - url reference to this object.
        type: str
    catalog_id:
        description:
            - Catalog ID this instance was created from.
        type: str
    cluster_id:
        description:
            - Cluster ID.
        type: str
    schematics_workspace_id:
        description:
            - Id of the schematics workspace, for offering instances provisioned through schematics.
        type: str
    id:
        description:
            - provisioned instance ID (part of the CRN).
        type: str
    cluster_namespaces:
        description:
            - List of target namespaces to install into.
        type: list
        elements: str
    cluster_all_namespaces:
        description:
            - designate to install into all namespaces.
        type: bool
    crn:
        description:
            - platform CRN for this instance.
        type: str
    last_operation:
        description:
            - the last operation performed and status.
        type: dict
        suboptions:
            operation:
                description:
                    - last operation performed.
                type: str
            state_:
                description:
                    - state after the last operation performed.
                type: str
            message:
                description:
                    - additional information about the last operation.
                type: str
            transaction_id:
                description:
                    - transaction id from the last operation.
                type: str
            updated:
                description:
                    - Date and time last updated.
                type: str
    instance_identifier:
        description:
            - Version Instance identifier.
        type: str
    x_auth_refresh_token:
        description:
            - IAM Refresh token.
        type: str
    state:
        description:
            - Should the resource be present or absent.
        type: str
        default: present
        choices: [present, absent]
'''

EXAMPLES = r'''
Examples coming soon.
'''

from ..module_utils import config
from ibm_platform_services import CatalogManagementV1
from ibm_cloud_sdk_core import ApiException
from ansible.module_utils.basic import AnsibleModule


def run_module():
    module_args = dict(
        kind_format=dict(
            type='str',
            required=False),
        install_plan=dict(
            type='str',
            required=False),
        metadata=dict(
            type='dict',
            required=False),
        cluster_region=dict(
            type='str',
            required=False),
        resource_group_id=dict(
            type='str',
            required=False),
        rev=dict(
            type='str',
            required=False),
        channel=dict(
            type='str',
            required=False),
        label=dict(
            type='str',
            required=False),
        offering_id=dict(
            type='str',
            required=False),
        version=dict(
            type='str',
            required=False),
        url=dict(
            type='str',
            required=False),
        catalog_id=dict(
            type='str',
            required=False),
        cluster_id=dict(
            type='str',
            required=False),
        schematics_workspace_id=dict(
            type='str',
            required=False),
        id=dict(
            type='str',
            required=False),
        cluster_namespaces=dict(
            type='list',
            elements=str,
            required=False),
        cluster_all_namespaces=dict(
            type='bool',
            required=False),
        crn=dict(
            type='str',
            required=False),
        # Represents the OfferingInstanceLastOperation Python class
        last_operation=dict(
            type='dict',
            options=dict(
                operation=dict(
                    type='str',
                    required=False),
                state_=dict(
                    type='str',
                    required=False),
                message=dict(
                    type='str',
                    required=False),
                transaction_id=dict(
                    type='str',
                    required=False),
                updated=dict(
                    type='str',
                    required=False),
            ),
            required=False),
        instance_identifier=dict(
            type='str',
            required=False),
        x_auth_refresh_token=dict(
            type='str',
            required=False),
        state=dict(
            type='str',
            default='present',
            choices=['absent', 'present'],
            required=False),
    )

    module = AnsibleModule(
        argument_spec=module_args,
        supports_check_mode=False
    )

    kind_format = module.params["kind_format"]
    install_plan = module.params["install_plan"]
    metadata = module.params["metadata"]
    cluster_region = module.params["cluster_region"]
    resource_group_id = module.params["resource_group_id"]
    rev = module.params["rev"]
    channel = module.params["channel"]
    label = module.params["label"]
    offering_id = module.params["offering_id"]
    version = module.params["version"]
    url = module.params["url"]
    catalog_id = module.params["catalog_id"]
    cluster_id = module.params["cluster_id"]
    schematics_workspace_id = module.params["schematics_workspace_id"]
    id = module.params["id"]
    cluster_namespaces = module.params["cluster_namespaces"]
    cluster_all_namespaces = module.params["cluster_all_namespaces"]
    crn = module.params["crn"]
    last_operation = module.params["last_operation"]
    instance_identifier = module.params["instance_identifier"]
    x_auth_refresh_token = module.params["x_auth_refresh_token"]
    state = module.params["state"]

    sdk = config.get_catalog_management_sdk()

    resource_exists = True

    # Check for existence
    if instance_identifier:
        try:
            sdk.get_offering_instance(
                instance_identifier=instance_identifier,
            )
        except ApiException as ex:
            if ex.code == 404:
                resource_exists = False
            else:
                module.fail_json(msg=ex.message)
    else:
        # assume resource does not exist
        resource_exists = False

    # Delete path
    if state == "absent":
        if resource_exists:
            try:
                sdk.delete_offering_instance(
                    instance_identifier=instance_identifier,
                    x_auth_refresh_token=x_auth_refresh_token,
                )
            except ApiException as ex:
                module.fail_json(msg=ex.message)
            else:
                payload = {"id": instance_identifier, "status": "deleted"}
                module.exit_json(changed=True, msg=payload)
        else:
            payload = {"id": instance_identifier, "status": "not_found"}
            module.exit_json(changed=False, msg=payload)

    if state == "present":
        if not resource_exists:
            # Create path
            try:
                result = sdk.create_offering_instance(
                    x_auth_refresh_token=x_auth_refresh_token,
                    id=id,
                    rev=rev,
                    url=url,
                    crn=crn,
                    label=label,
                    catalog_id=catalog_id,
                    offering_id=offering_id,
                    kind_format=kind_format,
                    version=version,
                    cluster_id=cluster_id,
                    cluster_region=cluster_region,
                    cluster_namespaces=cluster_namespaces,
                    cluster_all_namespaces=cluster_all_namespaces,
                    schematics_workspace_id=schematics_workspace_id,
                    resource_group_id=resource_group_id,
                    install_plan=install_plan,
                    channel=channel,
                    metadata=metadata,
                    last_operation=last_operation,
                ).get_result()
            except ApiException as ex:
                module.fail_json(msg=ex.message)
            else:
                module.exit_json(changed=True, msg=result)
        else:
            # Update path
            try:
                result = sdk.put_offering_instance(
                    instance_identifier=instance_identifier,
                    x_auth_refresh_token=x_auth_refresh_token,
                    id=id,
                    rev=rev,
                    url=url,
                    crn=crn,
                    label=label,
                    catalog_id=catalog_id,
                    offering_id=offering_id,
                    kind_format=kind_format,
                    version=version,
                    cluster_id=cluster_id,
                    cluster_region=cluster_region,
                    cluster_namespaces=cluster_namespaces,
                    cluster_all_namespaces=cluster_all_namespaces,
                    schematics_workspace_id=schematics_workspace_id,
                    resource_group_id=resource_group_id,
                    install_plan=install_plan,
                    channel=channel,
                    metadata=metadata,
                    last_operation=last_operation,
                ).get_result()
            except ApiException as ex:
                module.fail_json(msg=ex.message)
            else:
                module.exit_json(changed=True, msg=result)


def main():
    run_module()


if __name__ == '__main__':
    main()
