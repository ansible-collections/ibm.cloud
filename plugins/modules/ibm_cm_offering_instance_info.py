#!/usr/bin/python
# coding: utf-8

# (C) Copyright IBM Corp. 2024.
#
# GNU General Public License v3.0+ (see LICENSE or https://www.gnu.org/licenses/gpl-3.0.txt)

from __future__ import (absolute_import, division, print_function)
__metaclass__ = type


DOCUMENTATION = r'''
---
module: ibm_cm_offering_instance_info
short_description: Manage C(cm_offering_instance) for Catalog Management API.
author: Gannayak Pabra (@Gannayak0722)
version_added: "1.0.0"
description:
  - This module retrieves one or more C(cm_offering_instance) for Catalog Management API.
requirements:
  - "CatalogManagementV1"
options:
  instance_identifier:
    description: "Version Instance identifier."
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
- name: Read ibm_cm_offering_instance
  ibm_cm_offering_instance_info:
    instance_identifier: 'testString'
'''

RETURN = r'''
id:
  description: "provisioned instance ID (part of the CRN)."
  type: str
  returned: on success for read operation
rev:
  description: "Cloudant revision."
  type: str
  returned: on success for read operation
url:
  description: "url reference to this object."
  type: str
  returned: on success for read operation
crn:
  description: "platform CRN for this instance."
  type: str
  returned: on success for read operation
label:
  description: "the label for this instance."
  type: str
  returned: on success for read operation
catalog_id:
  description: "Catalog ID this instance was created from."
  type: str
  returned: on success for read operation
offering_id:
  description: "Offering ID this instance was created from."
  type: str
  returned: on success for read operation
kind_format:
  description: "the format this instance has (helm, operator, ova...)."
  type: str
  returned: on success for read operation
kind_format_label:
  description: "Display value for the format this instance has (helm, operator, ova...)."
  type: str
  returned: on success for read operation
version:
  description: "The version this instance was installed from (semver - not version id)."
  type: str
  returned: on success for read operation
version_id:
  description: "The version id this instance was installed from (version id - not semver)."
  type: str
  returned: on success for read operation
cluster_id:
  description: "Cluster ID."
  type: str
  returned: on success for read operation
cluster_region:
  description: "Cluster region (e.g., us-south)."
  type: str
  returned: on success for read operation
cluster_namespaces:
  description: "List of target namespaces to install into."
  type: list
  elements: str
  returned: on success for read operation
cluster_all_namespaces:
  description: "designate to install into all namespaces."
  type: bool
  returned: on success for read operation
schematics_workspace_id:
  description: "Id of the schematics workspace, for offering instances provisioned through schematics."
  type: str
  returned: on success for read operation
install_plan:
  description: "Type of install plan (also known as approval strategy) for operator subscriptions. Can
    be either automatic, which automatically upgrades operators to the latest in a
    channel, or manual, which requires approval on the cluster."
  type: str
  returned: on success for read operation
channel:
  description: "Channel to pin the operator subscription to."
  type: str
  returned: on success for read operation
created:
  description: "date and time create."
  type: str
  returned: on success for read operation
updated:
  description: "date and time updated."
  type: str
  returned: on success for read operation
metadata:
  description: "Map of metadata values for this offering instance."
  type: dict
  returned: on success for read operation
resource_group_id:
  description: "Id of the resource group to provision the offering instance into."
  type: str
  returned: on success for read operation
location:
  description: "String location of OfferingInstance deployment."
  type: str
  returned: on success for read operation
disabled:
  description: "Indicates if Resource Controller has disabled this instance."
  type: bool
  returned: on success for read operation
account:
  description: "The account this instance is owned by."
  type: str
  returned: on success for read operation
last_operation:
  description: "the last operation performed and status."
  type: dict
  contains:
    operation:
      description: "last operation performed."
      type: str
    state:
      description: "state after the last operation performed."
      type: str
    message_:
      description: "additional information about the last operation."
      type: str
    transaction_id:
      description: "transaction id from the last operation."
      type: str
    updated:
      description: "Date and time last updated."
      type: str
    code:
      description: "Error code from the last operation, if applicable."
      type: str
  returned: on success for read operation
kind_target:
  description: "The target kind for the installed software version."
  type: str
  returned: on success for read operation
kind_target_label:
  description: "Display value for the target kind for the installed software version."
  type: str
  returned: on success for read operation
sha:
  description: "The digest value of the installed software version."
  type: str
  returned: on success for read operation
plan_id:
  description: "The software plan ID used when creating this software instance."
  type: str
  returned: on success for read operation
parent_crn:
  description: "The CRN of the resource that is considered a parent of this software instance."
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
        instance_identifier=dict(
            type='str',
            required=False),
    )

    module = AnsibleModule(
        argument_spec=module_args,
        supports_check_mode=True
    )

    if MISSING_IMPORT_EXC is not None:
        module.fail_json(msg='Missing required import: ' + MISSING_IMPORT_EXC.msg)

    instance_identifier = module.params["instance_identifier"]

    if module.check_mode:
        module.exit_json(msg='The module would run with the following parameters: ' + module.paramss)

    authenticator = get_authenticator(service_name='catalog_management')
    if authenticator is None:
        module.fail_json(msg='Cannot create the authenticator.')

    sdk = CatalogManagementV1(
        authenticator=authenticator,
    )

    sdk.configure_service('catalog_management')

    if instance_identifier:
        # read
        try:
            response = sdk.get_offering_instance(
                instance_identifier=instance_identifier,
            )

            result = response.get_result()

            module.exit_json(**result)
        except ApiException as ex:
            module.fail_json(msg=ex.message)


def main():
    run_module()


if __name__ == '__main__':
    main()
