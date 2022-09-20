# (C) Copyright IBM Corp. 2022.
# GNU General Public License v3.0+ (see LICENSE or https://www.gnu.org/licenses/gpl-3.0.txt)


import os

from ibm_cloud_sdk_core import ApiException
from ansible_collections.community.internal_test_tools.tests.unit.compat.mock import patch
from ansible_collections.community.internal_test_tools.tests.unit.plugins.modules.utils import ModuleTestCase, AnsibleFailJson, AnsibleExitJson, set_module_args

from .common import DetailedResponseMock
from plugins.modules import ibm_resource_alias


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


class TestResourceAliasPostModule(ModuleTestCase):
    """
    Test class for ResourceAliasPost module testing.
    """

    def test_read_ibm_resource_alias_failed(self):
        """Test the inner "read" path in this module with a server error response."""

        patcher = patch(
            'plugins.modules.ibm_resource_alias.ResourceControllerV2.get_resource_alias')
        mock = patcher.start()
        mock.side_effect = ApiException(500, message='Something went wrong...')

        set_module_args({
            'id': 'testString',
        })

        with self.assertRaises(AnsibleFailJson) as result:
            os.environ['RESOURCE_CONTROLLER_AUTH_TYPE'] = 'noAuth'
            os.environ['IC_API_KEY'] = 'noAuthAPIKey'
            ibm_resource_alias.main()

        assert result.exception.args[0]['msg'] == 'Something went wrong...'

        mock_data = dict(
            id='testString',
        )

        mock.assert_called_once()
        processed_result = post_process_result(
            mock_data, mock.call_args.kwargs)
        assert mock_data == processed_result

        patcher.stop()

    def test_create_ibm_resource_alias_success(self):
        """Test the "create" path - successful."""
        resource = {
            'name': 'my-alias',
            'source': 'a8dff6d3-d287-4668-a81d-c87c55c2656d',
            'target': 'crn:v1:bluemix:public:cf:us-south:o/5e939cd5-6377-4383-b9e0-9db22cd11753::cf-space:66c8b915-101a-406c-a784-e6636676e4f5',
        }

        patcher = patch(
            'plugins.modules.ibm_resource_alias.ResourceControllerV2.create_resource_alias')
        mock = patcher.start()
        mock.return_value = DetailedResponseMock(resource)

        get_resource_alias_patcher = patch(
            'plugins.modules.ibm_resource_alias.ResourceControllerV2.get_resource_alias')
        get_resource_alias_mock = get_resource_alias_patcher.start()

        set_module_args({
            'name': 'my-alias',
            'source': 'a8dff6d3-d287-4668-a81d-c87c55c2656d',
            'target': 'crn:v1:bluemix:public:cf:us-south:o/5e939cd5-6377-4383-b9e0-9db22cd11753::cf-space:66c8b915-101a-406c-a784-e6636676e4f5',
        })

        with self.assertRaises(AnsibleExitJson) as result:
            os.environ['RESOURCE_CONTROLLER_AUTH_TYPE'] = 'noAuth'
            os.environ['IC_API_KEY'] = 'noAuthAPIKey'
            ibm_resource_alias.main()

        assert result.exception.args[0]['changed'] is True
        assert result.exception.args[0]['msg'] == resource

        mock_data = dict(
            name='my-alias',
            source='a8dff6d3-d287-4668-a81d-c87c55c2656d',
            target='crn:v1:bluemix:public:cf:us-south:o/5e939cd5-6377-4383-b9e0-9db22cd11753::cf-space:66c8b915-101a-406c-a784-e6636676e4f5',
        )

        mock.assert_called_once()
        processed_result = post_process_result(
            mock_data, mock.call_args.kwargs)
        assert mock_data == processed_result

        get_resource_alias_mock.assert_not_called()

        get_resource_alias_patcher.stop()
        patcher.stop()

    def test_create_ibm_resource_alias_failed(self):
        """Test the "create" path - failed."""

        get_resource_alias_patcher = patch(
            'plugins.modules.ibm_resource_alias.ResourceControllerV2.get_resource_alias')
        get_resource_alias_mock = get_resource_alias_patcher.start()

        patcher = patch(
            'plugins.modules.ibm_resource_alias.ResourceControllerV2.create_resource_alias')
        mock = patcher.start()
        mock.side_effect = ApiException(
            400, message='Create ibm_resource_alias error')

        set_module_args({
            'name': 'my-alias',
            'source': 'a8dff6d3-d287-4668-a81d-c87c55c2656d',
            'target': 'crn:v1:bluemix:public:cf:us-south:o/5e939cd5-6377-4383-b9e0-9db22cd11753::cf-space:66c8b915-101a-406c-a784-e6636676e4f5',
        })

        with self.assertRaises(AnsibleFailJson) as result:
            os.environ['RESOURCE_CONTROLLER_AUTH_TYPE'] = 'noAuth'
            os.environ['IC_API_KEY'] = 'noAuthAPIKey'
            ibm_resource_alias.main()

        assert result.exception.args[0]['msg'] == 'Create ibm_resource_alias error'

        mock_data = dict(
            name='my-alias',
            source='a8dff6d3-d287-4668-a81d-c87c55c2656d',
            target='crn:v1:bluemix:public:cf:us-south:o/5e939cd5-6377-4383-b9e0-9db22cd11753::cf-space:66c8b915-101a-406c-a784-e6636676e4f5',
        )

        mock.assert_called_once()
        processed_result = post_process_result(
            mock_data, mock.call_args.kwargs)
        assert mock_data == processed_result

        get_resource_alias_mock.assert_not_called()

        get_resource_alias_patcher.stop()
        patcher.stop()

    def test_update_ibm_resource_alias_success(self):
        """Test the "update" path - successful."""
        resource = {
            'id': 'testString',
            'name': 'my-new-alias-name',
        }

        patcher = patch(
            'plugins.modules.ibm_resource_alias.ResourceControllerV2.update_resource_alias')
        mock = patcher.start()
        mock.return_value = DetailedResponseMock(resource)

        get_resource_alias_patcher = patch(
            'plugins.modules.ibm_resource_alias.ResourceControllerV2.get_resource_alias')
        get_resource_alias_mock = get_resource_alias_patcher.start()
        get_resource_alias_mock.return_value = DetailedResponseMock(resource)

        set_module_args({
            'id': 'testString',
            'name': 'my-new-alias-name',
        })

        with self.assertRaises(AnsibleExitJson) as result:
            os.environ['RESOURCE_CONTROLLER_AUTH_TYPE'] = 'noAuth'
            os.environ['IC_API_KEY'] = 'noAuthAPIKey'
            ibm_resource_alias.main()

        assert result.exception.args[0]['changed'] is True
        assert result.exception.args[0]['msg'] == resource

        mock_data = dict(
            id='testString',
            name='my-new-alias-name',
        )

        mock.assert_called_once()
        processed_result = post_process_result(
            mock_data, mock.call_args.kwargs)
        assert mock_data == processed_result

        get_resource_alias_mock_data = dict(
            id='testString',
        )
        # Set the variables that belong to the "read" path to `None`
        # since we test the "delete" path here.
        for param in get_resource_alias_mock_data:
            get_resource_alias_mock_data[param] = mock_data.get(param, None)

        get_resource_alias_mock.assert_called_once()
        get_resource_alias_processed_result = post_process_result(
            get_resource_alias_mock_data, get_resource_alias_mock.call_args.kwargs)
        assert get_resource_alias_mock_data == get_resource_alias_processed_result
        get_resource_alias_patcher.stop()
        patcher.stop()

    def test_update_ibm_resource_alias_failed(self):
        """Test the "update" path - failed."""
        resource = {
            'id': 'testString',
            'name': 'my-new-alias-name',
        }

        patcher = patch(
            'plugins.modules.ibm_resource_alias.ResourceControllerV2.update_resource_alias')
        mock = patcher.start()
        mock.side_effect = ApiException(
            400, message='Update ibm_resource_alias error')

        get_resource_alias_patcher = patch(
            'plugins.modules.ibm_resource_alias.ResourceControllerV2.get_resource_alias')
        get_resource_alias_mock = get_resource_alias_patcher.start()
        get_resource_alias_mock.return_value = DetailedResponseMock(resource)

        set_module_args({
            'id': 'testString',
            'name': 'my-new-alias-name',
        })

        with self.assertRaises(AnsibleFailJson) as result:
            os.environ['RESOURCE_CONTROLLER_AUTH_TYPE'] = 'noAuth'
            os.environ['IC_API_KEY'] = 'noAuthAPIKey'
            ibm_resource_alias.main()

        assert result.exception.args[0]['msg'] == 'Update ibm_resource_alias error'

        mock_data = dict(
            id='testString',
            name='my-new-alias-name',
        )

        mock.assert_called_once()
        processed_result = post_process_result(
            mock_data, mock.call_args.kwargs)
        assert mock_data == processed_result

        get_resource_alias_mock_data = dict(
            id='testString',
        )
        # Set the variables that belong to the "read" path to `None`
        # since we test the "delete" path here.
        for param in get_resource_alias_mock_data:
            get_resource_alias_mock_data[param] = mock_data.get(param, None)

        get_resource_alias_mock.assert_called_once()
        get_resource_alias_processed_result = post_process_result(
            get_resource_alias_mock_data, get_resource_alias_mock.call_args.kwargs)
        assert get_resource_alias_mock_data == get_resource_alias_processed_result

        get_resource_alias_patcher.stop()
        patcher.stop()

    def test_delete_ibm_resource_alias_success(self):
        """Test the "delete" path - successfull."""
        patcher = patch(
            'plugins.modules.ibm_resource_alias.ResourceControllerV2.delete_resource_alias')
        mock = patcher.start()
        mock.return_value = DetailedResponseMock()

        get_resource_alias_patcher = patch(
            'plugins.modules.ibm_resource_alias.ResourceControllerV2.get_resource_alias')
        get_resource_alias_mock = get_resource_alias_patcher.start()
        get_resource_alias_mock.return_value = DetailedResponseMock()

        args = {
            'id': 'testString',
            'state': 'absent',
        }

        set_module_args(args)

        with self.assertRaises(AnsibleExitJson) as result:
            os.environ['RESOURCE_CONTROLLER_AUTH_TYPE'] = 'noAuth'
            os.environ['IC_API_KEY'] = 'noAuthAPIKey'
            ibm_resource_alias.main()

        assert result.exception.args[0]['changed'] is True
        assert result.exception.args[0]['msg']['id'] == 'testString'
        assert result.exception.args[0]['msg']['status'] == 'deleted'

        mock_data = dict(
            id='testString',
        )

        mock.assert_called_once()
        processed_result = post_process_result(
            mock_data, mock.call_args.kwargs)
        assert mock_data == processed_result

        get_resource_alias_mock_data = dict(
            id='testString',
        )
        # Set the variables that belong to the "read" path to `None`
        # since we test the "delete" path here.
        for param in get_resource_alias_mock_data:
            get_resource_alias_mock_data[param] = mock_data.get(param, None)

        get_resource_alias_mock.assert_called_once()
        get_resource_alias_processed_result = post_process_result(
            get_resource_alias_mock_data, get_resource_alias_mock.call_args.kwargs)
        assert get_resource_alias_mock_data == get_resource_alias_processed_result

        get_resource_alias_patcher.stop()
        patcher.stop()

    def test_delete_ibm_resource_alias_not_exists(self):
        """Test the "delete" path - not exists."""
        patcher = patch(
            'plugins.modules.ibm_resource_alias.ResourceControllerV2.delete_resource_alias')
        mock = patcher.start()
        mock.return_value = DetailedResponseMock()

        get_resource_alias_patcher = patch(
            'plugins.modules.ibm_resource_alias.ResourceControllerV2.get_resource_alias')
        get_resource_alias_mock = get_resource_alias_patcher.start()
        get_resource_alias_mock.side_effect = ApiException(404)

        args = {
            'id': 'testString',
            'state': 'absent',
        }

        set_module_args(args)

        with self.assertRaises(AnsibleExitJson) as result:
            os.environ['RESOURCE_CONTROLLER_AUTH_TYPE'] = 'noAuth'
            os.environ['IC_API_KEY'] = 'noAuthAPIKey'
            ibm_resource_alias.main()

        assert result.exception.args[0]['changed'] is False
        assert result.exception.args[0]['msg']['id'] == 'testString'
        assert result.exception.args[0]['msg']['status'] == 'not_found'

        mock_data = dict(
            id='testString',
        )

        mock.assert_not_called()

        get_resource_alias_mock_data = dict(
            id='testString',
        )
        # Set the variables that belong to the "read" path to `None`
        # since we test the "delete" path here.
        for param in get_resource_alias_mock_data:
            get_resource_alias_mock_data[param] = mock_data.get(param, None)

        get_resource_alias_mock.assert_called_once()
        get_resource_alias_processed_result = post_process_result(
            get_resource_alias_mock_data, get_resource_alias_mock.call_args.kwargs)
        assert get_resource_alias_mock_data == get_resource_alias_processed_result

        get_resource_alias_patcher.stop()
        patcher.stop()

    def test_delete_ibm_resource_alias_failed(self):
        """Test the "delete" path - failed."""
        patcher = patch(
            'plugins.modules.ibm_resource_alias.ResourceControllerV2.delete_resource_alias')
        mock = patcher.start()
        mock.side_effect = ApiException(
            400, message='Delete ibm_resource_alias error')

        get_resource_alias_patcher = patch(
            'plugins.modules.ibm_resource_alias.ResourceControllerV2.get_resource_alias')
        get_resource_alias_mock = get_resource_alias_patcher.start()
        get_resource_alias_mock.return_value = DetailedResponseMock()

        set_module_args({
            'id': 'testString',
            'state': 'absent',
        })

        with self.assertRaises(AnsibleFailJson) as result:
            os.environ['RESOURCE_CONTROLLER_AUTH_TYPE'] = 'noAuth'
            os.environ['IC_API_KEY'] = 'noAuthAPIKey'
            ibm_resource_alias.main()

        assert result.exception.args[0]['msg'] == 'Delete ibm_resource_alias error'

        mock_data = dict(
            id='testString',
        )

        mock.assert_called_once()
        processed_result = post_process_result(
            mock_data, mock.call_args.kwargs)
        assert mock_data == processed_result

        get_resource_alias_mock_data = dict(
            id='testString',
        )
        # Set the variables that belong to the "read" path to `None`
        # since we test the "delete" path here.
        for param in get_resource_alias_mock_data:
            get_resource_alias_mock_data[param] = mock_data.get(param, None)

        get_resource_alias_mock.assert_called_once()
        get_resource_alias_processed_result = post_process_result(
            get_resource_alias_mock_data, get_resource_alias_mock.call_args.kwargs)
        assert get_resource_alias_mock_data == get_resource_alias_processed_result

        get_resource_alias_patcher.stop()
        patcher.stop()
