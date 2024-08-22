#!/usr/bin/python
# coding: utf-8

# (C) Copyright IBM Corp. 2024.
#
# GNU General Public License v3.0+ (see LICENSE or https://www.gnu.org/licenses/gpl-3.0.txt)

from __future__ import (absolute_import, division, print_function)
__metaclass__ = type


DOCUMENTATION = r'''
---
module: ibm_schematics_policy
short_description: Manage C(schematics_policys) for Schematics Service API.
author: Gannayak Pabra (@Gannayak0722)
version_added: "1.0.0"
description:
  - This module creates, updates, or deletes a C(schematics_policy) resource for Schematics Service API.
requirements:
  - "SchematicsV1"
options:
  scoped_resources:
    description: "List of scoped Schematics resources targeted by the policy."
    type: list
    elements: 'dict'
    suboptions:
      kind:
        description: "Name of the Schematics automation resource."
        type: str
        choices:
          - "workspace"
          - "action"
          - "system"
          - "environment"
      id:
        description: "Schematics resource Id."
        type: str
  resource_group:
    description: "The resource group name for the policy.  By default, Policy will be created in
      C(default) Resource Group."
    type: str
  kind:
    description: "Policy kind or categories for managing and deriving policy decision
        * C(agentI(assignment)policy) Agent assignment policy for job execution."
    type: str
    choices:
      - "agent_assignment_policy"
  parameter:
    description: "The parameter to tune the Schematics policy."
    type: dict
    suboptions:
      agent_assignment_policy_parameter:
        description: "Parameters for the C(agentI(assignment)policy)."
        type: dict
        suboptions:
          selector_kind:
            description: "Types of schematics object selector."
            type: str
            choices:
              - "ids"
              - "scoped"
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
            suboptions:
              kind:
                description: "Name of the Schematics automation resource."
                type: str
                choices:
                  - "workspace"
                  - "action"
                  - "system"
                  - "environment"
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
  name:
    description: "Name of Schematics customization policy."
    type: str
  description:
    description: "The description of Schematics customization policy."
    type: str
  location:
    description: "List of locations supported by IBM Cloud Schematics service.  While creating your
      workspace or action, choose the right region, since it cannot be changed.  Note,
      this does not limit the location of the IBM Cloud resources, provisioned using
      Schematics."
    type: str
    choices:
      - "us-south"
      - "us-east"
      - "eu-gb"
      - "eu-de"
  schematics_policy_state:
    description: "User defined status of the Schematics object."
    type: dict
    suboptions:
      state:
        description: "User-defined states
            * C(draft) Object can be modified; can be used by Jobs run by the author, during
          execution
            * C(live) Object can be modified; can be used by Jobs during execution
            * C(locked) Object cannot be modified; can be used by Jobs during execution
            * C(disable) Object can be modified. cannot be used by Jobs during execution."
        type: str
        choices:
          - "draft"
          - "live"
          - "locked"
          - "disable"
      set_by:
        description: "Name of the User who set the state of the Object."
        type: str
      set_at:
        description: "When the User who set the state of the Object."
        type: str
  tags:
    description: "Tags for the Schematics customization policy."
    type: list
    elements: str
  target:
    description: "The objects for the Schematics policy."
    type: dict
    suboptions:
      selector_kind:
        description: "Types of schematics object selector."
        type: str
        choices:
          - "ids"
          - "scoped"
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
        suboptions:
          kind:
            description: "Name of the Schematics automation resource."
            type: str
            choices:
              - "workspace"
              - "action"
              - "system"
              - "environment"
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
- name: Create ibm_schematics_policy
  vars:
    user_state_model:
      state: 'draft'
      set_by: 'testString'
      set_at: '2019-01-01T12:00:00.000Z'
    policy_object_selector_model:
      kind: 'workspace'
      tags: ['testString']
      resource_groups: ['testString']
      locations: ['us-south']
    policy_objects_model:
      selector_kind: 'ids'
      selector_ids: ['testString']
      selector_scope: [policy_object_selector_model]
    agent_assignment_policy_parameter_model:
      selector_kind: 'ids'
      selector_ids: ['testString']
      selector_scope: [policy_object_selector_model]
    policy_parameter_model:
      agent_assignment_policy_parameter: agent_assignment_policy_parameter_model
    scoped_resource_model:
      kind: 'workspace'
      id: 'testString'
  ibm_schematics_policy:
    name: 'Agent1-DevWS'
    description: 'Policy for job execution of secured workspaces on agent1'
    resource_group: 'Default'
    tags: ['policy:secured-job']
    location: 'us-south'
    schematics_policy_state: '{{ user_state_model }}'
    kind: 'agent_assignment_policy'
    target: '{{ policy_objects_model }}'
    parameter: '{{ policy_parameter_model }}'
    scoped_resources: [scoped_resource_model]
    state: present

- name: Update ibm_schematics_policy
  vars:
    user_state_model:
      state: 'draft'
      set_by: 'testString'
      set_at: '2019-01-01T12:00:00.000Z'
    policy_object_selector_model:
      kind: 'workspace'
      tags: ['testString']
      resource_groups: ['testString']
      locations: ['us-south']
    policy_objects_model:
      selector_kind: 'ids'
      selector_ids: ['testString']
      selector_scope: [policy_object_selector_model]
    agent_assignment_policy_parameter_model:
      selector_kind: 'ids'
      selector_ids: ['testString']
      selector_scope: [policy_object_selector_model]
    policy_parameter_model:
      agent_assignment_policy_parameter: agent_assignment_policy_parameter_model
    scoped_resource_model:
      kind: 'workspace'
      id: 'testString'
  ibm_schematics_policy:
    policy_id: 'testString'
    name: 'Agent1-DevWS'
    description: 'Policy for job execution of secured workspaces on agent1'
    resource_group: 'Default'
    tags: ['policy:secured-job']
    location: 'us-south'
    schematics_policy_state: '{{ user_state_model }}'
    kind: 'agent_assignment_policy'
    target: '{{ policy_objects_model }}'
    parameter: '{{ policy_parameter_model }}'
    scoped_resources: [scoped_resource_model]
    state: present

- name: Delete ibm_schematics_policy
  ibm_schematics_policy:
    policy_id: 'testString'
    state: absent
'''

