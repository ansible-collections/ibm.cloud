#!/usr/bin/python
# coding: utf-8

# (C) Copyright IBM Corp. 2024.
#
# GNU General Public License v3.0+ (see LICENSE or https://www.gnu.org/licenses/gpl-3.0.txt)

from __future__ import (absolute_import, division, print_function)
__metaclass__ = type


DOCUMENTATION = r'''
---
module: ibm_schematics_workspace
short_description: Manage C(schematics_workspaces) for Schematics Service API.
author: Gannayak Pabra (@Gannayak0722)
version_added: "1.0.0"
description:
  - This module creates, updates, or deletes a C(schematics_workspace) resource for Schematics Service API.
requirements:
  - "SchematicsV1"
options:
  settings:
    description: "Input settings to be applied to the workspace, for example,
      C(jobI(timeout)override)."
    type: list
    elements: 'dict'
    suboptions:
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
        suboptions:
          type:
            description: "Type of the variable."
            type: str
            choices:
              - "boolean"
              - "string"
              - "integer"
              - "date"
              - "array"
              - "list"
              - "map"
              - "complex"
              - "link"
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
              - "normal"
              - "broken"
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
  agent_id:
    description: "agent id which is binded to with the workspace."
    type: str
  description:
    description: "The description of the workspace."
    type: str
  type:
    description: "List of Workspace type."
    type: list
    elements: str
  applied_shareddata_ids:
    description: "List of applied shared dataset ID."
    type: list
    elements: str
  shared_data:
    description: "Information about the Target used by the templates originating from the  IBM Cloud
      catalog offerings. This information is not relevant for workspace created using your
      own Terraform template."
    type: dict
    suboptions:
      cluster_created_on:
        description: "Cluster created on."
        type: str
      cluster_id:
        description: "The ID of the cluster where you want to provision the resources of all IBM Cloud
          catalog templates that are included in the catalog offering."
        type: str
      cluster_name:
        description: "The cluster name."
        type: str
      cluster_type:
        description: "The cluster type."
        type: str
      entitlement_keys:
        description: "The entitlement key that you want to use to install IBM Cloud entitled software."
        type: list
        elements: dict
      namespace:
        description: "The Kubernetes namespace or OpenShift project where the resources of all IBM Cloud
          catalog templates that are included in the catalog offering are deployed into."
        type: str
      region:
        description: "The IBM Cloud region that you want to use for the resources of all IBM Cloud catalog
          templates that are included in the catalog offering."
        type: str
      resource_group_id:
        description: "The ID of the resource group that you want to use for the resources of all IBM Cloud
          catalog templates that are included in the catalog offering."
        type: str
      worker_count:
        description: "The cluster worker count."
        type: int
      worker_machine_type:
        description: "The cluster worker type."
        type: str
  workspace_status_update_request_workspace_status:
    description: "Input to update the workspace status."
    type: dict
    suboptions:
      frozen:
        description: "If set to true, the workspace is frozen and changes to the workspace are disabled."
        type: bool
      frozen_at:
        description: "Frozen at."
        type: str
      frozen_by:
        description: "Frozen by."
        type: str
      locked:
        description: "Locked status."
        type: bool
      locked_by:
        description: "Locked by."
        type: str
      locked_time:
        description: "Locked at."
        type: str
  dependencies:
    description: "Workspace dependencies."
    type: dict
    suboptions:
      parents:
        description: "List of workspace parents CRN identifiers."
        type: list
        elements: str
      children:
        description: "List of workspace children CRN identifiers."
        type: list
        elements: str
  tags:
    description: "A list of tags that are associated with the workspace."
    type: list
    elements: str
  workspace_status:
    description: "WorkspaceStatusRequest -."
    type: dict
    suboptions:
      frozen:
        description: "If set to true, the workspace is frozen and changes to the workspace are disabled."
        type: bool
      frozen_at:
        description: "The timestamp when the workspace was frozen."
        type: str
      frozen_by:
        description: "The user ID that froze the workspace."
        type: str
      locked:
        description: "If set to true, the workspace is locked and disabled for changes."
        type: bool
      locked_by:
        description: "The user ID that initiated a resource-related job, such as applying or destroying
          resources, that locked the workspace."
        type: str
      locked_time:
        description: "The timestamp when the workspace was locked."
        type: str
  catalog_ref:
    description: "Information about the software template that you chose from the IBM Cloud catalog.
      This information is returned for IBM Cloud catalog offerings only."
    type: dict
    suboptions:
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
      offering_version:
        description: "The version of the software template that you chose to install from the IBM Cloud
          catalog."
        type: str
      service_extensions:
        description: "No description has been provided."
        type: list
        elements: 'dict'
        suboptions:
          name:
            description: "Name of the Service Data."
            type: str
          value:
            description: "Values of service data."
            type: raw
          type:
            description: "Type of the value string, int, bool."
            type: str
  template_data:
    description: "Input data for the Template."
    type: list
    elements: 'dict'
    suboptions:
      env_values:
        description: "A list of environment variables that you want to apply during the execution of a bash
          script or Terraform job. This field must be provided as a list of key-value pairs, for
          example, B(TF_LOG=debug). Each entry will be a map with one entry where C(key is the
          environment variable name and value is value). You can define environment variables
          for IBM Cloud catalog offerings that are provisioned by using a bash script. See
          [example to use special environment
          variable](https://cloud.ibm.com/docs/schematics?topic=schematics-set-parallelism#parallelism-example)
           that are supported by Schematics."
        type: list
        elements: dict
      env_values_metadata:
        description: "Environment variables metadata."
        type: list
        elements: 'dict'
        suboptions:
          hidden:
            description: "Environment variable is hidden."
            type: bool
          name:
            description: "Environment variable name."
            type: str
          secure:
            description: "Environment variable is secure."
            type: bool
      folder:
        description: "The subfolder in your GitHub or GitLab repository where your Terraform template is
          stored."
        type: str
      compact:
        description: "True, to use the files from the specified folder & subfolder in your GitHub or GitLab
          repository and ignore the other folders in the repository. For more information, see
          [Compact download for Schematics
          workspace](https://cloud.ibm.com/docs/schematics?topic=schematics-compact-download&interface=ui)."
        type: bool
      init_state_file:
        description: "The content of an existing Terraform statefile that you want to import in to your
          workspace. To get the content of a Terraform statefile for a specific Terraform
          template in an existing workspace, run C(ibmcloud terraform state pull --id
          <workspaceI(id> --template <template)id>)."
        type: str
      injectors:
        description: "Array of injectable terraform blocks."
        type: list
        elements: 'dict'
        suboptions:
          tft_git_url:
            description: "Git repo url hosting terraform template files."
            type: str
          tft_git_token:
            description: "Token to access the git repository (Optional)."
            type: str
          tft_prefix:
            description: "Optional prefix word to append to files (Optional)."
            type: str
          injection_type:
            description: "Injection type. Default is 'override'."
            type: str
          tft_name:
            description: "Terraform template name. Maps to folder name in git repo."
            type: str
          tft_parameters:
            description: "No description has been provided."
            type: list
            elements: 'dict'
            suboptions:
              name:
                description: "Key name to replace."
                type: str
              value:
                description: "Value to replace."
                type: str
      type:
        description: "The Terraform version that you want to use to run your Terraform code. Enter
          C(terraform_v1.1) to use Terraform version 1.1, and C(terraform_v1.0) to use Terraform
          version 1.0. This is a required variable. If the Terraform version is not specified,
          By default, Schematics selects the version from your template. For more information,
          refer to [Terraform
          version](https://cloud.ibm.com/docs/schematics?topic=schematics-workspace-setup&interface=ui#create-workspace_ui)."
        type: str
      uninstall_script_name:
        description: "Uninstall script name."
        type: str
      values:
        description: "A list of variable values that you want to apply during the Helm chart installation.
          The list must be provided in JSON format, such as C(\"autoscaling: enabled: true
          minReplicas: 2\"). The values that you define here override the default Helm chart
          values. This field is supported only for IBM Cloud catalog offerings that are
          provisioned by using the Terraform Helm provider."
        type: str
      values_metadata:
        description: "List of values metadata."
        type: list
        elements: dict
      variablestore:
        description: "VariablesRequest -."
        type: list
        elements: 'dict'
        suboptions:
          description:
            description: "The description of your input variable."
            type: str
          name:
            description: "The name of the variable."
            type: str
          secure:
            description: "If set to C(true), the value of your input variable is protected and not returned in
              your API response."
            type: bool
          type:
            description: "C(Terraform v0.11) supports C(string), C(list), C(map) data type. For more
              information, about the syntax, see [Configuring input
              variables](https://www.terraform.io/docs/configuration-0-11/variables.html).
              <br> C(Terraform v0.12) additionally, supports C(bool), C(number) and complex data
              types such as C(list(type)), C(map(type)),
              C(object({attribute name=type,..})), C(set(type)), C(tuple([type])). For more
              information, about the syntax to use the complex data type, see [Configuring
              variables](https://www.terraform.io/docs/configuration/variables.html#type-constraints)."
            type: str
          use_default:
            description: "Variable uses default value; and is not over-ridden."
            type: bool
          value:
            description: "Enter the value as a string for the primitive types such as C(bool), C(number),
              C(string), and C(HCL) format for the complex variables, as you provide in a C(.tfvars)
              file. B(You need to enter escaped string of C(HCL) format for the complex variable
              value). For more information, about how to declare variables in a terraform
              configuration file and provide value to schematics, see [Providing values for the
              declared
              variables](https://cloud.ibm.com/docs/schematics?topic=schematics-create-tf-config#declare-variable)."
            type: str
  resource_group:
    description: "The ID of the resource group where you want to provision the workspace."
    type: str
  template_repo:
    description: "Input variables for the Template repoository, while creating a workspace."
    type: dict
    suboptions:
      branch:
        description: "The repository branch."
        type: str
      release:
        description: "The repository release."
        type: str
      repo_sha_value:
        description: "The repository SHA value."
        type: str
      repo_url:
        description: "The repository URL."
        type: str
      url:
        description: "The source URL."
        type: str
  workspace_status_msg:
    description: "Information about the last job that ran against the workspace. -."
    type: dict
    suboptions:
      status_code:
        description: "The success or error code that was returned for the last plan, apply, or destroy job
          that ran against your workspace."
        type: str
      status_msg:
        description: "The success or error message that was returned for the last plan, apply, or destroy
          job that ran against your workspace."
        type: str
  template_ref:
    description: "Workspace template ref."
    type: str
  template_repo_update_request_template_repo:
    description: "Input to update the template repository data."
    type: dict
    suboptions:
      branch:
        description: "The repository branch."
        type: str
      release:
        description: "The repository release."
        type: str
      repo_sha_value:
        description: "The repository SHA value."
        type: str
      repo_url:
        description: "The repository URL."
        type: str
      url:
        description: "The source URL."
        type: str
  name:
    description: "The name of your workspace. The name can be up to 128 characters long and can
      include alphanumeric characters, spaces, dashes, and underscores. When you create a
      workspace for your own Terraform template, consider including the microservice
      component that you set up with your Terraform template and the IBM Cloud environment
      where you want to deploy your resources in your name."
    type: str
  location:
    description: "The location where you want to create your Schematics workspace and run the
      Schematics jobs. The location that you enter must match the API endpoint that you
      use. For example, if you use the Frankfurt API endpoint, you must specify C(eu-de)
      as your location. If you use an API endpoint for a geography and you do not specify
      a location, Schematics determines the location based on availability."
    type: str
  refresh_token:
    description: "The IAM refresh token for the user or service identity. The IAM refresh token is
      required only if you want to destroy the Terraform resources before deleting the
      Schematics workspace. If you want to delete the workspace only and keep all your
      Terraform resources, refresh token is not required.
        B(Retrieving refresh token):
        * Use C(export IBMCLOUD_API_KEY=<ibmcloud_api_key>), and execute C(curl -X POST
      \"https://iam.cloud.ibm.com/identity/token\" -H \"Content-Type:
      application/x-www-form-urlencoded\" -d
      \"grant_type=urn:ibm:params:oauth:grant-type:apikey&apikey=$IBMCLOUD_API_KEY\" -u
      bx:bx).
        * For more information, about creating IAM access token and API Docs, refer, [IAM
      access token](/apidocs/iam-identity-token-api#gettoken-password) and [Create API
      key](/apidocs/iam-identity-token-api#create-api-key).
        B(Limitation):
        * If the token is expired, you can use C(refresh token) to get a new IAM access
      token.
        * The C(refresh_token) parameter cannot be used to retrieve a new IAM access
      token.
        * When the IAM access token is about to expire, use the API key to create a new
      access token."
    type: str
  w_id:
    description: "The ID of the workspace.  To find the workspace ID, use the C(GET /v1/workspaces)
      API."
    type: str
  x_github_token:
    description: "The personal access token to authenticate with your private GitHub or GitLab
      repository and access your Terraform template."
    type: str
  destroy_resources:
    description: "If set to C(true), refresh_token header configuration is required to delete all the
      Terraform resources, and the Schematics workspace. If set to C(false), you can
      remove only the workspace. Your Terraform resources are still available and must be
      managed with the resource dashboard or CLI."
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
- name: Create ibm_schematics_workspace
  vars:
    service_extensions_model:
      name: 'flavor'
      value: 'testString'
      type: 'string'
    catalog_ref_model:
      dry_run: True
      owning_account: 'testString'
      item_icon_url: 'testString'
      item_id: 'testString'
      item_name: 'testString'
      item_readme_url: 'testString'
      item_url: 'testString'
      launch_url: 'testString'
      offering_version: 'testString'
      service_extensions: [service_extensions_model]
    dependencies_model:
      parents: ['testString']
      children: ['testString']
    shared_target_data_model:
      cluster_created_on: 'testString'
      cluster_id: 'testString'
      cluster_name: 'testString'
      cluster_type: 'testString'
      entitlement_keys: [{'anyKey': 'anyValue'}]
      namespace: 'testString'
      region: 'testString'
      resource_group_id: 'testString'
      worker_count: 26
      worker_machine_type: 'testString'
    environment_values_metadata_model:
      hidden: True
      name: 'testString'
      secure: True
    inject_terraform_template_inner_tft_parameters_item_model:
      name: 'testString'
      value: 'testString'
    inject_terraform_template_inner_model:
      tft_git_url: 'testString'
      tft_git_token: 'testString'
      tft_prefix: 'testString'
      injection_type: 'testString'
      tft_name: 'testString'
      tft_parameters: [inject_terraform_template_inner_tft_parameters_item_model]
    workspace_variable_request_model:
      description: 'testString'
      name: 'testString'
      secure: True
      type: 'testString'
      use_default: True
      value: 'testString'
    template_source_data_request_model:
      env_values: [{'anyKey': 'anyValue'}]
      env_values_metadata: [environment_values_metadata_model]
      folder: 'testString'
      compact: True
      init_state_file: 'testString'
      injectors: [inject_terraform_template_inner_model]
      type: 'testString'
      uninstall_script_name: 'testString'
      values: 'testString'
      values_metadata: [{'anyKey': 'anyValue'}]
      variablestore: [workspace_variable_request_model]
    template_repo_request_model:
      branch: 'testString'
      release: 'testString'
      repo_sha_value: 'testString'
      repo_url: 'testString'
      url: 'testString'
    workspace_status_request_model:
      frozen: True
      frozen_at: '2019-01-01T12:00:00.000Z'
      frozen_by: 'testString'
      locked: True
      locked_by: 'testString'
      locked_time: '2019-01-01T12:00:00.000Z'
    variable_metadata_model:
      type: 'boolean'
      aliases: ['testString']
      description: 'testString'
      cloud_data_type: 'testString'
      default_value: 'testString'
      link_status: 'normal'
      secure: True
      immutable: True
      hidden: True
      required: True
      options: ['testString']
      min_value: 38
      max_value: 38
      min_length: 38
      max_length: 38
      matches: 'testString'
      position: 38
      group_by: 'testString'
      source: 'testString'
    variable_data_model:
      name: 'testString'
      value: 'testString'
      use_default: True
      metadata: variable_metadata_model
  ibm_schematics_workspace:
    applied_shareddata_ids: ['testString']
    catalog_ref: '{{ catalog_ref_model }}'
    dependencies: '{{ dependencies_model }}'
    description: 'testString'
    location: 'testString'
    name: 'testString'
    resource_group: 'testString'
    shared_data: '{{ shared_target_data_model }}'
    tags: ['testString']
    template_data: [template_source_data_request_model]
    template_ref: 'testString'
    template_repo: '{{ template_repo_request_model }}'
    type: ['testString']
    workspace_status: '{{ workspace_status_request_model }}'
    agent_id: 'testString'
    settings: [variable_data_model]
    x_github_token: 'testString'
    state: present

- name: Update ibm_schematics_workspace
  vars:
    service_extensions_model:
      name: 'flavor'
      value: 'testString'
      type: 'string'
    catalog_ref_model:
      dry_run: True
      owning_account: 'testString'
      item_icon_url: 'testString'
      item_id: 'testString'
      item_name: 'testString'
      item_readme_url: 'testString'
      item_url: 'testString'
      launch_url: 'testString'
      offering_version: 'testString'
      service_extensions: [service_extensions_model]
    dependencies_model:
      parents: ['testString']
      children: ['testString']
    shared_target_data_model:
      cluster_created_on: 'testString'
      cluster_id: 'testString'
      cluster_name: 'testString'
      cluster_type: 'testString'
      entitlement_keys: [{'anyKey': 'anyValue'}]
      namespace: 'testString'
      region: 'testString'
      resource_group_id: 'testString'
      worker_count: 26
      worker_machine_type: 'testString'
    environment_values_metadata_model:
      hidden: True
      name: 'testString'
      secure: True
    inject_terraform_template_inner_tft_parameters_item_model:
      name: 'testString'
      value: 'testString'
    inject_terraform_template_inner_model:
      tft_git_url: 'testString'
      tft_git_token: 'testString'
      tft_prefix: 'testString'
      injection_type: 'testString'
      tft_name: 'testString'
      tft_parameters: [inject_terraform_template_inner_tft_parameters_item_model]
    workspace_variable_request_model:
      description: 'testString'
      name: 'testString'
      secure: True
      type: 'testString'
      use_default: True
      value: 'testString'
    template_source_data_request_model:
      env_values: [{'anyKey': 'anyValue'}]
      env_values_metadata: [environment_values_metadata_model]
      folder: 'testString'
      compact: True
      init_state_file: 'testString'
      injectors: [inject_terraform_template_inner_model]
      type: 'testString'
      uninstall_script_name: 'testString'
      values: 'testString'
      values_metadata: [{'anyKey': 'anyValue'}]
      variablestore: [workspace_variable_request_model]
    template_repo_update_request_model:
      branch: 'testString'
      release: 'testString'
      repo_sha_value: 'testString'
      repo_url: 'testString'
      url: 'testString'
    workspace_status_update_request_model:
      frozen: True
      frozen_at: '2019-01-01T12:00:00.000Z'
      frozen_by: 'testString'
      locked: True
      locked_by: 'testString'
      locked_time: '2019-01-01T12:00:00.000Z'
    workspace_status_message_model:
      status_code: 'testString'
      status_msg: 'testString'
    variable_metadata_model:
      type: 'boolean'
      aliases: ['testString']
      description: 'testString'
      cloud_data_type: 'testString'
      default_value: 'testString'
      link_status: 'normal'
      secure: True
      immutable: True
      hidden: True
      required: True
      options: ['testString']
      min_value: 38
      max_value: 38
      min_length: 38
      max_length: 38
      matches: 'testString'
      position: 38
      group_by: 'testString'
      source: 'testString'
    variable_data_model:
      name: 'testString'
      value: 'testString'
      use_default: True
      metadata: variable_metadata_model
  ibm_schematics_workspace:
    w_id: 'testString'
    catalog_ref: '{{ catalog_ref_model }}'
    description: 'testString'
    dependencies: '{{ dependencies_model }}'
    name: 'testString'
    shared_data: '{{ shared_target_data_model }}'
    tags: ['testString']
    template_data: [template_source_data_request_model]
    template_repo_update_request_template_repo: '{{ template_repo_update_request_model }}'
    type: ['testString']
    workspace_status_update_request_workspace_status: '{{ workspace_status_update_request_model }}'
    workspace_status_msg: '{{ workspace_status_message_model }}'
    agent_id: 'testString'
    settings: [variable_data_model]
    state: present

- name: Delete ibm_schematics_workspace
  ibm_schematics_workspace:
    refresh_token: 'testString'
    w_id: 'testString'
    destroy_resources: 'testString'
    state: absent
'''

