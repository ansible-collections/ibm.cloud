#!/usr/bin/python
# coding: utf-8

# (C) Copyright IBM Corp. 2024.
#
# GNU General Public License v3.0+ (see LICENSE or https://www.gnu.org/licenses/gpl-3.0.txt)

from __future__ import (absolute_import, division, print_function)
__metaclass__ = type


DOCUMENTATION = r'''
---
module: ibm_iam_profile_claim_rule_info
short_description: Manage C(iam_profile_claim_rule) for IAM Identity Services.
author: Gannayak Pabra (@Gannayak0722)
version_added: "1.0.0"
description:
  - This module retrieves one or more C(iam_profile_claim_rule) for IAM Identity Services.
requirements:
  - "IamIdentityV1"
options:
  rule_id:
    description: "ID of the claim rule to get."
    type: str
  profile_id:
    description: "ID of the trusted profile."
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
- name: Read ibm_iam_profile_claim_rule
  ibm_iam_profile_claim_rule_info:
    profile_id: 'testString'
    rule_id: 'testString'
'''

RETURN = r'''
id:
  description: "the unique identifier of the claim rule."
  type: str
  returned: on success for read operation
entity_tag:
  description: "version of the claim rule."
  type: str
  returned: on success for read operation
created_at:
  description: "If set contains a date time string of the creation date in ISO format."
  type: str
  returned: on success for read operation
modified_at:
  description: "If set contains a date time string of the last modification date in ISO format."
  type: str
  returned: on success for read operation
name:
  description: "The optional claim rule name."
  type: str
  returned: on success for read operation
type:
  description: "Type of the claim rule, either 'Profile-SAML' or 'Profile-CR'."
  type: str
  returned: on success for read operation
realm_name:
  description: "The realm name of the Idp this claim rule applies to."
  type: str
  returned: on success for read operation
expiration:
  description: "Session expiration in seconds."
  type: int
  returned: on success for read operation
cr_type:
  description: "The compute resource type. Not required if type is Profile-SAML. Valid values are VSI,
    IKSI(SA, ROKS)SA."
  type: str
  returned: on success for read operation
conditions:
  description: "Conditions of this claim rule."
  type: list
  elements: 'dict'
  contains:
    claim:
      description: "The claim to evaluate against. [Learn
        more](/docs/account?topic=account-iam-condition-properties&interface=ui#cr-attribute-names)."
      type: str
    operator:
      description: "The operation to perform on the claim. valid values are EQUALS, NOTI(EQUALS,
        EQUALS)IGNOREI(CASE, NOT)EQUALSI(IGNORE)CASE, CONTAINS, IN."
      type: str
    value:
      description: "The stringified JSON value that the claim is compared to using the operator."
      type: str
  returned: on success for read operation
msg:
  description: an error message that describes what went wrong
  type: str
  returned: on error
'''


from ansible.module_utils.basic import AnsibleModule

try:
    from ..module_utils.auth import get_authenticator
    from ibm_cloud_sdk_core import ApiException
    from ibm_platform_services import IamIdentityV1
except ImportError as imp_exc:
    MISSING_IMPORT_EXC = imp_exc
else:
    MISSING_IMPORT_EXC = None


def run_module():
    module_args = dict(
        rule_id=dict(
            type='str',
            required=False),
        profile_id=dict(
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
    profile_id = module.params["profile_id"]

    if module.check_mode:
        module.exit_json(msg='The module would run with the following parameters: ' + module.paramss)

    authenticator = get_authenticator(service_name='iam_identity')
    if authenticator is None:
        module.fail_json(msg='Cannot create the authenticator.')

    sdk = IamIdentityV1(
        authenticator=authenticator,
    )

    sdk.configure_service('iam_identity')

    if rule_id:
        # read
        try:
            response = sdk.get_claim_rule(
                profile_id=profile_id,
                rule_id=rule_id,
            )

            result = response.get_result()

            module.exit_json(**result)
        except ApiException as ex:
            module.fail_json(msg=ex.message)


def main():
    run_module()


if __name__ == '__main__':
    main()
