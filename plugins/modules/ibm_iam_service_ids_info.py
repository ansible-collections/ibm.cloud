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
module: ibm_iam_service_ids_info
short_description: Manage ibm_iam_service_ids info.
author: Kavya Handadi (@kavya498)
version_added: "1.0.0"
description:
    - This module retrieves one or more ibm_iam_service_ids(s).
requirements:
    - "IamIdentityV1"
options:
    include_history:
        description:
            - Defines if the entity history is included in the response.
        type: bool
    account_id:
        description:
            - Account ID of the service ID(s) to query. This parameter is required (unless using a pagetoken).
        type: str
    name:
        description:
            - Name of the service ID(s) to query. Optional.20 items per page. Valid range is 1 to 100.
        type: str
    pagesize:
        description:
            - Optional size of a single page. Default is 20 items per page. Valid range is 1 to 100.
        type: int
    sort:
        description: |
            Optional sort property, valid values are name, description, created_at and modified_at.
            If specified, the items are sorted by the value of this property.
        type: str
    id:
        description:
            - Unique ID of the service ID.
        type: str
    pagetoken:
        description:
            - Optional Prev or Next page token returned from a previous query execution. Default is start with first page.
        type: str
    include_activity:
        description: |
            Defines if the entity's activity is included in the response.
            Retrieving activity data is an expensive operation, so please only request this when needed.
        type: bool
    order:
        description:
            - Optional sort order, valid values are asc and desc. Default value is asc.
        type: str
'''

EXAMPLES = r'''
Examples coming soon.
'''

from ..module_utils import config
from ibm_platform_services import IamIdentityV1
from ibm_cloud_sdk_core import ApiException
from ansible.module_utils.basic import AnsibleModule


def run_module():
    module_args = dict(
        include_history=dict(
            type='bool',
            required=False),
        account_id=dict(
            type='str',
            required=False),
        name=dict(
            type='str',
            required=False),
        pagesize=dict(
            type='int',
            required=False),
        sort=dict(
            type='str',
            required=False),
        id=dict(
            type='str',
            required=False),
        pagetoken=dict(
            type='str',
            required=False),
        include_activity=dict(
            type='bool',
            required=False),
        order=dict(
            type='str',
            required=False),
    )

    module = AnsibleModule(
        argument_spec=module_args,
        supports_check_mode=False
    )

    include_history = module.params["include_history"]
    account_id = module.params["account_id"]
    name = module.params["name"]
    pagesize = module.params["pagesize"]
    sort = module.params["sort"]
    id = module.params["id"]
    pagetoken = module.params["pagetoken"]
    include_activity = module.params["include_activity"]
    order = module.params["order"]

    sdk = config.get_iam_identity_sdk()

    if id:
        # read
        try:
            response = sdk.get_service_id(
                id=id,
                include_history=include_history,
                include_activity=include_activity
            )
            module.exit_json(msg=response.get_result())
        except ApiException as ex:
            module.fail_json(msg=ex.message)

    # list
    try:
        response = sdk.list_service_ids(
            account_id=account_id,
            name=name,
            pagesize=pagesize,
            pagetoken=pagetoken,
            sort=sort,
            order=order,
            include_history=include_history
        )
        module.exit_json(msg=response.get_result())
    except ApiException as ex:
        module.fail_json(msg=ex.message)


def main():
    run_module()


if __name__ == '__main__':
    main()
