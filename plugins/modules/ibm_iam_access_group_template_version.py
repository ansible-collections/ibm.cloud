#!/usr/bin/python
# coding: utf-8

# (C) Copyright IBM Corp. 2024.
#
# GNU General Public License v3.0+ (see LICENSE or https://www.gnu.org/licenses/gpl-3.0.txt)

from __future__ import (absolute_import, division, print_function)
__metaclass__ = type


DOCUMENTATION = r'''
---
module: ibm_iam_access_group_template_version
short_description: Manage C(iam_access_group_template_versions) for IAM Access Groups.
author: Gannayak Pabra (@Gannayak0722)
version_added: "1.0.0"
description:
  - This module creates, updates, or deletes an C(iam_access_group_template_version) resource for IAM Access Groups.
requirements:
  - "IamAccessGroupsV2"
options:
  name:
    description: "This is an optional field. If the field is included it will change the name value
      for all existing versions of the template.."
    type: str
  description:
    description: "Assign an optional description for the access group template version."
    type: str
  policy_template_references:
    description: "The policy templates associated with the template version."
    type: list
    elements: 'dict'
    suboptions:
      id:
        description: "Policy template ID."
        type: str
      version:
        description: "Policy template version."
        type: str
  group:
    description: "Access Group Component."
    type: dict
    suboptions:
      name:
        description: "Give the access group a unique name that doesn't conflict with other templates access
          group name in the given account. This is shown in child accounts."
        type: str
      description:
        description: "Access group description. This is shown in child accounts."
        type: str
      members:
        description: "Array of enterprise users to add to the template. All enterprise users that you add to
          the template must be invited to the child accounts where the template is assigned."
        type: dict
        suboptions:
          users:
            description: "Array of enterprise users to add to the template. All enterprise users that you add to
              the template must be invited to the child accounts where the template is assigned."
            type: list
            elements: str
          services:
            description: "Array of service IDs to add to the template."
            type: list
            elements: str
          action_controls:
            description: "Control whether or not access group administrators in child accounts can add and
              remove members from the enterprise-managed access group in their account."
            type: dict
            suboptions:
              add:
                description: "Action control for adding child account members to an enterprise-managed access group.
                  If an access group administrator in a child account adds a member, they can always
                  remove them. Note that if conflicts arise between an update to this control in a new
                  version and members added by an administrator in the child account, you must resolve
                  those conflicts in the child account. This prevents breaking access in the child
                  account. For more information, see [Working with versions]
                  (https://cloud.ibm.com/docs/secure-enterprise?topic=secure-enterprise-working-with-versions#new-version-scenarios)."
                type: bool
              remove:
                description: "Action control for removing enterprise-managed members from an enterprise-managed
                  access group. Note that if an enterprise member is removed from an enterprise-managed
                  access group in a child account and you reassign the template, the membership is
                  reinstated."
                type: bool
      assertions:
        description: "Assertions Input Component."
        type: dict
        suboptions:
          rules:
            description: "Dynamic rules to automatically add federated users to access groups based on specific
              identity attributes."
            type: list
            elements: 'dict'
            suboptions:
              name:
                description: "Dynamic rule name."
                type: str
              expiration:
                description: "Session duration in hours. Access group membership is revoked after this time period
                  expires. Users must log back in to refresh their access group membership."
                type: int
              realm_name:
                description: "The identity provider (IdP) URL."
                type: str
              conditions:
                description: "Conditions of membership. You can think of this as a key:value pair."
                type: list
                elements: 'dict'
                suboptions:
                  claim:
                    description: "The key in the key:value pair."
                    type: str
                  operator:
                    description: "Compares the claim and the value."
                    type: str
                  value:
                    description: "The value in the key:value pair."
                    type: str
              action_controls:
                description: "Control whether or not access group administrators in child accounts can update and
                  remove this dynamic rule in the enterprise-managed access group in their account.This
                  overrides outer level AssertionsActionControls."
                type: dict
                suboptions:
                  remove:
                    description: "Action control for removing this enterprise-managed dynamic rule."
                    type: bool
          action_controls:
            description: "Control whether or not access group administrators in child accounts can add, remove,
              and update dynamic rules for the enterprise-managed access group in their account. The
              inner level RuleActionControls override these C(remove) and C(update) action controls."
            type: dict
            suboptions:
              add:
                description: "Action control for adding dynamic rules to an enterprise-managed access group. If an
                  access group administrator in a child account adds a dynamic rule, they can always
                  update or remove it. Note that if conflicts arise between an update to this control
                  and rules added or updated by an administrator in the child account, you must resolve
                  those conflicts in the child account. This prevents breaking access that the rules
                  might grant in the child account. For more information, see [Working with versions]."
                type: bool
              remove:
                description: "Action control for removing enterprise-managed dynamic rules in an enterprise-managed
                  access group. Note that if a rule is removed from an enterprise-managed access group
                  by an administrator in a child account and and you reassign the template, the rule is
                  reinstated."
                type: bool
      action_controls:
        description: "Access group action controls component."
        type: dict
        suboptions:
          access:
            description: "Control whether or not access group administrators in child accounts can add access
              policies to the enterprise-managed access group in their account."
            type: dict
            suboptions:
              add:
                description: "Action control for adding access policies to an enterprise-managed access group in a
                  child account. If an access group administrator in a child account adds a policy, they
                  can always update or remove it. Note that if conflicts arise between an update to this
                  control in a new version and polices added to the access group by an administrator in
                  a child account, you must resolve those conflicts in the child account. This prevents
                  breaking access in the child account. For more information, see [Working with
                  versions](https://cloud.ibm.com/docs/secure-enterprise?topic=secure-enterprise-working-with-versions#new-version-scenarios)."
                type: bool
  if_match:
    description: "ETag value of the template version document."
    type: str
  transaction_id:
    description: "An optional transaction id for the request."
    type: str
  version_num:
    description: "Version number."
    type: str
  template_id:
    description: "ID of the template that you want to create a new version of."
    type: str
  verbose:
    description: "If C(verbose=true), IAM resource details are returned. If performance is a concern,
      leave the C(verbose) parameter off so that details are not retrieved."
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
- name: Create ibm_iam_access_group_template_version
  vars:
    members_action_controls_model:
      add: True
      remove: False
    members_model:
      users: ['IBMid-50PJGPKYJJ', 'IBMid-665000T8WY']
      services: ['iam-ServiceId-345']
      action_controls: members_action_controls_model
    conditions_model:
      claim: 'blueGroup'
      operator: 'CONTAINS'
      value: 'test-bluegroup-saml'
    rule_action_controls_model:
      remove: False
    assertions_rule_model:
      name: 'Manager group rule'
      expiration: 12
      realm_name: 'https://idp.example.org/SAML2'
      conditions: [conditions_model]
      action_controls: rule_action_controls_model
    assertions_action_controls_model:
      add: False
      remove: True
    assertions_model:
      rules: [assertions_rule_model]
      action_controls: assertions_action_controls_model
    access_action_controls_model:
      add: False
    group_action_controls_model:
      access: access_action_controls_model
    access_group_request_model:
      name: 'IAM Admin Group 8'
      description: 'This access group template allows admin access to all IAM platform services in the account.'
      members: members_model
      assertions: assertions_model
      action_controls: group_action_controls_model
    policy_templates_model:
      id: 'policyTemplateId-123'
      version: '1'
  ibm_iam_access_group_template_version:
    template_id: 'testString'
    name: 'IAM Admin Group template 2'
    description: "This access group template allows admin access to all IAM platform services in the acco\
      unt."
    group: '{{ access_group_request_model }}'
    policy_template_references: [policy_templates_model]
    transaction_id: 'testString'
    state: present

- name: Update ibm_iam_access_group_template_version
  vars:
    members_action_controls_model:
      add: True
      remove: False
    members_model:
      users: ['IBMid-665000T8WY']
      services: ['iam-ServiceId-e371b0e5-1c80-48e3-bf12-c6a8ef2b1a11']
      action_controls: members_action_controls_model
    conditions_model:
      claim: 'blueGroup'
      operator: 'CONTAINS'
      value: 'test-bluegroup-saml'
    rule_action_controls_model:
      remove: False
    assertions_rule_model:
      name: 'Manager group rule'
      expiration: 12
      realm_name: 'https://idp.example.org/SAML2'
      conditions: [conditions_model]
      action_controls: rule_action_controls_model
    assertions_action_controls_model:
      add: False
      remove: True
    assertions_model:
      rules: [assertions_rule_model]
      action_controls: assertions_action_controls_model
    access_action_controls_model:
      add: False
    group_action_controls_model:
      access: access_action_controls_model
    access_group_request_model:
      name: 'IAM Admin Group 8'
      description: 'This access group template allows admin access to all IAM platform services in the account.'
      members: members_model
      assertions: assertions_model
      action_controls: group_action_controls_model
    policy_templates_model:
      id: 'policyTemplateId-123'
      version: '1'
  ibm_iam_access_group_template_version:
    template_id: 'testString'
    version_num: 'testString'
    if_match: 'testString'
    name: 'IAM Admin Group template 2'
    description: "This access group template allows admin access to all IAM platform services in the acco\
      unt."
    group: '{{ access_group_request_model }}'
    policy_template_references: [policy_templates_model]
    transaction_id: '83adf5bd-de790caa3'
    state: present

- name: Delete ibm_iam_access_group_template_version
  ibm_iam_access_group_template_version:
    template_id: 'testString'
    version_num: 'testString'
    transaction_id: 'testString'
    state: absent
'''

