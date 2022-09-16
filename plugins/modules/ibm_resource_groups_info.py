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
module: ibm_resource_groups_info
short_description: Manage ibm_resource_groups info.
author: Kavya Handadi (@kavya498)
version_added: "1.0.0"
description:
    - This module retrieves one or more ibm_resource_groups(s).
requirements:
    - "ResourceManagerV2"
options:
    date:
        description:
            - The date in the format of YYYY-MM which returns resource groups. Deleted resource groups will be excluded before this month.
        type: str
    default:
        description:
            - Boolean value to specify whether or not to list default resource groups.
        type: bool
    account_id:
        description:
            - The ID of the account that contains the resource groups that you want to get.
        type: str
    name:
        description:
            - The name of the resource group.
        type: str
    include_deleted:
        description:
            - Boolean value to specify whether or not to list default resource groups.
        type: bool
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
        date=dict(
            type='str',
            required=False),
        default=dict(
            type='bool',
            required=False),
        account_id=dict(
            type='str',
            required=False),
        name=dict(
            type='str',
            required=False),
        include_deleted=dict(
            type='bool',
            required=False),
    )

    module = AnsibleModule(
        argument_spec=module_args,
        supports_check_mode=False
    )

    date = module.params["date"]
    default = module.params["default"]
    account_id = module.params["account_id"]
    name = module.params["name"]
    include_deleted = module.params["include_deleted"]

    sdk = config.get_resource_manager_sdk()

    # list
    try:
        response = sdk.list_resource_groups(
            account_id=account_id,
            date=date,
            name=name,
            default=default,
            include_deleted=include_deleted
        )
        module.exit_json(msg=response.get_result())
    except ApiException as ex:
        module.fail_json(msg=ex.message)


def main():
    run_module()


if __name__ == '__main__':
    main()
