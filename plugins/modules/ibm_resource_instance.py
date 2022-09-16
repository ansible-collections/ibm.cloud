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

# pylint: disable=missing-function-docstring,too-many-branches


from __future__ import (absolute_import, division, print_function)
__metaclass__ = type


DOCUMENTATION = r'''
---
module: ibm_resource_instance
short_description: Manage ibm_resource_instance resources.
author: Kavya Handadi (@kavya498)
version_added: "1.0.0"
description:
    - This module creates, updates, or deletes a ibm_resource_instance.
    - By default the module will look for an existing ibm_resource_instance.
requirements:
    - "ResourceControllerV2"
options:
    resource_group:
        description:
            - The ID of the resource group.
        type: str
    plan:
        description:
            - The unique ID of the plan associated with the offering. This value is provided by and stored in the global catalog.
        type: str
    allow_cleanup:
        description:
            - A boolean that dictates if the resource instance should be deleted (cleaned up) during the processing of a region instance delete call.
        type: bool
    name:
        description:
            - The name of the instance. Must be 180 characters or less and cannot include any special characters other than `(space) - . _ :`.
        type: str
    parameters:
        description:
            - Configuration options represented as key-value pairs that are passed through to the target resource brokers.
        type: dict
    location:
        description:
            - The deployment location where the instance should be hosted.
        type: str
    tags:
        description:
            - Tags that are attached to the instance after provisioning. These tags can be searched and managed through the Tagging API in IBM Cloud.
        type: list
        elements: str
    entity_lock:
        description: |
            Indicates if the resource instance is locked for further update or delete operations.
            It does not affect actions performed on child resources like aliases, bindings or keys. False by default.
        type: bool
    id:
        description:
            - The ID of the instance.
        type: str
    recursive:
        description:
            - Will delete resource bindings, keys and aliases associated with the instance.
        type: bool
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
# Todo: change this to external python package format
from ibm_platform_services import ResourceControllerV2
from ..module_utils import catalog
from ansible.module_utils.basic import AnsibleModule
from ibm_cloud_sdk_core import ApiException

# pylint: disable=line-too-long,fixme


def run_module():
    module_args = dict(
        resource_group=dict(
            type='str',
            required=False),
        plan=dict(
            type='str',
            required=False),
        allow_cleanup=dict(
            type='bool',
            required=False),
        name=dict(
            type='str',
            required=False),
        parameters=dict(
            type='dict',
            required=False),
        location=dict(
            type='str',
            required=False),
        service=dict(
            type='str',
            required=False),
        tags=dict(
            type='list',
            elements=str,
            required=False),
        entity_lock=dict(
            type='bool',
            required=False),
        id=dict(
            type='str',
            required=False),
        recursive=dict(
            type='bool',
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

    resource_group = module.params["resource_group"]
    plan = module.params["plan"]  # renamed resource_plan_id to plan
    allow_cleanup = module.params["allow_cleanup"]
    name = module.params["name"]
    parameters = module.params["parameters"]
    location = module.params["location"]  # renamed target to location
    tags = module.params["tags"]
    entity_lock = module.params["entity_lock"]
    id = module.params["id"]
    recursive = module.params["recursive"]
    state = module.params["state"]
    service = module.params["service"]  # handcoded argument

    sdk = config.get_resource_contollerV2_sdk()
    resource_exists = True

    # Check for existence
    if id:
        try:
            sdk.get_resource_instance(
                id=id,
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
                sdk.delete_resource_instance(
                    id=id,
                    recursive=recursive,
                )
            except ApiException as ex:
                module.fail_json(msg=ex.message)
            else:
                payload = {"id": id, "status": "deleted"}
                module.exit_json(changed=True, msg=payload)
        else:
            payload = {"id": id, "status": "not_found"}
            module.exit_json(changed=False, msg=payload)

    if state == "present":
        catalogCRN, servicePlanID = '', ''
        if not resource_exists:
            if service is not None:
                serviceID, catalogCRN, servicePlanID = catalog.get_serviceID_targetCRN_planID(
                    service, plan, location)
            # Create path
            try:
                result = sdk.create_resource_instance(
                    name=name,
                    target=catalogCRN,
                    resource_group=resource_group,
                    resource_plan_id=servicePlanID,
                    tags=tags,
                    allow_cleanup=allow_cleanup,
                    parameters=parameters,
                    entity_lock=entity_lock,
                ).get_result()
            except ApiException as ex:
                module.fail_json(msg=ex.message)
            else:
                module.exit_json(changed=True, msg=result)
        else:
            # Update path
            try:
                result = sdk.update_resource_instance(
                    id=id,
                    name=name,
                    parameters=parameters,
                    resource_plan_id=plan,
                    allow_cleanup=allow_cleanup,
                ).get_result()
            except ApiException as ex:
                module.fail_json(msg=ex.message)
            else:
                module.exit_json(changed=True, msg=result)


def main():
    run_module()


if __name__ == '__main__':
    main()
