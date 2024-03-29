# (C) Copyright IBM Corp. 2023.
#
# GNU General Public License v3.0+ (see LICENSE or https://www.gnu.org/licenses/gpl-3.0.txt)

from __future__ import (absolute_import, division, print_function)
__metaclass__ = type

import os

from ansible_collections.community.internal_test_tools.tests.unit.compat.mock import patch
from ansible_collections.community.internal_test_tools.tests.unit.plugins.modules.utils import ModuleTestCase, AnsibleFailJson, AnsibleExitJson, set_module_args
from plugins.modules import ibm_resource_quotas_info

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
        self.assertIsNone(ibm_resource_quotas_info.MISSING_IMPORT_EXC)

        # Set-up mocks for each operation.
        self.list_patcher = patch('plugins.modules.ibm_resource_quotas_info.ResourceManagerV2.list_quota_definitions')
        self.list_mock = self.list_patcher.start()

        # Run the actual function.
        func(self)

        # Stop the patchers.
        self.list_patcher.stop()

    return wrapper


class TestQuotaDefinitionListModuleInfo(ModuleTestCase):
    """
    Test class for QuotaDefinitionList module testing.
    """

    @mock_operations
    def test_list_ibm_resource_quotas_success(self):
        """Test the "list" path - successful."""
        self.list_mock.return_value = DetailedResponseMock(dict(resources=[]))

        with self.assertRaises(AnsibleExitJson) as result:
            os.environ['RESOURCE_MANAGER_AUTH_TYPE'] = 'noAuth'
            ibm_resource_quotas_info.main()

        self.assertEqual(result.exception.args[0].get("resources"), [])

        self.list_mock.assert_called_once()

    @mock_operations
    def test_list_ibm_resource_quotas_failed(self):
        """Test the "list" path - failed."""
        self.list_mock.side_effect = ApiException(400, message='List ibm_resource_quotas error')

        with self.assertRaises(AnsibleFailJson) as result:
            os.environ['RESOURCE_MANAGER_AUTH_TYPE'] = 'noAuth'
            ibm_resource_quotas_info.main()

        self.assertEqual(result.exception.args[0]['msg'], 'List ibm_resource_quotas error')

        self.list_mock.assert_called_once()
