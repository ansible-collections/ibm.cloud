#!/usr/bin/python
# coding: utf-8

# (C) Copyright IBM Corp. 2023.
#
# GNU General Public License v3.0+ (see LICENSE or https://www.gnu.org/licenses/gpl-3.0.txt)

from __future__ import (absolute_import, division, print_function)
__metaclass__ = type


DOCUMENTATION = r'''
---
module: ibm_resource_binding
short_description: Manage C(resource_bindings) for Resource Controller.
author:
  - Kavya Handadi (@kavya498)
  - Umar Ali (@umarali-nagoor)
version_added: "1.0.0"
description:
  - This module creates, updates, or deletes a C(resource_binding) resource for Resource Controller.
requirements:
  - "ResourceControllerV2"
options:
  role:
    description: "The base IAM service role name (Reader, Writer, or Manager), or the service or
      custom role CRN. Refer to service's documentation for supported roles."
    type: str
  name:
    description: "The name of the binding. Must be 180 characters or less and cannot include any
      special characters other than C((space) - . _ :)."
    type: str
  source:
    description: "The ID of resource alias."
    type: str
  parameters:
    description: "Configuration options represented as key-value pairs. Service defined options are
      passed through to the target resource brokers, whereas platform defined options are
      not."
    type: raw
    suboptions:
      serviceid_crn:
        description: "An optional platform defined option to reuse an existing IAM serviceId for the role
          assignment."
        type: str
  target:
    description: "The CRN of application to bind to in a specific environment, for example, Dallas YP,
      CFEE instance."
    type: str
  id:
    description: "The resource binding URL-encoded CRN or GUID."
    type: str
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
- name: Create ibm_resource_binding
  vars:
    resource_binding_post_parameters_model:
      serviceid_crn: "crn:v1:bluemix:public:iam-identity::a/9fceaa56d1ab84893af6b9eec5ab81bb::serviceid:S\
        erviceId-fe4c29b5-db13-410a-bacc-b5779a03d393"
      foo: 'exampleValue'
  ibm_resource_binding:
    source: 'faaec9d8-ec64-44d8-ab83-868632fac6a2'
    target: "crn:v1:staging:public:bluemix:us-south:s/e1773b6e-17b4-40c8-b5ed-d2a1c4b620d7::cf-appli\
      cation:8d9457e0-1303-4f32-b4b3-5525575f6205"
    name: 'ExampleResourceBinding'
    parameters: '{{ resource_binding_post_parameters_model }}'
    role: 'Writer'
    state: present

- name: Update ibm_resource_binding
  ibm_resource_binding:
    id: 'testString'
    name: 'UpdatedExampleResourceBinding'
    state: present

- name: Delete ibm_resource_binding
  ibm_resource_binding:
    id: 'testString'
    state: absent
'''

RETURN = r'''
name:
  description: "The name of the binding. Must be 180 characters or less and cannot include any special
    characters other than C((space) - . _ :)."
  type: str
  returned: on success for create, update operations
source:
  description: "The ID of resource alias."
  type: str
  returned: on success for create, update operations
target:
  description: "The CRN of application to bind to in a specific environment, for example, Dallas YP,
    CFEE instance."
  type: str
  returned: on success for create, update operations
parameters:
  description: "Configuration options represented as key-value pairs. Service defined options are
    passed through to the target resource brokers, whereas platform defined options are
    not."
  type: dict
  contains:
    serviceid_crn:
      description: "An optional platform defined option to reuse an existing IAM serviceId for the role
        assignment."
      type: str
  returned: on success for create, update operations
role:
  description: "The base IAM service role name (Reader, Writer, or Manager), or the service or custom
    role CRN. Refer to service's documentation for supported roles."
  type: str
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
    from ..module_utils.auth import get_authenticator
    from ibm_cloud_sdk_core import ApiException
    from ibm_platform_services import ResourceControllerV2
except ImportError as imp_exc:
    MISSING_IMPORT_EXC = imp_exc
else:
    MISSING_IMPORT_EXC = None


def run_module():
    module_args = dict(
        role=dict(
            type='str',
            required=False),
        name=dict(
            type='str',
            required=False),
        source=dict(
            type='str',
            required=False),
        # Represents the ResourceBindingPostParameters Python class
        parameters=dict(
            type='raw',
            options=dict(
                serviceid_crn=dict(
                    type='str',
                    required=False),
            ),
            required=False),
        target=dict(
            type='str',
            required=False),
        id=dict(
            type='str',
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

    role = module.params["role"]
    name = module.params["name"]
    source = module.params["source"]
    parameters = module.params["parameters"]
    target = module.params["target"]
    id = module.params["id"]
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
            sdk.get_resource_binding(
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
                sdk.delete_resource_binding(
                    id=id,
                )
            except ApiException as ex:
                module.fail_json(msg=ex.message)
            else:
                module.exit_json(changed=True, id=id, status="deleted")
        else:
            module.exit_json(changed=False, id=id, status="not_found")

    if state == "present":
        if not resource_exists:
            # Create path
            try:
                response = sdk.create_resource_binding(
                    source=source,
                    target=target,
                    name=name,
                    parameters=parameters,
                    role=role,
                )
            except ApiException as ex:
                module.fail_json(msg=ex.message)
            else:
                result = response.get_result()

                module.exit_json(changed=True, **result)
        else:
            # Update path
            try:
                response = sdk.update_resource_binding(
                    id=id,
                    name=name,
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
