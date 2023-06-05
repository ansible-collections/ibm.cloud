#!/usr/bin/python
# coding: utf-8

# (C) Copyright IBM Corp. 2023.
#
# GNU General Public License v3.0+ (see LICENSE or https://www.gnu.org/licenses/gpl-3.0.txt)

from __future__ import (absolute_import, division, print_function)
__metaclass__ = type


DOCUMENTATION = r'''
---
module: ibm_schematics_inventory
short_description: Manage C(schematics_inventorys) for Schematics Service API.
author: IBM SDK Generator (@ibm)
version_added: "1.0.0"
description:
  - This module creates, updates, or deletes a C(schematics_inventory) resource for Schematics Service API.
requirements:
  - "SchematicsV1"
options:
  inventories_ini:
    description: "Input inventory of host and host group for the playbook, in the C(.ini) file format."
    type: str
  resource_group:
    description: "Resource-group name for the Inventory definition.   By default, Inventory definition
      will be created in Default Resource Group."
    type: str
  resource_queries:
    description: "Input resource query definitions that is used to dynamically generate the inventory
      of host and host group for the playbook."
    type: list
    elements: str
  name:
    description: "The unique name of your Inventory definition. The name can be up to 128 characters
      long and can include alphanumeric characters, spaces, dashes, and underscores."
    type: str
  description:
    description: "The description of your Inventory definition. The description can be up to 2048
      characters long in size."
    type: str
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
  inventory_id:
    description: "Resource Inventory Id.  Use C(GET /v2/inventories) API to look up the Resource
      Inventory definition Ids  in your IBM Cloud account."
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
- name: Create ibm_schematics_inventory
  ibm_schematics_inventory:
    name: 'testString'
    description: 'testString'
    location: 'us-south'
    resource_group: 'testString'
    inventories_ini: 'testString'
    resource_queries: ['testString']
    state: present

- name: Update ibm_schematics_inventory
  ibm_schematics_inventory:
    inventory_id: 'testString'
    name: 'testString'
    description: 'testString'
    location: 'us-south'
    resource_group: 'testString'
    inventories_ini: 'testString'
    resource_queries: ['testString']
    state: present

- name: Delete ibm_schematics_inventory
  ibm_schematics_inventory:
    inventory_id: 'testString'
    force: True
    propagate: True
    state: absent
'''

RETURN = r'''
name:
  description: "The unique name of your Inventory.  The name can be up to 128 characters long and can
    include alphanumeric  characters, spaces, dashes, and underscores."
  type: str
  returned: on success for create, update operations
id:
  description: "Inventory id."
  type: str
  returned: on success for create, update, delete operations
description:
  description: "The description of your Inventory.  The description can be up to 2048 characters long
    in size."
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
  description: "Resource-group name for the Inventory definition.  By default, Inventory will be
    created in Default Resource Group."
  type: str
  returned: on success for create, update operations
created_at:
  description: "Inventory creation time."
  type: str
  returned: on success for create, update operations
created_by:
  description: "Email address of user who created the Inventory."
  type: str
  returned: on success for create, update operations
updated_at:
  description: "Inventory updation time."
  type: str
  returned: on success for create, update operations
updated_by:
  description: "Email address of user who updated the Inventory."
  type: str
  returned: on success for create, update operations
inventories_ini:
  description: "Input inventory of host and host group for the playbook,  in the .ini file format."
  type: str
  returned: on success for create, update operations
resource_queries:
  description: "Input resource queries that is used to dynamically generate  the inventory of host and
    host group for the playbook."
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
    from ibm_schematics import SchematicsV1
    from ibm_cloud_sdk_core import ApiException
except ImportError as imp_exc:
    MISSING_IMPORT_EXC = imp_exc
else:
    MISSING_IMPORT_EXC = None


def run_module():
    module_args = dict(
        inventories_ini=dict(
            type='str',
            required=False),
        resource_group=dict(
            type='str',
            required=False),
        resource_queries=dict(
            type='list',
            elements='str',
            required=False),
        name=dict(
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
        inventory_id=dict(
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

    inventories_ini = module.params["inventories_ini"]
    resource_group = module.params["resource_group"]
    resource_queries = module.params["resource_queries"]
    name = module.params["name"]
    description = module.params["description"]
    location = module.params["location"]
    inventory_id = module.params["inventory_id"]
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
    if inventory_id:
        try:
            sdk.get_inventory(
                inventory_id=inventory_id,
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
                sdk.delete_inventory(
                    inventory_id=inventory_id,
                    force=force,
                    propagate=propagate,
                )
            except ApiException as ex:
                module.fail_json(msg=ex.message)
            else:
                module.exit_json(changed=True, id=inventory_id, status="deleted")
        else:
            module.exit_json(changed=False, id=inventory_id, status="not_found")

    if state == "present":
        if not resource_exists:
            # Create path
            try:
                response = sdk.create_inventory(
                    name=name,
                    description=description,
                    location=location,
                    resource_group=resource_group,
                    inventories_ini=inventories_ini,
                    resource_queries=resource_queries,
                )
            except ApiException as ex:
                module.fail_json(msg=ex.message)
            else:
                result = response.get_result()

                module.exit_json(changed=True, **result)
        else:
            # Update path
            try:
                response = sdk.replace_inventory(
                    inventory_id=inventory_id,
                    name=name,
                    description=description,
                    location=location,
                    resource_group=resource_group,
                    inventories_ini=inventories_ini,
                    resource_queries=resource_queries,
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
