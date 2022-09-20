#!/usr/bin/python
# -*- coding: utf-8 -*-

# (C) Copyright IBM Corp. 2022.
# GNU General Public License v3.0+ (see LICENSE or https://www.gnu.org/licenses/gpl-3.0.txt)

from __future__ import (absolute_import, division, print_function)
__metaclass__ = type


DOCUMENTATION = r'''
---
module: ibm_cm_offering
short_description: Manage ibm_cm_offering resources.
author: Kavya Handadi (@kavya498)
version_added: "0.0.1-beta0"
description:
    - This module creates, updates, or deletes a ibm_cm_offering.
    - By default the module will look for an existing ibm_cm_offering.
requirements:
    - "CatalogManagementV1"
options:
    short_description:
        description:
            - Short description in the requested language.
        type: str
    offering_support_url:
        description: |
            [deprecated] Use offering.support instead.
            URL to be displayed in the Consumption UI for getting support on this offering.
        type: str
    metadata:
        description:
            - Map of metadata values for this offering.
        type: dict
    keywords:
        description:
            - List of keywords associated with offering, typically used to search for it.
        type: list
        elements: str
    hidden:
        description:
            - Determine if this offering should be displayed in the Consumption UI.
        type: bool
    public_publish_approved:
        description:
            - Indicates if this offering has been approved for use by all IBM Cloud users.
        type: bool
    portal_ui_url:
        description:
            - The portal UI URL.
        type: str
    rev:
        description:
            - Cloudant revision.
        type: str
    rating:
        description:
            - Repository info for offerings.
        type: dict
        suboptions:
            one_star_count:
                description:
                    - One start rating.
                type: int
            two_star_count:
                description:
                    - Two start rating.
                type: int
            three_star_count:
                description:
                    - Three start rating.
                type: int
            four_star_count:
                description:
                    - Four start rating.
                type: int
    kinds:
        description:
            - Array of kind.
        type: list
        elements: dict
        suboptions:
            id:
                description:
                    - Unique ID.
                type: str
            format_kind:
                description:
                    - content kind, e.g., helm, vm image.
                type: str
            target_kind:
                description:
                    - target cloud to install, e.g., iks, open_shift_iks.
                type: str
            metadata:
                description:
                    - Open ended metadata information.
                type: dict
            install_description:
                description:
                    - Installation instruction.
                type: str
            tags:
                description:
                    - List of tags associated with this catalog.
                type: list
                elements: str
            additional_features:
                description:
                    - List of features associated with this offering.
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
            created:
                description:
                    - The date and time this catalog was created.
                type: str
            updated:
                description:
                    - The date and time this catalog was last updated.
                type: str
            versions:
                description:
                    - list of versions.
                type: list
                elements: dict
                suboptions:
                    id:
                        description:
                            - Unique ID.
                        type: str
                    rev:
                        description:
                            - Cloudant revision.
                        type: str
                    crn:
                        description:
                            - Version's CRN.
                        type: str
                    version:
                        description:
                            - Version of content type.
                        type: str
                    sha:
                        description:
                            - hash of the content.
                        type: str
                    created:
                        description:
                            - The date and time this version was created.
                        type: str
                    updated:
                        description:
                            - The date and time this version was last updated.
                        type: str
                    offering_id:
                        description:
                            - Offering ID.
                        type: str
                    catalog_id:
                        description:
                            - Catalog ID.
                        type: str
                    kind_id:
                        description:
                            - Kind ID.
                        type: str
                    tags:
                        description:
                            - List of tags associated with this catalog.
                        type: list
                        elements: str
                    repo_url:
                        description:
                            - Content's repo URL.
                        type: str
                    source_url:
                        description:
                            - Content's source URL (e.g git repo).
                        type: str
                    tgz_url:
                        description:
                            - File used to onboard this version.
                        type: str
                    configuration:
                        description:
                            - List of user solicited overrides.
                        type: list
                        elements: dict
                        suboptions:
                            key:
                                description:
                                    - Configuration key.
                                type: str
                            type:
                                description:
                                    - Value type (string, boolean, int).
                                type: str
                            default_value:
                                description: |
                                    The default value.
                                    To use a secret when the type is password,
                                    specify a JSON encoded value of $ref:#/components/schemas/SecretInstance, prefixed with `cmsm_v1:`.
                                type: raw
                            value_constraint:
                                description:
                                    - Constraint associated with value, e.g., for string type regx [a-z].
                                type: str
                            description:
                                description:
                                    - Key description.
                                type: str
                            required:
                                description:
                                    - Is key required to install.
                                type: bool
                            options:
                                description:
                                    - List of options of type.
                                type: list
                                elements: raw
                            hidden:
                                description:
                                    - Hide values.
                                type: bool
                    metadata:
                        description:
                            - Open ended metadata information.
                        type: dict
                    validation:
                        description:
                            - Validation response.
                        type: dict
                        suboptions:
                            validated:
                                description:
                                    - Date and time of last successful validation.
                                type: str
                            requested:
                                description:
                                    - Date and time of last validation was requested.
                                type: str
                            state_:
                                description: |
                                    Current validation state in_progress, valid, invalid, expired.
                                type: str
                            last_operation:
                                description:
                                    - Last operation (e.g. submit_deployment, generate_installer, install_offering.
                                type: str
                            target:
                                description:
                                    - Validation target information (e.g. cluster_id, region, namespace, etc).  Values will vary by Content type.
                                type: dict
                    required_resources:
                        description:
                            - Resource requirments for installation.
                        type: list
                        elements: dict
                        suboptions:
                            type:
                                description:
                                    - Type of requirement.
                                type: str
                            value:
                                description:
                                    - mem, disk, cores, and nodes can be parsed as an int.  targetVersion will be a semver range value.
                                type: raw
                    single_instance:
                        description:
                            - Denotes if single instance can be deployed to a given cluster.
                        type: bool
                    install:
                        description:
                            - Script information.
                        type: dict
                        suboptions:
                            instructions:
                                description:
                                    - Instruction on step and by whom (role) that are needed to take place to prepare the target for installing this version.
                                type: str
                            script:
                                description:
                                    - Optional script that needs to be run post any pre-condition script.
                                type: str
                            script_permission:
                                description:
                                    - Optional iam permissions that are required on the target cluster to run this script.
                                type: str
                            delete_script:
                                description:
                                    - Optional script that if run will remove the installed version.
                                type: str
                            scope:
                                description:
                                    - Optional value indicating if this script is scoped to a namespace or the entire cluster.
                                type: str
                    pre_install:
                        description:
                            - Optional pre install instructions.
                        type: list
                        elements: dict
                        suboptions:
                            instructions:
                                description:
                                    - Instruction on step and by whom (role) that are needed to take place to prepare the target for installing this version.
                                type: str
                            script:
                                description:
                                    - Optional script that needs to be run post any pre condition script.
                                type: str
                            script_permission:
                                description:
                                    - Optional iam permissions that are required on the target cluster to run this script.
                                type: str
                            delete_script:
                                description:
                                    - Optional script that if run will remove the installed version.
                                type: str
                            scope:
                                description:
                                    - Optional value indicating if this script is scoped to a namespace or the entire cluster.
                                type: str
                    entitlement:
                        description:
                            - Entitlement license info.
                        type: dict
                        suboptions:
                            provider_name:
                                description:
                                    - Provider name.
                                type: str
                            provider_id:
                                description:
                                    - Provider ID.
                                type: str
                            product_id:
                                description:
                                    - Product ID.
                                type: str
                            part_numbers:
                                description:
                                    - list of license entitlement part numbers, eg. D1YGZLL,D1ZXILL.
                                type: list
                                elements: str
                            image_repo_name:
                                description:
                                    - Image repository name.
                                type: str
                    licenses:
                        description:
                            - List of licenses the product was built with.
                        type: list
                        elements: dict
                        suboptions:
                            id:
                                description:
                                    - License ID.
                                type: str
                            name:
                                description:
                                    - license name.
                                type: str
                            type:
                                description:
                                    - type of license e.g., Apache xxx.
                                type: str
                            url:
                                description:
                                    - URL for the license text.
                                type: str
                            description:
                                description:
                                    - License description.
                                type: str
                    image_manifest_url:
                        description:
                            - If set, denotes a url to a YAML file with list of container images used by this version.
                        type: str
                    deprecated:
                        description:
                            - read only field, indicating if this version is deprecated.
                        type: bool
                    package_version:
                        description:
                            - Version of the package used to create this version.
                        type: str
                    state_:
                        description:
                            - Offering state.
                        type: dict
                        suboptions:
                            current:
                                description:
                                    - one of new, validated, 'account-published', 'ibm-published', 'public-published'.
                                type: str
                            current_entered:
                                description:
                                    - Date and time of current request.
                                type: str
                            pending:
                                description:
                                    - one of new, validated, 'account-published', 'ibm-published', 'public-published'.
                                type: str
                            pending_requested:
                                description:
                                    - Date and time of pending request.
                                type: str
                            previous:
                                description:
                                    - one of new, validated, 'account-published', 'ibm-published', 'public-published'.
                                type: str
                    version_locator:
                        description:
                            - A dotted value of `catalogID`.`versionID`.
                        type: str
                    console_url:
                        description:
                            - Console URL.
                        type: str
                    long_description:
                        description:
                            - Long description for version.
                        type: str
                    whitelisted_accounts:
                        description:
                            - Whitelisted accounts for version.
                        type: list
                        elements: str
            plans:
                description:
                    - list of plans.
                type: list
                elements: dict
                suboptions:
                    id:
                        description:
                            - unique id.
                        type: str
                    label:
                        description:
                            - Display Name in the requested language.
                        type: str
                    name:
                        description:
                            - The programmatic name of this offering.
                        type: str
                    short_description:
                        description:
                            - Short description in the requested language.
                        type: str
                    long_description:
                        description:
                            - Long description in the requested language.
                        type: str
                    metadata:
                        description:
                            - open ended metadata information.
                        type: dict
                    tags:
                        description:
                            - list of tags associated with this catalog.
                        type: list
                        elements: str
                    additional_features:
                        description:
                            - list of features associated with this offering.
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
                    created:
                        description:
                            - the date'time this catalog was created.
                        type: str
                    updated:
                        description:
                            - the date'time this catalog was last updated.
                        type: str
                    deployments:
                        description:
                            - list of deployments.
                        type: list
                        elements: dict
                        suboptions:
                            id:
                                description:
                                    - unique id.
                                type: str
                            label:
                                description:
                                    - Display Name in the requested language.
                                type: str
                            name:
                                description:
                                    - The programmatic name of this offering.
                                type: str
                            short_description:
                                description:
                                    - Short description in the requested language.
                                type: str
                            long_description:
                                description:
                                    - Long description in the requested language.
                                type: str
                            metadata:
                                description:
                                    - open ended metadata information.
                                type: dict
                            tags:
                                description:
                                    - list of tags associated with this catalog.
                                type: list
                                elements: str
                            created:
                                description:
                                    - the date'time this catalog was created.
                                type: str
                            updated:
                                description:
                                    - the date'time this catalog was last updated.
                                type: str
    media:
        description:
            - A list of media items related to this offering.
        type: list
        elements: dict
        suboptions:
            url:
                description:
                    - URL of the specified media item.
                type: str
            caption:
                description:
                    - Caption for this media item.
                type: str
            type:
                description:
                    - Type of this media item.
                type: str
            thumbnail_url:
                description:
                    - Thumbnail URL for this media item.
                type: str
    share_with_ibm:
        description:
            - Denotes IBM employee availability of an Offering.
        type: bool
    features:
        description:
            - list of features associated with this offering.
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
    ibm_publish_approved:
        description:
            - Indicates if this offering has been approved for use by all IBMers.
        type: bool
    provider:
        description:
            - Deprecated Provider of this offering.
        type: str
    portal_approval_record:
        description:
            - The portal's approval record ID.
        type: str
    public_original_crn:
        description:
            - The original offering CRN that this publish entry came from.
        type: str
    id:
        description:
            - unique id.
        type: str
    share_with_all:
        description:
            - Denotes public availability of an Offering.
        type: bool
    offering_docs_url:
        description:
            - URL for an additional docs with this offering.
        type: str
    crn:
        description:
            - The crn for this specific offering.
        type: str
    disclaimer:
        description:
            - A disclaimer for this offering.
        type: str
    pc_managed:
        description:
            - Offering is managed by Partner Center.
        type: bool
    catalog_name:
        description:
            - The name of the catalog.
        type: str
    share_enabled:
        description:
            - Denotes access list availability of an Offering.
        type: bool
    created:
        description:
            - The date and time this catalog was created.
        type: str
    publish_approved:
        description:
            - Offering has been approved to publish to permitted to IBM or Public Catalog.
        type: bool
    offering_icon_url:
        description:
            - URL for an icon associated with this offering.
        type: str
    label:
        description:
            - Display Name in the requested language.
        type: str
    long_description:
        description:
            - Long description in the requested language.
        type: str
    url:
        description:
            - The url for this specific offering.
        type: str
    tags:
        description:
            - List of tags associated with this catalog.
        type: list
        elements: str
    catalog_id:
        description:
            - The id of the catalog containing this offering.
        type: str
    permit_request_ibm_public_publish:
        description:
            - Is it permitted to request publishing to IBM or Public.
        type: bool
    name:
        description:
            - The programmatic name of this offering.
        type: str
    publish_public_crn:
        description:
            - The crn of the public catalog entry of this offering.
        type: str
    repo_info:
        description:
            - Repository info for offerings.
        type: dict
        suboptions:
            token:
                description:
                    - Token for private repos.
                type: str
            type:
                description:
                    - Public or enterprise GitHub.
                type: str
    updated:
        description:
            - The date and time this catalog was last updated.
        type: str
    support:
        description:
            - Offering Support information.
        type: dict
        suboptions:
            url:
                description:
                    - URL to be displayed in the Consumption UI for getting support on this offering.
                type: str
            process:
                description:
                    - Support process as provided by an ISV.
                type: str
            locations:
                description:
                    - A list of country codes indicating where support is provided.
                type: list
                elements: str
    provider_info:
        description:
            - Information on the provider for this offering, or omitted if no provider information is given.
        type: dict
        suboptions:
            id:
                description:
                    - The id of this provider.
                type: str
            name:
                description:
                    - The name of this provider.
                type: str
    if_match:
        description:
            - Offering etag contained in quotes.
        type: str
    digest:
        description:
            - Return the digest format of the specified offering.  Default is false.
        type: bool
    catalog_identifier:
        description:
            - Catalog identifier.
        type: str
    type:
        description:
            - Offering Parameter Type.  Valid values are 'name' or 'id'.  Default is 'id'.
        type: str
    updates:
        description:
            - "Updates"
        type: list
        elements: dict
        suboptions:
            op:
                description:
                    - op.
                type: str
            path:
                description:
                    - path
                type: str
            from_:
                description:
                    - from_.
                type: str
            value:
                description:
                    - value
                type: raw
    offering_id:
        description:
            - Offering identification.
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
        offering_support_url=dict(
            type='str',
            required=False),
        metadata=dict(
            type='dict',
            required=False),
        keywords=dict(
            type='list',
            elements=str,
            required=False),
        hidden=dict(
            type='bool',
            required=False),
        public_publish_approved=dict(
            type='bool',
            required=False),
        portal_ui_url=dict(
            type='str',
            required=False),
        rev=dict(
            type='str',
            required=False),
        # Represents the Rating Python class
        rating=dict(
            type='dict',
            options=dict(
                one_star_count=dict(
                    type='int',
                    required=False),
                two_star_count=dict(
                    type='int',
                    required=False),
                three_star_count=dict(
                    type='int',
                    required=False),
                four_star_count=dict(
                    type='int',
                    required=False),
            ),
            required=False),
        kinds=dict(
            type='list',
            elements='dict',
            options=dict(
                id=dict(
                    type='str',
                    required=False),
                format_kind=dict(
                    type='str',
                    required=False),
                target_kind=dict(
                    type='str',
                    required=False),
                metadata=dict(
                    type='dict',
                    required=False),
                install_description=dict(
                    type='str',
                    required=False),
                tags=dict(
                    type='list',
                    elements=str,
                    required=False),
                additional_features=dict(
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
                created=dict(
                    type='str',
                    required=False),
                updated=dict(
                    type='str',
                    required=False),
                versions=dict(
                    type='list',
                    elements='dict',
                    options=dict(
                        id=dict(
                            type='str',
                            required=False),
                        rev=dict(
                            type='str',
                            required=False),
                        crn=dict(
                            type='str',
                            required=False),
                        version=dict(
                            type='str',
                            required=False),
                        sha=dict(
                            type='str',
                            required=False),
                        created=dict(
                            type='str',
                            required=False),
                        updated=dict(
                            type='str',
                            required=False),
                        offering_id=dict(
                            type='str',
                            required=False),
                        catalog_id=dict(
                            type='str',
                            required=False),
                        kind_id=dict(
                            type='str',
                            required=False),
                        tags=dict(
                            type='list',
                            elements=str,
                            required=False),
                        repo_url=dict(
                            type='str',
                            required=False),
                        source_url=dict(
                            type='str',
                            required=False),
                        tgz_url=dict(
                            type='str',
                            required=False),
                        configuration=dict(
                            type='list',
                            elements='dict',
                            options=dict(
                                key=dict(
                                    type='str',
                                    required=False),
                                type=dict(
                                    type='str',
                                    required=False),
                                default_value=dict(
                                    type='raw',
                                    required=False),
                                value_constraint=dict(
                                    type='str',
                                    required=False),
                                description=dict(
                                    type='str',
                                    required=False),
                                required=dict(
                                    type='bool',
                                    required=False),
                                options=dict(
                                    type='list',
                                    elements='raw',
                                    required=False),
                                hidden=dict(
                                    type='bool',
                                    required=False),
                            ),
                            required=False),
                        metadata=dict(
                            type='dict',
                            required=False),
                        validation=dict(
                            type='dict',
                            options=dict(
                                validated=dict(
                                    type='str',
                                    required=False),
                                requested=dict(
                                    type='str',
                                    required=False),
                                state_=dict(
                                    type='str',
                                    required=False),
                                last_operation=dict(
                                    type='str',
                                    required=False),
                                target=dict(
                                    type='dict',
                                    required=False),
                            ),
                            required=False),
                        required_resources=dict(
                            type='list',
                            elements='dict',
                            options=dict(
                                type=dict(
                                    type='str',
                                    required=False),
                                value=dict(
                                    type='raw',
                                    required=False),
                            ),
                            required=False),
                        single_instance=dict(
                            type='bool',
                            required=False),
                        install=dict(
                            type='dict',
                            options=dict(
                                instructions=dict(
                                    type='str',
                                    required=False),
                                script=dict(
                                    type='str',
                                    required=False),
                                script_permission=dict(
                                    type='str',
                                    required=False),
                                delete_script=dict(
                                    type='str',
                                    required=False),
                                scope=dict(
                                    type='str',
                                    required=False),
                            ),
                            required=False),
                        pre_install=dict(
                            type='list',
                            elements='dict',
                            options=dict(
                                instructions=dict(
                                    type='str',
                                    required=False),
                                script=dict(
                                    type='str',
                                    required=False),
                                script_permission=dict(
                                    type='str',
                                    required=False),
                                delete_script=dict(
                                    type='str',
                                    required=False),
                                scope=dict(
                                    type='str',
                                    required=False),
                            ),
                            required=False),
                        entitlement=dict(
                            type='dict',
                            options=dict(
                                provider_name=dict(
                                    type='str',
                                    required=False),
                                provider_id=dict(
                                    type='str',
                                    required=False),
                                product_id=dict(
                                    type='str',
                                    required=False),
                                part_numbers=dict(
                                    type='list',
                                    elements=str,
                                    required=False),
                                image_repo_name=dict(
                                    type='str',
                                    required=False),
                            ),
                            required=False),
                        licenses=dict(
                            type='list',
                            elements='dict',
                            options=dict(
                                id=dict(
                                    type='str',
                                    required=False),
                                name=dict(
                                    type='str',
                                    required=False),
                                type=dict(
                                    type='str',
                                    required=False),
                                url=dict(
                                    type='str',
                                    required=False),
                                description=dict(
                                    type='str',
                                    required=False),
                            ),
                            required=False),
                        image_manifest_url=dict(
                            type='str',
                            required=False),
                        deprecated=dict(
                            type='bool',
                            required=False),
                        package_version=dict(
                            type='str',
                            required=False),
                        state_=dict(
                            type='dict',
                            options=dict(
                                current=dict(
                                    type='str',
                                    required=False),
                                current_entered=dict(
                                    type='str',
                                    required=False),
                                pending=dict(
                                    type='str',
                                    required=False),
                                pending_requested=dict(
                                    type='str',
                                    required=False),
                                previous=dict(
                                    type='str',
                                    required=False),
                            ),
                            required=False),
                        version_locator=dict(
                            type='str',
                            required=False),
                        console_url=dict(
                            type='str',
                            required=False),
                        long_description=dict(
                            type='str',
                            required=False),
                        whitelisted_accounts=dict(
                            type='list',
                            elements=str,
                            required=False),
                    ),
                    required=False),
                plans=dict(
                    type='list',
                    elements='dict',
                    options=dict(
                        id=dict(
                            type='str',
                            required=False),
                        label=dict(
                            type='str',
                            required=False),
                        name=dict(
                            type='str',
                            required=False),
                        short_description=dict(
                            type='str',
                            required=False),
                        long_description=dict(
                            type='str',
                            required=False),
                        metadata=dict(
                            type='dict',
                            required=False),
                        tags=dict(
                            type='list',
                            elements=str,
                            required=False),
                        additional_features=dict(
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
                        created=dict(
                            type='str',
                            required=False),
                        updated=dict(
                            type='str',
                            required=False),
                        deployments=dict(
                            type='list',
                            elements='dict',
                            options=dict(
                                id=dict(
                                    type='str',
                                    required=False),
                                label=dict(
                                    type='str',
                                    required=False),
                                name=dict(
                                    type='str',
                                    required=False),
                                short_description=dict(
                                    type='str',
                                    required=False),
                                long_description=dict(
                                    type='str',
                                    required=False),
                                metadata=dict(
                                    type='dict',
                                    required=False),
                                tags=dict(
                                    type='list',
                                    elements=str,
                                    required=False),
                                created=dict(
                                    type='str',
                                    required=False),
                                updated=dict(
                                    type='str',
                                    required=False),
                            ),
                            required=False),
                    ),
                    required=False),
            ),
            required=False),
        media=dict(
            type='list',
            elements='dict',
            options=dict(
                url=dict(
                    type='str',
                    required=False),
                caption=dict(
                    type='str',
                    required=False),
                type=dict(
                    type='str',
                    required=False),
                thumbnail_url=dict(
                    type='str',
                    required=False),
            ),
            required=False),
        share_with_ibm=dict(
            type='bool',
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
        ibm_publish_approved=dict(
            type='bool',
            required=False),
        provider=dict(
            type='str',
            required=False),
        portal_approval_record=dict(
            type='str',
            required=False),
        public_original_crn=dict(
            type='str',
            required=False),
        id=dict(
            type='str',
            required=False),
        share_with_all=dict(
            type='bool',
            required=False),
        offering_docs_url=dict(
            type='str',
            required=False),
        crn=dict(
            type='str',
            required=False),
        disclaimer=dict(
            type='str',
            required=False),
        pc_managed=dict(
            type='bool',
            required=False),
        catalog_name=dict(
            type='str',
            required=False),
        share_enabled=dict(
            type='bool',
            required=False),
        created=dict(
            type='str',
            required=False),
        publish_approved=dict(
            type='bool',
            required=False),
        offering_icon_url=dict(
            type='str',
            required=False),
        label=dict(
            type='str',
            required=False),
        long_description=dict(
            type='str',
            required=False),
        url=dict(
            type='str',
            required=False),
        tags=dict(
            type='list',
            elements=str,
            required=False),
        catalog_id=dict(
            type='str',
            required=False),
        permit_request_ibm_public_publish=dict(
            type='bool',
            required=False),
        name=dict(
            type='str',
            required=False),
        publish_public_crn=dict(
            type='str',
            required=False),
        # Represents the RepoInfo Python class
        repo_info=dict(
            type='dict',
            options=dict(
                token=dict(
                    type='str',
                    required=False),
                type=dict(
                    type='str',
                    required=False),
            ),
            required=False),
        updated=dict(
            type='str',
            required=False),
        # Represents the Support Python class
        support=dict(
            type='dict',
            options=dict(
                url=dict(
                    type='str',
                    required=False),
                process=dict(
                    type='str',
                    required=False),
                locations=dict(
                    type='list',
                    elements=str,
                    required=False),
            ),
            required=False),
        # Represents the ProviderInfo Python class
        provider_info=dict(
            type='dict',
            options=dict(
                id=dict(
                    type='str',
                    required=False),
                name=dict(
                    type='str',
                    required=False),
            ),
            required=False),
        if_match=dict(
            type='str',
            required=False),
        digest=dict(
            type='bool',
            required=False),
        catalog_identifier=dict(
            type='str',
            required=False),
        type=dict(
            type='str',
            required=False),
        updates=dict(
            type='list',
            options=dict(
                op=dict(
                    type='str',
                    required=False),
                path=dict(
                    type='str',
                    required=False),
                from_=dict(
                    type='str',
                    required=False),
                value=dict(
                    type='raw',
                    required=False),
            ),
            required=False),
        offering_id=dict(
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
    offering_support_url = module.params["offering_support_url"]
    metadata = module.params["metadata"]
    keywords = module.params["keywords"]
    hidden = module.params["hidden"]
    public_publish_approved = module.params["public_publish_approved"]
    portal_ui_url = module.params["portal_ui_url"]
    rev = module.params["rev"]
    rating = module.params["rating"]
    kinds = module.params["kinds"]
    media = module.params["media"]
    share_with_ibm = module.params["share_with_ibm"]
    features = module.params["features"]
    ibm_publish_approved = module.params["ibm_publish_approved"]
    provider = module.params["provider"]
    portal_approval_record = module.params["portal_approval_record"]
    public_original_crn = module.params["public_original_crn"]
    id = module.params["id"]
    share_with_all = module.params["share_with_all"]
    offering_docs_url = module.params["offering_docs_url"]
    crn = module.params["crn"]
    disclaimer = module.params["disclaimer"]
    pc_managed = module.params["pc_managed"]
    catalog_name = module.params["catalog_name"]
    share_enabled = module.params["share_enabled"]
    created = module.params["created"]
    publish_approved = module.params["publish_approved"]
    offering_icon_url = module.params["offering_icon_url"]
    label = module.params["label"]
    long_description = module.params["long_description"]
    url = module.params["url"]
    tags = module.params["tags"]
    catalog_id = module.params["catalog_id"]
    permit_request_ibm_public_publish = module.params["permit_request_ibm_public_publish"]
    name = module.params["name"]
    publish_public_crn = module.params["publish_public_crn"]
    repo_info = module.params["repo_info"]
    updated = module.params["updated"]
    support = module.params["support"]
    provider_info = module.params["provider_info"]
    if_match = module.params["if_match"]
    digest = module.params["digest"]
    catalog_identifier = module.params["catalog_identifier"]
    type = module.params["type"]
    updates = module.params["updates"]
    offering_id = module.params["offering_id"]
    state = module.params["state"]

    sdk = config.get_catalog_management_sdk()
    resource_exists = True

    # Check for existence
    if offering_id:
        try:
            sdk.get_offering(
                catalog_identifier=catalog_identifier,
                offering_id=offering_id,
                type=type,
                digest=digest,
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
                sdk.delete_offering(
                    catalog_identifier=catalog_identifier,
                    offering_id=offering_id,
                )
            except ApiException as ex:
                module.fail_json(msg=ex.message)
            else:
                payload = {"id": offering_id, "status": "deleted"}
                module.exit_json(changed=True, msg=payload)
        else:
            payload = {"id": offering_id, "status": "not_found"}
            module.exit_json(changed=False, msg=payload)

    if state == "present":
        if not resource_exists:
            # Create path
            try:
                result = sdk.create_offering(
                    catalog_identifier=catalog_identifier,
                    id=id,
                    rev=rev,
                    url=url,
                    crn=crn,
                    label=label,
                    name=name,
                    offering_icon_url=offering_icon_url,
                    offering_docs_url=offering_docs_url,
                    offering_support_url=offering_support_url,
                    tags=tags,
                    keywords=keywords,
                    rating=rating,
                    created=created,
                    updated=updated,
                    short_description=short_description,
                    long_description=long_description,
                    features=features,
                    kinds=kinds,
                    pc_managed=pc_managed,
                    publish_approved=publish_approved,
                    share_with_all=share_with_all,
                    share_with_ibm=share_with_ibm,
                    share_enabled=share_enabled,
                    permit_request_ibm_public_publish=permit_request_ibm_public_publish,
                    ibm_publish_approved=ibm_publish_approved,
                    public_publish_approved=public_publish_approved,
                    public_original_crn=public_original_crn,
                    publish_public_crn=publish_public_crn,
                    portal_approval_record=portal_approval_record,
                    portal_ui_url=portal_ui_url,
                    catalog_id=catalog_id,
                    catalog_name=catalog_name,
                    metadata=metadata,
                    disclaimer=disclaimer,
                    hidden=hidden,
                    provider=provider,
                    provider_info=provider_info,
                    repo_info=repo_info,
                    support=support,
                    media=media,
                ).get_result()
            except ApiException as ex:
                module.fail_json(msg=ex.message)
            else:
                module.exit_json(changed=True, msg=result)
        else:
            # Update path
            try:
                result = sdk.update_offering(
                    catalog_identifier=catalog_identifier,
                    offering_id=offering_id,
                    if_match=if_match,
                    updates=updates,
                ).get_result()
            except ApiException as ex:
                module.fail_json(msg=ex.message)
            else:
                module.exit_json(changed=True, msg=result)


def main():
    run_module()


if __name__ == '__main__':
    main()
