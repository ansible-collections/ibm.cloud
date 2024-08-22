#!/usr/bin/python
# coding: utf-8

# (C) Copyright IBM Corp. 2024.
#
# GNU General Public License v3.0+ (see LICENSE or https://www.gnu.org/licenses/gpl-3.0.txt)

from __future__ import (absolute_import, division, print_function)
__metaclass__ = type


DOCUMENTATION = r'''
---
module: ibm_iam_profile_link
short_description: Manage C(iam_profile_links) for IAM Identity Services.
author: Gannayak Pabra (@Gannayak0722)
version_added: "1.0.0"
description:
  - This module creates, updates, or deletes an C(iam_profile_link) resource for IAM Identity Services.
requirements:
  - "IamIdentityV1"
options:
  cr_type:
    description: "The compute resource type. Valid values are VSI, IKSI(SA, ROKS)SA."
    type: str
  link:
    description: "Link details."
    type: dict
    suboptions:
      crn:
        description: "The CRN of the compute resource."
        type: str
      namespace:
        description: "The compute resource namespace, only required if cr_type is IKS_SA or ROKS_SA."
        type: str
      name:
        description: "Name of the compute resource, only required if cr_type is IKS_SA or ROKS_SA."
        type: str
  name:
    description: "Optional name of the Link."
    type: str
  link_id:
    description: "ID of the link."
    type: str
  profile_id:
    description: "ID of the trusted profile."
    type: str
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
- name: Create ibm_iam_profile_link
  vars:
    create_profile_link_request_link_model:
      crn: 'testString'
      namespace: 'testString'
      name: 'testString'
  ibm_iam_profile_link:
    profile_id: 'testString'
    cr_type: 'testString'
    link: '{{ create_profile_link_request_link_model }}'
    name: 'testString'
    state: present

- name: Delete ibm_iam_profile_link
  ibm_iam_profile_link:
    profile_id: 'testString'
    link_id: 'testString'
    state: absent
'''

RETURN = r'''
id:
  description: "the unique identifier of the link."
  type: str
  returned: on success for create, delete operations
entity_tag:
  description: "version of the link."
  type: str
  returned: on success for create operation
created_at:
  description: "If set contains a date time string of the creation date in ISO format."
  type: str
  returned: on success for create operation
modified_at:
  description: "If set contains a date time string of the last modification date in ISO format."
  type: str
  returned: on success for create operation
name:
  description: "Optional name of the Link."
  type: str
  returned: on success for create operation
cr_type:
  description: "The compute resource type. Valid values are VSI, IKSI(SA, ROKS)SA."
  type: str
  returned: on success for create operation
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
  returned: on success for create operation
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
        cr_type=dict(
            type='str',
            required=False),
        # Represents the CreateProfileLinkRequestLink Python class
        link=dict(
            type='dict',
            options=dict(
                crn=dict(
                    type='str',
                    required=False),
                namespace=dict(
                    type='str',
                    required=False),
                name=dict(
                    type='str',
                    required=False),
            ),
            required=False),
        name=dict(
            type='str',
            required=False),
        link_id=dict(
            type='str',
            required=False),
        profile_id=dict(
            type='str',
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

    cr_type = module.params["cr_type"]
    link = module.params["link"]
    name = module.params["name"]
    link_id = module.params["link_id"]
    profile_id = module.params["profile_id"]
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
    if link_id:
        try:
            sdk.get_link(
                profile_id=profile_id,
                link_id=link_id,
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
                sdk.delete_link(
                    profile_id=profile_id,
                    link_id=link_id,
                )
            except ApiException as ex:
                module.fail_json(msg=ex.message)
            else:
                module.exit_json(changed=True, id=link_id, status="deleted")
        else:
            module.exit_json(changed=False, id=link_id, status="not_found")

    if state == "present":
        if not resource_exists:
            # Create path
            try:
                response = sdk.create_link(
                    profile_id=profile_id,
                    cr_type=cr_type,
                    link=link,
                    name=name,
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
