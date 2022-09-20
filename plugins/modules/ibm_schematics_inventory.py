#!/usr/bin/python
# -*- coding: utf-8 -*-

# (C) Copyright IBM Corp. 2022.
# GNU General Public License v3.0+ (see LICENSE or https://www.gnu.org/licenses/gpl-3.0.txt)

from __future__ import (absolute_import, division, print_function)
__metaclass__ = type


DOCUMENTATION = r'''
---
module: ibm_schematics_inventory
short_description: Manage C(schematics_inventorys) for Schematics Service API.
author: Kavya Handadi (@kavya498)
version_added: "0.0.1-beta0"
description:
  - This module creates, updates, or deletes a C(schematics_inventory) resource for Schematics Service API.
requirements:
  - "SchematicsV1"
options:
  inventories_ini:
    description:
      - Input inventory of host and host group for the playbook, in the C(.ini) file format.
    type: str
  resource_group:
    description:
      - Resource-group name for the Inventory definition.   By default, Inventory definition will be created in Default Resource Group.
    type: str
  resource_queries:
    description:
      - Input resource query definitions that is used to dynamically generate the inventory of host and host group for the playbook.
    type: list
    elements: str
  name:
    description: |
      The unique name of your Inventory definition.
      The name can be up to 128 characters long and can include alphanumeric characters, spaces, dashes, and underscores.
    type: str
  description:
    description:
      - The description of your Inventory definition. The description can be up to 2048 characters long in size.
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
  inventory_id:
    description: |
      Resource Inventory Id.
      Use C(GET /v2/inventories) API to look up the Resource Inventory definition Ids  in your IBM Cloud account.
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
- name: Create ibm_schematics_inventory
  ibm_schematics_inventory:

- name: Update ibm_schematics_inventory
  ibm_schematics_inventory:

- name: Delete ibm_schematics_inventory
  ibm_schematics_inventory:
'''

RETURN = '''
msg:
  description: |-
    A dictionary that represents the result.
    If a resource was created, an C(InventoryResourceRecord) object is returned.
    If a resource was updated, an C(InventoryResourceRecord) object is returned.
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
            choices=['us-south', 'us-east', 'eu-gb', 'eu-de'],
            required=False),
        inventory_id=dict(
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

    sdk = config.get_schematicsv1_sdk()

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
                payload = {"id": inventory_id, "status": "deleted"}
                module.exit_json(changed=True, msg=payload)
        else:
            payload = {"id": inventory_id, "status": "not_found"}
            module.exit_json(changed=False, msg=payload)

    if state == "present":
        if not resource_exists:
            # Create path
            try:
                result = sdk.create_inventory(
                    name=name,
                    description=description,
                    location=location,
                    resource_group=resource_group,
                    inventories_ini=inventories_ini,
                    resource_queries=resource_queries,
                ).get_result()
            except ApiException as ex:
                module.fail_json(msg=ex.message)
            else:
                module.exit_json(changed=True, msg=result)
        else:
            # Update path
            try:
                result = sdk.replace_inventory(
                    inventory_id=inventory_id,
                    name=name,
                    description=description,
                    location=location,
                    resource_group=resource_group,
                    inventories_ini=inventories_ini,
                    resource_queries=resource_queries,
                ).get_result()
            except ApiException as ex:
                module.fail_json(msg=ex.message)
            else:
                module.exit_json(changed=True, msg=result)


def main():
    run_module()


if __name__ == '__main__':
    main()
