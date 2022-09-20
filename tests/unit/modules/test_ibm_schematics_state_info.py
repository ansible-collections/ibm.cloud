# (C) Copyright IBM Corp. 2022.
# GNU General Public License v3.0+ (see LICENSE or https://www.gnu.org/licenses/gpl-3.0.txt)

from __future__ import (absolute_import, division, print_function)
__metaclass__ = type

import os

from .common import DetailedResponseMock
from plugins.modules import ibm_schematics_state_info
from ansible_collections.community.internal_test_tools.tests.unit.compat.mock import patch
from ansible_collections.community.internal_test_tools.tests.unit.plugins.modules.utils import ModuleTestCase, AnsibleFailJson, AnsibleExitJson, set_module_args

try:
    from ibm_cloud_sdk_core import ApiException
except ImportError:
    pass


class TestTemplateStateStoreModuleInfo(ModuleTestCase):
    """
    Test class for TemplateStateStore module testing.
    """

    def test_list_ibm_schematics_state_success(self):
        """Test the "list" path - successful."""
        patcher = patch(
            'plugins.modules.ibm_schematics_state_info.SchematicsV1.get_workspace_template_state')
        mock = patcher.start()
        mock.return_value = DetailedResponseMock([])

        set_module_args({
            'w_id': 'testString',
            't_id': 'testString',
        })

        with self.assertRaises(AnsibleExitJson) as result:
            os.environ['SCHEMATICS_AUTH_TYPE'] = 'noAuth'
            os.environ['IC_API_KEY'] = 'noAuthAPIKey'
            ibm_schematics_state_info.main()

        assert result.exception.args[0]['msg'] == []

        mock.assert_called_once()
        patcher.stop()

    def test_list_ibm_schematics_state_failed(self):
        """Test the "list" path - failed."""
        patcher = patch(
            'plugins.modules.ibm_schematics_state_info.SchematicsV1.get_workspace_template_state')
        mock = patcher.start()
        mock.side_effect = ApiException(
            400, message='List ibm_schematics_state error')

        set_module_args({
            'w_id': 'testString',
            't_id': 'testString',
        })

        with self.assertRaises(AnsibleFailJson) as result:
            os.environ['SCHEMATICS_AUTH_TYPE'] = 'noAuth'
            os.environ['IC_API_KEY'] = 'noAuthAPIKey'
            ibm_schematics_state_info.main()

        assert result.exception.args[0]['msg'] == 'List ibm_schematics_state error'

        mock.assert_called_once()

        patcher.stop()
