#!/usr/bin/python
# -*- coding: utf-8 -*-

# (C) Copyright IBM Corp. 2022.
# GNU General Public License v3.0+ (see LICENSE or https://www.gnu.org/licenses/gpl-3.0.txt)

from __future__ import (absolute_import, division, print_function)
__metaclass__ = type


DOCUMENTATION = r'''
---
module: ibm_iam_service_id_info
short_description: Manage ibm_iam_service_id info.
author: Kavya Handadi (@kavya498)
version_added: "0.0.1-beta0"
description:
    - This module retrieves one or more ibm_iam_service_id(s).
requirements:
    - "IamIdentityV1"
options:
    include_history:
        description:
            - Defines if the entity history is included in the response.
        type: bool
    id:
        description:
            - Unique ID of the service ID.
        type: str
    include_activity:
        description: |
            Defines if the entity's activity is included in the response.
            Retrieving activity data is an expensive operation, so please only request this when needed.
        type: bool
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
        id=dict(
            type='str',
            required=False),
        include_activity=dict(
            type='bool',
            required=False),
    )

    module = AnsibleModule(
        argument_spec=module_args,
        supports_check_mode=False
    )

    include_history = module.params["include_history"]
    id = module.params["id"]
    include_activity = module.params["include_activity"]

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


def main():
    run_module()


if __name__ == '__main__':
    main()
