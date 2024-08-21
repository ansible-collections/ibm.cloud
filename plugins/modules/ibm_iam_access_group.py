#!/usr/bin/python
# coding: utf-8

# (C) Copyright IBM Corp. 2024.
#
# GNU General Public License v3.0+ (see LICENSE or https://www.gnu.org/licenses/gpl-3.0.txt)

from __future__ import (absolute_import, division, print_function)
__metaclass__ = type


DOCUMENTATION = r'''
---
module: ibm_iam_access_group
short_description: Manage C(iam_access_groups) for IAM Access Groups.
author: Gannayak Pabra (@Gannayak0722)
version_added: "1.0.0"
description:
  - This module creates, updates, or deletes an C(iam_access_group) resource for IAM Access Groups.
requirements:
  - "IamAccessGroupsV2"
options:
  name:
    description: "Give the access group a unique name that doesn't conflict with an existing access
      group in the account. This field is case-insensitive and has a limit of 100
      characters."
    type: str
  description:
    description: "Assign an optional description for the access group. This field has a limit of 250
      characters."
    type: str
  access_group_id:
    description: "The access group identifier."
    type: str
  account_id:
    description: "Account ID of the API keys(s) to query. If a service IAM ID is specified in iamI(id
      then account)id must match the account of the IAM ID. If a user IAM ID is specified
      in iamI(id then then account)id must match the account of the Authorization token."
    type: str
  if_match:
    description: "The current revision number of the group being updated. This can be found in the
      Create/Get access group response ETag header."
    type: str
  transaction_id:
    description: "An optional transaction ID can be passed to your request, which can be useful for
      tracking calls through multiple services by using one identifier. The header key
      must be set to Transaction-Id and the value is anything that you choose. If no
      transaction ID is passed in, then a random ID is generated."
    type: str
  show_federated:
    description: "If showI(federated is true, the group will return an is)federated value that is set
      to true if rules exist for the group."
    type: bool
  force:
    description: "If force is true, delete the group as well as its associated members and rules."
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
- name: Create ibm_iam_access_group
  ibm_iam_access_group:
    account_id: 'testString'
    name: 'Managers'
    description: 'Group for managers'
    transaction_id: 'testString'
    state: present

- name: Update ibm_iam_access_group
  ibm_iam_access_group:
    access_group_id: 'testString'
    if_match: 'testString'
    name: 'Awesome Managers'
    description: 'Group for awesome managers.'
    transaction_id: 'testString'
    state: present

- name: Delete ibm_iam_access_group
  ibm_iam_access_group:
    access_group_id: 'testString'
    transaction_id: 'testString'
    force: False
    state: absent
'''

RETURN = r'''
id:
  description: "The group's access group ID."
  type: str
  returned: on success for create, update, delete operations
name:
  description: "The group's name."
  type: str
  returned: on success for create, update operations
description:
  description: "The group's description - if defined."
  type: str
  returned: on success for create, update operations
account_id:
  description: "The account id where the group was created."
  type: str
  returned: on success for create, update operations
created_at:
  description: "The timestamp of when the group was created."
  type: str
  returned: on success for create, update operations
created_by_id:
  description: "The C(iam_id) of the entity that created the group."
  type: str
  returned: on success for create, update operations
last_modified_at:
  description: "The timestamp of when the group was last edited."
  type: str
  returned: on success for create, update operations
last_modified_by_id:
  description: "The C(iam_id) of the entity that last modified the group name or description."
  type: str
  returned: on success for create, update operations
href:
  description: "A url to the given group resource."
  type: str
  returned: on success for create, update operations
is_federated:
  description: "This is set to true if rules exist for the group."
  type: bool
  returned: on success for create, update operations
status:
  description: The result status of the deletion
  type: str
  returned: on delete
msg:
  description: an error message that describes what went wrong
  type: str
  returned: on error
etag:
  description: The ETag value associated with the C(Group)
  returned: on create
  type: str
'''


from ansible.module_utils.basic import AnsibleModule

try:
    from ..module_utils.auth import get_authenticator
    from ibm_cloud_sdk_core import ApiException
    from ibm_platform_services import IamAccessGroupsV2
except ImportError as imp_exc:
    MISSING_IMPORT_EXC = imp_exc
else:
    MISSING_IMPORT_EXC = None


def run_module():
    module_args = dict(
        name=dict(
            type='str',
            required=False),
        description=dict(
            type='str',
            required=False),
        access_group_id=dict(
            type='str',
            required=False),
        account_id=dict(
            type='str',
            required=False),
        if_match=dict(
            type='str',
            required=False),
        transaction_id=dict(
            type='str',
            required=False),
        show_federated=dict(
            type='bool',
            required=False),
        force=dict(
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
    description = module.params["description"]
    access_group_id = module.params["access_group_id"]
    account_id = module.params["account_id"]
    if_match = module.params["if_match"]
    transaction_id = module.params["transaction_id"]
    show_federated = module.params["show_federated"]
    force = module.params["force"]
    state = module.params["state"]

    authenticator = get_authenticator(service_name='iam_access_groups')
    if authenticator is None:
        module.fail_json(msg='Cannot create the authenticator.')

    sdk = IamAccessGroupsV2(
        authenticator=authenticator,
    )

    sdk.configure_service('iam_access_groups')

    resource_exists = True

    # Check for existence
    if access_group_id:
        try:
            sdk.get_access_group(
                access_group_id=access_group_id,
                transaction_id=transaction_id,
                show_federated=show_federated,
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
                sdk.delete_access_group(
                    access_group_id=access_group_id,
                    transaction_id=transaction_id,
                    force=force,
                )
            except ApiException as ex:
                module.fail_json(msg=ex.message)
            else:
                module.exit_json(changed=True, id=access_group_id, status="deleted")
        else:
            module.exit_json(changed=False, id=access_group_id, status="not_found")

    if state == "present":
        if not resource_exists:
            # Create path
            try:
                response = sdk.create_access_group(
                    account_id=account_id,
                    name=name,
                    description=description,
                    transaction_id=transaction_id,
                )
            except ApiException as ex:
                module.fail_json(msg=ex.message)
            else:
                result = response.get_result()
                etag = response.get_headers().get('ETag')

                module.exit_json(changed=True, etag=etag, **result)
        else:
            # Update path
            try:
                response = sdk.update_access_group(
                    access_group_id=access_group_id,
                    if_match=if_match,
                    name=name,
                    description=description,
                    transaction_id=transaction_id,
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
