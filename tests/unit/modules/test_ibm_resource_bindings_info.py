# (C) Copyright IBM Corp. 2022.
# GNU General Public License v3.0+ (see LICENSE or https://www.gnu.org/licenses/gpl-3.0.txt)


import os

from ibm_cloud_sdk_core import ApiException
from ansible_collections.community.internal_test_tools.tests.unit.compat.mock import patch
from ansible_collections.community.internal_test_tools.tests.unit.plugins.modules.utils import ModuleTestCase, AnsibleFailJson, AnsibleExitJson, set_module_args

from .common import DetailedResponseMock
from plugins.modules import ibm_resource_bindings_info


class TestResourceBindingsListModuleInfo(ModuleTestCase):
    """
    Test class for ResourceBindingsList module testing.
    """

    def test_list_ibm_resource_bindings_success(self):
        """Test the "list" path - successful."""
        patcher = patch(
            'plugins.modules.ibm_resource_bindings_info.ResourceControllerV2.list_resource_bindings')
        mock = patcher.start()
        mock.return_value = DetailedResponseMock([])

        with self.assertRaises(AnsibleExitJson) as result:
            os.environ['RESOURCE_CONTROLLER_AUTH_TYPE'] = 'noAuth'
            os.environ['IC_API_KEY'] = 'noAuthAPIKey'
            ibm_resource_bindings_info.main()

        assert result.exception.args[0]['msg'] == []

        mock.assert_called_once()

        patcher.stop()

    def test_list_ibm_resource_bindings_failed(self):
        """Test the "list" path - failed."""
        patcher = patch(
            'plugins.modules.ibm_resource_bindings_info.ResourceControllerV2.list_resource_bindings')
        mock = patcher.start()
        mock.side_effect = ApiException(
            400, message='List ibm_resource_bindings error')

        with self.assertRaises(AnsibleFailJson) as result:
            os.environ['RESOURCE_CONTROLLER_AUTH_TYPE'] = 'noAuth'
            os.environ['IC_API_KEY'] = 'noAuthAPIKey'
            ibm_resource_bindings_info.main()

        assert result.exception.args[0]['msg'] == 'List ibm_resource_bindings error'

        mock.assert_called_once()

        patcher.stop()
