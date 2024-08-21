#!/usr/bin/python
# coding: utf-8

# (C) Copyright IBM Corp. 2024.
#
# GNU General Public License v3.0+ (see LICENSE or https://www.gnu.org/licenses/gpl-3.0.txt)

from __future__ import (absolute_import, division, print_function)
__metaclass__ = type


DOCUMENTATION = r'''
---
module: ibm_iam_service_role_info
short_description: Manage C(iam_service_role) for IAM Policy Management.
author: Gannayak Pabra (@Gannayak0722)
version_added: "1.0.0"
description:
  - This module retrieves one or more C(iam_service_role) for IAM Policy Management.
requirements:
  - "IamPolicyManagementV1"
options:
  role_id:
    description: "The role ID."
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
- name: Read ibm_iam_service_role
  ibm_iam_service_role_info:
    role_id: 'testString'
'''

RETURN = r'''
id:
  description: "The role ID. Composed of hexadecimal characters."
  type: str
  returned: on success for read operation
display_name:
  description: "The display name of the role that is shown in the console."
  type: str
  returned: on success for read operation
description:
  description: "The description of the role."
  type: str
  returned: on success for read operation
actions:
  description: "The actions of the role. For more information, see [IAM roles and
    actions](https://cloud.ibm.com/docs/account?topic=account-iam-service-roles-actions)."
  type: list
  elements: str
  returned: on success for read operation
crn:
  description: "The role Cloud Resource Name (CRN). Example CRN:
    'crn:v1:ibmcloud:public:iam-access-management::a/exampleAccountId::customRole:ExampleRoleName'."
  type: str
  returned: on success for read operation
name:
  description: "The name of the role that is used in the CRN. Can only be alphanumeric and has to be
    capitalized."
  type: str
  returned: on success for read operation
account_id:
  description: "The account GUID."
  type: str
  returned: on success for read operation
service_name:
  description: "The service name."
  type: str
  returned: on success for read operation
created_at:
  description: "The UTC timestamp when the role was created."
  type: str
  returned: on success for read operation
created_by_id:
  description: "The iam ID of the entity that created the role."
  type: str
  returned: on success for read operation
last_modified_at:
  description: "The UTC timestamp when the role was last modified."
  type: str
  returned: on success for read operation
last_modified_by_id:
  description: "The iam ID of the entity that last modified the policy."
  type: str
  returned: on success for read operation
href:
  description: "The href link back to the role."
  type: str
  returned: on success for read operation
msg:
  description: an error message that describes what went wrong
  type: str
  returned: on error
etag:
  description: The ETag value associated with the C(CustomRole)
  returned: on read
  type: str
'''


from ansible.module_utils.basic import AnsibleModule

try:
    from ..module_utils.auth import get_authenticator
    from ibm_cloud_sdk_core import ApiException
    from ibm_platform_services import IamPolicyManagementV1
except ImportError as imp_exc:
    MISSING_IMPORT_EXC = imp_exc
else:
    MISSING_IMPORT_EXC = None


def run_module():
    module_args = dict(
        role_id=dict(
            type='str',
            required=False),
    )

    module = AnsibleModule(
        argument_spec=module_args,
        supports_check_mode=True
    )

    if MISSING_IMPORT_EXC is not None:
        module.fail_json(msg='Missing required import: ' + MISSING_IMPORT_EXC.msg)

    role_id = module.params["role_id"]

    if module.check_mode:
        module.exit_json(msg='The module would run with the following parameters: ' + module.paramss)

    authenticator = get_authenticator(service_name='iam_policy_management')
    if authenticator is None:
        module.fail_json(msg='Cannot create the authenticator.')

    sdk = IamPolicyManagementV1(
        authenticator=authenticator,
    )

    sdk.configure_service('iam_policy_management')

    if role_id:
        # read
        try:
            response = sdk.get_role(
                role_id=role_id,
            )

            result = response.get_result()
            etag = response.get_headers().get('ETag')

            module.exit_json(etag=etag, **result)
        except ApiException as ex:
            module.fail_json(msg=ex.message)


def main():
    run_module()


if __name__ == '__main__':
    main()
