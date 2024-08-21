#!/usr/bin/python
# coding: utf-8

# (C) Copyright IBM Corp. 2024.
#
# GNU General Public License v3.0+ (see LICENSE or https://www.gnu.org/licenses/gpl-3.0.txt)

from __future__ import (absolute_import, division, print_function)
__metaclass__ = type


DOCUMENTATION = r'''
---
module: ibm_iam_service_policy_assignment_info
short_description: Manage C(iam_service_policy_assignment) for IAM Policy Management.
author: Gannayak Pabra (@Gannayak0722)
version_added: "1.0.0"
description:
  - This module retrieves one or more C(iam_service_policy_assignment) for IAM Policy Management.
requirements:
  - "IamPolicyManagementV1"
options:
  account_id:
    description: "The account GUID in which the policies belong to."
    type: str
  template_version:
    description: "Optional policy template version."
    type: str
  template_id:
    description: "Optional template id."
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

- name: List ibm_iam_service_policy_assignment
  ibm_iam_service_policy_assignment_info:
    version: '1.0'
    account_id: 'testString'
    accept_language: 'default'
    template_id: 'testString'
    template_version: 'testString'
'''

RETURN = r'''
assignments:
  description: "List of policy assignments."
  type: list
  elements: 'dict'
  contains:
    target:
      description: "assignment target account and type."
      type: dict
      contains:
        type:
          description: "Assignment target type."
          type: str
          choices:
            - 'Account'
        id:
          description: "ID of the target account."
          type: str
    options:
      description: "The set of properties required for a policy assignment."
      type: dict
      contains:
        root:
          description: "No description has been provided."
          type: dict
          contains:
            requester_id:
              description: "No description has been provided."
              type: str
            assignment_id:
              description: "Passed in value to correlate with other assignments."
              type: str
            template:
              description: "No description has been provided."
              type: dict
              contains:
                id:
                  description: "The template id where this policy is being assigned from."
                  type: str
                version:
                  description: "The template version where this policy is being assigned from."
                  type: str
    id:
      description: "Policy assignment ID."
      type: str
    account_id:
      description: "The account GUID that the policies assignments belong to.."
      type: str
    href:
      description: "The href URL that links to the policies assignments API by policy assignment ID."
      type: str
    created_at:
      description: "The UTC timestamp when the policy assignment was created."
      type: str
    created_by_id:
      description: "The iam ID of the entity that created the policy assignment."
      type: str
    last_modified_at:
      description: "The UTC timestamp when the policy assignment was last modified."
      type: str
    last_modified_by_id:
      description: "The iam ID of the entity that last modified the policy assignment."
      type: str
    resources:
      description: "Object for each account assigned."
      type: list
      elements: 'dict'
      contains:
        target:
          description: "assignment target account and type."
          type: dict
          contains:
            type:
              description: "Assignment target type."
              type: str
              choices:
                - 'Account'
            id:
              description: "ID of the target account."
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
    subject:
      description: "subject details of access type assignment."
      type: dict
      contains:
        id:
          description: "No description has been provided."
          type: str
        type:
          description: "No description has been provided."
          type: str
          choices:
            - 'iam_id'
            - 'access_group_id'
    template:
      description: "policy template details."
      type: dict
      contains:
        id:
          description: "policy template id."
          type: str
        version:
          description: "policy template version."
          type: str
    status:
      description: "The policy assignment status."
      type: str
      choices:
        - 'in_progress'
        - 'succeeded'
        - 'succeed_with_errors'
        - 'failed'
    template_id:
      description: "policy template id."
      type: str
    template_version:
      description: "policy template version."
      type: str
    assignment_id:
      description: "Passed in value to correlate with other assignments."
      type: str
    target_type:
      description: "Assignment target type."
      type: str
      choices:
        - 'Account'
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
        template_version=dict(
            type='str',
            required=False),
        template_id=dict(
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
    )

    module = AnsibleModule(
        argument_spec=module_args,
        supports_check_mode=True
    )

    if MISSING_IMPORT_EXC is not None:
        module.fail_json(msg='Missing required import: ' + MISSING_IMPORT_EXC.msg)

    account_id = module.params["account_id"]
    template_version = module.params["template_version"]
    template_id = module.params["template_id"]
    accept_language = module.params["accept_language"]
    version = module.params["version"]

    if module.check_mode:
        module.exit_json(msg='The module would run with the following parameters: ' + module.paramss)

    authenticator = get_authenticator(service_name='iam_policy_management')
    if authenticator is None:
        module.fail_json(msg='Cannot create the authenticator.')

    sdk = IamPolicyManagementV1(
        authenticator=authenticator,
    )

    sdk.configure_service('iam_policy_management')

    # list
    try:
        response = sdk.list_policy_assignments(
            version=version,
            account_id=account_id,
            accept_language=accept_language,
            template_id=template_id,
            template_version=template_version,
        )

        result = response.get_result()

        module.exit_json(**result)
    except ApiException as ex:
        module.fail_json(msg=ex.message)


def main():
    run_module()


if __name__ == '__main__':
    main()
