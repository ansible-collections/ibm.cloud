#!/usr/bin/python
# coding: utf-8

# (C) Copyright IBM Corp. 2024.
#
# GNU General Public License v3.0+ (see LICENSE or https://www.gnu.org/licenses/gpl-3.0.txt)

from __future__ import (absolute_import, division, print_function)
__metaclass__ = type


DOCUMENTATION = r'''
---
module: ibm_schematics_job_info
short_description: Manage C(schematics_job) for Schematics Service API.
author: Gannayak Pabra (@Gannayak0722)
version_added: "1.0.0"
description:
  - This module retrieves one or more C(schematics_job) for Schematics Service API.
requirements:
  - "SchematicsV1"
options:
  job_id:
    description: "Job Id. Use C(GET /v2/jobs) API to look up the Job Ids in your IBM Cloud account."
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
- name: Read ibm_schematics_job
  ibm_schematics_job_info:
    job_id: 'testString'
    profile: 'summary'
'''

RETURN = r'''
command_object:
  description: "Name of the Schematics automation resource."
  type: str
  choices:
    - "workspace"
    - "action"
    - "system"
    - "environment"
  returned: on success for read operation
command_object_id:
  description: "Job command object id (workspace-id, action-id)."
  type: str
  returned: on success for read operation
command_name:
  description: "Schematics job command name."
  type: str
  choices:
    - "workspace_plan"
    - "workspace_apply"
    - "workspace_destroy"
    - "workspace_refresh"
    - "ansible_playbook_run"
    - "ansible_playbook_check"
    - "create_action"
    - "put_action"
    - "patch_action"
    - "delete_action"
    - "system_key_enable"
    - "system_key_delete"
    - "system_key_disable"
    - "system_key_rotate"
    - "system_key_restore"
    - "create_workspace"
    - "put_workspace"
    - "patch_workspace"
    - "delete_workspace"
    - "create_cart"
    - "repository_process"
    - "terraform_commands"
  returned: on success for read operation
command_parameter:
  description: "Schematics job command parameter (playbook-name)."
  type: str
  returned: on success for read operation
command_options:
  description: "Command line options for the command."
  type: list
  elements: str
  returned: on success for read operation
inputs:
  description: "Job inputs used by Action or Workspace."
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
  description: "Environment variables used by the Job while performing Action or Workspace."
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
tags:
  description: "User defined tags, while running the job."
  type: list
  elements: str
  returned: on success for read operation
id:
  description: "Job ID."
  type: str
  returned: on success for read operation
name:
  description: "Job name, uniquely derived from the related Workspace or Action."
  type: str
  returned: on success for read operation
description:
  description: "The description of your job is derived from the related action or workspace.  The
    description can be up to 2048 characters long in size."
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
  description: "Resource-group name derived from the related Workspace or Action."
  type: str
  returned: on success for read operation
submitted_at:
  description: "Job submission time."
  type: str
  returned: on success for read operation
submitted_by:
  description: "Email address of user who submitted the job."
  type: str
  returned: on success for read operation
start_at:
  description: "Job start time."
  type: str
  returned: on success for read operation
end_at:
  description: "Job end time."
  type: str
  returned: on success for read operation
duration:
  description: "Duration of job execution; example 40 sec."
  type: str
  returned: on success for read operation
status:
  description: "Job Status."
  type: dict
  contains:
    position_in_queue:
      description: "Position of job in pending queue."
      type: float
    total_in_queue:
      description: "Total no. of jobs in pending queue."
      type: float
    workspace_job_status:
      description: "Workspace Job Status."
      type: dict
      contains:
        workspace_name:
          description: "Workspace name."
          type: str
        status_code:
          description: "Status of Jobs."
          type: str
          choices:
            - 'job_pending'
            - 'job_in_progress'
            - 'job_finished'
            - 'job_failed'
            - 'job_cancelled'
            - 'job_stopped'
            - 'job_stop_in_progress'
            - 'job_ready_to_execute'
        status_message:
          description: "Workspace job status message (eg. App1I(Setup)Pending, for a 'Setup' flow in the
            'App1' Workspace)."
          type: str
        flow_status:
          description: "Environment Flow JOB Status."
          type: dict
          contains:
            flow_id:
              description: "flow id."
              type: str
            flow_name:
              description: "flow name."
              type: str
            status_code:
              description: "Status of Jobs."
              type: str
              choices:
                - 'job_pending'
                - 'job_in_progress'
                - 'job_finished'
                - 'job_failed'
                - 'job_cancelled'
                - 'job_stopped'
                - 'job_stop_in_progress'
                - 'job_ready_to_execute'
            status_message:
              description: "Flow Job status message - to be displayed along with the status_code;."
              type: str
            workitems:
              description: "Environment's individual workItem status details;."
              type: list
              elements: 'dict'
              contains:
                workspace_id:
                  description: "Workspace id."
                  type: str
                workspace_name:
                  description: "workspace name."
                  type: str
                job_id:
                  description: "workspace job id."
                  type: str
                status_code:
                  description: "Status of Jobs."
                  type: str
                  choices:
                    - 'job_pending'
                    - 'job_in_progress'
                    - 'job_finished'
                    - 'job_failed'
                    - 'job_cancelled'
                    - 'job_stopped'
                    - 'job_stop_in_progress'
                    - 'job_ready_to_execute'
                status_message:
                  description: "workitem job status message;."
                  type: str
                updated_at:
                  description: "workitem job status updation timestamp."
                  type: str
            updated_at:
              description: "Job status updation timestamp."
              type: str
        template_status:
          description: "Workspace Flow Template job status."
          type: list
          elements: 'dict'
          contains:
            template_id:
              description: "Template Id."
              type: str
            template_name:
              description: "Template name."
              type: str
            flow_index:
              description: "Index of the template in the Flow."
              type: int
            status_code:
              description: "Status of Jobs."
              type: str
              choices:
                - 'job_pending'
                - 'job_in_progress'
                - 'job_finished'
                - 'job_failed'
                - 'job_cancelled'
                - 'job_stopped'
                - 'job_stop_in_progress'
                - 'job_ready_to_execute'
            status_message:
              description: "Template job status message (eg. VPCt1I(Apply)Pending, for a 'VPCt1' Template)."
              type: str
            updated_at:
              description: "Job status updation timestamp."
              type: str
        updated_at:
          description: "Job status updation timestamp."
          type: str
        commands:
          description: "List of terraform commands executed and their status."
          type: list
          elements: 'dict'
          contains:
            name:
              description: "Name of the command."
              type: str
            outcome:
              description: "outcome of the command."
              type: str
    action_job_status:
      description: "Action Job Status."
      type: dict
      contains:
        action_name:
          description: "Action name."
          type: str
        status_code:
          description: "Status of Jobs."
          type: str
          choices:
            - 'job_pending'
            - 'job_in_progress'
            - 'job_finished'
            - 'job_failed'
            - 'job_cancelled'
            - 'job_stopped'
            - 'job_stop_in_progress'
            - 'job_ready_to_execute'
        status_message:
          description: "Action Job status message - to be displayed along with the actionI(status)code."
          type: str
        bastion_status_code:
          description: "Status of Resources."
          type: str
          choices:
            - 'none'
            - 'ready'
            - 'processing'
            - 'error'
        bastion_status_message:
          description: "Bastion status message - to be displayed along with the bastionI(status)code;."
          type: str
        targets_status_code:
          description: "Status of Resources."
          type: str
          choices:
            - 'none'
            - 'ready'
            - 'processing'
            - 'error'
        targets_status_message:
          description: "Aggregated status message for all target resources,  to be displayed along with the
            targetsI(status)code;."
          type: str
        updated_at:
          description: "Job status updation timestamp."
          type: str
    system_job_status:
      description: "System Job Status."
      type: dict
      contains:
        system_status_message:
          description: "System job message."
          type: str
        system_status_code:
          description: "Status of Jobs."
          type: str
          choices:
            - 'job_pending'
            - 'job_in_progress'
            - 'job_finished'
            - 'job_failed'
            - 'job_cancelled'
            - 'job_stopped'
            - 'job_stop_in_progress'
            - 'job_ready_to_execute'
        schematics_resource_status:
          description: "job staus for each schematics resource."
          type: list
          elements: 'dict'
          contains:
            status_code:
              description: "Status of Jobs."
              type: str
              choices:
                - 'job_pending'
                - 'job_in_progress'
                - 'job_finished'
                - 'job_failed'
                - 'job_cancelled'
                - 'job_stopped'
                - 'job_stop_in_progress'
                - 'job_ready_to_execute'
            status_message:
              description: "system job status message."
              type: str
            schematics_resource_id:
              description: "id for each resource which is targeted as a part of system job."
              type: str
            updated_at:
              description: "Job status updation timestamp."
              type: str
        updated_at:
          description: "Job status updation timestamp."
          type: str
    flow_job_status:
      description: "Environment Flow JOB Status."
      type: dict
      contains:
        flow_id:
          description: "flow id."
          type: str
        flow_name:
          description: "flow name."
          type: str
        status_code:
          description: "Status of Jobs."
          type: str
          choices:
            - 'job_pending'
            - 'job_in_progress'
            - 'job_finished'
            - 'job_failed'
            - 'job_cancelled'
            - 'job_stopped'
            - 'job_stop_in_progress'
            - 'job_ready_to_execute'
        status_message:
          description: "Flow Job status message - to be displayed along with the status_code;."
          type: str
        workitems:
          description: "Environment's individual workItem status details;."
          type: list
          elements: 'dict'
          contains:
            workspace_id:
              description: "Workspace id."
              type: str
            workspace_name:
              description: "workspace name."
              type: str
            job_id:
              description: "workspace job id."
              type: str
            status_code:
              description: "Status of Jobs."
              type: str
              choices:
                - 'job_pending'
                - 'job_in_progress'
                - 'job_finished'
                - 'job_failed'
                - 'job_cancelled'
                - 'job_stopped'
                - 'job_stop_in_progress'
                - 'job_ready_to_execute'
            status_message:
              description: "workitem job status message;."
              type: str
            updated_at:
              description: "workitem job status updation timestamp."
              type: str
        updated_at:
          description: "Job status updation timestamp."
          type: str
  returned: on success for read operation
cart_order_data:
  description: "Contains the cart order data which can be used for different purpose for eg. service
    tagging."
  type: list
  elements: 'dict'
  contains:
    name:
      description: "Name of the property."
      type: str
    value:
      description: "Value of the property."
      type: str
    type:
      description: "Type of the values(string, int etc)."
      type: str
    usage_kind:
      description: "List of usage kind how the cart data can be used."
      type: list
      elements: str
      choices:
        - "servicetags"
  returned: on success for read operation
data:
  description: "Job data."
  type: dict
  contains:
    job_type:
      description: "Type of Job."
      type: str
      choices:
        - 'repo_download_job'
        - 'workspace_job'
        - 'action_job'
        - 'system_job'
        - 'flow-job'
    workspace_job_data:
      description: "Workspace Job data."
      type: dict
      contains:
        workspace_name:
          description: "Workspace name."
          type: str
        flow_id:
          description: "Flow Id."
          type: str
        flow_name:
          description: "Flow name."
          type: str
        inputs:
          description: "Input variables data used by the Workspace Job."
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
        outputs:
          description: "Output variables data from the Workspace Job."
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
        settings:
          description: "Environment variables used by all the templates in the Workspace."
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
        template_data:
          description: "Input / output data of the Template in the Workspace Job."
          type: list
          elements: 'dict'
          contains:
            template_id:
              description: "Template Id."
              type: str
            template_name:
              description: "Template name."
              type: str
            flow_index:
              description: "Index of the template in the Flow."
              type: int
            inputs:
              description: "Job inputs used by the Templates."
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
            outputs:
              description: "Job output from the Templates."
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
            settings:
              description: "Environment variables used by the template."
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
            updated_at:
              description: "Job status updation timestamp."
              type: str
        updated_at:
          description: "Job status updation timestamp."
          type: str
    action_job_data:
      description: "Action Job data."
      type: dict
      contains:
        action_name:
          description: "Flow name."
          type: str
        inputs:
          description: "Input variables data used by the Action Job."
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
        outputs:
          description: "Output variables data from the Action Job."
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
        settings:
          description: "Environment variables used by all the templates in the Action."
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
        updated_at:
          description: "Job status updation timestamp."
          type: str
        inventory_record:
          description: "Complete inventory definition details."
          type: dict
          contains:
            name:
              description: "The unique name of your Inventory.  The name can be up to 128 characters long and can
                include alphanumeric  characters, spaces, dashes, and underscores."
              type: str
            id:
              description: "Inventory id."
              type: str
            description:
              description: "The description of your Inventory.  The description can be up to 2048 characters long
                in size."
              type: str
            location:
              description: "List of locations supported by IBM Cloud Schematics service.  While creating your
                workspace or action, choose the right region, since it cannot be changed.  Note, this
                does not limit the location of the IBM Cloud resources, provisioned using Schematics."
              type: str
              choices:
                - 'us-south'
                - 'us-east'
                - 'eu-gb'
                - 'eu-de'
            resource_group:
              description: "Resource-group name for the Inventory definition.  By default, Inventory will be
                created in Default Resource Group."
              type: str
            created_at:
              description: "Inventory creation time."
              type: str
            created_by:
              description: "Email address of user who created the Inventory."
              type: str
            updated_at:
              description: "Inventory updation time."
              type: str
            updated_by:
              description: "Email address of user who updated the Inventory."
              type: str
            inventories_ini:
              description: "Input inventory of host and host group for the playbook,  in the .ini file format."
              type: str
            resource_queries:
              description: "Input resource queries that is used to dynamically generate  the inventory of host and
                host group for the playbook."
              type: list
              elements: str
        materialized_inventory:
          description: "Materialized inventory details used by the Action Job, in .ini format."
          type: str
    system_job_data:
      description: "Controls Job data."
      type: dict
      contains:
        key_id:
          description: "Key ID for which key event is generated."
          type: str
        schematics_resource_id:
          description: "List of the schematics resource id."
          type: list
          elements: str
        updated_at:
          description: "Job status updation timestamp."
          type: str
    flow_job_data:
      description: "Flow Job data."
      type: dict
      contains:
        flow_id:
          description: "Flow ID."
          type: str
        flow_name:
          description: "Flow Name."
          type: str
        workitems:
          description: "Job data used by each workitem Job."
          type: list
          elements: 'dict'
          contains:
            command_object_id:
              description: "command object id."
              type: str
            command_object_name:
              description: "command object name."
              type: str
            layers:
              description: "layer name."
              type: str
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
            inputs:
              description: "Input variables data for the workItem used in FlowJob."
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
            outputs:
              description: "Output variables for the workItem."
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
            settings:
              description: "Environment variables for the workItem."
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
            last_job:
              description: "Status of the last job executed by the workitem."
              type: dict
              contains:
                command_object:
                  description: "Name of the Schematics automation resource."
                  type: str
                  choices:
                    - 'workspace'
                    - 'action'
                    - 'system'
                    - 'environment'
                command_object_name:
                  description: "command object name (workspaceI(name/action)name)."
                  type: str
                command_object_id:
                  description: "Workitem command object id, maps to workspaceI(id or action)id."
                  type: str
                command_name:
                  description: "Schematics job command name."
                  type: str
                  choices:
                    - 'workspace_plan'
                    - 'workspace_apply'
                    - 'workspace_destroy'
                    - 'workspace_refresh'
                    - 'ansible_playbook_run'
                    - 'ansible_playbook_check'
                    - 'create_action'
                    - 'put_action'
                    - 'patch_action'
                    - 'delete_action'
                    - 'system_key_enable'
                    - 'system_key_delete'
                    - 'system_key_disable'
                    - 'system_key_rotate'
                    - 'system_key_restore'
                    - 'create_workspace'
                    - 'put_workspace'
                    - 'patch_workspace'
                    - 'delete_workspace'
                    - 'create_cart'
                    - 'repository_process'
                    - 'terraform_commands'
                job_id:
                  description: "Workspace job id."
                  type: str
                job_status:
                  description: "Status of Jobs."
                  type: str
                  choices:
                    - 'job_pending'
                    - 'job_in_progress'
                    - 'job_finished'
                    - 'job_failed'
                    - 'job_cancelled'
                    - 'job_stopped'
                    - 'job_stop_in_progress'
                    - 'job_ready_to_execute'
            updated_at:
              description: "Job status updation timestamp."
              type: str
        updated_at:
          description: "Job status updation timestamp."
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
log_summary:
  description: "Job log summary record."
  type: dict
  contains:
    job_id:
      description: "Workspace Id."
      type: str
    job_type:
      description: "Type of Job."
      type: str
      choices:
        - 'repo_download_job'
        - 'workspace_job'
        - 'action_job'
        - 'system_job'
        - 'flow_job'
    log_start_at:
      description: "Job log start timestamp."
      type: str
    log_analyzed_till:
      description: "Job log update timestamp."
      type: str
    elapsed_time:
      description: "Job log elapsed time (logI(analyzed)till - logI(start)at)."
      type: float
    log_errors:
      description: "Job log errors."
      type: list
      elements: 'dict'
      contains:
        error_code:
          description: "Error code in the Log."
          type: str
        error_msg:
          description: "Summary error message in the log."
          type: str
        error_count:
          description: "Number of occurrence."
          type: float
    repo_download_job:
      description: "Repo download Job log summary."
      type: dict
      contains:
        scanned_file_count:
          description: "Number of files scanned."
          type: float
        quarantined_file_count:
          description: "Number of files quarantined."
          type: float
        detected_filetype:
          description: "Detected template or data file type."
          type: str
        inputs_count:
          description: "Number of inputs detected."
          type: str
        outputs_count:
          description: "Number of outputs detected."
          type: str
    workspace_job:
      description: "Workspace Job log summary."
      type: dict
      contains:
        resources_add:
          description: "Number of resources add."
          type: float
        resources_modify:
          description: "Number of resources modify."
          type: float
        resources_destroy:
          description: "Number of resources destroy."
          type: float
    flow_job:
      description: "Flow Job log summary."
      type: dict
      contains:
        workitems_completed:
          description: "Number of workitems completed successfully."
          type: float
        workitems_pending:
          description: "Number of workitems pending in the flow."
          type: float
        workitems_failed:
          description: "Number of workitems failed."
          type: float
        workitems:
          description: "No description has been provided."
          type: list
          elements: 'dict'
          contains:
            workspace_id:
              description: "workspace ID."
              type: str
            job_id:
              description: "workspace JOB ID."
              type: str
            resources_add:
              description: "Number of resources add."
              type: float
            resources_modify:
              description: "Number of resources modify."
              type: float
            resources_destroy:
              description: "Number of resources destroy."
              type: float
            log_url:
              description: "Log url for job."
              type: str
    action_job:
      description: "Flow Job log summary."
      type: dict
      contains:
        target_count:
          description: "number of targets or hosts."
          type: float
        task_count:
          description: "number of tasks in playbook."
          type: float
        play_count:
          description: "number of plays in playbook."
          type: float
        recap:
          description: "Recap records."
          type: dict
          contains:
            target:
              description: "List of target or host name."
              type: list
              elements: str
            ok:
              description: "Number of OK."
              type: float
            changed:
              description: "Number of changed."
              type: float
            failed:
              description: "Number of failed."
              type: float
            skipped:
              description: "Number of skipped."
              type: float
            unreachable:
              description: "Number of unreachable."
              type: float
    system_job:
      description: "System Job log summary."
      type: dict
      contains:
        target_count:
          description: "number of targets or hosts."
          type: float
        success:
          description: "Number of passed."
          type: float
        failed:
          description: "Number of failed."
          type: float
  returned: on success for read operation
log_store_url:
  description: "Job log store URL."
  type: str
  returned: on success for read operation
state_store_url:
  description: "Job state store URL."
  type: str
  returned: on success for read operation
results_url:
  description: "Job results store URL."
  type: str
  returned: on success for read operation
updated_at:
  description: "Job status updation timestamp."
  type: str
  returned: on success for read operation
job_runner_id:
  description: "ID of the Job Runner."
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
        job_id=dict(
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

    job_id = module.params["job_id"]
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

    if job_id:
        # read
        try:
            response = sdk.get_job(
                job_id=job_id,
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
