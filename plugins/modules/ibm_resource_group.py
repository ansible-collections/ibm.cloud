#!/usr/bin/python
# -*- coding: utf-8 -*-

# (C) Copyright IBM Corp. 2022.
# GNU General Public License v3.0+ (see LICENSE or https://www.gnu.org/licenses/gpl-3.0.txt)

from __future__ import (absolute_import, division, print_function)
__metaclass__ = type


DOCUMENTATION = r'''
---
module: ibm_resource_group
short_description: Manage ibm_resource_group resources.
author: Kavya Handadi (@kavya498)
version_added: "0.0.1-beta0"
description:
    - This module creates, updates, or deletes a ibm_resource_group.
    - By default the module will look for an existing ibm_resource_group.
requirements:
    - "ResourceManagerV2"
options:
    account_id:
        description:
            - The account id of the resource group.
        type: str
    name:
        description:
            - The new name of the resource group.
        type: str
    state_:
        description:
            - The state of the resource group.
        type: str
    id:
        description:
            - The short or long ID of the alias.
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
from ibm_platform_services import ResourceManagerV2
from ibm_cloud_sdk_core import ApiException
from ansible.module_utils.basic import AnsibleModule


def run_module():
    module_args = dict(
        account_id=dict(
            type='str',
            required=False),
        name=dict(
            type='str',
            required=False),
        state_=dict(
            type='str',
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

    account_id = module.params["account_id"]
    name = module.params["name"]
    state_ = module.params["state_"]
    id = module.params["id"]
    state = module.params["state"]

    sdk = config.get_resource_manager_sdk()
    resource_exists = True

    # Check for existence
    if id:
        try:
            sdk.get_resource_group(
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
                sdk.delete_resource_group(
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
                result = sdk.create_resource_group(
                    name=name,
                    account_id=account_id,
                ).get_result()
            except ApiException as ex:
                module.fail_json(msg=ex.message)
            else:
                module.exit_json(changed=True, msg=result)
        else:
            # Update path
            try:
                result = sdk.update_resource_group(
                    id=id,
                    name=name,
                    state=state_,
                ).get_result()
            except ApiException as ex:
                module.fail_json(msg=ex.message)
            else:
                module.exit_json(changed=True, msg=result)


def main():
    run_module()


if __name__ == '__main__':
    main()
