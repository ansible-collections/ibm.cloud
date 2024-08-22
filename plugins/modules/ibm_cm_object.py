#!/usr/bin/python
# coding: utf-8

# (C) Copyright IBM Corp. 2024.
#
# GNU General Public License v3.0+ (see LICENSE or https://www.gnu.org/licenses/gpl-3.0.txt)

from __future__ import (absolute_import, division, print_function)
__metaclass__ = type


DOCUMENTATION = r'''
---
module: ibm_cm_object
short_description: Manage C(cm_objects) for Catalog Management API.
author: Gannayak Pabra (@Gannayak0722)
version_added: "1.0.0"
description:
  - This module creates, updates, or deletes a C(cm_object) resource for Catalog Management API.
requirements:
  - "CatalogManagementV1"
options:
  label_i18n:
    description: "A map of translated strings, by language code."
    type: dict
  short_description:
    description: "Short description in the requested language."
    type: str
  catalog_name:
    description: "The name of the catalog."
    type: str
  data:
    description: "Map of data values for this object."
    type: dict
  created:
    description: "The date and time this catalog was created."
    type: str
  kind:
    description: "Kind of object."
    type: str
  rev:
    description: "Cloudant revision."
    type: str
  label:
    description: "Display name in the requested language."
    type: str
  url:
    description: "The url for this specific object."
    type: str
  tags:
    description: "List of tags associated with this catalog."
    type: list
    elements: str
  catalog_id:
    description: "The id of the catalog containing this offering."
    type: str
  parent_id:
    description: "The parent for this specific object."
    type: str
  publish:
    description: "Publish information."
    type: dict
    suboptions:
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
  name:
    description: "The programmatic name of this object."
    type: str
  cm_object_state:
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
  id:
    description: "unique id."
    type: str
  updated:
    description: "The date and time this catalog was last updated."
    type: str
  crn:
    description: "The crn for this specific object."
    type: str
  short_description_i18n:
    description: "A map of translated strings, by language code."
    type: dict
  object_identifier:
    description: "Object identifier."
    type: str
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
- name: Create ibm_cm_object
  vars:
    publish_object_model:
      pc_managed: True
      approval_type: 'testString'
      publish_approved: True
      share_with_all: True
      share_with_ibm: True
      share_enabled: True
      original_crn: 'testString'
      public_crn: 'testString'
      approval_record: {'anyKey': 'anyValue'}
      permit_ibm_public_publish: True
      ibm_approved: True
      public_approved: True
    state_model:
      current: 'testString'
      current_entered: '2019-01-01T12:00:00.000Z'
      pending: 'testString'
      pending_requested: '2019-01-01T12:00:00.000Z'
      previous: 'testString'
  ibm_cm_object:
    catalog_identifier: 'testString'
    name: 'testString'
    crn: 'testString'
    url: 'testString'
    parent_id: 'testString'
    label_i18n: {'key1': 'testString'}
    label: 'testString'
    tags: ['testString']
    created: '2019-01-01T12:00:00.000Z'
    updated: '2019-01-01T12:00:00.000Z'
    short_description: 'testString'
    short_description_i18n: {'key1': 'testString'}
    kind: 'testString'
    publish: '{{ publish_object_model }}'
    cm_object_state: '{{ state_model }}'
    catalog_id: catalog_id_link
    catalog_name: 'testString'
    data: {'anyKey': 'anyValue'}
    state: present

- name: Update ibm_cm_object
  vars:
    publish_object_model:
      pc_managed: True
      approval_type: 'testString'
      publish_approved: True
      share_with_all: True
      share_with_ibm: True
      share_enabled: True
      original_crn: 'testString'
      public_crn: 'testString'
      approval_record: {'anyKey': 'anyValue'}
      permit_ibm_public_publish: True
      ibm_approved: True
      public_approved: True
    state_model:
      current: 'testString'
      current_entered: '2019-01-01T12:00:00.000Z'
      pending: 'testString'
      pending_requested: '2019-01-01T12:00:00.000Z'
      previous: 'testString'
  ibm_cm_object:
    catalog_identifier: 'testString'
    object_identifier: 'testString'
    id: 'testString'
    rev: 'testString'
    name: 'testString'
    crn: 'testString'
    url: 'testString'
    parent_id: 'testString'
    label_i18n: {'key1': 'testString'}
    label: 'testString'
    tags: ['testString']
    created: '2019-01-01T12:00:00.000Z'
    updated: '2019-01-01T12:00:00.000Z'
    short_description: 'testString'
    short_description_i18n: {'key1': 'testString'}
    kind: 'testString'
    publish: '{{ publish_object_model }}'
    cm_object_state: '{{ state_model }}'
    catalog_id: catalog_id_link
    catalog_name: 'testString'
    data: {'anyKey': 'anyValue'}
    state: present

- name: Delete ibm_cm_object
  ibm_cm_object:
    catalog_identifier: 'testString'
    object_identifier: 'testString'
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
name:
  description: "The programmatic name of this object."
  type: str
  returned: on success for create, update operations
crn:
  description: "The crn for this specific object."
  type: str
  returned: on success for create, update operations
url:
  description: "The url for this specific object."
  type: str
  returned: on success for create, update operations
parent_id:
  description: "The parent for this specific object."
  type: str
  returned: on success for create, update operations
label_i18n:
  description: "A map of translated strings, by language code."
  type: dict
  returned: on success for create, update operations
label:
  description: "Display name in the requested language."
  type: str
  returned: on success for create, update operations
tags:
  description: "List of tags associated with this catalog."
  type: list
  elements: str
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
kind:
  description: "Kind of object."
  type: str
  returned: on success for create, update operations
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
  returned: on success for create, update operations
cm_object_state:
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
  returned: on success for create, update operations
catalog_id:
  description: "The id of the catalog containing this offering."
  type: str
  returned: on success for create, update operations
catalog_name:
  description: "The name of the catalog."
  type: str
  returned: on success for create, update operations
data:
  description: "Map of data values for this object."
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
        catalog_name=dict(
            type='str',
            required=False),
        data=dict(
            type='dict',
            required=False),
        created=dict(
            type='str',
            required=False),
        kind=dict(
            type='str',
            required=False),
        rev=dict(
            type='str',
            required=False),
        label=dict(
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
        parent_id=dict(
            type='str',
            required=False),
        # Represents the PublishObject Python class
        publish=dict(
            type='dict',
            options=dict(
                pc_managed=dict(
                    type='bool',
                    required=False),
                approval_type=dict(
                    type='str',
                    required=False),
                publish_approved=dict(
                    type='bool',
                    required=False),
                share_with_all=dict(
                    type='bool',
                    required=False),
                share_with_ibm=dict(
                    type='bool',
                    required=False),
                share_enabled=dict(
                    type='bool',
                    required=False),
                original_crn=dict(
                    type='str',
                    required=False),
                public_crn=dict(
                    type='str',
                    required=False),
                approval_record=dict(
                    type='dict',
                    required=False),
                permit_ibm_public_publish=dict(
                    type='bool',
                    required=False),
                ibm_approved=dict(
                    type='bool',
                    required=False),
                public_approved=dict(
                    type='bool',
                    required=False),
            ),
            required=False),
        name=dict(
            type='str',
            required=False),
        # Represents the State Python class
        cm_object_state=dict(
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
        id=dict(
            type='str',
            required=False),
        updated=dict(
            type='str',
            required=False),
        crn=dict(
            type='str',
            required=False),
        short_description_i18n=dict(
            type='dict',
            required=False),
        object_identifier=dict(
            type='str',
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
    catalog_name = module.params["catalog_name"]
    data = module.params["data"]
    created = module.params["created"]
    kind = module.params["kind"]
    rev = module.params["rev"]
    label = module.params["label"]
    url = module.params["url"]
    tags = module.params["tags"]
    catalog_id = module.params["catalog_id"]
    parent_id = module.params["parent_id"]
    publish = module.params["publish"]
    name = module.params["name"]
    cm_object_state = module.params["cm_object_state"]
    id = module.params["id"]
    updated = module.params["updated"]
    crn = module.params["crn"]
    short_description_i18n = module.params["short_description_i18n"]
    object_identifier = module.params["object_identifier"]
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
    if object_identifier:
        try:
            sdk.get_object(
                catalog_identifier=catalog_identifier,
                object_identifier=object_identifier,
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
                sdk.delete_object(
                    catalog_identifier=catalog_identifier,
                    object_identifier=object_identifier,
                )
            except ApiException as ex:
                module.fail_json(msg=ex.message)
            else:
                module.exit_json(changed=True, id=object_identifier, status="deleted")
        else:
            module.exit_json(changed=False, id=object_identifier, status="not_found")

    if state == "present":
        if not resource_exists:
            # Create path
            try:
                response = sdk.create_object(
                    catalog_identifier=catalog_identifier,
                    name=name,
                    crn=crn,
                    url=url,
                    parent_id=parent_id,
                    label_i18n=label_i18n,
                    label=label,
                    tags=tags,
                    created=created,
                    updated=updated,
                    short_description=short_description,
                    short_description_i18n=short_description_i18n,
                    kind=kind,
                    publish=publish,
                    state=cm_object_state,
                    catalog_id=catalog_id,
                    catalog_name=catalog_name,
                    data=data,
                )
            except ApiException as ex:
                module.fail_json(msg=ex.message)
            else:
                result = response.get_result()
                if 'state' in result:
                    result['cm_object_state'] = result['state']
                    del result['state']

                module.exit_json(changed=True, **result)
        else:
            # Update path
            try:
                response = sdk.replace_object(
                    catalog_identifier=catalog_identifier,
                    object_identifier=object_identifier,
                    id=id,
                    rev=rev,
                    name=name,
                    crn=crn,
                    url=url,
                    parent_id=parent_id,
                    label_i18n=label_i18n,
                    label=label,
                    tags=tags,
                    created=created,
                    updated=updated,
                    short_description=short_description,
                    short_description_i18n=short_description_i18n,
                    kind=kind,
                    publish=publish,
                    state=cm_object_state,
                    catalog_id=catalog_id,
                    catalog_name=catalog_name,
                    data=data,
                )
            except ApiException as ex:
                module.fail_json(msg=ex.message)
            else:
                result = response.get_result()
                if 'state' in result:
                    result['cm_object_state'] = result['state']
                    del result['state']

                module.exit_json(changed=True, **result)


def main():
    run_module()


if __name__ == '__main__':
    main()
