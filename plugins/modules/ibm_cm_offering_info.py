#!/usr/bin/python
# coding: utf-8

# (C) Copyright IBM Corp. 2023.
#
# GNU General Public License v3.0+ (see LICENSE or https://www.gnu.org/licenses/gpl-3.0.txt)

from __future__ import (absolute_import, division, print_function)
__metaclass__ = type


DOCUMENTATION = r'''
---
module: ibm_cm_offering_info
short_description: Manage C(cm_offering) for Catalog Management API.
author: IBM SDK Generator (@ibm)
version_added: "1.0.0"
description:
  - This module retrieves one or more C(cm_offering) for Catalog Management API.
requirements:
  - "CatalogManagementV1"
options:
  digest:
    description: "Return the digest format of the specified offering.  Default is false."
    type: bool
  catalog_identifier:
    description: "Catalog identifier."
    type: str
  type:
    description: "Offering Parameter Type.  Valid values are 'name' or 'id'.  Default is 'id'."
    type: str
  offering_id:
    description: "Offering identification."
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
- name: Read ibm_cm_offering
  ibm_cm_offering_info:
    catalog_identifier: 'testString'
    offering_id: 'testString'
    type: 'testString'
    digest: True
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
url:
  description: "The url for this specific offering."
  type: str
  returned: on success for read operation
crn:
  description: "The crn for this specific offering."
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
name:
  description: "The programmatic name of this offering."
  type: str
  returned: on success for read operation
offering_icon_url:
  description: "URL for an icon associated with this offering."
  type: str
  returned: on success for read operation
offering_docs_url:
  description: "URL for an additional docs with this offering."
  type: str
  returned: on success for read operation
offering_support_url:
  description: "[deprecated] - Use offering.support instead.  URL to be displayed in the Consumption
    UI for getting support on this offering."
  type: str
  returned: on success for read operation
tags:
  description: "List of tags associated with this catalog."
  type: list
  elements: str
  returned: on success for read operation
keywords:
  description: "List of keywords associated with offering, typically used to search for it."
  type: list
  elements: str
  returned: on success for read operation
rating:
  description: "Repository info for offerings."
  type: dict
  contains:
    one_star_count:
      description: "One start rating."
      type: int
    two_star_count:
      description: "Two start rating."
      type: int
    three_star_count:
      description: "Three start rating."
      type: int
    four_star_count:
      description: "Four start rating."
      type: int
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
long_description:
  description: "Long description in the requested language."
  type: str
  returned: on success for read operation
long_description_i18n:
  description: "A map of translated strings, by language code."
  type: dict
  returned: on success for read operation
features:
  description: "list of features associated with this offering."
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
kinds:
  description: "Array of kind."
  type: list
  elements: 'dict'
  contains:
    id:
      description: "Unique ID."
      type: str
    format_kind:
      description: "content kind, e.g., helm, vm image."
      type: str
    install_kind:
      description: "install kind, e.g., helm, operator, terraform."
      type: str
    target_kind:
      description: "target cloud to install, e.g., iks, openI(shift)iks."
      type: str
    metadata:
      description: "Open ended metadata information."
      type: dict
    tags:
      description: "List of tags associated with this catalog."
      type: list
      elements: str
    additional_features:
      description: "List of features associated with this offering."
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
    created:
      description: "The date and time this catalog was created."
      type: str
    updated:
      description: "The date and time this catalog was last updated."
      type: str
    versions:
      description: "list of versions."
      type: list
      elements: 'dict'
      contains:
        id:
          description: "Unique ID."
          type: str
        rev:
          description: "Cloudant revision."
          type: str
        crn:
          description: "Version's CRN."
          type: str
        version:
          description: "Version of content type."
          type: str
        flavor:
          description: "Version Flavor Information.  Only supported for Product kind Solution."
          type: dict
          contains:
            name:
              description: "Programmatic name for this flavor."
              type: str
            label:
              description: "Label for this flavor."
              type: str
            label_i18n:
              description: "A map of translated strings, by language code."
              type: dict
            index:
              description: "Order that this flavor should appear when listed for a single version."
              type: int
        sha:
          description: "hash of the content."
          type: str
        created:
          description: "The date and time this version was created."
          type: str
        updated:
          description: "The date and time this version was last updated."
          type: str
        offering_id:
          description: "Offering ID."
          type: str
        catalog_id:
          description: "Catalog ID."
          type: str
        kind_id:
          description: "Kind ID."
          type: str
        tags:
          description: "List of tags associated with this catalog."
          type: list
          elements: str
        repo_url:
          description: "Content's repo URL."
          type: str
        source_url:
          description: "Content's source URL (e.g git repo)."
          type: str
        tgz_url:
          description: "File used to on-board this version."
          type: str
        configuration:
          description: "List of user solicited overrides."
          type: list
          elements: 'dict'
          contains:
            key:
              description: "Configuration key."
              type: str
            type:
              description: "Value type (string, boolean, int)."
              type: str
            default_value:
              description: "The default value.  To use a secret when the type is password, specify a JSON encoded
                value of $ref:#/components/schemas/SecretInstance, prefixed with C(cmsm_v1:)."
              type: dict
            display_name:
              description: "Display name for configuration type."
              type: str
            value_constraint:
              description: "Constraint associated with value, e.g., for string type - regx:[a-z]."
              type: str
            description:
              description: "Key description."
              type: str
            required:
              description: "Is key required to install."
              type: bool
            options:
              description: "List of options of type."
              type: list
              elements: raw
            hidden:
              description: "Hide values."
              type: bool
            custom_config:
              description: "Render type."
              type: dict
              contains:
                type:
                  description: "ID of the widget type."
                  type: str
                grouping:
                  description: "Determines where this configuration type is rendered (3 sections today - Target,
                    Resource, and Deployment)."
                  type: str
                original_grouping:
                  description: "Original grouping type for this configuration (3 types - Target, Resource, and
                    Deployment)."
                  type: str
                grouping_index:
                  description: "Determines the order that this configuration item shows in that particular grouping."
                  type: int
                config_constraints:
                  description: "Map of constraint parameters that will be passed to the custom widget."
                  type: dict
                associations:
                  description: "List of parameters that are associated with this configuration."
                  type: dict
                  contains:
                    parameters:
                      description: "Parameters for this association."
                      type: list
                      elements: 'dict'
                      contains:
                        name:
                          description: "Name of this parameter."
                          type: str
                        options_refresh:
                          description: "Refresh options."
                          type: bool
            type_metadata:
              description: "The original type, as found in the source being onboarded."
              type: str
        outputs:
          description: "List of output values for this version."
          type: list
          elements: 'dict'
          contains:
            key:
              description: "Output key."
              type: str
            description:
              description: "Output description."
              type: str
        iam_permissions:
          description: "List of IAM permissions that are required to consume this version."
          type: list
          elements: 'dict'
          contains:
            service_name:
              description: "Service name."
              type: str
            role_crns:
              description: "Role CRNs for this permission."
              type: list
              elements: str
            resources:
              description: "Resources for this permission."
              type: list
              elements: 'dict'
              contains:
                name:
                  description: "Resource name."
                  type: str
                description:
                  description: "Resource description."
                  type: str
                role_crns:
                  description: "Role CRNs for this permission."
                  type: list
                  elements: str
        metadata:
          description: "Open ended metadata information."
          type: dict
        validation:
          description: "Validation response."
          type: dict
          contains:
            validated:
              description: "Date and time of last successful validation."
              type: str
            requested:
              description: "Date and time of last validation was requested."
              type: str
            state:
              description: "Current validation state - <empty>, in_progress, valid, invalid, expired."
              type: str
            last_operation:
              description: "Last operation (e.g. submit_deployment, generate_installer, install_offering."
              type: str
            target:
              description: "Validation target information (e.g. cluster_id, region, namespace, etc).  Values will
                vary by Content type."
              type: dict
            message_:
              description: "Any message needing to be conveyed as part of the validation job."
              type: str
        required_resources:
          description: "Resource requirments for installation."
          type: list
          elements: 'dict'
          contains:
            type:
              description: "Type of requirement."
              type: str
              choices:
                - 'mem'
                - 'disk'
                - 'cores'
                - 'targetVersion'
                - 'nodes'
            value:
              description: "mem, disk, cores, and nodes can be parsed as an int.  targetVersion will be a semver
                range value."
              type: dict
        single_instance:
          description: "Denotes if single instance can be deployed to a given cluster."
          type: bool
        install:
          description: "Script information."
          type: dict
          contains:
            instructions:
              description: "Instruction on step and by whom (role) that are needed to take place to prepare the
                target for installing this version."
              type: str
            instructions_i18n:
              description: "A map of translated strings, by language code."
              type: dict
            script:
              description: "Optional script that needs to be run post any pre-condition script."
              type: str
            script_permission:
              description: "Optional iam permissions that are required on the target cluster to run this script."
              type: str
            delete_script:
              description: "Optional script that if run will remove the installed version."
              type: str
            scope:
              description: "Optional value indicating if this script is scoped to a namespace or the entire
                cluster."
              type: str
        pre_install:
          description: "Optional pre-install instructions."
          type: list
          elements: 'dict'
          contains:
            instructions:
              description: "Instruction on step and by whom (role) that are needed to take place to prepare the
                target for installing this version."
              type: str
            instructions_i18n:
              description: "A map of translated strings, by language code."
              type: dict
            script:
              description: "Optional script that needs to be run post any pre-condition script."
              type: str
            script_permission:
              description: "Optional iam permissions that are required on the target cluster to run this script."
              type: str
            delete_script:
              description: "Optional script that if run will remove the installed version."
              type: str
            scope:
              description: "Optional value indicating if this script is scoped to a namespace or the entire
                cluster."
              type: str
        entitlement:
          description: "Entitlement license info."
          type: dict
          contains:
            provider_name:
              description: "Provider name."
              type: str
            provider_id:
              description: "Provider ID."
              type: str
            product_id:
              description: "Product ID."
              type: str
            part_numbers:
              description: "list of license entitlement part numbers, eg. D1YGZLL,D1ZXILL."
              type: list
              elements: str
            image_repo_name:
              description: "Image repository name."
              type: str
        licenses:
          description: "List of licenses the product was built with."
          type: list
          elements: 'dict'
          contains:
            id:
              description: "License ID."
              type: str
            name:
              description: "license name."
              type: str
            type:
              description: "type of license e.g., Apache xxx."
              type: str
            url:
              description: "URL for the license text."
              type: str
            description:
              description: "License description."
              type: str
        image_manifest_url:
          description: "If set, denotes a url to a YAML file with list of container images used by this
            version."
          type: str
        deprecated:
          description: "read only field, indicating if this version is deprecated."
          type: bool
        package_version:
          description: "Version of the package used to create this version."
          type: str
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
        version_locator:
          description: "A dotted value of C(catalogID).C(versionID)."
          type: str
        long_description:
          description: "Long description for version."
          type: str
        long_description_i18n:
          description: "A map of translated strings, by language code."
          type: dict
        whitelisted_accounts:
          description: "Whitelisted accounts for version."
          type: list
          elements: str
        image_pull_key_name:
          description: "ID of the image pull key to use from Offering.ImagePullKeys."
          type: str
        deprecate_pending:
          description: "Deprecation information for an Offering."
          type: dict
          contains:
            deprecate_date:
              description: "Date of deprecation."
              type: str
            deprecate_state:
              description: "Deprecation state."
              type: str
            description:
              description: "No description has been provided."
              type: str
        solution_info:
          description: "Version Solution Information.  Only supported for Product kind Solution."
          type: dict
          contains:
            architecture_diagrams:
              description: "Architecture diagrams for this solution."
              type: list
              elements: 'dict'
              contains:
                diagram:
                  description: "Offering Media information."
                  type: dict
                  contains:
                    url:
                      description: "URL of the specified media item."
                      type: str
                    api_url:
                      description: "CM API specific URL of the specified media item."
                      type: str
                    url_proxy:
                      description: "Offering URL proxy information."
                      type: dict
                      contains:
                        url:
                          description: "URL of the specified media item being proxied."
                          type: str
                        sha:
                          description: "SHA256 fingerprint of image."
                          type: str
                    caption:
                      description: "Caption for this media item."
                      type: str
                    caption_i18n:
                      description: "A map of translated strings, by language code."
                      type: dict
                    type:
                      description: "Type of this media item."
                      type: str
                    thumbnail_url:
                      description: "Thumbnail URL for this media item."
                      type: str
                description:
                  description: "Description of this diagram."
                  type: str
                description_i18n:
                  description: "A map of translated strings, by language code."
                  type: dict
            features:
              description: "Features - titles only."
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
            cost_estimate:
              description: "Cost estimate definition."
              type: dict
              contains:
                version:
                  description: "Cost estimate version."
                  type: str
                currency:
                  description: "Cost estimate currency."
                  type: str
                projects:
                  description: "Cost estimate projects."
                  type: list
                  elements: 'dict'
                  contains:
                    name:
                      description: "Project name."
                      type: str
                    metadata:
                      description: "Project metadata."
                      type: dict
                    past_breakdown:
                      description: "Cost breakdown definition."
                      type: dict
                      contains:
                        total_hourly_cost:
                          description: "Total hourly cost."
                          type: str
                        total_monthly_cost:
                          description: "Total monthly cost."
                          type: str
                        resources:
                          description: "Resources."
                          type: list
                          elements: 'dict'
                          contains:
                            name:
                              description: "Resource name."
                              type: str
                            metadata:
                              description: "Resource metadata."
                              type: dict
                            hourly_cost:
                              description: "Hourly cost."
                              type: str
                            monthly_cost:
                              description: "Monthly cost."
                              type: str
                            cost_components:
                              description: "Cost components."
                              type: list
                              elements: 'dict'
                              contains:
                                name:
                                  description: "Cost component name."
                                  type: str
                                unit:
                                  description: "Cost component unit."
                                  type: str
                                hourly_quantity:
                                  description: "Cost component hourly quantity."
                                  type: str
                                monthly_quantity:
                                  description: "Cost component monthly quantity."
                                  type: str
                                price:
                                  description: "Cost component price."
                                  type: str
                                hourly_cost:
                                  description: "Cost component hourly cost."
                                  type: str
                                monthly_cost:
                                  description: "Cost component monthly cist."
                                  type: str
                    breakdown:
                      description: "Cost breakdown definition."
                      type: dict
                      contains:
                        total_hourly_cost:
                          description: "Total hourly cost."
                          type: str
                        total_monthly_cost:
                          description: "Total monthly cost."
                          type: str
                        resources:
                          description: "Resources."
                          type: list
                          elements: 'dict'
                          contains:
                            name:
                              description: "Resource name."
                              type: str
                            metadata:
                              description: "Resource metadata."
                              type: dict
                            hourly_cost:
                              description: "Hourly cost."
                              type: str
                            monthly_cost:
                              description: "Monthly cost."
                              type: str
                            cost_components:
                              description: "Cost components."
                              type: list
                              elements: 'dict'
                              contains:
                                name:
                                  description: "Cost component name."
                                  type: str
                                unit:
                                  description: "Cost component unit."
                                  type: str
                                hourly_quantity:
                                  description: "Cost component hourly quantity."
                                  type: str
                                monthly_quantity:
                                  description: "Cost component monthly quantity."
                                  type: str
                                price:
                                  description: "Cost component price."
                                  type: str
                                hourly_cost:
                                  description: "Cost component hourly cost."
                                  type: str
                                monthly_cost:
                                  description: "Cost component monthly cist."
                                  type: str
                    diff:
                      description: "Cost breakdown definition."
                      type: dict
                      contains:
                        total_hourly_cost:
                          description: "Total hourly cost."
                          type: str
                        total_monthly_cost:
                          description: "Total monthly cost."
                          type: str
                        resources:
                          description: "Resources."
                          type: list
                          elements: 'dict'
                          contains:
                            name:
                              description: "Resource name."
                              type: str
                            metadata:
                              description: "Resource metadata."
                              type: dict
                            hourly_cost:
                              description: "Hourly cost."
                              type: str
                            monthly_cost:
                              description: "Monthly cost."
                              type: str
                            cost_components:
                              description: "Cost components."
                              type: list
                              elements: 'dict'
                              contains:
                                name:
                                  description: "Cost component name."
                                  type: str
                                unit:
                                  description: "Cost component unit."
                                  type: str
                                hourly_quantity:
                                  description: "Cost component hourly quantity."
                                  type: str
                                monthly_quantity:
                                  description: "Cost component monthly quantity."
                                  type: str
                                price:
                                  description: "Cost component price."
                                  type: str
                                hourly_cost:
                                  description: "Cost component hourly cost."
                                  type: str
                                monthly_cost:
                                  description: "Cost component monthly cist."
                                  type: str
                    summary:
                      description: "Cost summary definition."
                      type: dict
                      contains:
                        total_detected_resources:
                          description: "Total detected resources."
                          type: int
                        total_supported_resources:
                          description: "Total supported resources."
                          type: int
                        total_unsupported_resources:
                          description: "Total unsupported resources."
                          type: int
                        total_usage_based_resources:
                          description: "Total usage based resources."
                          type: int
                        total_no_price_resources:
                          description: "Total no price resources."
                          type: int
                        unsupported_resource_counts:
                          description: "Unsupported resource counts."
                          type: dict
                        no_price_resource_counts:
                          description: "No price resource counts."
                          type: dict
                summary:
                  description: "Cost summary definition."
                  type: dict
                  contains:
                    total_detected_resources:
                      description: "Total detected resources."
                      type: int
                    total_supported_resources:
                      description: "Total supported resources."
                      type: int
                    total_unsupported_resources:
                      description: "Total unsupported resources."
                      type: int
                    total_usage_based_resources:
                      description: "Total usage based resources."
                      type: int
                    total_no_price_resources:
                      description: "Total no price resources."
                      type: int
                    unsupported_resource_counts:
                      description: "Unsupported resource counts."
                      type: dict
                    no_price_resource_counts:
                      description: "No price resource counts."
                      type: dict
                total_hourly_cost:
                  description: "Total hourly cost."
                  type: str
                total_monthly_cost:
                  description: "Total monthly cost."
                  type: str
                past_total_hourly_cost:
                  description: "Past total hourly cost."
                  type: str
                past_total_monthly_cost:
                  description: "Past total monthly cost."
                  type: str
                diff_total_hourly_cost:
                  description: "Difference in total hourly cost."
                  type: str
                diff_total_monthly_cost:
                  description: "Difference in total monthly cost."
                  type: str
                time_generated:
                  description: "When this estimate was generated."
                  type: str
            dependencies:
              description: "Dependencies for this solution."
              type: list
              elements: 'dict'
              contains:
                catalog_id:
                  description: "Optional - If not specified, assumes the Public Catalog."
                  type: str
                id:
                  description: "Optional - Offering ID - not required if name is set."
                  type: str
                name:
                  description: "Optional - Programmatic Offering name."
                  type: str
                kind:
                  description: "Format kind."
                  type: str
                version:
                  description: "Required - Semver value or range."
                  type: str
                flavors:
                  description: "Optional - List of dependent flavors in the specified range."
                  type: list
                  elements: str
        is_consumable:
          description: "Is the version able to be shared."
          type: bool
        compliance:
          description: "List of links to sec./compliance controls."
          type: list
          elements: 'dict'
          contains:
            scc_profile:
              description: "SCC profile."
              type: dict
              contains:
                type:
                  description: "Profile type."
                  type: str
            family:
              description: "Control family."
              type: dict
              contains:
                id:
                  description: "ID."
                  type: str
                external_id:
                  description: "External ID."
                  type: str
                description:
                  description: "Description."
                  type: str
                ui_href:
                  description: "UI href."
                  type: str
            goals:
              description: "Control goals."
              type: list
              elements: 'dict'
              contains:
                id:
                  description: "Goal ID."
                  type: str
                description:
                  description: "Goal description."
                  type: str
                ui_href:
                  description: "Goal UI href."
                  type: str
            validation:
              description: "Control validation."
              type: dict
              contains:
                certified:
                  description: "Validation certified bool."
                  type: bool
                results:
                  description: "Map of validation results."
                  type: dict
    plans:
      description: "list of plans."
      type: list
      elements: 'dict'
      contains:
        id:
          description: "unique id."
          type: str
        label:
          description: "Display Name in the requested language."
          type: str
        name:
          description: "The programmatic name of this offering."
          type: str
        short_description:
          description: "Short description in the requested language."
          type: str
        long_description:
          description: "Long description in the requested language."
          type: str
        metadata:
          description: "open ended metadata information."
          type: dict
        tags:
          description: "list of tags associated with this catalog."
          type: list
          elements: str
        additional_features:
          description: "list of features associated with this offering."
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
        created:
          description: "the date'time this catalog was created."
          type: str
        updated:
          description: "the date'time this catalog was last updated."
          type: str
        deployments:
          description: "list of deployments."
          type: list
          elements: 'dict'
          contains:
            id:
              description: "unique id."
              type: str
            label:
              description: "Display Name in the requested language."
              type: str
            name:
              description: "The programmatic name of this offering."
              type: str
            short_description:
              description: "Short description in the requested language."
              type: str
            long_description:
              description: "Long description in the requested language."
              type: str
            metadata:
              description: "open ended metadata information."
              type: dict
            tags:
              description: "list of tags associated with this catalog."
              type: list
              elements: str
            created:
              description: "the date'time this catalog was created."
              type: str
            updated:
              description: "the date'time this catalog was last updated."
              type: str
  returned: on success for read operation
pc_managed:
  description: "Offering is managed by Partner Center."
  type: bool
  returned: on success for read operation
publish_approved:
  description: "Offering has been approved to publish to permitted to IBM or Public Catalog."
  type: bool
  returned: on success for read operation
share_with_all:
  description: "Denotes public availability of an Offering - if share_enabled is true."
  type: bool
  returned: on success for read operation
share_with_ibm:
  description: "Denotes IBM employee availability of an Offering - if share_enabled is true."
  type: bool
  returned: on success for read operation
share_enabled:
  description: "Denotes sharing including access list availability of an Offering is enabled."
  type: bool
  returned: on success for read operation
permit_request_ibm_public_publish:
  description: "Is it permitted to request publishing to IBM or Public."
  type: bool
  returned: on success for read operation
ibm_publish_approved:
  description: "Indicates if this offering has been approved for use by all IBMers."
  type: bool
  returned: on success for read operation
public_publish_approved:
  description: "Indicates if this offering has been approved for use by all IBM Cloud users."
  type: bool
  returned: on success for read operation
public_original_crn:
  description: "The original offering CRN that this publish entry came from."
  type: str
  returned: on success for read operation
publish_public_crn:
  description: "The crn of the public catalog entry of this offering."
  type: str
  returned: on success for read operation
portal_approval_record:
  description: "The portal's approval record ID."
  type: str
  returned: on success for read operation
portal_ui_url:
  description: "The portal UI URL."
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
metadata:
  description: "Map of metadata values for this offering."
  type: dict
  returned: on success for read operation
disclaimer:
  description: "A disclaimer for this offering."
  type: str
  returned: on success for read operation
hidden:
  description: "Determine if this offering should be displayed in the Consumption UI."
  type: bool
  returned: on success for read operation
provider:
  description: "Deprecated - Provider of this offering."
  type: str
  returned: on success for read operation
provider_info:
  description: "Information on the provider for this offering, or omitted if no provider information
    is given."
  type: dict
  contains:
    id:
      description: "The id of this provider."
      type: str
    name:
      description: "The name of this provider."
      type: str
  returned: on success for read operation
repo_info:
  description: "Repository info for offerings."
  type: dict
  contains:
    token:
      description: "Token for private repos."
      type: str
    type:
      description: "Public or enterprise GitHub."
      type: str
  returned: on success for read operation
image_pull_keys:
  description: "Image pull keys for this offering."
  type: list
  elements: 'dict'
  contains:
    name:
      description: "Key name."
      type: str
    value:
      description: "Key value."
      type: str
    description:
      description: "Key description."
      type: str
  returned: on success for read operation
support:
  description: "Offering Support information."
  type: dict
  contains:
    url:
      description: "URL to be displayed in the Consumption UI for getting support on this offering."
      type: str
    process:
      description: "Support process as provided by an ISV."
      type: str
    process_i18n:
      description: "A map of translated strings, by language code."
      type: dict
    locations:
      description: "A list of country codes indicating where support is provided."
      type: list
      elements: str
    support_details:
      description: "A list of support options (e.g. email, phone, slack, other)."
      type: list
      elements: 'dict'
      contains:
        type:
          description: "Type of the current support detail."
          type: str
        contact:
          description: "Contact for the current support detail."
          type: str
        response_wait_time:
          description: "Time descriptor."
          type: dict
          contains:
            value:
              description: "Amount of time to wait in unit 'type'."
              type: int
            type:
              description: "Valid values are hour or day."
              type: str
        availability:
          description: "Times when support is available."
          type: dict
          contains:
            times:
              description: "A list of support times."
              type: list
              elements: 'dict'
              contains:
                day:
                  description: "The day of the week, represented as an integer."
                  type: int
                start_time:
                  description: "HOURS:MINUTES:SECONDS using 24 hour time (e.g. 8:15:00)."
                  type: str
                end_time:
                  description: "HOURS:MINUTES:SECONDS using 24 hour time (e.g. 8:15:00)."
                  type: str
            timezone:
              description: "Timezone (e.g. America/New_York)."
              type: str
            always_available:
              description: "Is this support always available."
              type: bool
    support_escalation:
      description: "Support escalation policy."
      type: dict
      contains:
        escalation_wait_time:
          description: "Time descriptor."
          type: dict
          contains:
            value:
              description: "Amount of time to wait in unit 'type'."
              type: int
            type:
              description: "Valid values are hour or day."
              type: str
        response_wait_time:
          description: "Time descriptor."
          type: dict
          contains:
            value:
              description: "Amount of time to wait in unit 'type'."
              type: int
            type:
              description: "Valid values are hour or day."
              type: str
        contact:
          description: "Escalation contact."
          type: str
    support_type:
      description: "Support type for this product."
      type: str
  returned: on success for read operation
media:
  description: "A list of media items related to this offering."
  type: list
  elements: 'dict'
  contains:
    url:
      description: "URL of the specified media item."
      type: str
    api_url:
      description: "CM API specific URL of the specified media item."
      type: str
    url_proxy:
      description: "Offering URL proxy information."
      type: dict
      contains:
        url:
          description: "URL of the specified media item being proxied."
          type: str
        sha:
          description: "SHA256 fingerprint of image."
          type: str
    caption:
      description: "Caption for this media item."
      type: str
    caption_i18n:
      description: "A map of translated strings, by language code."
      type: dict
    type:
      description: "Type of this media item."
      type: str
    thumbnail_url:
      description: "Thumbnail URL for this media item."
      type: str
  returned: on success for read operation
deprecate_pending:
  description: "Deprecation information for an Offering."
  type: dict
  contains:
    deprecate_date:
      description: "Date of deprecation."
      type: str
    deprecate_state:
      description: "Deprecation state."
      type: str
    description:
      description: "No description has been provided."
      type: str
  returned: on success for read operation
product_kind:
  description: "The product kind.  Valid values are module, solution, or empty string."
  type: str
  returned: on success for read operation
badges:
  description: "A list of badges for this offering."
  type: list
  elements: 'dict'
  contains:
    id:
      description: "ID of the current badge."
      type: str
    label:
      description: "Display name for the current badge."
      type: str
    label_i18n:
      description: "A map of translated strings, by language code."
      type: dict
    description:
      description: "Description of the current badge."
      type: str
    description_i18n:
      description: "A map of translated strings, by language code."
      type: dict
    icon:
      description: "Icon for the current badge."
      type: str
    authority:
      description: "Authority for the current badge."
      type: str
    tag:
      description: "Tag for the current badge."
      type: str
    learn_more_links:
      description: "Learn more links for a badge."
      type: dict
      contains:
        first_party:
          description: "First party link."
          type: str
        third_party:
          description: "Third party link."
          type: str
    constraints:
      description: "An optional set of constraints indicating which versions in an Offering have this
        particular badge."
      type: list
      elements: 'dict'
      contains:
        type:
          description: "Type of the current constraint."
          type: str
        rule:
          description: "Rule for the current constraint."
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
        digest=dict(
            type='bool',
            required=False),
        catalog_identifier=dict(
            type='str',
            required=False),
        type=dict(
            type='str',
            required=False),
        offering_id=dict(
            type='str',
            required=False),
    )

    module = AnsibleModule(
        argument_spec=module_args,
        supports_check_mode=True
    )

    if MISSING_IMPORT_EXC is not None:
        module.fail_json(msg='Missing required import: ' + MISSING_IMPORT_EXC.msg)

    digest = module.params["digest"]
    catalog_identifier = module.params["catalog_identifier"]
    type = module.params["type"]
    offering_id = module.params["offering_id"]

    if module.check_mode:
        module.exit_json(msg='The module would run with the following parameters: ' + module.paramss)

    authenticator = get_authenticator(service_name='catalog_management')
    if authenticator is None:
        module.fail_json(msg='Cannot create the authenticator.')

    sdk = CatalogManagementV1(
        authenticator=authenticator,
    )

    sdk.configure_service('catalog_management')

    if offering_id:
        # read
        try:
            response = sdk.get_offering(
                catalog_identifier=catalog_identifier,
                offering_id=offering_id,
                type=type,
                digest=digest,
            )

            result = response.get_result()

            module.exit_json(**result)
        except ApiException as ex:
            module.fail_json(msg=ex.message)


def main():
    run_module()


if __name__ == '__main__':
    main()
