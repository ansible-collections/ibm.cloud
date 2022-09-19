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


import os

from ibm_cloud_sdk_core import ApiException
from ansible_collections.community.internal_test_tools.tests.unit.compat.mock import patch
from ansible_collections.community.internal_test_tools.tests.unit.plugins.modules.utils import ModuleTestCase, AnsibleFailJson, AnsibleExitJson, set_module_args

from .common import DetailedResponseMock
from plugins.modules import ibm_resource_instance_info


class TestResourceInstanceModuleInfo(ModuleTestCase):
    """
    Test class for ResourceInstance module testing.
    """

    def test_list_ibm_resource_instance_success(self):
        """Test the "list" path - successful."""
        patcher = patch(
            'plugins.modules.ibm_resource_instance_info.ResourceControllerV2.get_resource_instance')
        mock = patcher.start()
        mock.return_value = DetailedResponseMock([])

        set_module_args({
            'id': 'testString',
        })

        with self.assertRaises(AnsibleExitJson) as result:
            os.environ['RESOURCE_CONTROLLER_AUTH_TYPE'] = 'noAuth'
            os.environ['IC_API_KEY'] = 'noAuthAPIKey'
            ibm_resource_instance_info.main()

        assert result.exception.args[0]['msg'] == []

        mock.assert_called_once()

        patcher.stop()

    def test_list_ibm_resource_instance_failed(self):
        """Test the "list" path - failed."""
        patcher = patch(
            'plugins.modules.ibm_resource_instance_info.ResourceControllerV2.get_resource_instance')
        mock = patcher.start()
        mock.side_effect = ApiException(
            400, message='List ibm_resource_instance error')

        set_module_args({
            'id': 'testString',
        })

        with self.assertRaises(AnsibleFailJson) as result:
            os.environ['RESOURCE_CONTROLLER_AUTH_TYPE'] = 'noAuth'
            os.environ['IC_API_KEY'] = 'noAuthAPIKey'
            ibm_resource_instance_info.main()

        assert result.exception.args[0]['msg'] == 'List ibm_resource_instance error'

        mock.assert_called_once()

        patcher.stop()
