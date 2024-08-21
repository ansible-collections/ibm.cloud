#!/usr/bin/python
# coding: utf-8

# (C) Copyright IBM Corp. 2024.
#
# GNU General Public License v3.0+ (see LICENSE or https://www.gnu.org/licenses/gpl-3.0.txt)

from __future__ import (absolute_import, division, print_function)
__metaclass__ = type


DOCUMENTATION = r'''
---
module: ibm_iam_service_role
short_description: Manage C(iam_service_roles) for IAM Policy Management.
author: Gannayak Pabra (@Gannayak0722)
version_added: "1.0.0"
description:
  - This module creates, updates, or deletes an C(iam_service_role) resource for IAM Policy Management.
requirements:
  - "IamPolicyManagementV1"
options:
  account_id:
    description: "The account GUID."
    type: str
  service_name:
    description: "The service name."
    type: str
  name:
    description: "The name of the role that is used in the CRN. Can only be alphanumeric and has to be
      capitalized."
    type: str
  description:
    description: "The description of the role."
    type: str
  display_name:
    description: "The display name of the role that is shown in the console."
    type: str
  actions:
    description: "The actions of the role. For more information, see [IAM roles and
      actions](https://cloud.ibm.com/docs/account?topic=account-iam-service-roles-actions)."
    type: list
    elements: str
  if_match:
    description: "The revision number for updating a role and must match the ETag value of the
      existing role. The Etag can be retrieved using the GET /v2/roles/{role_id} API and
      looking at the ETag response header."
    type: str
  role_id:
    description: "The role ID."
    type: str
  accept_language:
    description: "Language code for translations
      * C(default) - English
      * C(de) -  German (Standard)
      * C(en) - English
      * C(es) - Spanish (Spain)
      * C(fr) - French (Standard)
      * C(it) - Italian (Standard)
      * C(ja) - Japanese
      * C(ko) - Korean
      * C(pt-br) - Portuguese (Brazil)
      * C(zh-cn) - Chinese (Simplified, PRC)
      * C(zh-tw) - (Chinese, Taiwan)."
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
- name: Create ibm_iam_service_role
  ibm_iam_service_role:
    display_name: 'testString'
    actions: ['testString']
    name: 'Developer'
    account_id: 'testString'
    service_name: 'iam-groups'
    description: 'testString'
    accept_language: 'default'
    state: present

- name: Update ibm_iam_service_role
  ibm_iam_service_role:
    role_id: 'testString'
    if_match: 'testString'
    display_name: 'testString'
    actions: ['testString']
    description: 'testString'
    state: present

- name: Delete ibm_iam_service_role
  ibm_iam_service_role:
    role_id: 'testString'
    state: absent
'''

RETURN = r'''
display_name:
  description: "The display name of the role that is shown in the console."
  type: str
  returned: on success for create, update operations
description:
  description: "The description of the role."
  type: str
  returned: on success for create, update operations
actions:
  description: "The actions of the role. For more information, see [IAM roles and
    actions](https://cloud.ibm.com/docs/account?topic=account-iam-service-roles-actions)."
  type: list
  elements: str
  returned: on success for create, update operations
crn:
  description: "The role Cloud Resource Name (CRN). Example CRN:
    'crn:v1:ibmcloud:public:iam-access-management::a/exampleAccountId::customRole:ExampleRoleName'."
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
    from ibm_platform_services import IamPolicyManagementV1
except ImportError as imp_exc:
    MISSING_IMPORT_EXC = imp_exc
else:
    MISSING_IMPORT_EXC = None


def run_module():
    module_args = dict(
        account_id=dict(
            type='str',
            required=False),
        service_name=dict(
            type='str',
            required=False),
        name=dict(
            type='str',
            required=False),
        description=dict(
            type='str',
            required=False),
        display_name=dict(
            type='str',
            required=False),
        actions=dict(
            type='list',
            elements='str',
            required=False),
        if_match=dict(
            type='str',
            required=False),
        role_id=dict(
            type='str',
            required=False),
        accept_language=dict(
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
    service_name = module.params["service_name"]
    name = module.params["name"]
    description = module.params["description"]
    display_name = module.params["display_name"]
    actions = module.params["actions"]
    if_match = module.params["if_match"]
    role_id = module.params["role_id"]
    accept_language = module.params["accept_language"]
    state = module.params["state"]

    authenticator = get_authenticator(service_name='iam_policy_management')
    if authenticator is None:
        module.fail_json(msg='Cannot create the authenticator.')

    sdk = IamPolicyManagementV1(
        authenticator=authenticator,
    )

    sdk.configure_service('iam_policy_management')

    resource_exists = True

    # Check for existence
    if role_id:
        try:
            sdk.get_role(
                role_id=role_id,
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
                sdk.delete_role(
                    role_id=role_id,
                )
            except ApiException as ex:
                module.fail_json(msg=ex.message)
            else:
                module.exit_json(changed=True, id=role_id, status="deleted")
        else:
            module.exit_json(changed=False, id=role_id, status="not_found")

    if state == "present":
        if not resource_exists:
            # Create path
            try:
                response = sdk.create_role(
                    display_name=display_name,
                    actions=actions,
                    name=name,
                    account_id=account_id,
                    service_name=service_name,
                    description=description,
                    accept_language=accept_language,
                )
            except ApiException as ex:
                module.fail_json(msg=ex.message)
            else:
                result = response.get_result()

                module.exit_json(changed=True, **result)
        else:
            # Update path
            try:
                response = sdk.replace_role(
                    role_id=role_id,
                    if_match=if_match,
                    display_name=display_name,
                    actions=actions,
                    description=description,
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
