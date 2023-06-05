#!/usr/bin/python
# coding: utf-8

# (C) Copyright IBM Corp. 2023.
#
# GNU General Public License v3.0+ (see LICENSE or https://www.gnu.org/licenses/gpl-3.0.txt)

from __future__ import (absolute_import, division, print_function)
__metaclass__ = type


DOCUMENTATION = r'''
---
module: ibm_cm_catalog
short_description: Manage C(cm_catalogs) for Catalog Management API.
author: IBM SDK Generator (@ibm)
version_added: "1.0.0"
description:
  - This module creates, updates, or deletes a C(cm_catalog) resource for Catalog Management API.
requirements:
  - "CatalogManagementV1"
options:
  label_i18n:
    description: "A map of translated strings, by language code."
    type: dict
  short_description:
    description: "Description in the requested language."
    type: str
  catalog_banner_url:
    description: "URL for a banner image for this catalog."
    type: str
  metadata:
    description: "Catalog specific metadata."
    type: dict
  resource_group_id:
    description: "Resource group id the catalog is owned by."
    type: str
  owning_account:
    description: "Account that owns catalog."
    type: str
  kind:
    description: "Kind of catalog. Supported kinds are offering and vpe."
    type: str
  catalog_icon_url:
    description: "URL for an icon associated with this catalog."
    type: str
  rev:
    description: "Cloudant revision."
    type: str
  label:
    description: "Display Name in the requested language."
    type: str
  tags:
    description: "List of tags associated with this catalog."
    type: list
    elements: str
  features:
    description: "List of features associated with this catalog."
    type: list
    elements: 'dict'
    suboptions:
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
  disabled:
    description: "Denotes whether a catalog is disabled."
    type: bool
  catalog_filters:
    description: "Filters for account and catalog filters."
    type: dict
    suboptions:
      include_all:
        description: "-> true - Include all of the public catalog when filtering. Further settings will
          specifically exclude some offerings. false - Exclude all of the public catalog when
          filtering. Further settings will specifically include some offerings."
        type: bool
      category_filters:
        description: "Filter against offering properties."
        type: dict
        suboptions:
          include:
            description: "-> true - This is an include filter, false - this is an exclude filter."
            type: bool
          filter:
            description: "Offering filter terms."
            type: dict
            suboptions:
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
        suboptions:
          include:
            description: "Offering filter terms."
            type: dict
            suboptions:
              filter_terms:
                description: "List of values to match against. If include is true, then if the offering has one of
                  the values then the offering is included. If include is false, then if the offering
                  has one of the values then the offering is excluded."
                type: list
                elements: str
          exclude:
            description: "Offering filter terms."
            type: dict
            suboptions:
              filter_terms:
                description: "List of values to match against. If include is true, then if the offering has one of
                  the values then the offering is included. If include is false, then if the offering
                  has one of the values then the offering is excluded."
                type: list
                elements: str
  syndication_settings:
    description: "Feature information."
    type: dict
    suboptions:
      remove_related_components:
        description: "Remove related components."
        type: bool
      clusters:
        description: "Syndication clusters."
        type: list
        elements: 'dict'
        suboptions:
          region:
            description: "Cluster region."
            type: str
          id:
            description: "Cluster ID."
            type: str
          name:
            description: "Cluster name."
            type: str
          resource_group_name:
            description: "Resource group ID."
            type: str
          type:
            description: "Syndication type."
            type: str
          namespaces:
            description: "Syndicated namespaces."
            type: list
            elements: str
          all_namespaces:
            description: "Syndicated to all namespaces on cluster."
            type: bool
      history:
        description: "Feature information."
        type: dict
        suboptions:
          namespaces:
            description: "Array of syndicated namespaces."
            type: list
            elements: str
          clusters:
            description: "Array of syndicated namespaces."
            type: list
            elements: 'dict'
            suboptions:
              region:
                description: "Cluster region."
                type: str
              id:
                description: "Cluster ID."
                type: str
              name:
                description: "Cluster name."
                type: str
              resource_group_name:
                description: "Resource group ID."
                type: str
              type:
                description: "Syndication type."
                type: str
              namespaces:
                description: "Syndicated namespaces."
                type: list
                elements: str
              all_namespaces:
                description: "Syndicated to all namespaces on cluster."
                type: bool
          last_run:
            description: "Date and time last syndicated."
            type: str
      authorization:
        description: "Feature information."
        type: dict
        suboptions:
          token:
            description: "Array of syndicated namespaces."
            type: str
          last_run:
            description: "Date and time last updated."
            type: str
  id:
    description: "Unique ID."
    type: str
  short_description_i18n:
    description: "A map of translated strings, by language code."
    type: dict
  catalog_identifier:
    description: "Catalog identifier."
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
- name: Create ibm_cm_catalog
  vars:
    feature_model:
      title: 'testString'
      title_i18n: {'key1': 'testString'}
      description: 'testString'
      description_i18n: {'key1': 'testString'}
    filter_terms_model:
      filter_terms: ['testString']
    category_filter_model:
      include: True
      filter: filter_terms_model
    id_filter_model:
      include: filter_terms_model
      exclude: filter_terms_model
    filters_model:
      include_all: True
      category_filters: category_filter_model
      id_filters: id_filter_model
    syndication_cluster_model:
      region: 'testString'
      id: 'testString'
      name: 'testString'
      resource_group_name: 'testString'
      type: 'testString'
      namespaces: ['testString']
      all_namespaces: True
    syndication_history_model:
      namespaces: ['testString']
      clusters: [syndication_cluster_model]
      last_run: '2019-01-01T12:00:00.000Z'
    syndication_authorization_model:
      token: 'testString'
      last_run: '2019-01-01T12:00:00.000Z'
    syndication_resource_model:
      remove_related_components: True
      clusters: [syndication_cluster_model]
      history: syndication_history_model
      authorization: syndication_authorization_model
  ibm_cm_catalog:
    label: 'testString'
    label_i18n: {'key1': 'testString'}
    short_description: 'testString'
    short_description_i18n: {'key1': 'testString'}
    catalog_icon_url: 'testString'
    catalog_banner_url: 'testString'
    tags: ['testString']
    features: [feature_model]
    disabled: True
    resource_group_id: 'testString'
    owning_account: 'testString'
    catalog_filters: '{{ filters_model }}'
    syndication_settings: '{{ syndication_resource_model }}'
    kind: 'testString'
    metadata: {'key1': {'foo': 'bar'}}
    state: present

- name: Update ibm_cm_catalog
  vars:
    feature_model:
      title: 'testString'
      title_i18n: {'key1': 'testString'}
      description: 'testString'
      description_i18n: {'key1': 'testString'}
    filter_terms_model:
      filter_terms: ['testString']
    category_filter_model:
      include: True
      filter: filter_terms_model
    id_filter_model:
      include: filter_terms_model
      exclude: filter_terms_model
    filters_model:
      include_all: True
      category_filters: category_filter_model
      id_filters: id_filter_model
    syndication_cluster_model:
      region: 'testString'
      id: 'testString'
      name: 'testString'
      resource_group_name: 'testString'
      type: 'testString'
      namespaces: ['testString']
      all_namespaces: True
    syndication_history_model:
      namespaces: ['testString']
      clusters: [syndication_cluster_model]
      last_run: '2019-01-01T12:00:00.000Z'
    syndication_authorization_model:
      token: 'testString'
      last_run: '2019-01-01T12:00:00.000Z'
    syndication_resource_model:
      remove_related_components: True
      clusters: [syndication_cluster_model]
      history: syndication_history_model
      authorization: syndication_authorization_model
  ibm_cm_catalog:
    catalog_identifier: 'testString'
    id: 'testString'
    rev: 'testString'
    label: 'testString'
    label_i18n: {'key1': 'testString'}
    short_description: 'testString'
    short_description_i18n: {'key1': 'testString'}
    catalog_icon_url: 'testString'
    catalog_banner_url: 'testString'
    tags: ['testString']
    features: [feature_model]
    disabled: True
    resource_group_id: 'testString'
    owning_account: 'testString'
    catalog_filters: '{{ filters_model }}'
    syndication_settings: '{{ syndication_resource_model }}'
    kind: 'testString'
    metadata: {'key1': {'foo': 'bar'}}
    state: present

- name: Delete ibm_cm_catalog
  ibm_cm_catalog:
    catalog_identifier: 'testString'
    state: absent
'''

