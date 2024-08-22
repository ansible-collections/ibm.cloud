#!/usr/bin/python
# coding: utf-8

# (C) Copyright IBM Corp. 2024.
#
# GNU General Public License v3.0+ (see LICENSE or https://www.gnu.org/licenses/gpl-3.0.txt)

from __future__ import (absolute_import, division, print_function)
__metaclass__ = type


DOCUMENTATION = r'''
---
module: ibm_schematics_policy_info
short_description: Manage C(schematics_policy) for Schematics Service API.
author: Gannayak Pabra (@Gannayak0722)
version_added: "1.0.0"
description:
  - This module retrieves one or more C(schematics_policy) for Schematics Service API.
requirements:
  - "SchematicsV1"
options:
  policy_id:
    description: "ID to get the details of policy."
    type: str
  profile:
    description: "Level of details returned by the get method."
    type: str
    choices:
      - "summary"
      - "detailed"
      - "ids"
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
- name: Read ibm_schematics_policy
  ibm_schematics_policy_info:
    policy_id: 'testString'
    profile: 'summary'
'''

RETURN = r'''
name:
  description: "Name of Schematics customization policy."
  type: str
  returned: on success for read operation
description:
  description: "The description of Schematics customization policy."
  type: str
  returned: on success for read operation
resource_group:
  description: "The resource group name for the policy.  By default, Policy will be created in
    C(default) Resource Group."
  type: str
  returned: on success for read operation
tags:
  description: "Tags for the Schematics customization policy."
  type: list
  elements: str
  returned: on success for read operation
location:
  description: "List of locations supported by IBM Cloud Schematics service.  While creating your
    workspace or action, choose the right region, since it cannot be changed.  Note, this
    does not limit the location of the IBM Cloud resources, provisioned using Schematics."
  type: str
  choices:
    - "us-south"
    - "us-east"
    - "eu-gb"
    - "eu-de"
  returned: on success for read operation
state:
  description: "User defined status of the Schematics object."
  type: dict
  contains:
    state:
      description: "User-defined states
          * C(draft) Object can be modified; can be used by Jobs run by the author, during
        execution
          * C(live) Object can be modified; can be used by Jobs during execution
          * C(locked) Object cannot be modified; can be used by Jobs during execution
          * C(disable) Object can be modified. cannot be used by Jobs during execution."
      type: str
      choices:
        - 'draft'
        - 'live'
        - 'locked'
        - 'disable'
    set_by:
      description: "Name of the User who set the state of the Object."
      type: str
    set_at:
      description: "When the User who set the state of the Object."
      type: str
  returned: on success for read operation
kind:
  description: "Policy kind or categories for managing and deriving policy decision
      * C(agentI(assignment)policy) Agent assignment policy for job execution."
  type: str
  choices:
    - "agent_assignment_policy"
  returned: on success for read operation
target:
  description: "The objects for the Schematics policy."
  type: dict
  contains:
    selector_kind:
      description: "Types of schematics object selector."
      type: str
      choices:
        - 'ids'
        - 'scoped'
    selector_ids:
      description: "Static selectors of schematics object ids (agent, workspace or action) for the
        Schematics policy."
      type: list
      elements: str
    selector_scope:
      description: "Selectors to dynamically list of schematics object ids (agent, workspace or action)
        for the Schematics policy."
      type: list
      elements: 'dict'
      contains:
        kind:
          description: "Name of the Schematics automation resource."
          type: str
          choices:
            - 'workspace'
            - 'action'
            - 'system'
            - 'environment'
        tags:
          description: "The tag based selector."
          type: list
          elements: str
        resource_groups:
          description: "The resource group based selector."
          type: list
          elements: str
        locations:
          description: "The location based selector."
          type: list
          elements: str
          choices:
            - "us-south"
            - "us-east"
            - "eu-gb"
            - "eu-de"
  returned: on success for read operation
parameter:
  description: "The parameter to tune the Schematics policy."
  type: dict
  contains:
    agent_assignment_policy_parameter:
      description: "Parameters for the C(agentI(assignment)policy)."
      type: dict
      contains:
        selector_kind:
          description: "Types of schematics object selector."
          type: str
          choices:
            - 'ids'
            - 'scoped'
        selector_ids:
          description: "The static selectors of schematics object ids (workspace or action) for the Schematics
            policy."
          type: list
          elements: str
        selector_scope:
          description: "The selectors to dynamically list of schematics object ids (workspace or action) for
            the Schematics policy."
          type: list
          elements: 'dict'
          contains:
            kind:
              description: "Name of the Schematics automation resource."
              type: str
              choices:
                - 'workspace'
                - 'action'
                - 'system'
                - 'environment'
            tags:
              description: "The tag based selector."
              type: list
              elements: str
            resource_groups:
              description: "The resource group based selector."
              type: list
              elements: str
            locations:
              description: "The location based selector."
              type: list
              elements: str
              choices:
                - "us-south"
                - "us-east"
                - "eu-gb"
                - "eu-de"
  returned: on success for read operation
id:
  description: "The system generated policy Id."
  type: str
  returned: on success for read operation
crn:
  description: "The policy CRN."
  type: str
  returned: on success for read operation
account:
  description: "The Account id."
  type: str
  returned: on success for read operation
scoped_resources:
  description: "List of scoped Schematics resources targeted by the policy."
  type: list
  elements: 'dict'
  contains:
    kind:
      description: "Name of the Schematics automation resource."
      type: str
      choices:
        - 'workspace'
        - 'action'
        - 'system'
        - 'environment'
    id:
      description: "Schematics resource Id."
      type: str
  returned: on success for read operation
created_at:
  description: "The policy creation time."
  type: str
  returned: on success for read operation
created_by:
  description: "The user who created the policy."
  type: str
  returned: on success for read operation
updated_at:
  description: "The policy updation time."
  type: str
  returned: on success for read operation
msg:
  description: an error message that describes what went wrong
  type: str
  returned: on error
'''


from ansible.module_utils.basic import AnsibleModule

try:
    from ..module_utils.auth import get_authenticator
    from ibm_cloud import SchematicsV1
    from ibm_cloud_sdk_core import ApiException
except ImportError as imp_exc:
    MISSING_IMPORT_EXC = imp_exc
else:
    MISSING_IMPORT_EXC = None


def run_module():
    module_args = dict(
        policy_id=dict(
            type='str',
            required=False),
        profile=dict(
            type='str',
            choices=[
                'summary',
                'detailed',
                'ids',
            ],
            required=False),
    )

    module = AnsibleModule(
        argument_spec=module_args,
        supports_check_mode=True
    )

    if MISSING_IMPORT_EXC is not None:
        module.fail_json(msg='Missing required import: ' + MISSING_IMPORT_EXC.msg)

    policy_id = module.params["policy_id"]
    profile = module.params["profile"]

    if module.check_mode:
        module.exit_json(msg='The module would run with the following parameters: ' + module.paramss)

    authenticator = get_authenticator(service_name='schematics')
    if authenticator is None:
        module.fail_json(msg='Cannot create the authenticator.')

    sdk = SchematicsV1(
        authenticator=authenticator,
    )

    sdk.configure_service('schematics')

    if policy_id:
        # read
        try:
            response = sdk.get_policy(
                policy_id=policy_id,
                profile=profile,
            )

            result = response.get_result()

            module.exit_json(**result)
        except ApiException as ex:
            module.fail_json(msg=ex.message)


def main():
    run_module()


if __name__ == '__main__':
    main()
