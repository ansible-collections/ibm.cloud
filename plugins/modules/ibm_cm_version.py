# coding: utf-8

# (C) Copyright IBM Corp. 2022.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#      http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

from __future__ import (absolute_import, division, print_function)
__metaclass__ = type


DOCUMENTATION = r'''
---
module: ibm_cm_version
short_description: Manage ibm_cm_version resources.
author: Kavya Handadi (@kavya498)
version_added: "1.0.0"
description:
    - This module creates, updates, or deletes a ibm_cm_version.
    - By default the module will look for an existing ibm_cm_version.
requirements:
    - "CatalogManagementV1"
options:
    content:
        description:
            - byte array representing the content to be imported.  Only supported for OVA images at this time.
        type: str
    tags:
        description:
            - Tags array.
        type: list
        elements: str
    target_kinds:
        description:
            - Target kinds.  Current valid values are 'iks', 'roks', 'vcenter', and 'terraform'.
        type: list
        elements: str
    repo_type:
        description:
            - The type of repository containing this version.  Valid values are 'public_git' or 'enterprise_git'.
        type: str
    zipurl:
        description:
            - URL path to zip location.  If not specified, must provide content in the body of this call.
        type: str
    version_loc_id:
        description:
            - A dotted value of `catalogID`.`versionID`.
        type: str
    catalog_identifier:
        description:
            - Catalog identifier.
        type: str
    offering_id:
        description:
            - Offering identification.
        type: str
    target_version:
        description:
            - The semver value for this new version, if not found in the zip url package content.
        type: str
    include_config:
        description:
            - Add all possible configuration values to this version when importing.
        type: bool
    is_vsi:
        description:
            - Indicates that the current terraform template is used to install a VSI Image.
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
from ibm_platform_services import CatalogManagementV1
from ibm_cloud_sdk_core import ApiException
from ansible.module_utils.basic import AnsibleModule
import base64


def run_module():
    module_args = dict(
        content=dict(
            type='str',
            required=False),
        tags=dict(
            type='list',
            elements=str,
            required=False),
        target_kinds=dict(
            type='list',
            elements=str,
            required=False),
        repo_type=dict(
            type='str',
            required=False),
        zipurl=dict(
            type='str',
            required=False),
        version_loc_id=dict(
            type='str',
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

    content = module.params["content"]
    try:
        content = base64.b64decode(content) if content is not None else None
    except Exception as ex:
        module.fail_json(msg=f'Error during decoding value for content: {ex}')
    tags = module.params["tags"]
    target_kinds = module.params["target_kinds"]
    repo_type = module.params["repo_type"]
    zipurl = module.params["zipurl"]
    version_loc_id = module.params["version_loc_id"]
    catalog_identifier = module.params["catalog_identifier"]
    offering_id = module.params["offering_id"]
    target_version = module.params["target_version"]
    include_config = module.params["include_config"]
    is_vsi = module.params["is_vsi"]
    state = module.params["state"]

    sdk = config.get_catalog_management_sdk()

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
                payload = {"id": version_loc_id, "status": "deleted"}
                module.exit_json(changed=True, msg=payload)
        else:
            payload = {"id": version_loc_id, "status": "not_found"}
            module.exit_json(changed=False, msg=payload)

    if state == "present":
        if not resource_exists:
            # Create path
            try:
                result = sdk.import_offering_version(
                    catalog_identifier=catalog_identifier,
                    offering_id=offering_id,
                    tags=tags,
                    target_kinds=target_kinds,
                    content=content,
                    zipurl=zipurl,
                    target_version=target_version,
                    include_config=include_config,
                    is_vsi=is_vsi,
                    repo_type=repo_type,
                ).get_result()
            except ApiException as ex:
                module.fail_json(msg=ex.message)
            else:
                module.exit_json(changed=True, msg=result)


def main():
    run_module()


if __name__ == '__main__':
    main()
