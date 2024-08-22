# (C) Copyright IBM Corp. 2024.
#
# GNU General Public License v3.0+ (see LICENSE or https://www.gnu.org/licenses/gpl-3.0.txt)

from __future__ import (absolute_import, division, print_function)
__metaclass__ = type

import os

from ansible_collections.community.internal_test_tools.tests.unit.compat.mock import patch
from ansible_collections.community.internal_test_tools.tests.unit.plugins.modules.utils import ModuleTestCase, AnsibleFailJson, AnsibleExitJson, set_module_args
from plugins.modules import ibm_schematics_workspace

try:
    from .common import DetailedResponseMock
    from ibm_cloud_sdk_core import ApiException
except ImportError as imp_exc:
    MISSING_IMPORT_EXC = imp_exc
else:
    MISSING_IMPORT_EXC = None


def checkResult(mock_data: dict, result: dict) -> bool:
    """Compares the mock data with the result from an operation.

    Ansible initializes every argument with a `None` value even if they
    are not defined. That behaivor makes the result dictionary "polluted"
    with extra items and uncomparable by default so we need to use this
    custom function to remove those extra fields with `None` value and
    compare the rest.

    Args:
        mock_data: the data given to the operation
        result: the result from the oparation

    Returns:
        A boolean value that indicates that the result dictionary has the correct values.
    """
    try:
        for res_key, res_value in result.items():
            if res_key not in mock_data:
                # If this key is not presented in the mock_data dictionary and its value is None
                # we can ignore it, since it supposed to be an implicitly added item by Ansible.
                if res_value is None:
                    continue
                else:
                    raise AssertionError
            else:
                mock_value = mock_data[res_key]
                if isinstance(res_value, dict):
                    # Check inner dictionaries recursively.
                    checkResult(mock_value, res_value)
                elif isinstance(res_value, list) and len(res_value) > 0:
                    # Check inner lists recursively with an inner function that makes it easier.
                    def checkInnerList(m: list, r: list):
                        for mock_elem, res_elem in zip(m, r):
                            if isinstance(mock_elem, dict) and isinstance(res_elem, dict):
                                # If both items are dict use the outer function to process them.
                                checkResult(mock_elem, res_elem)
                            elif isinstance(mock_elem, list) and isinstance(res_elem, list):
                                # If both items are list, use this function to process them.
                                checkInnerList(mock_elem, res_elem)
                            else:
                                assert mock_elem == res_elem

                    checkInnerList(mock_value, res_value)
                else:
                    # Primitive values are checked as is.
                    assert mock_value == res_value
    except AssertionError:
        return False

    # If no error happened that means the dictionaries are the same.
    return True


def mock_operations(func):
    def wrapper(self):
        # Make sure the imports are correct in both test and module packages.
        self.assertIsNone(MISSING_IMPORT_EXC)
        self.assertIsNone(ibm_schematics_workspace.MISSING_IMPORT_EXC)

        # Set-up mocks for each operation.
        self.read_patcher = patch('plugins.modules.ibm_schematics_workspace.SchematicsV1.get_workspace')
        self.read_mock = self.read_patcher.start()
        self.create_patcher = patch('plugins.modules.ibm_schematics_workspace.SchematicsV1.create_workspace')
        self.create_mock = self.create_patcher.start()
        self.update_patcher = patch('plugins.modules.ibm_schematics_workspace.SchematicsV1.update_workspace')
        self.update_mock = self.update_patcher.start()
        self.delete_patcher = patch('plugins.modules.ibm_schematics_workspace.SchematicsV1.delete_workspace')
        self.delete_mock = self.delete_patcher.start()

        # Run the actual function.
        func(self)

        # Stop the patchers.
        self.read_patcher.stop()
        self.create_patcher.stop()
        self.update_patcher.stop()
        self.delete_patcher.stop()

    return wrapper


