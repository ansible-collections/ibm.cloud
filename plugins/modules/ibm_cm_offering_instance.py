#!/usr/bin/python
# coding: utf-8

# (C) Copyright IBM Corp. 2023.
#
# GNU General Public License v3.0+ (see LICENSE or https://www.gnu.org/licenses/gpl-3.0.txt)

from __future__ import (absolute_import, division, print_function)
__metaclass__ = type


DOCUMENTATION = r'''
---
module: ibm_cm_offering_instance
short_description: Manage C(cm_offering_instances) for Catalog Management API.
author: IBM SDK Generator (@ibm)
version_added: "1.0.0"
description:
  - This module creates, updates, or deletes a C(cm_offering_instance) resource for Catalog Management API.
requirements:
  - "CatalogManagementV1"
options:
  install_plan:
    description: "Type of install plan (also known as approval strategy) for operator subscriptions.
      Can be either automatic, which automatically upgrades operators to the latest in a
      channel, or manual, which requires approval on the cluster."
    type: str
  metadata:
    description: "Map of metadata values for this offering instance."
    type: dict
  resource_group_id:
    description: "Id of the resource group to provision the offering instance into."
    type: str
  rev:
    description: "Cloudant revision."
    type: str
  channel:
    description: "Channel to pin the operator subscription to."
    type: str
  offering_id:
    description: "Offering ID this instance was created from."
    type: str
  cluster_id:
    description: "Cluster ID."
    type: str
  schematics_workspace_id:
    description: "Id of the schematics workspace, for offering instances provisioned through
      schematics."
    type: str
  disabled:
    description: "Indicates if Resource Controller has disabled this instance."
    type: bool
  id:
    description: "provisioned instance ID (part of the CRN)."
    type: str
  cluster_namespaces:
    description: "List of target namespaces to install into."
    type: list
    elements: str
  cluster_all_namespaces:
    description: "designate to install into all namespaces."
    type: bool
  kind_target:
    description: "The target kind for the installed software version."
    type: str
  crn:
    description: "platform CRN for this instance."
    type: str
  kind_format:
    description: "the format this instance has (helm, operator, ova...)."
    type: str
  cluster_region:
    description: "Cluster region (e.g., us-south)."
    type: str
  created:
    description: "date and time create."
    type: str
  label:
    description: "the label for this instance."
    type: str
  version_id:
    description: "The version id this instance was installed from (version id - not semver)."
    type: str
  version:
    description: "The version this instance was installed from (semver - not version id)."
    type: str
  sha:
    description: "The digest value of the installed software version."
    type: str
  url:
    description: "url reference to this object."
    type: str
  catalog_id:
    description: "Catalog ID this instance was created from."
    type: str
  location:
    description: "String location of OfferingInstance deployment."
    type: str
  updated:
    description: "date and time updated."
    type: str
  account:
    description: "The account this instance is owned by."
    type: str
  last_operation:
    description: "the last operation performed and status."
    type: dict
    suboptions:
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
  instance_identifier:
    description: "Version Instance identifier."
    type: str
  x_auth_refresh_token:
    description: "IAM Refresh token."
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
- name: Create ibm_cm_offering_instance
  vars:
    offering_instance_last_operation_model:
      operation: 'testString'
      state: 'testString'
      message_: 'testString'
      transaction_id: 'testString'
      updated: '2019-01-01T12:00:00.000Z'
      code: 'testString'
  ibm_cm_offering_instance:
    x_auth_refresh_token: 'testString'
    id: 'testString'
    rev: 'testString'
    url: 'testString'
    crn: 'testString'
    label: 'testString'
    catalog_id: 'testString'
    offering_id: 'testString'
    kind_format: 'testString'
    version: 'testString'
    version_id: 'testString'
    cluster_id: 'testString'
    cluster_region: 'testString'
    cluster_namespaces: ['testString']
    cluster_all_namespaces: True
    schematics_workspace_id: 'testString'
    install_plan: 'testString'
    channel: 'testString'
    created: '2019-01-01T12:00:00.000Z'
    updated: '2019-01-01T12:00:00.000Z'
    metadata: {'key1': {'foo': 'bar'}}
    resource_group_id: 'testString'
    location: 'testString'
    disabled: True
    account: 'testString'
    last_operation: '{{ offering_instance_last_operation_model }}'
    kind_target: 'testString'
    sha: 'testString'
    state: present

- name: Update ibm_cm_offering_instance
  vars:
    offering_instance_last_operation_model:
      operation: 'testString'
      state: 'testString'
      message_: 'testString'
      transaction_id: 'testString'
      updated: '2019-01-01T12:00:00.000Z'
      code: 'testString'
  ibm_cm_offering_instance:
    instance_identifier: 'testString'
    x_auth_refresh_token: 'testString'
    id: 'testString'
    rev: 'testString'
    url: 'testString'
    crn: 'testString'
    label: 'testString'
    catalog_id: 'testString'
    offering_id: 'testString'
    kind_format: 'testString'
    version: 'testString'
    version_id: 'testString'
    cluster_id: 'testString'
    cluster_region: 'testString'
    cluster_namespaces: ['testString']
    cluster_all_namespaces: True
    schematics_workspace_id: 'testString'
    install_plan: 'testString'
    channel: 'testString'
    created: '2019-01-01T12:00:00.000Z'
    updated: '2019-01-01T12:00:00.000Z'
    metadata: {'key1': {'foo': 'bar'}}
    resource_group_id: 'testString'
    location: 'testString'
    disabled: True
    account: 'testString'
    last_operation: '{{ offering_instance_last_operation_model }}'
    kind_target: 'testString'
    sha: 'testString'
    state: present

- name: Delete ibm_cm_offering_instance
  ibm_cm_offering_instance:
    instance_identifier: 'testString'
    x_auth_refresh_token: 'testString'
    state: absent
'''