RETURN = r'''
applied_shareddata_ids:
  description: "List of applied shared dataset ID."
  type: list
  elements: str
  returned: on success for create, update operations
catalog_ref:
  description: "Information about the software template that you chose from the IBM Cloud catalog.
    This information is returned for IBM Cloud catalog offerings only."
  type: dict
  contains:
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
    offering_version:
      description: "The version of the software template that you chose to install from the IBM Cloud
        catalog."
      type: str
    service_extensions:
      description: "No description has been provided."
      type: list
      elements: 'dict'
      contains:
        name:
          description: "Name of the Service Data."
          type: str
        value:
          description: "Values of service data."
          type: dict
        type:
          description: "Type of the value string, int, bool."
          type: str
  returned: on success for create, update operations
created_at:
  description: "The timestamp when the workspace was created."
  type: str
  returned: on success for create, update operations
created_by:
  description: "The user ID that created the workspace."
  type: str
  returned: on success for create, update operations
crn:
  description: "The workspace CRN."
  type: str
  returned: on success for create, update operations
dependencies:
  description: "Workspace dependencies."
  type: dict
  contains:
    parents:
      description: "List of workspace parents CRN identifiers."
      type: list
      elements: str
    children:
      description: "List of workspace children CRN identifiers."
      type: list
      elements: str
  returned: on success for create, update operations
description:
  description: "The description of the workspace."
  type: str
  returned: on success for create, update operations
id:
  description: "The unique identifier of the workspace."
  type: str
  returned: on success for create, update, delete operations
last_health_check_at:
  description: "The timestamp when the last health check was performed by Schematics."
  type: str
  returned: on success for create, update operations
location:
  description: "The IBM Cloud location where your workspace was provisioned."
  type: str
  returned: on success for create, update operations
name:
  description: "The name of the workspace."
  type: str
  returned: on success for create, update operations
resource_group:
  description: "The resource group the workspace was provisioned in."
  type: str
  returned: on success for create, update operations
runtime_data:
  description: "Information about the provisioning engine, state file, and runtime logs."
  type: list
  elements: 'dict'
  contains:
    engine_cmd:
      description: "The command that was used to apply the Terraform template or IBM Cloud catalog
        software template."
      type: str
    engine_name:
      description: "The provisioning engine that was used to apply the Terraform template or IBM Cloud
        catalog software template."
      type: str
    engine_version:
      description: "The version of the provisioning engine that was used."
      type: str
    id:
      description: "The ID that was assigned to your Terraform template or IBM Cloud catalog software
        template."
      type: str
    log_store_url:
      description: "The URL to access the logs that were created during the creation, update, or deletion
        of your IBM Cloud resources."
      type: str
    output_values:
      description: "List of Output values."
      type: list
      elements: dict
    resources:
      description: "List of resources."
      type: list
      elements: list
    state_store_url:
      description: "The URL where the Terraform statefile (C(terraform.tfstate)) is stored. You can use
        the statefile to find an overview of IBM Cloud resources that were created by
        Schematics. Schematics uses the statefile as an inventory list to determine future
        create, update, or deletion jobs."
      type: str
  returned: on success for create, update operations
shared_data:
  description: "Information about the Target used by the templates originating from IBM Cloud catalog
    offerings. This information is not relevant when you create a workspace from your own
    Terraform template."
  type: dict
  contains:
    cluster_id:
      description: "The ID of the cluster where you want to provision the resources of all IBM Cloud
        catalog templates that are included in the catalog offering."
      type: str
    cluster_name:
      description: "Target cluster name."
      type: str
    entitlement_keys:
      description: "The entitlement key that you want to use to install IBM Cloud entitled software."
      type: list
      elements: dict
    namespace:
      description: "The Kubernetes namespace or OpenShift project where the resources of all IBM Cloud
        catalog templates that are included in the catalog offering are deployed into."
      type: str
    region:
      description: "The IBM Cloud region that you want to use for the resources of all IBM Cloud catalog
        templates that are included in the catalog offering."
      type: str
    resource_group_id:
      description: "The ID of the resource group that you want to use for the resources of all IBM Cloud
        catalog templates that are included in the catalog offering."
      type: str
  returned: on success for create, update operations
schematics_workspace_status:
  description: "The status of the workspace.
      B(Active): After you successfully ran your infrastructure code by applying your
    Terraform execution plan, the state of your workspace changes to C(Active).
      B(Connecting): Schematics tries to connect to the template in your source repo. If
    successfully connected, the template is downloaded and metadata, such as input
    parameters, is extracted. After the template is downloaded, the state of the workspace
    changes to C(Scanning).
      B(Draft): The workspace is created without a reference to a GitHub or GitLab
    repository.
      B(Failed): If errors occur during the execution of your infrastructure code in IBM
    Cloud Schematics, your workspace status is set to C(Failed).
      B(Inactive): The Terraform template was scanned successfully and the workspace
    creation is complete. You can now start running Schematics plan and apply jobs to
    provision the IBM Cloud resources that you specified in your template. If you have an
    C(Active) workspace and decide to remove all your resources, your workspace is set to
    C(Inactive) after all your resources are removed.
      B(In progress): When you instruct IBM Cloud Schematics to run your infrastructure
    code by applying your Terraform execution plan, the status of our workspace changes to
    C(In progress).
      B(Scanning): The download of the Terraform template is complete and vulnerability
    scanning started. If the scan is successful, the workspace state changes to
    C(Inactive). If errors in your template are found, the state changes to C(Template
    Error).
      B(Stopped): The Schematics plan, apply, or destroy job was cancelled manually.
      B(Template Error): The Schematics template contains errors and cannot be processed."
  type: str
  returned: on success for create, update operations
tags:
  description: "A list of tags that are associated with the workspace."
  type: list
  elements: str
  returned: on success for create, update operations
template_data:
  description: "Information about the Terraform or IBM Cloud software template that you want to use."
  type: list
  elements: 'dict'
  contains:
    env_values:
      description: "List of environment values."
      type: list
      elements: 'dict'
      contains:
        hidden:
          description: "Environment variable is hidden."
          type: bool
        name:
          description: "Environment variable name."
          type: str
        secure:
          description: "Environment variable is secure."
          type: bool
        value:
          description: "Value for environment variable."
          type: str
    folder:
      description: "The subfolder in your GitHub or GitLab repository where your Terraform template is
        stored. If your template is stored in the root directory, C(.) is returned."
      type: str
    compact:
      description: "True, to use the files from the specified folder & subfolder in your GitHub or GitLab
        repository and ignore the other folders in the repository."
      type: bool
    has_githubtoken:
      description: "Has github token."
      type: bool
    id:
      description: "The ID that was assigned to your Terraform template or IBM Cloud catalog software
        template."
      type: str
    type:
      description: "The Terraform version that was used to run your Terraform code."
      type: str
    uninstall_script_name:
      description: "Uninstall script name."
      type: str
    values:
      description: "A list of variable values that you want to apply during the Helm chart installation.
        The list must be provided in JSON format, such as C(\"autoscaling: enabled: true
        minReplicas: 2\"). The values that you define here override the default Helm chart
        values. This field is supported only for IBM Cloud catalog offerings that are
        provisioned by using the Terraform Helm provider."
      type: str
    values_metadata:
      description: "A list of input variables that are associated with the workspace."
      type: list
      elements: dict
    values_url:
      description: "The API endpoint to access the input variables that you defined for your template."
      type: str
    variablestore:
      description: "Information about the input variables that your template uses."
      type: list
      elements: 'dict'
      contains:
        description:
          description: "The description of your input variable."
          type: str
        name:
          description: "The name of the variable."
          type: str
        secure:
          description: "If set to C(true), the value of your input variable is protected and not returned in
            your API response."
          type: bool
        type:
          description: "C(Terraform v0.11) supports C(string), C(list), C(map) data type. For more
            information, about the syntax, see [Configuring input
            variables](https://www.terraform.io/docs/configuration-0-11/variables.html).
            <br> C(Terraform v0.12) additionally, supports C(bool), C(number) and complex data
            types such as C(list(type)), C(map(type)),
            C(object({attribute name=type,..})), C(set(type)), C(tuple([type])). For more
            information, about the syntax to use the complex data type, see [Configuring
            variables](https://www.terraform.io/docs/configuration/variables.html#type-constraints)."
          type: str
        value:
          description: "Enter the value as a string for the primitive types such as C(bool), C(number),
            C(string), and C(HCL) format for the complex variables, as you provide in a C(.tfvars)
            file. B(You need to enter escaped string of C(HCL) format for the complex variable
            value). For more information, about how to declare variables in a terraform
            configuration file and provide value to schematics, see [Providing values for the
            declared
            variables](https://cloud.ibm.com/docs/schematics?topic=schematics-create-tf-config#declare-variable)."
          type: str
  returned: on success for create, update operations
template_ref:
  description: "Workspace template reference."
  type: str
  returned: on success for create, update operations
template_repo:
  description: "Information about the Template repository used by the workspace."
  type: dict
  contains:
    branch:
      description: "The repository branch."
      type: str
    full_url:
      description: "Full repository URL."
      type: str
    has_uploadedgitrepotar:
      description: "Has uploaded Git repository tar."
      type: bool
    release:
      description: "The repository release."
      type: str
    repo_sha_value:
      description: "The repository SHA value."
      type: str
    repo_url:
      description: "The repository URL. For more information, about using C(.netrc) in C(env_values), see
        [Usage of private module
        template](https://cloud.ibm.com/docs/schematics?topic=schematics-download-modules-pvt-git)."
      type: str
    url:
      description: "The source URL."
      type: str
  returned: on success for create, update operations
type:
  description: "The Terraform version that was used to run your Terraform code."
  type: list
  elements: str
  returned: on success for create, update operations
updated_at:
  description: "The timestamp when the workspace was last updated."
  type: str
  returned: on success for create, update operations
updated_by:
  description: "The user ID that updated the workspace."
  type: str
  returned: on success for create, update operations
cart_id:
  description: "The associate cart order ID."
  type: str
  returned: on success for create, update operations
project_id:
  description: "The associate project ID."
  type: str
  returned: on success for create, update operations
last_action_name:
  description: "Name of the last Action performed on workspace."
  type: str
  returned: on success for create, update operations
last_activity_id:
  description: "ID of last Activity performed."
  type: str
  returned: on success for create, update operations
last_job:
  description: "Last job details."
  type: dict
  contains:
    job_id:
      description: "ID of last job."
      type: str
    job_name:
      description: "Name of the last job."
      type: str
    job_status:
      description: "Status of the last job."
      type: str
  returned: on success for create, update operations
workspace_status:
  description: "Response that indicate the status of the workspace as either frozen or locked."
  type: dict
  contains:
    frozen:
      description: "If set to true, the workspace is frozen and changes to the workspace are disabled."
      type: bool
    frozen_at:
      description: "The timestamp when the workspace was frozen."
      type: str
    frozen_by:
      description: "The user ID that froze the workspace."
      type: str
    locked:
      description: "If set to true, the workspace is locked and disabled for changes."
      type: bool
    locked_by:
      description: "The user ID that initiated a resource-related job, such as applying or destroying
        resources, that locked the workspace."
      type: str
    locked_time:
      description: "The timestamp when the workspace was locked."
      type: str
  returned: on success for create, update operations
workspace_status_msg:
  description: "Information about the last job that ran against the workspace. -."
  type: dict
  contains:
    status_code:
      description: "The success or error code that was returned for the last plan, apply, or destroy job
        that ran against your workspace."
      type: str
    status_msg:
      description: "The success or error message that was returned for the last plan, apply, or destroy
        job that ran against your workspace."
      type: str
  returned: on success for create, update operations
agent:
  description: "Agent name, Agent id and associated policy ID information."
  type: dict
  contains:
    id:
      description: "ID of the Agent bound to the schematics object (workspace, action)."
      type: str
    name:
      description: "Name of the Agent bound to the schematics object."
      type: str
    assignment_policy_id:
      description: "ID of the agent assignment policy, that is used to bind the Agent to schematics
        object."
      type: str
  returned: on success for create, update operations
settings:
  description: "Input settings to be applied to the workspace, for example, C(jobI(timeout)override)."
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
  returned: on success for create, update operations
git_token_ref:
  description: "secrets manager reference to git token."
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
                            choices=[
                                'boolean',
                                'string',
                                'integer',
                                'date',
                                'array',
                                'list',
                                'map',
                                'complex',
                                'link',
                            ],
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
                            choices=[
                                'normal',
                                'broken',
                            ],
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
                    no_log=True,
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
                service_extensions=dict(
                    type='list',
                    elements='dict',
                    options=dict(
                        name=dict(
                            type='str',
                            required=False),
                        value=dict(
                            type='raw',
                            required=False),
                        type=dict(
                            type='str',
                            required=False),
                    ),
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
                            no_log=True,
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
            no_log=True,
            required=False),
        w_id=dict(
            type='str',
            required=False),
        x_github_token=dict(
            type='str',
            no_log=True,
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

    if MISSING_IMPORT_EXC is not None:
        module.fail_json(msg='Missing required import: ' + MISSING_IMPORT_EXC.msg)

    settings = module.params["settings"]
    agent_id = module.params["agent_id"]
    description = module.params["description"]
    type = module.params["type"]
    applied_shareddata_ids = module.params["applied_shareddata_ids"]
    shared_data = module.params["shared_data"]
    workspace_status_update_request_workspace_status = module.params["workspace_status_update_request_workspace_status"]
    dependencies = module.params["dependencies"]
    tags = module.params["tags"]
    workspace_status = module.params["workspace_status"]
    catalog_ref = module.params["catalog_ref"]
    template_data = module.params["template_data"]
    resource_group = module.params["resource_group"]
    template_repo = module.params["template_repo"]
    workspace_status_msg = module.params["workspace_status_msg"]
    template_ref = module.params["template_ref"]
    template_repo_update_request_template_repo = module.params["template_repo_update_request_template_repo"]
    name = module.params["name"]
    location = module.params["location"]
    refresh_token = module.params["refresh_token"]
    w_id = module.params["w_id"]
    x_github_token = module.params["x_github_token"]
    destroy_resources = module.params["destroy_resources"]
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
                module.exit_json(changed=True, id=w_id, status="deleted")
        else:
            module.exit_json(changed=False, id=w_id, status="not_found")

    if state == "present":
        if not resource_exists:
            # Create path
            try:
                response = sdk.create_workspace(
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
                    settings=settings,
                    x_github_token=x_github_token,
                )
            except ApiException as ex:
                module.fail_json(msg=ex.message)
            else:
                result = response.get_result()
                if 'status' in result:
                    result['schematics_workspace_status'] = result['status']
                    del result['status']

                module.exit_json(changed=True, **result)
        else:
            # Update path
            try:
                response = sdk.update_workspace(
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
                    settings=settings,
                )
            except ApiException as ex:
                module.fail_json(msg=ex.message)
            else:
                result = response.get_result()
                if 'status' in result:
                    result['schematics_workspace_status'] = result['status']
                    del result['status']

                module.exit_json(changed=True, **result)


def main():
    run_module()


if __name__ == '__main__':
    main()
