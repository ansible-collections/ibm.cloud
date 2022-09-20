# (C) Copyright IBM Corp. 2022.
# GNU General Public License v3.0+ (see LICENSE or https://www.gnu.org/licenses/gpl-3.0.txt)


import os

from ibm_cloud_sdk_core import ApiException
from ansible_collections.community.internal_test_tools.tests.unit.compat.mock import patch
from ansible_collections.community.internal_test_tools.tests.unit.plugins.modules.utils import ModuleTestCase, AnsibleFailJson, AnsibleExitJson, set_module_args

from .common import DetailedResponseMock
from plugins.modules import ibm_iam_access_groups_info


class TestGroupsListModuleInfo(ModuleTestCase):
    """
    Test class for GroupsList module testing.
    """

    def test_list_ibm_iam_access_groups_success(self):
        """Test the "list" path - successful."""
        patcher = patch(
            'plugins.modules.ibm_iam_access_groups_info.IamAccessGroupsV2.list_access_groups')
        mock = patcher.start()
        mock.return_value = DetailedResponseMock([])

        set_module_args({
            'account_id': 'testString',
            'transaction_id': 'testString',
            'iam_id': 'testString',
            'limit': 38,
            'offset': 38,
            'sort': 'name',
            'show_federated': False,
            'hide_public_access': False,
        })

        with self.assertRaises(AnsibleExitJson) as result:
            os.environ['IAM_ACCESS_GROUPS_AUTH_TYPE'] = 'noAuth'
            os.environ['IC_API_KEY'] = 'noAuthAPIKey'
            ibm_iam_access_groups_info.main()

        assert result.exception.args[0]['msg'] == []

        mock.assert_called_once()

        patcher.stop()

    def test_list_ibm_iam_access_groups_failed(self):
        """Test the "list" path - failed."""
        patcher = patch(
            'plugins.modules.ibm_iam_access_groups_info.IamAccessGroupsV2.list_access_groups')
        mock = patcher.start()
        mock.side_effect = ApiException(
            400, message='List ibm_iam_access_groups error')

        set_module_args({
            'account_id': 'testString',
            'transaction_id': 'testString',
            'iam_id': 'testString',
            'limit': 38,
            'offset': 38,
            'sort': 'name',
            'show_federated': False,
            'hide_public_access': False,
        })

        with self.assertRaises(AnsibleFailJson) as result:
            os.environ['IAM_ACCESS_GROUPS_AUTH_TYPE'] = 'noAuth'
            os.environ['IC_API_KEY'] = 'noAuthAPIKey'
            ibm_iam_access_groups_info.main()

        assert result.exception.args[0]['msg'] == 'List ibm_iam_access_groups error'

        mock.assert_called_once()

        patcher.stop()
