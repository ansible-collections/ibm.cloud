#!/usr/bin/python
# coding: utf-8

# (C) Copyright IBM Corp. 2024.
#
# GNU General Public License v3.0+ (see LICENSE or https://www.gnu.org/licenses/gpl-3.0.txt)

from __future__ import (absolute_import, division, print_function)
__metaclass__ = type


DOCUMENTATION = r'''
---
module: ibm_iam_access_group_rule_info
short_description: Manage C(iam_access_group_rule) for IAM Access Groups.
author: - Gannayak Pabra (@Gannayak0722)
version_added: "1.0.0"
description:
  - This module retrieves one or more C(iam_access_group_rule) for IAM Access Groups.
requirements:
  - "IamAccessGroupsV2"
options:
  rule_id:
    description: "The rule to get."
    type: str
  access_group_id:
    description: "The access group identifier."
    type: str
  transaction_id:
    description: "An optional transaction ID can be passed to your request, which can be useful for
      tracking calls through multiple services by using one identifier. The header key
      must be set to Transaction-Id and the value is anything that you choose. If no
      transaction ID is passed in, then a random ID is generated."
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
- name: Read ibm_iam_access_group_rule
  ibm_iam_access_group_rule_info:
    access_group_id: 'testString'
    rule_id: 'testString'
    transaction_id: 'testString'
'''

RETURN = r'''
id:
  description: "The rule id."
  type: str
  returned: on success for read operation
name:
  description: "The name of the rule."
  type: str
  returned: on success for read operation
expiration:
  description: "Session duration in hours. Access group membership is revoked after this time period
    expires. Users must log back in to refresh their access group membership. Must be
    between 1 and 24."
  type: int
  returned: on success for read operation
realm_name:
  description: "The URL of the identity provider."
  type: str
  returned: on success for read operation
access_group_id:
  description: "The group id that the dynamic rule is assigned to."
  type: str
  returned: on success for read operation
account_id:
  description: "The account id that the group is in."
  type: str
  returned: on success for read operation
conditions:
  description: "A list of conditions that identities must satisfy to gain access group membership."
  type: list
  elements: 'dict'
  contains:
    claim:
      description: "The claim to evaluate against. This will be found in the C(ext) claims of a user's
        login request."
      type: str
    operator:
      description: "The operation to perform on the claim."
      type: str
      choices:
        - 'EQUALS'
        - 'EQUALS_IGNORE_CASE'
        - 'IN'
        - 'NOT_EQUALS_IGNORE_CASE'
        - 'NOT_EQUALS'
        - 'CONTAINS'
    value:
      description: "The stringified JSON value that the claim is compared to using the operator."
      type: str
  returned: on success for read operation
created_at:
  description: "The timestamp for when the rule was created."
  type: str
  returned: on success for read operation
created_by_id:
  description: "The C(iam_id) of the entity that created the dynamic rule."
  type: str
  returned: on success for read operation
last_modified_at:
  description: "The timestamp for when the dynamic rule was last edited."
  type: str
  returned: on success for read operation
last_modified_by_id:
  description: "The IAM id that last modified the rule."
  type: str
  returned: on success for read operation
msg:
  description: an error message that describes what went wrong
  type: str
  returned: on error
etag:
  description: The ETag value associated with the C(Rule)
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
        rule_id=dict(
            type='str',
            required=False),
        access_group_id=dict(
            type='str',
            required=False),
        transaction_id=dict(
            type='str',
            required=False),
    )

    module = AnsibleModule(
        argument_spec=module_args,
        supports_check_mode=True
    )

    if MISSING_IMPORT_EXC is not None:
        module.fail_json(msg='Missing required import: ' + MISSING_IMPORT_EXC.msg)

    rule_id = module.params["rule_id"]
    access_group_id = module.params["access_group_id"]
    transaction_id = module.params["transaction_id"]

    if module.check_mode:
        module.exit_json(msg='The module would run with the following parameters: ' + module.paramss)

    authenticator = get_authenticator(service_name='iam_access_groups')
    if authenticator is None:
        module.fail_json(msg='Cannot create the authenticator.')

    sdk = IamAccessGroupsV2(
        authenticator=authenticator,
    )

    sdk.configure_service('iam_access_groups')

    if rule_id:
        # read
        try:
            response = sdk.get_access_group_rule(
                access_group_id=access_group_id,
                rule_id=rule_id,
                transaction_id=transaction_id,
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
