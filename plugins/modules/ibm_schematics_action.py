# coding: utf-8

# (C) Copyright IBM Corp. 2022.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#      http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

from __future__ import (absolute_import, division, print_function)
__metaclass__ = type


DOCUMENTATION = r'''
---
module: ibm_schematics_action
short_description: Manage C(schematics_actions) for Schematics Service API.
author: Kavya Handadi (@kavya498)
version_added: "1.0.0"
description:
  - This module creates, updates, or deletes a C(schematics_action) resource for Schematics Service API.
requirements:
  - "SchematicsV1"
options:
  outputs:
    description:
      - Output variables for the Action.
    type: list
    elements: dict
    suboptions:
      name:
        description:
          - The name of the variable. For example, C(name = "inventory username").
        type: str
      value:
        description: |
          The value for the variable or reference to the value.
          For example, C(value = "<provide your sshI(key)value with \n>").
          B(Note) The SSH key should contain C(\n) at the end of the key details in case of command line or API calls.
        type: str
      use_default:
        description:
          - True, will ignore the data in the value attribute, instead the data in metadata.defaultI(value will be used.
        type: bool
      metadata:
        description:
          - An user editable metadata for the variables.
        type: dict
        suboptions:
          type:
            description:
              - Type of the variable.
            type: str
            choices:
              - boolean
              - string
              - integer
              - date
              - array
              - list
              - map
              - complex
              - link
          aliases:
            description:
              - The list of aliases for the variable name.
            type: list
            elements: str
          description:
            description:
              - The description of the meta data.
            type: str
          cloud_data_type:
            description:
              - Cloud data type of the variable. eg. resourceI(group)id, region, vpcI(id.
            type: str
          default_value:
            description:
              - Default value for the variable only if the override value is not specified.
            type: str
          link_status:
            description:
              - The status of the link.
            type: str
            choices:
              - normal
              - broken
          secure:
            description:
              - Is the variable secure or sensitive ?.
            type: bool
          immutable:
            description:
              - Is the variable readonly ?.
            type: bool
          hidden:
            description:
              - If B(true), the variable is not displayed on UI or Command line.
            type: bool
          required:
            description:
              - If the variable required?.
            type: bool
          options:
            description: |
              The list of possible values for this variable.
              If type is B(integer) or B(date),
              then the array of string is converted to array of integers or date during the runtime.
            type: list
            elements: str
          min_value:
            description:
              - The minimum value of the variable. Applicable for the integer type.
            type: int
          max_value:
            description:
              - The maximum value of the variable. Applicable for the integer type.
            type: int
          min_length:
            description:
              - The minimum length of the variable value. Applicable for the string type.
            type: int
          max_length:
            description:
              - The maximum length of the variable value. Applicable for the string type.
            type: int
          matches:
            description:
              - The regex for the variable value.
            type: str
          position:
            description:
              - The relative position of this variable in a list.
            type: int
          group_by:
            description:
              - The display name of the group this variable belongs to.
            type: str
          source:
            description:
              - The source of this meta-data.
            type: str
      link:
        description:
          - The reference link to the variable value By default the expression points to C($self.value).
        type: str
  settings:
    description:
      - Environment variables for the Action.
    type: list
    elements: dict
    suboptions:
      name:
        description:
          - The name of the variable. For example, C(name = "inventory username").
        type: str
      value:
        description: |
          The value for the variable or reference to the value.
          For example, C(value = "<provide your sshI(key)value with \n>").
          B(Note) The SSH key should contain C(\n) at the end of the key details in case of command line or API calls.
        type: str
      use_default:
        description:
          - True, will ignore the data in the value attribute, instead the data in metadata.defaultI(value will be used.
        type: bool
      metadata:
        description:
          - An user editable metadata for the variables.
        type: dict
        suboptions:
          type:
            description:
              - Type of the variable.
            type: str
            choices:
              - boolean
              - string
              - integer
              - date
              - array
              - list
              - map
              - complex
              - link
          aliases:
            description:
              - The list of aliases for the variable name.
            type: list
            elements: str
          description:
            description:
              - The description of the meta data.
            type: str
          cloud_data_type:
            description:
              - Cloud data type of the variable. eg. resourceI(group)id, region, vpcI(id.
            type: str
          default_value:
            description:
              - Default value for the variable only if the override value is not specified.
            type: str
          link_status:
            description:
              - The status of the link.
            type: str
            choices:
              - normal
              - broken
          secure:
            description:
              - Is the variable secure or sensitive ?.
            type: bool
          immutable:
            description:
              - Is the variable readonly ?.
            type: bool
          hidden:
            description:
              - If B(true), the variable is not displayed on UI or Command line.
            type: bool
          required:
            description:
              - If the variable required?.
            type: bool
          options:
            description: |
              The list of possible values for this variable.
              If type is B(integer) or B(date), then the array of string is converted to array of integers or date during the runtime.
            type: list
            elements: str
          min_value:
            description:
              - The minimum value of the variable. Applicable for the integer type.
            type: int
          max_value:
            description:
              - The maximum value of the variable. Applicable for the integer type.
            type: int
          min_length:
            description:
              - The minimum length of the variable value. Applicable for the string type.
            type: int
          max_length:
            description:
              - The maximum length of the variable value. Applicable for the string type.
            type: int
          matches:
            description:
              - The regex for the variable value.
            type: str
          position:
            description:
              - The relative position of this variable in a list.
            type: int
          group_by:
            description:
              - The display name of the group this variable belongs to.
            type: str
          source:
            description:
              - The source of this meta-data.
            type: str
      link:
        description:
          - The reference link to the variable value By default the expression points to C($self.value).
        type: str
  credentials:
    description:
      - credentials of the Action.
    type: list
    elements: dict
    suboptions:
      name:
        description:
          - The name of the credential variable.
        type: str
      value:
        description: |
          The credential value for the variable or reference to the value.
          For example, C(value = "<provide your sshI(key)value with \n>").
          B(Note) The SSH key should contain C(\n) at the end of the key details in case of command line or API calls.
        type: str
      use_default:
        description: |
          True, will ignore the data in the value attribute,instead the data in metadata.defaultI(value will be used.
        type: bool
      metadata:
        description:
          - An user editable metadata for the credential variables.
        type: dict
        suboptions:
          type:
            description:
              - Type of the variable.
            type: str
            choices:
              - string
              - link
          aliases:
            description:
              - The list of aliases for the variable name.
            type: list
            elements: str
          description:
            description:
              - The description of the meta data.
            type: str
          cloud_data_type:
            description:
              - Cloud data type of the credential variable. eg. apiI(key, iam)token, profileI(id.
            type: str
          default_value:
            description:
              - Default value for the variable only if the override value is not specified.
            type: str
          link_status:
            description:
              - The status of the link.
            type: str
            choices:
              - normal
              - broken
          immutable:
            description:
              - Is the variable readonly ?.
            type: bool
          hidden:
            description:
              - If B(true), the variable is not displayed on UI or Command line.
            type: bool
          required:
            description:
              - If the variable required?.
            type: bool
          position:
            description:
              - The relative position of this variable in a list.
            type: int
          group_by:
            description:
              - The display name of the group this variable belongs to.
            type: str
          source:
            description:
              - The source of this meta-data.
            type: str
      link:
        description:
          - The reference link to the variable value By default the expression points to C($self.value).
        type: str
  inputs:
    description:
      - Input variables for the Action.
    type: list
    elements: dict
    suboptions:
      name:
        description:
          - The name of the variable. For example, C(name = "inventory username").
        type: str
      value:
        description: |
          The value for the variable or reference to the value.
          For example, C(value = "<provide your sshI(key)value with \n>").
          B(Note) The SSH key should contain C(\n) at the end of the key details in case of command line or API calls.
        type: str
      use_default:
        description:
          - True, will ignore the data in the value attribute, instead the data in metadata.defaultI(value will be used.
        type: bool
      metadata:
        description:
          - An user editable metadata for the variables.
        type: dict
        suboptions:
          type:
            description:
              - Type of the variable.
            type: str
            choices:
              - boolean
              - string
              - integer
              - date
              - array
              - list
              - map
              - complex
              - link
          aliases:
            description:
              - The list of aliases for the variable name.
            type: list
            elements: str
          description:
            description:
              - The description of the meta data.
            type: str
          cloud_data_type:
            description:
              - Cloud data type of the variable. eg. resourceI(group)id, region, vpcI(id.
            type: str
          default_value:
            description:
              - Default value for the variable only if the override value is not specified.
            type: str
          link_status:
            description:
              - The status of the link.
            type: str
            choices:
              - normal
              - broken
          secure:
            description:
              - Is the variable secure or sensitive ?.
            type: bool
          immutable:
            description:
              - Is the variable readonly ?.
            type: bool
          hidden:
            description:
              - If B(true), the variable is not displayed on UI or Command line.
            type: bool
          required:
            description:
              - If the variable required?.
            type: bool
          options:
            description: |
              The list of possible values for this variable.
              If type is B(integer) or B(date), then the array of string is converted to array of integers or date during the runtime.
            type: list
            elements: str
          min_value:
            description:
              - The minimum value of the variable. Applicable for the integer type.
            type: int
          max_value:
            description:
              - The maximum value of the variable. Applicable for the integer type.
            type: int
          min_length:
            description:
              - The minimum length of the variable value. Applicable for the string type.
            type: int
          max_length:
            description:
              - The maximum length of the variable value. Applicable for the string type.
            type: int
          matches:
            description:
              - The regex for the variable value.
            type: str
          position:
            description:
              - The relative position of this variable in a list.
            type: int
          group_by:
            description:
              - The display name of the group this variable belongs to.
            type: str
          source:
            description:
              - The source of this meta-data.
            type: str
      link:
        description:
          - The reference link to the variable value By default the expression points to C($self.value).
        type: str
  description:
    description:
      - Action description.
    type: str
  source_readme_url:
    description:
      - URL of the C(README) file, for the source URL.
    type: str
  bastion_credential:
    description:
      - User editable credential variable data and system generated reference to the value.
    type: dict
    suboptions:
      name:
        description:
          - The name of the credential variable.
        type: str
      value:
        description: |
          The credential value for the variable or reference to the value.
          For example, C(value = "<provide your sshI(key)value with \n>").
          B(Note) The SSH key should contain C(\n) at the end of the key details in case of command line or API calls.
        type: str
      use_default:
        description:
          - True, will ignore the data in the value attribute, instead the data in metadata.defaultI(value will be used.
        type: bool
      metadata:
        description:
          - An user editable metadata for the credential variables.
        type: dict
        suboptions:
          type:
            description:
              - Type of the variable.
            type: str
            choices:
              - string
              - link
          aliases:
            description:
              - The list of aliases for the variable name.
            type: list
            elements: str
          description:
            description:
              - The description of the meta data.
            type: str
          cloud_data_type:
            description:
              - Cloud data type of the credential variable. eg. apiI(key, iam)token, profileI(id.
            type: str
          default_value:
            description:
              - Default value for the variable only if the override value is not specified.
            type: str
          link_status:
            description:
              - The status of the link.
            type: str
            choices:
              - normal
              - broken
          immutable:
            description:
              - Is the variable readonly ?.
            type: bool
          hidden:
            description:
              - If B(true), the variable is not displayed on UI or Command line.
            type: bool
          required:
            description:
              - If the variable required?.
            type: bool
          position:
            description:
              - The relative position of this variable in a list.
            type: int
          group_by:
            description:
              - The display name of the group this variable belongs to.
            type: str
          source:
            description:
              - The source of this meta-data.
            type: str
      link:
        description:
          - The reference link to the variable value By default the expression points to C($self.value).
        type: str
  source_type:
    description:
      - Type of source for the Template.
    type: str
    choices:
      - local
      - git_hub
      - git_hub_enterprise
      - git_lab
      - ibm_git_lab
      - ibm_cloud_catalog
  source:
    description:
      - Source of templates, playbooks, or controls.
    type: dict
    suboptions:
      source_type:
        description:
          - Type of source for the Template.
        type: str
        choices:
          - local
          - git_hub
          - git_hub_enterprise
          - git_lab
          - ibm_git_lab
          - ibm_cloud_catalog
      git:
        description:
          - The connection details to the Git source repository.
        type: dict
        suboptions:
          computed_git_repo_url:
            description:
              - The complete URL which is computed by the B(gitI(repo)url), B(gitI(repo)folder), and B(branch).
            type: str
          git_repo_url:
            description:
              - The URL to the Git repository that can be used to clone the template.
            type: str
          git_token:
            description:
              - The Personal Access Token (PAT) to connect to the Git URLs.
            type: str
          git_repo_folder:
            description:
              - The name of the folder in the Git repository, that contains the template.
            type: str
          git_release:
            description:
              - The name of the release tag that are used to fetch the Git repository.
            type: str
          git_branch:
            description:
              - The name of the branch that are used to fetch the Git repository.
            type: str
      catalog:
        description:
          - The connection details to the IBM Cloud Catalog source.
        type: dict
        suboptions:
          catalog_name:
            description:
              - The name of the private catalog.
            type: str
          offering_name:
            description:
              - The name of an offering in the IBM Cloud Catalog.
            type: str
          offering_version:
            description:
              - The version string of an offering in the IBM Cloud Catalog.
            type: str
          offering_kind:
            description:
              - The type of an offering, in the IBM Cloud Catalog.
            type: str
          catalog_id:
            description:
              - The ID of a private catalog.
            type: str
          offering_id:
            description:
              - The ID of an offering in the IBM Cloud Catalog.
            type: str
          offering_version_id:
            description:
              - The ID of an offering version the IBM Cloud Catalog.
            type: str
          offering_repo_url:
            description:
              - The repository URL of an offering, in the IBM Cloud Catalog.
            type: str
          offering_provisioner_working_directory:
            description:
              - Root folder name in .tgz file.
            type: str
  inventory:
    description:
      - Target inventory record ID, used by the action or ansible playbook.
    type: str
  command_parameter:
    description:
      - Schematics job command parameter (playbook-name).
    type: str
  tags:
    description:
      - Action tags.
    type: list
    elements: str
  user_state:
    description:
      - User defined status of the Schematics object.
    type: dict
    suboptions:
      state_:
        description: |
          User-defined states
          I( C(draft) Object can be modified; can be used by Jobs run by the author, during execution)
          C(live) Object can be modified; can be used by Jobs during execution
          I( C(locked) Object cannot be modified; can be used by Jobs during execution)
          C(disable) Object can be modified. cannot be used by Jobs during execution.
        type: str
        choices:
          - draft
          - live
          - locked
          - disable
      set_by:
        description:
          - Name of the User who set the state of the Object.
        type: str
      set_at:
        description:
          - When the User who set the state of the Object.
        type: str
  bastion_connection_type:
    description: |
      Type of connection to be used when connecting to bastion host.
      If the C(inventoryI(connection)type=winrm), then C(bastionI(connection)type) is not supported.
    type: str
    choices:
      - ssh
  inventory_connection_type:
    description: |
      Type of connection to be used when connecting to remote host.
      B(Note) Currently, WinRM supports only Windows system with the public IPs and do not support Bastion host.
    type: str
    choices:
      - ssh
      - winrm
  resource_group:
    description:
      - Resource-group name for an action. By default, an action is created in C(Default) resource group.
    type: str
  targets_ini:
    description: |
      Inventory of host and host group for the playbook in C(INI) file format.
      For example, C("targetsI(ini": "[webserverhost] 72.22.192.6 [dbhost]172.22.192.5").
      For more information, about an inventory host group syntax,
      see [Inventory host groups](https://cloud.ibm.com/docs/schematics?topic=schematics-schematics-cli-reference#schematics-inventory-host-grps).
    type: str
  name:
    description: |
      The unique name of your action.
      The name can be up to 128 characters long and can include alphanumeric characters, spaces, dashes, and underscores.
      B(Example) you can use the name to stop action.
    type: str
  location:
    description: |
      List of locations supported by IBM Cloud Schematics service.
      While creating your workspace or action, choose the right region, since it cannot be changed.
      Note, this does not limit the location of the IBM Cloud resources, provisioned using Schematics.
    type: str
    choices:
      - us-south
      - us-east
      - eu-gb
      - eu-de
  bastion:
    description:
      - Describes a bastion resource.
    type: dict
    suboptions:
      name:
        description:
          - Bastion Name; the name must be unique.
        type: str
      host:
        description:
          - Reference to the Inventory resource definition.
        type: str
  state_:
    description:
      - Computed state of the Action.
    type: dict
    suboptions:
      status_code:
        description:
          - Status of automation (workspace or action).
        type: str
        choices:
          - normal
          - pending
          - disabled
          - critical
      status_job_id:
        description:
          - Job id reference for this status.
        type: str
      status_message:
        description:
          - Automation status message - to be displayed along with the statusI(code.
        type: str
  sys_lock:
    description:
      - System lock status.
    type: dict
    suboptions:
      sys_locked:
        description:
          - Is the automation locked by a Schematic job ?.
        type: bool
      sys_locked_by:
        description:
          - Name of the User who performed the job, that lead to the locking of the automation.
        type: str
      sys_locked_at:
        description:
          - When the User performed the job that lead to locking of the automation ?.
        type: str
  action_id:
    description:
      - Action Id.  Use GET /actions API to look up the Action Ids in your IBM Cloud account.
    type: str
  profile:
    description:
      - Level of details returned by the get method.
    type: str
    choices:
      - summary
      - detailed
      - ids
  propagate:
    description:
      - Auto propagate the chaange or deletion to the dependent resources.
    type: bool
  force:
    description:
      - Equivalent to -force options in the command line.
    type: bool
  x_github_token:
    description: |
      The personal access token to authenticate with your private GitHub or GitLab repository and access your Terraform template.
    type: str
  state:
    description:
      - Should the resource be present or absent.
    type: str
    default: present
    choices: [present, absent]
seealso:
  - name: IBM Cloud Schematics docs
    description: Use Schematics to run your Ansible playbooks to provision, configure, and manage IBM Cloud resources.
    link: U(https://cloud.ibm.com/docs/schematics)
notes:
  - |
    Authenticate this module by using an IBM Cloud API key.
    For more information about working with IBM Cloud API keys, see I(Managing API keys): U(https://cloud.ibm.com/docs/account?topic=account-manapikey).
  - |
    To configure the authentication, set your IBM Cloud API key on the C(IC_API_KEY) environment variable.
    The API key will be used to authenticate all IBM Cloud modules that use this environment variable.
'''

