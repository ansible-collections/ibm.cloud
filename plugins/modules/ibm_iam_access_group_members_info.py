#!/usr/bin/python
# -*- coding: utf-8 -*-

# (C) Copyright IBM Corp. 2022.
# GNU General Public License v3.0+ (see LICENSE or https://www.gnu.org/licenses/gpl-3.0.txt)

from __future__ import (absolute_import, division, print_function)
__metaclass__ = type


DOCUMENTATION = r'''
---
module: ibm_iam_access_group_members_info
short_description: Manage ibm_iam_access_group_members info.
author: Kavya Handadi (@kavya498)
version_added: "0.0.1-beta0"
description:
    - This module retrieves one or more ibm_iam_access_group_members(s).
requirements:
    - "IamAccessGroupsV2"
options:
    access_group_id:
        description:
            - The access group identifier.
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
        access_group_id=dict(
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
    )

    module = AnsibleModule(
        argument_spec=module_args,
        supports_check_mode=False
    )

    access_group_id = module.params["access_group_id"]
    offset = module.params["offset"]
    transaction_id = module.params["transaction_id"]
    limit = module.params["limit"]
    sort = module.params["sort"]
    type = module.params["type"]
    verbose = module.params["verbose"]

    sdk = config.get_iam_access_group_sdk()

    # list
    try:
        response = sdk.list_access_group_members(
            access_group_id=access_group_id,
            transaction_id=transaction_id,
            limit=limit,
            offset=offset,
            type=type,
            verbose=verbose,
            sort=sort
        )
        module.exit_json(msg=response.get_result())
    except ApiException as ex:
        module.fail_json(msg=ex.message)


def main():
    run_module()


if __name__ == '__main__':
    main()
