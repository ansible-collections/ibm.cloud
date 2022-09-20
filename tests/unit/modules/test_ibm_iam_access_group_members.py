# (C) Copyright IBM Corp. 2022.
# GNU General Public License v3.0+ (see LICENSE or https://www.gnu.org/licenses/gpl-3.0.txt)


import os

from ibm_cloud_sdk_core import ApiException
from ansible_collections.community.internal_test_tools.tests.unit.compat.mock import patch
from ansible_collections.community.internal_test_tools.tests.unit.plugins.modules.utils import ModuleTestCase, AnsibleFailJson, AnsibleExitJson, set_module_args

from .common import DetailedResponseMock
from plugins.modules import ibm_iam_access_group_members


def post_process_result(expected: dict, result: dict) -> dict:
    """Removes implicitly added items by Ansible.

    Args:
        expected: the expected results
        result: the actual ressult
    Returns:
        A cleaned dictionary.
    """

    new_result = {}

    for res_key, res_value in result.items():
        try:
            mock_value = expected[res_key]
        except KeyError:
            # If this key not presented in the expected dictionary and its value is None
            # we can ignore it, since it supposed to be an implicitly added item by Ansible.
            if res_value is None:
                continue

            new_result[res_key] = res_value
        else:
            # We need to recursively check nested dictionaries as well.
            if isinstance(res_value, dict):
                new_result[res_key] = post_process_result(
                    mock_value, res_value)
            # Just like lists.
            elif isinstance(res_value, list) and len(res_value) > 0:
                # We use an inner function for recursive list processing.
                def process_list(m: list, r: list) -> list:
                    # Create a new list that we will return at the end of this function.
                    # We will check, process then add each elements one by one.
                    new_list = []
                    for mock_elem, res_elem in zip(m, r):
                        # If both items are dict use the outer function to process them.
                        if isinstance(mock_elem, dict) and isinstance(res_elem, dict):
                            new_list.append(
                                post_process_result(mock_elem, res_elem))
                        # If both items are list, use this function to process them.
                        elif isinstance(mock_elem, list) and isinstance(res_elem, list):
                            new_list.append(process_list(mock_elem, res_elem))
                        # Otherwise just add it to the new list, but only if both items have
                        # the same type. Otherwise do nothing, since it's and invalid scenario.
                        elif isinstance(mock_elem, type(res_elem)):
                            new_list.append(res_elem)

                    return new_list

                new_result[res_key] = process_list(mock_value, res_value)
            # This should be a simple value, so let's use it as is.
            else:
                new_result[res_key] = res_value

    return new_result


