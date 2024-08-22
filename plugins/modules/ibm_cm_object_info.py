#!/usr/bin/python
# coding: utf-8

# (C) Copyright IBM Corp. 2024.
#
# GNU General Public License v3.0+ (see LICENSE or https://www.gnu.org/licenses/gpl-3.0.txt)

from __future__ import (absolute_import, division, print_function)
__metaclass__ = type


DOCUMENTATION = r'''
---
module: ibm_cm_object_info
short_description: Manage C(cm_object) for Catalog Management API.
author: Gannayak Pabra (@Gannayak0722)
version_added: "1.0.0"
description:
  - This module retrieves one or more C(cm_object) for Catalog Management API.
requirements:
  - "CatalogManagementV1"
options:
  object_identifier:
    description: "Object identifier."
    type: str
  catalog_identifier:
    description: "Catalog identifier."
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
- name: Read ibm_cm_object
  ibm_cm_object_info:
    catalog_identifier: 'testString'
    object_identifier: 'testString'
'''

RETURN = r'''
id:
  description: "unique id."
  type: str
  returned: on success for read operation
rev:
  description: "Cloudant revision."
  type: str
  returned: on success for read operation
name:
  description: "The programmatic name of this object."
  type: str
  returned: on success for read operation
crn:
  description: "The crn for this specific object."
  type: str
  returned: on success for read operation
url:
  description: "The url for this specific object."
  type: str
  returned: on success for read operation
parent_id:
  description: "The parent for this specific object."
  type: str
  returned: on success for read operation
label_i18n:
  description: "A map of translated strings, by language code."
  type: dict
  returned: on success for read operation
label:
  description: "Display name in the requested language."
  type: str
  returned: on success for read operation
tags:
  description: "List of tags associated with this catalog."
  type: list
  elements: str
  returned: on success for read operation
created:
  description: "The date and time this catalog was created."
  type: str
  returned: on success for read operation
updated:
  description: "The date and time this catalog was last updated."
  type: str
  returned: on success for read operation
short_description:
  description: "Short description in the requested language."
  type: str
  returned: on success for read operation
short_description_i18n:
  description: "A map of translated strings, by language code."
  type: dict
  returned: on success for read operation
kind:
  description: "Kind of object."
  type: str
  returned: on success for read operation
publish:
  description: "Publish information."
  type: dict
  contains:
    pc_managed:
      description: "Offering is managed by Partner Center."
      type: bool
    approval_type:
      description: "Determines how the offering gets approved into the public catalog. The values
        supported right now are C(pcI(managed), C(ibm)moduleI(repo), and C(ibm)community)."
      type: str
    publish_approved:
      description: "Offering has been approved to publish to permitted to IBM or Public Catalog."
      type: bool
    share_with_all:
      description: "Denotes public availability of an Offering."
      type: bool
    share_with_ibm:
      description: "Denotes IBM employee availability of an Offering - if share_enabled is true."
      type: bool
    share_enabled:
      description: "Denotes sharing including access list availability of an Offering is enabled."
      type: bool
    original_crn:
      description: "The original offering CRN that this publish entry came from."
      type: str
    public_crn:
      description: "The crn of the public catalog entry of this offering."
      type: str
    approval_record:
      description: "Record describing offering's approval details."
      type: dict
    permit_ibm_public_publish:
      description: "Is it permitted to request publishing to IBM or Public."
      type: bool
    ibm_approved:
      description: "Indicates if this offering has been approved for use by all IBMers."
      type: bool
    public_approved:
      description: "Indicates if this offering has been approved for use by all IBM Cloud users."
      type: bool
  returned: on success for read operation
state:
  description: "Offering state."
  type: dict
  contains:
    current:
      description: "one of: new, validated, consumable."
      type: str
    current_entered:
      description: "Date and time of current request."
      type: str
    pending:
      description: "one of: new, validated, consumable."
      type: str
    pending_requested:
      description: "Date and time of pending request."
      type: str
    previous:
      description: "one of: new, validated, consumable."
      type: str
  returned: on success for read operation
catalog_id:
  description: "The id of the catalog containing this offering."
  type: str
  returned: on success for read operation
catalog_name:
  description: "The name of the catalog."
  type: str
  returned: on success for read operation
data:
  description: "Map of data values for this object."
  type: dict
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
    from ibm_platform_services import CatalogManagementV1
except ImportError as imp_exc:
    MISSING_IMPORT_EXC = imp_exc
else:
    MISSING_IMPORT_EXC = None


def run_module():
    module_args = dict(
        object_identifier=dict(
            type='str',
            required=False),
        catalog_identifier=dict(
            type='str',
            required=False),
    )

    module = AnsibleModule(
        argument_spec=module_args,
        supports_check_mode=True
    )

    if MISSING_IMPORT_EXC is not None:
        module.fail_json(msg='Missing required import: ' + MISSING_IMPORT_EXC.msg)

    object_identifier = module.params["object_identifier"]
    catalog_identifier = module.params["catalog_identifier"]

    if module.check_mode:
        module.exit_json(msg='The module would run with the following parameters: ' + module.paramss)

    authenticator = get_authenticator(service_name='catalog_management')
    if authenticator is None:
        module.fail_json(msg='Cannot create the authenticator.')

    sdk = CatalogManagementV1(
        authenticator=authenticator,
    )

    sdk.configure_service('catalog_management')

    if object_identifier:
        # read
        try:
            response = sdk.get_object(
                catalog_identifier=catalog_identifier,
                object_identifier=object_identifier,
            )

            result = response.get_result()

            module.exit_json(**result)
        except ApiException as ex:
            module.fail_json(msg=ex.message)


def main():
    run_module()


if __name__ == '__main__':
    main()
