# (C) Copyright IBM Corp. 2022.
# GNU General Public License v3.0+ (see LICENSE or https://www.gnu.org/licenses/gpl-3.0.txt)

from __future__ import (absolute_import, division, print_function)
__metaclass__ = type

import os

from .common import DetailedResponseMock
from plugins.modules import ibm_schematics_workspace
from ansible_collections.community.internal_test_tools.tests.unit.compat.mock import patch
from ansible_collections.community.internal_test_tools.tests.unit.plugins.modules.utils import ModuleTestCase, AnsibleFailJson, AnsibleExitJson, set_module_args

try:
    from ibm_cloud_sdk_core import ApiException
except ImportError:
    pass


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


class TestWorkspaceResponseModule(ModuleTestCase):
    """
    Test class for WorkspaceResponse module testing.
    """

    def test_read_ibm_schematics_workspace_failed(self):
        """Test the inner "read" path in this module with a server error response."""

        patcher = patch(
            'plugins.modules.ibm_schematics_workspace.SchematicsV1.get_workspace')
        mock = patcher.start()
        mock.side_effect = ApiException(500, message='Something went wrong...')

        set_module_args({
            'w_id': 'testString',
        })

        with self.assertRaises(AnsibleFailJson) as result:
            os.environ['SCHEMATICS_AUTH_TYPE'] = 'noAuth'
            os.environ['IC_API_KEY'] = 'noAuthAPIKey'
            ibm_schematics_workspace.main()

        assert result.exception.args[0]['msg'] == 'Something went wrong...'

        mock_data = dict(
            w_id='testString',
        )

        mock.assert_called_once()
        processed_result = post_process_result(
            mock_data, mock.call_args.kwargs)
        assert mock_data == processed_result

        patcher.stop()

    def test_create_ibm_schematics_workspace_success(self):
        """Test the "create" path - successful."""
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
            # 'entitlement_keys': [{'foo': 'bar'}],
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
            # 'env_values': [{'foo': 'bar'}],
            'env_values_metadata': [environment_values_metadata_model],
            'folder': 'testString',
            'compact': True,
            'init_state_file': 'testString',
            'injectors': [inject_terraform_template_inner_model],
            'type': 'testString',
            'uninstall_script_name': 'testString',
            'values': 'testString',
            # 'values_metadata': [{'foo': 'bar'}],
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
            'x_github_token': 'testString',
        }

        patcher = patch(
            'plugins.modules.ibm_schematics_workspace.SchematicsV1.create_workspace')
        mock = patcher.start()
        mock.return_value = DetailedResponseMock(resource)

        get_workspace_patcher = patch(
            'plugins.modules.ibm_schematics_workspace.SchematicsV1.get_workspace')
        get_workspace_mock = get_workspace_patcher.start()

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
            'x_github_token': 'testString',
        })

        with self.assertRaises(AnsibleExitJson) as result:
            os.environ['SCHEMATICS_AUTH_TYPE'] = 'noAuth'
            os.environ['IC_API_KEY'] = 'noAuthAPIKey'
            ibm_schematics_workspace.main()

        assert result.exception.args[0]['changed'] is True
        assert result.exception.args[0]['msg'] == resource

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
            x_github_token='testString',
        )

        mock.assert_called_once()
        processed_result = post_process_result(
            mock_data, mock.call_args.kwargs)
        assert mock_data == processed_result

        get_workspace_mock.assert_not_called()

        get_workspace_patcher.stop()
        patcher.stop()

    def test_create_ibm_schematics_workspace_failed(self):
        """Test the "create" path - failed."""

        get_workspace_patcher = patch(
            'plugins.modules.ibm_schematics_workspace.SchematicsV1.get_workspace')
        get_workspace_mock = get_workspace_patcher.start()

        patcher = patch(
            'plugins.modules.ibm_schematics_workspace.SchematicsV1.create_workspace')
        mock = patcher.start()
        mock.side_effect = ApiException(
            400, message='Create ibm_schematics_workspace error')

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
            # 'entitlement_keys': [{'foo': 'bar'}],
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
            # 'env_values': [{'foo': 'bar'}],
            'env_values_metadata': [environment_values_metadata_model],
            'folder': 'testString',
            'compact': True,
            'init_state_file': 'testString',
            'injectors': [inject_terraform_template_inner_model],
            'type': 'testString',
            'uninstall_script_name': 'testString',
            'values': 'testString',
            # 'values_metadata': [{'foo': 'bar'}],
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
            'x_github_token': 'testString',
        })

        with self.assertRaises(AnsibleFailJson) as result:
            os.environ['SCHEMATICS_AUTH_TYPE'] = 'noAuth'
            os.environ['IC_API_KEY'] = 'noAuthAPIKey'
            ibm_schematics_workspace.main()

        assert result.exception.args[0]['msg'] == 'Create ibm_schematics_workspace error'

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
            x_github_token='testString',
        )

        mock.assert_called_once()
        processed_result = post_process_result(
            mock_data, mock.call_args.kwargs)
        assert mock_data == processed_result

        get_workspace_mock.assert_not_called()

        get_workspace_patcher.stop()
        patcher.stop()

    def test_update_ibm_schematics_workspace_success(self):
        """Test the "update" path - successful."""
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
            # 'entitlement_keys': [{'foo': 'bar'}],
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
            # 'env_values': [{'foo': 'bar'}],
            'env_values_metadata': [environment_values_metadata_model],
            'folder': 'testString',
            'compact': True,
            'init_state_file': 'testString',
            'injectors': [inject_terraform_template_inner_model],
            'type': 'testString',
            'uninstall_script_name': 'testString',
            'values': 'testString',
            # 'values_metadata': [{'foo': 'bar'}],
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
        }

        patcher = patch(
            'plugins.modules.ibm_schematics_workspace.SchematicsV1.update_workspace')
        mock = patcher.start()
        mock.return_value = DetailedResponseMock(resource)

        get_workspace_patcher = patch(
            'plugins.modules.ibm_schematics_workspace.SchematicsV1.get_workspace')
        get_workspace_mock = get_workspace_patcher.start()
        get_workspace_mock.return_value = DetailedResponseMock(resource)

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
        })

        with self.assertRaises(AnsibleExitJson) as result:
            os.environ['SCHEMATICS_AUTH_TYPE'] = 'noAuth'
            os.environ['IC_API_KEY'] = 'noAuthAPIKey'
            ibm_schematics_workspace.main()

        assert result.exception.args[0]['changed'] is True
        assert result.exception.args[0]['msg'] == resource

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
        )

        mock.assert_called_once()
        processed_result = post_process_result(
            mock_data, mock.call_args.kwargs)
        assert mock_data == processed_result

        get_workspace_mock_data = dict(
            w_id='testString',
        )
        # Set the variables that belong to the "read" path to `None`
        # since we test the "delete" path here.
        for param in get_workspace_mock_data:
            get_workspace_mock_data[param] = mock_data.get(param, None)

        get_workspace_mock.assert_called_once()
        get_workspace_processed_result = post_process_result(
            get_workspace_mock_data, get_workspace_mock.call_args.kwargs)
        assert get_workspace_mock_data == get_workspace_processed_result
        get_workspace_patcher.stop()
        patcher.stop()

    def test_update_ibm_schematics_workspace_failed(self):
        """Test the "update" path - failed."""
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
            # 'entitlement_keys': [{'foo': 'bar'}],
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
            # 'env_values': [{'foo': 'bar'}],
            'env_values_metadata': [environment_values_metadata_model],
            'folder': 'testString',
            'compact': True,
            'init_state_file': 'testString',
            'injectors': [inject_terraform_template_inner_model],
            'type': 'testString',
            'uninstall_script_name': 'testString',
            'values': 'testString',
            # 'values_metadata': [{'foo': 'bar'}],
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
        }

        patcher = patch(
            'plugins.modules.ibm_schematics_workspace.SchematicsV1.update_workspace')
        mock = patcher.start()
        mock.side_effect = ApiException(
            400, message='Update ibm_schematics_workspace error')

        get_workspace_patcher = patch(
            'plugins.modules.ibm_schematics_workspace.SchematicsV1.get_workspace')
        get_workspace_mock = get_workspace_patcher.start()
        get_workspace_mock.return_value = DetailedResponseMock(resource)

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
        })

        with self.assertRaises(AnsibleFailJson) as result:
            os.environ['SCHEMATICS_AUTH_TYPE'] = 'noAuth'
            os.environ['IC_API_KEY'] = 'noAuthAPIKey'
            ibm_schematics_workspace.main()

        assert result.exception.args[0]['msg'] == 'Update ibm_schematics_workspace error'

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
        )

        mock.assert_called_once()
        processed_result = post_process_result(
            mock_data, mock.call_args.kwargs)
        assert mock_data == processed_result

        get_workspace_mock_data = dict(
            w_id='testString',
        )
        # Set the variables that belong to the "read" path to `None`
        # since we test the "delete" path here.
        for param in get_workspace_mock_data:
            get_workspace_mock_data[param] = mock_data.get(param, None)

        get_workspace_mock.assert_called_once()
        get_workspace_processed_result = post_process_result(
            get_workspace_mock_data, get_workspace_mock.call_args.kwargs)
        assert get_workspace_mock_data == get_workspace_processed_result

        get_workspace_patcher.stop()
        patcher.stop()

    def test_delete_ibm_schematics_workspace_success(self):
        """Test the "delete" path - successfull."""
        patcher = patch(
            'plugins.modules.ibm_schematics_workspace.SchematicsV1.delete_workspace')
        mock = patcher.start()
        mock.return_value = DetailedResponseMock()

        get_workspace_patcher = patch(
            'plugins.modules.ibm_schematics_workspace.SchematicsV1.get_workspace')
        get_workspace_mock = get_workspace_patcher.start()
        get_workspace_mock.return_value = DetailedResponseMock()

        args = {
            'refresh_token': 'testString',
            'w_id': 'testString',
            'destroy_resources': 'testString',
            'state': 'absent',
        }

        set_module_args(args)

        with self.assertRaises(AnsibleExitJson) as result:
            os.environ['SCHEMATICS_AUTH_TYPE'] = 'noAuth'
            os.environ['IC_API_KEY'] = 'noAuthAPIKey'
            ibm_schematics_workspace.main()

        assert result.exception.args[0]['changed'] is True
        assert result.exception.args[0]['msg']['id'] == 'testString'
        assert result.exception.args[0]['msg']['status'] == 'deleted'

        mock_data = dict(
            refresh_token='testString',
            w_id='testString',
            destroy_resources='testString',
        )

        mock.assert_called_once()
        processed_result = post_process_result(
            mock_data, mock.call_args.kwargs)
        assert mock_data == processed_result

        get_workspace_mock_data = dict(
            w_id='testString',
        )
        # Set the variables that belong to the "read" path to `None`
        # since we test the "delete" path here.
        for param in get_workspace_mock_data:
            get_workspace_mock_data[param] = mock_data.get(param, None)

        get_workspace_mock.assert_called_once()
        get_workspace_processed_result = post_process_result(
            get_workspace_mock_data, get_workspace_mock.call_args.kwargs)
        assert get_workspace_mock_data == get_workspace_processed_result

        get_workspace_patcher.stop()
        patcher.stop()

    def test_delete_ibm_schematics_workspace_not_exists(self):
        """Test the "delete" path - not exists."""
        patcher = patch(
            'plugins.modules.ibm_schematics_workspace.SchematicsV1.delete_workspace')
        mock = patcher.start()
        mock.return_value = DetailedResponseMock()

        get_workspace_patcher = patch(
            'plugins.modules.ibm_schematics_workspace.SchematicsV1.get_workspace')
        get_workspace_mock = get_workspace_patcher.start()
        get_workspace_mock.side_effect = ApiException(404)

        args = {
            'refresh_token': 'testString',
            'w_id': 'testString',
            'destroy_resources': 'testString',
            'state': 'absent',
        }

        set_module_args(args)

        with self.assertRaises(AnsibleExitJson) as result:
            os.environ['SCHEMATICS_AUTH_TYPE'] = 'noAuth'
            os.environ['IC_API_KEY'] = 'noAuthAPIKey'
            ibm_schematics_workspace.main()

        assert result.exception.args[0]['changed'] is False
        assert result.exception.args[0]['msg']['id'] == 'testString'
        assert result.exception.args[0]['msg']['status'] == 'not_found'

        mock_data = dict(
            refresh_token='testString',
            w_id='testString',
            destroy_resources='testString',
        )

        mock.assert_not_called()

        get_workspace_mock_data = dict(
            w_id='testString',
        )
        # Set the variables that belong to the "read" path to `None`
        # since we test the "delete" path here.
        for param in get_workspace_mock_data:
            get_workspace_mock_data[param] = mock_data.get(param, None)

        get_workspace_mock.assert_called_once()
        get_workspace_processed_result = post_process_result(
            get_workspace_mock_data, get_workspace_mock.call_args.kwargs)
        assert get_workspace_mock_data == get_workspace_processed_result

        get_workspace_patcher.stop()
        patcher.stop()

    def test_delete_ibm_schematics_workspace_failed(self):
        """Test the "delete" path - failed."""
        patcher = patch(
            'plugins.modules.ibm_schematics_workspace.SchematicsV1.delete_workspace')
        mock = patcher.start()
        mock.side_effect = ApiException(
            400, message='Delete ibm_schematics_workspace error')

        get_workspace_patcher = patch(
            'plugins.modules.ibm_schematics_workspace.SchematicsV1.get_workspace')
        get_workspace_mock = get_workspace_patcher.start()
        get_workspace_mock.return_value = DetailedResponseMock()

        set_module_args({
            'refresh_token': 'testString',
            'w_id': 'testString',
            'destroy_resources': 'testString',
            'state': 'absent',
        })

        with self.assertRaises(AnsibleFailJson) as result:
            os.environ['SCHEMATICS_AUTH_TYPE'] = 'noAuth'
            os.environ['IC_API_KEY'] = 'noAuthAPIKey'
            ibm_schematics_workspace.main()

        assert result.exception.args[0]['msg'] == 'Delete ibm_schematics_workspace error'

        mock_data = dict(
            refresh_token='testString',
            w_id='testString',
            destroy_resources='testString',
        )

        mock.assert_called_once()
        processed_result = post_process_result(
            mock_data, mock.call_args.kwargs)
        assert mock_data == processed_result

        get_workspace_mock_data = dict(
            w_id='testString',
        )
        # Set the variables that belong to the "read" path to `None`
        # since we test the "delete" path here.
        for param in get_workspace_mock_data:
            get_workspace_mock_data[param] = mock_data.get(param, None)

        get_workspace_mock.assert_called_once()
        get_workspace_processed_result = post_process_result(
            get_workspace_mock_data, get_workspace_mock.call_args.kwargs)
        assert get_workspace_mock_data == get_workspace_processed_result

        get_workspace_patcher.stop()
        patcher.stop()
