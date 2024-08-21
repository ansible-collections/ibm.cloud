#!/usr/bin/python
# coding: utf-8

# (C) Copyright IBM Corp. 2024.
#
# GNU General Public License v3.0+ (see LICENSE or https://www.gnu.org/licenses/gpl-3.0.txt)

from __future__ import (absolute_import, division, print_function)
__metaclass__ = type


DOCUMENTATION = r'''
---
module: ibm_iam_service_policy_assignment
short_description: Manage C(iam_service_policy_assignments) for IAM Policy Management.
author: Gannayak Pabra (@Gannayak0722)
version_added: "1.0.0"
description:
  - This module creates, updates, or deletes an C(iam_service_policy_assignment) resource for IAM Policy Management.
requirements:
  - "IamPolicyManagementV1"
options:
  template_version:
    description: "The policy template version to update to."
    type: str
  assignment_id:
    description: "The policy template assignment ID."
    type: str
  if_match:
    description: "The revision number for updating a policy assignment and must match the ETag value
      of the existing policy assignment. The Etag can be retrieved using the GET
      /v1/policyI(assignments/{assignment)id} API and looking at the ETag response header."
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
  version:
    description: "specify version of response body format."
    type: str
    choices:
      - "1.0"
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
- name: Create ibm_iam_service_policy_assignment
  vars:
    assignment_target_details_model:
      type: 'Account'
      id: 'testString'
    policy_assignment_v1_options_root_template_model:
      id: 'testString'
      version: 'testString'
    policy_assignment_v1_options_root_model:
      requester_id: 'testString'
      assignment_id: 'testString'
      template: policy_assignment_v1_options_root_template_model
    policy_assignment_v1_options_model:
      root: policy_assignment_v1_options_root_model
    assignment_template_details_model:
      id: 'testString'
      version: 'testString'
  ibm_iam_service_policy_assignment:
    version: '1.0'
    policy_assignment_v1_request: 'unknown type: PolicyAssignmentV1Request'
    accept_language: 'default'
    state: present

- name: Update ibm_iam_service_policy_assignment
  ibm_iam_service_policy_assignment:
    assignment_id: 'testString'
    version: '1.0'
    if_match: 'testString'
    template_version: 'testString'
    state: present

- name: Delete ibm_iam_service_policy_assignment
  ibm_iam_service_policy_assignment:
    assignment_id: 'testString'
    state: absent
'''