class TestAddGroupMembersResponseModule(ModuleTestCase):
    """
    Test class for AddGroupMembersResponse module testing.
    """

    # def test_read_ibm_iam_access_group_members_failed(self):
    #     """Test the inner "read" path in this module with a server error response."""

    #     patcher = patch(
    #         'plugins.modules.ibm_iam_access_group_members.IamAccessGroupsV2.list_access_group_members')
    #     mock = patcher.start()
    #     print("*****[ApiException]*****")
    #     mock.side_effect = ApiException(500, message='Something went wrong...')

    #     set_module_args({
    #         'access_group_id': 'testString',
    #         'transaction_id': 'testString',
    #         'limit': 38,
    #         'offset': 38,
    #         'type': 'testString',
    #         'verbose': False,
    #         'sort': 'testString',
    #     })

    #     with self.assertRaises(AnsibleFailJson) as result:
    #         os.environ['IAM_ACCESS_GROUPS_AUTH_TYPE'] = 'noAuth'
    #         os.environ['IC_API_KEY'] = 'noAuthAPIKey'
    #         ibm_iam_access_group_members.main()

    #     assert result.exception.args[0]['msg'] == 'Something went wrong...'

    #     mock_data = dict(
    #         access_group_id='testString',
    #         transaction_id='testString',
    #         limit=38,
    #         offset=38,
    #         type='testString',
    #         verbose=False,
    #         sort='testString',
    #     )

    #     mock.assert_called_once()
    #     processed_result = post_process_result(
    #         mock_data, mock.call_args.kwargs)
    #     assert mock_data == processed_result

    #     patcher.stop()

    def test_create_ibm_iam_access_group_members_success(self):
        """Test the "create" path - successful."""
        add_group_members_request_members_item_model = {
            'iam_id': 'IBMid-user1',
            'type': 'user',
        }

        resource = {
            'access_group_id': 'testString',
            'members': [add_group_members_request_members_item_model],
            'transaction_id': 'testString',
        }

        patcher = patch(
            'plugins.modules.ibm_iam_access_group_members.IamAccessGroupsV2.add_members_to_access_group')
        mock = patcher.start()
        mock.return_value = DetailedResponseMock(resource)

        list_access_group_members_patcher = patch(
            'plugins.modules.ibm_iam_access_group_members.IamAccessGroupsV2.list_access_group_members')
        list_access_group_members_mock = list_access_group_members_patcher.start()

        set_module_args({
            'access_group_id': 'testString',
            'members': [add_group_members_request_members_item_model],
            'transaction_id': 'testString',
        })

        with self.assertRaises(AnsibleExitJson) as result:
            os.environ['IAM_ACCESS_GROUPS_AUTH_TYPE'] = 'noAuth'
            os.environ['IC_API_KEY'] = 'noAuthAPIKey'
            ibm_iam_access_group_members.main()

        assert result.exception.args[0]['changed'] is True
        assert result.exception.args[0]['msg'] == resource

        mock_data = dict(
            access_group_id='testString',
            members=[add_group_members_request_members_item_model],
            transaction_id='testString',
        )

        mock.assert_called_once()
        processed_result = post_process_result(
            mock_data, mock.call_args.kwargs)
        assert mock_data == processed_result

        list_access_group_members_mock.assert_not_called()

        list_access_group_members_patcher.stop()
        patcher.stop()

    def test_create_ibm_iam_access_group_members_failed(self):
        """Test the "create" path - failed."""

        list_access_group_members_patcher = patch(
            'plugins.modules.ibm_iam_access_group_members.IamAccessGroupsV2.list_access_group_members')
        list_access_group_members_mock = list_access_group_members_patcher.start()

        patcher = patch(
            'plugins.modules.ibm_iam_access_group_members.IamAccessGroupsV2.add_members_to_access_group')
        mock = patcher.start()
        mock.side_effect = ApiException(
            400, message='Create ibm_iam_access_group_members error')

        add_group_members_request_members_item_model = {
            'iam_id': 'IBMid-user1',
            'type': 'user',
        }

        set_module_args({
            'access_group_id': 'testString',
            'members': [add_group_members_request_members_item_model],
            'transaction_id': 'testString',
        })

        with self.assertRaises(AnsibleFailJson) as result:
            os.environ['IAM_ACCESS_GROUPS_AUTH_TYPE'] = 'noAuth'
            os.environ['IC_API_KEY'] = 'noAuthAPIKey'
            ibm_iam_access_group_members.main()

        assert result.exception.args[0]['msg'] == 'Create ibm_iam_access_group_members error'

        mock_data = dict(
            access_group_id='testString',
            members=[add_group_members_request_members_item_model],
            transaction_id='testString',
        )

        mock.assert_called_once()
        processed_result = post_process_result(
            mock_data, mock.call_args.kwargs)
        assert mock_data == processed_result

        list_access_group_members_mock.assert_not_called()

        list_access_group_members_patcher.stop()
        patcher.stop()

    # def test_update_ibm_iam_access_group_members_success(self):
    #     """Test the "update" path - successful."""
    #     add_group_members_request_members_item_model = {
    #         'iam_id': 'IBMid-user1',
    #         'type': 'user',
    #     }

    #     resource = {
    #         'access_group_id': 'testString',
    #         'members': [add_group_members_request_members_item_model],
    #         'transaction_id': 'testString',
    #     }

    #     patcher = patch(
    #         'plugins.modules.ibm_iam_access_group_members.IamAccessGroupsV2.add_members_to_access_group')
    #     mock = patcher.start()
    #     mock.return_value = DetailedResponseMock(resource)

    #     list_access_group_members_patcher = patch(
    #         'plugins.modules.ibm_iam_access_group_members.IamAccessGroupsV2.list_access_group_members')
    #     list_access_group_members_mock = list_access_group_members_patcher.start()
    #     list_access_group_members_mock.return_value = DetailedResponseMock(
    #         resource)

    #     set_module_args({
    #         'access_group_id': 'testString',
    #         'members': [add_group_members_request_members_item_model],
    #         'transaction_id': 'testString',
    #     })

    #     with self.assertRaises(AnsibleExitJson) as result:
    #         os.environ['IAM_ACCESS_GROUPS_AUTH_TYPE'] = 'noAuth'
    #         os.environ['IC_API_KEY'] = 'noAuthAPIKey'
    #         ibm_iam_access_group_members.main()

    #     assert result.exception.args[0]['changed'] is True
    #     assert result.exception.args[0]['msg'] == resource

    #     mock_data = dict(
    #         access_group_id='testString',
    #         members=[add_group_members_request_members_item_model],
    #         transaction_id='testString',
    #     )

    #     mock.assert_called_once()
    #     processed_result = post_process_result(
    #         mock_data, mock.call_args.kwargs)
    #     assert mock_data == processed_result

    #     list_access_group_members_mock_data = dict(
    #         access_group_id='testString',
    #         transaction_id='testString',
    #         limit=38,
    #         offset=38,
    #         type='testString',
    #         verbose=False,
    #         sort='testString',
    #     )
    #     # Set the variables that belong to the "read" path to `None`
    #     # since we test the "delete" path here.
    #     for param in list_access_group_members_mock_data:
    #         list_access_group_members_mock_data[param] = mock_data.get(
    #             param, None)

    #     list_access_group_members_mock.assert_called_once()
    #     list_access_group_members_processed_result = post_process_result(
    #         list_access_group_members_mock_data, list_access_group_members_mock.call_args.kwargs)
    #     assert list_access_group_members_mock_data == list_access_group_members_processed_result
    #     list_access_group_members_patcher.stop()
    #     patcher.stop()

    # def test_update_ibm_iam_access_group_members_failed(self):
    #     """Test the "update" path - failed."""
    #     add_group_members_request_members_item_model = {
    #         'iam_id': 'IBMid-user1',
    #         'type': 'user',
    #     }

    #     resource = {
    #         'access_group_id': 'testString',
    #         'members': [add_group_members_request_members_item_model],
    #         'transaction_id': 'testString',
    #     }

    #     patcher = patch(
    #         'plugins.modules.ibm_iam_access_group_members.IamAccessGroupsV2.add_members_to_access_group')
    #     mock = patcher.start()
    #     mock.side_effect = ApiException(
    #         400, message='Update ibm_iam_access_group_members error')

    #     list_access_group_members_patcher = patch(
    #         'plugins.modules.ibm_iam_access_group_members.IamAccessGroupsV2.list_access_group_members')
    #     list_access_group_members_mock = list_access_group_members_patcher.start()
    #     list_access_group_members_mock.return_value = DetailedResponseMock(
    #         resource)

    #     set_module_args({
    #         'access_group_id': 'testString',
    #         'members': [add_group_members_request_members_item_model],
    #         'transaction_id': 'testString',
    #     })

    #     with self.assertRaises(AnsibleFailJson) as result:
    #         os.environ['IAM_ACCESS_GROUPS_AUTH_TYPE'] = 'noAuth'
    #         os.environ['IC_API_KEY'] = 'noAuthAPIKey'
    #         ibm_iam_access_group_members.main()

    #     assert result.exception.args[0]['msg'] == 'Update ibm_iam_access_group_members error'

    #     mock_data = dict(
    #         access_group_id='testString',
    #         members=[add_group_members_request_members_item_model],
    #         transaction_id='testString',
    #     )

    #     mock.assert_called_once()
    #     processed_result = post_process_result(
    #         mock_data, mock.call_args.kwargs)
    #     assert mock_data == processed_result

    #     list_access_group_members_mock_data = dict(
    #         access_group_id='testString',
    #         transaction_id='testString',
    #         limit=38,
    #         offset=38,
    #         type='testString',
    #         verbose=False,
    #         sort='testString',
    #     )
    #     # Set the variables that belong to the "read" path to `None`
    #     # since we test the "delete" path here.
    #     for param in list_access_group_members_mock_data:
    #         list_access_group_members_mock_data[param] = mock_data.get(
    #             param, None)

    #     list_access_group_members_mock.assert_called_once()
    #     list_access_group_members_processed_result = post_process_result(
    #         list_access_group_members_mock_data, list_access_group_members_mock.call_args.kwargs)
    #     assert list_access_group_members_mock_data == list_access_group_members_processed_result

    #     list_access_group_members_patcher.stop()
    #     patcher.stop()

    def test_delete_ibm_iam_access_group_members_success(self):
        """Test the "delete" path - successfull."""
        patcher = patch(
            'plugins.modules.ibm_iam_access_group_members.IamAccessGroupsV2.remove_member_from_access_group')
        mock = patcher.start()
        mock.return_value = DetailedResponseMock()

        list_access_group_members_patcher = patch(
            'plugins.modules.ibm_iam_access_group_members.IamAccessGroupsV2.list_access_group_members')
        list_access_group_members_mock = list_access_group_members_patcher.start()
        list_access_group_members_mock.return_value = DetailedResponseMock()

        args = {
            'access_group_id': 'testString',
            'iam_id': 'testString',
            'transaction_id': 'testString',
            'state': 'absent',
        }

        set_module_args(args)

        with self.assertRaises(AnsibleExitJson) as result:
            os.environ['IAM_ACCESS_GROUPS_AUTH_TYPE'] = 'noAuth'
            os.environ['IC_API_KEY'] = 'noAuthAPIKey'
            ibm_iam_access_group_members.main()

        assert result.exception.args[0]['changed'] is True
        assert result.exception.args[0]['msg']['id'] == 'testString'
        assert result.exception.args[0]['msg']['status'] == 'deleted'

        mock_data = dict(
            access_group_id='testString',
            iam_id='testString',
            transaction_id='testString',
        )

        mock.assert_called_once()
        processed_result = post_process_result(
            mock_data, mock.call_args.kwargs)
        assert mock_data == processed_result

        list_access_group_members_mock_data = dict(
            access_group_id='testString',
            transaction_id='testString',
            limit=38,
            offset=38,
            type='testString',
            verbose=False,
            sort='testString',
        )
        # Set the variables that belong to the "read" path to `None`
        # since we test the "delete" path here.
        for param in list_access_group_members_mock_data:
            list_access_group_members_mock_data[param] = mock_data.get(
                param, None)

        list_access_group_members_mock.assert_called_once()
        list_access_group_members_processed_result = post_process_result(
            list_access_group_members_mock_data, list_access_group_members_mock.call_args.kwargs)
        assert list_access_group_members_mock_data == list_access_group_members_processed_result

        list_access_group_members_patcher.stop()
        patcher.stop()

    def test_delete_ibm_iam_access_group_members_not_exists(self):
        """Test the "delete" path - not exists."""
        patcher = patch(
            'plugins.modules.ibm_iam_access_group_members.IamAccessGroupsV2.remove_member_from_access_group')
        mock = patcher.start()
        mock.return_value = DetailedResponseMock()

        list_access_group_members_patcher = patch(
            'plugins.modules.ibm_iam_access_group_members.IamAccessGroupsV2.list_access_group_members')
        list_access_group_members_mock = list_access_group_members_patcher.start()
        list_access_group_members_mock.side_effect = ApiException(404)

        args = {
            'access_group_id': 'testString',
            'iam_id': 'testString',
            'transaction_id': 'testString',
            'state': 'absent',
        }

        set_module_args(args)

        with self.assertRaises(AnsibleExitJson) as result:
            os.environ['IAM_ACCESS_GROUPS_AUTH_TYPE'] = 'noAuth'
            os.environ['IC_API_KEY'] = 'noAuthAPIKey'
            ibm_iam_access_group_members.main()

        assert result.exception.args[0]['changed'] is False
        assert result.exception.args[0]['msg']['id'] == 'testString'
        assert result.exception.args[0]['msg']['status'] == 'not_found'

        mock_data = dict(
            access_group_id='testString',
            iam_id='testString',
            transaction_id='testString',
        )

        mock.assert_not_called()

        list_access_group_members_mock_data = dict(
            access_group_id='testString',
            transaction_id='testString',
            limit=38,
            offset=38,
            type='testString',
            verbose=False,
            sort='testString',
        )
        # Set the variables that belong to the "read" path to `None`
        # since we test the "delete" path here.
        for param in list_access_group_members_mock_data:
            list_access_group_members_mock_data[param] = mock_data.get(
                param, None)

        list_access_group_members_mock.assert_called_once()
        list_access_group_members_processed_result = post_process_result(
            list_access_group_members_mock_data, list_access_group_members_mock.call_args.kwargs)
        assert list_access_group_members_mock_data == list_access_group_members_processed_result

        list_access_group_members_patcher.stop()
        patcher.stop()

    def test_delete_ibm_iam_access_group_members_failed(self):
        """Test the "delete" path - failed."""
        patcher = patch(
            'plugins.modules.ibm_iam_access_group_members.IamAccessGroupsV2.remove_member_from_access_group')
        mock = patcher.start()
        mock.side_effect = ApiException(
            400, message='Delete ibm_iam_access_group_members error')

        list_access_group_members_patcher = patch(
            'plugins.modules.ibm_iam_access_group_members.IamAccessGroupsV2.list_access_group_members')
        list_access_group_members_mock = list_access_group_members_patcher.start()
        list_access_group_members_mock.return_value = DetailedResponseMock()

        set_module_args({
            'access_group_id': 'testString',
            'iam_id': 'testString',
            'transaction_id': 'testString',
            'state': 'absent',
        })

        with self.assertRaises(AnsibleFailJson) as result:
            os.environ['IAM_ACCESS_GROUPS_AUTH_TYPE'] = 'noAuth'
            os.environ['IC_API_KEY'] = 'noAuthAPIKey'
            ibm_iam_access_group_members.main()

        assert result.exception.args[0]['msg'] == 'Delete ibm_iam_access_group_members error'

        mock_data = dict(
            access_group_id='testString',
            iam_id='testString',
            transaction_id='testString',
        )

        mock.assert_called_once()
        processed_result = post_process_result(
            mock_data, mock.call_args.kwargs)
        assert mock_data == processed_result

        list_access_group_members_mock_data = dict(
            access_group_id='testString',
            transaction_id='testString',
            limit=38,
            offset=38,
            type='testString',
            verbose=False,
            sort='testString',
        )
        # Set the variables that belong to the "read" path to `None`
        # since we test the "delete" path here.
        for param in list_access_group_members_mock_data:
            list_access_group_members_mock_data[param] = mock_data.get(
                param, None)

        list_access_group_members_mock.assert_called_once()
        list_access_group_members_processed_result = post_process_result(
            list_access_group_members_mock_data, list_access_group_members_mock.call_args.kwargs)
        assert list_access_group_members_mock_data == list_access_group_members_processed_result

        list_access_group_members_patcher.stop()
        patcher.stop()
