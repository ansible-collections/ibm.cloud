# (C) Copyright IBM Corp. 2022.
# GNU General Public License v3.0+ (see LICENSE or https://www.gnu.org/licenses/gpl-3.0.txt)

from __future__ import (absolute_import, division, print_function)
__metaclass__ = type

import os

from .common import DetailedResponseMock
from plugins.modules import ibm_schematics_inventory_info
from ansible_collections.community.internal_test_tools.tests.unit.compat.mock import patch
from ansible_collections.community.internal_test_tools.tests.unit.plugins.modules.utils import ModuleTestCase, AnsibleFailJson, AnsibleExitJson, set_module_args

try:
    from ibm_cloud_sdk_core import ApiException
except ImportError:
    pass


class TestInventoryResourceRecordModuleInfo(ModuleTestCase):
    """
    Test class for InventoryResourceRecord module testing.
    """

    def test_read_ibm_schematics_inventory_success(self):
        """Test the "read" path - successful."""
        datasource = {
            'inventory_id': 'testString',
            'profile': 'summary',
        }

        patcher = patch(
            'plugins.modules.ibm_schematics_inventory_info.SchematicsV1.get_inventory')
        mock = patcher.start()
        mock.return_value = DetailedResponseMock(datasource)

        set_module_args({
            'inventory_id': 'testString',
            'profile': 'summary',
        })

        with self.assertRaises(AnsibleExitJson) as result:
            os.environ['SCHEMATICS_AUTH_TYPE'] = 'noAuth'
            os.environ['IC_API_KEY'] = 'noAuthAPIKey'
            ibm_schematics_inventory_info.main()

        assert result.exception.args[0]['msg'] == datasource

        mock.assert_called_once_with(
            inventory_id='testString',
            profile='summary',
        )

        patcher.stop()

    def test_read_ibm_schematics_inventory_failed(self):
        """Test the "read" path - failed."""
        patcher = patch(
            'plugins.modules.ibm_schematics_inventory_info.SchematicsV1.get_inventory')
        mock = patcher.start()
        mock.side_effect = ApiException(
            400, message='Read ibm_schematics_inventory error')

        set_module_args({
            'inventory_id': 'testString',
            'profile': 'summary',
        })

        with self.assertRaises(AnsibleFailJson) as result:
            os.environ['SCHEMATICS_AUTH_TYPE'] = 'noAuth'
            os.environ['IC_API_KEY'] = 'noAuthAPIKey'
            ibm_schematics_inventory_info.main()

        assert result.exception.args[0]['msg'] == 'Read ibm_schematics_inventory error'

        mock.assert_called_once_with(
            inventory_id='testString',
            profile='summary',
        )

        patcher.stop()
