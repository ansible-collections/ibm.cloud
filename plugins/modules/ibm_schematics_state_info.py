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
module: ibm_schematics_state_info
short_description: Manage C(schematics_state) for Schematics Service API.
author: Kavya Handadi (@kavya498)
version_added: "1.0.0"
description:
  - This module retrieves one or more C(schematics_state) for Schematics Service API.
requirements:
  - "SchematicsV1"
options:
  t_id:
    description: |
      The ID of the Terraform template for which you want to retrieve the Terraform statefile.
      When you create a workspace, the Terraform template that your workspace points to is assigned a unique ID.
      To find this ID, use the C(GET /v1/workspaces) API and review the templateI(data.id value.
    type: str
  w_id:
    description:
      - The ID of the workspace for which you want to retrieve the Terraform statefile.  To find the workspace ID, use the C(GET /v1/workspaces) API.
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

- name: List ibm_schematics_state
  ibm_schematics_state_info:
'''

RETURN = '''
msg:
  description: |-
    A dictionary that represents the result.
    In case of "list", it's a C(TemplateStateStore).
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
        t_id=dict(
            type='str',
            required=False),
        w_id=dict(
            type='str',
            required=False),
    )

    module = AnsibleModule(
        argument_spec=module_args,
        supports_check_mode=False
    )

    t_id = module.params["t_id"]
    w_id = module.params["w_id"]

    sdk = config.get_schematicsv1_sdk()

    # list
    try:
        response = sdk.get_workspace_template_state(
            w_id=w_id,
            t_id=t_id
        )
        module.exit_json(msg=response.get_result())
    except ApiException as ex:
        module.fail_json(msg=ex.message)


def main():
    run_module()


if __name__ == '__main__':
    main()
