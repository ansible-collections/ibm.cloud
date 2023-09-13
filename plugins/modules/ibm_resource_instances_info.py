#!/usr/bin/python
# coding: utf-8

# (C) Copyright IBM Corp. 2023.
#
# GNU General Public License v3.0+ (see LICENSE or https://www.gnu.org/licenses/gpl-3.0.txt)

from __future__ import (absolute_import, division, print_function)
__metaclass__ = type


DOCUMENTATION = r'''
---
module: ibm_resource_instances_info
short_description: Manage C(resource_instances) for Resource Controller.
author:
  - Kavya Handadi (@kavya498)
  - Umar Ali (@umarali-nagoor)
version_added: "1.0.0"
description:
  - This module retrieves one or more C(resource_instances) for Resource Controller.
requirements:
  - "ResourceControllerV2"
options:
  resource_group_id:
    description: "The ID of the resource group."
    type: str
  updated_from:
    description: "Start date inclusive filter."
    type: str
  resource_plan_id:
    description: "The unique ID of the plan associated with the offering. This value is provided by
      and stored in the global catalog."
    type: str
  sub_type:
    description: "The sub-type of instance, for example, C(kms)."
    type: str
  name:
    description: "The human-readable name of the instance."
    type: str
  limit:
    description: "Limit on how many items should be returned."
    type: int
  guid:
    description: "The GUID of the instance."
    type: str
  resource_id:
    description: "The unique ID of the offering. This value is provided by and stored in the global
      catalog."
    type: str
  state:
    description: "The state of the instance. If not specified, instances in state C(active) and
      C(provisioning) are returned."
    type: str
    choices:
      - "active"
      - "inactive"
      - "failed"
      - "pending_reclamation"
      - "provisioning"
      - "pre_provisioning"
      - "removed"
  type:
    description: "The type of the instance, for example, C(service_instance)."
    type: str
  updated_to:
    description: "End date inclusive filter."
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

- name: List ibm_resource_instances
  ibm_resource_instances_info:
    guid: 'testString'
    name: 'testString'
    resource_group_id: 'testString'
    resource_id: 'testString'
    resource_plan_id: 'testString'
    type: 'testString'
    sub_type: 'testString'
    limit: 100
    state: 'active'
    updated_from: '2021-01-01'
    updated_to: '2021-01-01'
'''

RETURN = r'''
resources:
  description: "A list with all ResourceInstance instances."
  type: list
  elements: 'dict'
  contains:
    id:
      description: "The ID associated with the instance."
      type: str
    guid:
      description: "The GUID of the instance."
      type: str
    url:
      description: "When you provision a new resource, a relative URL path is created identifying the
        location of the instance."
      type: str
    created_at:
      description: "The date when the instance was created."
      type: str
    updated_at:
      description: "The date when the instance was last updated."
      type: str
    deleted_at:
      description: "The date when the instance was deleted."
      type: str
    created_by:
      description: "The subject who created the instance."
      type: str
    updated_by:
      description: "The subject who updated the instance."
      type: str
    deleted_by:
      description: "The subject who deleted the instance."
      type: str
    scheduled_reclaim_at:
      description: "The date when the instance was scheduled for reclamation."
      type: str
    restored_at:
      description: "The date when the instance under reclamation was restored."
      type: str
    restored_by:
      description: "The subject who restored the instance back from reclamation."
      type: str
    scheduled_reclaim_by:
      description: "The subject who initiated the instance reclamation."
      type: str
    name:
      description: "The human-readable name of the instance."
      type: str
    region_id:
      description: "The deployment location where the instance was provisioned."
      type: str
    account_id:
      description: "An alpha-numeric value identifying the account ID."
      type: str
    reseller_channel_id:
      description: "The unique ID of the reseller channel where the instance was provisioned from."
      type: str
    resource_plan_id:
      description: "The unique ID of the plan associated with the offering. This value is provided by and
        stored in the global catalog."
      type: str
    resource_group_id:
      description: "The ID of the resource group."
      type: str
    resource_group_crn:
      description: "The CRN of the resource group."
      type: str
    target_crn:
      description: "The deployment CRN as defined in the global catalog. The Cloud Resource Name (CRN) of
        the deployment location where the instance is provisioned."
      type: str
    parameters:
      description: "The current configuration parameters of the instance."
      type: dict
    allow_cleanup:
      description: "A boolean that dictates if the resource instance should be deleted (cleaned up) during
        the processing of a region instance delete call."
      type: bool
    crn:
      description: "The full Cloud Resource Name (CRN) associated with the instance. For more information
        about this format, see [Cloud Resource
        Names](https://cloud.ibm.com/docs/overview?topic=overview-crn)."
      type: str
    state:
      description: "The current state of the instance. For example, if the instance is deleted, it will
        return removed."
      type: str
      choices:
        - 'active'
        - 'inactive'
        - 'removed'
        - 'pending_removal'
        - 'pending_reclamation'
        - 'failed'
        - 'provisioning'
        - 'pre_provisioning'
    type:
      description: "The type of the instance, for example, C(service_instance)."
      type: str
    sub_type:
      description: "The sub-type of instance, for example, C(cfaas)."
      type: str
    resource_id:
      description: "The unique ID of the offering. This value is provided by and stored in the global
        catalog."
      type: str
    dashboard_url:
      description: "The resource-broker-provided URL to access administrative features of the instance."
      type: str
    last_operation:
      description: "The status of the last operation requested on the instance."
      type: dict
      contains:
        type:
          description: "The last operation type of the resource instance."
          type: str
        state:
          description: "The last operation state of the resoure instance. This indicates if the resource's
            last operation is in progress, succeeded or failed."
          type: str
          choices:
            - 'in progress'
            - 'succeeded'
            - 'failed'
        sub_type:
          description: "The last operation sub type of the resoure instance."
          type: str
        async_:
          description: "A boolean that indicates if the resource is provisioned asynchronously or not."
          type: bool
        description:
          description: "The description of the status of last operation."
          type: str
        reason_code:
          description: "Optional string that states the reason code for the last operation state change."
          type: str
        poll_after:
          description: "A field which indicates the time after which the instance's last operation is to be
            polled."
          type: float
        cancelable:
          description: "A boolean that indicates if the resource's last operation is cancelable or not."
          type: bool
        poll:
          description: "A boolean that indicates if the resource broker's last operation can be polled or not."
          type: bool
    resource_aliases_url:
      description: "The relative path to the resource aliases for the instance."
      type: str
    resource_bindings_url:
      description: "The relative path to the resource bindings for the instance."
      type: str
    resource_keys_url:
      description: "The relative path to the resource keys for the instance."
      type: str
    plan_history:
      description: "The plan history of the instance."
      type: list
      elements: 'dict'
      contains:
        resource_plan_id:
          description: "The unique ID of the plan associated with the offering. This value is provided by and
            stored in the global catalog."
          type: str
        start_date:
          description: "The date on which the plan was changed."
          type: str
        requestor_id:
          description: "The subject who made the plan change."
          type: str
    migrated:
      description: "A boolean that dictates if the resource instance was migrated from a previous CF
        instance."
      type: bool
    extensions:
      description: "Additional instance properties, contributed by the service and/or platform, are
        represented as key-value pairs."
      type: dict
    controlled_by:
      description: "The CRN of the resource that has control of the instance."
      type: str
    locked:
      description: "A boolean that dictates if the resource instance is locked or not."
      type: bool
  returned: on success for list operation
msg:
  description: an error message that describes what went wrong
  type: str
  returned: on error
'''


