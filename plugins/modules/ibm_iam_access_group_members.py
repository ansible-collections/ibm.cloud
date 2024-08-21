#!/usr/bin/python
# -*- coding: utf-8 -*-

# (C) Copyright IBM Corp. 2022.
# GNU General Public License v3.0+ (see LICENSE or https://www.gnu.org/licenses/gpl-3.0.txt)

from __future__ import (absolute_import, division, print_function)
__metaclass__ = type


DOCUMENTATION = r'''
---
module: ibm_iam_access_group_members
short_description: Manage ibm_iam_access_group_members resources.
author: 
  - Kavya Handadi (@kavya498)
  - Gannayak Pabra (@Gannayak0722)
version_added: "0.0.1-beta0"
description:
    - This module creates, updates, or deletes a ibm_iam_access_group_members.
    - By default the module will look for an existing ibm_iam_access_group_members.
requirements:
    - "IamAccessGroupsV2"
options:
    members:
        description:
            - An array of member objects to add to an access group.
        type: list
        elements: dict
        suboptions:
            iam_id:
                description:
                    - The IBMid, service ID or trusted profile ID of the member.
                type: str
            type:
                description:
                    - The type of the member, must be either "user", "service" or "trusted profile".
                type: str
    access_group_id:
        description:
            - The access group identifier.
        type: str
    iam_id:
        description:
            - The IAM identifier.
        type: str
    offset:
        description:
            - The offset of the first result item to be returned.
        type: int
    transaction_id:
        description: |
            An optional transaction ID can be passed to your request, which can be useful for tracking calls through multiple services by using one identifier.
            The header key must be set to Transaction-Id and the value is anything that you choose.
            If no transaction ID is passed in, then a random ID is generated.
        type: str
    limit:
        description:
            - Return up to this limit of results where limit is between 0 and 100.
        type: int
    sort:
        description:
            - If verbose is true, sort the results by id, name, or email.
        type: str
    type:
        description:
            - Filter the results by member type.
        type: str
    verbose:
        description:
            - Return user's email and name for each user ID or the name for each service ID or trusted profile.
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
from ibm_platform_services import IamAccessGroupsV2
from ibm_cloud_sdk_core import ApiException
from ansible.module_utils.basic import AnsibleModule


def run_module():
    module_args = dict(
        members=dict(
            type='list',
            elements='dict',
            options=dict(
                iam_id=dict(
                    type='str',
                    required=False),
                type=dict(
                    type='str',
                    required=False),
            ),
            required=False),
        access_group_id=dict(
            type='str',
            required=False),
        iam_id=dict(
            type='str',
            required=False),
        offset=dict(
            type='int',
            required=False),
        transaction_id=dict(
            type='str',
            required=False),
        limit=dict(
            type='int',
            required=False),
        sort=dict(
            type='str',
            required=False),
        type=dict(
            type='str',
            required=False),
        verbose=dict(
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

    members = module.params["members"]
    access_group_id = module.params["access_group_id"]
    iam_id = module.params["iam_id"]
    offset = module.params["offset"]
    transaction_id = module.params["transaction_id"]
    limit = module.params["limit"]
    sort = module.params["sort"]
    type = module.params["type"]
    verbose = module.params["verbose"]
    state = module.params["state"]

    sdk = config.get_iam_access_group_sdk()

    resource_exists = True

    # Check for existence
    if iam_id:
        try:
            sdk.list_access_group_members(
                access_group_id=access_group_id,
                transaction_id=transaction_id,
                limit=limit,
                offset=offset,
                type=type,
                verbose=verbose,
                sort=sort,
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
                sdk.remove_member_from_access_group(
                    access_group_id=access_group_id,
                    iam_id=iam_id,
                    transaction_id=transaction_id,
                )
            except ApiException as ex:
                module.fail_json(msg=ex.message)
            else:
                payload = {"id": iam_id, "status": "deleted"}
                module.exit_json(changed=True, msg=payload)
        else:
            payload = {"id": iam_id, "status": "not_found"}
            module.exit_json(changed=False, msg=payload)

    if state == "present":
        if not resource_exists:
            # Create path
            try:
                result = sdk.add_members_to_access_group(
                    access_group_id=access_group_id,
                    members=members,
                    transaction_id=transaction_id,
                ).get_result()
            except ApiException as ex:
                module.fail_json(msg=ex.message)
            else:
                module.exit_json(changed=True, msg=result)
        else:
            # Update path
            try:
                result = sdk.add_members_to_access_group(
                    access_group_id=access_group_id,
                    members=members,
                    transaction_id=transaction_id,
                ).get_result()
            except ApiException as ex:
                module.fail_json(msg=ex.message)
            else:
                module.exit_json(changed=True, msg=result)


def main():
    run_module()


if __name__ == '__main__':
    main()