RETURN = r'''
id:
  description: "provisioned instance ID (part of the CRN)."
  type: str
  returned: on success for create, update, delete operations
rev:
  description: "Cloudant revision."
  type: str
  returned: on success for create, update operations
url:
  description: "url reference to this object."
  type: str
  returned: on success for create, update operations
crn:
  description: "platform CRN for this instance."
  type: str
  returned: on success for create, update operations
label:
  description: "the label for this instance."
  type: str
  returned: on success for create, update operations
catalog_id:
  description: "Catalog ID this instance was created from."
  type: str
  returned: on success for create, update operations
offering_id:
  description: "Offering ID this instance was created from."
  type: str
  returned: on success for create, update operations
kind_format:
  description: "the format this instance has (helm, operator, ova...)."
  type: str
  returned: on success for create, update operations
version:
  description: "The version this instance was installed from (semver - not version id)."
  type: str
  returned: on success for create, update operations
version_id:
  description: "The version id this instance was installed from (version id - not semver)."
  type: str
  returned: on success for create, update operations
cluster_id:
  description: "Cluster ID."
  type: str
  returned: on success for create, update operations
cluster_region:
  description: "Cluster region (e.g., us-south)."
  type: str
  returned: on success for create, update operations
cluster_namespaces:
  description: "List of target namespaces to install into."
  type: list
  elements: str
  returned: on success for create, update operations
cluster_all_namespaces:
  description: "designate to install into all namespaces."
  type: bool
  returned: on success for create, update operations
schematics_workspace_id:
  description: "Id of the schematics workspace, for offering instances provisioned through schematics."
  type: str
  returned: on success for create, update operations
install_plan:
  description: "Type of install plan (also known as approval strategy) for operator subscriptions. Can
    be either automatic, which automatically upgrades operators to the latest in a
    channel, or manual, which requires approval on the cluster."
  type: str
  returned: on success for create, update operations
channel:
  description: "Channel to pin the operator subscription to."
  type: str
  returned: on success for create, update operations
created:
  description: "date and time create."
  type: str
  returned: on success for create, update operations
updated:
  description: "date and time updated."
  type: str
  returned: on success for create, update operations
metadata:
  description: "Map of metadata values for this offering instance."
  type: dict
  returned: on success for create, update operations
resource_group_id:
  description: "Id of the resource group to provision the offering instance into."
  type: str
  returned: on success for create, update operations
location:
  description: "String location of OfferingInstance deployment."
  type: str
  returned: on success for create, update operations
disabled:
  description: "Indicates if Resource Controller has disabled this instance."
  type: bool
  returned: on success for create, update operations
account:
  description: "The account this instance is owned by."
  type: str
  returned: on success for create, update operations
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
  returned: on success for create, update operations
kind_target:
  description: "The target kind for the installed software version."
  type: str
  returned: on success for create, update operations
sha:
  description: "The digest value of the installed software version."
  type: str
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
        install_plan=dict(
            type='str',
            required=False),
        metadata=dict(
            type='dict',
            required=False),
        resource_group_id=dict(
            type='str',
            required=False),
        rev=dict(
            type='str',
            required=False),
        channel=dict(
            type='str',
            required=False),
        offering_id=dict(
            type='str',
            required=False),
        cluster_id=dict(
            type='str',
            required=False),
        schematics_workspace_id=dict(
            type='str',
            required=False),
        disabled=dict(
            type='bool',
            required=False),
        id=dict(
            type='str',
            required=False),
        cluster_namespaces=dict(
            type='list',
            elements='str',
            required=False),
        cluster_all_namespaces=dict(
            type='bool',
            required=False),
        kind_target=dict(
            type='str',
            required=False),
        crn=dict(
            type='str',
            required=False),
        kind_format=dict(
            type='str',
            required=False),
        cluster_region=dict(
            type='str',
            required=False),
        created=dict(
            type='str',
            required=False),
        label=dict(
            type='str',
            required=False),
        version_id=dict(
            type='str',
            required=False),
        version=dict(
            type='str',
            required=False),
        sha=dict(
            type='str',
            required=False),
        url=dict(
            type='str',
            required=False),
        catalog_id=dict(
            type='str',
            required=False),
        location=dict(
            type='str',
            required=False),
        updated=dict(
            type='str',
            required=False),
        account=dict(
            type='str',
            required=False),
        # Represents the OfferingInstanceLastOperation Python class
        last_operation=dict(
            type='dict',
            options=dict(
                operation=dict(
                    type='str',
                    required=False),
                state=dict(
                    type='str',
                    required=False),
                message_=dict(
                    type='str',
                    required=False),
                transaction_id=dict(
                    type='str',
                    required=False),
                updated=dict(
                    type='str',
                    required=False),
                code=dict(
                    type='str',
                    required=False),
            ),
            required=False),
        instance_identifier=dict(
            type='str',
            required=False),
        x_auth_refresh_token=dict(
            type='str',
            no_log=True,
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

    install_plan = module.params["install_plan"]
    metadata = module.params["metadata"]
    resource_group_id = module.params["resource_group_id"]
    rev = module.params["rev"]
    channel = module.params["channel"]
    offering_id = module.params["offering_id"]
    cluster_id = module.params["cluster_id"]
    schematics_workspace_id = module.params["schematics_workspace_id"]
    disabled = module.params["disabled"]
    id = module.params["id"]
    cluster_namespaces = module.params["cluster_namespaces"]
    cluster_all_namespaces = module.params["cluster_all_namespaces"]
    kind_target = module.params["kind_target"]
    crn = module.params["crn"]
    kind_format = module.params["kind_format"]
    cluster_region = module.params["cluster_region"]
    created = module.params["created"]
    label = module.params["label"]
    version_id = module.params["version_id"]
    version = module.params["version"]
    sha = module.params["sha"]
    url = module.params["url"]
    catalog_id = module.params["catalog_id"]
    location = module.params["location"]
    updated = module.params["updated"]
    account = module.params["account"]
    last_operation = module.params["last_operation"]
    instance_identifier = module.params["instance_identifier"]
    x_auth_refresh_token = module.params["x_auth_refresh_token"]
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
    if instance_identifier:
        try:
            sdk.get_offering_instance(
                instance_identifier=instance_identifier,
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
                sdk.delete_offering_instance(
                    instance_identifier=instance_identifier,
                    x_auth_refresh_token=x_auth_refresh_token,
                )
            except ApiException as ex:
                module.fail_json(msg=ex.message)
            else:
                module.exit_json(changed=True, id=instance_identifier, status="deleted")
        else:
            module.exit_json(changed=False, id=instance_identifier, status="not_found")

    if state == "present":
        if not resource_exists:
            # Create path
            try:
                response = sdk.create_offering_instance(
                    x_auth_refresh_token=x_auth_refresh_token,
                    id=id,
                    rev=rev,
                    url=url,
                    crn=crn,
                    label=label,
                    catalog_id=catalog_id,
                    offering_id=offering_id,
                    kind_format=kind_format,
                    version=version,
                    version_id=version_id,
                    cluster_id=cluster_id,
                    cluster_region=cluster_region,
                    cluster_namespaces=cluster_namespaces,
                    cluster_all_namespaces=cluster_all_namespaces,
                    schematics_workspace_id=schematics_workspace_id,
                    install_plan=install_plan,
                    channel=channel,
                    created=created,
                    updated=updated,
                    metadata=metadata,
                    resource_group_id=resource_group_id,
                    location=location,
                    disabled=disabled,
                    account=account,
                    last_operation=last_operation,
                    kind_target=kind_target,
                    sha=sha,
                )
            except ApiException as ex:
                module.fail_json(msg=ex.message)
            else:
                result = response.get_result()

                module.exit_json(changed=True, **result)
        else:
            # Update path
            try:
                response = sdk.put_offering_instance(
                    instance_identifier=instance_identifier,
                    x_auth_refresh_token=x_auth_refresh_token,
                    id=id,
                    rev=rev,
                    url=url,
                    crn=crn,
                    label=label,
                    catalog_id=catalog_id,
                    offering_id=offering_id,
                    kind_format=kind_format,
                    version=version,
                    version_id=version_id,
                    cluster_id=cluster_id,
                    cluster_region=cluster_region,
                    cluster_namespaces=cluster_namespaces,
                    cluster_all_namespaces=cluster_all_namespaces,
                    schematics_workspace_id=schematics_workspace_id,
                    install_plan=install_plan,
                    channel=channel,
                    created=created,
                    updated=updated,
                    metadata=metadata,
                    resource_group_id=resource_group_id,
                    location=location,
                    disabled=disabled,
                    account=account,
                    last_operation=last_operation,
                    kind_target=kind_target,
                    sha=sha,
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
