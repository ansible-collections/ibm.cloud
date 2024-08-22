#!/usr/bin/python
# coding: utf-8

# (C) Copyright IBM Corp. 2024.
#
# GNU General Public License v3.0+ (see LICENSE or https://www.gnu.org/licenses/gpl-3.0.txt)

from __future__ import (absolute_import, division, print_function)
__metaclass__ = type


DOCUMENTATION = r'''
---
module: ibm_schematics_action_info
short_description: Manage C(schematics_action) for Schematics Service API.
author: Gannayak Pabra (@Gannayak0722)
version_added: "1.0.0"
description:
  - This module retrieves one or more C(schematics_action) for Schematics Service API.
requirements:
  - "SchematicsV1"
options:
  action_id:
    description: "Action Id.  Use GET /actions API to look up the Action Ids in your IBM Cloud
      account."
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
- name: Read ibm_schematics_action
  ibm_schematics_action_info:
    action_id: 'testString'
    profile: 'summary'
'''

RETURN = r'''
name:
  description: "The unique name of your action. The name can be up to 128 characters long and can
    include alphanumeric characters, spaces, dashes, and underscores. B(Example) you can
    use the name to stop action."
  type: str
  returned: on success for read operation
description:
  description: "Action description."
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
resource_group:
  description: "Resource-group name for an action. By default, an action is created in C(Default)
    resource group."
  type: str
  returned: on success for read operation
bastion_connection_type:
  description: "Type of connection to be used when connecting to bastion host.  If the
    C(inventoryI(connection)type=winrm), then C(bastionI(connection)type) is not
    supported."
  type: str
  choices:
    - "ssh"
  returned: on success for read operation
inventory_connection_type:
  description: "Type of connection to be used when connecting to remote host.  B(Note) Currently,
    WinRM supports only Windows system with the public IPs and do not support Bastion
    host."
  type: str
  choices:
    - "ssh"
    - "winrm"
  returned: on success for read operation
tags:
  description: "Action tags."
  type: list
  elements: str
  returned: on success for read operation
user_state:
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
source_readme_url:
  description: "URL of the C(README) file, for the source URL."
  type: str
  returned: on success for read operation
source:
  description: "Source of templates, playbooks, or controls."
  type: dict
  contains:
    source_type:
      description: "Type of source for the Template."
      type: str
      choices:
        - 'local'
        - 'git_hub'
        - 'git_hub_enterprise'
        - 'git_lab'
        - 'ibm_git_lab'
        - 'ibm_cloud_catalog'
    git:
      description: "The connection details to the Git source repository."
      type: dict
      contains:
        computed_git_repo_url:
          description: "The complete URL which is computed by the B(gitI(repo)url), B(gitI(repo)folder), and
            B(branch)."
          type: str
        git_repo_url:
          description: "The URL to the Git repository that can be used to clone the template."
          type: str
        git_token:
          description: "The Personal Access Token (PAT) to connect to the Git URLs."
          type: str
        git_repo_folder:
          description: "The name of the folder in the Git repository, that contains the template."
          type: str
        git_release:
          description: "The name of the release tag that are used to fetch the Git repository."
          type: str
        git_branch:
          description: "The name of the branch that are used to fetch the Git repository."
          type: str
        git_commit:
          description: "The git commit hash used to fetch the repository."
          type: str
        git_commit_timestamp:
          description: "The timestamp of the git commit hash used to fetch the repository."
          type: str
    catalog:
      description: "The connection details to the IBM Cloud Catalog source."
      type: dict
      contains:
        catalog_name:
          description: "The name of the private catalog."
          type: str
        catalog_id:
          description: "The ID of a private catalog."
          type: str
        offering_name:
          description: "The name of an offering in the IBM Cloud Catalog."
          type: str
        offering_version:
          description: "The version of the software template that you chose to install from the IBM Cloud
            catalog."
          type: str
        offering_kind:
          description: "The type of an offering, in the IBM Cloud Catalog."
          type: str
        offering_target_kind:
          description: "Offering Target Kind."
          type: str
        offering_id:
          description: "The ID of an offering in the IBM Cloud Catalog."
          type: str
        offering_version_id:
          description: "The ID of an offering version the IBM Cloud Catalog."
          type: str
        offering_version_flavour_name:
          description: "Offering version flavour name."
          type: str
        offering_repo_url:
          description: "The repository URL of an offering, in the IBM Cloud Catalog."
          type: str
        offering_provisioner_working_directory:
          description: "Root folder name in .tgz file."
          type: str
        dry_run:
          description: "Dry run."
          type: bool
        owning_account:
          description: "Owning account ID of the catalog."
          type: str
        item_icon_url:
          description: "The URL to the icon of the software template in the IBM Cloud catalog."
          type: str
        item_id:
          description: "The ID of the software template that you chose to install from the IBM Cloud catalog.
            This software is provisioned with Schematics."
          type: str
        item_name:
          description: "The name of the software that you chose to install from the IBM Cloud catalog."
          type: str
        item_readme_url:
          description: "The URL to the readme file of the software template in the IBM Cloud catalog."
          type: str
        item_url:
          description: "The URL to the software template in the IBM Cloud catalog."
          type: str
        launch_url:
          description: "The URL to the dashboard to access your software."
          type: str
  returned: on success for read operation
source_type:
  description: "Type of source for the Template."
  type: str
  choices:
    - "local"
    - "git_hub"
    - "git_hub_enterprise"
    - "git_lab"
    - "ibm_git_lab"
    - "ibm_cloud_catalog"
  returned: on success for read operation
command_parameter:
  description: "Schematics job command parameter (playbook-name)."
  type: str
  returned: on success for read operation
inventory:
  description: "Target inventory record ID, used by the action or ansible playbook."
  type: str
  returned: on success for read operation
credentials:
  description: "credentials of the Action."
  type: list
  elements: 'dict'
  contains:
    name:
      description: "The name of the credential variable."
      type: str
    value:
      description: "The credential value for the variable or reference to the value. B(Note) The SSH key
        should contain three C(\\n) in the SSH key value as shown in the example for CLI or
        API calls. When using Bastion from API you need to add SSH key in both C(credentials)
        and C(bastion_credentials)."
      type: str
    use_default:
      description: "True, will ignore the data in the value attribute, instead the data in
        metadata.default_value will be used."
      type: bool
    metadata:
      description: "An user editable metadata for the credential variables."
      type: dict
      contains:
        type:
          description: "Type of the variable."
          type: str
          choices:
            - 'string'
            - 'link'
        aliases:
          description: "The list of aliases for the variable name."
          type: list
          elements: str
        description:
          description: "The description of the meta data."
          type: str
        cloud_data_type:
          description: "Cloud data type of the credential variable. eg. api_key, iam_token, profile_id."
          type: str
        default_value:
          description: "Default value for the variable only if the override value is not specified."
          type: str
        link_status:
          description: "The status of the link."
          type: str
          choices:
            - 'normal'
            - 'broken'
        immutable:
          description: "Is the variable readonly ?."
          type: bool
        hidden:
          description: "If B(true), the variable is not displayed on UI or Command line."
          type: bool
        required:
          description: "If the variable required?."
          type: bool
        position:
          description: "The relative position of this variable in a list."
          type: int
        group_by:
          description: "The display name of the group this variable belongs to."
          type: str
        source:
          description: "The source of this meta-data."
          type: str
    link:
      description: "The reference link to the variable value By default the expression points to
        C($self.value)."
      type: str
  returned: on success for read operation
bastion:
  description: "Describes a bastion resource."
  type: dict
  contains:
    name:
      description: "Bastion Name; the name must be unique."
      type: str
    host:
      description: "Reference to the Inventory resource definition."
      type: str
  returned: on success for read operation
bastion_credential:
  description: "User editable credential variable data and system generated reference to the value."
  type: dict
  contains:
    name:
      description: "The name of the credential variable."
      type: str
    value:
      description: "The credential value for the variable or reference to the value. B(Note) The SSH key
        should contain three C(\\n) in the SSH key value as shown in the example for CLI or
        API calls. When using Bastion from API you need to add SSH key in both C(credentials)
        and C(bastion_credentials)."
      type: str
    use_default:
      description: "True, will ignore the data in the value attribute, instead the data in
        metadata.default_value will be used."
      type: bool
    metadata:
      description: "An user editable metadata for the credential variables."
      type: dict
      contains:
        type:
          description: "Type of the variable."
          type: str
          choices:
            - 'string'
            - 'link'
        aliases:
          description: "The list of aliases for the variable name."
          type: list
          elements: str
        description:
          description: "The description of the meta data."
          type: str
        cloud_data_type:
          description: "Cloud data type of the credential variable. eg. api_key, iam_token, profile_id."
          type: str
        default_value:
          description: "Default value for the variable only if the override value is not specified."
          type: str
        link_status:
          description: "The status of the link."
          type: str
          choices:
            - 'normal'
            - 'broken'
        immutable:
          description: "Is the variable readonly ?."
          type: bool
        hidden:
          description: "If B(true), the variable is not displayed on UI or Command line."
          type: bool
        required:
          description: "If the variable required?."
          type: bool
        position:
          description: "The relative position of this variable in a list."
          type: int
        group_by:
          description: "The display name of the group this variable belongs to."
          type: str
        source:
          description: "The source of this meta-data."
          type: str
    link:
      description: "The reference link to the variable value By default the expression points to
        C($self.value)."
      type: str
  returned: on success for read operation
targets_ini:
  description: "Inventory of host and host group for the playbook in `INI` file format. For example,
    `\"targets_ini\": \"[webserverhost]
     172.22.192.6
     [dbhost]
     172.22.192.5\"`. For more information, about an inventory host group syntax, see
    [Inventory host
    groups](https://cloud.ibm.com/docs/schematics?topic=schematics-schematics-cli-reference#schematics-inventory-host-grps)."
  type: str
  returned: on success for read operation
inputs:
  description: "Input variables for the Action."
  type: list
  elements: 'dict'
  contains:
    name:
      description: "The name of the variable. For example, C(name = \"inventory username\")."
      type: str
    value:
      description: "The value for the variable or reference to the value. For example, C(value =
        \"<provide your sshI(key)value with \\n>\"). B(Note) The SSH key should contain C(\\n)
        at the end of the key details in case of command line or API calls."
      type: str
    use_default:
      description: "True, will ignore the data in the value attribute, instead the data in
        metadata.default_value will be used."
      type: bool
    metadata:
      description: "An user editable metadata for the variables."
      type: dict
      contains:
        type:
          description: "Type of the variable."
          type: str
          choices:
            - 'boolean'
            - 'string'
            - 'integer'
            - 'date'
            - 'array'
            - 'list'
            - 'map'
            - 'complex'
            - 'link'
        aliases:
          description: "The list of aliases for the variable name."
          type: list
          elements: str
        description:
          description: "The description of the meta data."
          type: str
        cloud_data_type:
          description: "Cloud data type of the variable. eg. resource_group_id, region, vpc_id."
          type: str
        default_value:
          description: "Default value for the variable only if the override value is not specified."
          type: str
        link_status:
          description: "The status of the link."
          type: str
          choices:
            - 'normal'
            - 'broken'
        secure:
          description: "Is the variable secure or sensitive ?."
          type: bool
        immutable:
          description: "Is the variable readonly ?."
          type: bool
        hidden:
          description: "If B(true), the variable is not displayed on UI or Command line."
          type: bool
        required:
          description: "If the variable required?."
          type: bool
        options:
          description: "The list of possible values for this variable.  If type is B(integer) or B(date), then
            the array of string is  converted to array of integers or date during the runtime."
          type: list
          elements: str
        min_value:
          description: "The minimum value of the variable. Applicable for the integer type."
          type: int
        max_value:
          description: "The maximum value of the variable. Applicable for the integer type."
          type: int
        min_length:
          description: "The minimum length of the variable value. Applicable for the string type."
          type: int
        max_length:
          description: "The maximum length of the variable value. Applicable for the string type."
          type: int
        matches:
          description: "The regex for the variable value."
          type: str
        position:
          description: "The relative position of this variable in a list."
          type: int
        group_by:
          description: "The display name of the group this variable belongs to."
          type: str
        source:
          description: "The source of this meta-data."
          type: str
    link:
      description: "The reference link to the variable value By default the expression points to
        C($self.value)."
      type: str
  returned: on success for read operation
outputs:
  description: "Output variables for the Action."
  type: list
  elements: 'dict'
  contains:
    name:
      description: "The name of the variable. For example, C(name = \"inventory username\")."
      type: str
    value:
      description: "The value for the variable or reference to the value. For example, C(value =
        \"<provide your sshI(key)value with \\n>\"). B(Note) The SSH key should contain C(\\n)
        at the end of the key details in case of command line or API calls."
      type: str
    use_default:
      description: "True, will ignore the data in the value attribute, instead the data in
        metadata.default_value will be used."
      type: bool
    metadata:
      description: "An user editable metadata for the variables."
      type: dict
      contains:
        type:
          description: "Type of the variable."
          type: str
          choices:
            - 'boolean'
            - 'string'
            - 'integer'
            - 'date'
            - 'array'
            - 'list'
            - 'map'
            - 'complex'
            - 'link'
        aliases:
          description: "The list of aliases for the variable name."
          type: list
          elements: str
        description:
          description: "The description of the meta data."
          type: str
        cloud_data_type:
          description: "Cloud data type of the variable. eg. resource_group_id, region, vpc_id."
          type: str
        default_value:
          description: "Default value for the variable only if the override value is not specified."
          type: str
        link_status:
          description: "The status of the link."
          type: str
          choices:
            - 'normal'
            - 'broken'
        secure:
          description: "Is the variable secure or sensitive ?."
          type: bool
        immutable:
          description: "Is the variable readonly ?."
          type: bool
        hidden:
          description: "If B(true), the variable is not displayed on UI or Command line."
          type: bool
        required:
          description: "If the variable required?."
          type: bool
        options:
          description: "The list of possible values for this variable.  If type is B(integer) or B(date), then
            the array of string is  converted to array of integers or date during the runtime."
          type: list
          elements: str
        min_value:
          description: "The minimum value of the variable. Applicable for the integer type."
          type: int
        max_value:
          description: "The maximum value of the variable. Applicable for the integer type."
          type: int
        min_length:
          description: "The minimum length of the variable value. Applicable for the string type."
          type: int
        max_length:
          description: "The maximum length of the variable value. Applicable for the string type."
          type: int
        matches:
          description: "The regex for the variable value."
          type: str
        position:
          description: "The relative position of this variable in a list."
          type: int
        group_by:
          description: "The display name of the group this variable belongs to."
          type: str
        source:
          description: "The source of this meta-data."
          type: str
    link:
      description: "The reference link to the variable value By default the expression points to
        C($self.value)."
      type: str
  returned: on success for read operation
settings:
  description: "Environment variables for the Action."
  type: list
  elements: 'dict'
  contains:
    name:
      description: "The name of the variable. For example, C(name = \"inventory username\")."
      type: str
    value:
      description: "The value for the variable or reference to the value. For example, C(value =
        \"<provide your sshI(key)value with \\n>\"). B(Note) The SSH key should contain C(\\n)
        at the end of the key details in case of command line or API calls."
      type: str
    use_default:
      description: "True, will ignore the data in the value attribute, instead the data in
        metadata.default_value will be used."
      type: bool
    metadata:
      description: "An user editable metadata for the variables."
      type: dict
      contains:
        type:
          description: "Type of the variable."
          type: str
          choices:
            - 'boolean'
            - 'string'
            - 'integer'
            - 'date'
            - 'array'
            - 'list'
            - 'map'
            - 'complex'
            - 'link'
        aliases:
          description: "The list of aliases for the variable name."
          type: list
          elements: str
        description:
          description: "The description of the meta data."
          type: str
        cloud_data_type:
          description: "Cloud data type of the variable. eg. resource_group_id, region, vpc_id."
          type: str
        default_value:
          description: "Default value for the variable only if the override value is not specified."
          type: str
        link_status:
          description: "The status of the link."
          type: str
          choices:
            - 'normal'
            - 'broken'
        secure:
          description: "Is the variable secure or sensitive ?."
          type: bool
        immutable:
          description: "Is the variable readonly ?."
          type: bool
        hidden:
          description: "If B(true), the variable is not displayed on UI or Command line."
          type: bool
        required:
          description: "If the variable required?."
          type: bool
        options:
          description: "The list of possible values for this variable.  If type is B(integer) or B(date), then
            the array of string is  converted to array of integers or date during the runtime."
          type: list
          elements: str
        min_value:
          description: "The minimum value of the variable. Applicable for the integer type."
          type: int
        max_value:
          description: "The maximum value of the variable. Applicable for the integer type."
          type: int
        min_length:
          description: "The minimum length of the variable value. Applicable for the string type."
          type: int
        max_length:
          description: "The maximum length of the variable value. Applicable for the string type."
          type: int
        matches:
          description: "The regex for the variable value."
          type: str
        position:
          description: "The relative position of this variable in a list."
          type: int
        group_by:
          description: "The display name of the group this variable belongs to."
          type: str
        source:
          description: "The source of this meta-data."
          type: str
    link:
      description: "The reference link to the variable value By default the expression points to
        C($self.value)."
      type: str
  returned: on success for read operation
id:
  description: "Action ID."
  type: str
  returned: on success for read operation
crn:
  description: "Action Cloud Resource Name."
  type: str
  returned: on success for read operation
account:
  description: "Action account ID."
  type: str
  returned: on success for read operation
source_created_at:
  description: "Action Playbook Source creation time."
  type: str
  returned: on success for read operation
source_created_by:
  description: "E-mail address of user who created the Action Playbook Source."
  type: str
  returned: on success for read operation
source_updated_at:
  description: "The action playbook updation time."
  type: str
  returned: on success for read operation
source_updated_by:
  description: "E-mail address of user who updated the action playbook source."
  type: str
  returned: on success for read operation
created_at:
  description: "Action creation time."
  type: str
  returned: on success for read operation
created_by:
  description: "E-mail address of the user who created an action."
  type: str
  returned: on success for read operation
updated_at:
  description: "Action updation time."
  type: str
  returned: on success for read operation
updated_by:
  description: "E-mail address of the user who updated an action."
  type: str
  returned: on success for read operation
state:
  description: "Computed state of the Action."
  type: dict
  contains:
    status_code:
      description: "Status of automation (workspace or action)."
      type: str
      choices:
        - 'normal'
        - 'pending'
        - 'disabled'
        - 'critical'
    status_job_id:
      description: "Job id reference for this status."
      type: str
    status_message:
      description: "Automation status message - to be displayed along with the status_code."
      type: str
  returned: on success for read operation
playbook_names:
  description: "Playbook names retrieved from the repository."
  type: list
  elements: str
  returned: on success for read operation
sys_lock:
  description: "System lock status."
  type: dict
  contains:
    sys_locked:
      description: "Is the automation locked by a Schematic job ?."
      type: bool
    sys_locked_by:
      description: "Name of the User who performed the job, that lead to the locking of the automation."
      type: str
    sys_locked_at:
      description: "When the User performed the job that lead to locking of the automation ?."
      type: str
  returned: on success for read operation
git_token_ref:
  description: "secrets manager reference to git token."
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
        action_id=dict(
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

    action_id = module.params["action_id"]
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

    if action_id:
        # read
        try:
            response = sdk.get_action(
                action_id=action_id,
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
