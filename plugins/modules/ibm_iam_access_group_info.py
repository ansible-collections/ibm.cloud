#!/usr/bin/python
# coding: utf-8

# (C) Copyright IBM Corp. 2024.
#
# GNU General Public License v3.0+ (see LICENSE or https://www.gnu.org/licenses/gpl-3.0.txt)

from __future__ import (absolute_import, division, print_function)
__metaclass__ = type


DOCUMENTATION = r'''
---
module: ibm_iam_access_group_info
short_description: Manage C(iam_access_group) for IAM Access Groups.
author: Gannayak Pabra (@Gannayak0722)
version_added: "1.0.0"
description:
  - This module retrieves one or more C(iam_access_group) for IAM Access Groups.
requirements:
  - "IamAccessGroupsV2"
options:
  access_group_id:
    description: "The access group identifier."
    type: str
  transaction_id:
    description: "An optional transaction ID can be passed to your request, which can be useful for
      tracking calls through multiple services by using one identifier. The header key
      must be set to Transaction-Id and the value is anything that you choose. If no
      transaction ID is passed in, then a random ID is generated."
    type: str
  show_federated:
    description: "If showI(federated is true, the group will return an is)federated value that is set
      to true if rules exist for the group."
    type: bool
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
- name: Read ibm_iam_access_groups
  ibm_iam_access_groups_info:
    access_group_id: 'testString'
    transaction_id: 'testString'
    show_federated: False
'''

RETURN = r'''
id:
  description: "The group's access group ID."
  type: str
  returned: on success for read operation
name:
  description: "The group's name."
  type: str
  returned: on success for read operation
description:
  description: "The group's description - if defined."
  type: str
  returned: on success for read operation
account_id:
  description: "The account id where the group was created."
  type: str
  returned: on success for read operation
created_at:
  description: "The timestamp of when the group was created."
  type: str
  returned: on success for read operation
created_by_id:
  description: "The C(iam_id) of the entity that created the group."
  type: str
  returned: on success for read operation
last_modified_at:
  description: "The timestamp of when the group was last edited."
  type: str
  returned: on success for read operation
last_modified_by_id:
  description: "The C(iam_id) of the entity that last modified the group name or description."
  type: str
  returned: on success for read operation
href:
  description: "A url to the given group resource."
  type: str
  returned: on success for read operation
is_federated:
  description: "This is set to true if rules exist for the group."
  type: bool
  returned: on success for read operation
msg:
  description: an error message that describes what went wrong
  type: str
  returned: on error
etag:
  description: The ETag value associated with the C(Group)
  returned: on read
  type: str
'''


from ansible.module_utils.basic import AnsibleModule

try:
    from ..module_utils.auth import get_authenticator
    from ibm_cloud_sdk_core import ApiException
    from ibm_platform_services import IamAccessGroupsV2
except ImportError as imp_exc:
    MISSING_IMPORT_EXC = imp_exc
else:
    MISSING_IMPORT_EXC = None


def run_module():
    module_args = dict(
        access_group_id=dict(
            type='str',
            required=False),
        transaction_id=dict(
            type='str',
            required=False),
        show_federated=dict(
            type='bool',
            required=False),
    )

    module = AnsibleModule(
        argument_spec=module_args,
        supports_check_mode=True
    )

    if MISSING_IMPORT_EXC is not None:
        module.fail_json(msg='Missing required import: ' + MISSING_IMPORT_EXC.msg)

    access_group_id = module.params["access_group_id"]
    transaction_id = module.params["transaction_id"]
    show_federated = module.params["show_federated"]

    if module.check_mode:
        module.exit_json(msg='The module would run with the following parameters: ' + module.paramss)

    authenticator = get_authenticator(service_name='iam_access_groups')
    if authenticator is None:
        module.fail_json(msg='Cannot create the authenticator.')

    sdk = IamAccessGroupsV2(
        authenticator=authenticator,
    )

    sdk.configure_service('iam_access_groups')

    if access_group_id:
        # read
        try:
            response = sdk.get_access_group(
                access_group_id=access_group_id,
                transaction_id=transaction_id,
                show_federated=show_federated,
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