RETURN = r'''
template_id:
  description: "policy template id."
  type: str
  returned: on success for create, update operations
template_version:
  description: "policy template version."
  type: str
  returned: on success for create, update operations
assignment_id:
  description: "Passed in value to correlate with other assignments."
  type: str
  returned: on success for create, update operations
target_type:
  description: "Assignment target type."
  type: str
  choices:
    - "Account"
  returned: on success for create, update operations
target:
  description: "ID of the target account."
  type: str
  returned: on success for create, update operations
options:
  description: "List of objects with required properties for a policy assignment."
  type: list
  elements: 'dict'
  contains:
    subject_type:
      description: "The policy subject type; either 'iam_id' or 'access_group_id'."
      type: str
      choices:
        - 'iam_id'
        - 'access_group_id'
    subject_id:
      description: "The policy subject id."
      type: str
    root_requester_id:
      description: "The policy assignment requester id."
      type: str
    root_template_id:
      description: "The template id where this policy is being assigned from."
      type: str
    root_template_version:
      description: "The template version where this policy is being assigned from."
      type: str
  returned: on success for create, update operations
id:
  description: "Policy assignment ID."
  type: str
  returned: on success for create, update, delete operations
account_id:
  description: "The account GUID that the policies assignments belong to.."
  type: str
  returned: on success for create, update operations
href:
  description: "The href URL that links to the policies assignments API by policy assignment ID."
  type: str
  returned: on success for create, update operations
created_at:
  description: "The UTC timestamp when the policy assignment was created."
  type: str
  returned: on success for create, update operations
created_by_id:
  description: "The iam ID of the entity that created the policy assignment."
  type: str
  returned: on success for create, update operations
last_modified_at:
  description: "The UTC timestamp when the policy assignment was last modified."
  type: str
  returned: on success for create, update operations
last_modified_by_id:
  description: "The iam ID of the entity that last modified the policy assignment."
  type: str
  returned: on success for create, update operations
resources:
  description: "Object for each account assigned."
  type: list
  elements: 'dict'
  contains:
    target:
      description: "Account ID where resources are assigned."
      type: str
    policy:
      description: "Set of properties for the assigned resource."
      type: dict
      contains:
        resource_created:
          description: "On success, includes the  policy assigned."
          type: dict
          contains:
            id:
              description: "policy id."
              type: str
        status:
          description: "policy status."
          type: str
        error_message:
          description: "The error response from API."
          type: dict
          contains:
            trace:
              description: "The unique transaction id for the request."
              type: str
            errors:
              description: "The errors encountered during the response."
              type: list
              elements: 'dict'
              contains:
                code:
                  description: "The API error code for the error."
                  type: str
                  choices:
                    - 'insufficent_permissions'
                    - 'invalid_body'
                    - 'invalid_token'
                    - 'missing_required_query_parameter'
                    - 'not_found'
                    - 'policy_conflict_error'
                    - 'policy_not_found'
                    - 'request_not_processed'
                    - 'role_conflict_error'
                    - 'role_not_found'
                    - 'too_many_requests'
                    - 'unable_to_process'
                    - 'unsupported_content_type'
                    - 'policy_template_conflict_error'
                    - 'policy_template_not_found'
                    - 'policy_assignment_not_found'
                    - 'policy_assignment_conflict_error'
                message_:
                  description: "The error message returned by the API."
                  type: str
                details:
                  description: "Additional error details."
                  type: dict
                  contains:
                    conflicts_with:
                      description: "Details of conflicting resource."
                      type: dict
                      contains:
                        etag:
                          description: "The revision number of the resource."
                          type: str
                        role:
                          description: "The conflicting role id."
                          type: str
                        policy:
                          description: "The conflicting policy id."
                          type: str
                more_info:
                  description: "Additional info for error."
                  type: str
            status_code:
              description: "The http error code of the response."
              type: int
  returned: on success for create, update operations
iam_service_policy_assignment_status:
  description: "The policy assignment status."
  type: str
  choices:
    - "in_progress"
    - "succeeded"
    - "succeed_with_errors"
    - "failed"
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
  description: The ETag value associated with the C(PolicyAssignmentV1)
  returned: on update
  type: str
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
        template_version=dict(
            type='str',
            required=False),
        assignment_id=dict(
            type='str',
            required=False),
        if_match=dict(
            type='str',
            required=False),
        accept_language=dict(
            type='str',
            required=False),
        version=dict(
            type='str',
            choices=[
                '1.0',
            ],
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
    assignment_id = module.params["assignment_id"]
    if_match = module.params["if_match"]
    accept_language = module.params["accept_language"]
    version = module.params["version"]
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
    if assignment_id:
        try:
            sdk.get_policy_assignment(
                assignment_id=assignment_id,
                version=version,
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
                sdk.delete_policy_assignment(
                    assignment_id=assignment_id,
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
                response = sdk.create_policy_template_assignment(
                    version=version,
                    policy_assignment_v1_request=policy_assignment_v1_request,
                    accept_language=accept_language,
                )
            except ApiException as ex:
                module.fail_json(msg=ex.message)
            else:
                result = response.get_result()
                if 'status' in result:
                    result['iam_service_policy_assignment_status'] = result['status']
                    del result['status']

                module.exit_json(changed=True, **result)
        else:
            # Update path
            try:
                response = sdk.update_policy_assignment(
                    assignment_id=assignment_id,
                    version=version,
                    if_match=if_match,
                    template_version=template_version,
                )
            except ApiException as ex:
                module.fail_json(msg=ex.message)
            else:
                result = response.get_result()
                if 'status' in result:
                    result['iam_service_policy_assignment_status'] = result['status']
                    del result['status']
                etag = response.get_headers().get('ETag')

                module.exit_json(changed=True, etag=etag, **result)


def main():
    run_module()


if __name__ == '__main__':
    main()
