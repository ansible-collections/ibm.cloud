#!/usr/bin/python
# coding: utf-8

# (C) Copyright IBM Corp. 2024.
#
# GNU General Public License v3.0+ (see LICENSE or https://www.gnu.org/licenses/gpl-3.0.txt)

from __future__ import (absolute_import, division, print_function)
__metaclass__ = type


DOCUMENTATION = r'''
---
module: ibm_iam_access_group_template_assignment
short_description: Manage C(iam_access_group_template_assignments) for IAM Access Groups.
author: Gannayak Pabra (@Gannayak0722)
version_added: "1.0.0"
description:
  - This module creates, updates, or deletes an C(iam_access_group_template_assignment) resource for IAM Access Groups.
requirements:
  - "IamAccessGroupsV2"
options:
  template_version:
    description: "The version number of the template to be assigned."
    type: str
  target_type:
    description: "The type of the entity to which the template should be assigned, e.g. 'Account',
      'AccountGroup', etc."
    type: str
    choices:
      - "Account"
      - "AccountGroup"
  template_id:
    description: "The unique identifier of the template to be assigned."
    type: str
  target:
    description: "The unique identifier of the entity to which the template should be assigned."
    type: str
  assignment_id:
    description: "Assignment ID."
    type: str
  if_match:
    description: "Version of the Assignment to be updated. Specify the version that you retrieved when
      reading the Assignment. This value helps identifying parallel usage of this API.
      Pass * to indicate to update any version available. This might result in stale
      updates."
    type: str
  transaction_id:
    description: "An optional transaction id for the request."
    type: str
  verbose:
    description: "Returns resources access group template assigned, possible values C(true) or
      C(false)."
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
- name: Create ibm_iam_access_group_template_assignment
  ibm_iam_access_group_template_assignment:
    template_id: 'AccessGroupTemplateId-4be4'
    template_version: '1'
    target_type: 'AccountGroup'
    target: '0a45594d0f-123'
    transaction_id: 'testString'
    state: present

- name: Update ibm_iam_access_group_template_assignment
  ibm_iam_access_group_template_assignment:
    assignment_id: 'testString'
    if_match: 'testString'
    template_version: '1'
    state: present

- name: Delete ibm_iam_access_group_template_assignment
  ibm_iam_access_group_template_assignment:
    assignment_id: 'testString'
    transaction_id: 'testString'
    state: absent
'''

RETURN = r'''
id:
  description: "The ID of the assignment."
  type: str
  returned: on success for create, update, delete operations
account_id:
  description: "The ID of the account that the assignment belongs to."
  type: str
  returned: on success for create, update operations
template_id:
  description: "The ID of the template that the assignment is based on."
  type: str
  returned: on success for create, update operations
template_version:
  description: "The version of the template that the assignment is based on."
  type: str
  returned: on success for create, update operations
target_type:
  description: "The type of the entity that the assignment applies to."
  type: str
  choices:
    - "Account"
    - "AccountGroup"
  returned: on success for create, update operations
target:
  description: "The ID of the entity that the assignment applies to."
  type: str
  returned: on success for create, update operations
operation:
  description: "The operation that the assignment applies to (e.g. 'assign', 'update', 'remove')."
  type: str
  choices:
    - "assign"
    - "update"
    - "remove"
  returned: on success for create, update operations
iam_access_group_template_assignment_status:
  description: "The status of the assignment (e.g. 'accepted', 'in_progress', 'succeeded', 'failed',
    'superseded')."
  type: str
  choices:
    - "accepted"
    - "in_progress"
    - "succeeded"
    - "failed"
    - "superseded"
  returned: on success for create, update operations
href:
  description: "The URL of the assignment resource."
  type: str
  returned: on success for create, update operations
created_at:
  description: "The date and time when the assignment was created."
  type: str
  returned: on success for create, update operations
created_by_id:
  description: "The user or system that created the assignment."
  type: str
  returned: on success for create, update operations
last_modified_at:
  description: "The date and time when the assignment was last updated."
  type: str
  returned: on success for create, update operations
last_modified_by_id:
  description: "The user or system that last updated the assignment."
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
    from ibm_platform_services import IamAccessGroupsV2
except ImportError as imp_exc:
    MISSING_IMPORT_EXC = imp_exc
else:
    MISSING_IMPORT_EXC = None


def run_module():
    module_args = dict(
        template_version=dict(
            type='str',
            required=False),
        target_type=dict(
            type='str',
            choices=[
                'Account',
                'AccountGroup',
            ],
            required=False),
        template_id=dict(
            type='str',
            required=False),
        target=dict(
            type='str',
            required=False),
        assignment_id=dict(
            type='str',
            required=False),
        if_match=dict(
            type='str',
            required=False),
        transaction_id=dict(
            type='str',
            required=False),
        verbose=dict(
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

    template_version = module.params["template_version"]
    target_type = module.params["target_type"]
    template_id = module.params["template_id"]
    target = module.params["target"]
    assignment_id = module.params["assignment_id"]
    if_match = module.params["if_match"]
    transaction_id = module.params["transaction_id"]
    verbose = module.params["verbose"]
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
    if assignment_id:
        try:
            sdk.get_assignment(
                assignment_id=assignment_id,
                transaction_id=transaction_id,
                verbose=verbose,
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
                sdk.delete_assignment(
                    assignment_id=assignment_id,
                    transaction_id=transaction_id,
                )
            except ApiException as ex:
                module.fail_json(msg=ex.message)
            else:
                module.exit_json(changed=True, id=assignment_id, status="deleted")
        else:
            module.exit_json(changed=False, id=assignment_id, status="not_found")

    if state == "present":
        if not resource_exists:
            # Create path
            try:
                response = sdk.create_assignment(
                    template_id=template_id,
                    template_version=template_version,
                    target_type=target_type,
                    target=target,
                    transaction_id=transaction_id,
                )
            except ApiException as ex:
                module.fail_json(msg=ex.message)
            else:
                result = response.get_result()
                if 'status' in result:
                    result['iam_access_group_template_assignment_status'] = result['status']
                    del result['status']

                module.exit_json(changed=True, **result)
        else:
            # Update path
            try:
                response = sdk.update_assignment(
                    assignment_id=assignment_id,
                    if_match=if_match,
                    template_version=template_version,
                )
            except ApiException as ex:
                module.fail_json(msg=ex.message)
            else:
                result = response.get_result()
                if 'status' in result:
                    result['iam_access_group_template_assignment_status'] = result['status']
                    del result['status']

                module.exit_json(changed=True, **result)


def main():
    run_module()


if __name__ == '__main__':
    main()
