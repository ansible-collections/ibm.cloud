#!/usr/bin/python
# coding: utf-8

# (C) Copyright IBM Corp. 2024.
#
# GNU General Public License v3.0+ (see LICENSE or https://www.gnu.org/licenses/gpl-3.0.txt)

from __future__ import (absolute_import, division, print_function)
__metaclass__ = type


DOCUMENTATION = r'''
---
module: ibm_iam_service_policy_info
short_description: Manage C(iam_service_policy) for IAM Policy Management.
author: Gannayak Pabra (@Gannayak0722)
version_added: "1.0.0"
description:
  - This module retrieves one or more C(iam_service_policy) for IAM Policy Management.
requirements:
  - "IamPolicyManagementV1"
options:
  policy_id:
    description: "The policy ID."
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
- name: Read ibm_iam_service_policy
  ibm_iam_service_policy_info:
    policy_id: 'testString'
'''

RETURN = r'''
id:
  description: "The policy ID."
  type: str
  returned: on success for read operation
type:
  description: "The policy type; either 'access' or 'authorization'."
  type: str
  returned: on success for read operation
description:
  description: "Customer-defined description."
  type: str
  returned: on success for read operation
subjects:
  description: "The subjects associated with a policy."
  type: list
  elements: 'dict'
  contains:
    attributes:
      description: "List of subject attributes."
      type: list
      elements: 'dict'
      contains:
        name:
          description: "The name of an attribute."
          type: str
        value:
          description: "The value of an attribute."
          type: str
  returned: on success for read operation
roles:
  description: "A set of role cloud resource names (CRNs) granted by the policy."
  type: list
  elements: 'dict'
  contains:
    role_id:
      description: "The role Cloud Resource Name (CRN) granted by the policy. Example CRN:
        'crn:v1:bluemix:public:iam::::role:Editor'."
      type: str
    display_name:
      description: "The display name of the role."
      type: str
    description:
      description: "The description of the role."
      type: str
  returned: on success for read operation
resources:
  description: "The resources associated with a policy."
  type: list
  elements: 'dict'
  contains:
    attributes:
      description: "List of resource attributes."
      type: list
      elements: 'dict'
      contains:
        name:
          description: "The name of an attribute."
          type: str
        value:
          description: "The value of an attribute."
          type: str
        operator:
          description: "The operator of an attribute."
          type: str
    tags:
      description: "List of access management tags."
      type: list
      elements: 'dict'
      contains:
        name:
          description: "The name of an access management tag."
          type: str
        value:
          description: "The value of an access management tag."
          type: str
        operator:
          description: "The operator of an access management tag."
          type: str
  returned: on success for read operation
template:
  description: "The details of the IAM template that was used to create an enterprise-managed policy
    in your account. When returned, this indicates that the policy is created from and
    managed by a template in the root enterprise account."
  type: dict
  contains:
    id:
      description: "The policy template ID."
      type: str
    version:
      description: "Template version."
      type: str
    assignment_id:
      description: "policy assignment id."
      type: str
    root_id:
      description: "orchestrator template id."
      type: str
    root_version:
      description: "orchestrator template version."
      type: str
  returned: on success for read operation
msg:
  description: an error message that describes what went wrong
  type: str
  returned: on error
etag:
  description: The ETag value associated with the C(PolicyTemplateMetaData)
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
        policy_id=dict(
            type='str',
            required=False),
    )

    module = AnsibleModule(
        argument_spec=module_args,
        supports_check_mode=True
    )

    if MISSING_IMPORT_EXC is not None:
        module.fail_json(msg='Missing required import: ' + MISSING_IMPORT_EXC.msg)

    policy_id = module.params["policy_id"]

    if module.check_mode:
        module.exit_json(msg='The module would run with the following parameters: ' + module.paramss)

    authenticator = get_authenticator(service_name='iam_policy_management')
    if authenticator is None:
        module.fail_json(msg='Cannot create the authenticator.')

    sdk = IamPolicyManagementV1(
        authenticator=authenticator,
    )

    sdk.configure_service('iam_policy_management')

    if policy_id:
        # read
        try:
            response = sdk.get_policy(
                policy_id=policy_id,
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
