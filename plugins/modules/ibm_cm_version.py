#!/usr/bin/python
# coding: utf-8

# (C) Copyright IBM Corp. 2023.
#
# GNU General Public License v3.0+ (see LICENSE or https://www.gnu.org/licenses/gpl-3.0.txt)

from __future__ import (absolute_import, division, print_function)
__metaclass__ = type


DOCUMENTATION = r'''
---
module: ibm_cm_version
short_description: Manage C(cm_versions) for Catalog Management API.
author: IBM SDK Generator (@ibm)
version_added: "1.0.0"
description:
  - This module creates, updates, or deletes a C(cm_version) resource for Catalog Management API.
requirements:
  - "CatalogManagementV1"
options:
  metadata:
    description: "Generic data to be included with content being onboarded. Required for virtual
      server image for VPC."
    type: dict
    suboptions:
      operating_system:
        description: "Operating system included in this image. Required for virtual server image for VPC."
        type: dict
        suboptions:
          dedicated_host_only:
            description: "Images with this operating system can only be used on dedicated hosts or dedicated
              host groups. Required for virtual server image for VPC."
            type: bool
          vendor:
            description: "Vendor of the operating system. Required for virtual server image for VPC."
            type: str
          name:
            description: "Globally unique name for this operating system Required for virtual server image for
              VPC."
            type: str
          href:
            description: "URL for this operating system. Required for virtual server image for VPC."
            type: str
          display_name:
            description: "Unique, display-friendly name for the operating system. Required for virtual server
              image for VPC."
            type: str
          family:
            description: "Software family for this operating system. Required for virtual server image for VPC."
            type: str
          version:
            description: "Major release version of this operating system. Required for virtual server image for
              VPC."
            type: str
          architecture:
            description: "Operating system architecture. Required for virtual server image for VPC."
            type: str
      file:
        description: "Details for the stored image file. Required for virtual server image for VPC."
        type: dict
        suboptions:
          size:
            description: "Size of the stored image file rounded up to the next gigabyte. Required for virtual
              server image for VPC."
            type: int
      minimum_provisioned_size:
        description: "Minimum size (in gigabytes) of a volume onto which this image may be provisioned.
          Required for virtual server image for VPC."
        type: int
      images:
        description: "Image operating system. Required for virtual server image for VPC."
        type: list
        elements: 'dict'
        suboptions:
          id:
            description: "Programmatic ID of virtual server image. Required for virtual server image for VPC."
            type: str
          name:
            description: "Programmatic name of virtual server image. Required for virtual server image for VPC."
            type: str
          region:
            description: "Region the virtual server image is available in. Required for virtual server image for
              VPC."
            type: str
  working_directory:
    description: "Optional - The sub-folder within the specified tgz file that contains the software
      being onboarded."
    type: str
  label:
    description: "Display name of version. Required for virtual server image for VPC."
    type: str
  sha:
    description: "SHA256 fingerprint of the image file. Required for virtual server image for VPC."
    type: str
  version:
    description: "Semantic version of the software being onboarded. Required for virtual server image
      for VPC."
    type: str
  content:
    description: "Byte array representing the content to be imported. Only supported for OVA images at
      this time."
    type: str
  tags:
    description: "Tags array."
    type: list
    elements: str
  target_kinds:
    description: "Deployment target of the content being onboarded. Current valid values are iks,
      roks, vcenter, power-iaas, terraform, and vpc-x86. Required for virtual server image
      for VPC."
    type: list
    elements: str
  format_kind:
    description: "Format of content being onboarded. Example: vsi-image. Required for virtual server
      image for VPC."
    type: str
  product_kind:
    description: "Optional product kind for the software being onboarded.  Valid values are software,
      module, or solution.  Default value is software."
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
  install_kind:
    description: "Install type. Example: instance. Required for virtual server image for VPC."
    type: str
  name:
    description: "Name of version. Required for virtual server image for VPC."
    type: str
  repotype:
    description: "The type of repository containing this version.  Valid values are 'publicI(git' or
      'enterprise)git'."
    type: str
  zipurl:
    description: "URL path to zip location.  If not specified, must provide content in the body of
      this call."
    type: str
  version_loc_id:
    description: "A dotted value of C(catalogID).C(versionID)."
    type: str
  x_auth_token:
    description: "Authentication token used to access the specified zip file."
    type: str
  catalog_identifier:
    description: "Catalog identifier."
    type: str
  offering_id:
    description: "Offering identification."
    type: str
  target_version:
    description: "The semver value for this new version, if not found in the zip url package content."
    type: str
  include_config:
    description: "Add all possible configuration values to this version when importing."
    type: bool
  is_vsi:
    description: "Indicates that the current terraform template is used to install a virtual server
      image."
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
- name: Create ibm_cm_version
  vars:
    flavor_model:
      name: 'testString'
      label: 'testString'
      label_i18n: {'key1': 'testString'}
      index: 38
    import_offering_body_metadata_operating_system_model:
      dedicated_host_only: True
      vendor: 'testString'
      name: 'testString'
      href: 'testString'
      display_name: 'testString'
      family: 'testString'
      version: 'testString'
      architecture: 'testString'
    import_offering_body_metadata_file_model:
      size: 38
    import_offering_body_metadata_images_item_model:
      id: 'testString'
      name: 'testString'
      region: 'testString'
    import_offering_body_metadata_model:
      operating_system: import_offering_body_metadata_operating_system_model
      file: import_offering_body_metadata_file_model
      minimum_provisioned_size: 38
      images: [import_offering_body_metadata_images_item_model]
  ibm_cm_version:
    catalog_identifier: 'testString'
    offering_id: 'testString'
    tags: ['testString']
    content: 'VGhpcyBpcyBhIG1vY2sgYnl0ZSBhcnJheSB2YWx1ZS4='
    name: 'testString'
    label: 'testString'
    install_kind: 'testString'
    target_kinds: ['testString']
    format_kind: 'testString'
    product_kind: 'testString'
    sha: 'testString'
    version: 'testString'
    flavor: '{{ flavor_model }}'
    metadata: '{{ import_offering_body_metadata_model }}'
    working_directory: 'testString'
    zipurl: 'testString'
    target_version: 'testString'
    include_config: True
    is_vsi: True
    repotype: 'testString'
    x_auth_token: 'testString'
    state: present

- name: Delete ibm_cm_version
  ibm_cm_version:
    version_loc_id: 'testString'
    state: absent
'''

