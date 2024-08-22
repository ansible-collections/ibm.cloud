#!/usr/bin/python
# coding: utf-8

# (C) Copyright IBM Corp. 2024.
#
# GNU General Public License v3.0+ (see LICENSE or https://www.gnu.org/licenses/gpl-3.0.txt)

from __future__ import (absolute_import, division, print_function)
__metaclass__ = type


DOCUMENTATION = r'''
---
module: ibm_schematics_job
short_description: Manage C(schematics_jobs) for Schematics Service API.
author: Gannayak Pabra (@Gannayak0722)
version_added: "1.0.0"
description:
  - This module creates, updates, or deletes a C(schematics_job) resource for Schematics Service API.
requirements:
  - "SchematicsV1"
options:
  settings:
    description: "Environment variables used by the Job while performing Action or Workspace."
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
  agent:
    description: "Agent name, Agent id and associated policy ID information."
    type: dict
    suboptions:
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
  data:
    description: "Job data."
    type: dict
    suboptions:
      job_type:
        description: "Type of Job."
        type: str
        choices:
          - "repo_download_job"
          - "workspace_job"
          - "action_job"
          - "system_job"
          - "flow-job"
      workspace_job_data:
        description: "Workspace Job data."
        type: dict
        suboptions:
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
          outputs:
            description: "Output variables data from the Workspace Job."
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
          settings:
            description: "Environment variables used by all the templates in the Workspace."
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
          template_data:
            description: "Input / output data of the Template in the Workspace Job."
            type: list
            elements: 'dict'
            suboptions:
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
              outputs:
                description: "Job output from the Templates."
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
              settings:
                description: "Environment variables used by the template."
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
              updated_at:
                description: "Job status updation timestamp."
                type: str
          updated_at:
            description: "Job status updation timestamp."
            type: str
      action_job_data:
        description: "Action Job data."
        type: dict
        suboptions:
          action_name:
            description: "Flow name."
            type: str
          inputs:
            description: "Input variables data used by the Action Job."
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
          outputs:
            description: "Output variables data from the Action Job."
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
          settings:
            description: "Environment variables used by all the templates in the Action."
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
          updated_at:
            description: "Job status updation timestamp."
            type: str
          inventory_record:
            description: "Complete inventory definition details."
            type: dict
            suboptions:
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
                  - "us-south"
                  - "us-east"
                  - "eu-gb"
                  - "eu-de"
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
        suboptions:
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
        suboptions:
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
            suboptions:
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
                  - "local"
                  - "git_hub"
                  - "git_hub_enterprise"
                  - "git_lab"
                  - "ibm_git_lab"
                  - "ibm_cloud_catalog"
              source:
                description: "Source of templates, playbooks, or controls."
                type: dict
                suboptions:
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
                  git:
                    description: "The connection details to the Git source repository."
                    type: dict
                    suboptions:
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
                    suboptions:
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
              outputs:
                description: "Output variables for the workItem."
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
              settings:
                description: "Environment variables for the workItem."
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
              last_job:
                description: "Status of the last job executed by the workitem."
                type: dict
                suboptions:
                  command_object:
                    description: "Name of the Schematics automation resource."
                    type: str
                    choices:
                      - "workspace"
                      - "action"
                      - "system"
                      - "environment"
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
                  job_id:
                    description: "Workspace job id."
                    type: str
                  job_status:
                    description: "Status of Jobs."
                    type: str
                    choices:
                      - "job_pending"
                      - "job_in_progress"
                      - "job_finished"
                      - "job_failed"
                      - "job_cancelled"
                      - "job_stopped"
                      - "job_stop_in_progress"
                      - "job_ready_to_execute"
              updated_at:
                description: "Job status updation timestamp."
                type: str
          updated_at:
            description: "Job status updation timestamp."
            type: str
  inputs:
    description: "Job inputs used by Action or Workspace."
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
  command_object:
    description: "Name of the Schematics automation resource."
    type: str
    choices:
      - "workspace"
      - "action"
      - "system"
      - "environment"
  command_parameter:
    description: "Schematics job command parameter (playbook-name)."
    type: str
  tags:
    description: "User defined tags, while running the job."
    type: list
    elements: str
  cart_order_data:
    description: "Contains the cart order data which can be used for different purpose for eg. service
      tagging."
    type: list
    elements: 'dict'
    suboptions:
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
  command_options:
    description: "Command line options for the command."
    type: list
    elements: str
  command_object_id:
    description: "Job command object id (workspace-id, action-id)."
    type: str
  log_summary:
    description: "Job log summary record."
    type: dict
    suboptions:
      job_id:
        description: "Workspace Id."
        type: str
      job_type:
        description: "Type of Job."
        type: str
        choices:
          - "repo_download_job"
          - "workspace_job"
          - "action_job"
          - "system_job"
          - "flow_job"
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
        suboptions:
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
        suboptions:
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
        suboptions:
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
        suboptions:
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
            suboptions:
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
        suboptions:
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
            suboptions:
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
        suboptions:
          target_count:
            description: "number of targets or hosts."
            type: float
          success:
            description: "Number of passed."
            type: float
          failed:
            description: "Number of failed."
            type: float
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
  bastion:
    description: "Describes a bastion resource."
    type: dict
    suboptions:
      name:
        description: "Bastion Name; the name must be unique."
        type: str
      host:
        description: "Reference to the Inventory resource definition."
        type: str
  schematics_job_status:
    description: "Job Status."
    type: dict
    suboptions:
      position_in_queue:
        description: "Position of job in pending queue."
        type: float
      total_in_queue:
        description: "Total no. of jobs in pending queue."
        type: float
      workspace_job_status:
        description: "Workspace Job Status."
        type: dict
        suboptions:
          workspace_name:
            description: "Workspace name."
            type: str
          status_code:
            description: "Status of Jobs."
            type: str
            choices:
              - "job_pending"
              - "job_in_progress"
              - "job_finished"
              - "job_failed"
              - "job_cancelled"
              - "job_stopped"
              - "job_stop_in_progress"
              - "job_ready_to_execute"
          status_message:
            description: "Workspace job status message (eg. App1I(Setup)Pending, for a 'Setup' flow in the
              'App1' Workspace)."
            type: str
          flow_status:
            description: "Environment Flow JOB Status."
            type: dict
            suboptions:
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
                  - "job_pending"
                  - "job_in_progress"
                  - "job_finished"
                  - "job_failed"
                  - "job_cancelled"
                  - "job_stopped"
                  - "job_stop_in_progress"
                  - "job_ready_to_execute"
              status_message:
                description: "Flow Job status message - to be displayed along with the status_code;."
                type: str
              workitems:
                description: "Environment's individual workItem status details;."
                type: list
                elements: 'dict'
                suboptions:
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
                      - "job_pending"
                      - "job_in_progress"
                      - "job_finished"
                      - "job_failed"
                      - "job_cancelled"
                      - "job_stopped"
                      - "job_stop_in_progress"
                      - "job_ready_to_execute"
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
            suboptions:
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
                  - "job_pending"
                  - "job_in_progress"
                  - "job_finished"
                  - "job_failed"
                  - "job_cancelled"
                  - "job_stopped"
                  - "job_stop_in_progress"
                  - "job_ready_to_execute"
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
            suboptions:
              name:
                description: "Name of the command."
                type: str
              outcome:
                description: "outcome of the command."
                type: str
      action_job_status:
        description: "Action Job Status."
        type: dict
        suboptions:
          action_name:
            description: "Action name."
            type: str
          status_code:
            description: "Status of Jobs."
            type: str
            choices:
              - "job_pending"
              - "job_in_progress"
              - "job_finished"
              - "job_failed"
              - "job_cancelled"
              - "job_stopped"
              - "job_stop_in_progress"
              - "job_ready_to_execute"
          status_message:
            description: "Action Job status message - to be displayed along with the actionI(status)code."
            type: str
          bastion_status_code:
            description: "Status of Resources."
            type: str
            choices:
              - "none"
              - "ready"
              - "processing"
              - "error"
          bastion_status_message:
            description: "Bastion status message - to be displayed along with the bastionI(status)code;."
            type: str
          targets_status_code:
            description: "Status of Resources."
            type: str
            choices:
              - "none"
              - "ready"
              - "processing"
              - "error"
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
        suboptions:
          system_status_message:
            description: "System job message."
            type: str
          system_status_code:
            description: "Status of Jobs."
            type: str
            choices:
              - "job_pending"
              - "job_in_progress"
              - "job_finished"
              - "job_failed"
              - "job_cancelled"
              - "job_stopped"
              - "job_stop_in_progress"
              - "job_ready_to_execute"
          schematics_resource_status:
            description: "job staus for each schematics resource."
            type: list
            elements: 'dict'
            suboptions:
              status_code:
                description: "Status of Jobs."
                type: str
                choices:
                  - "job_pending"
                  - "job_in_progress"
                  - "job_finished"
                  - "job_failed"
                  - "job_cancelled"
                  - "job_stopped"
                  - "job_stop_in_progress"
                  - "job_ready_to_execute"
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
        suboptions:
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
              - "job_pending"
              - "job_in_progress"
              - "job_finished"
              - "job_failed"
              - "job_cancelled"
              - "job_stopped"
              - "job_stop_in_progress"
              - "job_ready_to_execute"
          status_message:
            description: "Flow Job status message - to be displayed along with the status_code;."
            type: str
          workitems:
            description: "Environment's individual workItem status details;."
            type: list
            elements: 'dict'
            suboptions:
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
                  - "job_pending"
                  - "job_in_progress"
                  - "job_finished"
                  - "job_failed"
                  - "job_cancelled"
                  - "job_stopped"
                  - "job_stop_in_progress"
                  - "job_ready_to_execute"
              status_message:
                description: "workitem job status message;."
                type: str
              updated_at:
                description: "workitem job status updation timestamp."
                type: str
          updated_at:
            description: "Job status updation timestamp."
            type: str
  refresh_token:
    description: "The IAM refresh token for the user or service identity.
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
  propagate:
    description: "Auto propagate the chaange or deletion to the dependent resources."
    type: bool
  force:
    description: "Equivalent to -force options in the command line."
    type: bool
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
- name: Create ibm_schematics_job
  vars:
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
    job_status_workitem_model:
      workspace_id: 'testString'
      workspace_name: 'testString'
      job_id: 'testString'
      status_code: 'job_pending'
      status_message: 'testString'
      updated_at: '2019-01-01T12:00:00.000Z'
    job_status_flow_model:
      flow_id: 'testString'
      flow_name: 'testString'
      status_code: 'job_pending'
      status_message: 'testString'
      workitems: [job_status_workitem_model]
      updated_at: '2019-01-01T12:00:00.000Z'
    job_status_template_model:
      template_id: 'testString'
      template_name: 'testString'
      flow_index: 38
      status_code: 'job_pending'
      status_message: 'testString'
      updated_at: '2019-01-01T12:00:00.000Z'
    job_status_workspace_model:
      workspace_name: 'testString'
      status_code: 'job_pending'
      status_message: 'testString'
      flow_status: job_status_flow_model
      template_status: [job_status_template_model]
      updated_at: '2019-01-01T12:00:00.000Z'
    job_status_action_model:
      action_name: 'testString'
      status_code: 'job_pending'
      status_message: 'testString'
      bastion_status_code: 'none'
      bastion_status_message: 'testString'
      targets_status_code: 'none'
      targets_status_message: 'testString'
      updated_at: '2019-01-01T12:00:00.000Z'
    job_status_schematics_resources_model:
      status_code: 'job_pending'
      status_message: 'testString'
      schematics_resource_id: 'testString'
      updated_at: '2019-01-01T12:00:00.000Z'
    job_status_system_model:
      system_status_message: 'testString'
      system_status_code: 'job_pending'
      schematics_resource_status: [job_status_schematics_resources_model]
      updated_at: '2019-01-01T12:00:00.000Z'
    job_status_model:
      position_in_queue: 72.5
      total_in_queue: 72.5
      workspace_job_status: job_status_workspace_model
      action_job_status: job_status_action_model
      system_job_status: job_status_system_model
      flow_job_status: job_status_flow_model
    cart_order_data_model:
      name: 'testString'
      value: 'testString'
      type: 'testString'
      usage_kind: ['servicetags']
    job_data_template_model:
      template_id: 'testString'
      template_name: 'testString'
      flow_index: 38
      inputs: [variable_data_model]
      outputs: [variable_data_model]
      settings: [variable_data_model]
      updated_at: '2019-01-01T12:00:00.000Z'
    job_data_workspace_model:
      workspace_name: 'testString'
      flow_id: 'testString'
      flow_name: 'testString'
      inputs: [variable_data_model]
      outputs: [variable_data_model]
      settings: [variable_data_model]
      template_data: [job_data_template_model]
      updated_at: '2019-01-01T12:00:00.000Z'
    inventory_resource_record_model:
      name: 'testString'
      description: 'testString'
      location: 'us-south'
      resource_group: 'testString'
      inventories_ini: 'testString'
      resource_queries: ['testString']
    job_data_action_model:
      action_name: 'testString'
      inputs: [variable_data_model]
      outputs: [variable_data_model]
      settings: [variable_data_model]
      updated_at: '2019-01-01T12:00:00.000Z'
      inventory_record: inventory_resource_record_model
      materialized_inventory: 'testString'
    job_data_system_model:
      key_id: 'testString'
      schematics_resource_id: ['testString']
      updated_at: '2019-01-01T12:00:00.000Z'
    git_source_model:
      computed_git_repo_url: 'testString'
      git_repo_url: 'testString'
      git_token: 'testString'
      git_repo_folder: 'testString'
      git_release: 'testString'
      git_branch: 'testString'
    catalog_source_model:
      catalog_name: 'testString'
      catalog_id: 'testString'
      offering_name: 'testString'
      offering_version: 'testString'
      offering_kind: 'testString'
      offering_target_kind: 'testString'
      offering_id: 'testString'
      offering_version_id: 'testString'
      offering_version_flavour_name: 'testString'
      offering_repo_url: 'testString'
      offering_provisioner_working_directory: 'testString'
      dry_run: True
      owning_account: 'testString'
      item_icon_url: 'testString'
      item_id: 'testString'
      item_name: 'testString'
      item_readme_url: 'testString'
      item_url: 'testString'
      launch_url: 'testString'
    external_source_model:
      source_type: 'local'
      git: git_source_model
      catalog: catalog_source_model
    job_data_work_item_last_job_model:
      command_object: 'workspace'
      command_object_name: 'testString'
      command_object_id: 'testString'
      command_name: 'workspace_plan'
      job_id: 'testString'
      job_status: 'job_pending'
    job_data_work_item_model:
      command_object_id: 'testString'
      command_object_name: 'testString'
      layers: 'testString'
      source_type: 'local'
      source: external_source_model
      inputs: [variable_data_model]
      outputs: [variable_data_model]
      settings: [variable_data_model]
      last_job: job_data_work_item_last_job_model
      updated_at: '2019-01-01T12:00:00.000Z'
    job_data_flow_model:
      flow_id: 'testString'
      flow_name: 'testString'
      workitems: [job_data_work_item_model]
      updated_at: '2019-01-01T12:00:00.000Z'
    job_data_model:
      job_type: 'repo_download_job'
      workspace_job_data: job_data_workspace_model
      action_job_data: job_data_action_model
      system_job_data: job_data_system_model
      flow_job_data: job_data_flow_model
    bastion_resource_definition_model:
      name: 'testString'
      host: 'testString'
    job_log_summary_repo_download_job_model:
    job_log_summary_workspace_job_model:
    job_log_summary_workitems_model:
      workspace_id: 'testString'
      job_id: 'testString'
      log_url: 'testString'
    job_log_summary_flow_job_model:
      workitems: [job_log_summary_workitems_model]
    job_log_summary_action_job_recap_model:
      target: ['testString']
      ok: 72.5
      changed: 72.5
      failed: 72.5
      skipped: 72.5
      unreachable: 72.5
    job_log_summary_action_job_model:
      recap: job_log_summary_action_job_recap_model
    job_log_summary_system_job_model:
      success: 72.5
      failed: 72.5
    job_log_summary_model:
      job_type: 'repo_download_job'
      repo_download_job: job_log_summary_repo_download_job_model
      workspace_job: job_log_summary_workspace_job_model
      flow_job: job_log_summary_flow_job_model
      action_job: job_log_summary_action_job_model
      system_job: job_log_summary_system_job_model
    agent_info_model:
      id: 'testString'
      name: 'testString'
      assignment_policy_id: 'testString'
  ibm_schematics_job:
    refresh_token: 'testString'
    command_object: 'workspace'
    command_object_id: 'testString'
    command_name: 'workspace_plan'
    command_parameter: 'testString'
    command_options: ['testString']
    inputs: [variable_data_model]
    settings: [variable_data_model]
    tags: ['testString']
    location: 'us-south'
    schematics_job_status: '{{ job_status_model }}'
    cart_order_data: [cart_order_data_model]
    data: '{{ job_data_model }}'
    bastion: '{{ bastion_resource_definition_model }}'
    log_summary: '{{ job_log_summary_model }}'
    agent: '{{ agent_info_model }}'
    state: present

- name: Update ibm_schematics_job
  vars:
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
    job_status_workitem_model:
      workspace_id: 'testString'
      workspace_name: 'testString'
      job_id: 'testString'
      status_code: 'job_pending'
      status_message: 'testString'
      updated_at: '2019-01-01T12:00:00.000Z'
    job_status_flow_model:
      flow_id: 'testString'
      flow_name: 'testString'
      status_code: 'job_pending'
      status_message: 'testString'
      workitems: [job_status_workitem_model]
      updated_at: '2019-01-01T12:00:00.000Z'
    job_status_template_model:
      template_id: 'testString'
      template_name: 'testString'
      flow_index: 38
      status_code: 'job_pending'
      status_message: 'testString'
      updated_at: '2019-01-01T12:00:00.000Z'
    job_status_workspace_model:
      workspace_name: 'testString'
      status_code: 'job_pending'
      status_message: 'testString'
      flow_status: job_status_flow_model
      template_status: [job_status_template_model]
      updated_at: '2019-01-01T12:00:00.000Z'
    job_status_action_model:
      action_name: 'testString'
      status_code: 'job_pending'
      status_message: 'testString'
      bastion_status_code: 'none'
      bastion_status_message: 'testString'
      targets_status_code: 'none'
      targets_status_message: 'testString'
      updated_at: '2019-01-01T12:00:00.000Z'
    job_status_schematics_resources_model:
      status_code: 'job_pending'
      status_message: 'testString'
      schematics_resource_id: 'testString'
      updated_at: '2019-01-01T12:00:00.000Z'
    job_status_system_model:
      system_status_message: 'testString'
      system_status_code: 'job_pending'
      schematics_resource_status: [job_status_schematics_resources_model]
      updated_at: '2019-01-01T12:00:00.000Z'
    job_status_model:
      position_in_queue: 72.5
      total_in_queue: 72.5
      workspace_job_status: job_status_workspace_model
      action_job_status: job_status_action_model
      system_job_status: job_status_system_model
      flow_job_status: job_status_flow_model
    cart_order_data_model:
      name: 'testString'
      value: 'testString'
      type: 'testString'
      usage_kind: ['servicetags']
    job_data_template_model:
      template_id: 'testString'
      template_name: 'testString'
      flow_index: 38
      inputs: [variable_data_model]
      outputs: [variable_data_model]
      settings: [variable_data_model]
      updated_at: '2019-01-01T12:00:00.000Z'
    job_data_workspace_model:
      workspace_name: 'testString'
      flow_id: 'testString'
      flow_name: 'testString'
      inputs: [variable_data_model]
      outputs: [variable_data_model]
      settings: [variable_data_model]
      template_data: [job_data_template_model]
      updated_at: '2019-01-01T12:00:00.000Z'
    inventory_resource_record_model:
      name: 'testString'
      description: 'testString'
      location: 'us-south'
      resource_group: 'testString'
      inventories_ini: 'testString'
      resource_queries: ['testString']
    job_data_action_model:
      action_name: 'testString'
      inputs: [variable_data_model]
      outputs: [variable_data_model]
      settings: [variable_data_model]
      updated_at: '2019-01-01T12:00:00.000Z'
      inventory_record: inventory_resource_record_model
      materialized_inventory: 'testString'
    job_data_system_model:
      key_id: 'testString'
      schematics_resource_id: ['testString']
      updated_at: '2019-01-01T12:00:00.000Z'
    git_source_model:
      computed_git_repo_url: 'testString'
      git_repo_url: 'testString'
      git_token: 'testString'
      git_repo_folder: 'testString'
      git_release: 'testString'
      git_branch: 'testString'
    catalog_source_model:
      catalog_name: 'testString'
      catalog_id: 'testString'
      offering_name: 'testString'
      offering_version: 'testString'
      offering_kind: 'testString'
      offering_target_kind: 'testString'
      offering_id: 'testString'
      offering_version_id: 'testString'
      offering_version_flavour_name: 'testString'
      offering_repo_url: 'testString'
      offering_provisioner_working_directory: 'testString'
      dry_run: True
      owning_account: 'testString'
      item_icon_url: 'testString'
      item_id: 'testString'
      item_name: 'testString'
      item_readme_url: 'testString'
      item_url: 'testString'
      launch_url: 'testString'
    external_source_model:
      source_type: 'local'
      git: git_source_model
      catalog: catalog_source_model
    job_data_work_item_last_job_model:
      command_object: 'workspace'
      command_object_name: 'testString'
      command_object_id: 'testString'
      command_name: 'workspace_plan'
      job_id: 'testString'
      job_status: 'job_pending'
    job_data_work_item_model:
      command_object_id: 'testString'
      command_object_name: 'testString'
      layers: 'testString'
      source_type: 'local'
      source: external_source_model
      inputs: [variable_data_model]
      outputs: [variable_data_model]
      settings: [variable_data_model]
      last_job: job_data_work_item_last_job_model
      updated_at: '2019-01-01T12:00:00.000Z'
    job_data_flow_model:
      flow_id: 'testString'
      flow_name: 'testString'
      workitems: [job_data_work_item_model]
      updated_at: '2019-01-01T12:00:00.000Z'
    job_data_model:
      job_type: 'repo_download_job'
      workspace_job_data: job_data_workspace_model
      action_job_data: job_data_action_model
      system_job_data: job_data_system_model
      flow_job_data: job_data_flow_model
    bastion_resource_definition_model:
      name: 'testString'
      host: 'testString'
    job_log_summary_repo_download_job_model:
    job_log_summary_workspace_job_model:
    job_log_summary_workitems_model:
      workspace_id: 'testString'
      job_id: 'testString'
      log_url: 'testString'
    job_log_summary_flow_job_model:
      workitems: [job_log_summary_workitems_model]
    job_log_summary_action_job_recap_model:
      target: ['testString']
      ok: 72.5
      changed: 72.5
      failed: 72.5
      skipped: 72.5
      unreachable: 72.5
    job_log_summary_action_job_model:
      recap: job_log_summary_action_job_recap_model
    job_log_summary_system_job_model:
      success: 72.5
      failed: 72.5
    job_log_summary_model:
      job_type: 'repo_download_job'
      repo_download_job: job_log_summary_repo_download_job_model
      workspace_job: job_log_summary_workspace_job_model
      flow_job: job_log_summary_flow_job_model
      action_job: job_log_summary_action_job_model
      system_job: job_log_summary_system_job_model
    agent_info_model:
      id: 'testString'
      name: 'testString'
      assignment_policy_id: 'testString'
  ibm_schematics_job:
    job_id: 'testString'
    refresh_token: 'testString'
    command_object: 'workspace'
    command_object_id: 'testString'
    command_name: 'workspace_plan'
    command_parameter: 'testString'
    command_options: ['testString']
    inputs: [variable_data_model]
    settings: [variable_data_model]
    tags: ['testString']
    location: 'us-south'
    schematics_job_status: '{{ job_status_model }}'
    cart_order_data: [cart_order_data_model]
    data: '{{ job_data_model }}'
    bastion: '{{ bastion_resource_definition_model }}'
    log_summary: '{{ job_log_summary_model }}'
    agent: '{{ agent_info_model }}'
    state: present

- name: Delete ibm_schematics_job
  ibm_schematics_job:
    job_id: 'testString'
    refresh_token: 'testString'
    force: True
    propagate: True
    state: absent
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
  returned: on success for create, update operations
command_object_id:
  description: "Job command object id (workspace-id, action-id)."
  type: str
  returned: on success for create, update operations
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
  returned: on success for create, update operations
command_parameter:
  description: "Schematics job command parameter (playbook-name)."
  type: str
  returned: on success for create, update operations
command_options:
  description: "Command line options for the command."
  type: list
  elements: str
  returned: on success for create, update operations
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
  returned: on success for create, update operations
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
  returned: on success for create, update operations
tags:
  description: "User defined tags, while running the job."
  type: list
  elements: str
  returned: on success for create, update operations
id:
  description: "Job ID."
  type: str
  returned: on success for create, update, delete operations
name:
  description: "Job name, uniquely derived from the related Workspace or Action."
  type: str
  returned: on success for create, update operations
description:
  description: "The description of your job is derived from the related action or workspace.  The
    description can be up to 2048 characters long in size."
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
resource_group:
  description: "Resource-group name derived from the related Workspace or Action."
  type: str
  returned: on success for create, update operations
submitted_at:
  description: "Job submission time."
  type: str
  returned: on success for create, update operations
submitted_by:
  description: "Email address of user who submitted the job."
  type: str
  returned: on success for create, update operations
start_at:
  description: "Job start time."
  type: str
  returned: on success for create, update operations
end_at:
  description: "Job end time."
  type: str
  returned: on success for create, update operations
duration:
  description: "Duration of job execution; example 40 sec."
  type: str
  returned: on success for create, update operations
schematics_job_status:
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
  returned: on success for create, update operations
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
  returned: on success for create, update operations
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
  returned: on success for create, update operations
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
  returned: on success for create, update operations
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
  returned: on success for create, update operations
log_store_url:
  description: "Job log store URL."
  type: str
  returned: on success for create, update operations
state_store_url:
  description: "Job state store URL."
  type: str
  returned: on success for create, update operations
results_url:
  description: "Job results store URL."
  type: str
  returned: on success for create, update operations
updated_at:
  description: "Job status updation timestamp."
  type: str
  returned: on success for create, update operations
job_runner_id:
  description: "ID of the Job Runner."
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
        # Represents the AgentInfo Python class
        agent=dict(
            type='dict',
            options=dict(
                id=dict(
                    type='str',
                    required=False),
                name=dict(
                    type='str',
                    required=False),
                assignment_policy_id=dict(
                    type='str',
                    required=False),
            ),
            required=False),
        # Represents the JobData Python class
        data=dict(
            type='dict',
            options=dict(
                job_type=dict(
                    type='str',
                    choices=[
                        'repo_download_job',
                        'workspace_job',
                        'action_job',
                        'system_job',
                        'flow-job',
                    ],
                    required=False),
                workspace_job_data=dict(
                    type='dict',
                    options=dict(
                        workspace_name=dict(
                            type='str',
                            required=False),
                        flow_id=dict(
                            type='str',
                            required=False),
                        flow_name=dict(
                            type='str',
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
                        template_data=dict(
                            type='list',
                            elements='dict',
                            options=dict(
                                template_id=dict(
                                    type='str',
                                    required=False),
                                template_name=dict(
                                    type='str',
                                    required=False),
                                flow_index=dict(
                                    type='int',
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
                                updated_at=dict(
                                    type='str',
                                    required=False),
                            ),
                            required=False),
                        updated_at=dict(
                            type='str',
                            required=False),
                    ),
                    required=False),
                action_job_data=dict(
                    type='dict',
                    options=dict(
                        action_name=dict(
                            type='str',
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
                        updated_at=dict(
                            type='str',
                            required=False),
                        inventory_record=dict(
                            type='dict',
                            options=dict(
                                name=dict(
                                    type='str',
                                    required=False),
                                id=dict(
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
                                resource_group=dict(
                                    type='str',
                                    required=False),
                                created_at=dict(
                                    type='str',
                                    required=False),
                                created_by=dict(
                                    type='str',
                                    required=False),
                                updated_at=dict(
                                    type='str',
                                    required=False),
                                updated_by=dict(
                                    type='str',
                                    required=False),
                                inventories_ini=dict(
                                    type='str',
                                    required=False),
                                resource_queries=dict(
                                    type='list',
                                    elements='str',
                                    required=False),
                            ),
                            required=False),
                        materialized_inventory=dict(
                            type='str',
                            required=False),
                    ),
                    required=False),
                system_job_data=dict(
                    type='dict',
                    options=dict(
                        key_id=dict(
                            type='str',
                            required=False),
                        schematics_resource_id=dict(
                            type='list',
                            elements='str',
                            required=False),
                        updated_at=dict(
                            type='str',
                            required=False),
                    ),
                    required=False),
                flow_job_data=dict(
                    type='dict',
                    options=dict(
                        flow_id=dict(
                            type='str',
                            required=False),
                        flow_name=dict(
                            type='str',
                            required=False),
                        workitems=dict(
                            type='list',
                            elements='dict',
                            options=dict(
                                command_object_id=dict(
                                    type='str',
                                    required=False),
                                command_object_name=dict(
                                    type='str',
                                    required=False),
                                layers=dict(
                                    type='str',
                                    required=False),
                                source_type=dict(
                                    type='str',
                                    choices=[
                                        'local',
                                        'git_hub',
                                        'git_hub_enterprise',
                                        'git_lab',
                                        'ibm_git_lab',
                                        'ibm_cloud_catalog',
                                    ],
                                    required=False),
                                source=dict(
                                    type='dict',
                                    options=dict(
                                        source_type=dict(
                                            type='str',
                                            choices=[
                                                'local',
                                                'git_hub',
                                                'git_hub_enterprise',
                                                'git_lab',
                                                'ibm_git_lab',
                                                'ibm_cloud_catalog',
                                            ],
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
                                                    no_log=True,
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
                                                git_commit=dict(
                                                    type='str',
                                                    required=False),
                                                git_commit_timestamp=dict(
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
                                                catalog_id=dict(
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
                                                offering_target_kind=dict(
                                                    type='str',
                                                    required=False),
                                                offering_id=dict(
                                                    type='str',
                                                    required=False),
                                                offering_version_id=dict(
                                                    type='str',
                                                    required=False),
                                                offering_version_flavour_name=dict(
                                                    type='str',
                                                    required=False),
                                                offering_repo_url=dict(
                                                    type='str',
                                                    required=False),
                                                offering_provisioner_working_directory=dict(
                                                    type='str',
                                                    required=False),
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
                                            ),
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
                                last_job=dict(
                                    type='dict',
                                    options=dict(
                                        command_object=dict(
                                            type='str',
                                            choices=[
                                                'workspace',
                                                'action',
                                                'system',
                                                'environment',
                                            ],
                                            required=False),
                                        command_object_name=dict(
                                            type='str',
                                            required=False),
                                        command_object_id=dict(
                                            type='str',
                                            required=False),
                                        command_name=dict(
                                            type='str',
                                            choices=[
                                                'workspace_plan',
                                                'workspace_apply',
                                                'workspace_destroy',
                                                'workspace_refresh',
                                                'ansible_playbook_run',
                                                'ansible_playbook_check',
                                                'create_action',
                                                'put_action',
                                                'patch_action',
                                                'delete_action',
                                                'system_key_enable',
                                                'system_key_delete',
                                                'system_key_disable',
                                                'system_key_rotate',
                                                'system_key_restore',
                                                'create_workspace',
                                                'put_workspace',
                                                'patch_workspace',
                                                'delete_workspace',
                                                'create_cart',
                                                'repository_process',
                                                'terraform_commands',
                                            ],
                                            required=False),
                                        job_id=dict(
                                            type='str',
                                            required=False),
                                        job_status=dict(
                                            type='str',
                                            choices=[
                                                'job_pending',
                                                'job_in_progress',
                                                'job_finished',
                                                'job_failed',
                                                'job_cancelled',
                                                'job_stopped',
                                                'job_stop_in_progress',
                                                'job_ready_to_execute',
                                            ],
                                            required=False),
                                    ),
                                    required=False),
                                updated_at=dict(
                                    type='str',
                                    required=False),
                            ),
                            required=False),
                        updated_at=dict(
                            type='str',
                            required=False),
                    ),
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
        command_name=dict(
            type='str',
            choices=[
                'workspace_plan',
                'workspace_apply',
                'workspace_destroy',
                'workspace_refresh',
                'ansible_playbook_run',
                'ansible_playbook_check',
                'create_action',
                'put_action',
                'patch_action',
                'delete_action',
                'system_key_enable',
                'system_key_delete',
                'system_key_disable',
                'system_key_rotate',
                'system_key_restore',
                'create_workspace',
                'put_workspace',
                'patch_workspace',
                'delete_workspace',
                'create_cart',
                'repository_process',
                'terraform_commands',
            ],
            required=False),
        command_object=dict(
            type='str',
            choices=[
                'workspace',
                'action',
                'system',
                'environment',
            ],
            required=False),
        command_parameter=dict(
            type='str',
            required=False),
        tags=dict(
            type='list',
            elements='str',
            required=False),
        cart_order_data=dict(
            type='list',
            elements='dict',
            options=dict(
                name=dict(
                    type='str',
                    required=False),
                value=dict(
                    type='str',
                    required=False),
                type=dict(
                    type='str',
                    required=False),
                usage_kind=dict(
                    type='list',
                    elements='str',
                    choices=[
                        'servicetags',
                    ],
                    required=False),
            ),
            required=False),
        command_options=dict(
            type='list',
            elements='str',
            required=False),
        command_object_id=dict(
            type='str',
            required=False),
        # Represents the JobLogSummary Python class
        log_summary=dict(
            type='dict',
            options=dict(
                job_id=dict(
                    type='str',
                    required=False),
                job_type=dict(
                    type='str',
                    choices=[
                        'repo_download_job',
                        'workspace_job',
                        'action_job',
                        'system_job',
                        'flow_job',
                    ],
                    required=False),
                log_start_at=dict(
                    type='str',
                    required=False),
                log_analyzed_till=dict(
                    type='str',
                    required=False),
                elapsed_time=dict(
                    type='float',
                    required=False),
                log_errors=dict(
                    type='list',
                    elements='dict',
                    options=dict(
                        error_code=dict(
                            type='str',
                            required=False),
                        error_msg=dict(
                            type='str',
                            required=False),
                        error_count=dict(
                            type='float',
                            required=False),
                    ),
                    required=False),
                repo_download_job=dict(
                    type='dict',
                    options=dict(
                        scanned_file_count=dict(
                            type='float',
                            required=False),
                        quarantined_file_count=dict(
                            type='float',
                            required=False),
                        detected_filetype=dict(
                            type='str',
                            required=False),
                        inputs_count=dict(
                            type='str',
                            required=False),
                        outputs_count=dict(
                            type='str',
                            required=False),
                    ),
                    required=False),
                workspace_job=dict(
                    type='dict',
                    options=dict(
                        resources_add=dict(
                            type='float',
                            required=False),
                        resources_modify=dict(
                            type='float',
                            required=False),
                        resources_destroy=dict(
                            type='float',
                            required=False),
                    ),
                    required=False),
                flow_job=dict(
                    type='dict',
                    options=dict(
                        workitems_completed=dict(
                            type='float',
                            required=False),
                        workitems_pending=dict(
                            type='float',
                            required=False),
                        workitems_failed=dict(
                            type='float',
                            required=False),
                        workitems=dict(
                            type='list',
                            elements='dict',
                            options=dict(
                                workspace_id=dict(
                                    type='str',
                                    required=False),
                                job_id=dict(
                                    type='str',
                                    required=False),
                                resources_add=dict(
                                    type='float',
                                    required=False),
                                resources_modify=dict(
                                    type='float',
                                    required=False),
                                resources_destroy=dict(
                                    type='float',
                                    required=False),
                                log_url=dict(
                                    type='str',
                                    required=False),
                            ),
                            required=False),
                    ),
                    required=False),
                action_job=dict(
                    type='dict',
                    options=dict(
                        target_count=dict(
                            type='float',
                            required=False),
                        task_count=dict(
                            type='float',
                            required=False),
                        play_count=dict(
                            type='float',
                            required=False),
                        recap=dict(
                            type='dict',
                            options=dict(
                                target=dict(
                                    type='list',
                                    elements='str',
                                    required=False),
                                ok=dict(
                                    type='float',
                                    required=False),
                                changed=dict(
                                    type='float',
                                    required=False),
                                failed=dict(
                                    type='float',
                                    required=False),
                                skipped=dict(
                                    type='float',
                                    required=False),
                                unreachable=dict(
                                    type='float',
                                    required=False),
                            ),
                            required=False),
                    ),
                    required=False),
                system_job=dict(
                    type='dict',
                    options=dict(
                        target_count=dict(
                            type='float',
                            required=False),
                        success=dict(
                            type='float',
                            required=False),
                        failed=dict(
                            type='float',
                            required=False),
                    ),
                    required=False),
            ),
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
        # Represents the JobStatus Python class
        schematics_job_status=dict(
            type='dict',
            options=dict(
                position_in_queue=dict(
                    type='float',
                    required=False),
                total_in_queue=dict(
                    type='float',
                    required=False),
                workspace_job_status=dict(
                    type='dict',
                    options=dict(
                        workspace_name=dict(
                            type='str',
                            required=False),
                        status_code=dict(
                            type='str',
                            choices=[
                                'job_pending',
                                'job_in_progress',
                                'job_finished',
                                'job_failed',
                                'job_cancelled',
                                'job_stopped',
                                'job_stop_in_progress',
                                'job_ready_to_execute',
                            ],
                            required=False),
                        status_message=dict(
                            type='str',
                            required=False),
                        flow_status=dict(
                            type='dict',
                            options=dict(
                                flow_id=dict(
                                    type='str',
                                    required=False),
                                flow_name=dict(
                                    type='str',
                                    required=False),
                                status_code=dict(
                                    type='str',
                                    choices=[
                                        'job_pending',
                                        'job_in_progress',
                                        'job_finished',
                                        'job_failed',
                                        'job_cancelled',
                                        'job_stopped',
                                        'job_stop_in_progress',
                                        'job_ready_to_execute',
                                    ],
                                    required=False),
                                status_message=dict(
                                    type='str',
                                    required=False),
                                workitems=dict(
                                    type='list',
                                    elements='dict',
                                    options=dict(
                                        workspace_id=dict(
                                            type='str',
                                            required=False),
                                        workspace_name=dict(
                                            type='str',
                                            required=False),
                                        job_id=dict(
                                            type='str',
                                            required=False),
                                        status_code=dict(
                                            type='str',
                                            choices=[
                                                'job_pending',
                                                'job_in_progress',
                                                'job_finished',
                                                'job_failed',
                                                'job_cancelled',
                                                'job_stopped',
                                                'job_stop_in_progress',
                                                'job_ready_to_execute',
                                            ],
                                            required=False),
                                        status_message=dict(
                                            type='str',
                                            required=False),
                                        updated_at=dict(
                                            type='str',
                                            required=False),
                                    ),
                                    required=False),
                                updated_at=dict(
                                    type='str',
                                    required=False),
                            ),
                            required=False),
                        template_status=dict(
                            type='list',
                            elements='dict',
                            options=dict(
                                template_id=dict(
                                    type='str',
                                    required=False),
                                template_name=dict(
                                    type='str',
                                    required=False),
                                flow_index=dict(
                                    type='int',
                                    required=False),
                                status_code=dict(
                                    type='str',
                                    choices=[
                                        'job_pending',
                                        'job_in_progress',
                                        'job_finished',
                                        'job_failed',
                                        'job_cancelled',
                                        'job_stopped',
                                        'job_stop_in_progress',
                                        'job_ready_to_execute',
                                    ],
                                    required=False),
                                status_message=dict(
                                    type='str',
                                    required=False),
                                updated_at=dict(
                                    type='str',
                                    required=False),
                            ),
                            required=False),
                        updated_at=dict(
                            type='str',
                            required=False),
                        commands=dict(
                            type='list',
                            elements='dict',
                            options=dict(
                                name=dict(
                                    type='str',
                                    required=False),
                                outcome=dict(
                                    type='str',
                                    required=False),
                            ),
                            required=False),
                    ),
                    required=False),
                action_job_status=dict(
                    type='dict',
                    options=dict(
                        action_name=dict(
                            type='str',
                            required=False),
                        status_code=dict(
                            type='str',
                            choices=[
                                'job_pending',
                                'job_in_progress',
                                'job_finished',
                                'job_failed',
                                'job_cancelled',
                                'job_stopped',
                                'job_stop_in_progress',
                                'job_ready_to_execute',
                            ],
                            required=False),
                        status_message=dict(
                            type='str',
                            required=False),
                        bastion_status_code=dict(
                            type='str',
                            choices=[
                                'none',
                                'ready',
                                'processing',
                                'error',
                            ],
                            required=False),
                        bastion_status_message=dict(
                            type='str',
                            required=False),
                        targets_status_code=dict(
                            type='str',
                            choices=[
                                'none',
                                'ready',
                                'processing',
                                'error',
                            ],
                            required=False),
                        targets_status_message=dict(
                            type='str',
                            required=False),
                        updated_at=dict(
                            type='str',
                            required=False),
                    ),
                    required=False),
                system_job_status=dict(
                    type='dict',
                    options=dict(
                        system_status_message=dict(
                            type='str',
                            required=False),
                        system_status_code=dict(
                            type='str',
                            choices=[
                                'job_pending',
                                'job_in_progress',
                                'job_finished',
                                'job_failed',
                                'job_cancelled',
                                'job_stopped',
                                'job_stop_in_progress',
                                'job_ready_to_execute',
                            ],
                            required=False),
                        schematics_resource_status=dict(
                            type='list',
                            elements='dict',
                            options=dict(
                                status_code=dict(
                                    type='str',
                                    choices=[
                                        'job_pending',
                                        'job_in_progress',
                                        'job_finished',
                                        'job_failed',
                                        'job_cancelled',
                                        'job_stopped',
                                        'job_stop_in_progress',
                                        'job_ready_to_execute',
                                    ],
                                    required=False),
                                status_message=dict(
                                    type='str',
                                    required=False),
                                schematics_resource_id=dict(
                                    type='str',
                                    required=False),
                                updated_at=dict(
                                    type='str',
                                    required=False),
                            ),
                            required=False),
                        updated_at=dict(
                            type='str',
                            required=False),
                    ),
                    required=False),
                flow_job_status=dict(
                    type='dict',
                    options=dict(
                        flow_id=dict(
                            type='str',
                            required=False),
                        flow_name=dict(
                            type='str',
                            required=False),
                        status_code=dict(
                            type='str',
                            choices=[
                                'job_pending',
                                'job_in_progress',
                                'job_finished',
                                'job_failed',
                                'job_cancelled',
                                'job_stopped',
                                'job_stop_in_progress',
                                'job_ready_to_execute',
                            ],
                            required=False),
                        status_message=dict(
                            type='str',
                            required=False),
                        workitems=dict(
                            type='list',
                            elements='dict',
                            options=dict(
                                workspace_id=dict(
                                    type='str',
                                    required=False),
                                workspace_name=dict(
                                    type='str',
                                    required=False),
                                job_id=dict(
                                    type='str',
                                    required=False),
                                status_code=dict(
                                    type='str',
                                    choices=[
                                        'job_pending',
                                        'job_in_progress',
                                        'job_finished',
                                        'job_failed',
                                        'job_cancelled',
                                        'job_stopped',
                                        'job_stop_in_progress',
                                        'job_ready_to_execute',
                                    ],
                                    required=False),
                                status_message=dict(
                                    type='str',
                                    required=False),
                                updated_at=dict(
                                    type='str',
                                    required=False),
                            ),
                            required=False),
                        updated_at=dict(
                            type='str',
                            required=False),
                    ),
                    required=False),
            ),
            required=False),
        refresh_token=dict(
            type='str',
            no_log=True,
            required=False),
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
        propagate=dict(
            type='bool',
            required=False),
        force=dict(
            type='bool',
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
    agent = module.params["agent"]
    data = module.params["data"]
    inputs = module.params["inputs"]
    command_name = module.params["command_name"]
    command_object = module.params["command_object"]
    command_parameter = module.params["command_parameter"]
    tags = module.params["tags"]
    cart_order_data = module.params["cart_order_data"]
    command_options = module.params["command_options"]
    command_object_id = module.params["command_object_id"]
    log_summary = module.params["log_summary"]
    location = module.params["location"]
    bastion = module.params["bastion"]
    schematics_job_status = module.params["schematics_job_status"]
    refresh_token = module.params["refresh_token"]
    job_id = module.params["job_id"]
    profile = module.params["profile"]
    propagate = module.params["propagate"]
    force = module.params["force"]
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
    if job_id:
        try:
            sdk.get_job(
                job_id=job_id,
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
                sdk.delete_job(
                    job_id=job_id,
                    refresh_token=refresh_token,
                    force=force,
                    propagate=propagate,
                )
            except ApiException as ex:
                module.fail_json(msg=ex.message)
            else:
                module.exit_json(changed=True, id=job_id, status="deleted")
        else:
            module.exit_json(changed=False, id=job_id, status="not_found")

    if state == "present":
        if not resource_exists:
            # Create path
            try:
                response = sdk.create_job(
                    refresh_token=refresh_token,
                    command_object=command_object,
                    command_object_id=command_object_id,
                    command_name=command_name,
                    command_parameter=command_parameter,
                    command_options=command_options,
                    inputs=inputs,
                    settings=settings,
                    tags=tags,
                    location=location,
                    status=schematics_job_status,
                    cart_order_data=cart_order_data,
                    data=data,
                    bastion=bastion,
                    log_summary=log_summary,
                    agent=agent,
                )
            except ApiException as ex:
                module.fail_json(msg=ex.message)
            else:
                result = response.get_result()
                if 'status' in result:
                    result['schematics_job_status'] = result['status']
                    del result['status']

                module.exit_json(changed=True, **result)
        else:
            # Update path
            try:
                response = sdk.update_job(
                    job_id=job_id,
                    refresh_token=refresh_token,
                    command_object=command_object,
                    command_object_id=command_object_id,
                    command_name=command_name,
                    command_parameter=command_parameter,
                    command_options=command_options,
                    inputs=inputs,
                    settings=settings,
                    tags=tags,
                    location=location,
                    status=schematics_job_status,
                    cart_order_data=cart_order_data,
                    data=data,
                    bastion=bastion,
                    log_summary=log_summary,
                    agent=agent,
                )
            except ApiException as ex:
                module.fail_json(msg=ex.message)
            else:
                result = response.get_result()
                if 'status' in result:
                    result['schematics_job_status'] = result['status']
                    del result['status']

                module.exit_json(changed=True, **result)


def main():
    run_module()


if __name__ == '__main__':
    main()
