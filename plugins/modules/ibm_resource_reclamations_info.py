#!/usr/bin/python
# coding: utf-8

# (C) Copyright IBM Corp. 2023.
#
# GNU General Public License v3.0+ (see LICENSE or https://www.gnu.org/licenses/gpl-3.0.txt)

from __future__ import (absolute_import, division, print_function)
__metaclass__ = type


DOCUMENTATION = r'''
---
module: ibm_resource_reclamations_info
short_description: Manage C(resource_reclamations) for Resource Controller.
author:
  - Kavya Handadi (@kavya498)
  - Umar Ali (@umarali-nagoor)
version_added: "1.0.0"
description:
  - This module retrieves one or more C(resource_reclamations) for Resource Controller.
requirements:
  - "ResourceControllerV2"
options:
  account_id:
    description: "An alpha-numeric value identifying the account ID."
    type: str
  resource_group_id:
    description: "The ID of the resource group."
    type: str
  resource_instance_id:
    description: "The GUID of the resource instance."
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

- name: List ibm_resource_reclamations
  ibm_resource_reclamations_info:
    account_id: 'testString'
    resource_instance_id: 'testString'
    resource_group_id: 'testString'
'''

RETURN = r'''
resources:
  description: "A list of reclamations."
  type: list
  elements: 'dict'
  contains:
    id:
      description: "The ID associated with the reclamation."
      type: str
    entity_id:
      description: "The ID of the entity for the reclamation."
      type: str
    entity_type_id:
      description: "The ID of the entity type for the reclamation."
      type: str
    entity_crn:
      description: "The full Cloud Resource Name (CRN) associated with the binding. For more information
        about this format, see [Cloud Resource
        Names](https://cloud.ibm.com/docs/overview?topic=overview-crn)."
      type: str
    resource_instance_id:
      description: "The ID of the resource instance."
      type: str
    resource_group_id:
      description: "The ID of the resource group."
      type: str
    account_id:
      description: "An alpha-numeric value identifying the account ID."
      type: str
    policy_id:
      description: "The ID of policy for the reclamation."
      type: str
    state:
      description: "The state of the reclamation."
      type: str
    target_time:
      description: "The target time that the reclamation retention period end."
      type: str
    custom_properties:
      description: "The custom properties of the reclamation."
      type: dict
    created_at:
      description: "The date when the reclamation was created."
      type: str
    created_by:
      description: "The subject who created the reclamation."
      type: str
    updated_at:
      description: "The date when the reclamation was last updated."
      type: str
    updated_by:
      description: "The subject who updated the reclamation."
      type: str
  returned: on success for list operation
msg:
  description: an error message that describes what went wrong
  type: str
  returned: on error
'''


from ansible.module_utils.basic import AnsibleModule

try:
    from ..module_utils.auth import get_authenticator
    from ibm_cloud_sdk_core import ApiException
    from ibm_platform_services import ResourceControllerV2
except ImportError as imp_exc:
    MISSING_IMPORT_EXC = imp_exc
else:
    MISSING_IMPORT_EXC = None


def run_module():
    module_args = dict(
        account_id=dict(
            type='str',
            required=False),
        resource_group_id=dict(
            type='str',
            required=False),
        resource_instance_id=dict(
            type='str',
            required=False),
    )

    module = AnsibleModule(
        argument_spec=module_args,
        supports_check_mode=True
    )

    if MISSING_IMPORT_EXC is not None:
        module.fail_json(msg='Missing required import: ' + MISSING_IMPORT_EXC.msg)

    account_id = module.params["account_id"]
    resource_group_id = module.params["resource_group_id"]
    resource_instance_id = module.params["resource_instance_id"]

    if module.check_mode:
        module.exit_json(msg='The module would run with the following parameters: ' + module.paramss)

    authenticator = get_authenticator(service_name='resource_controller')
    if authenticator is None:
        module.fail_json(msg='Cannot create the authenticator.')

    sdk = ResourceControllerV2(
        authenticator=authenticator,
    )

    sdk.configure_service('resource_controller')

    # list
    try:
        response = sdk.list_reclamations(
            account_id=account_id,
            resource_instance_id=resource_instance_id,
            resource_group_id=resource_group_id,
        )

        result = response.get_result()

        module.exit_json(**result)
    except ApiException as ex:
        module.fail_json(msg=ex.message)


def main():
    run_module()


if __name__ == '__main__':
    main()
