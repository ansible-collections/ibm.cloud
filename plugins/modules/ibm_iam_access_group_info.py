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
module: ibm_iam_access_group_info
short_description: Manage ibm_iam_access_group info.
author: Kavya Handadi (@kavya498)
version_added: "1.0.0"
description:
    - This module retrieves one or more ibm_iam_access_group(s).
requirements:
    - "IamAccessGroupsV2"
options:
    access_group_id:
        description:
            - The access group identifier.
        type: str
    transaction_id:
        description: |
            An optional transaction ID can be passed to your request, which can be useful for tracking calls through multiple services by using one identifier.
            The header key must be set to Transaction-Id and the value is anything that you choose.
            If no transaction ID is passed in, then a random ID is generated.
        type: str
    show_federated:
        description:
            - If show_federated is true, the group will return an is_federated value that is set to true if rules exist for the group.
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
        transaction_id=dict(
            type='str',
            required=False),
        show_federated=dict(
            type='bool',
            required=False),
    )

    module = AnsibleModule(
        argument_spec=module_args,
        supports_check_mode=False
    )

    access_group_id = module.params["access_group_id"]
    transaction_id = module.params["transaction_id"]
    show_federated = module.params["show_federated"]

    sdk = config.get_iam_access_group_sdk()
    if access_group_id:
        # read
        try:
            response = sdk.get_access_group(
                access_group_id=access_group_id,
                transaction_id=transaction_id,
                show_federated=show_federated
            )
            module.exit_json(msg=response.get_result())
        except ApiException as ex:
            module.fail_json(msg=ex.message)


def main():
    run_module()


if __name__ == '__main__':
    main()