RETURN = r'''
id:
  description: "Unique ID."
  type: str
  returned: on success for create, update, delete operations
rev:
  description: "Cloudant revision."
  type: str
  returned: on success for create, update operations
label:
  description: "Display Name in the requested language."
  type: str
  returned: on success for create, update operations
label_i18n:
  description: "A map of translated strings, by language code."
  type: dict
  returned: on success for create, update operations
short_description:
  description: "Description in the requested language."
  type: str
  returned: on success for create, update operations
short_description_i18n:
  description: "A map of translated strings, by language code."
  type: dict
  returned: on success for create, update operations
catalog_icon_url:
  description: "URL for an icon associated with this catalog."
  type: str
  returned: on success for create, update operations
catalog_banner_url:
  description: "URL for a banner image for this catalog."
  type: str
  returned: on success for create, update operations
tags:
  description: "List of tags associated with this catalog."
  type: list
  elements: str
  returned: on success for create, update operations
url:
  description: "The url for this specific catalog."
  type: str
  returned: on success for create, update operations
crn:
  description: "CRN associated with the catalog."
  type: str
  returned: on success for create, update operations
offerings_url:
  description: "URL path to offerings."
  type: str
  returned: on success for create, update operations
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
  returned: on success for create, update operations
disabled:
  description: "Denotes whether a catalog is disabled."
  type: bool
  returned: on success for create, update operations
created:
  description: "The date-time this catalog was created."
  type: str
  returned: on success for create, update operations
updated:
  description: "The date-time this catalog was last updated."
  type: str
  returned: on success for create, update operations
resource_group_id:
  description: "Resource group id the catalog is owned by."
  type: str
  returned: on success for create, update operations
owning_account:
  description: "Account that owns catalog."
  type: str
  returned: on success for create, update operations
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
  returned: on success for create, update operations
syndication_settings:
  description: "Feature information."
  type: dict
  contains:
    remove_related_components:
      description: "Remove related components."
      type: bool
    clusters:
      description: "Syndication clusters."
      type: list
      elements: 'dict'
      contains:
        region:
          description: "Cluster region."
          type: str
        id:
          description: "Cluster ID."
          type: str
        name:
          description: "Cluster name."
          type: str
        resource_group_name:
          description: "Resource group ID."
          type: str
        type:
          description: "Syndication type."
          type: str
        namespaces:
          description: "Syndicated namespaces."
          type: list
          elements: str
        all_namespaces:
          description: "Syndicated to all namespaces on cluster."
          type: bool
    history:
      description: "Feature information."
      type: dict
      contains:
        namespaces:
          description: "Array of syndicated namespaces."
          type: list
          elements: str
        clusters:
          description: "Array of syndicated namespaces."
          type: list
          elements: 'dict'
          contains:
            region:
              description: "Cluster region."
              type: str
            id:
              description: "Cluster ID."
              type: str
            name:
              description: "Cluster name."
              type: str
            resource_group_name:
              description: "Resource group ID."
              type: str
            type:
              description: "Syndication type."
              type: str
            namespaces:
              description: "Syndicated namespaces."
              type: list
              elements: str
            all_namespaces:
              description: "Syndicated to all namespaces on cluster."
              type: bool
        last_run:
          description: "Date and time last syndicated."
          type: str
    authorization:
      description: "Feature information."
      type: dict
      contains:
        token:
          description: "Array of syndicated namespaces."
          type: str
        last_run:
          description: "Date and time last updated."
          type: str
  returned: on success for create, update operations
kind:
  description: "Kind of catalog. Supported kinds are offering and vpe."
  type: str
  returned: on success for create, update operations
metadata:
  description: "Catalog specific metadata."
  type: dict
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
    from ibm_platform_services import CatalogManagementV1
except ImportError as imp_exc:
    MISSING_IMPORT_EXC = imp_exc
else:
    MISSING_IMPORT_EXC = None


def run_module():
    module_args = dict(
        label_i18n=dict(
            type='dict',
            required=False),
        short_description=dict(
            type='str',
            required=False),
        catalog_banner_url=dict(
            type='str',
            required=False),
        metadata=dict(
            type='dict',
            required=False),
        resource_group_id=dict(
            type='str',
            required=False),
        owning_account=dict(
            type='str',
            required=False),
        kind=dict(
            type='str',
            required=False),
        catalog_icon_url=dict(
            type='str',
            required=False),
        rev=dict(
            type='str',
            required=False),
        label=dict(
            type='str',
            required=False),
        tags=dict(
            type='list',
            elements='str',
            required=False),
        features=dict(
            type='list',
            elements='dict',
            options=dict(
                title=dict(
                    type='str',
                    required=False),
                title_i18n=dict(
                    type='dict',
                    required=False),
                description=dict(
                    type='str',
                    required=False),
                description_i18n=dict(
                    type='dict',
                    required=False),
            ),
            required=False),
        disabled=dict(
            type='bool',
            required=False),
        # Represents the Filters Python class
        catalog_filters=dict(
            type='dict',
            options=dict(
                include_all=dict(
                    type='bool',
                    required=False),
                category_filters=dict(
                    type='dict',
                    options=dict(
                        include=dict(
                            type='bool',
                            required=False),
                        filter=dict(
                            type='dict',
                            options=dict(
                                filter_terms=dict(
                                    type='list',
                                    elements='str',
                                    required=False),
                            ),
                            required=False),
                    ),
                    required=False),
                id_filters=dict(
                    type='dict',
                    options=dict(
                        include=dict(
                            type='dict',
                            options=dict(
                                filter_terms=dict(
                                    type='list',
                                    elements='str',
                                    required=False),
                            ),
                            required=False),
                        exclude=dict(
                            type='dict',
                            options=dict(
                                filter_terms=dict(
                                    type='list',
                                    elements='str',
                                    required=False),
                            ),
                            required=False),
                    ),
                    required=False),
            ),
            required=False),
        # Represents the SyndicationResource Python class
        syndication_settings=dict(
            type='dict',
            options=dict(
                remove_related_components=dict(
                    type='bool',
                    required=False),
                clusters=dict(
                    type='list',
                    elements='dict',
                    options=dict(
                        region=dict(
                            type='str',
                            required=False),
                        id=dict(
                            type='str',
                            required=False),
                        name=dict(
                            type='str',
                            required=False),
                        resource_group_name=dict(
                            type='str',
                            required=False),
                        type=dict(
                            type='str',
                            required=False),
                        namespaces=dict(
                            type='list',
                            elements='str',
                            required=False),
                        all_namespaces=dict(
                            type='bool',
                            required=False),
                    ),
                    required=False),
                history=dict(
                    type='dict',
                    options=dict(
                        namespaces=dict(
                            type='list',
                            elements='str',
                            required=False),
                        clusters=dict(
                            type='list',
                            elements='dict',
                            options=dict(
                                region=dict(
                                    type='str',
                                    required=False),
                                id=dict(
                                    type='str',
                                    required=False),
                                name=dict(
                                    type='str',
                                    required=False),
                                resource_group_name=dict(
                                    type='str',
                                    required=False),
                                type=dict(
                                    type='str',
                                    required=False),
                                namespaces=dict(
                                    type='list',
                                    elements='str',
                                    required=False),
                                all_namespaces=dict(
                                    type='bool',
                                    required=False),
                            ),
                            required=False),
                        last_run=dict(
                            type='str',
                            required=False),
                    ),
                    required=False),
                authorization=dict(
                    type='dict',
                    options=dict(
                        token=dict(
                            type='str',
                            no_log=True,
                            required=False),
                        last_run=dict(
                            type='str',
                            required=False),
                    ),
                    required=False),
            ),
            required=False),
        id=dict(
            type='str',
            required=False),
        short_description_i18n=dict(
            type='dict',
            required=False),
        catalog_identifier=dict(
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

    label_i18n = module.params["label_i18n"]
    short_description = module.params["short_description"]
    catalog_banner_url = module.params["catalog_banner_url"]
    metadata = module.params["metadata"]
    resource_group_id = module.params["resource_group_id"]
    owning_account = module.params["owning_account"]
    kind = module.params["kind"]
    catalog_icon_url = module.params["catalog_icon_url"]
    rev = module.params["rev"]
    label = module.params["label"]
    tags = module.params["tags"]
    features = module.params["features"]
    disabled = module.params["disabled"]
    catalog_filters = module.params["catalog_filters"]
    syndication_settings = module.params["syndication_settings"]
    id = module.params["id"]
    short_description_i18n = module.params["short_description_i18n"]
    catalog_identifier = module.params["catalog_identifier"]
    state = module.params["state"]

    authenticator = get_authenticator(service_name='catalog_management')
    if authenticator is None:
        module.fail_json(msg='Cannot create the authenticator.')

    sdk = CatalogManagementV1(
        authenticator=authenticator,
    )

    sdk.configure_service('catalog_management')

    resource_exists = True

    # Check for existence
    if catalog_identifier:
        try:
            sdk.get_catalog(
                catalog_identifier=catalog_identifier,
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
                sdk.delete_catalog(
                    catalog_identifier=catalog_identifier,
                )
            except ApiException as ex:
                module.fail_json(msg=ex.message)
            else:
                module.exit_json(changed=True, id=catalog_identifier, status="deleted")
        else:
            module.exit_json(changed=False, id=catalog_identifier, status="not_found")

    if state == "present":
        if not resource_exists:
            # Create path
            try:
                response = sdk.create_catalog(
                    label=label,
                    label_i18n=label_i18n,
                    short_description=short_description,
                    short_description_i18n=short_description_i18n,
                    catalog_icon_url=catalog_icon_url,
                    catalog_banner_url=catalog_banner_url,
                    tags=tags,
                    features=features,
                    disabled=disabled,
                    resource_group_id=resource_group_id,
                    owning_account=owning_account,
                    catalog_filters=catalog_filters,
                    syndication_settings=syndication_settings,
                    kind=kind,
                    metadata=metadata,
                )
            except ApiException as ex:
                module.fail_json(msg=ex.message)
            else:
                result = response.get_result()

                module.exit_json(changed=True, **result)
        else:
            # Update path
            try:
                response = sdk.replace_catalog(
                    catalog_identifier=catalog_identifier,
                    id=id,
                    rev=rev,
                    label=label,
                    label_i18n=label_i18n,
                    short_description=short_description,
                    short_description_i18n=short_description_i18n,
                    catalog_icon_url=catalog_icon_url,
                    catalog_banner_url=catalog_banner_url,
                    tags=tags,
                    features=features,
                    disabled=disabled,
                    resource_group_id=resource_group_id,
                    owning_account=owning_account,
                    catalog_filters=catalog_filters,
                    syndication_settings=syndication_settings,
                    kind=kind,
                    metadata=metadata,
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
