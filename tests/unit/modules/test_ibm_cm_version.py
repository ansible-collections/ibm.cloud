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
from plugins.modules import ibm_cm_version


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


class TestVersionModule(ModuleTestCase):
    """
    Test class for Version module testing.
    """

    def test_read_ibm_cm_version_failed(self):
        """Test the inner "read" path in this module with a server error response."""

        patcher = patch(
            'plugins.modules.ibm_cm_version.CatalogManagementV1.get_version')
        mock = patcher.start()
        mock.side_effect = ApiException(500, message='Something went wrong...')

        set_module_args({
            'version_loc_id': 'testString',
        })

        with self.assertRaises(AnsibleFailJson) as result:
            os.environ['CATALOG_MANAGEMENT_AUTH_TYPE'] = 'noAuth'
            os.environ['IC_API_KEY'] = 'noAuthAPIKey'
            ibm_cm_version.main()

        assert result.exception.args[0]['msg'] == 'Something went wrong...'

        mock_data = dict(
            version_loc_id='testString',
        )

        mock.assert_called_once()
        processed_result = post_process_result(
            mock_data, mock.call_args.kwargs)
        assert mock_data == processed_result

        patcher.stop()

    def test_create_ibm_cm_version_success(self):
        """Test the "create" path - successful."""
        resource = {
            'catalog_identifier': 'testString',
            'offering_id': 'testString',
            'tags': ['testString'],
            'target_kinds': ['testString'],
            'content': 'VGhpcyBpcyBhIG1vY2sgYnl0ZSBhcnJheSB2YWx1ZS4=',
            'zipurl': 'testString',
            'target_version': 'testString',
            'include_config': True,
            'is_vsi': True,
            'repo_type': 'testString',
        }

        patcher = patch(
            'plugins.modules.ibm_cm_version.CatalogManagementV1.import_offering_version')
        mock = patcher.start()
        mock.return_value = DetailedResponseMock(resource)

        get_version_patcher = patch(
            'plugins.modules.ibm_cm_version.CatalogManagementV1.get_version')
        get_version_mock = get_version_patcher.start()

        set_module_args({
            'catalog_identifier': 'testString',
            'offering_id': 'testString',
            'tags': ['testString'],
            'target_kinds': ['testString'],
            'content': 'VGhpcyBpcyBhIG1vY2sgYnl0ZSBhcnJheSB2YWx1ZS4=',
            'zipurl': 'testString',
            'target_version': 'testString',
            'include_config': True,
            'is_vsi': True,
            'repo_type': 'testString',
        })

        with self.assertRaises(AnsibleExitJson) as result:
            os.environ['CATALOG_MANAGEMENT_AUTH_TYPE'] = 'noAuth'
            os.environ['IC_API_KEY'] = 'noAuthAPIKey'
            ibm_cm_version.main()

        assert result.exception.args[0]['changed'] is True
        assert result.exception.args[0]['msg'] == resource

        mock_data = dict(
            catalog_identifier='testString',
            offering_id='testString',
            tags=['testString'],
            target_kinds=['testString'],
            content=b'This is a mock byte array value.',
            zipurl='testString',
            target_version='testString',
            include_config=True,
            is_vsi=True,
            repo_type='testString',
        )

        mock.assert_called_once()
        processed_result = post_process_result(
            mock_data, mock.call_args.kwargs)
        assert mock_data == processed_result

        get_version_mock.assert_not_called()

        get_version_patcher.stop()
        patcher.stop()

    def test_create_ibm_cm_version_failed(self):
        """Test the "create" path - failed."""

        get_version_patcher = patch(
            'plugins.modules.ibm_cm_version.CatalogManagementV1.get_version')
        get_version_mock = get_version_patcher.start()

        patcher = patch(
            'plugins.modules.ibm_cm_version.CatalogManagementV1.import_offering_version')
        mock = patcher.start()
        mock.side_effect = ApiException(
            400, message='Create ibm_cm_version error')

        set_module_args({
            'catalog_identifier': 'testString',
            'offering_id': 'testString',
            'tags': ['testString'],
            'target_kinds': ['testString'],
            'content': 'VGhpcyBpcyBhIG1vY2sgYnl0ZSBhcnJheSB2YWx1ZS4=',
            'zipurl': 'testString',
            'target_version': 'testString',
            'include_config': True,
            'is_vsi': True,
            'repo_type': 'testString',
        })

        with self.assertRaises(AnsibleFailJson) as result:
            os.environ['CATALOG_MANAGEMENT_AUTH_TYPE'] = 'noAuth'
            os.environ['IC_API_KEY'] = 'noAuthAPIKey'
            ibm_cm_version.main()

        assert result.exception.args[0]['msg'] == 'Create ibm_cm_version error'

        mock_data = dict(
            catalog_identifier='testString',
            offering_id='testString',
            tags=['testString'],
            target_kinds=['testString'],
            content=b'This is a mock byte array value.',
            zipurl='testString',
            target_version='testString',
            include_config=True,
            is_vsi=True,
            repo_type='testString',
        )

        mock.assert_called_once()
        processed_result = post_process_result(
            mock_data, mock.call_args.kwargs)
        assert mock_data == processed_result

        get_version_mock.assert_not_called()

        get_version_patcher.stop()
        patcher.stop()

    def test_delete_ibm_cm_version_success(self):
        """Test the "delete" path - successfull."""
        patcher = patch(
            'plugins.modules.ibm_cm_version.CatalogManagementV1.delete_version')
        mock = patcher.start()
        mock.return_value = DetailedResponseMock()

        get_version_patcher = patch(
            'plugins.modules.ibm_cm_version.CatalogManagementV1.get_version')
        get_version_mock = get_version_patcher.start()
        get_version_mock.return_value = DetailedResponseMock()

        args = {
            'version_loc_id': 'testString',
            'state': 'absent',
        }

        set_module_args(args)

        with self.assertRaises(AnsibleExitJson) as result:
            os.environ['CATALOG_MANAGEMENT_AUTH_TYPE'] = 'noAuth'
            os.environ['IC_API_KEY'] = 'noAuthAPIKey'
            ibm_cm_version.main()

        assert result.exception.args[0]['changed'] is True
        assert result.exception.args[0]['msg']['id'] == 'testString'
        assert result.exception.args[0]['msg']['status'] == 'deleted'

        mock_data = dict(
            version_loc_id='testString',
        )

        mock.assert_called_once()
        processed_result = post_process_result(
            mock_data, mock.call_args.kwargs)
        assert mock_data == processed_result

        get_version_mock_data = dict(
            version_loc_id='testString',
        )
        # Set the variables that belong to the "read" path to `None`
        # since we test the "delete" path here.
        for param in get_version_mock_data:
            get_version_mock_data[param] = mock_data.get(param, None)

        get_version_mock.assert_called_once()
        get_version_processed_result = post_process_result(
            get_version_mock_data, get_version_mock.call_args.kwargs)
        assert get_version_mock_data == get_version_processed_result

        get_version_patcher.stop()
        patcher.stop()

    def test_delete_ibm_cm_version_not_exists(self):
        """Test the "delete" path - not exists."""
        patcher = patch(
            'plugins.modules.ibm_cm_version.CatalogManagementV1.delete_version')
        mock = patcher.start()
        mock.return_value = DetailedResponseMock()

        get_version_patcher = patch(
            'plugins.modules.ibm_cm_version.CatalogManagementV1.get_version')
        get_version_mock = get_version_patcher.start()
        get_version_mock.side_effect = ApiException(404)

        args = {
            'version_loc_id': 'testString',
            'state': 'absent',
        }

        set_module_args(args)

        with self.assertRaises(AnsibleExitJson) as result:
            os.environ['CATALOG_MANAGEMENT_AUTH_TYPE'] = 'noAuth'
            os.environ['IC_API_KEY'] = 'noAuthAPIKey'
            ibm_cm_version.main()

        assert result.exception.args[0]['changed'] is False
        assert result.exception.args[0]['msg']['id'] == 'testString'
        assert result.exception.args[0]['msg']['status'] == 'not_found'

        mock_data = dict(
            version_loc_id='testString',
        )

        mock.assert_not_called()

        get_version_mock_data = dict(
            version_loc_id='testString',
        )
        # Set the variables that belong to the "read" path to `None`
        # since we test the "delete" path here.
        for param in get_version_mock_data:
            get_version_mock_data[param] = mock_data.get(param, None)

        get_version_mock.assert_called_once()
        get_version_processed_result = post_process_result(
            get_version_mock_data, get_version_mock.call_args.kwargs)
        assert get_version_mock_data == get_version_processed_result

        get_version_patcher.stop()
        patcher.stop()

    def test_delete_ibm_cm_version_failed(self):
        """Test the "delete" path - failed."""
        patcher = patch(
            'plugins.modules.ibm_cm_version.CatalogManagementV1.delete_version')
        mock = patcher.start()
        mock.side_effect = ApiException(
            400, message='Delete ibm_cm_version error')

        get_version_patcher = patch(
            'plugins.modules.ibm_cm_version.CatalogManagementV1.get_version')
        get_version_mock = get_version_patcher.start()
        get_version_mock.return_value = DetailedResponseMock()

        set_module_args({
            'version_loc_id': 'testString',
            'state': 'absent',
        })

        with self.assertRaises(AnsibleFailJson) as result:
            os.environ['CATALOG_MANAGEMENT_AUTH_TYPE'] = 'noAuth'
            os.environ['IC_API_KEY'] = 'noAuthAPIKey'
            ibm_cm_version.main()

        assert result.exception.args[0]['msg'] == 'Delete ibm_cm_version error'

        mock_data = dict(
            version_loc_id='testString',
        )

        mock.assert_called_once()
        processed_result = post_process_result(
            mock_data, mock.call_args.kwargs)
        assert mock_data == processed_result

        get_version_mock_data = dict(
            version_loc_id='testString',
        )
        # Set the variables that belong to the "read" path to `None`
        # since we test the "delete" path here.
        for param in get_version_mock_data:
            get_version_mock_data[param] = mock_data.get(param, None)

        get_version_mock.assert_called_once()
        get_version_processed_result = post_process_result(
            get_version_mock_data, get_version_mock.call_args.kwargs)
        assert get_version_mock_data == get_version_processed_result

        get_version_patcher.stop()
        patcher.stop()
