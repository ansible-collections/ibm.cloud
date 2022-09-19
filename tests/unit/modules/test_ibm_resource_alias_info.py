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
from plugins.modules import ibm_resource_alias_info


class TestResourceAliasModuleInfo(ModuleTestCase):
    """
    Test class for ResourceAlias module testing.
    """

    def test_read_ibm_resource_alias_success(self):
        """Test the "read" path - successful."""
        datasource = {
            'id': 'testString',
        }

        patcher = patch(
            'plugins.modules.ibm_resource_alias_info.ResourceControllerV2.get_resource_alias')
        mock = patcher.start()
        mock.return_value = DetailedResponseMock(datasource)

        set_module_args({
            'id': 'testString',
        })

        with self.assertRaises(AnsibleExitJson) as result:
            os.environ['RESOURCE_CONTROLLER_AUTH_TYPE'] = 'noAuth'
            os.environ['IC_API_KEY'] = 'noAuthAPIKey'
            ibm_resource_alias_info.main()

        assert result.exception.args[0]['msg'] == datasource

        mock.assert_called_once_with(
            id='testString',
        )

        patcher.stop()

    def test_read_ibm_resource_alias_failed(self):
        """Test the "read" path - failed."""
        patcher = patch(
            'plugins.modules.ibm_resource_alias_info.ResourceControllerV2.get_resource_alias')
        mock = patcher.start()
        mock.side_effect = ApiException(
            400, message='Read ibm_resource_alias error')

        set_module_args({
            'id': 'testString',
        })

        with self.assertRaises(AnsibleFailJson) as result:
            os.environ['RESOURCE_CONTROLLER_AUTH_TYPE'] = 'noAuth'
            os.environ['IC_API_KEY'] = 'noAuthAPIKey'
            ibm_resource_alias_info.main()

        assert result.exception.args[0]['msg'] == 'Read ibm_resource_alias error'

        mock.assert_called_once_with(
            id='testString',
        )

        patcher.stop()
