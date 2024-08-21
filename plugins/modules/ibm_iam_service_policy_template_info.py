#!/usr/bin/python
# coding: utf-8

# (C) Copyright IBM Corp. 2024.
#
# GNU General Public License v3.0+ (see LICENSE or https://www.gnu.org/licenses/gpl-3.0.txt)

from __future__ import (absolute_import, division, print_function)
__metaclass__ = type


DOCUMENTATION = r'''
---
module: ibm_iam_service_policy_template_info
short_description: Manage C(iam_service_policy_template) for IAM Policy Management.
author: Gannayak Pabra (@Gannayak0722)
version_added: "1.0.0"
description:
  - This module retrieves one or more C(iam_service_policy_template) for IAM Policy Management.
requirements:
  - "IamPolicyManagementV1"
options:
  version:
    description: "The policy template version."
    type: str
  policy_template_id:
    description: "The policy template ID."
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
- name: Read ibm_iam_service_policy_template
  ibm_iam_service_policy_template_info:
    policy_template_id: 'testString'
    version: 'testString'
'''

RETURN = r'''
name:
  description: "Required field when creating a new template. Otherwise this field is optional. If the
    field is included it will change the name value for all existing versions of the
    template."
  type: str
  returned: on success for read operation
description:
  description: "Description of the policy template. This is shown to users in the enterprise account.
    Use this to describe the purpose or context of the policy for enterprise users
    managing IAM templates."
  type: str
  returned: on success for read operation
account_id:
  description: "Enterprise account ID where this template will be created."
  type: str
  returned: on success for read operation
version:
  description: "Template version."
  type: str
  returned: on success for read operation
committed:
  description: "Committed status of the template version."
  type: bool
  returned: on success for read operation
policy:
  description: "The core set of properties associated with the template's policy objet."
  type: dict
  contains:
    type:
      description: "The policy type; either 'access' or 'authorization'."
      type: str
      choices:
        - 'access'
        - 'authorization'
    description:
      description: "Description of the policy. This is shown in child accounts when an access group or
        trusted profile template uses the policy template to assign access."
      type: str
    resource:
      description: "The resource attributes to which the policy grants access."
      type: dict
      contains:
        attributes:
          description: "List of resource attributes to which the policy grants access."
          type: list
          elements: 'dict'
          contains:
            key:
              description: "The name of a resource attribute."
              type: str
            operator:
              description: "The operator of an attribute."
              type: str
              choices:
                - 'stringEquals'
                - 'stringExists'
                - 'stringMatch'
                - 'stringEqualsAnyOf'
                - 'stringMatchAnyOf'
            value:
              description: "The value of a rule, resource, or subject attribute; can be boolean or string for
                resource and subject attribute. Can be string or an array of strings (e.g., array of
                days to permit access) for rule attribute."
              type: dict
        tags:
          description: "Optional list of resource tags to which the policy grants access."
          type: list
          elements: 'dict'
          contains:
            key:
              description: "The name of an access management tag."
              type: str
            value:
              description: "The value of an access management tag."
              type: str
            operator:
              description: "The operator of an access management tag."
              type: str
              choices:
                - 'stringEquals'
                - 'stringMatch'
    subject:
      description: "The subject attributes for whom the policy grants access."
      type: dict
      contains:
        attributes:
          description: "List of subject attributes associated with policy/."
          type: list
          elements: 'dict'
          contains:
            key:
              description: "The name of a subject attribute, e.g., iam_id, access_group_id."
              type: str
            operator:
              description: "The operator of an attribute."
              type: str
              choices:
                - 'stringEquals'
                - 'stringExists'
            value:
              description: "The value of a rule, resource, or subject attribute; can be boolean or string for
                resource and subject attribute. Can be string or an array of strings (e.g., array of
                days to permit access) for rule attribute."
              type: dict
    pattern:
      description: "Indicates pattern of rule, either 'time-based-conditions:once',
        'time-based-conditions:weekly:all-day', or
        'time-based-conditions:weekly:custom-hours'."
      type: str
    rule:
      description: "Additional access conditions associated with the policy."
      type: dict
      contains:
        key:
          description: "The name of an attribute."
          type: str
        operator:
          description: "The operator of an attribute."
          type: str
          choices:
            - 'stringEquals'
            - 'stringExists'
            - 'stringEqualsAnyOf'
            - 'stringMatchAnyOf'
            - 'stringMatch'
            - 'timeLessThan'
            - 'timeLessThanOrEquals'
            - 'timeGreaterThan'
            - 'timeGreaterThanOrEquals'
            - 'dateLessThan'
            - 'dateLessThanOrEquals'
            - 'dateGreaterThan'
            - 'dateGreaterThanOrEquals'
            - 'dateTimeLessThan'
            - 'dateTimeLessThanOrEquals'
            - 'dateTimeGreaterThan'
            - 'dateTimeGreaterThanOrEquals'
            - 'dayOfWeekEquals'
            - 'dayOfWeekAnyOf'
        value:
          description: "The value of a rule, resource, or subject attribute; can be boolean or string for
            resource and subject attribute. Can be string or an array of strings (e.g., array of
            days to permit access) for rule attribute."
          type: dict
        conditions:
          description: "List of conditions associated with a policy, e.g., time-based conditions that grant
            access over a certain time period."
          type: list
          elements: 'dict'
          contains:
            key:
              description: "The name of an attribute."
              type: str
            operator:
              description: "The operator of an attribute."
              type: str
              choices:
                - 'stringEquals'
                - 'stringExists'
                - 'stringEqualsAnyOf'
                - 'stringMatchAnyOf'
                - 'stringMatch'
                - 'timeLessThan'
                - 'timeLessThanOrEquals'
                - 'timeGreaterThan'
                - 'timeGreaterThanOrEquals'
                - 'dateLessThan'
                - 'dateLessThanOrEquals'
                - 'dateGreaterThan'
                - 'dateGreaterThanOrEquals'
                - 'dateTimeLessThan'
                - 'dateTimeLessThanOrEquals'
                - 'dateTimeGreaterThan'
                - 'dateTimeGreaterThanOrEquals'
                - 'dayOfWeekEquals'
                - 'dayOfWeekAnyOf'
            value:
              description: "The value of a rule, resource, or subject attribute; can be boolean or string for
                resource and subject attribute. Can be string or an array of strings (e.g., array of
                days to permit access) for rule attribute."
              type: dict
            conditions:
              description: "List of conditions associated with a policy, e.g., time-based conditions that grant
                access over a certain time period."
              type: list
              elements: 'dict'
              contains:
                key:
                  description: "The name of an attribute."
                  type: str
                operator:
                  description: "The operator of an attribute."
                  type: str
                  choices:
                    - 'stringEquals'
                    - 'stringExists'
                    - 'stringEqualsAnyOf'
                    - 'stringMatchAnyOf'
                    - 'stringMatch'
                    - 'timeLessThan'
                    - 'timeLessThanOrEquals'
                    - 'timeGreaterThan'
                    - 'timeGreaterThanOrEquals'
                    - 'dateLessThan'
                    - 'dateLessThanOrEquals'
                    - 'dateGreaterThan'
                    - 'dateGreaterThanOrEquals'
                    - 'dateTimeLessThan'
                    - 'dateTimeLessThanOrEquals'
                    - 'dateTimeGreaterThan'
                    - 'dateTimeGreaterThanOrEquals'
                    - 'dayOfWeekEquals'
                    - 'dayOfWeekAnyOf'
                value:
                  description: "The value of a rule, resource, or subject attribute; can be boolean or string for
                    resource and subject attribute. Can be string or an array of strings (e.g., array of
                    days to permit access) for rule attribute."
                  type: dict
    control:
      description: "Specifies the type of access granted by the policy."
      type: dict
      contains:
        grant:
          description: "Permission granted by the policy."
          type: dict
          contains:
            roles:
              description: "A set of role cloud resource names (CRNs) granted by the policy."
              type: list
              elements: 'dict'
              contains:
                role_id:
                  description: "The role Cloud Resource Name (CRN) granted by the policy. Example CRN:
                    'crn:v1:bluemix:public:iam::::role:Editor'."
                  type: str
  returned: on success for read operation
state:
  description: "State of policy template."
  type: str
  choices:
    - "active"
    - "deleted"
  returned: on success for read operation
msg:
  description: an error message that describes what went wrong
  type: str
  returned: on error
etag:
  description: The ETag value associated with the C(PolicyTemplate)
  returned: on read
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
        version=dict(
            type='str',
            required=False),
        policy_template_id=dict(
            type='str',
            required=False),
    )

    module = AnsibleModule(
        argument_spec=module_args,
        supports_check_mode=True
    )

    if MISSING_IMPORT_EXC is not None:
        module.fail_json(msg='Missing required import: ' + MISSING_IMPORT_EXC.msg)

    version = module.params["version"]
    policy_template_id = module.params["policy_template_id"]

    if module.check_mode:
        module.exit_json(msg='The module would run with the following parameters: ' + module.paramss)

    authenticator = get_authenticator(service_name='iam_policy_management')
    if authenticator is None:
        module.fail_json(msg='Cannot create the authenticator.')

    sdk = IamPolicyManagementV1(
        authenticator=authenticator,
    )

    sdk.configure_service('iam_policy_management')

    if policy_template_id:
        # read
        try:
            response = sdk.get_policy_template_version(
                policy_template_id=policy_template_id,
                version=version,
            )

            result = response.get_result()
            etag = response.get_headers().get('ETag')

            module.exit_json(etag=etag, **result)
        except ApiException as ex:
            module.fail_json(msg=ex.message)


def main():
    run_module()


if __name__ == '__main__':
    main()
