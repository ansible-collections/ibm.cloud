#!/usr/bin/python
# coding: utf-8

# (C) Copyright IBM Corp. 2023.
#
# GNU General Public License v3.0+ (see LICENSE or https://www.gnu.org/licenses/gpl-3.0.txt)

from __future__ import (absolute_import, division, print_function)
__metaclass__ = type


DOCUMENTATION = r'''
---
module: ibm_resource_group
short_description: Manage C(resource_groups) for Resource Manager.
author:
  - Kavya Handadi (@kavya498)
  - Umar Ali (@umarali-nagoor)
version_added: "1.0.0"
description:
  - This module creates, updates, or deletes a C(resource_group) resource for Resource Manager.
requirements:
  - "ResourceManagerV2"
options:
  account_id:
    description: "The account id of the resource group."
    type: str
  name:
    description: "The new name of the resource group."
    type: str
  resource_group_state:
    description: "The state of the resource group."
    type: str
  id:
    description: "The short or long ID of the alias."
    type: str
  state:
    description:
      - Should the resource be present or absent.
    type: str
    default: present
    choices: [present, absent]
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
- name: Create ibm_resource_group
  ibm_resource_group:
    name: 'test1'
    account_id: '25eba2a9-beef-450b-82cf-f5ad5e36c6dd'
    state: present

- name: Update ibm_resource_group
  ibm_resource_group:
    id: 'testString'
    name: 'testString'
    resource_group_state: 'testString'
    state: present

- name: Delete ibm_resource_group
  ibm_resource_group:
    id: 'testString'
    state: absent
'''

RETURN = r'''
id:
  description: "An alpha-numeric value identifying the resource group."
  type: str
  returned: on success for create, update, delete operations
crn:
  description: "The full CRN (cloud resource name) associated with the resource group. For more on
    this format, see [Cloud Resource
    Names](https://cloud.ibm.com/docs/account?topic=account-crn)."
  type: str
  returned: on success for create, update operations
status:
  description: The result status of the deletion
  type: str
  returned: on delete
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
        account_id=dict(
            type='str',
            required=False),
        name=dict(
            type='str',
            required=False),
        resource_group_state=dict(
            type='str',
            required=False),
        id=dict(
            type='str',
            required=False),
        state=dict(
            type='str',
            default='present',
            choices=['absent', 'present'],
            required=False),
    )

    module = AnsibleModule(
        argument_spec=module_args,
        supports_check_mode=False
    )

    if MISSING_IMPORT_EXC is not None:
        module.fail_json(msg='Missing required import: ' + MISSING_IMPORT_EXC.msg)

    account_id = module.params["account_id"]
    name = module.params["name"]
    resource_group_state = module.params["resource_group_state"]
    id = module.params["id"]
    state = module.params["state"]

    authenticator = get_authenticator(service_name='resource_manager')
    if authenticator is None:
        module.fail_json(msg='Cannot create the authenticator.')

    sdk = ResourceManagerV2(
        authenticator=authenticator,
    )

    sdk.configure_service('resource_manager')

    resource_exists = True

    # Check for existence
    if id:
        try:
            sdk.get_resource_group(
                id=id,
            )
        except ApiException as ex:
            if ex.code == 404:
                resource_exists = False
            else:
                module.fail_json(msg=ex.message)
    else:
        # assume resource does not exist
        resource_exists = False

    # Delete path
    if state == "absent":
        if resource_exists:
            try:
                sdk.delete_resource_group(
                    id=id,
                )
            except ApiException as ex:
                module.fail_json(msg=ex.message)
            else:
                module.exit_json(changed=True, id=id, status="deleted")
        else:
            module.exit_json(changed=False, id=id, status="not_found")

    if state == "present":
        if not resource_exists:
            # Create path
            try:
                response = sdk.create_resource_group(
                    name=name,
                    account_id=account_id,
                )
            except ApiException as ex:
                module.fail_json(msg=ex.message)
            else:
                result = response.get_result()

                module.exit_json(changed=True, **result)
        else:
            # Update path
            try:
                response = sdk.update_resource_group(
                    id=id,
                    name=name,
                    state=resource_group_state,
                )
            except ApiException as ex:
                module.fail_json(msg=ex.message)
            else:
                result = response.get_result()

                module.exit_json(changed=True, **result)


def main():
    run_module()


if __name__ == '__main__':
    main()
