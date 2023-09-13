#!/usr/bin/python
# coding: utf-8

# (C) Copyright IBM Corp. 2023.
#
# GNU General Public License v3.0+ (see LICENSE or https://www.gnu.org/licenses/gpl-3.0.txt)

from __future__ import (absolute_import, division, print_function)
__metaclass__ = type


DOCUMENTATION = r'''
---
module: ibm_resource_bindings_info
short_description: Manage C(resource_bindings) for Resource Controller.
author:
  - Kavya Handadi (@kavya498)
  - Umar Ali (@umarali-nagoor)
version_added: "1.0.0"
description:
  - This module retrieves one or more C(resource_bindings) for Resource Controller.
requirements:
  - "ResourceControllerV2"
options:
  resource_group_id:
    description: "The ID of the resource group."
    type: str
  updated_from:
    description: "Start date inclusive filter."
    type: str
  name:
    description: "The human-readable name of the binding."
    type: str
  limit:
    description: "Limit on how many items should be returned."
    type: int
  guid:
    description: "The GUID of the binding."
    type: str
  resource_id:
    description: "The unique ID of the offering (service name). This value is provided by and stored
      in the global catalog."
    type: str
  updated_to:
    description: "End date inclusive filter."
    type: str
  region_binding_id:
    description: "The ID of the binding in the target environment. For example, C(serviceI(binding)id)
      in a given IBM Cloud environment."
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

- name: List ibm_resource_bindings
  ibm_resource_bindings_info:
    guid: 'testString'
    name: 'testString'
    resource_group_id: 'testString'
    resource_id: 'testString'
    region_binding_id: 'testString'
    limit: 100
    updated_from: '2021-01-01'
    updated_to: '2021-01-01'
'''

RETURN = r'''
resources:
  description: "A list with all ResourceBinding instances."
  type: list
  elements: 'dict'
  contains:
    id:
      description: "The ID associated with the binding."
      type: str
    guid:
      description: "The GUID of the binding."
      type: str
    url:
      description: "When you provision a new binding, a relative URL path is created identifying the
        location of the binding."
      type: str
    created_at:
      description: "The date when the binding was created."
      type: str
    updated_at:
      description: "The date when the binding was last updated."
      type: str
    deleted_at:
      description: "The date when the binding was deleted."
      type: str
    created_by:
      description: "The subject who created the binding."
      type: str
    updated_by:
      description: "The subject who updated the binding."
      type: str
    deleted_by:
      description: "The subject who deleted the binding."
      type: str
    source_crn:
      description: "The CRN of resource alias associated to the binding."
      type: str
    target_crn:
      description: "The CRN of target resource, for example, application, in a specific environment."
      type: str
    crn:
      description: "The full Cloud Resource Name (CRN) associated with the binding. For more information
        about this format, see [Cloud Resource
        Names](https://cloud.ibm.com/docs/overview?topic=overview-crn)."
      type: str
    region_binding_id:
      description: "The ID of the binding in the target environment. For example, C(serviceI(binding)id)
        in a given IBM Cloud environment."
      type: str
    region_binding_crn:
      description: "The CRN of the binding in the target environment."
      type: str
    name:
      description: "The human-readable name of the binding."
      type: str
    account_id:
      description: "An alpha-numeric value identifying the account ID."
      type: str
    resource_group_id:
      description: "The ID of the resource group."
      type: str
    state:
      description: "The state of the binding."
      type: str
    credentials:
      description: "The credentials for the binding. Additional key-value pairs are passed through from
        the resource brokers. After a credential is created for a service, it can be viewed at
        any time for users that need the API key value. However, all users must have the
        correct level of access to see the details of a credential that includes the API key
        value. For additional details, see [viewing a
        credential](https://cloud.ibm.com/docs/account?topic=account-service_credentials&interface=ui#viewing-credentials-ui)
        or the service's documentation."
      type: dict
      contains:
        redacted:
          description: "If present, the user doesn't have the correct access to view the credentials and the
            details are redacted.  The string value identifies the level of access that's required
            to view the credential. For additional information, see [viewing a
            credential](https://cloud.ibm.com/docs/account?topic=account-service_credentials&interface=ui#viewing-credentials-ui)."
          type: str
          choices:
            - 'REDACTED'
            - 'REDACTED_EXPLICIT'
        apikey:
          description: "The API key for the credentials."
          type: str
        iam_apikey_description:
          description: "The optional description of the API key."
          type: str
        iam_apikey_name:
          description: "The name of the API key."
          type: str
        iam_role_crn:
          description: "The Cloud Resource Name for the role of the credentials."
          type: str
        iam_serviceid_crn:
          description: "The Cloud Resource Name for the service ID of the credentials."
          type: str
    iam_compatible:
      description: "Specifies whether the binding's credentials support IAM."
      type: bool
    resource_id:
      description: "The unique ID of the offering. This value is provided by and stored in the global
        catalog."
      type: str
    migrated:
      description: "A boolean that dictates if the alias was migrated from a previous CF instance."
      type: bool
    resource_alias_url:
      description: "The relative path to the resource alias that this binding is associated with."
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
    from ibm_platform_services.resource_controller_v2 import ResourceBindingsPager
except ImportError as imp_exc:
    MISSING_IMPORT_EXC = imp_exc
else:
    MISSING_IMPORT_EXC = None


def run_module():
    module_args = dict(
        resource_group_id=dict(
            type='str',
            required=False),
        updated_from=dict(
            type='str',
            required=False),
        name=dict(
            type='str',
            required=False),
        limit=dict(
            type='int',
            required=False),
        guid=dict(
            type='str',
            required=False),
        resource_id=dict(
            type='str',
            required=False),
        updated_to=dict(
            type='str',
            required=False),
        region_binding_id=dict(
            type='str',
            required=False),
    )

    module = AnsibleModule(
        argument_spec=module_args,
        supports_check_mode=True
    )

    if MISSING_IMPORT_EXC is not None:
        module.fail_json(msg='Missing required import: ' + MISSING_IMPORT_EXC.msg)

    resource_group_id = module.params["resource_group_id"]
    updated_from = module.params["updated_from"]
    name = module.params["name"]
    limit = module.params["limit"]
    guid = module.params["guid"]
    resource_id = module.params["resource_id"]
    updated_to = module.params["updated_to"]
    region_binding_id = module.params["region_binding_id"]

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
        pager = ResourceBindingsPager(
            client=sdk,
            guid=guid,
            name=name,
            resource_group_id=resource_group_id,
            resource_id=resource_id,
            region_binding_id=region_binding_id,
            limit=limit,
            updated_from=updated_from,
            updated_to=updated_to,
        )
        result = pager.get_all()
        module.exit_json(resources=result)
    except ApiException as ex:
        module.fail_json(msg=ex.message)


def main():
    run_module()


if __name__ == '__main__':
    main()