EXAMPLES = r'''
- name: Create ibm_schematics_action
  vars:
    user_state_model:
    git_source_model:
    catalog_source_model:
    external_source_model:
    credential_variable_metadata_model:
    credential_variable_data_model:
    bastion_resource_definition_model:
    variable_metadata_model:
    variable_data_model:
    action_state_model:
    system_lock_model:
  ibm_schematics_action:
    name: 'Stop Action'
    description: |
      'The description of your action.
      The description can be up to 2048 characters long in size.
      **Example** you can use the description to stop the targets.'

- name: Update ibm_schematics_action
  vars:
    user_state_model:
    git_source_model:
    catalog_source_model:
    external_source_model:
    credential_variable_metadata_model:
    credential_variable_data_model:
    bastion_resource_definition_model:
    variable_metadata_model:
    variable_data_model:
    action_state_model:
    system_lock_model:
  ibm_schematics_action:
    name: 'Stop Action'
    description: |
      'The description of your action.
      The description can be up to 2048 characters long in size.
      **Example** you can use the description to stop the targets.'

- name: Delete ibm_schematics_action
  ibm_schematics_action:
'''

RETURN = '''
msg:
  description: |-
    A dictionary that represents the result.
    If a resource was created, an C(Action) object is returned.
    If a resource was updated, an C(Action) object is returned.
    If a resource was deleted, the C(id) and C(status) fields are returned.
  returned: always
  type: dict
'''


