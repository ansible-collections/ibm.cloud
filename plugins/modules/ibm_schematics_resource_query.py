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
module: ibm_schematics_resource_query
short_description: Manage C(schematics_resource_querys) for Schematics Service API.
author: Kavya Handadi (@kavya498)
version_added: "1.0.0"
description:
  - This module creates, updates, or deletes a C(schematics_resource_query) resource for Schematics Service API.
requirements:
  - "SchematicsV1"
options:
  name:
    description:
      - Resource query name.
    type: str
  type:
    description:
      - Resource type (cluster, vsi, icd, vpc).
    type: str
    choices:
      - vsi
  queries:
    description:
      - queries
    type: list
    elements: dict
    suboptions:
      query_type:
        description:
          - Type of the query(workspaces).
        type: str
        choices:
          - workspaces
      query_condition:
        description:
          - query_condition
        type: list
        elements: dict
        suboptions:
          name:
            description:
              - Name of the resource query param.
            type: str
          value:
            description:
              - Value of the resource query param.
            type: str
          description:
            description:
              - Description of resource query param variable.
            type: str
      query_select:
        description:
          - List of query selection parameters.
        type: list
        elements: str
  query_id:
    description:
      - Resource query Id.  Use C(GET /v2/resourceI(query) API to look up the Resource query definition Ids  in your IBM Cloud account.
    type: str
  propagate:
    description:
      - Auto propagate the chaange or deletion to the dependent resources.
    type: bool
  force:
    description:
      - Equivalent to -force options in the command line.
    type: bool
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
- name: Create ibm_schematics_resource_query
  vars:
    resource_query_param_model:
    resource_query_model:
  ibm_schematics_resource_query:

- name: Update ibm_schematics_resource_query
  vars:
    resource_query_param_model:
    resource_query_model:
  ibm_schematics_resource_query:

- name: Delete ibm_schematics_resource_query
  ibm_schematics_resource_query:
'''

RETURN = '''
msg:
  description: |-
    A dictionary that represents the result.
    If a resource was created, a C(ResourceQueryRecord) object is returned.
    If a resource was updated, a C(ResourceQueryRecord) object is returned.
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
        name=dict(
            type='str',
            required=False),
        type=dict(
            type='str',
            choices=['vsi'],
            required=False),
        queries=dict(
            type='list',
            elements='dict',
            options=dict(
                query_type=dict(
                    type='str',
                    choices=['workspaces'],
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

    name = module.params["name"]
    type = module.params["type"]
    queries = module.params["queries"]
    query_id = module.params["query_id"]
    propagate = module.params["propagate"]
    force = module.params["force"]
    state = module.params["state"]

    sdk = config.get_schematicsv1_sdk()

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
                payload = {"id": query_id, "status": "deleted"}
                module.exit_json(changed=True, msg=payload)
        else:
            payload = {"id": query_id, "status": "not_found"}
            module.exit_json(changed=False, msg=payload)

    if state == "present":
        if not resource_exists:
            # Create path
            try:
                result = sdk.create_resource_query(
                    type=type,
                    name=name,
                    queries=queries,
                ).get_result()
            except ApiException as ex:
                module.fail_json(msg=ex.message)
            else:
                module.exit_json(changed=True, msg=result)
        else:
            # Update path
            try:
                result = sdk.replace_resources_query(
                    query_id=query_id,
                    type=type,
                    name=name,
                    queries=queries,
                ).get_result()
            except ApiException as ex:
                module.fail_json(msg=ex.message)
            else:
                module.exit_json(changed=True, msg=result)


def main():
    run_module()


if __name__ == '__main__':
    main()
