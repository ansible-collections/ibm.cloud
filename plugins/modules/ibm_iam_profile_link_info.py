#!/usr/bin/python
# coding: utf-8

# (C) Copyright IBM Corp. 2024.
#
# GNU General Public License v3.0+ (see LICENSE or https://www.gnu.org/licenses/gpl-3.0.txt)

from __future__ import (absolute_import, division, print_function)
__metaclass__ = type


DOCUMENTATION = r'''
---
module: ibm_iam_profile_link_info
short_description: Manage C(iam_profile_link) for IAM Identity Services.
author: Gannayak Pabra (@Gannayak0722)
version_added: "1.0.0"
description:
  - This module retrieves one or more C(iam_profile_link) for IAM Identity Services.
requirements:
  - "IamIdentityV1"
options:
  link_id:
    description: "ID of the link."
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
- name: Read ibm_iam_profile_link
  ibm_iam_profile_link_info:
    profile_id: 'testString'
    link_id: 'testString'
'''

RETURN = r'''
id:
  description: "the unique identifier of the link."
  type: str
  returned: on success for read operation
entity_tag:
  description: "version of the link."
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
  description: "Optional name of the Link."
  type: str
  returned: on success for read operation
cr_type:
  description: "The compute resource type. Valid values are VSI, IKSI(SA, ROKS)SA."
  type: str
  returned: on success for read operation
link:
  description: "No description has been provided."
  type: dict
  contains:
    crn:
      description: "The CRN of the compute resource."
      type: str
    namespace:
      description: "The compute resource namespace, only required if cr_type is IKS_SA or ROKS_SA."
      type: str
    name:
      description: "Name of the compute resource, only required if cr_type is IKS_SA or ROKS_SA."
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
        link_id=dict(
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

    link_id = module.params["link_id"]
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

    if link_id:
        # read
        try:
            response = sdk.get_link(
                profile_id=profile_id,
                link_id=link_id,
            )

            result = response.get_result()

            module.exit_json(**result)
        except ApiException as ex:
            module.fail_json(msg=ex.message)


def main():
    run_module()


if __name__ == '__main__':
    main()
