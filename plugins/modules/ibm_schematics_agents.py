#!/usr/bin/python
# coding: utf-8

# (C) Copyright IBM Corp. 2024.
#
# GNU General Public License v3.0+ (see LICENSE or https://www.gnu.org/licenses/gpl-3.0.txt)

from __future__ import (absolute_import, division, print_function)
__metaclass__ = type


DOCUMENTATION = r'''
---
module: ibm_schematics_agents
short_description: Manage C(schematics_agentss) for Schematics Service API.
author: Gannayak Pabra (@Gannayak0722)
version_added: "1.0.0"
description:
  - This module creates, updates, or deletes a C(schematics_agents) resource for Schematics Service API.
requirements:
  - "SchematicsV1"
options:
  resource_group:
    description: "The resource-group name for the agent.  By default, Agent will be registered in
      Default Resource Group."
    type: str
  profile_id:
    description: "The IAM trusted profile id, used by the Agent instance."
    type: str
  agent_location:
    description: "The location where agent is deployed in the user environment."
    type: str
  name:
    description: "The name of the agent (must be unique, for an account)."
    type: str
  description:
    description: "Agent description."
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
  tags:
    description: "Tags for the agent."
    type: list
    elements: str
  user_state:
    description: "User defined status of the agent."
    type: dict
    suboptions:
      state:
        description: "User-defined states
            * C(enable)  Agent is enabled by the user.
            * C(disable) Agent is disbaled by the user."
        type: str
        choices:
          - "enable"
          - "disable"
      set_by:
        description: "Name of the User who set the state of the Object."
        type: str
      set_at:
        description: "When the User who set the state of the Object."
        type: str
  agent_id:
    description: "Agent ID to get the details of agent."
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
- name: Create ibm_schematics_agents
  vars:
    agent_user_state_model:
      state: 'enable'
  ibm_schematics_agents:
    name: 'MyDevAgent'
    agent_location: 'us-south'
    location: 'us-south'
    profile_id: 'testString'
    description: 'Register agent'
    resource_group: 'testString'
    tags: ['testString']
    user_state: '{{ agent_user_state_model }}'
    state: present

- name: Update ibm_schematics_agents
  vars:
    agent_user_state_model:
      state: 'enable'
  ibm_schematics_agents:
    agent_id: 'testString'
    name: 'MyDevAgent'
    agent_location: 'us-south'
    location: 'us-south'
    profile_id: 'testString'
    description: 'Register agent'
    resource_group: 'testString'
    tags: ['testString']
    user_state: '{{ agent_user_state_model }}'
    state: present

- name: Delete ibm_schematics_agents
  ibm_schematics_agents:
    agent_id: 'testString'
    state: absent
'''

RETURN = r'''
name:
  description: "The name of the agent (must be unique, for an account)."
  type: str
  returned: on success for create, update operations
description:
  description: "Agent description."
  type: str
  returned: on success for create, update operations
resource_group:
  description: "The resource-group name for the agent.  By default, Agent will be registered in
    Default Resource Group."
  type: str
  returned: on success for create, update operations
tags:
  description: "Tags for the agent."
  type: list
  elements: str
  returned: on success for create, update operations
agent_location:
  description: "The location where agent is deployed in the user environment."
  type: str
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
profile_id:
  description: "The IAM trusted profile id, used by the Agent instance."
  type: str
  returned: on success for create, update operations
agent_crn:
  description: "The Agent crn, obtained from the Schematics Agent deployment configuration."
  type: str
  returned: on success for create, update operations
id:
  description: "The Agent registration id."
  type: str
  returned: on success for create, update, delete operations
registered_at:
  description: "The Agent registration date-time."
  type: str
  returned: on success for create, update operations
registered_by:
  description: "The email address of an user who registered the Agent."
  type: str
  returned: on success for create, update operations
updated_at:
  description: "The Agent registration updation time."
  type: str
  returned: on success for create, update operations
updated_by:
  description: "Email address of user who updated the Agent registration."
  type: str
  returned: on success for create, update operations
user_state:
  description: "User defined status of the agent."
  type: dict
  contains:
    state:
      description: "User-defined states
          * C(enable)  Agent is enabled by the user.
          * C(disable) Agent is disbaled by the user."
      type: str
      choices:
        - 'enable'
        - 'disable'
    set_by:
      description: "Name of the User who set the state of the Object."
      type: str
    set_at:
      description: "When the User who set the state of the Object."
      type: str
  returned: on success for create, update operations
connection_state:
  description: "Connection status of the agent."
  type: dict
  contains:
    state:
      description: "Agent Connection Status
          * C(Connected) When Schematics is able to connect to the agent.
          * C(Disconnected) When Schematics is able not connect to the agent."
      type: str
      choices:
        - 'Connected'
        - 'Disconnected'
    checked_at:
      description: "When the connection state is modified."
      type: str
  returned: on success for create, update operations
system_state:
  description: "Computed state of the agent."
  type: dict
  contains:
    state:
      description: "Agent Status."
      type: str
      choices:
        - 'error'
        - 'normal'
        - 'in_progress'
        - 'pending'
        - 'draft'
    message_:
      description: "The Agent status message."
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
        resource_group=dict(
            type='str',
            required=False),
        profile_id=dict(
            type='str',
            required=False),
        agent_location=dict(
            type='str',
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
        tags=dict(
            type='list',
            elements='str',
            required=False),
        # Represents the AgentUserState Python class
        user_state=dict(
            type='dict',
            options=dict(
                state=dict(
                    type='str',
                    choices=[
                        'enable',
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
        agent_id=dict(
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

    resource_group = module.params["resource_group"]
    profile_id = module.params["profile_id"]
    agent_location = module.params["agent_location"]
    name = module.params["name"]
    description = module.params["description"]
    location = module.params["location"]
    tags = module.params["tags"]
    user_state = module.params["user_state"]
    agent_id = module.params["agent_id"]
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
    if agent_id:
        try:
            sdk.get_agent(
                agent_id=agent_id,
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
                sdk.delete_agent(
                    agent_id=agent_id,
                )
            except ApiException as ex:
                module.fail_json(msg=ex.message)
            else:
                module.exit_json(changed=True, id=agent_id, status="deleted")
        else:
            module.exit_json(changed=False, id=agent_id, status="not_found")

    if state == "present":
        if not resource_exists:
            # Create path
            try:
                response = sdk.register_agent(
                    name=name,
                    agent_location=agent_location,
                    location=location,
                    profile_id=profile_id,
                    description=description,
                    resource_group=resource_group,
                    tags=tags,
                    user_state=user_state,
                )
            except ApiException as ex:
                module.fail_json(msg=ex.message)
            else:
                result = response.get_result()

                module.exit_json(changed=True, **result)
        else:
            # Update path
            try:
                response = sdk.update_agent_registration(
                    agent_id=agent_id,
                    name=name,
                    agent_location=agent_location,
                    location=location,
                    profile_id=profile_id,
                    description=description,
                    resource_group=resource_group,
                    tags=tags,
                    user_state=user_state,
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
