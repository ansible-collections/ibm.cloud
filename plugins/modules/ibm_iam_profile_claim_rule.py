#!/usr/bin/python
# coding: utf-8

# (C) Copyright IBM Corp. 2024.
#
# GNU General Public License v3.0+ (see LICENSE or https://www.gnu.org/licenses/gpl-3.0.txt)

from __future__ import (absolute_import, division, print_function)
__metaclass__ = type


DOCUMENTATION = r'''
---
module: ibm_iam_profile_claim_rule
short_description: Manage C(iam_profile_claim_rules) for IAM Identity Services.
author: Gannayak Pabra (@Gannayak0722)
version_added: "1.0.0"
description:
  - This module creates, updates, or deletes an C(iam_profile_claim_rule) resource for IAM Identity Services.
requirements:
  - "IamIdentityV1"
options:
  context:
    description: "Context with key properties for problem determination."
    type: dict
    suboptions:
      transaction_id:
        description: "The transaction ID of the inbound REST request."
        type: str
      operation:
        description: "The operation of the inbound REST request."
        type: str
      user_agent:
        description: "The user agent of the inbound REST request."
        type: str
      url:
        description: "The URL of that cluster."
        type: str
      instance_id:
        description: "The instance ID of the server instance processing the request."
        type: str
      thread_id:
        description: "The thread ID of the server instance processing the request."
        type: str
      host:
        description: "The host of the server instance processing the request."
        type: str
      start_time:
        description: "The start time of the request."
        type: str
      end_time:
        description: "The finish time of the request."
        type: str
      elapsed_time:
        description: "The elapsed time in msec."
        type: str
      cluster_name:
        description: "The cluster name."
        type: str
  name:
    description: "Name of the claim rule to be created or updated."
    type: str
  cr_type:
    description: "The compute resource type the rule applies to, required only if type is specified as
      'Profile-CR'. Valid values are VSI, IKSI(SA, ROKS)SA."
    type: str
  expiration:
    description: "Session expiration in seconds, only required if type is 'Profile-SAML'."
    type: int
  type:
    description: "Type of the claim rule, either 'Profile-SAML' or 'Profile-CR'."
    type: str
  conditions:
    description: "Conditions of this claim rule."
    type: list
    elements: 'dict'
    suboptions:
      claim:
        description: "The claim to evaluate against. [Learn
          more](/docs/account?topic=account-iam-condition-properties&interface=ui#cr-attribute-names)."
        type: str
      operator:
        description: "The operation to perform on the claim. valid values are EQUALS, NOTI(EQUALS,
          EQUALS)IGNOREI(CASE, NOT)EQUALSI(IGNORE)CASE, CONTAINS, IN."
        type: str
      value:
        description: "The stringified JSON value that the claim is compared to using the operator."
        type: str
  realm_name:
    description: "The realm name of the Idp this claim rule applies to. This field is required only if
      the type is specified as 'Profile-SAML'."
    type: str
  rule_id:
    description: "ID of the claim rule to get."
    type: str
  if_match:
    description: "Version of the claim rule to be updated. Specify the version that you retrived when
      reading list of claim rules. This value helps to identify any parallel usage of
      claim rule. Pass * to indicate to update any version available. This might result in
      stale updates."
    type: str
  profile_id:
    description: "ID of the trusted profile to create a claim rule."
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
- name: Create ibm_iam_profile_claim_rule
  vars:
    profile_claim_rule_conditions_model:
      claim: 'testString'
      operator: 'testString'
      value: 'testString'
    response_context_model:
      transaction_id: 'testString'
      operation: 'testString'
      user_agent: 'testString'
      url: 'testString'
      instance_id: 'testString'
      thread_id: 'testString'
      host: 'testString'
      start_time: 'testString'
      end_time: 'testString'
      elapsed_time: 'testString'
      cluster_name: 'testString'
  ibm_iam_profile_claim_rule:
    profile_id: 'testString'
    type: 'testString'
    conditions: [profile_claim_rule_conditions_model]
    context: '{{ response_context_model }}'
    name: 'testString'
    realm_name: 'testString'
    cr_type: 'testString'
    expiration: 38
    state: present

- name: Update ibm_iam_profile_claim_rule
  vars:
    profile_claim_rule_conditions_model:
      claim: 'testString'
      operator: 'testString'
      value: 'testString'
    response_context_model:
      transaction_id: 'testString'
      operation: 'testString'
      user_agent: 'testString'
      url: 'testString'
      instance_id: 'testString'
      thread_id: 'testString'
      host: 'testString'
      start_time: 'testString'
      end_time: 'testString'
      elapsed_time: 'testString'
      cluster_name: 'testString'
  ibm_iam_profile_claim_rule:
    profile_id: 'testString'
    rule_id: 'testString'
    if_match: 'testString'
    type: 'testString'
    conditions: [profile_claim_rule_conditions_model]
    context: '{{ response_context_model }}'
    name: 'testString'
    realm_name: 'testString'
    cr_type: 'testString'
    expiration: 38
    state: present

- name: Delete ibm_iam_profile_claim_rule
  ibm_iam_profile_claim_rule:
    profile_id: 'testString'
    rule_id: 'testString'
    state: absent
'''

