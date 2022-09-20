#!/usr/bin/python
# -*- coding: utf-8 -*-

# (C) Copyright IBM Corp. 2022.
# GNU General Public License v3.0+ (see LICENSE or https://www.gnu.org/licenses/gpl-3.0.txt)

# pylint: disable=missing-function-docstring

from __future__ import (absolute_import, division, print_function)
__metaclass__ = type


DOCUMENTATION = r'''
---
module: ibm_resource_instances_info
short_description: Manage ibm_resource_instances info.
author:
    - "Kavya Handadi (@kavya498)"
version_added: "0.0.1-beta0"
description:
    - This module retrieves one or more ibm_resource_instances(s).
requirements:
    - "ResourceControllerV2"
options:
    resource_group_id:
        description:
            - The ID of the resource group.
        type: str
    updated_from:
        description:
            - Start date inclusive filter.
        type: str
    plan:
        description:
            - The unique ID of the plan associated with the offering. This value is provided by and stored in the global catalog.
        type: str
    sub_type:
        description:
            - The sub-type of instance, for example, `kms`.
        type: str
    name:
        description:
            - The human-readable name of the instance.
        type: str
    limit:
        description:
            - Limit on how many items should be returned.
        type: int
    start:
        description: |
            An optional token that indicates the beginning of the page of results to be returned.
            Any additional query parameters are ignored if a page token is present.
            If omitted, the first page of results is returned. This value is obtained from the 'next_url' field of the operation response.
        type: str
    guid:
        description:
            - The GUID of the instance.
        type: str
    service:
        description:
            - The unique ID of the offering. This value is provided by and stored in the global catalog.
        type: str
    state_:
        description:
            - The state of the instance. If not specified, instances in state `active` and `provisioning` are returned.
        type: str
    type:
        description:
            - The type of the instance, for example, `service_instance`.
        type: str
    updated_to:
        description:
            - End date inclusive filter.
        type: str
'''

EXAMPLES = r'''
Examples coming soon.
'''

from ..module_utils import config
# Todo: change this to external python package format
from ibm_platform_services import ResourceControllerV2
from ..module_utils import catalog
from ansible.module_utils.basic import AnsibleModule
from ibm_cloud_sdk_core import ApiException


def run_module():
    module_args = dict(
        resource_group_id=dict(
            type='str',
            required=False),
        updated_from=dict(
            type='str',
            required=False),
        plan=dict(
            type='str',
            required=False),
        sub_type=dict(
            type='str',
            required=False),
        name=dict(
            type='str',
            required=False),
        limit=dict(
            type='int',
            required=False),
        start=dict(
            type='str',
            required=False),
        guid=dict(
            type='str',
            required=False),
        service=dict(
            type='str',
            required=False),
        state_=dict(
            type='str',
            required=False),
        type=dict(
            type='str',
            required=False),
        updated_to=dict(
            type='str',
            required=False),
    )

    module = AnsibleModule(
        argument_spec=module_args,
        supports_check_mode=False
    )

    resource_group_id = module.params["resource_group_id"]
    updated_from = module.params["updated_from"]
    plan = module.params["plan"]
    sub_type = module.params["sub_type"]
    name = module.params["name"]
    limit = module.params["limit"]
    start = module.params["start"]
    guid = module.params["guid"]
    service = module.params["service"]
    state_ = module.params["state_"]
    type = module.params["type"]
    updated_to = module.params["updated_to"]

    # sdk = ResourceControllerV2.new_instance()

    sdk = config.get_resource_contollerV2_sdk()
    # list
    try:
        serviceID = ""
        servicePlanID = ""
        if service is not None:
            serviceID = catalog.get_serviceID(service)
            servicePlanID = ""
            if plan != "" and plan is not None and plan != "None":
                serviceID, servicePlanID = catalog.get_planID(service, plan)
        response = sdk.list_resource_instances(
            guid=guid,
            name=name,
            resource_group_id=resource_group_id,
            resource_id=serviceID,
            resource_plan_id=servicePlanID,
            type=type,
            sub_type=sub_type,
            limit=limit,
            start=start,
            state=state_,
            updated_from=updated_from,
            updated_to=updated_to
        )
        module.exit_json(msg=response.get_result())
    except ApiException as ex:
        module.fail_json(msg=ex.message)


def main():
    run_module()


if __name__ == '__main__':
    main()
