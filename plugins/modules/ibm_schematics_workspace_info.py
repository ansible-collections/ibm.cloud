#!/usr/bin/python
# coding: utf-8

# (C) Copyright IBM Corp. 2024.
#
# GNU General Public License v3.0+ (see LICENSE or https://www.gnu.org/licenses/gpl-3.0.txt)

from __future__ import (absolute_import, division, print_function)
__metaclass__ = type


DOCUMENTATION = r'''
---
module: ibm_schematics_workspace_info
short_description: Manage C(schematics_workspace) for Schematics Service API.
author: Gannayak Pabra (@Gannayak0722)
version_added: "1.0.0"
description:
  - This module retrieves one or more C(schematics_workspace) for Schematics Service API.
requirements:
  - "SchematicsV1"
options:
  w_id:
    description: "The ID of the workspace.  To find the workspace ID, use the C(GET /v1/workspaces)
      API."
    type: str
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
- name: Read ibm_schematics_workspace
  ibm_schematics_workspace_info:
    w_id: 'testString'
'''

RETURN = r'''
applied_shareddata_ids:
  description: "List of applied shared dataset ID."
  type: list
  elements: str
  returned: on success for read operation
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
  returned: on success for read operation
created_at:
  description: "The timestamp when the workspace was created."
  type: str
  returned: on success for read operation
created_by:
  description: "The user ID that created the workspace."
  type: str
  returned: on success for read operation
crn:
  description: "The workspace CRN."
  type: str
  returned: on success for read operation
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
  returned: on success for read operation
description:
  description: "The description of the workspace."
  type: str
  returned: on success for read operation
id:
  description: "The unique identifier of the workspace."
  type: str
  returned: on success for read operation
last_health_check_at:
  description: "The timestamp when the last health check was performed by Schematics."
  type: str
  returned: on success for read operation
location:
  description: "The IBM Cloud location where your workspace was provisioned."
  type: str
  returned: on success for read operation
name:
  description: "The name of the workspace."
  type: str
  returned: on success for read operation
resource_group:
  description: "The resource group the workspace was provisioned in."
  type: str
  returned: on success for read operation
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
  returned: on success for read operation
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
  returned: on success for read operation
status:
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
  returned: on success for read operation
tags:
  description: "A list of tags that are associated with the workspace."
  type: list
  elements: str
  returned: on success for read operation
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
  returned: on success for read operation
template_ref:
  description: "Workspace template reference."
  type: str
  returned: on success for read operation
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
  returned: on success for read operation
type:
  description: "The Terraform version that was used to run your Terraform code."
  type: list
  elements: str
  returned: on success for read operation
updated_at:
  description: "The timestamp when the workspace was last updated."
  type: str
  returned: on success for read operation
updated_by:
  description: "The user ID that updated the workspace."
  type: str
  returned: on success for read operation
cart_id:
  description: "The associate cart order ID."
  type: str
  returned: on success for read operation
project_id:
  description: "The associate project ID."
  type: str
  returned: on success for read operation
last_action_name:
  description: "Name of the last Action performed on workspace."
  type: str
  returned: on success for read operation
last_activity_id:
  description: "ID of last Activity performed."
  type: str
  returned: on success for read operation
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
  returned: on success for read operation
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
  returned: on success for read operation
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
  returned: on success for read operation
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
  returned: on success for read operation
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
        w_id=dict(
            type='str',
            required=False),
    )

    module = AnsibleModule(
        argument_spec=module_args,
        supports_check_mode=True
    )

    if MISSING_IMPORT_EXC is not None:
        module.fail_json(msg='Missing required import: ' + MISSING_IMPORT_EXC.msg)

    w_id = module.params["w_id"]

    if module.check_mode:
        module.exit_json(msg='The module would run with the following parameters: ' + module.paramss)

    authenticator = get_authenticator(service_name='schematics')
    if authenticator is None:
        module.fail_json(msg='Cannot create the authenticator.')

    sdk = SchematicsV1(
        authenticator=authenticator,
    )

    sdk.configure_service('schematics')

    if w_id:
        # read
        try:
            response = sdk.get_workspace(
                w_id=w_id,
            )

            result = response.get_result()

            module.exit_json(**result)
        except ApiException as ex:
            module.fail_json(msg=ex.message)


def main():
    run_module()


if __name__ == '__main__':
    main()
