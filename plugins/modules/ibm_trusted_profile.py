#!/usr/bin/python
# coding: utf-8

# (C) Copyright IBM Corp. 2024.
#
# GNU General Public License v3.0+ (see LICENSE or https://www.gnu.org/licenses/gpl-3.0.txt)

from __future__ import (absolute_import, division, print_function)
__metaclass__ = type


DOCUMENTATION = r'''
---
module: ibm_trusted_profile
short_description: Manage C(trusted_profiles) for IAM Identity Services.
author: Gannayak Pabra (@Gannayak0722)
version_added: "1.0.0"
description:
  - This module creates, updates, or deletes a C(trusted_profile) resource for IAM Identity Services.
requirements:
  - "IamIdentityV1"
options:
  account_id:
    description: "The account ID of the trusted profile."
    type: str
  name:
    description: "Name of the trusted profile. The name is checked for uniqueness. Therefore trusted
      profiles with the same names can not exist in the same account."
    type: str
  description:
    description: "The optional description of the trusted profile. The 'description' property is only
      available if a description was provided during creation of trusted profile."
    type: str
  if_match:
    description: "Version of the trusted profile to be updated. Specify the version that you retrived
      when reading list of trusted profiles. This value helps to identify any parallel
      usage of trusted profile. Pass * to indicate to update any version available. This
      might result in stale updates."
    type: str
  profile_id:
    description: "ID of the trusted profile to get."
    type: str
  include_activity:
    description: "Defines if the entity's activity is included in the response. Retrieving activity
      data is an expensive operation, so only request this when needed."
    type: bool
  state:
    description:
      - Should the resource be present or absent.
    type: str
    default: present
    choices: [present, absent]
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
- name: Create ibm_trusted_profile
  ibm_trusted_profile:
    name: 'testString'
    account_id: 'testString'
    description: 'testString'
    state: present

- name: Update ibm_trusted_profile
  ibm_trusted_profile:
    profile_id: 'testString'
    if_match: 'testString'
    name: 'testString'
    description: 'testString'
    state: present

- name: Delete ibm_trusted_profile
  ibm_trusted_profile:
    profile_id: 'testString'
    state: absent
'''