RETURN = r'''
id:
  description: "The ID of the access group template."
  type: str
  returned: on success for create, update, delete operations
name:
  description: "The name of the access group template."
  type: str
  returned: on success for create, update operations
description:
  description: "The description of the access group template."
  type: str
  returned: on success for create, update operations
account_id:
  description: "The ID of the account to which the access group template is assigned."
  type: str
  returned: on success for create, update operations
version:
  description: "The version of the access group template."
  type: str
  returned: on success for create, update operations
committed:
  description: "A boolean indicating whether the access group template is committed. You must commit a
    template before you can assign it to child accounts."
  type: bool
  returned: on success for create, update operations
group:
  description: "Access Group Component."
  type: dict
  contains:
    name:
      description: "Give the access group a unique name that doesn't conflict with other templates access
        group name in the given account. This is shown in child accounts."
      type: str
    description:
      description: "Access group description. This is shown in child accounts."
      type: str
    members:
      description: "Array of enterprise users to add to the template. All enterprise users that you add to
        the template must be invited to the child accounts where the template is assigned."
      type: dict
      contains:
        users:
          description: "Array of enterprise users to add to the template. All enterprise users that you add to
            the template must be invited to the child accounts where the template is assigned."
          type: list
          elements: str
        services:
          description: "Array of service IDs to add to the template."
          type: list
          elements: str
        action_controls:
          description: "Control whether or not access group administrators in child accounts can add and
            remove members from the enterprise-managed access group in their account."
          type: dict
          contains:
            add:
              description: "Action control for adding child account members to an enterprise-managed access group.
                If an access group administrator in a child account adds a member, they can always
                remove them. Note that if conflicts arise between an update to this control in a new
                version and members added by an administrator in the child account, you must resolve
                those conflicts in the child account. This prevents breaking access in the child
                account. For more information, see [Working with versions]
                (https://cloud.ibm.com/docs/secure-enterprise?topic=secure-enterprise-working-with-versions#new-version-scenarios)."
              type: bool
            remove:
              description: "Action control for removing enterprise-managed members from an enterprise-managed
                access group. Note that if an enterprise member is removed from an enterprise-managed
                access group in a child account and you reassign the template, the membership is
                reinstated."
              type: bool
    assertions:
      description: "Assertions Input Component."
      type: dict
      contains:
        rules:
          description: "Dynamic rules to automatically add federated users to access groups based on specific
            identity attributes."
          type: list
          elements: 'dict'
          contains:
            name:
              description: "Dynamic rule name."
              type: str
            expiration:
              description: "Session duration in hours. Access group membership is revoked after this time period
                expires. Users must log back in to refresh their access group membership."
              type: int
            realm_name:
              description: "The identity provider (IdP) URL."
              type: str
            conditions:
              description: "Conditions of membership. You can think of this as a key:value pair."
              type: list
              elements: 'dict'
              contains:
                claim:
                  description: "The key in the key:value pair."
                  type: str
                operator:
                  description: "Compares the claim and the value."
                  type: str
                value:
                  description: "The value in the key:value pair."
                  type: str
            action_controls:
              description: "Control whether or not access group administrators in child accounts can update and
                remove this dynamic rule in the enterprise-managed access group in their account.This
                overrides outer level AssertionsActionControls."
              type: dict
              contains:
                remove:
                  description: "Action control for removing this enterprise-managed dynamic rule."
                  type: bool
        action_controls:
          description: "Control whether or not access group administrators in child accounts can add, remove,
            and update dynamic rules for the enterprise-managed access group in their account. The
            inner level RuleActionControls override these C(remove) and C(update) action controls."
          type: dict
          contains:
            add:
              description: "Action control for adding dynamic rules to an enterprise-managed access group. If an
                access group administrator in a child account adds a dynamic rule, they can always
                update or remove it. Note that if conflicts arise between an update to this control
                and rules added or updated by an administrator in the child account, you must resolve
                those conflicts in the child account. This prevents breaking access that the rules
                might grant in the child account. For more information, see [Working with versions]."
              type: bool
            remove:
              description: "Action control for removing enterprise-managed dynamic rules in an enterprise-managed
                access group. Note that if a rule is removed from an enterprise-managed access group
                by an administrator in a child account and and you reassign the template, the rule is
                reinstated."
              type: bool
    action_controls:
      description: "Access group action controls component."
      type: dict
      contains:
        access:
          description: "Control whether or not access group administrators in child accounts can add access
            policies to the enterprise-managed access group in their account."
          type: dict
          contains:
            add:
              description: "Action control for adding access policies to an enterprise-managed access group in a
                child account. If an access group administrator in a child account adds a policy, they
                can always update or remove it. Note that if conflicts arise between an update to this
                control in a new version and polices added to the access group by an administrator in
                a child account, you must resolve those conflicts in the child account. This prevents
                breaking access in the child account. For more information, see [Working with
                versions](https://cloud.ibm.com/docs/secure-enterprise?topic=secure-enterprise-working-with-versions#new-version-scenarios)."
              type: bool
  returned: on success for create, update operations
policy_template_references:
  description: "References to policy templates assigned to the access group template."
  type: list
  elements: 'dict'
  contains:
    id:
      description: "Policy template ID."
      type: str
    version:
      description: "Policy template version."
      type: str
  returned: on success for create, update operations
href:
  description: "The URL of the access group template resource."
  type: str
  returned: on success for create, update operations
created_at:
  description: "The date and time when the access group template was created."
  type: str
  returned: on success for create, update operations
created_by_id:
  description: "The ID of the user who created the access group template."
  type: str
  returned: on success for create, update operations
last_modified_at:
  description: "The date and time when the access group template was last modified."
  type: str
  returned: on success for create, update operations
last_modified_by_id:
  description: "The ID of the user who last modified the access group template."
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
        name=dict(
            type='str',
            required=False),
        description=dict(
            type='str',
            required=False),
        policy_template_references=dict(
            type='list',
            elements='dict',
            options=dict(
                id=dict(
                    type='str',
                    required=False),
                version=dict(
                    type='str',
                    required=False),
            ),
            required=False),
        # Represents the AccessGroupRequest Python class
        group=dict(
            type='dict',
            options=dict(
                name=dict(
                    type='str',
                    required=False),
                description=dict(
                    type='str',
                    required=False),
                members=dict(
                    type='dict',
                    options=dict(
                        users=dict(
                            type='list',
                            elements='str',
                            required=False),
                        services=dict(
                            type='list',
                            elements='str',
                            required=False),
                        action_controls=dict(
                            type='dict',
                            options=dict(
                                add=dict(
                                    type='bool',
                                    required=False),
                                remove=dict(
                                    type='bool',
                                    required=False),
                            ),
                            required=False),
                    ),
                    required=False),
                assertions=dict(
                    type='dict',
                    options=dict(
                        rules=dict(
                            type='list',
                            elements='dict',
                            options=dict(
                                name=dict(
                                    type='str',
                                    required=False),
                                expiration=dict(
                                    type='int',
                                    required=False),
                                realm_name=dict(
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
                                action_controls=dict(
                                    type='dict',
                                    options=dict(
                                        remove=dict(
                                            type='bool',
                                            required=False),
                                    ),
                                    required=False),
                            ),
                            required=False),
                        action_controls=dict(
                            type='dict',
                            options=dict(
                                add=dict(
                                    type='bool',
                                    required=False),
                                remove=dict(
                                    type='bool',
                                    required=False),
                            ),
                            required=False),
                    ),
                    required=False),
                action_controls=dict(
                    type='dict',
                    options=dict(
                        access=dict(
                            type='dict',
                            options=dict(
                                add=dict(
                                    type='bool',
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
        transaction_id=dict(
            type='str',
            required=False),
        version_num=dict(
            type='str',
            required=False),
        template_id=dict(
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

    name = module.params["name"]
    description = module.params["description"]
    policy_template_references = module.params["policy_template_references"]
    group = module.params["group"]
    if_match = module.params["if_match"]
    transaction_id = module.params["transaction_id"]
    version_num = module.params["version_num"]
    template_id = module.params["template_id"]
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
    if version_num:
        try:
            sdk.get_template_version(
                template_id=template_id,
                version_num=version_num,
                verbose=verbose,
                transaction_id=transaction_id,
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
                sdk.delete_template_version(
                    template_id=template_id,
                    version_num=version_num,
                    transaction_id=transaction_id,
                )
            except ApiException as ex:
                module.fail_json(msg=ex.message)
            else:
                module.exit_json(changed=True, id=version_num, status="deleted")
        else:
            module.exit_json(changed=False, id=version_num, status="not_found")

    if state == "present":
        if not resource_exists:
            # Create path
            try:
                response = sdk.create_template_version(
                    template_id=template_id,
                    name=name,
                    description=description,
                    group=group,
                    policy_template_references=policy_template_references,
                    transaction_id=transaction_id,
                )
            except ApiException as ex:
                module.fail_json(msg=ex.message)
            else:
                result = response.get_result()

                module.exit_json(changed=True, **result)
        else:
            # Update path
            try:
                response = sdk.update_template_version(
                    template_id=template_id,
                    version_num=version_num,
                    if_match=if_match,
                    name=name,
                    description=description,
                    group=group,
                    policy_template_references=policy_template_references,
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
