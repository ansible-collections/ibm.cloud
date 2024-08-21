#!/usr/bin/python
# coding: utf-8

# (C) Copyright IBM Corp. 2024.
#
# GNU General Public License v3.0+ (see LICENSE or https://www.gnu.org/licenses/gpl-3.0.txt)

from __future__ import (absolute_import, division, print_function)
__metaclass__ = type


DOCUMENTATION = r'''
---
module: ibm_iam_service_policy
short_description: Manage C(iam_service_policys) for IAM Policy Management.
author: Gannayak Pabra (@Gannayak0722)
version_added: "1.0.0"
description:
  - This module creates, updates, or deletes an C(iam_service_policy) resource for IAM Policy Management.
requirements:
  - "IamPolicyManagementV1"
options:
  subjects:
    description: "The subjects associated with a policy."
    type: list
    elements: 'dict'
    suboptions:
      attributes:
        description: "List of subject attributes."
        type: list
        elements: 'dict'
        suboptions:
          name:
            description: "The name of an attribute."
            type: str
          value:
            description: "The value of an attribute."
            type: str
  roles:
    description: "A set of role cloud resource names (CRNs) granted by the policy."
    type: list
    elements: 'dict'
    suboptions:
      role_id:
        description: "The role Cloud Resource Name (CRN) granted by the policy. Example CRN:
          'crn:v1:bluemix:public:iam::::role:Editor'."
        type: str
      display_name:
        description: "The display name of the role."
        type: str
      description:
        description: "The description of the role."
        type: str
  resources:
    description: "The resources associated with a policy."
    type: list
    elements: 'dict'
    suboptions:
      attributes:
        description: "List of resource attributes."
        type: list
        elements: 'dict'
        suboptions:
          name:
            description: "The name of an attribute."
            type: str
          value:
            description: "The value of an attribute."
            type: str
          operator:
            description: "The operator of an attribute."
            type: str
      tags:
        description: "List of access management tags."
        type: list
        elements: 'dict'
        suboptions:
          name:
            description: "The name of an access management tag."
            type: str
          value:
            description: "The value of an access management tag."
            type: str
          operator:
            description: "The operator of an access management tag."
            type: str
  description:
    description: "Customer-defined description."
    type: str
  type:
    description: "The policy type; either 'access' or 'authorization'."
    type: str
  if_match:
    description: "The revision number for updating a policy and must match the ETag value of the
      existing policy. The Etag can be retrieved using the GET /v1/policies/{policy_id}
      API and looking at the ETag response header."
    type: str
  policy_id:
    description: "The policy ID."
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
- name: Create ibm_iam_service_policy
  vars:
    subject_attribute_model:
      name: 'testString'
      value: 'testString'
    policy_subject_model:
      attributes: [subject_attribute_model]
    policy_role_model:
      role_id: 'testString'
    resource_attribute_model:
      name: 'testString'
      value: 'testString'
      operator: 'testString'
    resource_tag_model:
      name: 'testString'
      value: 'testString'
      operator: 'testString'
    policy_resource_model:
      attributes: [resource_attribute_model]
      tags: [resource_tag_model]
  ibm_iam_service_policy:
    type: 'testString'
    subjects: [policy_subject_model]
    roles: [policy_role_model]
    resources: [policy_resource_model]
    description: 'testString'
    accept_language: 'default'
    state: present

- name: Update ibm_iam_service_policy
  vars:
    subject_attribute_model:
      name: 'testString'
      value: 'testString'
    policy_subject_model:
      attributes: [subject_attribute_model]
    policy_role_model:
      role_id: 'testString'
    resource_attribute_model:
      name: 'testString'
      value: 'testString'
      operator: 'testString'
    resource_tag_model:
      name: 'testString'
      value: 'testString'
      operator: 'testString'
    policy_resource_model:
      attributes: [resource_attribute_model]
      tags: [resource_tag_model]
  ibm_iam_service_policy:
    policy_id: 'testString'
    if_match: 'testString'
    type: 'testString'
    subjects: [policy_subject_model]
    roles: [policy_role_model]
    resources: [policy_resource_model]
    description: 'testString'
    state: present

- name: Delete ibm_iam_service_policy
  ibm_iam_service_policy:
    policy_id: 'testString'
    state: absent
'''

