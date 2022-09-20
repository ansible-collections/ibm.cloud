#!/usr/bin/python
# -*- coding: utf-8 -*-

# (C) Copyright IBM Corp. 2022.
# GNU General Public License v3.0+ (see LICENSE or https://www.gnu.org/licenses/gpl-3.0.txt)

from __future__ import (absolute_import, division, print_function)
__metaclass__ = type


DOCUMENTATION = r'''
---
module: ibm_cm_catalog
short_description: Manage ibm_cm_catalog resources.
author: Kavya Handadi (@kavya498)
version_added: "0.0.1-beta0"
description:
    - This module creates, updates, C(resource_alias) or deletes a ibm_cm_catalog.
    - By default the module will look for an existing ibm_cm_catalog.
requirements:
    - "CatalogManagementV1"
options:
    short_description:
        description:
            - Description in the requested language.
        type: str
    resource_group_id:
        description:
            - Resource group id the catalog is owned by.
        type: str
    owning_account:
        description:
            - Account that owns catalog.
        type: str
    kind:
        description:
            - Kind of catalog. Supported kinds are offering and vpe.
        type: str
    rev:
        description:
            - Cloudant revision.
        type: str
    catalog_icon_url:
        description:
            - URL for an icon associated with this catalog.
        type: str
    label:
        description:
            - Display Name in the requested language.
        type: str
    tags:
        description:
            - List of tags associated with this catalog.
        type: list
        elements: str
    features:
        description:
            - List of features associated with this catalog.
        type: list
        elements: dict
        suboptions:
            title:
                description:
                    - Heading.
                type: str
            description:
                description:
                    - Feature description.
                type: str
    disabled:
        description:
            - Denotes whether a catalog is disabled.
        type: bool
    id:
        description:
            - Unique ID.
        type: str
    catalog_filters:
        description:
            - Filters for account and catalog filters.
        type: dict
        suboptions:
            include_all:
                description: |
                    true - Include all of the public catalog when filtering.
                    Further settings will specifically exclude some offerings.
                    false - Exclude all of the public catalog when filtering.
                    Further settings will specifically include some offerings.
                type: bool
            category_filters:
                description:
                    - Filter against offering properties.
                type: dict
                suboptions:
                    include:
                        description:
                            - -> true - This is an include filter, false - this is an exclude filter.
                        type: bool
                    filter:
                        description:
                            - Offering filter terms.
                        type: dict
                        suboptions:
                            filter_terms:
                                description: |
                                    List of values to match against.
                                    If include is true, then if the offering has one of the values then the offering is included.
                                    If include is false, then if the offering has one of the values then the offering is excluded.
                                type: list
                                elements: str
            id_filters:
                description:
                    - Filter on offering ID's. There is an include filter and an exclule filter. Both can be set.
                type: dict
                suboptions:
                    include:
                        description:
                            - Offering filter terms.
                        type: dict
                        suboptions:
                            filter_terms:
                                description: |
                                    List of values to match against.
                                    If include is true, then if the offering has one of the values then the offering is included.
                                    If include is false, then if the offering has one of the values then the offering is excluded.
                                type: list
                                elements: str
                    exclude:
                        description:
                            - Offering filter terms.
                        type: dict
                        suboptions:
                            filter_terms:
                                description: |
                                    List of values to match against.
                                    If include is true, then if the offering has one of the values then the offering is included.
                                    If include is false, then if the offering has one of the values then the offering is excluded.
                                type: list
                                elements: str
    syndication_settings:
        description:
            - Feature information.
        type: dict
        suboptions:
            remove_related_components:
                description:
                    - Remove related components.
                type: bool
            clusters:
                description:
                    - Syndication clusters.
                type: list
                elements: dict
                suboptions:
                    region:
                        description:
                            - Cluster region.
                        type: str
                    id:
                        description:
                            - Cluster ID.
                        type: str
                    name:
                        description:
                            - Cluster name.
                        type: str
                    resource_group_name:
                        description:
                            - Resource group ID.
                        type: str
                    type:
                        description:
                            - Syndication type.
                        type: str
                    namespaces:
                        description:
                            - Syndicated namespaces.
                        type: list
                        elements: str
                    all_namespaces:
                        description:
                            - Syndicated to all namespaces on cluster.
                        type: bool
            history:
                description:
                    - Feature information.
                type: dict
                suboptions:
                    namespaces:
                        description:
                            - Array of syndicated namespaces.
                        type: list
                        elements: str
                    clusters:
                        description:
                            - Array of syndicated namespaces.
                        type: list
                        elements: dict
                        suboptions:
                            region:
                                description:
                                    - Cluster region.
                                type: str
                            id:
                                description:
                                    - Cluster ID.
                                type: str
                            name:
                                description:
                                    - Cluster name.
                                type: str
                            resource_group_name:
                                description:
                                    - Resource group ID.
                                type: str
                            type:
                                description:
                                    - Syndication type.
                                type: str
                            namespaces:
                                description:
                                    - Syndicated namespaces.
                                type: list
                                elements: str
                            all_namespaces:
                                description:
                                    - Syndicated to all namespaces on cluster.
                                type: bool
                    last_run:
                        description:
                            - Date and time last syndicated.
                        type: str
            authorization:
                description:
                    - Feature information.
                type: dict
                suboptions:
                    token:
                        description:
                            - Array of syndicated namespaces.
                        type: str
                    last_run:
                        description:
                            - Date and time last updated.
                        type: str
    catalog_identifier:
        description:
            - Catalog identifier.
        type: str
    state:
        description:
            - Should the resource be present or absent.
        type: str
        default: present
        choices: [present, absent]
'''

