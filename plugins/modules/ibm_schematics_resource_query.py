#!/usr/bin/python
# coding: utf-8

# (C) Copyright IBM Corp. 2024.
#
# GNU General Public License v3.0+ (see LICENSE or https://www.gnu.org/licenses/gpl-3.0.txt)

from __future__ import (absolute_import, division, print_function)
__metaclass__ = type


DOCUMENTATION = r'''
---
module: ibm_schematics_resource_query
short_description: Manage C(schematics_resource_querys) for Schematics Service API.
author: Gannayak Pabra (@Gannayak0722)
version_added: "1.0.0"
description:
  - This module creates, updates, or deletes a C(schematics_resource_query) resource for Schematics Service API.
requirements:
  - "SchematicsV1"
options:
  name:
    description: "Resource query name."
    type: str
  type:
    description: "Resource type (cluster, vsi, icd, vpc)."
    type: str
    choices:
      - "vsi"
  queries:
    description: "No description has been provided."
    type: list
    elements: 'dict'
    suboptions:
      query_type:
        description: "Type of the query(workspaces)."
        type: str
        choices:
          - "workspaces"
      query_condition:
        description: "No description has been provided."
        type: list
        elements: 'dict'
        suboptions:
          name:
            description: "Name of the resource query param."
            type: str
          value:
            description: "Value of the resource query param."
            type: str
          description:
            description: "Description of resource query param variable."
            type: str
      query_select:
        description: "List of query selection parameters."
        type: list
        elements: str
  query_id:
    description: "Resource query Id.  Use C(GET /v2/resource_query) API to look up the Resource query
      definition Ids  in your IBM Cloud account."
    type: str
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
- name: Create ibm_schematics_resource_query
  vars:
    resource_query_param_model:
      name: 'testString'
      value: 'testString'
      description: 'testString'
    resource_query_model:
      query_type: 'workspaces'
      query_condition: [resource_query_param_model]
      query_select: ['testString']
  ibm_schematics_resource_query:
    type: 'vsi'
    name: 'testString'
    queries: [resource_query_model]
    state: present

- name: Update ibm_schematics_resource_query
  vars:
    resource_query_param_model:
      name: 'testString'
      value: 'testString'
      description: 'testString'
    resource_query_model:
      query_type: 'workspaces'
      query_condition: [resource_query_param_model]
      query_select: ['testString']
  ibm_schematics_resource_query:
    query_id: 'testString'
    type: 'vsi'
    name: 'testString'
    queries: [resource_query_model]
    state: present

- name: Delete ibm_schematics_resource_query
  ibm_schematics_resource_query:
    query_id: 'testString'
    force: True
    propagate: True
    state: absent
'''

RETURN = r'''
type:
  description: "Resource type (cluster, vsi, icd, vpc)."
  type: str
  choices:
    - "vsi"
  returned: on success for create, update operations
name:
  description: "Resource query name."
  type: str
  returned: on success for create, update operations
id:
  description: "Resource Query id."
  type: str
  returned: on success for create, update, delete operations
created_at:
  description: "Resource query creation time."
  type: str
  returned: on success for create, update operations
created_by:
  description: "Email address of user who created the Resource query."
  type: str
  returned: on success for create, update operations
updated_at:
  description: "Resource query updation time."
  type: str
  returned: on success for create, update operations
updated_by:
  description: "Email address of user who updated the Resource query."
  type: str
  returned: on success for create, update operations
queries:
  description: "No description has been provided."
  type: list
  elements: 'dict'
  contains:
    query_type:
      description: "Type of the query(workspaces)."
      type: str
      choices:
        - 'workspaces'
    query_condition:
      description: "No description has been provided."
      type: list
      elements: 'dict'
      contains:
        name:
          description: "Name of the resource query param."
          type: str
        value:
          description: "Value of the resource query param."
          type: str
        description:
          description: "Description of resource query param variable."
          type: str
    query_select:
      description: "List of query selection parameters."
      type: list
      elements: str
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
        name=dict(
            type='str',
            required=False),
        type=dict(
            type='str',
            choices=[
                'vsi',
            ],
            required=False),
        queries=dict(
            type='list',
            elements='dict',
            options=dict(
                query_type=dict(
                    type='str',
                    choices=[
                        'workspaces',
                    ],
                    required=False),
                query_condition=dict(
                    type='list',
                    elements='dict',
                    options=dict(
                        name=dict(
                            type='str',
                            required=False),
                        value=dict(
                            type='str',
                            required=False),
                        description=dict(
                            type='str',
                            required=False),
                    ),
                    required=False),
                query_select=dict(
                    type='list',
                    elements='str',
                    required=False),
            ),
            required=False),
        query_id=dict(
            type='str',
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

    name = module.params["name"]
    type = module.params["type"]
    queries = module.params["queries"]
    query_id = module.params["query_id"]
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
    if query_id:
        try:
            sdk.get_resources_query(
                query_id=query_id,
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
                sdk.delete_resources_query(
                    query_id=query_id,
                    force=force,
                    propagate=propagate,
                )
            except ApiException as ex:
                module.fail_json(msg=ex.message)
            else:
                module.exit_json(changed=True, id=query_id, status="deleted")
        else:
            module.exit_json(changed=False, id=query_id, status="not_found")

    if state == "present":
        if not resource_exists:
            # Create path
            try:
                response = sdk.create_resource_query(
                    type=type,
                    name=name,
                    queries=queries,
                )
            except ApiException as ex:
                module.fail_json(msg=ex.message)
            else:
                result = response.get_result()

                module.exit_json(changed=True, **result)
        else:
            # Update path
            try:
                response = sdk.replace_resources_query(
                    query_id=query_id,
                    type=type,
                    name=name,
                    queries=queries,
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
