#!/usr/bin/python
# coding: utf-8

# (C) Copyright IBM Corp. 2023.
#
# GNU General Public License v3.0+ (see LICENSE or https://www.gnu.org/licenses/gpl-3.0.txt)

from __future__ import (absolute_import, division, print_function)
__metaclass__ = type


DOCUMENTATION = r'''
---
module: ibm_resource_alias
short_description: Manage C(resource_aliass) for Resource Controller.
author:
  - Kavya Handadi (@kavya498)
  - Umar Ali (@umarali-nagoor)
version_added: "1.0.0"
description:
  - This module creates, updates, or deletes a C(resource_alias) resource for Resource Controller.
requirements:
  - "ResourceControllerV2"
options:
  name:
    description: "The name of the alias. Must be 180 characters or less and cannot include any special
      characters other than C((space) - . _ :)."
    type: str
  source:
    description: "The ID of resource instance."
    type: str
  target:
    description: "The CRN of target name(space) in a specific environment, for example, space in
      Dallas YP, CFEE instance etc."
    type: str
  id:
    description: "The resource alias URL-encoded CRN or GUID."
    type: str
  recursive:
    description: "Deletes the resource bindings and keys associated with the alias."
    type: bool
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
- name: Create ibm_resource_alias
  ibm_resource_alias:
    name: 'ExampleResourceAlias'
    source: '381fd51a-f251-4f95-aff4-2b03fa8caa63'
    target: "crn:v1:bluemix:public:bluemix:us-south:o/d35d4f0e-5076-4c89-9361-2522894b6548::cf-space\
      :e1773b6e-17b4-40c8-b5ed-d2a1c4b620d7"
    state: present

- name: Update ibm_resource_alias
  ibm_resource_alias:
    id: 'testString'
    name: 'UpdatedExampleResourceAlias'
    state: present

- name: Delete ibm_resource_alias
  ibm_resource_alias:
    id: 'testString'
    recursive: False
    state: absent
'''

RETURN = r'''
name:
  description: "The name of the alias. Must be 180 characters or less and cannot include any special
    characters other than C((space) - . _ :)."
  type: str
  returned: on success for create, update operations
source:
  description: "The ID of resource instance."
  type: str
  returned: on success for create, update operations
target:
  description: "The CRN of target name(space) in a specific environment, for example, space in Dallas
    YP, CFEE instance etc."
  type: str
  returned: on success for create, update operations
id:
  description: "ID of the deleted resource"
  type: str
  returned: on success for delete operation
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
    from ibm_platform_services import ResourceControllerV2
except ImportError as imp_exc:
    MISSING_IMPORT_EXC = imp_exc
else:
    MISSING_IMPORT_EXC = None


def run_module():
    module_args = dict(
        name=dict(
            type='str',
            required=False),
        source=dict(
            type='str',
            required=False),
        target=dict(
            type='str',
            required=False),
        id=dict(
            type='str',
            required=False),
        recursive=dict(
            type='bool',
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

    name = module.params["name"]
    source = module.params["source"]
    target = module.params["target"]
    id = module.params["id"]
    recursive = module.params["recursive"]
    state = module.params["state"]

    authenticator = get_authenticator(service_name='resource_controller')
    if authenticator is None:
        module.fail_json(msg='Cannot create the authenticator.')

    sdk = ResourceControllerV2(
        authenticator=authenticator,
    )

    sdk.configure_service('resource_controller')

    resource_exists = True

    # Check for existence
    if id:
        try:
            sdk.get_resource_alias(
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
                sdk.delete_resource_alias(
                    id=id,
                    recursive=recursive,
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
                response = sdk.create_resource_alias(
                    name=name,
                    source=source,
                    target=target,
                )
            except ApiException as ex:
                module.fail_json(msg=ex.message)
            else:
                result = response.get_result()

                module.exit_json(changed=True, **result)
        else:
            # Update path
            try:
                response = sdk.update_resource_alias(
                    id=id,
                    name=name,
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
