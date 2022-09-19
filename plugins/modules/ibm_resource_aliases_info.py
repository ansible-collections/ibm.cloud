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
module: ibm_resource_aliases_info
short_description: Manage ibm_resource_aliases info.
author: Kavya Handadi (@kavya498)
version_added: "1.0.0"
description:
    - This module retrieves one or more ibm_resource_aliases(s).
requirements:
    - "ResourceControllerV2"
options:
    limit:
        description:
            - Limit on how many items should be returned.
        type: int
    start:
        description: |
            An optional token that indicates the beginning of the page of results to be returned.
            Any additional query parameters are ignored if a page token is present.
            If omitted, the first page of results is returned. This value is obtained from the 'next_url' field of the operation response.
        type: str
    id:
        description:
            - The ID of the instance.
        type: str
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
        limit=dict(
            type='int',
            required=False),
        start=dict(
            type='str',
            required=False),
        id=dict(
            type='str',
            required=False),
    )

    module = AnsibleModule(
        argument_spec=module_args,
        supports_check_mode=False
    )

    limit = module.params["limit"]
    start = module.params["start"]
    id = module.params["id"]

    sdk = config.get_resource_contollerV2_sdk()

    # list
    try:
        response = sdk.list_resource_aliases_for_instance(
            id=id,
            limit=limit,
            start=start
        )
        module.exit_json(msg=response.get_result())
    except ApiException as ex:
        module.fail_json(msg=ex.message)


def main():
    run_module()


if __name__ == '__main__':
    main()
