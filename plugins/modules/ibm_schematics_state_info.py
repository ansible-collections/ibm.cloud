#!/usr/bin/python
# coding: utf-8

# (C) Copyright IBM Corp. 2024.
#
# GNU General Public License v3.0+ (see LICENSE or https://www.gnu.org/licenses/gpl-3.0.txt)

from __future__ import (absolute_import, division, print_function)
__metaclass__ = type


DOCUMENTATION = r'''
---
module: ibm_schematics_state_info
short_description: Manage C(schematics_state) for Schematics Service API.
author: Gannayak Pabra (@Gannayak0722)
version_added: "1.0.0"
description:
  - This module retrieves one or more C(schematics_state) for Schematics Service API.
requirements:
  - "SchematicsV1"
options:
  t_id:
    description: "The ID of the Terraform template for which you want to retrieve the Terraform
      statefile.  When you create a workspace, the Terraform template that your workspace
      points to is assigned a unique ID.  To find this ID, use the C(GET /v1/workspaces)
      API and review the template_data.id value."
    type: str
  w_id:
    description: "The ID of the workspace for which you want to retrieve the Terraform statefile.  To
      find the workspace ID, use the C(GET /v1/workspaces) API."
    type: str
seealso:
  - name: IBM Cloud Schematics docs
    description: "Use Schematics to run your Ansible playbooks to provision, configure, and manage IBM Cloud resources."
    link: https://cloud.ibm.com/docs/schematics
notes:
  - "Authenticate this module by using an IBM Cloud API key. For more information about working with IBM Cloud API keys,
    see I(Managing API keys): U(https://cloud.ibm.com/docs/account?topic=account-manapikey)."
  - "To configure the authentication, set your IBM Cloud API key on the C(IC_API_KEY) environment variable.
    The API key will be used to authenticate all IBM Cloud modules that use this environment variable."
'''

EXAMPLES = r'''

- name: List ibm_schematics_state
  ibm_schematics_state_info:
    w_id: 'testString'
    t_id: 'testString'
'''

RETURN = r'''
version:
  description: "No description has been provided."
  type: float
  returned: on success for list operation
terraform_version:
  description: "No description has been provided."
  type: str
  returned: on success for list operation
serial:
  description: "No description has been provided."
  type: float
  returned: on success for list operation
lineage:
  description: "No description has been provided."
  type: str
  returned: on success for list operation
modules:
  description: "No description has been provided."
  type: list
  elements: dict
  returned: on success for list operation
msg:
  description: an error message that describes what went wrong
  type: str
  returned: on error
'''


from ansible.module_utils.basic import AnsibleModule

try:
    from ..module_utils.auth import get_authenticator
    from ibm_cloud import SchematicsV1
    from ibm_cloud_sdk_core import ApiException
except ImportError as imp_exc:
    MISSING_IMPORT_EXC = imp_exc
else:
    MISSING_IMPORT_EXC = None


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
        supports_check_mode=True
    )

    if MISSING_IMPORT_EXC is not None:
        module.fail_json(msg='Missing required import: ' + MISSING_IMPORT_EXC.msg)

    t_id = module.params["t_id"]
    w_id = module.params["w_id"]

    if module.check_mode:
        module.exit_json(msg='The module would run with the following parameters: ' + module.paramss)

    authenticator = get_authenticator(service_name='schematics')
    if authenticator is None:
        module.fail_json(msg='Cannot create the authenticator.')

    sdk = SchematicsV1(
        authenticator=authenticator,
    )

    sdk.configure_service('schematics')

    # list
    try:
        response = sdk.get_workspace_template_state(
            w_id=w_id,
            t_id=t_id,
        )

        result = response.get_result()

        module.exit_json(**result)
    except ApiException as ex:
        module.fail_json(msg=ex.message)


def main():
    run_module()


if __name__ == '__main__':
    main()
