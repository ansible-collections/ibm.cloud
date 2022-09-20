# (C) Copyright IBM Corp. 2022.
# GNU General Public License v3.0+ (see LICENSE or https://www.gnu.org/licenses/gpl-3.0.txt)


import os

from ibm_cloud_sdk_core import ApiException
from ansible_collections.community.internal_test_tools.tests.unit.compat.mock import patch
from ansible_collections.community.internal_test_tools.tests.unit.plugins.modules.utils import ModuleTestCase, AnsibleFailJson, AnsibleExitJson, set_module_args

from .common import DetailedResponseMock
from plugins.modules import ibm_iam_access_group_info


class TestGroupModuleInfo(ModuleTestCase):
    """
    Test class for Group module testing.
    """

    def test_read_ibm_iam_access_group_success(self):
        """Test the "read" path - successful."""
        datasource = {
            'access_group_id': 'testString',
            'transaction_id': 'testString',
            'show_federated': False,
        }

        patcher = patch(
            'plugins.modules.ibm_iam_access_group_info.IamAccessGroupsV2.get_access_group')
        mock = patcher.start()
        mock.return_value = DetailedResponseMock(datasource)

        set_module_args({
            'access_group_id': 'testString',
            'transaction_id': 'testString',
            'show_federated': False,
        })

        with self.assertRaises(AnsibleExitJson) as result:
            os.environ['IAM_ACCESS_GROUPS_AUTH_TYPE'] = 'noAuth'
            os.environ['IC_API_KEY'] = 'noAuthAPIKey'
            ibm_iam_access_group_info.main()

        assert result.exception.args[0]['msg'] == datasource

        mock.assert_called_once_with(
            access_group_id='testString',
            transaction_id='testString',
            show_federated=False,
        )

        patcher.stop()

    def test_read_ibm_iam_access_group_failed(self):
        """Test the "read" path - failed."""
        patcher = patch(
            'plugins.modules.ibm_iam_access_group_info.IamAccessGroupsV2.get_access_group')
        mock = patcher.start()
        mock.side_effect = ApiException(
            400, message='Read ibm_iam_access_group error')

        set_module_args({
            'access_group_id': 'testString',
            'transaction_id': 'testString',
            'show_federated': False,
        })

        with self.assertRaises(AnsibleFailJson) as result:
            os.environ['IAM_ACCESS_GROUPS_AUTH_TYPE'] = 'noAuth'
            os.environ['IC_API_KEY'] = 'noAuthAPIKey'
            ibm_iam_access_group_info.main()

        assert result.exception.args[0]['msg'] == 'Read ibm_iam_access_group error'

        mock.assert_called_once_with(
            access_group_id='testString',
            transaction_id='testString',
            show_federated=False,
        )

        patcher.stop()