EXAMPLES = r'''
Examples coming soon.
'''

from ..module_utils import config
from ibm_platform_services import CatalogManagementV1
from ibm_cloud_sdk_core import ApiException
from ansible.module_utils.basic import AnsibleModule


def run_module():
    module_args = dict(
        short_description=dict(
            type='str',
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
        rev=dict(
            type='str',
            required=False),
        catalog_icon_url=dict(
            type='str',
            required=False),
        label=dict(
            type='str',
            required=False),
        tags=dict(
            type='list',
            elements=str,
            required=False),
        features=dict(
            type='list',
            elements='dict',
            options=dict(
                title=dict(
                    type='str',
                    required=False),
                description=dict(
                    type='str',
                    required=False),
            ),
            required=False),
        disabled=dict(
            type='bool',
            required=False),
        id=dict(
            type='str',
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
                                    elements=str,
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
                                    elements=str,
                                    required=False),
                            ),
                            required=False),
                        exclude=dict(
                            type='dict',
                            options=dict(
                                filter_terms=dict(
                                    type='list',
                                    elements=str,
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
                            elements=str,
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
                            elements=str,
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
                                    elements=str,
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
                            required=False),
                        last_run=dict(
                            type='str',
                            required=False),
                    ),
                    required=False),
            ),
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

    short_description = module.params["short_description"]
    resource_group_id = module.params["resource_group_id"]
    owning_account = module.params["owning_account"]
    kind = module.params["kind"]
    rev = module.params["rev"]
    catalog_icon_url = module.params["catalog_icon_url"]
    label = module.params["label"]
    tags = module.params["tags"]
    features = module.params["features"]
    disabled = module.params["disabled"]
    id = module.params["id"]
    catalog_filters = module.params["catalog_filters"]
    syndication_settings = module.params["syndication_settings"]
    catalog_identifier = module.params["catalog_identifier"]
    state = module.params["state"]

    sdk = config.get_catalog_management_sdk()
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
                payload = {"id": catalog_identifier, "status": "deleted"}
                module.exit_json(changed=True, msg=payload)
        else:
            payload = {"id": catalog_identifier, "status": "not_found"}
            module.exit_json(changed=False, msg=payload)

    if state == "present":
        if not resource_exists:
            # Create path
            try:
                result = sdk.create_catalog(
                    id=id,
                    rev=rev,
                    label=label,
                    short_description=short_description,
                    catalog_icon_url=catalog_icon_url,
                    tags=tags,
                    features=features,
                    disabled=disabled,
                    resource_group_id=resource_group_id,
                    owning_account=owning_account,
                    catalog_filters=catalog_filters,
                    syndication_settings=syndication_settings,
                    kind=kind,
                ).get_result()
            except ApiException as ex:
                module.fail_json(msg=ex.message)
            else:
                module.exit_json(changed=True, msg=result)
        else:
            # Update path
            try:
                result = sdk.replace_catalog(
                    catalog_identifier=catalog_identifier,
                    id=id,
                    rev=rev,
                    label=label,
                    short_description=short_description,
                    catalog_icon_url=catalog_icon_url,
                    tags=tags,
                    features=features,
                    disabled=disabled,
                    resource_group_id=resource_group_id,
                    owning_account=owning_account,
                    catalog_filters=catalog_filters,
                    syndication_settings=syndication_settings,
                    kind=kind,
                ).get_result()
            except ApiException as ex:
                module.fail_json(msg=ex.message)
            else:
                module.exit_json(changed=True, msg=result)


def main():
    run_module()


if __name__ == '__main__':
    main()
