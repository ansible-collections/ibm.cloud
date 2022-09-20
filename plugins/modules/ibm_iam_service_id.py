#!/usr/bin/python
# -*- coding: utf-8 -*-

# (C) Copyright IBM Corp. 2022.
# GNU General Public License v3.0+ (see LICENSE or https://www.gnu.org/licenses/gpl-3.0.txt)

from __future__ import (absolute_import, division, print_function)
__metaclass__ = type


DOCUMENTATION = r'''
---
module: ibm_iam_service_id
short_description: Manage ibm_iam_service_id resources.
author: Kavya Handadi (@kavya498)
version_added: "0.0.1-beta0"
description:
    - This module creates, updates, or deletes a ibm_iam_service_id.
    - By default the module will look for an existing ibm_iam_service_id.
requirements:
    - "IamIdentityV1"
options:
    account_id:
        description:
            - ID of the account the service ID belongs to.
        type: str
    apikey:
        description:
            - Parameters for the API key in the Create service Id V1 REST request.
        type: dict
        suboptions:
            name:
                description: |
                    Name of the API key. The name is not checked for uniqueness.
                    Therefore multiple names with the same value can exist. Access is done via the UUID of the API key.
                type: str
            description:
                description: |
                    The optional description of the API key.
                    The 'description' property is only available if a description was provided during a create of an API key.
                type: str
            apikey:
                description: |
                    You can optionally passthrough the API key value for this API key.
                    If passed, NO validation of that apiKey value is done, i.e. the value can be non-URL safe.
                    If omitted, the API key management will create an URL safe opaque API key value. The value of the API key is checked for uniqueness.
                    Please ensure enough variations when passing in this value.
                type: str
            store_value:
                description: |
                    Send true or false to set whether the API key value is retrievable in the future by using the Get details of an API key request.
                    If you create an API key for a user, you must specify `false` or omit the value. We don't allow storing of API keys for users.
                type: bool
    name:
        description: |
            Name of the Service Id. The name is not checked for uniqueness.
            Therefore multiple names with the same value can exist. Access is done via the UUID of the Service Id.
        type: str
    unique_instance_crns:
        description:
            - Optional list of CRNs (string array) which point to the services connected to the service ID.
        type: list
        elements: str
    description:
        description: |
            The optional description of the Service Id.
            The 'description' property is only available if a description was provided during a create of a Service Id.
        type: str
    include_history:
        description:
            - Defines if the entity history is included in the response.
        type: bool
    if_match:
        description: |
            Version of the service ID to be updated.
            Specify the version that you retrieved as entity_tag (ETag header) when reading the service ID.
            This value helps identifying parallel usage of this API. Pass * to indicate to update any version available. This might result in stale updates.
        type: str
    entity_lock:
        description:
            - Indicates if the service ID is locked for further write operations. False by default.
        type: str
    id:
        description:
            - Unique ID of the service ID.
        type: str
    include_activity:
        description: |
            Defines if the entity's activity is included in the response.
            Retrieving activity data is an expensive operation, so please only request this when needed.
        type: bool
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
from ibm_platform_services import IamIdentityV1
from ibm_cloud_sdk_core import ApiException
from ansible.module_utils.basic import AnsibleModule


def run_module():
    module_args = dict(
        account_id=dict(
            type='str',
            required=False),
        # Represents the ApiKeyInsideCreateServiceIdRequest Python class
        apikey=dict(
            type='dict',
            options=dict(
                name=dict(
                    type='str',
                    required=False),
                description=dict(
                    type='str',
                    required=False),
                apikey=dict(
                    type='str',
                    required=False),
                store_value=dict(
                    type='bool',
                    required=False),
            ),
            required=False),
        name=dict(
            type='str',
            required=False),
        unique_instance_crns=dict(
            type='list',
            elements=str,
            required=False),
        description=dict(
            type='str',
            required=False),
        include_history=dict(
            type='bool',
            required=False),
        if_match=dict(
            type='str',
            required=False),
        entity_lock=dict(
            type='str',
            required=False),
        id=dict(
            type='str',
            required=False),
        include_activity=dict(
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

    account_id = module.params["account_id"]
    apikey = module.params["apikey"]
    name = module.params["name"]
    unique_instance_crns = module.params["unique_instance_crns"]
    description = module.params["description"]
    # include_history = module.params["include_history"]
    if_match = module.params["if_match"]
    entity_lock = module.params["entity_lock"]
    id = module.params["id"]
    # include_activity = module.params["include_activity"]
    state = module.params["state"]

    sdk = config.get_iam_identity_sdk()
    resource_exists = True

    # Check for existence
    if id:
        try:
            sdk.get_service_id(
                id=id,
                # include_history=include_history,
                # include_activity=include_activity,
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
                sdk.delete_service_id(
                    id=id,
                )
            except ApiException as ex:
                module.fail_json(msg=ex.message)
            else:
                payload = {"id": id, "status": "deleted"}
                module.exit_json(changed=True, msg=payload)
        else:
            payload = {"id": id, "status": "not_found"}
            module.exit_json(changed=False, msg=payload)

    if state == "present":
        if not resource_exists:
            # Create path
            try:
                result = sdk.create_service_id(
                    account_id=account_id,
                    name=name,
                    description=description,
                    unique_instance_crns=unique_instance_crns,
                    apikey=apikey,
                    entity_lock=entity_lock,
                ).get_result()
            except ApiException as ex:
                module.fail_json(msg=ex.message)
            else:
                module.exit_json(changed=True, msg=result)
        else:
            # Update path
            try:
                result = sdk.update_service_id(
                    id=id,
                    if_match=if_match,
                    name=name,
                    description=description,
                    unique_instance_crns=unique_instance_crns,
                ).get_result()
            except ApiException as ex:
                module.fail_json(msg=ex.message)
            else:
                module.exit_json(changed=True, msg=result)


def main():
    run_module()


if __name__ == '__main__':
    main()
