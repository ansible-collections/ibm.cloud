#!/usr/bin/python
# coding: utf-8

# (C) Copyright IBM Corp. 2023.
#
# GNU General Public License v3.0+ (see LICENSE or https://www.gnu.org/licenses/gpl-3.0.txt)

from __future__ import (absolute_import, division, print_function)
__metaclass__ = type


DOCUMENTATION = r'''
---
module: ibm_resource_quotas_info
short_description: Manage C(resource_quotas) for Resource Manager.
author: IBM SDK Generator (@ibm)
version_added: "1.0.0"
description:
  - This module retrieves one or more C(resource_quotas) for Resource Manager.
requirements:
  - "ResourceManagerV2"
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

- name: List ibm_resource_quotas
  ibm_resource_quotas_info:
'''

RETURN = r'''
resources:
  description: "The list of quota definitions."
  type: list
  elements: 'dict'
  contains:
    id:
      description: "An alpha-numeric value identifying the quota."
      type: str
    name:
      description: "The human-readable name of the quota."
      type: str
    type:
      description: "The type of the quota."
      type: str
    number_of_apps:
      description: "The total app limit."
      type: float
    number_of_service_instances:
      description: "The total service instances limit per app."
      type: float
    default_number_of_instances_per_lite_plan:
      description: "Default number of instances per lite plan."
      type: float
    instances_per_app:
      description: "The total instances limit per app."
      type: float
    instance_memory:
      description: "The total memory of app instance."
      type: str
    total_app_memory:
      description: "The total app memory capacity."
      type: str
    vsi_limit:
      description: "The VSI limit."
      type: float
    resource_quotas:
      description: "The resource quotas associated with a quota definition."
      type: list
      elements: 'dict'
      contains:
        id:
          description: "An alpha-numeric value identifying the quota."
          type: str
        resource_id:
          description: "The human-readable name of the quota."
          type: str
        crn:
          description: "The full CRN (cloud resource name) associated with the quota. For more on this format,
            see https://cloud.ibm.com/docs/account?topic=account-crn."
          type: str
        limit:
          description: "The limit number of this resource."
          type: float
    created_at:
      description: "The date when the quota was initially created."
      type: str
    updated_at:
      description: "The date when the quota was last updated."
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
    from ibm_platform_services import ResourceManagerV2
except ImportError as imp_exc:
    MISSING_IMPORT_EXC = imp_exc
else:
    MISSING_IMPORT_EXC = None


def run_module():
    module_args = dict(
    )

    module = AnsibleModule(
        argument_spec=module_args,
        supports_check_mode=True
    )

    if MISSING_IMPORT_EXC is not None:
        module.fail_json(msg='Missing required import: ' + MISSING_IMPORT_EXC.msg)

    if module.check_mode:
        module.exit_json(msg='The module would run with the following parameters: ' + module.paramss)

    authenticator = get_authenticator(service_name='resource_manager')
    if authenticator is None:
        module.fail_json(msg='Cannot create the authenticator.')

    sdk = ResourceManagerV2(
        authenticator=authenticator,
    )

    sdk.configure_service('resource_manager')

    # list
    try:
        response = sdk.list_quota_definitions(
        )

        result = response.get_result()

        module.exit_json(**result)
    except ApiException as ex:
        module.fail_json(msg=ex.message)


def main():
    run_module()


if __name__ == '__main__':
    main()
