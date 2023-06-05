#!/usr/bin/python
# coding: utf-8

# (C) Copyright IBM Corp. 2023.
#
# GNU General Public License v3.0+ (see LICENSE or https://www.gnu.org/licenses/gpl-3.0.txt)

from __future__ import (absolute_import, division, print_function)
__metaclass__ = type


DOCUMENTATION = r'''
---
module: ibm_cm_offering
short_description: Manage C(cm_offerings) for Catalog Management API.
author: IBM SDK Generator (@ibm)
version_added: "1.0.0"
description:
  - This module creates, updates, or deletes a C(cm_offering) resource for Catalog Management API.
requirements:
  - "CatalogManagementV1"
options:
  short_description:
    description: "Short description in the requested language."
    type: str
  offering_support_url:
    description: "[deprecated] - Use offering.support instead.  URL to be displayed in the Consumption
      UI for getting support on this offering."
    type: str
  metadata:
    description: "Map of metadata values for this offering."
    type: dict
  keywords:
    description: "List of keywords associated with offering, typically used to search for it."
    type: list
    elements: str
  hidden:
    description: "Determine if this offering should be displayed in the Consumption UI."
    type: bool
  public_publish_approved:
    description: "Indicates if this offering has been approved for use by all IBM Cloud users."
    type: bool
  portal_ui_url:
    description: "The portal UI URL."
    type: str
  rating:
    description: "Repository info for offerings."
    type: dict
    suboptions:
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
  kinds:
    description: "Array of kind."
    type: list
    elements: 'dict'
    suboptions:
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
        suboptions:
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
            suboptions:
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
            suboptions:
              key:
                description: "Configuration key."
                type: str
              type:
                description: "Value type (string, boolean, int)."
                type: str
              default_value:
                description: "The default value.  To use a secret when the type is password, specify a JSON encoded
                  value of $ref:#/components/schemas/SecretInstance, prefixed with C(cmsm_v1:)."
                type: raw
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
                suboptions:
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
                    suboptions:
                      parameters:
                        description: "Parameters for this association."
                        type: list
                        elements: 'dict'
                        suboptions:
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
            suboptions:
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
            suboptions:
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
                suboptions:
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
            suboptions:
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
            suboptions:
              type:
                description: "Type of requirement."
                type: str
                choices:
                  - "mem"
                  - "disk"
                  - "cores"
                  - "targetVersion"
                  - "nodes"
              value:
                description: "mem, disk, cores, and nodes can be parsed as an int.  targetVersion will be a semver
                  range value."
                type: raw
          single_instance:
            description: "Denotes if single instance can be deployed to a given cluster."
            type: bool
          install:
            description: "Script information."
            type: dict
            suboptions:
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
            suboptions:
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
            suboptions:
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
            suboptions:
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
            suboptions:
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
            suboptions:
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
            suboptions:
              architecture_diagrams:
                description: "Architecture diagrams for this solution."
                type: list
                elements: 'dict'
                suboptions:
                  diagram:
                    description: "Offering Media information."
                    type: dict
                    suboptions:
                      url:
                        description: "URL of the specified media item."
                        type: str
                      api_url:
                        description: "CM API specific URL of the specified media item."
                        type: str
                      url_proxy:
                        description: "Offering URL proxy information."
                        type: dict
                        suboptions:
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
              cost_estimate:
                description: "Cost estimate definition."
                type: dict
                suboptions:
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
                    suboptions:
                      name:
                        description: "Project name."
                        type: str
                      metadata:
                        description: "Project metadata."
                        type: dict
                      past_breakdown:
                        description: "Cost breakdown definition."
                        type: dict
                        suboptions:
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
                            suboptions:
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
                                suboptions:
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
                        suboptions:
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
                            suboptions:
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
                                suboptions:
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
                        suboptions:
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
                            suboptions:
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
                                suboptions:
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
                        suboptions:
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
                    suboptions:
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
                suboptions:
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
            suboptions:
              scc_profile:
                description: "SCC profile."
                type: dict
                suboptions:
                  type:
                    description: "Profile type."
                    type: str
              family:
                description: "Control family."
                type: dict
                suboptions:
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
                suboptions:
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
                suboptions:
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
        suboptions:
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
            suboptions:
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
  media:
    description: "A list of media items related to this offering."
    type: list
    elements: 'dict'
    suboptions:
      url:
        description: "URL of the specified media item."
        type: str
      api_url:
        description: "CM API specific URL of the specified media item."
        type: str
      url_proxy:
        description: "Offering URL proxy information."
        type: dict
        suboptions:
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
  share_with_ibm:
    description: "Denotes IBM employee availability of an Offering - if share_enabled is true."
    type: bool
  product_kind:
    description: "The product kind.  Valid values are module, solution, or empty string."
    type: str
  features:
    description: "list of features associated with this offering."
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
  ibm_publish_approved:
    description: "Indicates if this offering has been approved for use by all IBMers."
    type: bool
  provider:
    description: "Deprecated - Provider of this offering."
    type: str
  portal_approval_record:
    description: "The portal's approval record ID."
    type: str
  public_original_crn:
    description: "The original offering CRN that this publish entry came from."
    type: str
  share_with_all:
    description: "Denotes public availability of an Offering - if share_enabled is true."
    type: bool
  offering_docs_url:
    description: "URL for an additional docs with this offering."
    type: str
  crn:
    description: "The crn for this specific offering."
    type: str
  disclaimer:
    description: "A disclaimer for this offering."
    type: str
  label_i18n:
    description: "A map of translated strings, by language code."
    type: dict
  pc_managed:
    description: "Offering is managed by Partner Center."
    type: bool
  catalog_name:
    description: "The name of the catalog."
    type: str
  share_enabled:
    description: "Denotes sharing including access list availability of an Offering is enabled."
    type: bool
  created:
    description: "The date and time this catalog was created."
    type: str
  publish_approved:
    description: "Offering has been approved to publish to permitted to IBM or Public Catalog."
    type: bool
  offering_icon_url:
    description: "URL for an icon associated with this offering."
    type: str
  label:
    description: "Display Name in the requested language."
    type: str
  long_description:
    description: "Long description in the requested language."
    type: str
  url:
    description: "The url for this specific offering."
    type: str
  tags:
    description: "List of tags associated with this catalog."
    type: list
    elements: str
  catalog_id:
    description: "The id of the catalog containing this offering."
    type: str
  badges:
    description: "A list of badges for this offering."
    type: list
    elements: 'dict'
    suboptions:
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
        suboptions:
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
        suboptions:
          type:
            description: "Type of the current constraint."
            type: str
          rule:
            description: "Rule for the current constraint."
            type: raw
  image_pull_keys:
    description: "Image pull keys for this offering."
    type: list
    elements: 'dict'
    suboptions:
      name:
        description: "Key name."
        type: str
      value:
        description: "Key value."
        type: str
      description:
        description: "Key description."
        type: str
  deprecate_pending:
    description: "Deprecation information for an Offering."
    type: dict
    suboptions:
      deprecate_date:
        description: "Date of deprecation."
        type: str
      deprecate_state:
        description: "Deprecation state."
        type: str
      description:
        description: "No description has been provided."
        type: str
  permit_request_ibm_public_publish:
    description: "Is it permitted to request publishing to IBM or Public."
    type: bool
  name:
    description: "The programmatic name of this offering."
    type: str
  publish_public_crn:
    description: "The crn of the public catalog entry of this offering."
    type: str
  repo_info:
    description: "Repository info for offerings."
    type: dict
    suboptions:
      token:
        description: "Token for private repos."
        type: str
      type:
        description: "Public or enterprise GitHub."
        type: str
  updated:
    description: "The date and time this catalog was last updated."
    type: str
  long_description_i18n:
    description: "A map of translated strings, by language code."
    type: dict
  support:
    description: "Offering Support information."
    type: dict
    suboptions:
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
        suboptions:
          type:
            description: "Type of the current support detail."
            type: str
          contact:
            description: "Contact for the current support detail."
            type: str
          response_wait_time:
            description: "Time descriptor."
            type: dict
            suboptions:
              value:
                description: "Amount of time to wait in unit 'type'."
                type: int
              type:
                description: "Valid values are hour or day."
                type: str
          availability:
            description: "Times when support is available."
            type: dict
            suboptions:
              times:
                description: "A list of support times."
                type: list
                elements: 'dict'
                suboptions:
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
        suboptions:
          escalation_wait_time:
            description: "Time descriptor."
            type: dict
            suboptions:
              value:
                description: "Amount of time to wait in unit 'type'."
                type: int
              type:
                description: "Valid values are hour or day."
                type: str
          response_wait_time:
            description: "Time descriptor."
            type: dict
            suboptions:
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
  short_description_i18n:
    description: "A map of translated strings, by language code."
    type: dict
  provider_info:
    description: "Information on the provider for this offering, or omitted if no provider information
      is given."
    type: dict
    suboptions:
      id:
        description: "The id of this provider."
        type: str
      name:
        description: "The name of this provider."
        type: str
  if_match:
    description: "Offering etag contained in quotes."
    type: str
  digest:
    description: "Return the digest format of the specified offering.  Default is false."
    type: bool
  catalog_identifier:
    description: "Catalog identifier."
    type: str
  type:
    description: "Offering Parameter Type.  Valid values are 'name' or 'id'.  Default is 'id'."
    type: str
  updates:
    description: "No description has been provided."
    type: list
    elements: dict
    suboptions:
      op:
        description: "The operation to be performed."
        type: str
        choices:
          - "add"
          - "remove"
          - "replace"
          - "move"
          - "copy"
          - "test"
      path:
        description: "A JSON-Pointer."
        type: str
      value:
        description: "The value to be used within the operations."
        type: raw
      from_:
        description: "A string containing a JSON Pointer value."
        type: str
  offering_id:
    description: "Offering identification."
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
- name: Create ibm_cm_offering
  vars:
    rating_model:
      one_star_count: 38
      two_star_count: 38
      three_star_count: 38
      four_star_count: 38
    feature_model:
      title: 'testString'
      title_i18n: {'key1': 'testString'}
      description: 'testString'
      description_i18n: {'key1': 'testString'}
    flavor_model:
      name: 'testString'
      label: 'testString'
      label_i18n: {'key1': 'testString'}
      index: 38
    render_type_associations_parameters_item_model:
      name: 'testString'
      options_refresh: True
    render_type_associations_model:
      parameters: [render_type_associations_parameters_item_model]
    render_type_model:
      type: 'testString'
      grouping: 'testString'
      original_grouping: 'testString'
      grouping_index: 38
      config_constraints: {'key1': {'foo': 'bar'}}
      associations: render_type_associations_model
    configuration_model:
      key: 'testString'
      type: 'testString'
      default_value: 'testString'
      display_name: 'testString'
      value_constraint: 'testString'
      description: 'testString'
      required: True
      options: ['testString']
      hidden: True
      custom_config: render_type_model
      type_metadata: 'testString'
    output_model:
      key: 'testString'
      description: 'testString'
    iam_resource_model:
      name: 'testString'
      description: 'testString'
      role_crns: ['testString']
    iam_permission_model:
      service_name: 'testString'
      role_crns: ['testString']
      resources: [iam_resource_model]
    validation_model:
      validated: '2019-01-01T12:00:00.000Z'
      requested: '2019-01-01T12:00:00.000Z'
      state: 'testString'
      last_operation: 'testString'
      target: {'key1': {'foo': 'bar'}}
      message_: 'testString'
    resource_model:
      type: 'mem'
      value: 'testString'
    script_model:
      instructions: 'testString'
      instructions_i18n: {'key1': 'testString'}
      script: 'testString'
      script_permission: 'testString'
      delete_script: 'testString'
      scope: 'testString'
    version_entitlement_model:
      provider_name: 'testString'
      provider_id: 'testString'
      product_id: 'testString'
      part_numbers: ['testString']
      image_repo_name: 'testString'
    license_model:
      id: 'testString'
      name: 'testString'
      type: 'testString'
      url: 'testString'
      description: 'testString'
    state_model:
      current: 'testString'
      current_entered: '2019-01-01T12:00:00.000Z'
      pending: 'testString'
      pending_requested: '2019-01-01T12:00:00.000Z'
      previous: 'testString'
    deprecate_pending_model:
      deprecate_date: '2019-01-01T12:00:00.000Z'
      deprecate_state: 'testString'
      description: 'testString'
    url_proxy_model:
      url: 'testString'
      sha: 'testString'
    media_item_model:
      url: 'testString'
      api_url: 'testString'
      url_proxy: url_proxy_model
      caption: 'testString'
      caption_i18n: {'key1': 'testString'}
      type: 'testString'
      thumbnail_url: 'testString'
    architecture_diagram_model:
      diagram: media_item_model
      description: 'testString'
      description_i18n: {'key1': 'testString'}
    cost_component_model:
      name: 'testString'
      unit: 'testString'
      hourly_quantity: 'testString'
      monthly_quantity: 'testString'
      price: 'testString'
      hourly_cost: 'testString'
      monthly_cost: 'testString'
    cost_resource_model:
      name: 'testString'
      metadata: {'key1': {'foo': 'bar'}}
      hourly_cost: 'testString'
      monthly_cost: 'testString'
      cost_components: [cost_component_model]
    cost_breakdown_model:
      total_hourly_cost: 'testString'
      total_monthly_cost: 'testString'
      resources: [cost_resource_model]
    cost_summary_model:
      total_detected_resources: 38
      total_supported_resources: 38
      total_unsupported_resources: 38
      total_usage_based_resources: 38
      total_no_price_resources: 38
      unsupported_resource_counts: {'key1': 38}
      no_price_resource_counts: {'key1': 38}
    project_model:
      name: 'testString'
      metadata: {'key1': {'foo': 'bar'}}
      past_breakdown: cost_breakdown_model
      breakdown: cost_breakdown_model
      diff: cost_breakdown_model
      summary: cost_summary_model
    cost_estimate_model:
      version: 'testString'
      currency: 'testString'
      projects: [project_model]
      summary: cost_summary_model
      total_hourly_cost: 'testString'
      total_monthly_cost: 'testString'
      past_total_hourly_cost: 'testString'
      past_total_monthly_cost: 'testString'
      diff_total_hourly_cost: 'testString'
      diff_total_monthly_cost: 'testString'
      time_generated: '2019-01-01T12:00:00.000Z'
    offering_reference_model:
      catalog_id: 'testString'
      id: 'testString'
      name: 'testString'
      kind: 'testString'
      version: 'testString'
      flavors: ['testString']
    solution_info_model:
      architecture_diagrams: [architecture_diagram_model]
      features: [feature_model]
      cost_estimate: cost_estimate_model
      dependencies: [offering_reference_model]
    compliance_control_scc_profile_model:
      type: 'testString'
    compliance_control_family_model:
      id: 'testString'
      external_id: 'testString'
      description: 'testString'
      ui_href: 'testString'
    goal_model:
      id: 'testString'
      description: 'testString'
      ui_href: 'testString'
    compliance_control_validation_model:
      certified: True
      results: {'key1': {'foo': 'bar'}}
    compliance_control_model:
      scc_profile: compliance_control_scc_profile_model
      family: compliance_control_family_model
      goals: [goal_model]
      validation: compliance_control_validation_model
    version_model:
      crn: 'testString'
      version: 'testString'
      flavor: flavor_model
      sha: 'testString'
      created: '2019-01-01T12:00:00.000Z'
      updated: '2019-01-01T12:00:00.000Z'
      offering_id: offering_id_link
      catalog_id: catalog_id_link
      kind_id: 'testString'
      tags: ['testString']
      repo_url: 'testString'
      source_url: 'testString'
      tgz_url: 'testString'
      configuration: [configuration_model]
      outputs: [output_model]
      iam_permissions: [iam_permission_model]
      metadata: {'key1': {'foo': 'bar'}}
      validation: validation_model
      required_resources: [resource_model]
      single_instance: True
      install: script_model
      pre_install: [script_model]
      entitlement: version_entitlement_model
      licenses: [license_model]
      image_manifest_url: 'testString'
      deprecated: True
      package_version: 'testString'
      state: state_model
      version_locator: version_id_link
      long_description: 'testString'
      long_description_i18n: {'key1': 'testString'}
      whitelisted_accounts: ['testString']
      image_pull_key_name: 'testString'
      deprecate_pending: deprecate_pending_model
      solution_info: solution_info_model
      is_consumable: True
      compliance: [compliance_control_model]
    deployment_model:
      id: 'testString'
      label: 'testString'
      name: 'testString'
      short_description: 'testString'
      long_description: 'testString'
      metadata: {'key1': {'foo': 'bar'}}
      tags: ['testString']
      created: '2019-01-01T12:00:00.000Z'
      updated: '2019-01-01T12:00:00.000Z'
    plan_model:
      id: 'testString'
      label: 'testString'
      name: 'testString'
      short_description: 'testString'
      long_description: 'testString'
      metadata: {'key1': {'foo': 'bar'}}
      tags: ['testString']
      additional_features: [feature_model]
      created: '2019-01-01T12:00:00.000Z'
      updated: '2019-01-01T12:00:00.000Z'
      deployments: [deployment_model]
    kind_model:
      id: 'testString'
      format_kind: 'testString'
      install_kind: 'testString'
      target_kind: 'testString'
      metadata: {'key1': {'foo': 'bar'}}
      tags: ['testString']
      additional_features: [feature_model]
      created: '2019-01-01T12:00:00.000Z'
      updated: '2019-01-01T12:00:00.000Z'
      versions: [version_model]
      plans: [plan_model]
    provider_info_model:
      id: 'testString'
      name: 'testString'
    repo_info_model:
      token: 'testString'
      type: 'testString'
    image_pull_key_model:
      name: 'testString'
      value: 'testString'
      description: 'testString'
    support_wait_time_model:
      value: 38
      type: 'testString'
    support_time_model:
      day: 38
      start_time: 'testString'
      end_time: 'testString'
    support_availability_model:
      times: [support_time_model]
      timezone: 'testString'
      always_available: True
    support_detail_model:
      type: 'testString'
      contact: 'testString'
      response_wait_time: support_wait_time_model
      availability: support_availability_model
    support_escalation_model:
      escalation_wait_time: support_wait_time_model
      response_wait_time: support_wait_time_model
      contact: 'testString'
    support_model:
      url: 'testString'
      process: 'testString'
      process_i18n: {'key1': 'testString'}
      locations: ['testString']
      support_details: [support_detail_model]
      support_escalation: support_escalation_model
      support_type: 'testString'
    learn_more_links_model:
      first_party: 'testString'
      third_party: 'testString'
    constraint_model:
      type: 'testString'
      rule: 'testString'
    badge_model:
      id: 'testString'
      label: 'testString'
      label_i18n: {'key1': 'testString'}
      description: 'testString'
      description_i18n: {'key1': 'testString'}
      icon: 'testString'
      authority: 'testString'
      tag: 'testString'
      learn_more_links: learn_more_links_model
      constraints: [constraint_model]
  ibm_cm_offering:
    catalog_identifier: 'testString'
    url: 'testString'
    crn: 'testString'
    label: 'testString'
    label_i18n: {'key1': 'testString'}
    name: 'testString'
    offering_icon_url: 'testString'
    offering_docs_url: 'testString'
    offering_support_url: 'testString'
    tags: ['testString']
    keywords: ['testString']
    rating: '{{ rating_model }}'
    created: '2019-01-01T12:00:00.000Z'
    updated: '2019-01-01T12:00:00.000Z'
    short_description: 'testString'
    short_description_i18n: {'key1': 'testString'}
    long_description: 'testString'
    long_description_i18n: {'key1': 'testString'}
    features: [feature_model]
    kinds: [kind_model]
    pc_managed: True
    publish_approved: True
    share_with_all: True
    share_with_ibm: True
    share_enabled: True
    permit_request_ibm_public_publish: True
    ibm_publish_approved: True
    public_publish_approved: True
    public_original_crn: 'testString'
    publish_public_crn: 'testString'
    portal_approval_record: 'testString'
    portal_ui_url: 'testString'
    catalog_id: catalog_id_link
    catalog_name: 'testString'
    metadata: {'key1': {'foo': 'bar'}}
    disclaimer: 'testString'
    hidden: True
    provider: 'testString'
    provider_info: '{{ provider_info_model }}'
    repo_info: '{{ repo_info_model }}'
    image_pull_keys: [image_pull_key_model]
    support: '{{ support_model }}'
    media: [media_item_model]
    deprecate_pending: '{{ deprecate_pending_model }}'
    product_kind: 'testString'
    badges: [badge_model]
    state: present

- name: Update ibm_cm_offering
  vars:
    json_patch_operation_model:
      op: 'add'
      path: 'testString'
      value: 'testString'
      from_: 'testString'
  ibm_cm_offering:
    catalog_identifier: 'testString'
    offering_id: 'testString'
    if_match: 'testString'
    updates: [json_patch_operation_model]
    state: present

- name: Delete ibm_cm_offering
  ibm_cm_offering:
    catalog_identifier: 'testString'
    offering_id: 'testString'
    state: absent
'''

