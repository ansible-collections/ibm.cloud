#!/usr/bin/python
# -*- coding: utf-8 -*-

# (C) Copyright IBM Corp. 2022.
# GNU General Public License v3.0+ (see LICENSE or https://www.gnu.org/licenses/gpl-3.0.txt)

from __future__ import (absolute_import, division, print_function)
__metaclass__ = type


DOCUMENTATION = r'''
---
module: ibm_schematics_workspace_activity_info
short_description: Manage C(schematics_workspace_activity) for Schematics Service API.
author: Kavya Handadi (@kavya498)
version_added: "0.0.1-beta0"
description:
  - This module retrieves one or more C(schematics_workspace_activity) for Schematics Service API.
requirements:
  - "SchematicsV1"
options:
  w_id:
    description:
      - The ID of the workspace.  To find the workspace ID, use the C(GET /v1/workspaces) API.
    type: str
  activity_id:
    description:
      - The ID of the activity or job, for which you want to retrieve details.  To find the job ID, use the C(GET /v1/workspaces/{id}/actions) API.
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

- name: List ibm_schematics_workspace_activity
  ibm_schematics_workspace_activity_info:
'''

RETURN = '''
msg:
  description: |-
    A dictionary that represents the result.
    In case of "list", it's a C(WorkspaceActivity).
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
        w_id=dict(
            type='str',
            required=False),
        activity_id=dict(
            type='str',
            required=False),
    )

    module = AnsibleModule(
        argument_spec=module_args,
        supports_check_mode=False
    )

    w_id = module.params["w_id"]
    activity_id = module.params["activity_id"]

    sdk = config.get_schematicsv1_sdk()

    # list
    try:
        response = sdk.get_workspace_activity(
            w_id=w_id,
            activity_id=activity_id
        )
        module.exit_json(msg=response.get_result())
    except ApiException as ex:
        module.fail_json(msg=ex.message)


def main():
    run_module()


if __name__ == '__main__':
    main()
