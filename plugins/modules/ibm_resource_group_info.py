#!/usr/bin/python
# coding: utf-8

# (C) Copyright IBM Corp. 2023.
#
# GNU General Public License v3.0+ (see LICENSE or https://www.gnu.org/licenses/gpl-3.0.txt)

from __future__ import (absolute_import, division, print_function)
__metaclass__ = type


DOCUMENTATION = r'''
---
module: ibm_resource_group_info
short_description: Manage C(resource_group) for Resource Manager.
author: Kavya Handadi (@kavya498)
version_added: "0.0.1-beta0"
description:
  - This module retrieves one or more C(resource_group) for Resource Manager.
requirements:
  - "ResourceManagerV2"
options:
  id:
    description: "The short or long ID of the alias."
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

- name: List ibm_resource_group
  ibm_resource_group_info:
    id: 'testString'
'''

RETURN = r'''
id:
  description: "An alpha-numeric value identifying the resource group."
  type: str
  returned: on success for list operation
crn:
  description: "The full CRN (cloud resource name) associated with the resource group. For more on
    this format, see [Cloud Resource
    Names](https://cloud.ibm.com/docs/account?topic=account-crn)."
  type: str
  returned: on success for list operation
account_id:
  description: "An alpha-numeric value identifying the account ID."
  type: str
  returned: on success for list operation
name:
  description: "The human-readable name of the resource group."
  type: str
  returned: on success for list operation
state:
  description: "The state of the resource group."
  type: str
  returned: on success for list operation
default:
  description: "Identify if this resource group is default of the account or not."
  type: bool
  returned: on success for list operation
quota_id:
  description: "An alpha-numeric value identifying the quota ID associated with the resource group."
  type: str
  returned: on success for list operation
quota_url:
  description: "The URL to access the quota details that associated with the resource group."
  type: str
  returned: on success for list operation
payment_methods_url:
  description: "The URL to access the payment methods details that associated with the resource group."
  type: str
  returned: on success for list operation
resource_linkages:
  description: "An array of the resources that linked to the resource group."
  type: list
  elements: dict
  returned: on success for list operation
teams_url:
  description: "The URL to access the team details that associated with the resource group."
  type: str
  returned: on success for list operation
created_at:
  description: "The date when the resource group was initially created."
  type: str
  returned: on success for list operation
updated_at:
  description: "The date when the resource group was last updated."
  type: str
  returned: on success for list operation
msg:
  description: an error message that describes what went wrong
  type: str
  returned: on error
'''


from ansible.module_utils.basic import AnsibleModule

try:
    from ..module_utils.auth import get_authenticator
    from ibm_cloud_sdk_core import ApiException
    from ibm_platform_services import ResourceManagerV2
except ImportError as imp_exc:
    MISSING_IMPORT_EXC = imp_exc
else:
    MISSING_IMPORT_EXC = None


def run_module():
    module_args = dict(
        id=dict(
            type='str',
            required=False),
    )

    module = AnsibleModule(
        argument_spec=module_args,
        supports_check_mode=True
    )

    if MISSING_IMPORT_EXC is not None:
        module.fail_json(msg='Missing required import: ' + MISSING_IMPORT_EXC.msg)

    id = module.params["id"]

    if module.check_mode:
        module.exit_json(msg='The module would run with the following parameters: ' + module.paramss)

    authenticator = get_authenticator(service_name='resource_manager')
    if authenticator is None:
        module.fail_json(msg='Cannot create the authenticator.')

    sdk = ResourceManagerV2(
        authenticator=authenticator,
    )

    sdk.configure_service('resource_manager')

    # list
    try:
        response = sdk.get_resource_group(
            id=id,
        )

        result = response.get_result()

        module.exit_json(**result)
    except ApiException as ex:
        module.fail_json(msg=ex.message)


def main():
    run_module()


if __name__ == '__main__':
    main()