from ..module_utils import config
from ansible.module_utils.basic import AnsibleModule
try:
    from ibm_schematics import SchematicsV1
    from ibm_cloud_sdk_core import ApiException
except ImportError:
    pass


def run_module():
    module_args = dict(
        outputs=dict(
            type='list',
            elements='dict',
            options=dict(
                name=dict(
                    type='str',
                    required=False),
                value=dict(
                    type='str',
                    required=False),
                use_default=dict(
                    type='bool',
                    required=False),
                metadata=dict(
                    type='dict',
                    options=dict(
                        type=dict(
                            type='str',
                            choices=['boolean', 'string', 'integer', 'date',
                                     'array', 'list', 'map', 'complex', 'link'],
                            required=False),
                        aliases=dict(
                            type='list',
                            elements='str',
                            required=False),
                        description=dict(
                            type='str',
                            required=False),
                        cloud_data_type=dict(
                            type='str',
                            required=False),
                        default_value=dict(
                            type='str',
                            required=False),
                        link_status=dict(
                            type='str',
                            choices=['normal', 'broken'],
                            required=False),
                        secure=dict(
                            type='bool',
                            required=False),
                        immutable=dict(
                            type='bool',
                            required=False),
                        hidden=dict(
                            type='bool',
                            required=False),
                        required=dict(
                            type='bool',
                            required=False),
                        options=dict(
                            type='list',
                            elements='str',
                            required=False),
                        min_value=dict(
                            type='int',
                            required=False),
                        max_value=dict(
                            type='int',
                            required=False),
                        min_length=dict(
                            type='int',
                            required=False),
                        max_length=dict(
                            type='int',
                            required=False),
                        matches=dict(
                            type='str',
                            required=False),
                        position=dict(
                            type='int',
                            required=False),
                        group_by=dict(
                            type='str',
                            required=False),
                        source=dict(
                            type='str',
                            required=False),
                    ),
                    required=False),
                link=dict(
                    type='str',
                    required=False),
            ),
            required=False),
        settings=dict(
            type='list',
            elements='dict',
            options=dict(
                name=dict(
                    type='str',
                    required=False),
                value=dict(
                    type='str',
                    required=False),
                use_default=dict(
                    type='bool',
                    required=False),
                metadata=dict(
                    type='dict',
                    options=dict(
                        type=dict(
                            type='str',
                            choices=['boolean', 'string', 'integer', 'date',
                                     'array', 'list', 'map', 'complex', 'link'],
                            required=False),
                        aliases=dict(
                            type='list',
                            elements='str',
                            required=False),
                        description=dict(
                            type='str',
                            required=False),
                        cloud_data_type=dict(
                            type='str',
                            required=False),
                        default_value=dict(
                            type='str',
                            required=False),
                        link_status=dict(
                            type='str',
                            choices=['normal', 'broken'],
                            required=False),
                        secure=dict(
                            type='bool',
                            required=False),
                        immutable=dict(
                            type='bool',
                            required=False),
                        hidden=dict(
                            type='bool',
                            required=False),
                        required=dict(
                            type='bool',
                            required=False),
                        options=dict(
                            type='list',
                            elements='str',
                            required=False),
                        min_value=dict(
                            type='int',
                            required=False),
                        max_value=dict(
                            type='int',
                            required=False),
                        min_length=dict(
                            type='int',
                            required=False),
                        max_length=dict(
                            type='int',
                            required=False),
                        matches=dict(
                            type='str',
                            required=False),
                        position=dict(
                            type='int',
                            required=False),
                        group_by=dict(
                            type='str',
                            required=False),
                        source=dict(
                            type='str',
                            required=False),
                    ),
                    required=False),
                link=dict(
                    type='str',
                    required=False),
            ),
            required=False),
        credentials=dict(
            type='list',
            elements='dict',
            options=dict(
                name=dict(
                    type='str',
                    required=False),
                value=dict(
                    type='str',
                    required=False),
                use_default=dict(
                    type='bool',
                    required=False),
                metadata=dict(
                    type='dict',
                    options=dict(
                        type=dict(
                            type='str',
                            choices=['string', 'link'],
                            required=False),
                        aliases=dict(
                            type='list',
                            elements='str',
                            required=False),
                        description=dict(
                            type='str',
                            required=False),
                        cloud_data_type=dict(
                            type='str',
                            required=False),
                        default_value=dict(
                            type='str',
                            required=False),
                        link_status=dict(
                            type='str',
                            choices=['normal', 'broken'],
                            required=False),
                        immutable=dict(
                            type='bool',
                            required=False),
                        hidden=dict(
                            type='bool',
                            required=False),
                        required=dict(
                            type='bool',
                            required=False),
                        position=dict(
                            type='int',
                            required=False),
                        group_by=dict(
                            type='str',
                            required=False),
                        source=dict(
                            type='str',
                            required=False),
                    ),
                    required=False),
                link=dict(
                    type='str',
                    required=False),
            ),
            required=False),
        inputs=dict(
            type='list',
            elements='dict',
            options=dict(
                name=dict(
                    type='str',
                    required=False),
                value=dict(
                    type='str',
                    required=False),
                use_default=dict(
                    type='bool',
                    required=False),
                metadata=dict(
                    type='dict',
                    options=dict(
                        type=dict(
                            type='str',
                            choices=['boolean', 'string', 'integer', 'date',
                                     'array', 'list', 'map', 'complex', 'link'],
                            required=False),
                        aliases=dict(
                            type='list',
                            elements='str',
                            required=False),
                        description=dict(
                            type='str',
                            required=False),
                        cloud_data_type=dict(
                            type='str',
                            required=False),
                        default_value=dict(
                            type='str',
                            required=False),
                        link_status=dict(
                            type='str',
                            choices=['normal', 'broken'],
                            required=False),
                        secure=dict(
                            type='bool',
                            required=False),
                        immutable=dict(
                            type='bool',
                            required=False),
                        hidden=dict(
                            type='bool',
                            required=False),
                        required=dict(
                            type='bool',
                            required=False),
                        options=dict(
                            type='list',
                            elements='str',
                            required=False),
                        min_value=dict(
                            type='int',
                            required=False),
                        max_value=dict(
                            type='int',
                            required=False),
                        min_length=dict(
                            type='int',
                            required=False),
                        max_length=dict(
                            type='int',
                            required=False),
                        matches=dict(
                            type='str',
                            required=False),
                        position=dict(
                            type='int',
                            required=False),
                        group_by=dict(
                            type='str',
                            required=False),
                        source=dict(
                            type='str',
                            required=False),
                    ),
                    required=False),
                link=dict(
                    type='str',
                    required=False),
            ),
            required=False),
        description=dict(
            type='str',
            required=False),
        source_readme_url=dict(
            type='str',
            required=False),
        # Represents the CredentialVariableData Python class
        bastion_credential=dict(
            type='dict',
            options=dict(
                name=dict(
                    type='str',
                    required=False),
                value=dict(
                    type='str',
                    required=False),
                use_default=dict(
                    type='bool',
                    required=False),
                metadata=dict(
                    type='dict',
                    options=dict(
                        type=dict(
                            type='str',
                            choices=['string', 'link'],
                            required=False),
                        aliases=dict(
                            type='list',
                            elements='str',
                            required=False),
                        description=dict(
                            type='str',
                            required=False),
                        cloud_data_type=dict(
                            type='str',
                            required=False),
                        default_value=dict(
                            type='str',
                            required=False),
                        link_status=dict(
                            type='str',
                            choices=['normal', 'broken'],
                            required=False),
                        immutable=dict(
                            type='bool',
                            required=False),
                        hidden=dict(
                            type='bool',
                            required=False),
                        required=dict(
                            type='bool',
                            required=False),
                        position=dict(
                            type='int',
                            required=False),
                        group_by=dict(
                            type='str',
                            required=False),
                        source=dict(
                            type='str',
                            required=False),
                    ),
                    required=False),
                link=dict(
                    type='str',
                    required=False),
            ),
            required=False),
        source_type=dict(
            type='str',
            choices=['local', 'git_hub', 'git_hub_enterprise',
                     'git_lab', 'ibm_git_lab', 'ibm_cloud_catalog'],
            required=False),
        # Represents the ExternalSource Python class
        source=dict(
            type='dict',
            options=dict(
                source_type=dict(
                    type='str',
                    choices=['local', 'git_hub', 'git_hub_enterprise',
                             'git_lab', 'ibm_git_lab', 'ibm_cloud_catalog'],
                    required=False),
                git=dict(
                    type='dict',
                    options=dict(
                        computed_git_repo_url=dict(
                            type='str',
                            required=False),
                        git_repo_url=dict(
                            type='str',
                            required=False),
                        git_token=dict(
                            type='str',
                            required=False),
                        git_repo_folder=dict(
                            type='str',
                            required=False),
                        git_release=dict(
                            type='str',
                            required=False),
                        git_branch=dict(
                            type='str',
                            required=False),
                    ),
                    required=False),
                catalog=dict(
                    type='dict',
                    options=dict(
                        catalog_name=dict(
                            type='str',
                            required=False),
                        offering_name=dict(
                            type='str',
                            required=False),
                        offering_version=dict(
                            type='str',
                            required=False),
                        offering_kind=dict(
                            type='str',
                            required=False),
                        catalog_id=dict(
                            type='str',
                            required=False),
                        offering_id=dict(
                            type='str',
                            required=False),
                        offering_version_id=dict(
                            type='str',
                            required=False),
                        offering_repo_url=dict(
                            type='str',
                            required=False),
                        offering_provisioner_working_directory=dict(
                            type='str',
                            required=False),
                    ),
                    required=False),
            ),
            required=False),
        inventory=dict(
            type='str',
            required=False),
        command_parameter=dict(
            type='str',
            required=False),
        tags=dict(
            type='list',
            elements='str',
            required=False),
        # Represents the UserState Python class
        user_state=dict(
            type='dict',
            options=dict(
                state_=dict(
                    type='str',
                    choices=['draft', 'live', 'locked', 'disable'],
                    required=False),
                set_by=dict(
                    type='str',
                    required=False),
                set_at=dict(
                    type='str',
                    required=False),
            ),
            required=False),
        bastion_connection_type=dict(
            type='str',
            choices=['ssh'],
            required=False),
        inventory_connection_type=dict(
            type='str',
            choices=['ssh', 'winrm'],
            required=False),
        resource_group=dict(
            type='str',
            required=False),
        targets_ini=dict(
            type='str',
            required=False),
        name=dict(
            type='str',
            required=False),
        location=dict(
            type='str',
            choices=['us-south', 'us-east', 'eu-gb', 'eu-de'],
            required=False),
        # Represents the BastionResourceDefinition Python class
        bastion=dict(
            type='dict',
            options=dict(
                name=dict(
                    type='str',
                    required=False),
                host=dict(
                    type='str',
                    required=False),
            ),
            required=False),
        # Represents the ActionState Python class
        state_=dict(
            type='dict',
            options=dict(
                status_code=dict(
                    type='str',
                    choices=['normal', 'pending', 'disabled', 'critical'],
                    required=False),
                status_job_id=dict(
                    type='str',
                    required=False),
                status_message=dict(
                    type='str',
                    required=False),
            ),
            required=False),
        # Represents the SystemLock Python class
        sys_lock=dict(
            type='dict',
            options=dict(
                sys_locked=dict(
                    type='bool',
                    required=False),
                sys_locked_by=dict(
                    type='str',
                    required=False),
                sys_locked_at=dict(
                    type='str',
                    required=False),
            ),
            required=False),
        action_id=dict(
            type='str',
            required=False),
        profile=dict(
            type='str',
            choices=['summary', 'detailed', 'ids'],
            required=False),
        propagate=dict(
            type='bool',
            required=False),
        force=dict(
            type='bool',
            required=False),
        x_github_token=dict(
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

    outputs = module.params["outputs"]
    settings = module.params["settings"]
    credentials = module.params["credentials"]
    inputs = module.params["inputs"]
    description = module.params["description"]
    source_readme_url = module.params["source_readme_url"]
    bastion_credential = module.params["bastion_credential"]
    source_type = module.params["source_type"]
    source = module.params["source"]
    inventory = module.params["inventory"]
    command_parameter = module.params["command_parameter"]
    tags = module.params["tags"]
    user_state = module.params["user_state"]
    bastion_connection_type = module.params["bastion_connection_type"]
    inventory_connection_type = module.params["inventory_connection_type"]
    resource_group = module.params["resource_group"]
    targets_ini = module.params["targets_ini"]
    name = module.params["name"]
    location = module.params["location"]
    bastion = module.params["bastion"]
    state_ = module.params["state_"]
    sys_lock = module.params["sys_lock"]
    action_id = module.params["action_id"]
    profile = module.params["profile"]
    propagate = module.params["propagate"]
    force = module.params["force"]
    x_github_token = module.params["x_github_token"]
    state = module.params["state"]

    sdk = config.get_schematicsv1_sdk()

    resource_exists = True

    # Check for existence
    if action_id:
        try:
            sdk.get_action(
                action_id=action_id,
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
                sdk.delete_action(
                    action_id=action_id,
                    force=force,
                    propagate=propagate,
                )
            except ApiException as ex:
                module.fail_json(msg=ex.message)
            else:
                payload = {"id": action_id, "status": "deleted"}
                module.exit_json(changed=True, msg=payload)
        else:
            payload = {"id": action_id, "status": "not_found"}
            module.exit_json(changed=False, msg=payload)

    if state == "present":
        if not resource_exists:
            # Create path
            try:
                result = sdk.create_action(
                    name=name,
                    description=description,
                    location=location,
                    resource_group=resource_group,
                    bastion_connection_type=bastion_connection_type,
                    inventory_connection_type=inventory_connection_type,
                    tags=tags,
                    user_state=user_state,
                    source_readme_url=source_readme_url,
                    source=source,
                    source_type=source_type,
                    command_parameter=command_parameter,
                    inventory=inventory,
                    credentials=credentials,
                    bastion=bastion,
                    bastion_credential=bastion_credential,
                    targets_ini=targets_ini,
                    inputs=inputs,
                    outputs=outputs,
                    settings=settings,
                    state=state_,
                    sys_lock=sys_lock,
                    x_github_token=x_github_token,
                ).get_result()
            except ApiException as ex:
                module.fail_json(msg=ex.message)
            else:
                module.exit_json(changed=True, msg=result)
        else:
            # Update path
            try:
                result = sdk.update_action(
                    action_id=action_id,
                    name=name,
                    description=description,
                    location=location,
                    resource_group=resource_group,
                    bastion_connection_type=bastion_connection_type,
                    inventory_connection_type=inventory_connection_type,
                    tags=tags,
                    user_state=user_state,
                    source_readme_url=source_readme_url,
                    source=source,
                    source_type=source_type,
                    command_parameter=command_parameter,
                    inventory=inventory,
                    credentials=credentials,
                    bastion=bastion,
                    bastion_credential=bastion_credential,
                    targets_ini=targets_ini,
                    inputs=inputs,
                    outputs=outputs,
                    settings=settings,
                    state=state_,
                    sys_lock=sys_lock,
                    x_github_token=x_github_token,
                ).get_result()
            except ApiException as ex:
                module.fail_json(msg=ex.message)
            else:
                module.exit_json(changed=True, msg=result)


def main():
    run_module()


if __name__ == '__main__':
    main()