RETURN = r'''
context:
  description: "Context with key properties for problem determination."
  type: dict
  contains:
    transaction_id:
      description: "The transaction ID of the inbound REST request."
      type: str
    operation:
      description: "The operation of the inbound REST request."
      type: str
    user_agent:
      description: "The user agent of the inbound REST request."
      type: str
    url:
      description: "The URL of that cluster."
      type: str
    instance_id:
      description: "The instance ID of the server instance processing the request."
      type: str
    thread_id:
      description: "The thread ID of the server instance processing the request."
      type: str
    host:
      description: "The host of the server instance processing the request."
      type: str
    start_time:
      description: "The start time of the request."
      type: str
    end_time:
      description: "The finish time of the request."
      type: str
    elapsed_time:
      description: "The elapsed time in msec."
      type: str
    cluster_name:
      description: "The cluster name."
      type: str
  returned: on success for create, update operations
id:
  description: "the unique identifier of the trusted profile.
    Example:'Profile-94497d0d-2ac3-41bf-a993-a49d1b14627c'."
  type: str
  returned: on success for create, update, delete operations
entity_tag:
  description: "Version of the trusted profile details object. You need to specify this value when
    updating the trusted profile to avoid stale updates."
  type: str
  returned: on success for create, update operations
crn:
  description: "Cloud Resource Name of the item. Example Cloud Resource Name:
    'crn:v1:bluemix:public:iam-identity:us-south:a/myaccount::profile:Profile-94497d0d-2ac3-41bf-a993-a49d1b14627c'."
  type: str
  returned: on success for create, update operations
name:
  description: "Name of the trusted profile. The name is checked for uniqueness. Therefore trusted
    profiles with the same names can not exist in the same account."
  type: str
  returned: on success for create, update operations
description:
  description: "The optional description of the trusted profile. The 'description' property is only
    available if a description was provided during a create of a trusted profile."
  type: str
  returned: on success for create, update operations
created_at:
  description: "If set contains a date time string of the creation date in ISO format."
  type: str
  returned: on success for create, update operations
modified_at:
  description: "If set contains a date time string of the last modification date in ISO format."
  type: str
  returned: on success for create, update operations
iam_id:
  description: "The iam_id of this trusted profile."
  type: str
  returned: on success for create, update operations
account_id:
  description: "ID of the account that this trusted profile belong to."
  type: str
  returned: on success for create, update operations
template_id:
  description: "ID of the IAM template that was used to create an enterprise-managed trusted profile
    in your account. When returned, this indicates that the trusted profile is created
    from and managed by a template in the root enterprise account."
  type: str
  returned: on success for create, update operations
assignment_id:
  description: "ID of the assignment that was used to create an enterprise-managed trusted profile in
    your account. When returned, this indicates that the trusted profile is created from
    and managed by a template in the root enterprise account."
  type: str
  returned: on success for create, update operations
ims_account_id:
  description: "IMS acount ID of the trusted profile."
  type: int
  returned: on success for create, update operations
ims_user_id:
  description: "IMS user ID of the trusted profile."
  type: int
  returned: on success for create, update operations
history:
  description: "History of the trusted profile."
  type: list
  elements: 'dict'
  contains:
    timestamp:
      description: "Timestamp when the action was triggered."
      type: str
    iam_id:
      description: "IAM ID of the identity which triggered the action."
      type: str
    iam_id_account:
      description: "Account of the identity which triggered the action."
      type: str
    action:
      description: "Action of the history entry."
      type: str
    params:
      description: "Params of the history entry."
      type: list
      elements: str
    message_:
      description: "Message which summarizes the executed action."
      type: str
  returned: on success for create, update operations
activity:
  description: "No description has been provided."
  type: dict
  contains:
    last_authn:
      description: "Time when the entity was last authenticated."
      type: str
    authn_count:
      description: "Authentication count, number of times the entity was authenticated."
      type: int
  returned: on success for create, update operations
status:
  description: The result status of the deletion
  type: str
  returned: on delete
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
        account_id=dict(
            type='str',
            required=False),
        name=dict(
            type='str',
            required=False),
        description=dict(
            type='str',
            required=False),
        if_match=dict(
            type='str',
            required=False),
        profile_id=dict(
            type='str',
            required=False),
        include_activity=dict(
            type='bool',
            required=False),
        state=dict(
            type='str',
            default='present',
            choices=['absent', 'present'],
            required=False),
    )

    module = AnsibleModule(
        argument_spec=module_args,
        supports_check_mode=False
    )

    if MISSING_IMPORT_EXC is not None:
        module.fail_json(msg='Missing required import: ' + MISSING_IMPORT_EXC.msg)

    account_id = module.params["account_id"]
    name = module.params["name"]
    description = module.params["description"]
    if_match = module.params["if_match"]
    profile_id = module.params["profile_id"]
    include_activity = module.params["include_activity"]
    state = module.params["state"]

    authenticator = get_authenticator(service_name='iam_identity')
    if authenticator is None:
        module.fail_json(msg='Cannot create the authenticator.')

    sdk = IamIdentityV1(
        authenticator=authenticator,
    )

    sdk.configure_service('iam_identity')

    resource_exists = True

    # Check for existence
    if profile_id:
        try:
            sdk.get_profile(
                profile_id=profile_id,
                include_activity=include_activity,
            )
        except ApiException as ex:
            if ex.code == 404:
                resource_exists = False
            else:
                module.fail_json(msg=ex.message)
    else:
        # assume resource does not exist
        resource_exists = False

    # Delete path
    if state == "absent":
        if resource_exists:
            try:
                sdk.delete_profile(
                    profile_id=profile_id,
                )
            except ApiException as ex:
                module.fail_json(msg=ex.message)
            else:
                module.exit_json(changed=True, id=profile_id, status="deleted")
        else:
            module.exit_json(changed=False, id=profile_id, status="not_found")

    if state == "present":
        if not resource_exists:
            # Create path
            try:
                response = sdk.create_profile(
                    name=name,
                    account_id=account_id,
                    description=description,
                )
            except ApiException as ex:
                module.fail_json(msg=ex.message)
            else:
                result = response.get_result()

                module.exit_json(changed=True, **result)
        else:
            # Update path
            try:
                response = sdk.update_profile(
                    profile_id=profile_id,
                    if_match=if_match,
                    name=name,
                    description=description,
                )
            except ApiException as ex:
                module.fail_json(msg=ex.message)
            else:
                result = response.get_result()

                module.exit_json(changed=True, **result)


def main():
    run_module()


if __name__ == '__main__':
    main()
