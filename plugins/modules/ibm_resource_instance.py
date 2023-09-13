#!/usr/bin/python
# coding: utf-8

# (C) Copyright IBM Corp. 2023.
#
# GNU General Public License v3.0+ (see LICENSE or https://www.gnu.org/licenses/gpl-3.0.txt)

from __future__ import (absolute_import, division, print_function)
__metaclass__ = type


DOCUMENTATION = r'''
---
module: ibm_resource_instance
short_description: Manage C(resource_instances) for Resource Controller.
author:
  - Kavya Handadi (@kavya498)
  - Umar Ali (@umarali-nagoor)
version_added: "1.0.0"
description:
  - This module creates, updates, or deletes a C(resource_instance) resource for Resource Controller.
requirements:
  - "ResourceControllerV2"
options:
  resource_group:
    description: "The ID of the resource group."
    type: str
  allow_cleanup:
    description: "A boolean that dictates if the resource instance should be deleted (cleaned up)
      during the processing of a region instance delete call."
    type: bool
  name:
    description: "The name of the instance. Must be 180 characters or less and cannot include any
      special characters other than C((space) - . _ :)."
    type: str
  parameters:
    description: "Configuration options represented as key-value pairs that are passed through to the
      target resource brokers."
    type: dict
  target:
    description: "The deployment location where the instance should be hosted."
    type: str
  tags:
    description: "Tags that are attached to the instance after provisioning. These tags can be
      searched and managed through the Tagging API in IBM Cloud."
    type: list
    elements: str
  entity_lock:
    description: "Indicates if the resource instance is locked for further update or delete
      operations. It does not affect actions performed on child resources like aliases,
      bindings or keys. False by default."
    type: bool
  id:
    description: "The resource instance URL-encoded CRN or GUID."
    type: str
  recursive:
    description: "Will delete resource bindings, keys and aliases associated with the instance."
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
- name: Create ibm_resource_instance
  ibm_resource_instance:
    name: 'ExampleResourceInstance'
    target: 'global'
    resource_group: '13aa3ee48c3b44ddb64c05c79f7ab8ef'
    tags: ['testString']
    allow_cleanup: False
    parameters: {'anyKey': 'anyValue'}
    entity_lock: False
    state: present

- name: Update ibm_resource_instance
  ibm_resource_instance:
    id: 'testString'
    name: 'UpdatedExampleResourceInstance'
    parameters: {'exampleProperty':'exampleValue'}
    allow_cleanup: True
    state: present

- name: Delete ibm_resource_instance
  ibm_resource_instance:
    id: 'testString'
    recursive: False
    state: absent
'''

RETURN = r'''
name:
  description: "The name of the instance. Must be 180 characters or less and cannot include any
    special characters other than C((space) - . _ :)."
  type: str
  returned: on success for create, update operations
target:
  description: "The deployment location where the instance should be hosted."
  type: str
  returned: on success for create, update operations
resource_group:
  description: "The ID of the resource group."
  type: str
  returned: on success for create, update operations
tags:
  description: "Tags that are attached to the instance after provisioning. These tags can be searched
    and managed through the Tagging API in IBM Cloud."
  type: list
  elements: str
  returned: on success for create, update operations
allow_cleanup:
  description: "A boolean that dictates if the resource instance should be deleted (cleaned up) during
    the processing of a region instance delete call."
  type: bool
  returned: on success for create, update operations
parameters:
  description: "Configuration options represented as key-value pairs that are passed through to the
    target resource brokers."
  type: dict
  returned: on success for create, update operations
id:
  description: "ID of the deleted resource"
  type: str
  returned: on success for delete operation
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
    from ..module_utils import config
    from ..module_utils import catalog
    from ..module_utils.auth import get_authenticator
    from ibm_cloud_sdk_core import ApiException
    from ibm_platform_services import ResourceControllerV2
except ImportError as imp_exc:
    MISSING_IMPORT_EXC = imp_exc
else:
    MISSING_IMPORT_EXC = None


def run_module():
    module_args = dict(
        name=dict(
            type='str',
            required=False),
        service=dict(
            type='str',
            required=False),
        plan=dict(
            type='str',
            required=False),
        location=dict(
            type='str',
            required=False),
        resource_group=dict(
            type='str',
            required=False),
        allow_cleanup=dict(
            type='bool',
            required=False),
        parameters=dict(
            type='dict',
            required=False),
        tags=dict(
            type='list',
            elements=str,
            required=False),
        entity_lock=dict(
            type='bool',
            required=False),
        id=dict(
            type='str',
            required=False),
        recursive=dict(
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
    service = module.params["service"]  # handcoded argument
    location = module.params["location"]  # renamed target to location
    plan = module.params["plan"]  # renamed resource_plan_id to plan
    resource_group = module.params["resource_group"]
    allow_cleanup = module.params["allow_cleanup"]
    parameters = module.params["parameters"]
    tags = module.params["tags"]
    entity_lock = module.params["entity_lock"]
    id = module.params["id"]
    recursive = module.params["recursive"]
    state = module.params["state"]
    

    authenticator = get_authenticator(service_name='resource_controller')
    if authenticator is None:
        module.fail_json(msg='Cannot create the authenticator.')

    sdk = ResourceControllerV2(
        authenticator=authenticator,
    )

    sdk.configure_service('resource_controller')

    resource_exists = True

    # Check for existence
    if id:
        try:
            sdk.get_resource_instance(
                id=id,
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
                sdk.delete_resource_instance(
                    id=id,
                    recursive=recursive,
                )
            except ApiException as ex:
                module.fail_json(msg=ex.message)
            else:
                module.exit_json(changed=True, id=id, status="deleted")
        else:
            module.exit_json(changed=False, id=id, status="not_found")

    if state == "present":
        catalogCRN, servicePlanID = '', ''
        if not resource_exists:
            if service is not None:
                serviceID, catalogCRN, servicePlanID = catalog.get_serviceID_targetCRN_planID(
                    service, plan, location)
            # Create path
            try:
                result = sdk.create_resource_instance(
                    name=name,
                    target=catalogCRN,
                    resource_group=resource_group,
                    resource_plan_id=servicePlanID,
                    tags=tags,
                    allow_cleanup=allow_cleanup,
                    parameters=parameters,
                    entity_lock=entity_lock,
                ).get_result()
            except ApiException as ex:
                module.fail_json(msg=ex.message)
            else:
                module.exit_json(changed=True, msg=result)
        else:
            # Update path
            try:
                result = sdk.update_resource_instance(
                    id=id,
                    name=name,
                    parameters=parameters,
                    resource_plan_id=plan,
                    allow_cleanup=allow_cleanup,
                ).get_result()
            except ApiException as ex:
                module.fail_json(msg=ex.message)
            else:
                module.exit_json(changed=True, msg=result)


def main():
    run_module()


if __name__ == '__main__':
    main()
