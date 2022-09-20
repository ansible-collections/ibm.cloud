#!/usr/bin/python
# -*- coding: utf-8 -*-

# (C) Copyright IBM Corp. 2022.
# GNU General Public License v3.0+ (see LICENSE or https://www.gnu.org/licenses/gpl-3.0.txt)

from __future__ import (absolute_import, division, print_function)
__metaclass__ = type


DOCUMENTATION = r'''
---
module: ibm_schematics_resource_query_info
short_description: Manage C(schematics_resource_query) for Schematics Service API.
author: Kavya Handadi (@kavya498)
version_added: "0.0.1-beta0"
description:
  - This module retrieves one or more C(schematics_resource_query) for Schematics Service API.
requirements:
  - "SchematicsV1"
options:
  query_id:
    description:
      - Resource query Id.  Use C(GET /v2/resourceI(query) API to look up the Resource query definition Ids  in your IBM Cloud account.
    type: str
seealso:
  - name: IBM Cloud Schematics docs
    description: Use Schematics to run your Ansible playbooks to provision, configure, and manage IBM Cloud resources.
    link: U(https://cloud.ibm.com/docs/schematics)
notes:
  - |
    Authenticate this module by using an IBM Cloud API key.
    For more information about working with IBM Cloud API keys, see I(Managing API keys): U(https://cloud.ibm.com/docs/account?topic=account-manapikey).
  - |
    To configure the authentication, set your IBM Cloud API key on the C(IC_API_KEY) environment variable.
    The API key will be used to authenticate all IBM Cloud modules that use this environment variable.
'''

EXAMPLES = r'''
- name: Read ibm_schematics_resource_query
  ibm_schematics_resource_query_info:
'''

RETURN = '''
msg:
  description: |-
    A dictionary that represents the result.
    In case of "read", it's a C(ResourceQueryRecord).
  returned: always
  type: dict
'''


from ..module_utils import config
from ansible.module_utils.basic import AnsibleModule
try:
    from ibm_schematics import SchematicsV1
    from ibm_cloud_sdk_core import ApiException
except ImportError:
    pass


def run_module():
    module_args = dict(
        query_id=dict(
            type='str',
            required=False),
    )

    module = AnsibleModule(
        argument_spec=module_args,
        supports_check_mode=False
    )

    query_id = module.params["query_id"]

    sdk = config.get_schematicsv1_sdk()

    if query_id:
        # read
        try:
            response = sdk.get_resources_query(
                query_id=query_id
            )
            module.exit_json(msg=response.get_result())
        except ApiException as ex:
            module.fail_json(msg=ex.message)


def main():
    run_module()


if __name__ == '__main__':
    main()
