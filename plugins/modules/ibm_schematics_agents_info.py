#!/usr/bin/python
# coding: utf-8

# (C) Copyright IBM Corp. 2024.
#
# GNU General Public License v3.0+ (see LICENSE or https://www.gnu.org/licenses/gpl-3.0.txt)

from __future__ import (absolute_import, division, print_function)
__metaclass__ = type


DOCUMENTATION = r'''
---
module: ibm_schematics_agents_info
short_description: Manage C(schematics_agents) for Schematics Service API.
author: Gannayak Pabra (@Gannayak0722)
version_added: "1.0.0"
description:
  - This module retrieves one or more C(schematics_agents) for Schematics Service API.
requirements:
  - "SchematicsV1"
options:
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
- name: Read ibm_schematics_agents
  ibm_schematics_agents_info:
    agent_id: 'testString'
    profile: 'summary'
'''

RETURN = r'''
name:
  description: "The name of the agent (must be unique, for an account)."
  type: str
  returned: on success for read operation
description:
  description: "Agent description."
  type: str
  returned: on success for read operation
resource_group:
  description: "The resource-group name for the agent.  By default, Agent will be registered in
    Default Resource Group."
  type: str
  returned: on success for read operation
tags:
  description: "Tags for the agent."
  type: list
  elements: str
  returned: on success for read operation
agent_location:
  description: "The location where agent is deployed in the user environment."
  type: str
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
profile_id:
  description: "The IAM trusted profile id, used by the Agent instance."
  type: str
  returned: on success for read operation
agent_crn:
  description: "The Agent crn, obtained from the Schematics Agent deployment configuration."
  type: str
  returned: on success for read operation
id:
  description: "The Agent registration id."
  type: str
  returned: on success for read operation
registered_at:
  description: "The Agent registration date-time."
  type: str
  returned: on success for read operation
registered_by:
  description: "The email address of an user who registered the Agent."
  type: str
  returned: on success for read operation
updated_at:
  description: "The Agent registration updation time."
  type: str
  returned: on success for read operation
updated_by:
  description: "Email address of user who updated the Agent registration."
  type: str
  returned: on success for read operation
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
  returned: on success for read operation
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
  returned: on success for read operation
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
    )

    module = AnsibleModule(
        argument_spec=module_args,
        supports_check_mode=True
    )

    if MISSING_IMPORT_EXC is not None:
        module.fail_json(msg='Missing required import: ' + MISSING_IMPORT_EXC.msg)

    agent_id = module.params["agent_id"]
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

    if agent_id:
        # read
        try:
            response = sdk.get_agent(
                agent_id=agent_id,
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
