#!/usr/bin/python
# -*- coding: utf-8 -*-

# (C) Copyright IBM Corp. 2022.
# GNU General Public License v3.0+ (see LICENSE or https://www.gnu.org/licenses/gpl-3.0.txt)

from __future__ import (absolute_import, division, print_function)
__metaclass__ = type


DOCUMENTATION = r'''
---
module: ibm_resource_quota_info
short_description: Manage ibm_resource_quota info.
author: Kavya Handadi (@kavya498)
version_added: "0.0.1-beta0"
description:
    - This module retrieves one or more ibm_resource_quota(s).
requirements:
    - "ResourceManagerV2"
options:
    id:
        description:
            - The id of the quota.
        type: str
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
        id=dict(
            type='str',
            required=False),
    )

    module = AnsibleModule(
        argument_spec=module_args,
        supports_check_mode=False
    )

    id = module.params["id"]

    sdk = config.get_resource_manager_sdk()

    # list
    try:
        response = sdk.get_quota_definition(
            id=id
        )
        module.exit_json(msg=response.get_result())
    except ApiException as ex:
        module.fail_json(msg=ex.message)


def main():
    run_module()


if __name__ == '__main__':
    main()
