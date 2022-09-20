#!/usr/bin/python
# -*- coding: utf-8 -*-

# (C) Copyright IBM Corp. 2022.
# GNU General Public License v3.0+ (see LICENSE or https://www.gnu.org/licenses/gpl-3.0.txt)

from __future__ import (absolute_import, division, print_function)
__metaclass__ = type


DOCUMENTATION = r'''
---
module: ibm_resource_alias
short_description: Manage ibm_resource_alias resources.
author: Kavya Handadi (@kavya498)
version_added: "0.0.1-beta0"
description:
    - This module creates, updates, or deletes a ibm_resource_alias.
    - By default the module will look for an existing ibm_resource_alias.
requirements:
    - "ResourceControllerV2"
options:
    name:
        description:
            - The name of the alias. Must be 180 characters or less and cannot include any special characters other than `(space) - . _ :`.
        type: str
    source:
        description:
            - The ID of resource instance.
        type: str
    target:
        description:
            - The CRN of target name(space) in a specific environment, for example, space in Dallas YP, CFEE instance etc.
        type: str
    id:
        description:
            - The ID of the alias.
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
from ibm_platform_services import ResourceControllerV2
from ibm_cloud_sdk_core import ApiException
from ansible.module_utils.basic import AnsibleModule


def run_module():
    module_args = dict(
        name=dict(
            type='str',
            required=False),
        source=dict(
            type='str',
            required=False),
        target=dict(
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

    name = module.params["name"]
    source = module.params["source"]
    target = module.params["target"]
    id = module.params["id"]
    state = module.params["state"]

    sdk = config.get_resource_contollerV2_sdk()

    resource_exists = True

    # Check for existence
    if id:
        try:
            sdk.get_resource_alias(
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
                sdk.delete_resource_alias(
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
                result = sdk.create_resource_alias(
                    name=name,
                    source=source,
                    target=target,
                ).get_result()
            except ApiException as ex:
                module.fail_json(msg=ex.message)
            else:
                module.exit_json(changed=True, msg=result)
        else:
            # Update path
            try:
                result = sdk.update_resource_alias(
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
