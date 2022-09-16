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
module: ibm_iam_access_group
short_description: Manage ibm_iam_access_group resources.
author: Kavya Handadi (@kavya498)
version_added: "1.0.0"
description:
    - This module creates, updates, or deletes a ibm_iam_access_group.
    - By default the module will look for an existing ibm_iam_access_group.
requirements:
    - "IamAccessGroupsV2"
options:
    name:
        description: |
            Assign the specified name to the access group.
            This field is case-insensitive and has a limit of 100 characters.
            The group name has to be unique within an account.
        type: str
    description:
        description:
            - Assign an optional description for the access group. This field has a limit of 250 characters.
        type: str
    access_group_id:
        description:
            - The access group identifier.
        type: str
    account_id:
        description: |
            Account ID of the API keys(s) to query.
            If a service IAM ID is specified in iam_id then account_id must match the account of the IAM ID.
            If a user IAM ID is specified in iam_id then then account_id must match the account of the Authorization token.
        type: str
    if_match:
        description: |
            The current revision number of the group being updated.
            This can be found in the Create/Get access group response ETag header.
        type: str
    transaction_id:
        description: |
            An optional transaction ID can be passed to your request, which can be useful for tracking calls through multiple services by using one identifier.
            The header key must be set to Transaction-Id and the value is anything that you choose.
            If no transaction ID is passed in, then a random ID is generated.
        type: str
    show_federated:
        description: |
            If show_federated is true, the group will return an is_federated value that is set to true if rules exist for the group.
        type: bool
    force:
        description:
            - If force is true, delete the group as well as its associated members and rules.
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
        name=dict(
            type='str',
            required=False),
        description=dict(
            type='str',
            required=False),
        access_group_id=dict(
            type='str',
            required=False),
        account_id=dict(
            type='str',
            required=False),
        if_match=dict(
            type='str',
            required=False),
        transaction_id=dict(
            type='str',
            required=False),
        show_federated=dict(
            type='bool',
            required=False),
        force=dict(
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

    name = module.params["name"]
    description = module.params["description"]
    access_group_id = module.params["access_group_id"]
    account_id = module.params["account_id"]
    if_match = module.params["if_match"]
    transaction_id = module.params["transaction_id"]
    show_federated = module.params["show_federated"]
    force = module.params["force"]
    state = module.params["state"]

    sdk = config.get_iam_access_group_sdk()

    resource_exists = True

    # Check for existence
    if access_group_id:
        try:
            sdk.get_access_group(
                access_group_id=access_group_id,
                transaction_id=transaction_id,
                show_federated=show_federated,
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
                sdk.delete_access_group(
                    access_group_id=access_group_id,
                    transaction_id=transaction_id,
                    force=force,
                )
            except ApiException as ex:
                module.fail_json(msg=ex.message)
            else:
                payload = {"id": access_group_id, "status": "deleted"}
                module.exit_json(changed=True, msg=payload)
        else:
            payload = {"id": access_group_id, "status": "not_found"}
            module.exit_json(changed=False, msg=payload)

    if state == "present":
        if not resource_exists:
            # Create path
            try:
                result = sdk.create_access_group(
                    account_id=account_id,
                    name=name,
                    description=description,
                    transaction_id=transaction_id,
                ).get_result()
            except ApiException as ex:
                module.fail_json(msg=ex.message)
            else:
                module.exit_json(changed=True, msg=result)
        else:
            # Update path
            try:
                result = sdk.update_access_group(
                    access_group_id=access_group_id,
                    if_match=if_match,
                    name=name,
                    description=description,
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
