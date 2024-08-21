#!/usr/bin/python
# coding: utf-8

# (C) Copyright IBM Corp. 2024.
#
# GNU General Public License v3.0+ (see LICENSE or https://www.gnu.org/licenses/gpl-3.0.txt)

from __future__ import (absolute_import, division, print_function)
__metaclass__ = type


DOCUMENTATION = r'''
---
module: ibm_iam_service_policy_template
short_description: Manage C(iam_service_policy_templates) for IAM Policy Management.
author: Gannayak Pabra (@Gannayak0722)
version_added: "1.0.0"
description:
  - This module creates, updates, or deletes an C(iam_service_policy_template) resource for IAM Policy Management.
requirements:
  - "IamPolicyManagementV1"
options:
  committed:
    description: "Committed status of the template."
    type: bool
  account_id:
    description: "Enterprise account ID where this template will be created."
    type: str
  name:
    description: "Required field when creating a new template. Otherwise this field is optional. If
      the field is included it will change the name value for all existing versions of the
      template."
    type: str
  description:
    description: "Description of the policy template. This is shown to users in the enterprise
      account. Use this to describe the purpose or context of the policy for enterprise
      users managing IAM templates."
    type: str
  policy:
    description: "The core set of properties associated with the template's policy objet."
    type: dict
    suboptions:
      type:
        description: "The policy type; either 'access' or 'authorization'."
        type: str
        choices:
          - "access"
          - "authorization"
      description:
        description: "Description of the policy. This is shown in child accounts when an access group or
          trusted profile template uses the policy template to assign access."
        type: str
      resource:
        description: "The resource attributes to which the policy grants access."
        type: dict
        suboptions:
          attributes:
            description: "List of resource attributes to which the policy grants access."
            type: list
            elements: 'dict'
            suboptions:
              key:
                description: "The name of a resource attribute."
                type: str
              operator:
                description: "The operator of an attribute."
                type: str
                choices:
                  - "stringEquals"
                  - "stringExists"
                  - "stringMatch"
                  - "stringEqualsAnyOf"
                  - "stringMatchAnyOf"
              value:
                description: "The value of a rule, resource, or subject attribute; can be boolean or string for
                  resource and subject attribute. Can be string or an array of strings (e.g., array of
                  days to permit access) for rule attribute."
                type: raw
          tags:
            description: "Optional list of resource tags to which the policy grants access."
            type: list
            elements: 'dict'
            suboptions:
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
                  - "stringEquals"
                  - "stringMatch"
      subject:
        description: "The subject attributes for whom the policy grants access."
        type: dict
        suboptions:
          attributes:
            description: "List of subject attributes associated with policy/."
            type: list
            elements: 'dict'
            suboptions:
              key:
                description: "The name of a subject attribute, e.g., iam_id, access_group_id."
                type: str
              operator:
                description: "The operator of an attribute."
                type: str
                choices:
                  - "stringEquals"
                  - "stringExists"
              value:
                description: "The value of a rule, resource, or subject attribute; can be boolean or string for
                  resource and subject attribute. Can be string or an array of strings (e.g., array of
                  days to permit access) for rule attribute."
                type: raw
      pattern:
        description: "Indicates pattern of rule, either 'time-based-conditions:once',
          'time-based-conditions:weekly:all-day', or
          'time-based-conditions:weekly:custom-hours'."
        type: str
      rule:
        description: "Additional access conditions associated with the policy."
        type: dict
        suboptions:
          key:
            description: "The name of an attribute."
            type: str
          operator:
            description: "The operator of an attribute."
            type: str
            choices:
              - "stringEquals"
              - "stringExists"
              - "stringEqualsAnyOf"
              - "stringMatchAnyOf"
              - "stringMatch"
              - "timeLessThan"
              - "timeLessThanOrEquals"
              - "timeGreaterThan"
              - "timeGreaterThanOrEquals"
              - "dateLessThan"
              - "dateLessThanOrEquals"
              - "dateGreaterThan"
              - "dateGreaterThanOrEquals"
              - "dateTimeLessThan"
              - "dateTimeLessThanOrEquals"
              - "dateTimeGreaterThan"
              - "dateTimeGreaterThanOrEquals"
              - "dayOfWeekEquals"
              - "dayOfWeekAnyOf"
          value:
            description: "The value of a rule, resource, or subject attribute; can be boolean or string for
              resource and subject attribute. Can be string or an array of strings (e.g., array of
              days to permit access) for rule attribute."
            type: raw
          conditions:
            description: "List of conditions associated with a policy, e.g., time-based conditions that grant
              access over a certain time period."
            type: list
            elements: 'dict'
            suboptions:
              key:
                description: "The name of an attribute."
                type: str
              operator:
                description: "The operator of an attribute."
                type: str
                choices:
                  - "stringEquals"
                  - "stringExists"
                  - "stringEqualsAnyOf"
                  - "stringMatchAnyOf"
                  - "stringMatch"
                  - "timeLessThan"
                  - "timeLessThanOrEquals"
                  - "timeGreaterThan"
                  - "timeGreaterThanOrEquals"
                  - "dateLessThan"
                  - "dateLessThanOrEquals"
                  - "dateGreaterThan"
                  - "dateGreaterThanOrEquals"
                  - "dateTimeLessThan"
                  - "dateTimeLessThanOrEquals"
                  - "dateTimeGreaterThan"
                  - "dateTimeGreaterThanOrEquals"
                  - "dayOfWeekEquals"
                  - "dayOfWeekAnyOf"
              value:
                description: "The value of a rule, resource, or subject attribute; can be boolean or string for
                  resource and subject attribute. Can be string or an array of strings (e.g., array of
                  days to permit access) for rule attribute."
                type: raw
              conditions:
                description: "List of conditions associated with a policy, e.g., time-based conditions that grant
                  access over a certain time period."
                type: list
                elements: 'dict'
                suboptions:
                  key:
                    description: "The name of an attribute."
                    type: str
                  operator:
                    description: "The operator of an attribute."
                    type: str
                    choices:
                      - "stringEquals"
                      - "stringExists"
                      - "stringEqualsAnyOf"
                      - "stringMatchAnyOf"
                      - "stringMatch"
                      - "timeLessThan"
                      - "timeLessThanOrEquals"
                      - "timeGreaterThan"
                      - "timeGreaterThanOrEquals"
                      - "dateLessThan"
                      - "dateLessThanOrEquals"
                      - "dateGreaterThan"
                      - "dateGreaterThanOrEquals"
                      - "dateTimeLessThan"
                      - "dateTimeLessThanOrEquals"
                      - "dateTimeGreaterThan"
                      - "dateTimeGreaterThanOrEquals"
                      - "dayOfWeekEquals"
                      - "dayOfWeekAnyOf"
                  value:
                    description: "The value of a rule, resource, or subject attribute; can be boolean or string for
                      resource and subject attribute. Can be string or an array of strings (e.g., array of
                      days to permit access) for rule attribute."
                    type: raw
      control:
        description: "Specifies the type of access granted by the policy."
        type: dict
        suboptions:
          grant:
            description: "Permission granted by the policy."
            type: dict
            suboptions:
              roles:
                description: "A set of role cloud resource names (CRNs) granted by the policy."
                type: list
                elements: 'dict'
                suboptions:
                  role_id:
                    description: "The role Cloud Resource Name (CRN) granted by the policy. Example CRN:
                      'crn:v1:bluemix:public:iam::::role:Editor'."
                    type: str
  if_match:
    description: "The revision number for updating a policy template version and must match the ETag
      value of the existing policy template version. The Etag can be retrieved using the
      GET /v1/policy_templates/{policy_template_id}/versions/{version} API and looking at
      the ETag response header."
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
  iam_service_policy_template_state:
    description: "The policy template state."
    type: str
    choices:
      - "active"
      - "deleted"
  version:
    description: "The policy template version."
    type: str
  policy_template_id:
    description: "The policy template ID."
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
- name: Create ibm_iam_service_policy_template
  vars:
    v2_policy_resource_attribute_model:
      key: 'testString'
      operator: 'stringEquals'
      value: 'testString'
    v2_policy_resource_tag_model:
      key: 'testString'
      value: 'testString'
      operator: 'stringEquals'
    v2_policy_resource_model:
      attributes: [v2_policy_resource_attribute_model]
      tags: [v2_policy_resource_tag_model]
    v2_policy_subject_attribute_model:
      key: 'testString'
      operator: 'stringEquals'
      value: 'testString'
    v2_policy_subject_model:
      attributes: [v2_policy_subject_attribute_model]
    v2_policy_rule_model:
      key: 'testString'
      operator: 'stringEquals'
      value: 'testString'
    roles_model:
      role_id: 'testString'
    grant_model:
      roles: [roles_model]
    control_model:
      grant: grant_model
    template_policy_model:
      type: 'access'
      description: 'testString'
      resource: v2_policy_resource_model
      subject: v2_policy_subject_model
      pattern: 'testString'
      rule: v2_policy_rule_model
      control: control_model
  ibm_iam_service_policy_template:
    name: 'testString'
    account_id: 'testString'
    policy: '{{ template_policy_model }}'
    description: 'testString'
    committed: True
    accept_language: 'default'
    state: present

- name: Update ibm_iam_service_policy_template
  vars:
    v2_policy_resource_attribute_model:
      key: 'testString'
      operator: 'stringEquals'
      value: 'testString'
    v2_policy_resource_tag_model:
      key: 'testString'
      value: 'testString'
      operator: 'stringEquals'
    v2_policy_resource_model:
      attributes: [v2_policy_resource_attribute_model]
      tags: [v2_policy_resource_tag_model]
    v2_policy_subject_attribute_model:
      key: 'testString'
      operator: 'stringEquals'
      value: 'testString'
    v2_policy_subject_model:
      attributes: [v2_policy_subject_attribute_model]
    v2_policy_rule_model:
      key: 'testString'
      operator: 'stringEquals'
      value: 'testString'
    roles_model:
      role_id: 'testString'
    grant_model:
      roles: [roles_model]
    control_model:
      grant: grant_model
    template_policy_model:
      type: 'access'
      description: 'testString'
      resource: v2_policy_resource_model
      subject: v2_policy_subject_model
      pattern: 'testString'
      rule: v2_policy_rule_model
      control: control_model
  ibm_iam_service_policy_template:
    policy_template_id: 'testString'
    version: 'testString'
    if_match: 'testString'
    policy: '{{ template_policy_model }}'
    name: 'testString'
    description: 'testString'
    committed: True
    state: present

- name: Delete ibm_iam_service_policy_template
  ibm_iam_service_policy_template:
    policy_template_id: 'testString'
    state: absent
'''