RETURN = r'''
id:
  description: "Unique ID."
  type: str
  returned: on success for create, delete operations
rev:
  description: "Cloudant revision."
  type: str
  returned: on success for create operation
crn:
  description: "Version's CRN."
  type: str
  returned: on success for create operation
version:
  description: "Version of content type."
  type: str
  returned: on success for create operation
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
  returned: on success for create operation
sha:
  description: "hash of the content."
  type: str
  returned: on success for create operation
created:
  description: "The date and time this version was created."
  type: str
  returned: on success for create operation
updated:
  description: "The date and time this version was last updated."
  type: str
  returned: on success for create operation
offering_id:
  description: "Offering ID."
  type: str
  returned: on success for create operation
catalog_id:
  description: "Catalog ID."
  type: str
  returned: on success for create operation
kind_id:
  description: "Kind ID."
  type: str
  returned: on success for create operation
tags:
  description: "List of tags associated with this catalog."
  type: list
  elements: str
  returned: on success for create operation
repo_url:
  description: "Content's repo URL."
  type: str
  returned: on success for create operation
source_url:
  description: "Content's source URL (e.g git repo)."
  type: str
  returned: on success for create operation
tgz_url:
  description: "File used to on-board this version."
  type: str
  returned: on success for create operation
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
  returned: on success for create operation
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
  returned: on success for create operation
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
  returned: on success for create operation
metadata:
  description: "Open ended metadata information."
  type: dict
  returned: on success for create operation
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
  returned: on success for create operation
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
  returned: on success for create operation
single_instance:
  description: "Denotes if single instance can be deployed to a given cluster."
  type: bool
  returned: on success for create operation
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
  returned: on success for create operation
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
  returned: on success for create operation
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
  returned: on success for create operation
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
  returned: on success for create operation
image_manifest_url:
  description: "If set, denotes a url to a YAML file with list of container images used by this
    version."
  type: str
  returned: on success for create operation
deprecated:
  description: "read only field, indicating if this version is deprecated."
  type: bool
  returned: on success for create operation
package_version:
  description: "Version of the package used to create this version."
  type: str
  returned: on success for create operation
cm_version_state:
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
  returned: on success for create operation
version_locator:
  description: "A dotted value of C(catalogID).C(versionID)."
  type: str
  returned: on success for create operation
long_description:
  description: "Long description for version."
  type: str
  returned: on success for create operation
long_description_i18n:
  description: "A map of translated strings, by language code."
  type: dict
  returned: on success for create operation
whitelisted_accounts:
  description: "Whitelisted accounts for version."
  type: list
  elements: str
  returned: on success for create operation
image_pull_key_name:
  description: "ID of the image pull key to use from Offering.ImagePullKeys."
  type: str
  returned: on success for create operation
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
  returned: on success for create operation
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
  returned: on success for create operation
is_consumable:
  description: "Is the version able to be shared."
  type: bool
  returned: on success for create operation
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


import base64

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
        # Represents the ImportOfferingBodyMetadata Python class
        metadata=dict(
            type='dict',
            options=dict(
                operating_system=dict(
                    type='dict',
                    options=dict(
                        dedicated_host_only=dict(
                            type='bool',
                            required=False),
                        vendor=dict(
                            type='str',
                            required=False),
                        name=dict(
                            type='str',
                            required=False),
                        href=dict(
                            type='str',
                            required=False),
                        display_name=dict(
                            type='str',
                            required=False),
                        family=dict(
                            type='str',
                            required=False),
                        version=dict(
                            type='str',
                            required=False),
                        architecture=dict(
                            type='str',
                            required=False),
                    ),
                    required=False),
                file=dict(
                    type='dict',
                    options=dict(
                        size=dict(
                            type='int',
                            required=False),
                    ),
                    required=False),
                minimum_provisioned_size=dict(
                    type='int',
                    required=False),
                images=dict(
                    type='list',
                    elements='dict',
                    options=dict(
                        id=dict(
                            type='str',
                            required=False),
                        name=dict(
                            type='str',
                            required=False),
                        region=dict(
                            type='str',
                            required=False),
                    ),
                    required=False),
            ),
            required=False),
        working_directory=dict(
            type='str',
            required=False),
        label=dict(
            type='str',
            required=False),
        sha=dict(
            type='str',
            required=False),
        version=dict(
            type='str',
            required=False),
        content=dict(
            type='str',
            required=False),
        tags=dict(
            type='list',
            elements='str',
            required=False),
        target_kinds=dict(
            type='list',
            elements='str',
            required=False),
        format_kind=dict(
            type='str',
            required=False),
        product_kind=dict(
            type='str',
            required=False),
        # Represents the Flavor Python class
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
        install_kind=dict(
            type='str',
            required=False),
        name=dict(
            type='str',
            required=False),
        repotype=dict(
            type='str',
            required=False),
        zipurl=dict(
            type='str',
            required=False),
        version_loc_id=dict(
            type='str',
            required=False),
        x_auth_token=dict(
            type='str',
            no_log=True,
            required=False),
        catalog_identifier=dict(
            type='str',
            required=False),
        offering_id=dict(
            type='str',
            required=False),
        target_version=dict(
            type='str',
            required=False),
        include_config=dict(
            type='bool',
            required=False),
        is_vsi=dict(
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

    metadata = module.params["metadata"]
    working_directory = module.params["working_directory"]
    label = module.params["label"]
    sha = module.params["sha"]
    version = module.params["version"]
    content = module.params["content"]
    try:
        content = base64.b64decode(content) if content is not None else None
    except Exception as ex:
        module.fail_json(msg=f'Error during decoding value for content: {ex}')
    tags = module.params["tags"]
    target_kinds = module.params["target_kinds"]
    format_kind = module.params["format_kind"]
    product_kind = module.params["product_kind"]
    flavor = module.params["flavor"]
    install_kind = module.params["install_kind"]
    name = module.params["name"]
    repotype = module.params["repotype"]
    zipurl = module.params["zipurl"]
    version_loc_id = module.params["version_loc_id"]
    x_auth_token = module.params["x_auth_token"]
    catalog_identifier = module.params["catalog_identifier"]
    offering_id = module.params["offering_id"]
    target_version = module.params["target_version"]
    include_config = module.params["include_config"]
    is_vsi = module.params["is_vsi"]
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
    if version_loc_id:
        try:
            sdk.get_version(
                version_loc_id=version_loc_id,
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
                sdk.delete_version(
                    version_loc_id=version_loc_id,
                )
            except ApiException as ex:
                module.fail_json(msg=ex.message)
            else:
                module.exit_json(changed=True, id=version_loc_id, status="deleted")
        else:
            module.exit_json(changed=False, id=version_loc_id, status="not_found")

    if state == "present":
        if not resource_exists:
            # Create path
            try:
                response = sdk.import_offering_version(
                    catalog_identifier=catalog_identifier,
                    offering_id=offering_id,
                    tags=tags,
                    content=content,
                    name=name,
                    label=label,
                    install_kind=install_kind,
                    target_kinds=target_kinds,
                    format_kind=format_kind,
                    product_kind=product_kind,
                    sha=sha,
                    version=version,
                    flavor=flavor,
                    metadata=metadata,
                    working_directory=working_directory,
                    zipurl=zipurl,
                    target_version=target_version,
                    include_config=include_config,
                    is_vsi=is_vsi,
                    repotype=repotype,
                    x_auth_token=x_auth_token,
                )
            except ApiException as ex:
                module.fail_json(msg=ex.message)
            else:
                result = response.get_result()
                if 'state' in result:
                    result['cm_version_state'] = result['state']
                    del result['state']

                module.exit_json(changed=True, **result)


def main():
    run_module()


if __name__ == '__main__':
    main()
