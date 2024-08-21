#!/usr/bin/python
# coding: utf-8

# (C) Copyright IBM Corp. 2024.
#
# GNU General Public License v3.0+ (see LICENSE or https://www.gnu.org/licenses/gpl-3.0.txt)

from __future__ import (absolute_import, division, print_function)
__metaclass__ = type


DOCUMENTATION = r'''
---
module: ibm_iam_service_v2policy_info
short_description: Manage C(iam_service_v2policy) for IAM Policy Management.
author: Gannayak Pabra (@Gannayak0722)
version_added: "1.0.0"
description:
  - This module retrieves one or more C(iam_service_v2policy) for IAM Policy Management.
requirements:
  - "IamPolicyManagementV1"
options:
  format:
    description: "Include additional data for policy returned
      * C(includeI(last)permit) - returns details of when the policy last granted a permit
      decision and the number of times it has done so
      * C(display) - returns the list of all actions included in each of the policy roles
      and translations for all relevant fields."
    type: str
    choices:
      - "include_last_permit"
      - "display"
  id:
    description: "The policy ID."
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
- name: Read ibm_iam_service_v2policy
  ibm_iam_service_v2policy_info:
    id: 'testString'
    format: 'include_last_permit'
'''

RETURN = r'''
type:
  description: "The policy type; either 'access' or 'authorization'."
  type: str
  choices:
    - "access"
    - "authorization"
  returned: on success for read operation
description:
  description: "Description of the policy."
  type: str
  returned: on success for read operation
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
  returned: on success for read operation
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
  returned: on success for read operation
pattern:
  description: "Indicates pattern of rule, either 'time-based-conditions:once',
    'time-based-conditions:weekly:all-day', or
    'time-based-conditions:weekly:custom-hours'."
  type: str
  returned: on success for read operation
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
  returned: on success for read operation
template:
  description: "The details of the IAM template that was used to create an enterprise-managed policy
    in your account. When returned, this indicates that the policy is created from and
    managed by a template in the root enterprise account."
  type: dict
  contains:
    id:
      description: "The policy template ID."
      type: str
    version:
      description: "Template version."
      type: str
    assignment_id:
      description: "policy assignment id."
      type: str
    root_id:
      description: "orchestrator template id."
      type: str
    root_version:
      description: "orchestrator template version."
      type: str
  returned: on success for read operation
msg:
  description: an error message that describes what went wrong
  type: str
  returned: on error
etag:
  description: The ETag value associated with the C(V2PolicyTemplateMetaData)
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
        format=dict(
            type='str',
            choices=[
                'include_last_permit',
                'display',
            ],
            required=False),
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

    format = module.params["format"]
    id = module.params["id"]

    if module.check_mode:
        module.exit_json(msg='The module would run with the following parameters: ' + module.paramss)

    authenticator = get_authenticator(service_name='iam_policy_management')
    if authenticator is None:
        module.fail_json(msg='Cannot create the authenticator.')

    sdk = IamPolicyManagementV1(
        authenticator=authenticator,
    )

    sdk.configure_service('iam_policy_management')

    if id:
        # read
        try:
            response = sdk.get_v2_policy(
                id=id,
                format=format,
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