RETURN = r'''
name:
  description: "Name of Schematics customization policy."
  type: str
  returned: on success for create, update operations
description:
  description: "The description of Schematics customization policy."
  type: str
  returned: on success for create, update operations
resource_group:
  description: "The resource group name for the policy.  By default, Policy will be created in
    C(default) Resource Group."
  type: str
  returned: on success for create, update operations
tags:
  description: "Tags for the Schematics customization policy."
  type: list
  elements: str
  returned: on success for create, update operations
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
  returned: on success for create, update operations
schematics_policy_state:
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
  returned: on success for create, update operations
kind:
  description: "Policy kind or categories for managing and deriving policy decision
      * C(agentI(assignment)policy) Agent assignment policy for job execution."
  type: str
  choices:
    - "agent_assignment_policy"
  returned: on success for create, update operations
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
  returned: on success for create, update operations
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
  returned: on success for create, update operations
id:
  description: "The system generated policy Id."
  type: str
  returned: on success for create, update, delete operations
crn:
  description: "The policy CRN."
  type: str
  returned: on success for create, update operations
account:
  description: "The Account id."
  type: str
  returned: on success for create, update operations
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
  returned: on success for create, update operations
created_at:
  description: "The policy creation time."
  type: str
  returned: on success for create, update operations
created_by:
  description: "The user who created the policy."
  type: str
  returned: on success for create, update operations
updated_at:
  description: "The policy updation time."
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
    from ibm_cloud import SchematicsV1
    from ibm_cloud_sdk_core import ApiException
except ImportError as imp_exc:
    MISSING_IMPORT_EXC = imp_exc
else:
    MISSING_IMPORT_EXC = None


def run_module():
    module_args = dict(
        scoped_resources=dict(
            type='list',
            elements='dict',
            options=dict(
                kind=dict(
                    type='str',
                    choices=[
                        'workspace',
                        'action',
                        'system',
                        'environment',
                    ],
                    required=False),
                id=dict(
                    type='str',
                    required=False),
            ),
            required=False),
        resource_group=dict(
            type='str',
            required=False),
        kind=dict(
            type='str',
            choices=[
                'agent_assignment_policy',
            ],
            required=False),
        # Represents the PolicyParameter Python class
        parameter=dict(
            type='dict',
            options=dict(
                agent_assignment_policy_parameter=dict(
                    type='dict',
                    options=dict(
                        selector_kind=dict(
                            type='str',
                            choices=[
                                'ids',
                                'scoped',
                            ],
                            required=False),
                        selector_ids=dict(
                            type='list',
                            elements='str',
                            required=False),
                        selector_scope=dict(
                            type='list',
                            elements='dict',
                            options=dict(
                                kind=dict(
                                    type='str',
                                    choices=[
                                        'workspace',
                                        'action',
                                        'system',
                                        'environment',
                                    ],
                                    required=False),
                                tags=dict(
                                    type='list',
                                    elements='str',
                                    required=False),
                                resource_groups=dict(
                                    type='list',
                                    elements='str',
                                    required=False),
                                locations=dict(
                                    type='list',
                                    elements='str',
                                    choices=[
                                        'us-south',
                                        'us-east',
                                        'eu-gb',
                                        'eu-de',
                                    ],
                                    required=False),
                            ),
                            required=False),
                    ),
                    required=False),
            ),
            required=False),
        name=dict(
            type='str',
            required=False),
        description=dict(
            type='str',
            required=False),
        location=dict(
            type='str',
            choices=[
                'us-south',
                'us-east',
                'eu-gb',
                'eu-de',
            ],
            required=False),
        # Represents the UserState Python class
        schematics_policy_state=dict(
            type='dict',
            options=dict(
                state=dict(
                    type='str',
                    choices=[
                        'draft',
                        'live',
                        'locked',
                        'disable',
                    ],
                    required=False),
                set_by=dict(
                    type='str',
                    required=False),
                set_at=dict(
                    type='str',
                    required=False),
            ),
            required=False),
        tags=dict(
            type='list',
            elements='str',
            required=False),
        # Represents the PolicyObjects Python class
        target=dict(
            type='dict',
            options=dict(
                selector_kind=dict(
                    type='str',
                    choices=[
                        'ids',
                        'scoped',
                    ],
                    required=False),
                selector_ids=dict(
                    type='list',
                    elements='str',
                    required=False),
                selector_scope=dict(
                    type='list',
                    elements='dict',
                    options=dict(
                        kind=dict(
                            type='str',
                            choices=[
                                'workspace',
                                'action',
                                'system',
                                'environment',
                            ],
                            required=False),
                        tags=dict(
                            type='list',
                            elements='str',
                            required=False),
                        resource_groups=dict(
                            type='list',
                            elements='str',
                            required=False),
                        locations=dict(
                            type='list',
                            elements='str',
                            choices=[
                                'us-south',
                                'us-east',
                                'eu-gb',
                                'eu-de',
                            ],
                            required=False),
                    ),
                    required=False),
            ),
            required=False),
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

    scoped_resources = module.params["scoped_resources"]
    resource_group = module.params["resource_group"]
    kind = module.params["kind"]
    parameter = module.params["parameter"]
    name = module.params["name"]
    description = module.params["description"]
    location = module.params["location"]
    schematics_policy_state = module.params["schematics_policy_state"]
    tags = module.params["tags"]
    target = module.params["target"]
    policy_id = module.params["policy_id"]
    profile = module.params["profile"]
    state = module.params["state"]

    authenticator = get_authenticator(service_name='schematics')
    if authenticator is None:
        module.fail_json(msg='Cannot create the authenticator.')

    sdk = SchematicsV1(
        authenticator=authenticator,
    )

    sdk.configure_service('schematics')

    resource_exists = True

    # Check for existence
    if policy_id:
        try:
            sdk.get_policy(
                policy_id=policy_id,
                profile=profile,
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
                    name=name,
                    description=description,
                    resource_group=resource_group,
                    tags=tags,
                    location=location,
                    state=schematics_policy_state,
                    kind=kind,
                    target=target,
                    parameter=parameter,
                    scoped_resources=scoped_resources,
                )
            except ApiException as ex:
                module.fail_json(msg=ex.message)
            else:
                result = response.get_result()
                if 'state' in result:
                    result['schematics_policy_state'] = result['state']
                    del result['state']

                module.exit_json(changed=True, **result)
        else:
            # Update path
            try:
                response = sdk.update_policy(
                    policy_id=policy_id,
                    name=name,
                    description=description,
                    resource_group=resource_group,
                    tags=tags,
                    location=location,
                    state=schematics_policy_state,
                    kind=kind,
                    target=target,
                    parameter=parameter,
                    scoped_resources=scoped_resources,
                )
            except ApiException as ex:
                module.fail_json(msg=ex.message)
            else:
                result = response.get_result()
                if 'state' in result:
                    result['schematics_policy_state'] = result['state']
                    del result['state']

                module.exit_json(changed=True, **result)


def main():
    run_module()


if __name__ == '__main__':
    main()
