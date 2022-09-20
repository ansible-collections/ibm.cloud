# (C) Copyright IBM Corp. 2022.
# GNU General Public License v3.0+ (see LICENSE or https://www.gnu.org/licenses/gpl-3.0.txt)


import os

from ibm_cloud_sdk_core import ApiException
from ansible_collections.community.internal_test_tools.tests.unit.compat.mock import patch
from ansible_collections.community.internal_test_tools.tests.unit.plugins.modules.utils import ModuleTestCase, AnsibleFailJson, AnsibleExitJson, set_module_args

from .common import DetailedResponseMock
from plugins.modules import ibm_resource_binding_info


class TestResourceBindingModuleInfo(ModuleTestCase):
    """
    Test class for ResourceBinding module testing.
    """

    def test_read_ibm_resource_binding_success(self):
        """Test the "read" path - successful."""
        datasource = {
            'id': 'testString',
        }

        patcher = patch(
            'plugins.modules.ibm_resource_binding_info.ResourceControllerV2.get_resource_binding')
        mock = patcher.start()
        mock.return_value = DetailedResponseMock(datasource)

        set_module_args({
            'id': 'testString',
        })

        with self.assertRaises(AnsibleExitJson) as result:
            os.environ['RESOURCE_CONTROLLER_AUTH_TYPE'] = 'noAuth'
            os.environ['IC_API_KEY'] = 'noAuthAPIKey'
            ibm_resource_binding_info.main()

        assert result.exception.args[0]['msg'] == datasource

        mock.assert_called_once_with(
            id='testString',
        )

        patcher.stop()

    def test_read_ibm_resource_binding_failed(self):
        """Test the "read" path - failed."""
        patcher = patch(
            'plugins.modules.ibm_resource_binding_info.ResourceControllerV2.get_resource_binding')
        mock = patcher.start()
        mock.side_effect = ApiException(
            400, message='Read ibm_resource_binding error')

        set_module_args({
            'id': 'testString',
        })

        with self.assertRaises(AnsibleFailJson) as result:
            os.environ['RESOURCE_CONTROLLER_AUTH_TYPE'] = 'noAuth'
            os.environ['IC_API_KEY'] = 'noAuthAPIKey'
            ibm_resource_binding_info.main()

        assert result.exception.args[0]['msg'] == 'Read ibm_resource_binding error'

        mock.assert_called_once_with(
            id='testString',
        )

        patcher.stop()