RETURN = r'''
id:
  description: "The policy ID."
  type: str
  returned: on success for create, update, delete operations
type:
  description: "The policy type; either 'access' or 'authorization'."
  type: str
  returned: on success for create, update operations
description:
  description: "Customer-defined description."
  type: str
  returned: on success for create, update operations
subjects:
  description: "The subjects associated with a policy."
  type: list
  elements: 'dict'
  contains:
    attributes:
      description: "List of subject attributes."
      type: list
      elements: 'dict'
      contains:
        name:
          description: "The name of an attribute."
          type: str
        value:
          description: "The value of an attribute."
          type: str
  returned: on success for create, update operations
roles:
  description: "A set of role cloud resource names (CRNs) granted by the policy."
  type: list
  elements: 'dict'
  contains:
    role_id:
      description: "The role Cloud Resource Name (CRN) granted by the policy. Example CRN:
        'crn:v1:bluemix:public:iam::::role:Editor'."
      type: str
    display_name:
      description: "The display name of the role."
      type: str
    description:
      description: "The description of the role."
      type: str
  returned: on success for create, update operations
resources:
  description: "The resources associated with a policy."
  type: list
  elements: 'dict'
  contains:
    attributes:
      description: "List of resource attributes."
      type: list
      elements: 'dict'
      contains:
        name:
          description: "The name of an attribute."
          type: str
        value:
          description: "The value of an attribute."
          type: str
        operator:
          description: "The operator of an attribute."
          type: str
    tags:
      description: "List of access management tags."
      type: list
      elements: 'dict'
      contains:
        name:
          description: "The name of an access management tag."
          type: str
        value:
          description: "The value of an access management tag."
          type: str
        operator:
          description: "The operator of an access management tag."
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
    from ibm_platform_services import IamPolicyManagementV1
except ImportError as imp_exc:
    MISSING_IMPORT_EXC = imp_exc
else:
    MISSING_IMPORT_EXC = None


def run_module():
    module_args = dict(
        subjects=dict(
            type='list',
            elements='dict',
            options=dict(
                attributes=dict(
                    type='list',
                    elements='dict',
                    options=dict(
                        name=dict(
                            type='str',
                            required=False),
                        value=dict(
                            type='str',
                            required=False),
                    ),
                    required=False),
            ),
            required=False),
        roles=dict(
            type='list',
            elements='dict',
            options=dict(
                role_id=dict(
                    type='str',
                    required=False),
                display_name=dict(
                    type='str',
                    required=False),
                description=dict(
                    type='str',
                    required=False),
            ),
            required=False),
        resources=dict(
            type='list',
            elements='dict',
            options=dict(
                attributes=dict(
                    type='list',
                    elements='dict',
                    options=dict(
                        name=dict(
                            type='str',
                            required=False),
                        value=dict(
                            type='str',
                            required=False),
                        operator=dict(
                            type='str',
                            required=False),
                    ),
                    required=False),
                tags=dict(
                    type='list',
                    elements='dict',
                    options=dict(
                        name=dict(
                            type='str',
                            required=False),
                        value=dict(
                            type='str',
                            required=False),
                        operator=dict(
                            type='str',
                            required=False),
                    ),
                    required=False),
            ),
            required=False),
        description=dict(
            type='str',
            required=False),
        type=dict(
            type='str',
            required=False),
        if_match=dict(
            type='str',
            required=False),
        policy_id=dict(
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

    subjects = module.params["subjects"]
    roles = module.params["roles"]
    resources = module.params["resources"]
    description = module.params["description"]
    type = module.params["type"]
    if_match = module.params["if_match"]
    policy_id = module.params["policy_id"]
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
    if policy_id:
        try:
            sdk.get_policy(
                policy_id=policy_id,
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
                sdk.delete_policy(
                    policy_id=policy_id,
                )
            except ApiException as ex:
                module.fail_json(msg=ex.message)
            else:
                module.exit_json(changed=True, id=policy_id, status="deleted")
        else:
            module.exit_json(changed=False, id=policy_id, status="not_found")

    if state == "present":
        if not resource_exists:
            # Create path
            try:
                response = sdk.create_policy(
                    type=type,
                    subjects=subjects,
                    roles=roles,
                    resources=resources,
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
                response = sdk.replace_policy(
                    policy_id=policy_id,
                    if_match=if_match,
                    type=type,
                    subjects=subjects,
                    roles=roles,
                    resources=resources,
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
