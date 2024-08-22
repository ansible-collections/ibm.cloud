#!/usr/bin/python
# coding: utf-8

# (C) Copyright IBM Corp. 2024.
#
# GNU General Public License v3.0+ (see LICENSE or https://www.gnu.org/licenses/gpl-3.0.txt)

from __future__ import (absolute_import, division, print_function)
__metaclass__ = type


DOCUMENTATION = r'''
---
module: ibm_cm_catalog_info
short_description: Manage C(cm_catalog) for Catalog Management API.
author: IBM SDK Generator (@ibm)
version_added: "1.0.0"
description:
  - This module retrieves one or more C(cm_catalog) for Catalog Management API.
requirements:
  - "CatalogManagementV1"
options:
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
- name: Read ibm_cm_catalog
  ibm_cm_catalog_info:
    catalog_identifier: 'testString'
'''

RETURN = r'''
id:
  description: "Unique ID."
  type: str
  returned: on success for read operation
rev:
  description: "Cloudant revision."
  type: str
  returned: on success for read operation
label:
  description: "Display Name in the requested language."
  type: str
  returned: on success for read operation
label_i18n:
  description: "A map of translated strings, by language code."
  type: dict
  returned: on success for read operation
short_description:
  description: "Description in the requested language."
  type: str
  returned: on success for read operation
short_description_i18n:
  description: "A map of translated strings, by language code."
  type: dict
  returned: on success for read operation
catalog_icon_url:
  description: "URL for an icon associated with this catalog."
  type: str
  returned: on success for read operation
catalog_banner_url:
  description: "URL for a banner image for this catalog."
  type: str
  returned: on success for read operation
tags:
  description: "List of tags associated with this catalog."
  type: list
  elements: str
  returned: on success for read operation
url:
  description: "The url for this specific catalog."
  type: str
  returned: on success for read operation
crn:
  description: "CRN associated with the catalog."
  type: str
  returned: on success for read operation
offerings_url:
  description: "URL path to offerings."
  type: str
  returned: on success for read operation
features:
  description: "List of features associated with this catalog."
  type: list
  elements: 'dict'
  contains:
    title:
      description: "Heading."
      type: str
    title_i18n:
      description: "A map of translated strings, by language code."
      type: dict
    description:
      description: "Feature description."
      type: str
    description_i18n:
      description: "A map of translated strings, by language code."
      type: dict
  returned: on success for read operation
disabled:
  description: "Denotes whether a catalog is disabled."
  type: bool
  returned: on success for read operation
created:
  description: "The date-time this catalog was created."
  type: str
  returned: on success for read operation
updated:
  description: "The date-time this catalog was last updated."
  type: str
  returned: on success for read operation
resource_group_id:
  description: "Resource group id the catalog is owned by."
  type: str
  returned: on success for read operation
owning_account:
  description: "Account that owns catalog."
  type: str
  returned: on success for read operation
catalog_filters:
  description: "Filters for account and catalog filters."
  type: dict
  contains:
    include_all:
      description: "-> true - Include all of the public catalog when filtering. Further settings will
        specifically exclude some offerings. false - Exclude all of the public catalog when
        filtering. Further settings will specifically include some offerings."
      type: bool
    category_filters:
      description: "Filter against offering properties."
      type: dict
      contains:
        include:
          description: "-> true - This is an include filter, false - this is an exclude filter."
          type: bool
        filter:
          description: "Offering filter terms."
          type: dict
          contains:
            filter_terms:
              description: "List of values to match against. If include is true, then if the offering has one of
                the values then the offering is included. If include is false, then if the offering
                has one of the values then the offering is excluded."
              type: list
              elements: str
    id_filters:
      description: "Filter on offering ID's. There is an include filter and an exclule filter. Both can be
        set."
      type: dict
      contains:
        include:
          description: "Offering filter terms."
          type: dict
          contains:
            filter_terms:
              description: "List of values to match against. If include is true, then if the offering has one of
                the values then the offering is included. If include is false, then if the offering
                has one of the values then the offering is excluded."
              type: list
              elements: str
        exclude:
          description: "Offering filter terms."
          type: dict
          contains:
            filter_terms:
              description: "List of values to match against. If include is true, then if the offering has one of
                the values then the offering is included. If include is false, then if the offering
                has one of the values then the offering is excluded."
              type: list
              elements: str
  returned: on success for read operation
kind:
  description: "Kind of catalog. Supported kinds are offering and vpe."
  type: str
  returned: on success for read operation
metadata:
  description: "Catalog specific metadata."
  type: dict
  returned: on success for read operation
target_account_contexts:
  description: "List of target accounts contexts on this catalog."
  type: list
  elements: 'dict'
  contains:
    api_key:
      description: "API Key."
      type: str
    trusted_profile:
      description: "Trusted profile info."
      type: dict
      contains:
        trusted_profile_id:
          description: "Trusted profile ID."
          type: str
        catalog_crn:
          description: "Catalog CRN."
          type: str
        catalog_name:
          description: "Catalog name."
          type: str
        target_service_id:
          description: "Target service ID."
          type: str
    name:
      description: "Unique identifier/name."
      type: str
    label:
      description: "Display name."
      type: str
    project_id:
      description: "Project ID."
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
    from ibm_platform_services import CatalogManagementV1
except ImportError as imp_exc:
    MISSING_IMPORT_EXC = imp_exc
else:
    MISSING_IMPORT_EXC = None


def run_module():
    module_args = dict(
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

    if catalog_identifier:
        # read
        try:
            response = sdk.get_catalog(
                catalog_identifier=catalog_identifier,
            )

            result = response.get_result()

            module.exit_json(**result)
        except ApiException as ex:
            module.fail_json(msg=ex.message)


def main():
    run_module()


if __name__ == '__main__':
    main()
