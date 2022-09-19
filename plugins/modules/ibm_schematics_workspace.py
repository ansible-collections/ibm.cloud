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
module: ibm_schematics_workspace
short_description: Manage C(schematics_workspaces) for Schematics Service API.
author: Kavya Handadi (@kavya498)
version_added: "1.0.0"
description:
  - This module creates, updates, or deletes a C(schematics_workspace) resource for Schematics Service API.
requirements:
  - "SchematicsV1"
options:
  agent_id:
    description:
      - agent id which is binded to with the workspace.
    type: str
  description:
    description:
      - The description of the workspace.
    type: str
  type:
    description:
      - List of Workspace type.
    type: list
    elements: str
  applied_shareddata_ids:
    description:
      - List of applied shared dataset ID.
    type: list
    elements: str
  shared_data:
    description: |
      Information about the Target used by the templates originating from the IBM Cloud catalog offerings.
      This information is not relevant for workspace created using your own Terraform template.
    type: dict
    suboptions:
      cluster_created_on:
        description:
          - Cluster created on.
        type: str
      cluster_id:
        description: |
          The ID of the cluster where you want to provision the resources of all IBM Cloud catalog templates that are included in the catalog offering.
        type: str
      cluster_name:
        description:
          - The cluster name.
        type: str
      cluster_type:
        description:
          - The cluster type.
        type: str
      entitlement_keys:
        description:
          - The entitlement key that you want to use to install IBM Cloud entitled software.
        type: list
        elements: dict
      namespace:
        description: |
          The Kubernetes namespace or OpenShift project
          where the resources of all IBM Cloud catalog templates that are included in the catalog offering are deployed into.
        type: str
      region:
        description:
          - The IBM Cloud region that you want to use for the resources of all IBM Cloud catalog templates that are included in the catalog offering.
        type: str
      resource_group_id:
        description:
          - The ID of the resource group that you want to use for the resources of all IBM Cloud catalog templates that are included in the catalog offering.
        type: str
      worker_count:
        description:
          - The cluster worker count.
        type: int
      worker_machine_type:
        description:
          - The cluster worker type.
        type: str
  workspace_status_update_request_workspace_status:
    description:
      - Input to update the workspace status.
    type: dict
    suboptions:
      frozen:
        description:
          - If set to true, the workspace is frozen and changes to the workspace are disabled.
        type: bool
      frozen_at:
        description:
          - Frozen at.
        type: str
      frozen_by:
        description:
          - Frozen by.
        type: str
      locked:
        description:
          - Locked status.
        type: bool
      locked_by:
        description:
          - Locked by.
        type: str
      locked_time:
        description:
          - Locked at.
        type: str
  dependencies:
    description:
      - Workspace dependencies.
    type: dict
    suboptions:
      parents:
        description:
          - List of workspace parents CRN identifiers.
        type: list
        elements: str
      children:
        description:
          - List of workspace children CRN identifiers.
        type: list
        elements: str
  tags:
    description:
      - A list of tags that are associated with the workspace.
    type: list
    elements: str
  workspace_status:
    description:
      - WorkspaceStatusRequest -.
    type: dict
    suboptions:
      frozen:
        description:
          - If set to true, the workspace is frozen and changes to the workspace are disabled.
        type: bool
      frozen_at:
        description:
          - The timestamp when the workspace was frozen.
        type: str
      frozen_by:
        description:
          - The user ID that froze the workspace.
        type: str
      locked:
        description:
          - If set to true, the workspace is locked and disabled for changes.
        type: bool
      locked_by:
        description:
          - The user ID that initiated a resource-related job, such as applying or destroying resources, that locked the workspace.
        type: str
      locked_time:
        description:
          - The timestamp when the workspace was locked.
        type: str
  catalog_ref:
    description:
      - Information about the software template that you chose from the IBM Cloud catalog. This information is returned for IBM Cloud catalog offerings only.
    type: dict
    suboptions:
      dry_run:
        description:
          - Dry run.
        type: bool
      owning_account:
        description:
          - Owning account ID of the catalog.
        type: str
      item_icon_url:
        description:
          - The URL to the icon of the software template in the IBM Cloud catalog.
        type: str
      item_id:
        description:
          - The ID of the software template that you chose to install from the IBM Cloud catalog. This software is provisioned with Schematics.
        type: str
      item_name:
        description:
          - The name of the software that you chose to install from the IBM Cloud catalog.
        type: str
      item_readme_url:
        description:
          - The URL to the readme file of the software template in the IBM Cloud catalog.
        type: str
      item_url:
        description:
          - The URL to the software template in the IBM Cloud catalog.
        type: str
      launch_url:
        description:
          - The URL to the dashboard to access your software.
        type: str
      offering_version:
        description:
          - The version of the software template that you chose to install from the IBM Cloud catalog.
        type: str
  template_data:
    description:
      - Input data for the Template.
    type: list
    elements: dict
    suboptions:
      env_values:
        description: |
          A list of environment variables that you want to apply during the execution of a bash script or Terraform job.
          This field must be provided as a list of key-value pairs,
          for example, B(TFI(LOG=debug). Each entry will be a map with one entry where C(key is the environment variable name and value is value).
          You can define environment variables for IBM Cloud catalog offerings that are provisioned by using a bash script.
          See [example to use special environment variable](https://cloud.ibm.com/docs/schematics?topic=schematics-set-parallelism#parallelism-example)
          that are supported by Schematics.
        type: list
        elements: dict
      env_values_metadata:
        description:
          - Environment variables metadata.
        type: list
        elements: dict
        suboptions:
          hidden:
            description:
              - Environment variable is hidden.
            type: bool
          name:
            description:
              - Environment variable name.
            type: str
          secure:
            description:
              - Environment variable is secure.
            type: bool
      folder:
        description:
          - The subfolder in your GitHub or GitLab repository where your Terraform template is stored.
        type: str
      compact:
        description: |
          True, to use the files from the specified folder & subfolder in your GitHub or GitLab repository
          and ignore the other folders in the repository. For more information,
          see [Compact download for Schematics workspace](https://cloud.ibm.com/docs/schematics?topic=schematics-compact-download&interface=ui).
        type: bool
      init_state_file:
        description: |
          The content of an existing Terraform statefile that you want to import in to your workspace.
          To get the content of a Terraform statefile for a specific Terraform template in an existing workspace,
          run C(ibmcloud terraform state pull --id <workspaceI(id> --template <template)id>).
        type: str
      injectors:
        description:
          - Array of injectable terraform blocks.
        type: list
        elements: dict
        suboptions:
          tft_git_url:
            description:
              - Git repo url hosting terraform template files.
            type: str
          tft_git_token:
            description:
              - Token to access the git repository (Optional).
            type: str
          tft_prefix:
            description:
              - Optional prefix word to append to files (Optional).
            type: str
          injection_type:
            description:
              - Injection type. Default is 'override'.
            type: str
          tft_name:
            description:
              - Terraform template name. Maps to folder name in git repo.
            type: str
          tft_parameters:
            description:
              - tft parameters
            type: list
            elements: dict
            suboptions:
              name:
                description:
                  - Key name to replace.
                type: str
              value:
                description:
                  - Value to replace.
                type: str
      type:
        description: |
          The Terraform version that you want to use to run your Terraform code.
          Enter C(terraformI(v1.1)) to use Terraform version 1.1, and C(terraform)v1.0) to use Terraform version 1.0. This is a required variable.
          If the Terraform version is not specified, By default, Schematics selects the version from your template. For more information,
          refer to [Terraform version](https://cloud.ibm.com/docs/schematics?topic=schematics-workspace-setup&interface=ui#create-workspaceI(ui).
        type: str
      uninstall_script_name:
        description:
          - Uninstall script name.
        type: str
      values:
        description: |
          A list of variable values that you want to apply during the Helm chart installation.
          The list must be provided in JSON format.The values that you define here override the default Helm chart values.
          This field is supported only for IBM Cloud catalog offerings that are provisioned by using the Terraform Helm provider.
        type: str
      values_metadata:
        description:
          - List of values metadata.
        type: list
        elements: dict
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
      variablestore:
        description:
          - VariablesRequest -.
        type: list
        elements: dict
        suboptions:
          description:
            description:
              - The description of your input variable.
            type: str
          name:
            description:
              - The name of the variable.
            type: str
          secure:
            description:
              - If set to C(true), the value of your input variable is protected and not returned in your API response.
            type: bool
          type:
            description: |
              C(Terraform v0.11) supports C(string), C(list), C(map) data type.
              For more information, about the syntax, see [Configuring input variables](https://www.terraform.io/docs/configuration-0-11/variables.html).
              C(Terraform v0.12) additionally, supports C(bool), C(number) and complex data types such as
              C(list(type)), C(map(type)), C(object({attribute name=type,..})), C(set(type)), C(tuple([type])).
              For more information, about the syntax to use the complex data type,
              see [Configuring variables](https://www.terraform.io/docs/configuration/variables.html#type-constraints).
            type: str
          use_default:
            description:
              - Variable uses default value; and is not over-ridden.
            type: bool
          value:
            description: |
              Enter the value as a string for the primitive types such as C(bool), C(number), C(string), and C(HCL) format for the complex variables,
              as you provide in a C(.tfvars) file B(You need to enter escaped string of C(HCL) format for the complex variable value).
              For more information, about how to declare variables in a terraform configuration file and provide value to schematics,
              see [Providing values for the declared variables](https://cloud.ibm.com/docs/schematics?topic=schematics-create-tf-config#declare-variable).
            type: str
  resource_group:
    description:
      - The ID of the resource group where you want to provision the workspace.
    type: str
  template_repo:
    description:
      - Input variables for the Template repoository, while creating a workspace.
    type: dict
    suboptions:
      branch:
        description:
          - The repository branch.
        type: str
      release:
        description:
          - The repository release.
        type: str
      repo_sha_value:
        description:
          - The repository SHA value.
        type: str
      repo_url:
        description:
          - The repository URL.
        type: str
      url:
        description:
          - The source URL.
        type: str
  workspace_status_msg:
    description:
      - Information about the last job that ran against the workspace. -.
    type: dict
    suboptions:
      status_code:
        description:
          - The success or error code that was returned for the last plan, apply, or destroy job that ran against your workspace.
        type: str
      status_msg:
        description:
          - The success or error message that was returned for the last plan, apply, or destroy job that ran against your workspace.
        type: str
  template_ref:
    description:
      - Workspace template ref.
    type: str
  template_repo_update_request_template_repo:
    description:
      - Input to update the template repository data.
    type: dict
    suboptions:
      branch:
        description:
          - The repository branch.
        type: str
      release:
        description:
          - The repository release.
        type: str
      repo_sha_value:
        description:
          - The repository SHA value.
        type: str
      repo_url:
        description:
          - The repository URL.
        type: str
      url:
        description:
          - The source URL.
        type: str
  name:
    description: |
      The name of your workspace. The name can be up to 128 characters long and can include alphanumeric characters, spaces, dashes, and underscores.
      When you create a workspace for your own Terraform template,
      consider including the microservice component that you set up with your Terraform template and
      the IBM Cloud environment where you want to deploy your resources in your name.
    type: str
  location:
    description: |
      The location where you want to create your Schematics workspace and run the Schematics jobs.
      The location that you enter must match the API endpoint that you use.
      For example, if you use the Frankfurt API endpoint, you must specify C(eu-de) as your location.
      If you use an API endpoint for a geography and you do not specify a location, Schematics determines the location based on availability.
    type: str
  refresh_token:
    description: |
      The IAM refresh token for the user or service identity.
      The IAM refresh token is required only if you want to destroy the Terraform resources before deleting the Schematics workspace.
      If you want to delete the workspace only and keep all your Terraform resources, refresh token is not required.
      B(Retrieving refresh token)I( Use C(export IBMCLOUDI(API)KEY=<ibmcloudI(api)key>),
      and execute C(curl -X POST "https://iam.cloud.ibm.com/identity/token" -H "Content-Type: application/x-www-form-urlencoded"
      -d "grantI(type=urn:ibm:params:oauth:grant-type:apikey&apikey=$IBMCLOUD)APII(KEY" -u bx:bx).)
      For more information, about creating IAM access token and API Docs, refer, [IAM access token](/apidocs/iam-identity-token-api#gettoken-password)
      and [Create API key](/apidocs/iam-identity-token-api#create-api-key).
      B(Limitation) I( If the token is expired, you can use C(refresh token) to get a new IAM access token.)
      The C(refresh)token) parameter cannot be used to retrieve a new IAM access token.
      I( When the IAM access token is about to expire, use the API key to create a new access token.)
    type: str
  w_id:
    description:
      - The ID of the workspace.  To find the workspace ID, use the C(GET /v1/workspaces) API.
    type: str
  x_github_token:
    description:
      - The personal access token to authenticate with your private GitHub or GitLab repository and access your Terraform template.
    type: str
  destroy_resources:
    description: |
      If set to C(true), refreshI(token header configuration is required to delete all the Terraform resources, and the Schematics workspace.
      If set to C(false), you can remove only the workspace.
      Your Terraform resources are still available and must be managed with the resource dashboard or CLI.
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
- name: Create ibm_schematics_workspace
  vars:
    catalog_ref_model:
    dependencies_model:
    shared_target_data_model:
    environment_values_metadata_model:
    inject_terraform_template_inner_tft_parameters_item_model:
    inject_terraform_template_inner_model:
    variable_metadata_model:
    workspace_variable_request_model:
    template_source_data_request_model:
    template_repo_request_model:
    workspace_status_request_model:
  ibm_schematics_workspace:

- name: Update ibm_schematics_workspace
  vars:
    catalog_ref_model:
    dependencies_model:
    shared_target_data_model:
    environment_values_metadata_model:
    inject_terraform_template_inner_tft_parameters_item_model:
    inject_terraform_template_inner_model:
    variable_metadata_model:
    workspace_variable_request_model:
    template_source_data_request_model:
    template_repo_update_request_model:
    workspace_status_update_request_model:
    workspace_status_message_model:
  ibm_schematics_workspace:

- name: Delete ibm_schematics_workspace
  ibm_schematics_workspace:
'''

RETURN = '''
msg:
  description: |-
    A dictionary that represents the result.
    If a resource was created, a C(WorkspaceResponse) object is returned.
    If a resource was updated, a C(WorkspaceResponse) object is returned.
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
        agent_id=dict(
            type='str',
            required=False),
        description=dict(
            type='str',
            required=False),
        type=dict(
            type='list',
            elements='str',
            required=False),
        applied_shareddata_ids=dict(
            type='list',
            elements='str',
            required=False),
        # Represents the SharedTargetData Python class
        shared_data=dict(
            type='dict',
            options=dict(
                cluster_created_on=dict(
                    type='str',
                    required=False),
                cluster_id=dict(
                    type='str',
                    required=False),
                cluster_name=dict(
                    type='str',
                    required=False),
                cluster_type=dict(
                    type='str',
                    required=False),
                entitlement_keys=dict(
                    type='list',
                    elements='dict',
                    required=False),
                namespace=dict(
                    type='str',
                    required=False),
                region=dict(
                    type='str',
                    required=False),
                resource_group_id=dict(
                    type='str',
                    required=False),
                worker_count=dict(
                    type='int',
                    required=False),
                worker_machine_type=dict(
                    type='str',
                    required=False),
            ),
            required=False),
        # Represents the WorkspaceStatusUpdateRequest Python class
        workspace_status_update_request_workspace_status=dict(
            type='dict',
            options=dict(
                frozen=dict(
                    type='bool',
                    required=False),
                frozen_at=dict(
                    type='str',
                    required=False),
                frozen_by=dict(
                    type='str',
                    required=False),
                locked=dict(
                    type='bool',
                    required=False),
                locked_by=dict(
                    type='str',
                    required=False),
                locked_time=dict(
                    type='str',
                    required=False),
            ),
            required=False),
        # Represents the Dependencies Python class
        dependencies=dict(
            type='dict',
            options=dict(
                parents=dict(
                    type='list',
                    elements='str',
                    required=False),
                children=dict(
                    type='list',
                    elements='str',
                    required=False),
            ),
            required=False),
        tags=dict(
            type='list',
            elements='str',
            required=False),
        # Represents the WorkspaceStatusRequest Python class
        workspace_status=dict(
            type='dict',
            options=dict(
                frozen=dict(
                    type='bool',
                    required=False),
                frozen_at=dict(
                    type='str',
                    required=False),
                frozen_by=dict(
                    type='str',
                    required=False),
                locked=dict(
                    type='bool',
                    required=False),
                locked_by=dict(
                    type='str',
                    required=False),
                locked_time=dict(
                    type='str',
                    required=False),
            ),
            required=False),
        # Represents the CatalogRef Python class
        catalog_ref=dict(
            type='dict',
            options=dict(
                dry_run=dict(
                    type='bool',
                    required=False),
                owning_account=dict(
                    type='str',
                    required=False),
                item_icon_url=dict(
                    type='str',
                    required=False),
                item_id=dict(
                    type='str',
                    required=False),
                item_name=dict(
                    type='str',
                    required=False),
                item_readme_url=dict(
                    type='str',
                    required=False),
                item_url=dict(
                    type='str',
                    required=False),
                launch_url=dict(
                    type='str',
                    required=False),
                offering_version=dict(
                    type='str',
                    required=False),
            ),
            required=False),
        template_data=dict(
            type='list',
            elements='dict',
            options=dict(
                env_values=dict(
                    type='list',
                    elements='dict',
                    required=False),
                env_values_metadata=dict(
                    type='list',
                    elements='dict',
                    options=dict(
                        hidden=dict(
                            type='bool',
                            required=False),
                        name=dict(
                            type='str',
                            required=False),
                        secure=dict(
                            type='bool',
                            required=False),
                    ),
                    required=False),
                folder=dict(
                    type='str',
                    required=False),
                compact=dict(
                    type='bool',
                    required=False),
                init_state_file=dict(
                    type='str',
                    required=False),
                injectors=dict(
                    type='list',
                    elements='dict',
                    options=dict(
                        tft_git_url=dict(
                            type='str',
                            required=False),
                        tft_git_token=dict(
                            type='str',
                            required=False),
                        tft_prefix=dict(
                            type='str',
                            required=False),
                        injection_type=dict(
                            type='str',
                            required=False),
                        tft_name=dict(
                            type='str',
                            required=False),
                        tft_parameters=dict(
                            type='list',
                            elemets='dict',
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
                type=dict(
                    type='str',
                    required=False),
                uninstall_script_name=dict(
                    type='str',
                    required=False),
                values=dict(
                    type='str',
                    required=False),
                values_metadata=dict(
                    type='list',
                    elements='dict',
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
                variablestore=dict(
                    type='list',
                    elements='dict',
                    options=dict(
                        description=dict(
                            type='str',
                            required=False),
                        name=dict(
                            type='str',
                            required=False),
                        secure=dict(
                            type='bool',
                            required=False),
                        type=dict(
                            type='str',
                            required=False),
                        use_default=dict(
                            type='bool',
                            required=False),
                        value=dict(
                            type='str',
                            required=False),
                    ),
                    required=False),
            ),
            required=False),
        resource_group=dict(
            type='str',
            required=False),
        # Represents the TemplateRepoRequest Python class
        template_repo=dict(
            type='dict',
            options=dict(
                branch=dict(
                    type='str',
                    required=False),
                release=dict(
                    type='str',
                    required=False),
                repo_sha_value=dict(
                    type='str',
                    required=False),
                repo_url=dict(
                    type='str',
                    required=False),
                url=dict(
                    type='str',
                    required=False),
            ),
            required=False),
        # Represents the WorkspaceStatusMessage Python class
        workspace_status_msg=dict(
            type='dict',
            options=dict(
                status_code=dict(
                    type='str',
                    required=False),
                status_msg=dict(
                    type='str',
                    required=False),
            ),
            required=False),
        template_ref=dict(
            type='str',
            required=False),
        # Represents the TemplateRepoUpdateRequest Python class
        template_repo_update_request_template_repo=dict(
            type='dict',
            options=dict(
                branch=dict(
                    type='str',
                    required=False),
                release=dict(
                    type='str',
                    required=False),
                repo_sha_value=dict(
                    type='str',
                    required=False),
                repo_url=dict(
                    type='str',
                    required=False),
                url=dict(
                    type='str',
                    required=False),
            ),
            required=False),
        name=dict(
            type='str',
            required=False),
        location=dict(
            type='str',
            required=False),
        refresh_token=dict(
            type='str',
            required=False),
        w_id=dict(
            type='str',
            required=False),
        x_github_token=dict(
            type='str',
            required=False),
        destroy_resources=dict(
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

    agent_id = module.params["agent_id"]
    description = module.params["description"]
    type = module.params["type"]
    applied_shareddata_ids = module.params["applied_shareddata_ids"]
    shared_data = module.params["shared_data"]
    workspace_status_update_request_workspace_status = module.params[
        "workspace_status_update_request_workspace_status"]
    dependencies = module.params["dependencies"]
    tags = module.params["tags"]
    workspace_status = module.params["workspace_status"]
    catalog_ref = module.params["catalog_ref"]
    template_data = module.params["template_data"]
    resource_group = module.params["resource_group"]
    template_repo = module.params["template_repo"]
    workspace_status_msg = module.params["workspace_status_msg"]
    template_ref = module.params["template_ref"]
    template_repo_update_request_template_repo = module.params[
        "template_repo_update_request_template_repo"]
    name = module.params["name"]
    location = module.params["location"]
    refresh_token = module.params["refresh_token"]
    w_id = module.params["w_id"]
    x_github_token = module.params["x_github_token"]
    destroy_resources = module.params["destroy_resources"]
    state = module.params["state"]

    sdk = config.get_schematicsv1_sdk()

    resource_exists = True

    # Check for existence
    if w_id:
        try:
            sdk.get_workspace(
                w_id=w_id,
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
                sdk.delete_workspace(
                    refresh_token=refresh_token,
                    w_id=w_id,
                    destroy_resources=destroy_resources,
                )
            except ApiException as ex:
                module.fail_json(msg=ex.message)
            else:
                payload = {"id": w_id, "status": "deleted"}
                module.exit_json(changed=True, msg=payload)
        else:
            payload = {"id": w_id, "status": "not_found"}
            module.exit_json(changed=False, msg=payload)

    if state == "present":
        if not resource_exists:
            # Create path
            try:
                result = sdk.create_workspace(
                    applied_shareddata_ids=applied_shareddata_ids,
                    catalog_ref=catalog_ref,
                    dependencies=dependencies,
                    description=description,
                    location=location,
                    name=name,
                    resource_group=resource_group,
                    shared_data=shared_data,
                    tags=tags,
                    template_data=template_data,
                    template_ref=template_ref,
                    template_repo=template_repo,
                    type=type,
                    workspace_status=workspace_status,
                    agent_id=agent_id,
                    x_github_token=x_github_token,
                ).get_result()
            except ApiException as ex:
                module.fail_json(msg=ex.message)
            else:
                module.exit_json(changed=True, msg=result)
        else:
            # Update path
            try:
                result = sdk.update_workspace(
                    w_id=w_id,
                    catalog_ref=catalog_ref,
                    description=description,
                    dependencies=dependencies,
                    name=name,
                    shared_data=shared_data,
                    tags=tags,
                    template_data=template_data,
                    template_repo=template_repo_update_request_template_repo,
                    type=type,
                    workspace_status=workspace_status_update_request_workspace_status,
                    workspace_status_msg=workspace_status_msg,
                    agent_id=agent_id,
                ).get_result()
            except ApiException as ex:
                module.fail_json(msg=ex.message)
            else:
                module.exit_json(changed=True, msg=result)


def main():
    run_module()


if __name__ == '__main__':
    main()