RETURN = r'''
id:
  description: "the unique identifier of the claim rule."
  type: str
  returned: on success for create, update, delete operations
entity_tag:
  description: "version of the claim rule."
  type: str
  returned: on success for create, update operations
created_at:
  description: "If set contains a date time string of the creation date in ISO format."
  type: str
  returned: on success for create, update operations
modified_at:
  description: "If set contains a date time string of the last modification date in ISO format."
  type: str
  returned: on success for create, update operations
name:
  description: "The optional claim rule name."
  type: str
  returned: on success for create, update operations
type:
  description: "Type of the claim rule, either 'Profile-SAML' or 'Profile-CR'."
  type: str
  returned: on success for create, update operations
realm_name:
  description: "The realm name of the Idp this claim rule applies to."
  type: str
  returned: on success for create, update operations
expiration:
  description: "Session expiration in seconds."
  type: int
  returned: on success for create, update operations
cr_type:
  description: "The compute resource type. Not required if type is Profile-SAML. Valid values are VSI,
    IKSI(SA, ROKS)SA."
  type: str
  returned: on success for create, update operations
conditions:
  description: "Conditions of this claim rule."
  type: list
  elements: 'dict'
  contains:
    claim:
      description: "The claim to evaluate against. [Learn
        more](/docs/account?topic=account-iam-condition-properties&interface=ui#cr-attribute-names)."
      type: str
    operator:
      description: "The operation to perform on the claim. valid values are EQUALS, NOTI(EQUALS,
        EQUALS)IGNOREI(CASE, NOT)EQUALSI(IGNORE)CASE, CONTAINS, IN."
      type: str
    value:
      description: "The stringified JSON value that the claim is compared to using the operator."
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
    from ibm_platform_services import IamIdentityV1
except ImportError as imp_exc:
    MISSING_IMPORT_EXC = imp_exc
else:
    MISSING_IMPORT_EXC = None


def run_module():
    module_args = dict(
        # Represents the ResponseContext Python class
        context=dict(
            type='dict',
            options=dict(
                transaction_id=dict(
                    type='str',
                    required=False),
                operation=dict(
                    type='str',
                    required=False),
                user_agent=dict(
                    type='str',
                    required=False),
                url=dict(
                    type='str',
                    required=False),
                instance_id=dict(
                    type='str',
                    required=False),
                thread_id=dict(
                    type='str',
                    required=False),
                host=dict(
                    type='str',
                    required=False),
                start_time=dict(
                    type='str',
                    required=False),
                end_time=dict(
                    type='str',
                    required=False),
                elapsed_time=dict(
                    type='str',
                    required=False),
                cluster_name=dict(
                    type='str',
                    required=False),
            ),
            required=False),
        name=dict(
            type='str',
            required=False),
        cr_type=dict(
            type='str',
            required=False),
        expiration=dict(
            type='int',
            required=False),
        type=dict(
            type='str',
            required=False),
        conditions=dict(
            type='list',
            elements='dict',
            options=dict(
                claim=dict(
                    type='str',
                    required=False),
                operator=dict(
                    type='str',
                    required=False),
                value=dict(
                    type='str',
                    required=False),
            ),
            required=False),
        realm_name=dict(
            type='str',
            required=False),
        rule_id=dict(
            type='str',
            required=False),
        if_match=dict(
            type='str',
            required=False),
        profile_id=dict(
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

    context = module.params["context"]
    name = module.params["name"]
    cr_type = module.params["cr_type"]
    expiration = module.params["expiration"]
    type = module.params["type"]
    conditions = module.params["conditions"]
    realm_name = module.params["realm_name"]
    rule_id = module.params["rule_id"]
    if_match = module.params["if_match"]
    profile_id = module.params["profile_id"]
    state = module.params["state"]

    authenticator = get_authenticator(service_name='iam_identity')
    if authenticator is None:
        module.fail_json(msg='Cannot create the authenticator.')

    sdk = IamIdentityV1(
        authenticator=authenticator,
    )

    sdk.configure_service('iam_identity')

    resource_exists = True

    # Check for existence
    if rule_id:
        try:
            sdk.get_claim_rule(
                profile_id=profile_id,
                rule_id=rule_id,
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
                sdk.delete_claim_rule(
                    profile_id=profile_id,
                    rule_id=rule_id,
                )
            except ApiException as ex:
                module.fail_json(msg=ex.message)
            else:
                module.exit_json(changed=True, id=rule_id, status="deleted")
        else:
            module.exit_json(changed=False, id=rule_id, status="not_found")

    if state == "present":
        if not resource_exists:
            # Create path
            try:
                response = sdk.create_claim_rule(
                    profile_id=profile_id,
                    type=type,
                    conditions=conditions,
                    context=context,
                    name=name,
                    realm_name=realm_name,
                    cr_type=cr_type,
                    expiration=expiration,
                )
            except ApiException as ex:
                module.fail_json(msg=ex.message)
            else:
                result = response.get_result()

                module.exit_json(changed=True, **result)
        else:
            # Update path
            try:
                response = sdk.update_claim_rule(
                    profile_id=profile_id,
                    rule_id=rule_id,
                    if_match=if_match,
                    type=type,
                    conditions=conditions,
                    context=context,
                    name=name,
                    realm_name=realm_name,
                    cr_type=cr_type,
                    expiration=expiration,
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
