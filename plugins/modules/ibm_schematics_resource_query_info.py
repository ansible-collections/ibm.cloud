#!/usr/bin/python
# coding: utf-8

# (C) Copyright IBM Corp. 2024.
#
# GNU General Public License v3.0+ (see LICENSE or https://www.gnu.org/licenses/gpl-3.0.txt)

from __future__ import (absolute_import, division, print_function)
__metaclass__ = type


DOCUMENTATION = r'''
---
module: ibm_schematics_resource_query_info
short_description: Manage C(schematics_resource_query) for Schematics Service API.
author: Gannayak Pabra (@Gannayak0722)
version_added: "1.0.0"
description:
  - This module retrieves one or more C(schematics_resource_query) for Schematics Service API.
requirements:
  - "SchematicsV1"
options:
  query_id:
    description: "Resource query Id.  Use C(GET /v2/resource_query) API to look up the Resource query
      definition Ids  in your IBM Cloud account."
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
- name: Read ibm_schematics_resource_query
  ibm_schematics_resource_query_info:
    query_id: 'testString'
'''

RETURN = r'''
type:
  description: "Resource type (cluster, vsi, icd, vpc)."
  type: str
  choices:
    - "vsi"
  returned: on success for read operation
name:
  description: "Resource query name."
  type: str
  returned: on success for read operation
id:
  description: "Resource Query id."
  type: str
  returned: on success for read operation
created_at:
  description: "Resource query creation time."
  type: str
  returned: on success for read operation
created_by:
  description: "Email address of user who created the Resource query."
  type: str
  returned: on success for read operation
updated_at:
  description: "Resource query updation time."
  type: str
  returned: on success for read operation
updated_by:
  description: "Email address of user who updated the Resource query."
  type: str
  returned: on success for read operation
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
  returned: on success for read operation
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
        query_id=dict(
            type='str',
            required=False),
    )

    module = AnsibleModule(
        argument_spec=module_args,
        supports_check_mode=True
    )

    if MISSING_IMPORT_EXC is not None:
        module.fail_json(msg='Missing required import: ' + MISSING_IMPORT_EXC.msg)

    query_id = module.params["query_id"]

    if module.check_mode:
        module.exit_json(msg='The module would run with the following parameters: ' + module.paramss)

    authenticator = get_authenticator(service_name='schematics')
    if authenticator is None:
        module.fail_json(msg='Cannot create the authenticator.')

    sdk = SchematicsV1(
        authenticator=authenticator,
    )

    sdk.configure_service('schematics')

    if query_id:
        # read
        try:
            response = sdk.get_resources_query(
                query_id=query_id,
            )

            result = response.get_result()

            module.exit_json(**result)
        except ApiException as ex:
            module.fail_json(msg=ex.message)


def main():
    run_module()


if __name__ == '__main__':
    main()
