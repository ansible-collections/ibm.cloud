#!/usr/bin/python
# -*- coding: utf-8 -*-

# (C) Copyright IBM Corp. 2022.
# GNU General Public License v3.0+ (see LICENSE or https://www.gnu.org/licenses/gpl-3.0.txt)

# pylint: disable=missing-function-docstring,too-many-branches

from __future__ import (absolute_import, division, print_function)
__metaclass__ = type


DOCUMENTATION = r'''
---
module: ibm_resource_key
short_description: Manage ibm_resource_key resources.
author: Kavya Handadi (@kavya498)
version_added: "0.0.1-beta0"
description:
    - This module creates, updates, or deletes a ibm_resource_key.
    - By default the module will look for an existing ibm_resource_key.
requirements:
    - "ResourceControllerV2"
options:
    role:
        description:
            - The service or custom role name or it's CRN.
        type: str
    name:
        description:
            - The name of the key.
        type: str
    source:
        description:
            - The ID of resource instance or alias.
        type: str
    parameters:
        description: |
            Configuration options represented as key-value pairs.
            Service defined options are passed through to the target resource brokers, whereas platform defined options are not.
        type: dict
        suboptions:
            serviceid_crn:
                description:
                    - An optional platform defined option to reuse an existing IAM serviceId for the role assignment.
                type: str
    id:
        description:
            - The ID of the key.
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
# Todo: change this to external python package format
from ibm_platform_services import ResourceControllerV2
from ansible.module_utils.basic import AnsibleModule
from ibm_cloud_sdk_core import ApiException


def run_module():
    module_args = dict(
        role=dict(
            type='str',
            required=False),
        name=dict(
            type='str',
            required=False),
        source=dict(
            type='str',
            required=False),
        # Represents the ResourceKeyPostParameters Python class
        parameters=dict(
            type='dict',
            options=dict(
                serviceid_crn=dict(
                    type='str',
                    required=False),
            ),
            required=False),
        id=dict(
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

    role = module.params["role"]
    name = module.params["name"]
    source = module.params["source"]
    parameters = module.params["parameters"]
    id = module.params["id"]
    state = module.params["state"]

    # sdk = ResourceControllerV2.new_instance()

    sdk = config.get_resource_contollerV2_sdk()
    resource_exists = True

    # Check for existence
    if id:
        try:
            sdk.get_resource_key(
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
                sdk.delete_resource_key(
                    id=id,
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
        if not resource_exists:
            # Create path
            try:
                result = sdk.create_resource_key(
                    name=name,
                    source=source,
                    parameters=parameters,
                    role=role,
                ).get_result()
            except ApiException as ex:
                module.fail_json(msg=ex.message)
            else:
                module.exit_json(changed=True, msg=result)
        else:
            # Update path
            try:
                result = sdk.update_resource_key(
                    id=id,
                    name=name,
                ).get_result()
            except ApiException as ex:
                module.fail_json(msg=ex.message)
            else:
                module.exit_json(changed=True, msg=result)


def main():
    run_module()


if __name__ == '__main__':
    main()
