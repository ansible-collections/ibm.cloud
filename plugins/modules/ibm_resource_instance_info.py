#!/usr/bin/python
# coding: utf-8

# (C) Copyright IBM Corp. 2023.
#
# GNU General Public License v3.0+ (see LICENSE or https://www.gnu.org/licenses/gpl-3.0.txt)

from __future__ import (absolute_import, division, print_function)
__metaclass__ = type


DOCUMENTATION = r'''
---
module: ibm_resource_instance_info
short_description: Manage C(resource_instance) for Resource Controller.
author:
  - Kavya Handadi (@kavya498)
  - Umar Ali (@umarali-nagoor)
version_added: "1.0.0"
description:
  - This module retrieves one or more C(resource_instance) for Resource Controller.
requirements:
  - "ResourceControllerV2"
options:
  id:
    description: "The resource instance URL-encoded CRN or GUID."
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

- name: List ibm_resource_instance
  ibm_resource_instance_info:
    id: 'testString'
'''

RETURN = r'''
id:
  description: "The ID associated with the instance."
  type: str
  returned: on success for list operation
guid:
  description: "The GUID of the instance."
  type: str
  returned: on success for list operation
url:
  description: "When you provision a new resource, a relative URL path is created identifying the
    location of the instance."
  type: str
  returned: on success for list operation
created_at:
  description: "The date when the instance was created."
  type: str
  returned: on success for list operation
updated_at:
  description: "The date when the instance was last updated."
  type: str
  returned: on success for list operation
deleted_at:
  description: "The date when the instance was deleted."
  type: str
  returned: on success for list operation
created_by:
  description: "The subject who created the instance."
  type: str
  returned: on success for list operation
updated_by:
  description: "The subject who updated the instance."
  type: str
  returned: on success for list operation
deleted_by:
  description: "The subject who deleted the instance."
  type: str
  returned: on success for list operation
scheduled_reclaim_at:
  description: "The date when the instance was scheduled for reclamation."
  type: str
  returned: on success for list operation
restored_at:
  description: "The date when the instance under reclamation was restored."
  type: str
  returned: on success for list operation
restored_by:
  description: "The subject who restored the instance back from reclamation."
  type: str
  returned: on success for list operation
scheduled_reclaim_by:
  description: "The subject who initiated the instance reclamation."
  type: str
  returned: on success for list operation
name:
  description: "The human-readable name of the instance."
  type: str
  returned: on success for list operation
region_id:
  description: "The deployment location where the instance was provisioned."
  type: str
  returned: on success for list operation
account_id:
  description: "An alpha-numeric value identifying the account ID."
  type: str
  returned: on success for list operation
reseller_channel_id:
  description: "The unique ID of the reseller channel where the instance was provisioned from."
  type: str
  returned: on success for list operation
resource_plan_id:
  description: "The unique ID of the plan associated with the offering. This value is provided by and
    stored in the global catalog."
  type: str
  returned: on success for list operation
resource_group_id:
  description: "The ID of the resource group."
  type: str
  returned: on success for list operation
resource_group_crn:
  description: "The CRN of the resource group."
  type: str
  returned: on success for list operation
target_crn:
  description: "The deployment CRN as defined in the global catalog. The Cloud Resource Name (CRN) of
    the deployment location where the instance is provisioned."
  type: str
  returned: on success for list operation
parameters:
  description: "The current configuration parameters of the instance."
  type: dict
  returned: on success for list operation
allow_cleanup:
  description: "A boolean that dictates if the resource instance should be deleted (cleaned up) during
    the processing of a region instance delete call."
  type: bool
  returned: on success for list operation
crn:
  description: "The full Cloud Resource Name (CRN) associated with the instance. For more information
    about this format, see [Cloud Resource
    Names](https://cloud.ibm.com/docs/overview?topic=overview-crn)."
  type: str
  returned: on success for list operation
state:
  description: "The current state of the instance. For example, if the instance is deleted, it will
    return removed."
  type: str
  choices:
    - "active"
    - "inactive"
    - "removed"
    - "pending_removal"
    - "pending_reclamation"
    - "failed"
    - "provisioning"
    - "pre_provisioning"
  returned: on success for list operation
type:
  description: "The type of the instance, for example, C(service_instance)."
  type: str
  returned: on success for list operation
sub_type:
  description: "The sub-type of instance, for example, C(cfaas)."
  type: str
  returned: on success for list operation
resource_id:
  description: "The unique ID of the offering. This value is provided by and stored in the global
    catalog."
  type: str
  returned: on success for list operation
dashboard_url:
  description: "The resource-broker-provided URL to access administrative features of the instance."
  type: str
  returned: on success for list operation
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
  returned: on success for list operation
resource_aliases_url:
  description: "The relative path to the resource aliases for the instance."
  type: str
  returned: on success for list operation
resource_bindings_url:
  description: "The relative path to the resource bindings for the instance."
  type: str
  returned: on success for list operation
resource_keys_url:
  description: "The relative path to the resource keys for the instance."
  type: str
  returned: on success for list operation
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
  returned: on success for list operation
migrated:
  description: "A boolean that dictates if the resource instance was migrated from a previous CF
    instance."
  type: bool
  returned: on success for list operation
extensions:
  description: "Additional instance properties, contributed by the service and/or platform, are
    represented as key-value pairs."
  type: dict
  returned: on success for list operation
controlled_by:
  description: "The CRN of the resource that has control of the instance."
  type: str
  returned: on success for list operation
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
except ImportError as imp_exc:
    MISSING_IMPORT_EXC = imp_exc
else:
    MISSING_IMPORT_EXC = None


def run_module():
    module_args = dict(
        id=dict(
            type='str',
            required=False),
    )

    module = AnsibleModule(
        argument_spec=module_args,
        supports_check_mode=True
    )

    if MISSING_IMPORT_EXC is not None:
        module.fail_json(msg='Missing required import: ' + MISSING_IMPORT_EXC.msg)

    id = module.params["id"]

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
        response = sdk.get_resource_instance(
            id=id,
        )

        result = response.get_result()

        module.exit_json(**result)
    except ApiException as ex:
        module.fail_json(msg=ex.message)


def main():
    run_module()


if __name__ == '__main__':
    main()