RETURN = r'''
name:
  description: "Required field when creating a new template. Otherwise this field is optional. If the
    field is included it will change the name value for all existing versions of the
    template."
  type: str
  returned: on success for create, update operations
description:
  description: "Description of the policy template. This is shown to users in the enterprise account.
    Use this to describe the purpose or context of the policy for enterprise users
    managing IAM templates."
  type: str
  returned: on success for create, update operations
account_id:
  description: "Enterprise account ID where this template will be created."
  type: str
  returned: on success for create, update operations
version:
  description: "Template version."
  type: str
  returned: on success for create, update operations
committed:
  description: "Committed status of the template version."
  type: bool
  returned: on success for create, update operations
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
  returned: on success for create, update operations
iam_service_policy_template_state:
  description: "State of policy template."
  type: str
  choices:
    - "active"
    - "deleted"
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
        committed=dict(
            type='bool',
            required=False),
        account_id=dict(
            type='str',
            required=False),
        name=dict(
            type='str',
            required=False),
        description=dict(
            type='str',
            required=False),
        # Represents the TemplatePolicy Python class
        policy=dict(
            type='dict',
            options=dict(
                type=dict(
                    type='str',
                    choices=[
                        'access',
                        'authorization',
                    ],
                    required=False),
                description=dict(
                    type='str',
                    required=False),
                resource=dict(
                    type='dict',
                    options=dict(
                        attributes=dict(
                            type='list',
                            elements='dict',
                            options=dict(
                                key=dict(
                                    type='str',
                                    no_log=True,
                                    required=False),
                                operator=dict(
                                    type='str',
                                    choices=[
                                        'stringEquals',
                                        'stringExists',
                                        'stringMatch',
                                        'stringEqualsAnyOf',
                                        'stringMatchAnyOf',
                                    ],
                                    required=False),
                                value=dict(
                                    type='raw',
                                    required=False),
                            ),
                            required=False),
                        tags=dict(
                            type='list',
                            elements='dict',
                            options=dict(
                                key=dict(
                                    type='str',
                                    no_log=True,
                                    required=False),
                                value=dict(
                                    type='str',
                                    required=False),
                                operator=dict(
                                    type='str',
                                    choices=[
                                        'stringEquals',
                                        'stringMatch',
                                    ],
                                    required=False),
                            ),
                            required=False),
                    ),
                    required=False),
                subject=dict(
                    type='dict',
                    options=dict(
                        attributes=dict(
                            type='list',
                            elements='dict',
                            options=dict(
                                key=dict(
                                    type='str',
                                    no_log=True,
                                    required=False),
                                operator=dict(
                                    type='str',
                                    choices=[
                                        'stringEquals',
                                        'stringExists',
                                    ],
                                    required=False),
                                value=dict(
                                    type='raw',
                                    required=False),
                            ),
                            required=False),
                    ),
                    required=False),
                pattern=dict(
                    type='str',
                    required=False),
                rule=dict(
                    type='dict',
                    options=dict(
                        key=dict(
                            type='str',
                            no_log=True,
                            required=False),
                        operator=dict(
                            type='str',
                            choices=[
                                'stringEquals',
                                'stringExists',
                                'stringEqualsAnyOf',
                                'stringMatchAnyOf',
                                'stringMatch',
                                'timeLessThan',
                                'timeLessThanOrEquals',
                                'timeGreaterThan',
                                'timeGreaterThanOrEquals',
                                'dateLessThan',
                                'dateLessThanOrEquals',
                                'dateGreaterThan',
                                'dateGreaterThanOrEquals',
                                'dateTimeLessThan',
                                'dateTimeLessThanOrEquals',
                                'dateTimeGreaterThan',
                                'dateTimeGreaterThanOrEquals',
                                'dayOfWeekEquals',
                                'dayOfWeekAnyOf',
                            ],
                            required=False),
                        value=dict(
                            type='raw',
                            required=False),
                        conditions=dict(
                            type='list',
                            elements='dict',
                            options=dict(
                                key=dict(
                                    type='str',
                                    no_log=True,
                                    required=False),
                                operator=dict(
                                    type='str',
                                    choices=[
                                        'stringEquals',
                                        'stringExists',
                                        'stringEqualsAnyOf',
                                        'stringMatchAnyOf',
                                        'stringMatch',
                                        'timeLessThan',
                                        'timeLessThanOrEquals',
                                        'timeGreaterThan',
                                        'timeGreaterThanOrEquals',
                                        'dateLessThan',
                                        'dateLessThanOrEquals',
                                        'dateGreaterThan',
                                        'dateGreaterThanOrEquals',
                                        'dateTimeLessThan',
                                        'dateTimeLessThanOrEquals',
                                        'dateTimeGreaterThan',
                                        'dateTimeGreaterThanOrEquals',
                                        'dayOfWeekEquals',
                                        'dayOfWeekAnyOf',
                                    ],
                                    required=False),
                                value=dict(
                                    type='raw',
                                    required=False),
                                conditions=dict(
                                    type='list',
                                    elements='dict',
                                    options=dict(
                                        key=dict(
                                            type='str',
                                            no_log=True,
                                            required=False),
                                        operator=dict(
                                            type='str',
                                            choices=[
                                                'stringEquals',
                                                'stringExists',
                                                'stringEqualsAnyOf',
                                                'stringMatchAnyOf',
                                                'stringMatch',
                                                'timeLessThan',
                                                'timeLessThanOrEquals',
                                                'timeGreaterThan',
                                                'timeGreaterThanOrEquals',
                                                'dateLessThan',
                                                'dateLessThanOrEquals',
                                                'dateGreaterThan',
                                                'dateGreaterThanOrEquals',
                                                'dateTimeLessThan',
                                                'dateTimeLessThanOrEquals',
                                                'dateTimeGreaterThan',
                                                'dateTimeGreaterThanOrEquals',
                                                'dayOfWeekEquals',
                                                'dayOfWeekAnyOf',
                                            ],
                                            required=False),
                                        value=dict(
                                            type='raw',
                                            required=False),
                                    ),
                                    required=False),
                            ),
                            required=False),
                    ),
                    required=False),
                control=dict(
                    type='dict',
                    options=dict(
                        grant=dict(
                            type='dict',
                            options=dict(
                                roles=dict(
                                    type='list',
                                    elements='dict',
                                    options=dict(
                                        role_id=dict(
                                            type='str',
                                            required=False),
                                    ),
                                    required=False),
                            ),
                            required=False),
                    ),
                    required=False),
            ),
            required=False),
        if_match=dict(
            type='str',
            required=False),
        accept_language=dict(
            type='str',
            required=False),
        iam_service_policy_template_state=dict(
            type='str',
            choices=[
                'active',
                'deleted',
            ],
            required=False),
        version=dict(
            type='str',
            required=False),
        policy_template_id=dict(
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

    committed = module.params["committed"]
    account_id = module.params["account_id"]
    name = module.params["name"]
    description = module.params["description"]
    policy = module.params["policy"]
    if_match = module.params["if_match"]
    accept_language = module.params["accept_language"]
    iam_service_policy_template_state = module.params["iam_service_policy_template_state"]
    version = module.params["version"]
    policy_template_id = module.params["policy_template_id"]
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
    if policy_template_id:
        try:
            sdk.get_policy_template(
                policy_template_id=policy_template_id,
                state=iam_service_policy_template_state,
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
                sdk.delete_policy_template(
                    policy_template_id=policy_template_id,
                )
            except ApiException as ex:
                module.fail_json(msg=ex.message)
            else:
                module.exit_json(changed=True, id=policy_template_id, status="deleted")
        else:
            module.exit_json(changed=False, id=policy_template_id, status="not_found")

    if state == "present":
        if not resource_exists:
            # Create path
            try:
                response = sdk.create_policy_template(
                    name=name,
                    account_id=account_id,
                    policy=policy,
                    description=description,
                    committed=committed,
                    accept_language=accept_language,
                )
            except ApiException as ex:
                module.fail_json(msg=ex.message)
            else:
                result = response.get_result()
                if 'state' in result:
                    result['iam_service_policy_template_state'] = result['state']
                    del result['state']

                module.exit_json(changed=True, **result)
        else:
            # Update path
            try:
                response = sdk.replace_policy_template(
                    policy_template_id=policy_template_id,
                    version=version,
                    if_match=if_match,
                    policy=policy,
                    name=name,
                    description=description,
                    committed=committed,
                )
            except ApiException as ex:
                module.fail_json(msg=ex.message)
            else:
                result = response.get_result()
                if 'state' in result:
                    result['iam_service_policy_template_state'] = result['state']
                    del result['state']

                module.exit_json(changed=True, **result)


def main():
    run_module()


if __name__ == '__main__':
    main()