RETURN = r'''
id:
  description: "unique id."
  type: str
  returned: on success for create, update, delete operations
rev:
  description: "Cloudant revision."
  type: str
  returned: on success for create, update operations
url:
  description: "The url for this specific offering."
  type: str
  returned: on success for create, update operations
crn:
  description: "The crn for this specific offering."
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
name:
  description: "The programmatic name of this offering."
  type: str
  returned: on success for create, update operations
offering_icon_url:
  description: "URL for an icon associated with this offering."
  type: str
  returned: on success for create, update operations
offering_docs_url:
  description: "URL for an additional docs with this offering."
  type: str
  returned: on success for create, update operations
offering_support_url:
  description: "[deprecated] - Use offering.support instead.  URL to be displayed in the Consumption
    UI for getting support on this offering."
  type: str
  returned: on success for create, update operations
tags:
  description: "List of tags associated with this catalog."
  type: list
  elements: str
  returned: on success for create, update operations
keywords:
  description: "List of keywords associated with offering, typically used to search for it."
  type: list
  elements: str
  returned: on success for create, update operations
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
  returned: on success for create, update operations
created:
  description: "The date and time this catalog was created."
  type: str
  returned: on success for create, update operations
updated:
  description: "The date and time this catalog was last updated."
  type: str
  returned: on success for create, update operations
short_description:
  description: "Short description in the requested language."
  type: str
  returned: on success for create, update operations
short_description_i18n:
  description: "A map of translated strings, by language code."
  type: dict
  returned: on success for create, update operations
long_description:
  description: "Long description in the requested language."
  type: str
  returned: on success for create, update operations
long_description_i18n:
  description: "A map of translated strings, by language code."
  type: dict
  returned: on success for create, update operations
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
  returned: on success for create, update operations
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
  returned: on success for create, update operations
pc_managed:
  description: "Offering is managed by Partner Center."
  type: bool
  returned: on success for create, update operations
publish_approved:
  description: "Offering has been approved to publish to permitted to IBM or Public Catalog."
  type: bool
  returned: on success for create, update operations
share_with_all:
  description: "Denotes public availability of an Offering - if share_enabled is true."
  type: bool
  returned: on success for create, update operations
share_with_ibm:
  description: "Denotes IBM employee availability of an Offering - if share_enabled is true."
  type: bool
  returned: on success for create, update operations
share_enabled:
  description: "Denotes sharing including access list availability of an Offering is enabled."
  type: bool
  returned: on success for create, update operations
permit_request_ibm_public_publish:
  description: "Is it permitted to request publishing to IBM or Public."
  type: bool
  returned: on success for create, update operations
ibm_publish_approved:
  description: "Indicates if this offering has been approved for use by all IBMers."
  type: bool
  returned: on success for create, update operations
public_publish_approved:
  description: "Indicates if this offering has been approved for use by all IBM Cloud users."
  type: bool
  returned: on success for create, update operations
public_original_crn:
  description: "The original offering CRN that this publish entry came from."
  type: str
  returned: on success for create, update operations
publish_public_crn:
  description: "The crn of the public catalog entry of this offering."
  type: str
  returned: on success for create, update operations
portal_approval_record:
  description: "The portal's approval record ID."
  type: str
  returned: on success for create, update operations
portal_ui_url:
  description: "The portal UI URL."
  type: str
  returned: on success for create, update operations
catalog_id:
  description: "The id of the catalog containing this offering."
  type: str
  returned: on success for create, update operations
catalog_name:
  description: "The name of the catalog."
  type: str
  returned: on success for create, update operations
metadata:
  description: "Map of metadata values for this offering."
  type: dict
  returned: on success for create, update operations
disclaimer:
  description: "A disclaimer for this offering."
  type: str
  returned: on success for create, update operations
hidden:
  description: "Determine if this offering should be displayed in the Consumption UI."
  type: bool
  returned: on success for create, update operations
provider:
  description: "Deprecated - Provider of this offering."
  type: str
  returned: on success for create, update operations
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
  returned: on success for create, update operations
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
  returned: on success for create, update operations
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
  returned: on success for create, update operations
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
  returned: on success for create, update operations
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
  returned: on success for create, update operations
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
  returned: on success for create, update operations
product_kind:
  description: "The product kind.  Valid values are module, solution, or empty string."
  type: str
  returned: on success for create, update operations
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
            elements='str',
            no_log=True,
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
                install_kind=dict(
                    type='str',
                    required=False),
                target_kind=dict(
                    type='str',
                    required=False),
                metadata=dict(
                    type='dict',
                    required=False),
                tags=dict(
                    type='list',
                    elements='str',
                    required=False),
                additional_features=dict(
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
                        flavor=dict(
                            type='dict',
                            options=dict(
                                name=dict(
                                    type='str',
                                    required=False),
                                label=dict(
                                    type='str',
                                    required=False),
                                label_i18n=dict(
                                    type='dict',
                                    required=False),
                                index=dict(
                                    type='int',
                                    required=False),
                            ),
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
                            elements='str',
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
                                    no_log=True,
                                    required=False),
                                type=dict(
                                    type='str',
                                    required=False),
                                default_value=dict(
                                    type='raw',
                                    required=False),
                                display_name=dict(
                                    type='str',
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
                                custom_config=dict(
                                    type='dict',
                                    options=dict(
                                        type=dict(
                                            type='str',
                                            required=False),
                                        grouping=dict(
                                            type='str',
                                            required=False),
                                        original_grouping=dict(
                                            type='str',
                                            required=False),
                                        grouping_index=dict(
                                            type='int',
                                            required=False),
                                        config_constraints=dict(
                                            type='dict',
                                            required=False),
                                        associations=dict(
                                            type='dict',
                                            options=dict(
                                                parameters=dict(
                                                    type='list',
                                                    elements='dict',
                                                    options=dict(
                                                        name=dict(
                                                            type='str',
                                                            required=False),
                                                        options_refresh=dict(
                                                            type='bool',
                                                            required=False),
                                                    ),
                                                    required=False),
                                            ),
                                            required=False),
                                    ),
                                    required=False),
                                type_metadata=dict(
                                    type='str',
                                    required=False),
                            ),
                            required=False),
                        outputs=dict(
                            type='list',
                            elements='dict',
                            options=dict(
                                key=dict(
                                    type='str',
                                    no_log=True,
                                    required=False),
                                description=dict(
                                    type='str',
                                    required=False),
                            ),
                            required=False),
                        iam_permissions=dict(
                            type='list',
                            elements='dict',
                            options=dict(
                                service_name=dict(
                                    type='str',
                                    required=False),
                                role_crns=dict(
                                    type='list',
                                    elements='str',
                                    required=False),
                                resources=dict(
                                    type='list',
                                    elements='dict',
                                    options=dict(
                                        name=dict(
                                            type='str',
                                            required=False),
                                        description=dict(
                                            type='str',
                                            required=False),
                                        role_crns=dict(
                                            type='list',
                                            elements='str',
                                            required=False),
                                    ),
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
                                state=dict(
                                    type='str',
                                    required=False),
                                last_operation=dict(
                                    type='str',
                                    required=False),
                                target=dict(
                                    type='dict',
                                    required=False),
                                message_=dict(
                                    type='str',
                                    required=False),
                            ),
                            required=False),
                        required_resources=dict(
                            type='list',
                            elements='dict',
                            options=dict(
                                type=dict(
                                    type='str',
                                    choices=[
                                        'mem',
                                        'disk',
                                        'cores',
                                        'targetVersion',
                                        'nodes',
                                    ],
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
                                instructions_i18n=dict(
                                    type='dict',
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
                                instructions_i18n=dict(
                                    type='dict',
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
                                    elements='str',
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
                        state=dict(
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
                        long_description=dict(
                            type='str',
                            required=False),
                        long_description_i18n=dict(
                            type='dict',
                            required=False),
                        whitelisted_accounts=dict(
                            type='list',
                            elements='str',
                            required=False),
                        image_pull_key_name=dict(
                            type='str',
                            required=False),
                        deprecate_pending=dict(
                            type='dict',
                            options=dict(
                                deprecate_date=dict(
                                    type='str',
                                    required=False),
                                deprecate_state=dict(
                                    type='str',
                                    required=False),
                                description=dict(
                                    type='str',
                                    required=False),
                            ),
                            required=False),
                        solution_info=dict(
                            type='dict',
                            options=dict(
                                architecture_diagrams=dict(
                                    type='list',
                                    elements='dict',
                                    options=dict(
                                        diagram=dict(
                                            type='dict',
                                            options=dict(
                                                url=dict(
                                                    type='str',
                                                    required=False),
                                                api_url=dict(
                                                    type='str',
                                                    required=False),
                                                url_proxy=dict(
                                                    type='dict',
                                                    options=dict(
                                                        url=dict(
                                                            type='str',
                                                            required=False),
                                                        sha=dict(
                                                            type='str',
                                                            required=False),
                                                    ),
                                                    required=False),
                                                caption=dict(
                                                    type='str',
                                                    required=False),
                                                caption_i18n=dict(
                                                    type='dict',
                                                    required=False),
                                                type=dict(
                                                    type='str',
                                                    required=False),
                                                thumbnail_url=dict(
                                                    type='str',
                                                    required=False),
                                            ),
                                            required=False),
                                        description=dict(
                                            type='str',
                                            required=False),
                                        description_i18n=dict(
                                            type='dict',
                                            required=False),
                                    ),
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
                                cost_estimate=dict(
                                    type='dict',
                                    options=dict(
                                        version=dict(
                                            type='str',
                                            required=False),
                                        currency=dict(
                                            type='str',
                                            required=False),
                                        projects=dict(
                                            type='list',
                                            elements='dict',
                                            options=dict(
                                                name=dict(
                                                    type='str',
                                                    required=False),
                                                metadata=dict(
                                                    type='dict',
                                                    required=False),
                                                past_breakdown=dict(
                                                    type='dict',
                                                    options=dict(
                                                        total_hourly_cost=dict(
                                                            type='str',
                                                            required=False),
                                                        total_monthly_cost=dict(
                                                            type='str',
                                                            required=False),
                                                        resources=dict(
                                                            type='list',
                                                            elements='dict',
                                                            options=dict(
                                                                name=dict(
                                                                    type='str',
                                                                    required=False),
                                                                metadata=dict(
                                                                    type='dict',
                                                                    required=False),
                                                                hourly_cost=dict(
                                                                    type='str',
                                                                    required=False),
                                                                monthly_cost=dict(
                                                                    type='str',
                                                                    required=False),
                                                                cost_components=dict(
                                                                    type='list',
                                                                    elements='dict',
                                                                    options=dict(
                                                                        name=dict(
                                                                            type='str',
                                                                            required=False),
                                                                        unit=dict(
                                                                            type='str',
                                                                            required=False),
                                                                        hourly_quantity=dict(
                                                                            type='str',
                                                                            required=False),
                                                                        monthly_quantity=dict(
                                                                            type='str',
                                                                            required=False),
                                                                        price=dict(
                                                                            type='str',
                                                                            required=False),
                                                                        hourly_cost=dict(
                                                                            type='str',
                                                                            required=False),
                                                                        monthly_cost=dict(
                                                                            type='str',
                                                                            required=False),
                                                                    ),
                                                                    required=False),
                                                            ),
                                                            required=False),
                                                    ),
                                                    required=False),
                                                breakdown=dict(
                                                    type='dict',
                                                    options=dict(
                                                        total_hourly_cost=dict(
                                                            type='str',
                                                            required=False),
                                                        total_monthly_cost=dict(
                                                            type='str',
                                                            required=False),
                                                        resources=dict(
                                                            type='list',
                                                            elements='dict',
                                                            options=dict(
                                                                name=dict(
                                                                    type='str',
                                                                    required=False),
                                                                metadata=dict(
                                                                    type='dict',
                                                                    required=False),
                                                                hourly_cost=dict(
                                                                    type='str',
                                                                    required=False),
                                                                monthly_cost=dict(
                                                                    type='str',
                                                                    required=False),
                                                                cost_components=dict(
                                                                    type='list',
                                                                    elements='dict',
                                                                    options=dict(
                                                                        name=dict(
                                                                            type='str',
                                                                            required=False),
                                                                        unit=dict(
                                                                            type='str',
                                                                            required=False),
                                                                        hourly_quantity=dict(
                                                                            type='str',
                                                                            required=False),
                                                                        monthly_quantity=dict(
                                                                            type='str',
                                                                            required=False),
                                                                        price=dict(
                                                                            type='str',
                                                                            required=False),
                                                                        hourly_cost=dict(
                                                                            type='str',
                                                                            required=False),
                                                                        monthly_cost=dict(
                                                                            type='str',
                                                                            required=False),
                                                                    ),
                                                                    required=False),
                                                            ),
                                                            required=False),
                                                    ),
                                                    required=False),
                                                diff=dict(
                                                    type='dict',
                                                    options=dict(
                                                        total_hourly_cost=dict(
                                                            type='str',
                                                            required=False),
                                                        total_monthly_cost=dict(
                                                            type='str',
                                                            required=False),
                                                        resources=dict(
                                                            type='list',
                                                            elements='dict',
                                                            options=dict(
                                                                name=dict(
                                                                    type='str',
                                                                    required=False),
                                                                metadata=dict(
                                                                    type='dict',
                                                                    required=False),
                                                                hourly_cost=dict(
                                                                    type='str',
                                                                    required=False),
                                                                monthly_cost=dict(
                                                                    type='str',
                                                                    required=False),
                                                                cost_components=dict(
                                                                    type='list',
                                                                    elements='dict',
                                                                    options=dict(
                                                                        name=dict(
                                                                            type='str',
                                                                            required=False),
                                                                        unit=dict(
                                                                            type='str',
                                                                            required=False),
                                                                        hourly_quantity=dict(
                                                                            type='str',
                                                                            required=False),
                                                                        monthly_quantity=dict(
                                                                            type='str',
                                                                            required=False),
                                                                        price=dict(
                                                                            type='str',
                                                                            required=False),
                                                                        hourly_cost=dict(
                                                                            type='str',
                                                                            required=False),
                                                                        monthly_cost=dict(
                                                                            type='str',
                                                                            required=False),
                                                                    ),
                                                                    required=False),
                                                            ),
                                                            required=False),
                                                    ),
                                                    required=False),
                                                summary=dict(
                                                    type='dict',
                                                    options=dict(
                                                        total_detected_resources=dict(
                                                            type='int',
                                                            required=False),
                                                        total_supported_resources=dict(
                                                            type='int',
                                                            required=False),
                                                        total_unsupported_resources=dict(
                                                            type='int',
                                                            required=False),
                                                        total_usage_based_resources=dict(
                                                            type='int',
                                                            required=False),
                                                        total_no_price_resources=dict(
                                                            type='int',
                                                            required=False),
                                                        unsupported_resource_counts=dict(
                                                            type='dict',
                                                            required=False),
                                                        no_price_resource_counts=dict(
                                                            type='dict',
                                                            required=False),
                                                    ),
                                                    required=False),
                                            ),
                                            required=False),
                                        summary=dict(
                                            type='dict',
                                            options=dict(
                                                total_detected_resources=dict(
                                                    type='int',
                                                    required=False),
                                                total_supported_resources=dict(
                                                    type='int',
                                                    required=False),
                                                total_unsupported_resources=dict(
                                                    type='int',
                                                    required=False),
                                                total_usage_based_resources=dict(
                                                    type='int',
                                                    required=False),
                                                total_no_price_resources=dict(
                                                    type='int',
                                                    required=False),
                                                unsupported_resource_counts=dict(
                                                    type='dict',
                                                    required=False),
                                                no_price_resource_counts=dict(
                                                    type='dict',
                                                    required=False),
                                            ),
                                            required=False),
                                        total_hourly_cost=dict(
                                            type='str',
                                            required=False),
                                        total_monthly_cost=dict(
                                            type='str',
                                            required=False),
                                        past_total_hourly_cost=dict(
                                            type='str',
                                            required=False),
                                        past_total_monthly_cost=dict(
                                            type='str',
                                            required=False),
                                        diff_total_hourly_cost=dict(
                                            type='str',
                                            required=False),
                                        diff_total_monthly_cost=dict(
                                            type='str',
                                            required=False),
                                        time_generated=dict(
                                            type='str',
                                            required=False),
                                    ),
                                    required=False),
                                dependencies=dict(
                                    type='list',
                                    elements='dict',
                                    options=dict(
                                        catalog_id=dict(
                                            type='str',
                                            required=False),
                                        id=dict(
                                            type='str',
                                            required=False),
                                        name=dict(
                                            type='str',
                                            required=False),
                                        kind=dict(
                                            type='str',
                                            required=False),
                                        version=dict(
                                            type='str',
                                            required=False),
                                        flavors=dict(
                                            type='list',
                                            elements='str',
                                            required=False),
                                    ),
                                    required=False),
                            ),
                            required=False),
                        is_consumable=dict(
                            type='bool',
                            required=False),
                        compliance=dict(
                            type='list',
                            elements='dict',
                            options=dict(
                                scc_profile=dict(
                                    type='dict',
                                    options=dict(
                                        type=dict(
                                            type='str',
                                            required=False),
                                    ),
                                    required=False),
                                family=dict(
                                    type='dict',
                                    options=dict(
                                        id=dict(
                                            type='str',
                                            required=False),
                                        external_id=dict(
                                            type='str',
                                            required=False),
                                        description=dict(
                                            type='str',
                                            required=False),
                                        ui_href=dict(
                                            type='str',
                                            required=False),
                                    ),
                                    required=False),
                                goals=dict(
                                    type='list',
                                    elements='dict',
                                    options=dict(
                                        id=dict(
                                            type='str',
                                            required=False),
                                        description=dict(
                                            type='str',
                                            required=False),
                                        ui_href=dict(
                                            type='str',
                                            required=False),
                                    ),
                                    required=False),
                                validation=dict(
                                    type='dict',
                                    options=dict(
                                        certified=dict(
                                            type='bool',
                                            required=False),
                                        results=dict(
                                            type='dict',
                                            required=False),
                                    ),
                                    required=False),
                            ),
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
                            elements='str',
                            required=False),
                        additional_features=dict(
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
                                    elements='str',
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
                api_url=dict(
                    type='str',
                    required=False),
                url_proxy=dict(
                    type='dict',
                    options=dict(
                        url=dict(
                            type='str',
                            required=False),
                        sha=dict(
                            type='str',
                            required=False),
                    ),
                    required=False),
                caption=dict(
                    type='str',
                    required=False),
                caption_i18n=dict(
                    type='dict',
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
        product_kind=dict(
            type='str',
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
        label_i18n=dict(
            type='dict',
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
            elements='str',
            required=False),
        catalog_id=dict(
            type='str',
            required=False),
        badges=dict(
            type='list',
            elements='dict',
            options=dict(
                id=dict(
                    type='str',
                    required=False),
                label=dict(
                    type='str',
                    required=False),
                label_i18n=dict(
                    type='dict',
                    required=False),
                description=dict(
                    type='str',
                    required=False),
                description_i18n=dict(
                    type='dict',
                    required=False),
                icon=dict(
                    type='str',
                    required=False),
                authority=dict(
                    type='str',
                    required=False),
                tag=dict(
                    type='str',
                    required=False),
                learn_more_links=dict(
                    type='dict',
                    options=dict(
                        first_party=dict(
                            type='str',
                            required=False),
                        third_party=dict(
                            type='str',
                            required=False),
                    ),
                    required=False),
                constraints=dict(
                    type='list',
                    elements='dict',
                    options=dict(
                        type=dict(
                            type='str',
                            required=False),
                        rule=dict(
                            type='raw',
                            required=False),
                    ),
                    required=False),
            ),
            required=False),
        image_pull_keys=dict(
            type='list',
            elements='dict',
            options=dict(
                name=dict(
                    type='str',
                    required=False),
                value=dict(
                    type='str',
                    required=False),
                description=dict(
                    type='str',
                    required=False),
            ),
            no_log=True,
            required=False),
        # Represents the DeprecatePending Python class
        deprecate_pending=dict(
            type='dict',
            options=dict(
                deprecate_date=dict(
                    type='str',
                    required=False),
                deprecate_state=dict(
                    type='str',
                    required=False),
                description=dict(
                    type='str',
                    required=False),
            ),
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
                    no_log=True,
                    required=False),
                type=dict(
                    type='str',
                    required=False),
            ),
            required=False),
        updated=dict(
            type='str',
            required=False),
        long_description_i18n=dict(
            type='dict',
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
                process_i18n=dict(
                    type='dict',
                    required=False),
                locations=dict(
                    type='list',
                    elements='str',
                    required=False),
                support_details=dict(
                    type='list',
                    elements='dict',
                    options=dict(
                        type=dict(
                            type='str',
                            required=False),
                        contact=dict(
                            type='str',
                            required=False),
                        response_wait_time=dict(
                            type='dict',
                            options=dict(
                                value=dict(
                                    type='int',
                                    required=False),
                                type=dict(
                                    type='str',
                                    required=False),
                            ),
                            required=False),
                        availability=dict(
                            type='dict',
                            options=dict(
                                times=dict(
                                    type='list',
                                    elements='dict',
                                    options=dict(
                                        day=dict(
                                            type='int',
                                            required=False),
                                        start_time=dict(
                                            type='str',
                                            required=False),
                                        end_time=dict(
                                            type='str',
                                            required=False),
                                    ),
                                    required=False),
                                timezone=dict(
                                    type='str',
                                    required=False),
                                always_available=dict(
                                    type='bool',
                                    required=False),
                            ),
                            required=False),
                    ),
                    required=False),
                support_escalation=dict(
                    type='dict',
                    options=dict(
                        escalation_wait_time=dict(
                            type='dict',
                            options=dict(
                                value=dict(
                                    type='int',
                                    required=False),
                                type=dict(
                                    type='str',
                                    required=False),
                            ),
                            required=False),
                        response_wait_time=dict(
                            type='dict',
                            options=dict(
                                value=dict(
                                    type='int',
                                    required=False),
                                type=dict(
                                    type='str',
                                    required=False),
                            ),
                            required=False),
                        contact=dict(
                            type='str',
                            required=False),
                    ),
                    required=False),
                support_type=dict(
                    type='str',
                    required=False),
            ),
            required=False),
        short_description_i18n=dict(
            type='dict',
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
            elements='dict',
            options=dict(
                op=dict(
                    type='str',
                    choices=[
                        'add',
                        'remove',
                        'replace',
                        'move',
                        'copy',
                        'test',
                    ],
                    required=False),
                path=dict(
                    type='str',
                    required=False),
                value=dict(
                    type='raw',
                    required=False),
                from_=dict(
                    type='str',
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

    if MISSING_IMPORT_EXC is not None:
        module.fail_json(msg='Missing required import: ' + MISSING_IMPORT_EXC.msg)

    short_description = module.params["short_description"]
    offering_support_url = module.params["offering_support_url"]
    metadata = module.params["metadata"]
    keywords = module.params["keywords"]
    hidden = module.params["hidden"]
    public_publish_approved = module.params["public_publish_approved"]
    portal_ui_url = module.params["portal_ui_url"]
    rating = module.params["rating"]
    kinds = module.params["kinds"]
    media = module.params["media"]
    share_with_ibm = module.params["share_with_ibm"]
    product_kind = module.params["product_kind"]
    features = module.params["features"]
    ibm_publish_approved = module.params["ibm_publish_approved"]
    provider = module.params["provider"]
    portal_approval_record = module.params["portal_approval_record"]
    public_original_crn = module.params["public_original_crn"]
    share_with_all = module.params["share_with_all"]
    offering_docs_url = module.params["offering_docs_url"]
    crn = module.params["crn"]
    disclaimer = module.params["disclaimer"]
    label_i18n = module.params["label_i18n"]
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
    badges = module.params["badges"]
    image_pull_keys = module.params["image_pull_keys"]
    deprecate_pending = module.params["deprecate_pending"]
    permit_request_ibm_public_publish = module.params["permit_request_ibm_public_publish"]
    name = module.params["name"]
    publish_public_crn = module.params["publish_public_crn"]
    repo_info = module.params["repo_info"]
    updated = module.params["updated"]
    long_description_i18n = module.params["long_description_i18n"]
    support = module.params["support"]
    short_description_i18n = module.params["short_description_i18n"]
    provider_info = module.params["provider_info"]
    if_match = module.params["if_match"]
    digest = module.params["digest"]
    catalog_identifier = module.params["catalog_identifier"]
    type = module.params["type"]
    updates = module.params["updates"]
    offering_id = module.params["offering_id"]
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
                module.exit_json(changed=True, id=offering_id, status="deleted")
        else:
            module.exit_json(changed=False, id=offering_id, status="not_found")

    if state == "present":
        if not resource_exists:
            # Create path
            try:
                response = sdk.create_offering(
                    catalog_identifier=catalog_identifier,
                    url=url,
                    crn=crn,
                    label=label,
                    label_i18n=label_i18n,
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
                    short_description_i18n=short_description_i18n,
                    long_description=long_description,
                    long_description_i18n=long_description_i18n,
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
                    image_pull_keys=image_pull_keys,
                    support=support,
                    media=media,
                    deprecate_pending=deprecate_pending,
                    product_kind=product_kind,
                    badges=badges,
                )
            except ApiException as ex:
                module.fail_json(msg=ex.message)
            else:
                result = response.get_result()

                module.exit_json(changed=True, **result)
        else:
            # Update path
            try:
                response = sdk.update_offering(
                    catalog_identifier=catalog_identifier,
                    offering_id=offering_id,
                    if_match=if_match,
                    updates=updates,
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
