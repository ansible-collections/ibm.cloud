#!/usr/bin/python
# coding: utf-8

# (C) Copyright IBM Corp. 2023.
#
# GNU General Public License v3.0+ (see LICENSE or https://www.gnu.org/licenses/gpl-3.0.txt)

from __future__ import (absolute_import, division, print_function)
__metaclass__ = type


DOCUMENTATION = r'''
---
module: ibm_resource_groups_info
short_description: Manage C(resource_groups) for Resource Manager.
author: IBM SDK Generator (@ibm)
version_added: "1.0.0"
description:
  - This module retrieves one or more C(resource_groups) for Resource Manager.
requirements:
  - "ResourceManagerV2"
options:
  date:
    description: "The date in the format of YYYY-MM which returns resource groups. Deleted resource
      groups will be excluded before this month."
    type: str
  default:
    description: "Boolean value to specify whether or not to list default resource groups."
    type: bool
  account_id:
    description: "The ID of the account that contains the resource groups that you want to get."
    type: str
  name:
    description: "The name of the resource group."
    type: str
  include_deleted:
    description: "Boolean value to specify whether or not to list deleted resource groups."
    type: bool
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

- name: List ibm_resource_groups
  ibm_resource_groups_info:
    account_id: 'testString'
    date: 'testString'
    name: 'testString'
    default: True
    include_deleted: True
'''

RETURN = r'''
resources:
  description: "The list of resource groups."
  type: list
  elements: 'dict'
  contains:
    id:
      description: "An alpha-numeric value identifying the resource group."
      type: str
    crn:
      description: "The full CRN (cloud resource name) associated with the resource group. For more on
        this format, see [Cloud Resource
        Names](https://cloud.ibm.com/docs/account?topic=account-crn)."
      type: str
    account_id:
      description: "An alpha-numeric value identifying the account ID."
      type: str
    name:
      description: "The human-readable name of the resource group."
      type: str
    state:
      description: "The state of the resource group."
      type: str
    default:
      description: "Identify if this resource group is default of the account or not."
      type: bool
    quota_id:
      description: "An alpha-numeric value identifying the quota ID associated with the resource group."
      type: str
    quota_url:
      description: "The URL to access the quota details that associated with the resource group."
      type: str
    payment_methods_url:
      description: "The URL to access the payment methods details that associated with the resource group."
      type: str
    resource_linkages:
      description: "An array of the resources that linked to the resource group."
      type: list
      elements: dict
    teams_url:
      description: "The URL to access the team details that associated with the resource group."
      type: str
    created_at:
      description: "The date when the resource group was initially created."
      type: str
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
        date=dict(
            type='str',
            required=False),
        default=dict(
            type='bool',
            required=False),
        account_id=dict(
            type='str',
            required=False),
        name=dict(
            type='str',
            required=False),
        include_deleted=dict(
            type='bool',
            required=False),
    )

    module = AnsibleModule(
        argument_spec=module_args,
        supports_check_mode=True
    )

    if MISSING_IMPORT_EXC is not None:
        module.fail_json(msg='Missing required import: ' + MISSING_IMPORT_EXC.msg)

    date = module.params["date"]
    default = module.params["default"]
    account_id = module.params["account_id"]
    name = module.params["name"]
    include_deleted = module.params["include_deleted"]

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
        response = sdk.list_resource_groups(
            account_id=account_id,
            date=date,
            name=name,
            default=default,
            include_deleted=include_deleted,
        )

        result = response.get_result()

        module.exit_json(**result)
    except ApiException as ex:
        module.fail_json(msg=ex.message)


def main():
    run_module()


if __name__ == '__main__':
    main()
