#!/usr/bin/python
# coding: utf-8

# (C) Copyright IBM Corp. 2023.
#
# GNU General Public License v3.0+ (see LICENSE or https://www.gnu.org/licenses/gpl-3.0.txt)

from __future__ import (absolute_import, division, print_function)
__metaclass__ = type


DOCUMENTATION = r'''
---
module: ibm_resource_key_info
short_description: Manage C(resource_key) for Resource Controller.
author:
  - Kavya Handadi (@kavya498)
  - Umar Ali (@umarali-nagoor)
version_added: "1.0.0"
description:
  - This module retrieves one or more C(resource_key) for Resource Controller.
requirements:
  - "ResourceControllerV2"
options:
  id:
    description: "The resource key URL-encoded CRN or GUID."
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
- name: Read ibm_resource_key
  ibm_resource_key_info:
    id: 'testString'
'''

RETURN = r'''
id:
  description: "The ID associated with the key."
  type: str
  returned: on success for read operation
guid:
  description: "The GUID of the key."
  type: str
  returned: on success for read operation
url:
  description: "When you created a new key, a relative URL path is created identifying the location of
    the key."
  type: str
  returned: on success for read operation
created_at:
  description: "The date when the key was created."
  type: str
  returned: on success for read operation
updated_at:
  description: "The date when the key was last updated."
  type: str
  returned: on success for read operation
deleted_at:
  description: "The date when the key was deleted."
  type: str
  returned: on success for read operation
created_by:
  description: "The subject who created the key."
  type: str
  returned: on success for read operation
updated_by:
  description: "The subject who updated the key."
  type: str
  returned: on success for read operation
deleted_by:
  description: "The subject who deleted the key."
  type: str
  returned: on success for read operation
source_crn:
  description: "The CRN of resource instance or alias associated to the key."
  type: str
  returned: on success for read operation
name:
  description: "The human-readable name of the key."
  type: str
  returned: on success for read operation
crn:
  description: "The full Cloud Resource Name (CRN) associated with the key. For more information about
    this format, see [Cloud Resource
    Names](https://cloud.ibm.com/docs/overview?topic=overview-crn)."
  type: str
  returned: on success for read operation
state:
  description: "The state of the key."
  type: str
  returned: on success for read operation
account_id:
  description: "An alpha-numeric value identifying the account ID."
  type: str
  returned: on success for read operation
resource_group_id:
  description: "The ID of the resource group."
  type: str
  returned: on success for read operation
resource_id:
  description: "The unique ID of the offering. This value is provided by and stored in the global
    catalog."
  type: str
  returned: on success for read operation
credentials:
  description: "The credentials for the key. Additional key-value pairs are passed through from the
    resource brokers. After a credential is created for a service, it can be viewed at any
    time for users that need the API key value. However, all users must have the correct
    level of access to see the details of a credential that includes the API key value.
    For additional details, see [viewing a
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
  returned: on success for read operation
iam_compatible:
  description: "Specifies whether the key's credentials support IAM."
  type: bool
  returned: on success for read operation
migrated:
  description: "A boolean that dictates if the alias was migrated from a previous CF instance."
  type: bool
  returned: on success for read operation
resource_instance_url:
  description: "The relative path to the resource."
  type: str
  returned: on success for read operation
resource_alias_url:
  description: "The relative path to the resource alias that this binding is associated with."
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
    from ibm_platform_services import ResourceControllerV2
except ImportError as imp_exc:
    MISSING_IMPORT_EXC = imp_exc
else:
    MISSING_IMPORT_EXC = None


def run_module():
    module_args = dict(
        id=dict(
            type='str',
            required=False),
    )

    module = AnsibleModule(
        argument_spec=module_args,
        supports_check_mode=True
    )

    if MISSING_IMPORT_EXC is not None:
        module.fail_json(msg='Missing required import: ' + MISSING_IMPORT_EXC.msg)

    id = module.params["id"]

    if module.check_mode:
        module.exit_json(msg='The module would run with the following parameters: ' + module.paramss)

    authenticator = get_authenticator(service_name='resource_controller')
    if authenticator is None:
        module.fail_json(msg='Cannot create the authenticator.')

    sdk = ResourceControllerV2(
        authenticator=authenticator,
    )

    sdk.configure_service('resource_controller')

    if id:
        # read
        try:
            response = sdk.get_resource_key(
                id=id,
            )

            result = response.get_result()

            module.exit_json(**result)
        except ApiException as ex:
            module.fail_json(msg=ex.message)


def main():
    run_module()


if __name__ == '__main__':
    main()
