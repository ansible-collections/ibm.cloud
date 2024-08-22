# (C) Copyright IBM Corp. 2024.
#
# GNU General Public License v3.0+ (see LICENSE or https://www.gnu.org/licenses/gpl-3.0.txt)

from __future__ import (absolute_import, division, print_function)
__metaclass__ = type

import os

from ansible_collections.community.internal_test_tools.tests.unit.compat.mock import patch
from ansible_collections.community.internal_test_tools.tests.unit.plugins.modules.utils import ModuleTestCase, AnsibleFailJson, AnsibleExitJson, set_module_args
from plugins.modules import ibm_cm_object_info

try:
    from .common import DetailedResponseMock
    from ibm_cloud_sdk_core import ApiException
except ImportError as imp_exc:
    MISSING_IMPORT_EXC = imp_exc
else:
    MISSING_IMPORT_EXC = None


def mock_operations(func):
    def wrapper(self):
        # Make sure the imports are correct in both test and module packages.
        self.assertIsNone(MISSING_IMPORT_EXC)
        self.assertIsNone(ibm_cm_object_info.MISSING_IMPORT_EXC)

        # Set-up mocks for each operation.
        self.read_patcher = patch('plugins.modules.ibm_cm_object_info.CatalogManagementV1.get_object')
        self.read_mock = self.read_patcher.start()

        # Run the actual function.
        func(self)

        # Stop the patchers.
        self.read_patcher.stop()

    return wrapper


class TestCatalogObjectModuleInfo(ModuleTestCase):
    """
    Test class for CatalogObject module testing.
    """

    @mock_operations
    def test_read_ibm_cm_object_success(self):
        """Test the "read" path - successful."""
        datasource = {
            'catalog_identifier': 'testString',
            'object_identifier': 'testString',
        }

        self.read_mock.return_value = DetailedResponseMock(datasource)

        set_module_args({
            'catalog_identifier': 'testString',
            'object_identifier': 'testString',
        })

        with self.assertRaises(AnsibleExitJson) as result:
            os.environ['CATALOG_MANAGEMENT_AUTH_TYPE'] = 'noAuth'
            ibm_cm_object_info.main()

        for field, value in datasource.items():
            self.assertEqual(value, result.exception.args[0].get(field))

        self.read_mock.assert_called_once_with(
            catalog_identifier='testString',
            object_identifier='testString',
        )

    @mock_operations
    def test_read_ibm_cm_object_failed(self):
        """Test the "read" path - failed."""
        self.read_mock.side_effect = ApiException(400, message='Read ibm_cm_object error')

        set_module_args({
            'catalog_identifier': 'testString',
            'object_identifier': 'testString',
        })

        with self.assertRaises(AnsibleFailJson) as result:
            os.environ['CATALOG_MANAGEMENT_AUTH_TYPE'] = 'noAuth'
            ibm_cm_object_info.main()

        self.assertEqual(result.exception.args[0]['msg'], 'Read ibm_cm_object error')

        self.read_mock.assert_called_once_with(
            catalog_identifier='testString',
            object_identifier='testString',
        )