from ansible.module_utils.basic import AnsibleModule

try:
    from ..module_utils.auth import get_authenticator
    from ibm_cloud_sdk_core import ApiException
    from ibm_platform_services import ResourceControllerV2
    from ibm_platform_services.resource_controller_v2 import ResourceInstancesPager
except ImportError as imp_exc:
    MISSING_IMPORT_EXC = imp_exc
else:
    MISSING_IMPORT_EXC = None


def run_module():
    module_args = dict(
        resource_group_id=dict(
            type='str',
            required=False),
        updated_from=dict(
            type='str',
            required=False),
        resource_plan_id=dict(
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
        guid=dict(
            type='str',
            required=False),
        resource_id=dict(
            type='str',
            required=False),
        state=dict(
            type='str',
            choices=[
                'active',
                'inactive',
                'failed',
                'pending_reclamation',
                'provisioning',
                'pre_provisioning',
                'removed',
            ],
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
        supports_check_mode=True
    )

    if MISSING_IMPORT_EXC is not None:
        module.fail_json(msg='Missing required import: ' + MISSING_IMPORT_EXC.msg)

    resource_group_id = module.params["resource_group_id"]
    updated_from = module.params["updated_from"]
    resource_plan_id = module.params["resource_plan_id"]
    sub_type = module.params["sub_type"]
    name = module.params["name"]
    limit = module.params["limit"]
    guid = module.params["guid"]
    resource_id = module.params["resource_id"]
    state = module.params["state"]
    type = module.params["type"]
    updated_to = module.params["updated_to"]

    if module.check_mode:
        module.exit_json(msg='The module would run with the following parameters: ' + module.paramss)

    authenticator = get_authenticator(service_name='resource_controller')
    if authenticator is None:
        module.fail_json(msg='Cannot create the authenticator.')

    sdk = ResourceControllerV2(
        authenticator=authenticator,
    )

    sdk.configure_service('resource_controller')

    # list
    try:
        pager = ResourceInstancesPager(
            client=sdk,
            guid=guid,
            name=name,
            resource_group_id=resource_group_id,
            resource_id=resource_id,
            resource_plan_id=resource_plan_id,
            type=type,
            sub_type=sub_type,
            limit=limit,
            state=state,
            updated_from=updated_from,
            updated_to=updated_to,
        )
        result = pager.get_all()
        module.exit_json(resources=result)
    except ApiException as ex:
        module.fail_json(msg=ex.message)


def main():
    run_module()


if __name__ == '__main__':
    main()
