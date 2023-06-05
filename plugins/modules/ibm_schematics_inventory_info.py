#!/usr/bin/python
# coding: utf-8

# (C) Copyright IBM Corp. 2023.
#
# GNU General Public License v3.0+ (see LICENSE or https://www.gnu.org/licenses/gpl-3.0.txt)

from __future__ import (absolute_import, division, print_function)
__metaclass__ = type


DOCUMENTATION = r'''
---
module: ibm_schematics_inventory_info
short_description: Manage C(schematics_inventory) for Schematics Service API.
author: IBM SDK Generator (@ibm)
version_added: "1.0.0"
description:
  - This module retrieves one or more C(schematics_inventory) for Schematics Service API.
requirements:
  - "SchematicsV1"
options:
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
- name: Read ibm_schematics_inventory
  ibm_schematics_inventory_info:
    inventory_id: 'testString'
    profile: 'summary'
'''

RETURN = r'''
name:
  description: "The unique name of your Inventory.  The name can be up to 128 characters long and can
    include alphanumeric  characters, spaces, dashes, and underscores."
  type: str
  returned: on success for read operation
id:
  description: "Inventory id."
  type: str
  returned: on success for read operation
description:
  description: "The description of your Inventory.  The description can be up to 2048 characters long
    in size."
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
  description: "Resource-group name for the Inventory definition.  By default, Inventory will be
    created in Default Resource Group."
  type: str
  returned: on success for read operation
created_at:
  description: "Inventory creation time."
  type: str
  returned: on success for read operation
created_by:
  description: "Email address of user who created the Inventory."
  type: str
  returned: on success for read operation
updated_at:
  description: "Inventory updation time."
  type: str
  returned: on success for read operation
updated_by:
  description: "Email address of user who updated the Inventory."
  type: str
  returned: on success for read operation
inventories_ini:
  description: "Input inventory of host and host group for the playbook,  in the .ini file format."
  type: str
  returned: on success for read operation
resource_queries:
  description: "Input resource queries that is used to dynamically generate  the inventory of host and
    host group for the playbook."
  type: list
  elements: str
  returned: on success for read operation
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
    )

    module = AnsibleModule(
        argument_spec=module_args,
        supports_check_mode=True
    )

    if MISSING_IMPORT_EXC is not None:
        module.fail_json(msg='Missing required import: ' + MISSING_IMPORT_EXC.msg)

    inventory_id = module.params["inventory_id"]
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

    if inventory_id:
        # read
        try:
            response = sdk.get_inventory(
                inventory_id=inventory_id,
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