class TestWorkspaceResponseModule(ModuleTestCase):
    """
    Test class for WorkspaceResponse module testing.
    """

    @mock_operations
    def test_read_ibm_schematics_workspace_failed(self):
        """Test the inner "read" path in this module with a server error response."""
        self.read_mock.side_effect = ApiException(500, message='Something went wrong...')

        set_module_args({
            'w_id': 'testString',
        })

        with self.assertRaises(AnsibleFailJson) as result:
            os.environ['SCHEMATICS_AUTH_TYPE'] = 'noAuth'
            ibm_schematics_workspace.main()

        self.assertEqual(result.exception.args[0]['msg'], 'Something went wrong...')

        mock_data = dict(
            w_id='testString',
        )

        self.read_mock.assert_called_once()
        self.assertTrue(checkResult(mock_data, self.read_mock.call_args.kwargs))

    @mock_operations
    def test_create_ibm_schematics_workspace_success(self):
        """Test the "create" path - successful."""
        service_extensions_model = {
            'name': 'flavor',
            'value': 'testString',
            'type': 'string',
        }

        catalog_ref_model = {
            'dry_run': True,
            'owning_account': 'testString',
            'item_icon_url': 'testString',
            'item_id': 'testString',
            'item_name': 'testString',
            'item_readme_url': 'testString',
            'item_url': 'testString',
            'launch_url': 'testString',
            'offering_version': 'testString',
            'service_extensions': [service_extensions_model],
        }

        dependencies_model = {
            'parents': ['testString'],
            'children': ['testString'],
        }

        shared_target_data_model = {
            'cluster_created_on': 'testString',
            'cluster_id': 'testString',
            'cluster_name': 'testString',
            'cluster_type': 'testString',
            'entitlement_keys': [{'anyKey': 'anyValue'}],
            'namespace': 'testString',
            'region': 'testString',
            'resource_group_id': 'testString',
            'worker_count': 26,
            'worker_machine_type': 'testString',
        }

        environment_values_metadata_model = {
            'hidden': True,
            'name': 'testString',
            'secure': True,
        }

        inject_terraform_template_inner_tft_parameters_item_model = {
            'name': 'testString',
            'value': 'testString',
        }

        inject_terraform_template_inner_model = {
            'tft_git_url': 'testString',
            'tft_git_token': 'testString',
            'tft_prefix': 'testString',
            'injection_type': 'testString',
            'tft_name': 'testString',
            'tft_parameters': [inject_terraform_template_inner_tft_parameters_item_model],
        }

        workspace_variable_request_model = {
            'description': 'testString',
            'name': 'testString',
            'secure': True,
            'type': 'testString',
            'use_default': True,
            'value': 'testString',
        }

        template_source_data_request_model = {
            'env_values': [{'anyKey': 'anyValue'}],
            'env_values_metadata': [environment_values_metadata_model],
            'folder': 'testString',
            'compact': True,
            'init_state_file': 'testString',
            'injectors': [inject_terraform_template_inner_model],
            'type': 'testString',
            'uninstall_script_name': 'testString',
            'values': 'testString',
            'values_metadata': [{'anyKey': 'anyValue'}],
            'variablestore': [workspace_variable_request_model],
        }

        template_repo_request_model = {
            'branch': 'testString',
            'release': 'testString',
            'repo_sha_value': 'testString',
            'repo_url': 'testString',
            'url': 'testString',
        }

        workspace_status_request_model = {
            'frozen': True,
            'frozen_at': '2019-01-01T12:00:00.000Z',
            'frozen_by': 'testString',
            'locked': True,
            'locked_by': 'testString',
            'locked_time': '2019-01-01T12:00:00.000Z',
        }

        variable_metadata_model = {
            'type': 'boolean',
            'aliases': ['testString'],
            'description': 'testString',
            'cloud_data_type': 'testString',
            'default_value': 'testString',
            'link_status': 'normal',
            'secure': True,
            'immutable': True,
            'hidden': True,
            'required': True,
            'options': ['testString'],
            'min_value': 38,
            'max_value': 38,
            'min_length': 38,
            'max_length': 38,
            'matches': 'testString',
            'position': 38,
            'group_by': 'testString',
            'source': 'testString',
        }

        variable_data_model = {
            'name': 'testString',
            'value': 'testString',
            'use_default': True,
            'metadata': variable_metadata_model,
        }

        resource = {
            'applied_shareddata_ids': ['testString'],
            'catalog_ref': catalog_ref_model,
            'dependencies': dependencies_model,
            'description': 'testString',
            'location': 'testString',
            'name': 'testString',
            'resource_group': 'testString',
            'shared_data': shared_target_data_model,
            'tags': ['testString'],
            'template_data': [template_source_data_request_model],
            'template_ref': 'testString',
            'template_repo': template_repo_request_model,
            'type': ['testString'],
            'workspace_status': workspace_status_request_model,
            'agent_id': 'testString',
            'settings': [variable_data_model],
            'x_github_token': 'testString',
        }

        self.read_mock.side_effect = ApiException(404)
        self.create_mock.return_value = DetailedResponseMock(resource)

        set_module_args({
            'applied_shareddata_ids': ['testString'],
            'catalog_ref': catalog_ref_model,
            'dependencies': dependencies_model,
            'description': 'testString',
            'location': 'testString',
            'name': 'testString',
            'resource_group': 'testString',
            'shared_data': shared_target_data_model,
            'tags': ['testString'],
            'template_data': [template_source_data_request_model],
            'template_ref': 'testString',
            'template_repo': template_repo_request_model,
            'type': ['testString'],
            'workspace_status': workspace_status_request_model,
            'agent_id': 'testString',
            'settings': [variable_data_model],
            'x_github_token': 'testString',
        })

        with self.assertRaises(AnsibleExitJson) as result:
            os.environ['SCHEMATICS_AUTH_TYPE'] = 'noAuth'
            ibm_schematics_workspace.main()

        self.assertTrue(result.exception.args[0]['changed'])
        for field, value in resource.items():
            self.assertEqual(value, result.exception.args[0].get(field))

        mock_data = dict(
            applied_shareddata_ids=['testString'],
            catalog_ref=catalog_ref_model,
            dependencies=dependencies_model,
            description='testString',
            location='testString',
            name='testString',
            resource_group='testString',
            shared_data=shared_target_data_model,
            tags=['testString'],
            template_data=[template_source_data_request_model],
            template_ref='testString',
            template_repo=template_repo_request_model,
            type=['testString'],
            workspace_status=workspace_status_request_model,
            agent_id='testString',
            settings=[variable_data_model],
            x_github_token='testString',
        )

        self.create_mock.assert_called_once()
        self.assertTrue(checkResult(mock_data, self.create_mock.call_args.kwargs))

    @mock_operations
    def test_create_ibm_schematics_workspace_failed(self):
        """Test the "create" path - failed."""
        self.read_mock.side_effect = ApiException(404)
        self.create_mock.side_effect = ApiException(400, message='Create ibm_schematics_workspace error')

        service_extensions_model = {
            'name': 'flavor',
            'value': 'testString',
            'type': 'string',
        }

        catalog_ref_model = {
            'dry_run': True,
            'owning_account': 'testString',
            'item_icon_url': 'testString',
            'item_id': 'testString',
            'item_name': 'testString',
            'item_readme_url': 'testString',
            'item_url': 'testString',
            'launch_url': 'testString',
            'offering_version': 'testString',
            'service_extensions': [service_extensions_model],
        }

        dependencies_model = {
            'parents': ['testString'],
            'children': ['testString'],
        }

        shared_target_data_model = {
            'cluster_created_on': 'testString',
            'cluster_id': 'testString',
            'cluster_name': 'testString',
            'cluster_type': 'testString',
            'entitlement_keys': [{'anyKey': 'anyValue'}],
            'namespace': 'testString',
            'region': 'testString',
            'resource_group_id': 'testString',
            'worker_count': 26,
            'worker_machine_type': 'testString',
        }

        environment_values_metadata_model = {
            'hidden': True,
            'name': 'testString',
            'secure': True,
        }

        inject_terraform_template_inner_tft_parameters_item_model = {
            'name': 'testString',
            'value': 'testString',
        }

        inject_terraform_template_inner_model = {
            'tft_git_url': 'testString',
            'tft_git_token': 'testString',
            'tft_prefix': 'testString',
            'injection_type': 'testString',
            'tft_name': 'testString',
            'tft_parameters': [inject_terraform_template_inner_tft_parameters_item_model],
        }

        workspace_variable_request_model = {
            'description': 'testString',
            'name': 'testString',
            'secure': True,
            'type': 'testString',
            'use_default': True,
            'value': 'testString',
        }

        template_source_data_request_model = {
            'env_values': [{'anyKey': 'anyValue'}],
            'env_values_metadata': [environment_values_metadata_model],
            'folder': 'testString',
            'compact': True,
            'init_state_file': 'testString',
            'injectors': [inject_terraform_template_inner_model],
            'type': 'testString',
            'uninstall_script_name': 'testString',
            'values': 'testString',
            'values_metadata': [{'anyKey': 'anyValue'}],
            'variablestore': [workspace_variable_request_model],
        }

        template_repo_request_model = {
            'branch': 'testString',
            'release': 'testString',
            'repo_sha_value': 'testString',
            'repo_url': 'testString',
            'url': 'testString',
        }

        workspace_status_request_model = {
            'frozen': True,
            'frozen_at': '2019-01-01T12:00:00.000Z',
            'frozen_by': 'testString',
            'locked': True,
            'locked_by': 'testString',
            'locked_time': '2019-01-01T12:00:00.000Z',
        }

        variable_metadata_model = {
            'type': 'boolean',
            'aliases': ['testString'],
            'description': 'testString',
            'cloud_data_type': 'testString',
            'default_value': 'testString',
            'link_status': 'normal',
            'secure': True,
            'immutable': True,
            'hidden': True,
            'required': True,
            'options': ['testString'],
            'min_value': 38,
            'max_value': 38,
            'min_length': 38,
            'max_length': 38,
            'matches': 'testString',
            'position': 38,
            'group_by': 'testString',
            'source': 'testString',
        }

        variable_data_model = {
            'name': 'testString',
            'value': 'testString',
            'use_default': True,
            'metadata': variable_metadata_model,
        }

        set_module_args({
            'applied_shareddata_ids': ['testString'],
            'catalog_ref': catalog_ref_model,
            'dependencies': dependencies_model,
            'description': 'testString',
            'location': 'testString',
            'name': 'testString',
            'resource_group': 'testString',
            'shared_data': shared_target_data_model,
            'tags': ['testString'],
            'template_data': [template_source_data_request_model],
            'template_ref': 'testString',
            'template_repo': template_repo_request_model,
            'type': ['testString'],
            'workspace_status': workspace_status_request_model,
            'agent_id': 'testString',
            'settings': [variable_data_model],
            'x_github_token': 'testString',
        })

        with self.assertRaises(AnsibleFailJson) as result:
            os.environ['SCHEMATICS_AUTH_TYPE'] = 'noAuth'
            ibm_schematics_workspace.main()

        self.assertEqual(result.exception.args[0]['msg'], 'Create ibm_schematics_workspace error')

        mock_data = dict(
            applied_shareddata_ids=['testString'],
            catalog_ref=catalog_ref_model,
            dependencies=dependencies_model,
            description='testString',
            location='testString',
            name='testString',
            resource_group='testString',
            shared_data=shared_target_data_model,
            tags=['testString'],
            template_data=[template_source_data_request_model],
            template_ref='testString',
            template_repo=template_repo_request_model,
            type=['testString'],
            workspace_status=workspace_status_request_model,
            agent_id='testString',
            settings=[variable_data_model],
            x_github_token='testString',
        )

        self.create_mock.assert_called_once()
        self.assertTrue(checkResult(mock_data, self.create_mock.call_args.kwargs))

    @mock_operations
    def test_update_ibm_schematics_workspace_success(self):
        """Test the "update" path - successful."""
        service_extensions_model = {
            'name': 'flavor',
            'value': 'testString',
            'type': 'string',
        }

        catalog_ref_model = {
            'dry_run': True,
            'owning_account': 'testString',
            'item_icon_url': 'testString',
            'item_id': 'testString',
            'item_name': 'testString',
            'item_readme_url': 'testString',
            'item_url': 'testString',
            'launch_url': 'testString',
            'offering_version': 'testString',
            'service_extensions': [service_extensions_model],
        }

        dependencies_model = {
            'parents': ['testString'],
            'children': ['testString'],
        }

        shared_target_data_model = {
            'cluster_created_on': 'testString',
            'cluster_id': 'testString',
            'cluster_name': 'testString',
            'cluster_type': 'testString',
            'entitlement_keys': [{'anyKey': 'anyValue'}],
            'namespace': 'testString',
            'region': 'testString',
            'resource_group_id': 'testString',
            'worker_count': 26,
            'worker_machine_type': 'testString',
        }

        environment_values_metadata_model = {
            'hidden': True,
            'name': 'testString',
            'secure': True,
        }

        inject_terraform_template_inner_tft_parameters_item_model = {
            'name': 'testString',
            'value': 'testString',
        }

        inject_terraform_template_inner_model = {
            'tft_git_url': 'testString',
            'tft_git_token': 'testString',
            'tft_prefix': 'testString',
            'injection_type': 'testString',
            'tft_name': 'testString',
            'tft_parameters': [inject_terraform_template_inner_tft_parameters_item_model],
        }

        workspace_variable_request_model = {
            'description': 'testString',
            'name': 'testString',
            'secure': True,
            'type': 'testString',
            'use_default': True,
            'value': 'testString',
        }

        template_source_data_request_model = {
            'env_values': [{'anyKey': 'anyValue'}],
            'env_values_metadata': [environment_values_metadata_model],
            'folder': 'testString',
            'compact': True,
            'init_state_file': 'testString',
            'injectors': [inject_terraform_template_inner_model],
            'type': 'testString',
            'uninstall_script_name': 'testString',
            'values': 'testString',
            'values_metadata': [{'anyKey': 'anyValue'}],
            'variablestore': [workspace_variable_request_model],
        }

        template_repo_update_request_model = {
            'branch': 'testString',
            'release': 'testString',
            'repo_sha_value': 'testString',
            'repo_url': 'testString',
            'url': 'testString',
        }

        workspace_status_update_request_model = {
            'frozen': True,
            'frozen_at': '2019-01-01T12:00:00.000Z',
            'frozen_by': 'testString',
            'locked': True,
            'locked_by': 'testString',
            'locked_time': '2019-01-01T12:00:00.000Z',
        }

        workspace_status_message_model = {
            'status_code': 'testString',
            'status_msg': 'testString',
        }

        variable_metadata_model = {
            'type': 'boolean',
            'aliases': ['testString'],
            'description': 'testString',
            'cloud_data_type': 'testString',
            'default_value': 'testString',
            'link_status': 'normal',
            'secure': True,
            'immutable': True,
            'hidden': True,
            'required': True,
            'options': ['testString'],
            'min_value': 38,
            'max_value': 38,
            'min_length': 38,
            'max_length': 38,
            'matches': 'testString',
            'position': 38,
            'group_by': 'testString',
            'source': 'testString',
        }

        variable_data_model = {
            'name': 'testString',
            'value': 'testString',
            'use_default': True,
            'metadata': variable_metadata_model,
        }

        resource = {
            'w_id': 'testString',
            'catalog_ref': catalog_ref_model,
            'description': 'testString',
            'dependencies': dependencies_model,
            'name': 'testString',
            'shared_data': shared_target_data_model,
            'tags': ['testString'],
            'template_data': [template_source_data_request_model],
            'template_repo_update_request_template_repo': template_repo_update_request_model,
            'type': ['testString'],
            'workspace_status_update_request_workspace_status': workspace_status_update_request_model,
            'workspace_status_msg': workspace_status_message_model,
            'agent_id': 'testString',
            'settings': [variable_data_model],
        }

        self.read_mock.return_value = DetailedResponseMock(resource)
        self.update_mock.return_value = DetailedResponseMock(resource)

        set_module_args({
            'w_id': 'testString',
            'catalog_ref': catalog_ref_model,
            'description': 'testString',
            'dependencies': dependencies_model,
            'name': 'testString',
            'shared_data': shared_target_data_model,
            'tags': ['testString'],
            'template_data': [template_source_data_request_model],
            'template_repo_update_request_template_repo': template_repo_update_request_model,
            'type': ['testString'],
            'workspace_status_update_request_workspace_status': workspace_status_update_request_model,
            'workspace_status_msg': workspace_status_message_model,
            'agent_id': 'testString',
            'settings': [variable_data_model],
        })

        with self.assertRaises(AnsibleExitJson) as result:
            os.environ['SCHEMATICS_AUTH_TYPE'] = 'noAuth'
            ibm_schematics_workspace.main()

        self.assertTrue(result.exception.args[0]['changed'])
        for field, value in resource.items():
            self.assertEqual(value, result.exception.args[0].get(field))

        mock_data = dict(
            w_id='testString',
            catalog_ref=catalog_ref_model,
            description='testString',
            dependencies=dependencies_model,
            name='testString',
            shared_data=shared_target_data_model,
            tags=['testString'],
            template_data=[template_source_data_request_model],
            template_repo=template_repo_update_request_model,
            type=['testString'],
            workspace_status=workspace_status_update_request_model,
            workspace_status_msg=workspace_status_message_model,
            agent_id='testString',
            settings=[variable_data_model],
        )

        self.update_mock.assert_called_once()
        self.assertTrue(checkResult(mock_data, self.update_mock.call_args.kwargs))

        read_mock_data = dict(
            w_id='testString',
        )
        # Set the variables that belong to the "read" path to `None`
        # because we test the "update" path here.
        for param in read_mock_data:
            read_mock_data[param] = mock_data.get(param, None)

        self.read_mock.assert_called_once()
        self.assertTrue(checkResult(read_mock_data, self.read_mock.call_args.kwargs))

    @mock_operations
    def test_update_ibm_schematics_workspace_failed(self):
        """Test the "update" path - failed."""
        service_extensions_model = {
            'name': 'flavor',
            'value': 'testString',
            'type': 'string',
        }

        catalog_ref_model = {
            'dry_run': True,
            'owning_account': 'testString',
            'item_icon_url': 'testString',
            'item_id': 'testString',
            'item_name': 'testString',
            'item_readme_url': 'testString',
            'item_url': 'testString',
            'launch_url': 'testString',
            'offering_version': 'testString',
            'service_extensions': [service_extensions_model],
        }

        dependencies_model = {
            'parents': ['testString'],
            'children': ['testString'],
        }

        shared_target_data_model = {
            'cluster_created_on': 'testString',
            'cluster_id': 'testString',
            'cluster_name': 'testString',
            'cluster_type': 'testString',
            'entitlement_keys': [{'anyKey': 'anyValue'}],
            'namespace': 'testString',
            'region': 'testString',
            'resource_group_id': 'testString',
            'worker_count': 26,
            'worker_machine_type': 'testString',
        }

        environment_values_metadata_model = {
            'hidden': True,
            'name': 'testString',
            'secure': True,
        }

        inject_terraform_template_inner_tft_parameters_item_model = {
            'name': 'testString',
            'value': 'testString',
        }

        inject_terraform_template_inner_model = {
            'tft_git_url': 'testString',
            'tft_git_token': 'testString',
            'tft_prefix': 'testString',
            'injection_type': 'testString',
            'tft_name': 'testString',
            'tft_parameters': [inject_terraform_template_inner_tft_parameters_item_model],
        }

        workspace_variable_request_model = {
            'description': 'testString',
            'name': 'testString',
            'secure': True,
            'type': 'testString',
            'use_default': True,
            'value': 'testString',
        }

        template_source_data_request_model = {
            'env_values': [{'anyKey': 'anyValue'}],
            'env_values_metadata': [environment_values_metadata_model],
            'folder': 'testString',
            'compact': True,
            'init_state_file': 'testString',
            'injectors': [inject_terraform_template_inner_model],
            'type': 'testString',
            'uninstall_script_name': 'testString',
            'values': 'testString',
            'values_metadata': [{'anyKey': 'anyValue'}],
            'variablestore': [workspace_variable_request_model],
        }

        template_repo_update_request_model = {
            'branch': 'testString',
            'release': 'testString',
            'repo_sha_value': 'testString',
            'repo_url': 'testString',
            'url': 'testString',
        }

        workspace_status_update_request_model = {
            'frozen': True,
            'frozen_at': '2019-01-01T12:00:00.000Z',
            'frozen_by': 'testString',
            'locked': True,
            'locked_by': 'testString',
            'locked_time': '2019-01-01T12:00:00.000Z',
        }

        workspace_status_message_model = {
            'status_code': 'testString',
            'status_msg': 'testString',
        }

        variable_metadata_model = {
            'type': 'boolean',
            'aliases': ['testString'],
            'description': 'testString',
            'cloud_data_type': 'testString',
            'default_value': 'testString',
            'link_status': 'normal',
            'secure': True,
            'immutable': True,
            'hidden': True,
            'required': True,
            'options': ['testString'],
            'min_value': 38,
            'max_value': 38,
            'min_length': 38,
            'max_length': 38,
            'matches': 'testString',
            'position': 38,
            'group_by': 'testString',
            'source': 'testString',
        }

        variable_data_model = {
            'name': 'testString',
            'value': 'testString',
            'use_default': True,
            'metadata': variable_metadata_model,
        }

        resource = {
            'w_id': 'testString',
            'catalog_ref': catalog_ref_model,
            'description': 'testString',
            'dependencies': dependencies_model,
            'name': 'testString',
            'shared_data': shared_target_data_model,
            'tags': ['testString'],
            'template_data': [template_source_data_request_model],
            'template_repo_update_request_template_repo': template_repo_update_request_model,
            'type': ['testString'],
            'workspace_status_update_request_workspace_status': workspace_status_update_request_model,
            'workspace_status_msg': workspace_status_message_model,
            'agent_id': 'testString',
            'settings': [variable_data_model],
        }

        self.read_mock.return_value = DetailedResponseMock(resource)
        self.update_mock.side_effect = ApiException(400, message='Update ibm_schematics_workspace error')

        set_module_args({
            'w_id': 'testString',
            'catalog_ref': catalog_ref_model,
            'description': 'testString',
            'dependencies': dependencies_model,
            'name': 'testString',
            'shared_data': shared_target_data_model,
            'tags': ['testString'],
            'template_data': [template_source_data_request_model],
            'template_repo_update_request_template_repo': template_repo_update_request_model,
            'type': ['testString'],
            'workspace_status_update_request_workspace_status': workspace_status_update_request_model,
            'workspace_status_msg': workspace_status_message_model,
            'agent_id': 'testString',
            'settings': [variable_data_model],
        })

        with self.assertRaises(AnsibleFailJson) as result:
            os.environ['SCHEMATICS_AUTH_TYPE'] = 'noAuth'
            ibm_schematics_workspace.main()

        self.assertEqual(result.exception.args[0]['msg'], 'Update ibm_schematics_workspace error')

        mock_data = dict(
            w_id='testString',
            catalog_ref=catalog_ref_model,
            description='testString',
            dependencies=dependencies_model,
            name='testString',
            shared_data=shared_target_data_model,
            tags=['testString'],
            template_data=[template_source_data_request_model],
            template_repo=template_repo_update_request_model,
            type=['testString'],
            workspace_status=workspace_status_update_request_model,
            workspace_status_msg=workspace_status_message_model,
            agent_id='testString',
            settings=[variable_data_model],
        )

        self.update_mock.assert_called_once()
        self.assertTrue(checkResult(mock_data, self.update_mock.call_args.kwargs))

        read_mock_data = dict(
            w_id='testString',
        )
        # Set the variables that belong to the "read" path to `None`
        # because we test the "update" path here.
        for param in read_mock_data:
            read_mock_data[param] = mock_data.get(param, None)

        self.read_mock.assert_called_once()
        self.assertTrue(checkResult(read_mock_data, self.read_mock.call_args.kwargs))

    @mock_operations
    def test_delete_ibm_schematics_workspace_success(self):
        """Test the "delete" path - successfull."""
        self.read_mock.return_value = DetailedResponseMock()
        self.delete_mock.return_value = DetailedResponseMock()

        args = {
            'refresh_token': 'testString',
            'w_id': 'testString',
            'destroy_resources': 'testString',
            'state': 'absent',
        }

        set_module_args(args)

        with self.assertRaises(AnsibleExitJson) as result:
            os.environ['SCHEMATICS_AUTH_TYPE'] = 'noAuth'
            ibm_schematics_workspace.main()

        self.assertTrue(result.exception.args[0]['changed'])
        self.assertEqual(result.exception.args[0]['id'], 'testString')
        self.assertEqual(result.exception.args[0]['status'], 'deleted')

        mock_data = dict(
            refresh_token='testString',
            w_id='testString',
            destroy_resources='testString',
        )

        self.delete_mock.assert_called_once()
        self.assertTrue(checkResult(mock_data, self.delete_mock.call_args.kwargs))

        read_mock_data = dict(
            w_id='testString',
        )
        # Set the variables that belong to the "read" path to `None`
        # because we test the "delete" path here.
        for param in read_mock_data:
            read_mock_data[param] = mock_data.get(param, None)

        self.read_mock.assert_called_once()
        self.assertTrue(checkResult(read_mock_data, self.read_mock.call_args.kwargs))

    @mock_operations
    def test_delete_ibm_schematics_workspace_not_exists(self):
        """Test the "delete" path - not exists."""
        self.read_mock.side_effect = ApiException(404)
        self.delete_mock.return_value = DetailedResponseMock()

        args = {
            'refresh_token': 'testString',
            'w_id': 'testString',
            'destroy_resources': 'testString',
            'state': 'absent',
        }

        set_module_args(args)

        with self.assertRaises(AnsibleExitJson) as result:
            os.environ['SCHEMATICS_AUTH_TYPE'] = 'noAuth'
            ibm_schematics_workspace.main()

        self.assertFalse(result.exception.args[0]['changed'])
        self.assertEqual(result.exception.args[0]['id'], 'testString')
        self.assertEqual(result.exception.args[0]['status'], 'not_found')

        mock_data = dict(
            refresh_token='testString',
            w_id='testString',
            destroy_resources='testString',
        )

        self.delete_mock.assert_not_called()

        read_mock_data = dict(
            w_id='testString',
        )
        # Set the variables that belong to the "read" path to `None`
        # because we test the "delete" path here.
        for param in read_mock_data:
            read_mock_data[param] = mock_data.get(param, None)

        self.read_mock.assert_called_once()
        self.assertTrue(checkResult(read_mock_data, self.read_mock.call_args.kwargs))

    @mock_operations
    def test_delete_ibm_schematics_workspace_failed(self):
        """Test the "delete" path - failed."""
        self.read_mock.return_value = DetailedResponseMock()
        self.delete_mock.side_effect = ApiException(400, message='Delete ibm_schematics_workspace error')

        set_module_args({
            'refresh_token': 'testString',
            'w_id': 'testString',
            'destroy_resources': 'testString',
            'state': 'absent',
        })

        with self.assertRaises(AnsibleFailJson) as result:
            os.environ['SCHEMATICS_AUTH_TYPE'] = 'noAuth'
            ibm_schematics_workspace.main()

        self.assertEqual(result.exception.args[0]['msg'], 'Delete ibm_schematics_workspace error')

        mock_data = dict(
            refresh_token='testString',
            w_id='testString',
            destroy_resources='testString',
        )

        self.delete_mock.assert_called_once()
        self.assertTrue(checkResult(mock_data, self.delete_mock.call_args.kwargs))

        read_mock_data = dict(
            w_id='testString',
        )
        # Set the variables that belong to the "read" path to `None`
        # because we test the "delete" path here.
        for param in read_mock_data:
            read_mock_data[param] = mock_data.get(param, None)

        self.read_mock.assert_called_once()
        self.assertTrue(checkResult(read_mock_data, self.read_mock.call_args.kwargs))
