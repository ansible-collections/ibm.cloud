# (C) Copyright IBM Corp. 2022.
# GNU General Public License v3.0+ (see LICENSE or https://www.gnu.org/licenses/gpl-3.0.txt)

from __future__ import (absolute_import, division, print_function)
__metaclass__ = type

import os

from .common import DetailedResponseMock
from plugins.modules import ibm_schematics_job
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


class TestJobModule(ModuleTestCase):
    """
    Test class for Job module testing.
    """

    def test_read_ibm_schematics_job_failed(self):
        """Test the inner "read" path in this module with a server error response."""

        patcher = patch(
            'plugins.modules.ibm_schematics_job.SchematicsV1.get_job')
        mock = patcher.start()
        mock.side_effect = ApiException(500, message='Something went wrong...')

        set_module_args({
            'job_id': 'testString',
            'profile': 'summary',
        })

        with self.assertRaises(AnsibleFailJson) as result:
            os.environ['SCHEMATICS_AUTH_TYPE'] = 'noAuth'
            os.environ['IC_API_KEY'] = 'noAuthAPIKey'
            ibm_schematics_job.main()

        assert result.exception.args[0]['msg'] == 'Something went wrong...'

        mock_data = dict(
            job_id='testString',
            profile='summary',
        )

        mock.assert_called_once()
        processed_result = post_process_result(
            mock_data, mock.call_args.kwargs)
        assert mock_data == processed_result

        patcher.stop()

    def test_create_ibm_schematics_job_success(self):
        """Test the "create" path - successful."""
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

        job_status_workitem_model = {
            'workspace_id': 'testString',
            'workspace_name': 'testString',
            'job_id': 'testString',
            'status_code': 'job_pending',
            'status_message': 'testString',
            'updated_at': '2019-01-01T12:00:00.000Z',
        }

        job_status_flow_model = {
            'flow_id': 'testString',
            'flow_name': 'testString',
            'status_code': 'job_pending',
            'status_message': 'testString',
            'workitems': [job_status_workitem_model],
            'updated_at': '2019-01-01T12:00:00.000Z',
        }

        job_status_template_model = {
            'template_id': 'testString',
            'template_name': 'testString',
            'flow_index': 38,
            'status_code': 'job_pending',
            'status_message': 'testString',
            'updated_at': '2019-01-01T12:00:00.000Z',
        }

        job_status_workspace_model = {
            'workspace_name': 'testString',
            'status_code': 'job_pending',
            'status_message': 'testString',
            'flow_status': job_status_flow_model,
            'template_status': [job_status_template_model],
            'updated_at': '2019-01-01T12:00:00.000Z',
        }

        job_status_action_model = {
            'action_name': 'testString',
            'status_code': 'job_pending',
            'status_message': 'testString',
            'bastion_status_code': 'none',
            'bastion_status_message': 'testString',
            'targets_status_code': 'none',
            'targets_status_message': 'testString',
            'updated_at': '2019-01-01T12:00:00.000Z',
        }

        job_status_schematics_resources_model = {
            'status_code': 'job_pending',
            'status_message': 'testString',
            'schematics_resource_id': 'testString',
            'updated_at': '2019-01-01T12:00:00.000Z',
        }

        job_status_system_model = {
            'system_status_message': 'testString',
            'system_status_code': 'job_pending',
            'schematics_resource_status': [job_status_schematics_resources_model],
            'updated_at': '2019-01-01T12:00:00.000Z',
        }

        job_status_model = {
            'position_in_queue': 72.5,
            'total_in_queue': 72.5,
            'workspace_job_status': job_status_workspace_model,
            'action_job_status': job_status_action_model,
            'system_job_status': job_status_system_model,
            'flow_job_status': job_status_flow_model,
        }

        job_data_template_model = {
            'template_id': 'testString',
            'template_name': 'testString',
            'flow_index': 38,
            'inputs': [variable_data_model],
            'outputs': [variable_data_model],
            'settings': [variable_data_model],
            'updated_at': '2019-01-01T12:00:00.000Z',
        }

        job_data_workspace_model = {
            'workspace_name': 'testString',
            'flow_id': 'testString',
            'flow_name': 'testString',
            'inputs': [variable_data_model],
            'outputs': [variable_data_model],
            'settings': [variable_data_model],
            'template_data': [job_data_template_model],
            'updated_at': '2019-01-01T12:00:00.000Z',
        }

        inventory_resource_record_model = {
            'name': 'testString',
            'description': 'testString',
            'location': 'us-south',
            'resource_group': 'testString',
            'inventories_ini': 'testString',
            'resource_queries': ['testString'],
        }

        job_data_action_model = {
            'action_name': 'testString',
            'inputs': [variable_data_model],
            'outputs': [variable_data_model],
            'settings': [variable_data_model],
            'updated_at': '2019-01-01T12:00:00.000Z',
            'inventory_record': inventory_resource_record_model,
            'materialized_inventory': 'testString',
        }

        job_data_system_model = {
            'key_id': 'testString',
            'schematics_resource_id': ['testString'],
            'updated_at': '2019-01-01T12:00:00.000Z',
        }

        git_source_model = {
            'computed_git_repo_url': 'testString',
            'git_repo_url': 'testString',
            'git_token': 'testString',
            'git_repo_folder': 'testString',
            'git_release': 'testString',
            'git_branch': 'testString',
        }

        catalog_source_model = {
            'catalog_name': 'testString',
            'offering_name': 'testString',
            'offering_version': 'testString',
            'offering_kind': 'testString',
            'catalog_id': 'testString',
            'offering_id': 'testString',
            'offering_version_id': 'testString',
            'offering_repo_url': 'testString',
            'offering_provisioner_working_directory': 'testString',
        }

        external_source_model = {
            'source_type': 'local',
            'git': git_source_model,
            'catalog': catalog_source_model,
        }

        job_data_work_item_last_job_model = {
            'command_object': 'workspace',
            'command_object_name': 'testString',
            'command_object_id': 'testString',
            'command_name': 'workspace_plan',
            'job_id': 'testString',
            'job_status': 'job_pending',
        }

        job_data_work_item_model = {
            'command_object_id': 'testString',
            'command_object_name': 'testString',
            'layers': 'testString',
            'source_type': 'local',
            'source': external_source_model,
            'inputs': [variable_data_model],
            'outputs': [variable_data_model],
            'settings': [variable_data_model],
            'last_job': job_data_work_item_last_job_model,
            'updated_at': '2019-01-01T12:00:00.000Z',
        }

        job_data_flow_model = {
            'flow_id': 'testString',
            'flow_name': 'testString',
            'workitems': [job_data_work_item_model],
            'updated_at': '2019-01-01T12:00:00.000Z',
        }

        job_data_model = {
            'job_type': 'repo_download_job',
            'workspace_job_data': job_data_workspace_model,
            'action_job_data': job_data_action_model,
            'system_job_data': job_data_system_model,
            'flow_job_data': job_data_flow_model,
        }

        bastion_resource_definition_model = {
            'name': 'testString',
            'host': 'testString',
        }

        job_log_summary_repo_download_job_model = {
        }

        job_log_summary_workspace_job_model = {
        }

        job_log_summary_workitems_model = {
            'workspace_id': 'testString',
            'job_id': 'testString',
            'log_url': 'testString',
        }

        job_log_summary_flow_job_model = {
            'workitems': [job_log_summary_workitems_model],
        }

        job_log_summary_action_job_recap_model = {
            'target': ['testString'],
            'ok': 72.5,
            'changed': 72.5,
            'failed': 72.5,
            'skipped': 72.5,
            'unreachable': 72.5,
        }

        job_log_summary_action_job_model = {
            'recap': job_log_summary_action_job_recap_model,
        }

        job_log_summary_system_job_model = {
            'success': 72.5,
            'failed': 72.5,
        }

        job_log_summary_model = {
            'job_type': 'repo_download_job',
            'repo_download_job': job_log_summary_repo_download_job_model,
            'workspace_job': job_log_summary_workspace_job_model,
            'flow_job': job_log_summary_flow_job_model,
            'action_job': job_log_summary_action_job_model,
            'system_job': job_log_summary_system_job_model,
        }

        resource = {
            'refresh_token': 'testString',
            'command_object': 'workspace',
            'command_object_id': 'testString',
            'command_name': 'workspace_plan',
            'command_parameter': 'testString',
            'command_options': ['testString'],
            'inputs': [variable_data_model],
            'settings': [variable_data_model],
            'tags': ['testString'],
            'location': 'us-south',
            'status': job_status_model,
            'data': job_data_model,
            'bastion': bastion_resource_definition_model,
            'log_summary': job_log_summary_model,
        }

        patcher = patch(
            'plugins.modules.ibm_schematics_job.SchematicsV1.create_job')
        mock = patcher.start()
        mock.return_value = DetailedResponseMock(resource)

        get_job_patcher = patch(
            'plugins.modules.ibm_schematics_job.SchematicsV1.get_job')
        get_job_mock = get_job_patcher.start()

        set_module_args({
            'refresh_token': 'testString',
            'command_object': 'workspace',
            'command_object_id': 'testString',
            'command_name': 'workspace_plan',
            'command_parameter': 'testString',
            'command_options': ['testString'],
            'inputs': [variable_data_model],
            'settings': [variable_data_model],
            'tags': ['testString'],
            'location': 'us-south',
            'status': job_status_model,
            'data': job_data_model,
            'bastion': bastion_resource_definition_model,
            'log_summary': job_log_summary_model,
        })

        with self.assertRaises(AnsibleExitJson) as result:
            os.environ['SCHEMATICS_AUTH_TYPE'] = 'noAuth'
            os.environ['IC_API_KEY'] = 'noAuthAPIKey'
            ibm_schematics_job.main()

        assert result.exception.args[0]['changed'] is True
        assert result.exception.args[0]['msg'] == resource

        mock_data = dict(
            refresh_token='testString',
            command_object='workspace',
            command_object_id='testString',
            command_name='workspace_plan',
            command_parameter='testString',
            command_options=['testString'],
            inputs=[variable_data_model],
            settings=[variable_data_model],
            tags=['testString'],
            location='us-south',
            status=job_status_model,
            data=job_data_model,
            bastion=bastion_resource_definition_model,
            log_summary=job_log_summary_model,
        )

        mock.assert_called_once()
        processed_result = post_process_result(
            mock_data, mock.call_args.kwargs)
        assert mock_data == processed_result

        get_job_mock.assert_not_called()

        get_job_patcher.stop()
        patcher.stop()

    def test_create_ibm_schematics_job_failed(self):
        """Test the "create" path - failed."""

        get_job_patcher = patch(
            'plugins.modules.ibm_schematics_job.SchematicsV1.get_job')
        get_job_mock = get_job_patcher.start()

        patcher = patch(
            'plugins.modules.ibm_schematics_job.SchematicsV1.create_job')
        mock = patcher.start()
        mock.side_effect = ApiException(
            400, message='Create ibm_schematics_job error')

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

        job_status_workitem_model = {
            'workspace_id': 'testString',
            'workspace_name': 'testString',
            'job_id': 'testString',
            'status_code': 'job_pending',
            'status_message': 'testString',
            'updated_at': '2019-01-01T12:00:00.000Z',
        }

        job_status_flow_model = {
            'flow_id': 'testString',
            'flow_name': 'testString',
            'status_code': 'job_pending',
            'status_message': 'testString',
            'workitems': [job_status_workitem_model],
            'updated_at': '2019-01-01T12:00:00.000Z',
        }

        job_status_template_model = {
            'template_id': 'testString',
            'template_name': 'testString',
            'flow_index': 38,
            'status_code': 'job_pending',
            'status_message': 'testString',
            'updated_at': '2019-01-01T12:00:00.000Z',
        }

        job_status_workspace_model = {
            'workspace_name': 'testString',
            'status_code': 'job_pending',
            'status_message': 'testString',
            'flow_status': job_status_flow_model,
            'template_status': [job_status_template_model],
            'updated_at': '2019-01-01T12:00:00.000Z',
        }

        job_status_action_model = {
            'action_name': 'testString',
            'status_code': 'job_pending',
            'status_message': 'testString',
            'bastion_status_code': 'none',
            'bastion_status_message': 'testString',
            'targets_status_code': 'none',
            'targets_status_message': 'testString',
            'updated_at': '2019-01-01T12:00:00.000Z',
        }

        job_status_schematics_resources_model = {
            'status_code': 'job_pending',
            'status_message': 'testString',
            'schematics_resource_id': 'testString',
            'updated_at': '2019-01-01T12:00:00.000Z',
        }

        job_status_system_model = {
            'system_status_message': 'testString',
            'system_status_code': 'job_pending',
            'schematics_resource_status': [job_status_schematics_resources_model],
            'updated_at': '2019-01-01T12:00:00.000Z',
        }

        job_status_model = {
            'position_in_queue': 72.5,
            'total_in_queue': 72.5,
            'workspace_job_status': job_status_workspace_model,
            'action_job_status': job_status_action_model,
            'system_job_status': job_status_system_model,
            'flow_job_status': job_status_flow_model,
        }

        job_data_template_model = {
            'template_id': 'testString',
            'template_name': 'testString',
            'flow_index': 38,
            'inputs': [variable_data_model],
            'outputs': [variable_data_model],
            'settings': [variable_data_model],
            'updated_at': '2019-01-01T12:00:00.000Z',
        }

        job_data_workspace_model = {
            'workspace_name': 'testString',
            'flow_id': 'testString',
            'flow_name': 'testString',
            'inputs': [variable_data_model],
            'outputs': [variable_data_model],
            'settings': [variable_data_model],
            'template_data': [job_data_template_model],
            'updated_at': '2019-01-01T12:00:00.000Z',
        }

        inventory_resource_record_model = {
            'name': 'testString',
            'description': 'testString',
            'location': 'us-south',
            'resource_group': 'testString',
            'inventories_ini': 'testString',
            'resource_queries': ['testString'],
        }

        job_data_action_model = {
            'action_name': 'testString',
            'inputs': [variable_data_model],
            'outputs': [variable_data_model],
            'settings': [variable_data_model],
            'updated_at': '2019-01-01T12:00:00.000Z',
            'inventory_record': inventory_resource_record_model,
            'materialized_inventory': 'testString',
        }

        job_data_system_model = {
            'key_id': 'testString',
            'schematics_resource_id': ['testString'],
            'updated_at': '2019-01-01T12:00:00.000Z',
        }

        git_source_model = {
            'computed_git_repo_url': 'testString',
            'git_repo_url': 'testString',
            'git_token': 'testString',
            'git_repo_folder': 'testString',
            'git_release': 'testString',
            'git_branch': 'testString',
        }

        catalog_source_model = {
            'catalog_name': 'testString',
            'offering_name': 'testString',
            'offering_version': 'testString',
            'offering_kind': 'testString',
            'catalog_id': 'testString',
            'offering_id': 'testString',
            'offering_version_id': 'testString',
            'offering_repo_url': 'testString',
            'offering_provisioner_working_directory': 'testString',
        }

        external_source_model = {
            'source_type': 'local',
            'git': git_source_model,
            'catalog': catalog_source_model,
        }

        job_data_work_item_last_job_model = {
            'command_object': 'workspace',
            'command_object_name': 'testString',
            'command_object_id': 'testString',
            'command_name': 'workspace_plan',
            'job_id': 'testString',
            'job_status': 'job_pending',
        }

        job_data_work_item_model = {
            'command_object_id': 'testString',
            'command_object_name': 'testString',
            'layers': 'testString',
            'source_type': 'local',
            'source': external_source_model,
            'inputs': [variable_data_model],
            'outputs': [variable_data_model],
            'settings': [variable_data_model],
            'last_job': job_data_work_item_last_job_model,
            'updated_at': '2019-01-01T12:00:00.000Z',
        }

        job_data_flow_model = {
            'flow_id': 'testString',
            'flow_name': 'testString',
            'workitems': [job_data_work_item_model],
            'updated_at': '2019-01-01T12:00:00.000Z',
        }

        job_data_model = {
            'job_type': 'repo_download_job',
            'workspace_job_data': job_data_workspace_model,
            'action_job_data': job_data_action_model,
            'system_job_data': job_data_system_model,
            'flow_job_data': job_data_flow_model,
        }

        bastion_resource_definition_model = {
            'name': 'testString',
            'host': 'testString',
        }

        job_log_summary_repo_download_job_model = {
        }

        job_log_summary_workspace_job_model = {
        }

        job_log_summary_workitems_model = {
            'workspace_id': 'testString',
            'job_id': 'testString',
            'log_url': 'testString',
        }

        job_log_summary_flow_job_model = {
            'workitems': [job_log_summary_workitems_model],
        }

        job_log_summary_action_job_recap_model = {
            'target': ['testString'],
            'ok': 72.5,
            'changed': 72.5,
            'failed': 72.5,
            'skipped': 72.5,
            'unreachable': 72.5,
        }

        job_log_summary_action_job_model = {
            'recap': job_log_summary_action_job_recap_model,
        }

        job_log_summary_system_job_model = {
            'success': 72.5,
            'failed': 72.5,
        }

        job_log_summary_model = {
            'job_type': 'repo_download_job',
            'repo_download_job': job_log_summary_repo_download_job_model,
            'workspace_job': job_log_summary_workspace_job_model,
            'flow_job': job_log_summary_flow_job_model,
            'action_job': job_log_summary_action_job_model,
            'system_job': job_log_summary_system_job_model,
        }

        set_module_args({
            'refresh_token': 'testString',
            'command_object': 'workspace',
            'command_object_id': 'testString',
            'command_name': 'workspace_plan',
            'command_parameter': 'testString',
            'command_options': ['testString'],
            'inputs': [variable_data_model],
            'settings': [variable_data_model],
            'tags': ['testString'],
            'location': 'us-south',
            'status': job_status_model,
            'data': job_data_model,
            'bastion': bastion_resource_definition_model,
            'log_summary': job_log_summary_model,
        })

        with self.assertRaises(AnsibleFailJson) as result:
            os.environ['SCHEMATICS_AUTH_TYPE'] = 'noAuth'
            os.environ['IC_API_KEY'] = 'noAuthAPIKey'
            ibm_schematics_job.main()

        assert result.exception.args[0]['msg'] == 'Create ibm_schematics_job error'

        mock_data = dict(
            refresh_token='testString',
            command_object='workspace',
            command_object_id='testString',
            command_name='workspace_plan',
            command_parameter='testString',
            command_options=['testString'],
            inputs=[variable_data_model],
            settings=[variable_data_model],
            tags=['testString'],
            location='us-south',
            status=job_status_model,
            data=job_data_model,
            bastion=bastion_resource_definition_model,
            log_summary=job_log_summary_model,
        )

        mock.assert_called_once()
        processed_result = post_process_result(
            mock_data, mock.call_args.kwargs)
        assert mock_data == processed_result

        get_job_mock.assert_not_called()

        get_job_patcher.stop()
        patcher.stop()

    def test_update_ibm_schematics_job_success(self):
        """Test the "update" path - successful."""
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

        job_status_workitem_model = {
            'workspace_id': 'testString',
            'workspace_name': 'testString',
            'job_id': 'testString',
            'status_code': 'job_pending',
            'status_message': 'testString',
            'updated_at': '2019-01-01T12:00:00.000Z',
        }

        job_status_flow_model = {
            'flow_id': 'testString',
            'flow_name': 'testString',
            'status_code': 'job_pending',
            'status_message': 'testString',
            'workitems': [job_status_workitem_model],
            'updated_at': '2019-01-01T12:00:00.000Z',
        }

        job_status_template_model = {
            'template_id': 'testString',
            'template_name': 'testString',
            'flow_index': 38,
            'status_code': 'job_pending',
            'status_message': 'testString',
            'updated_at': '2019-01-01T12:00:00.000Z',
        }

        job_status_workspace_model = {
            'workspace_name': 'testString',
            'status_code': 'job_pending',
            'status_message': 'testString',
            'flow_status': job_status_flow_model,
            'template_status': [job_status_template_model],
            'updated_at': '2019-01-01T12:00:00.000Z',
        }

        job_status_action_model = {
            'action_name': 'testString',
            'status_code': 'job_pending',
            'status_message': 'testString',
            'bastion_status_code': 'none',
            'bastion_status_message': 'testString',
            'targets_status_code': 'none',
            'targets_status_message': 'testString',
            'updated_at': '2019-01-01T12:00:00.000Z',
        }

        job_status_schematics_resources_model = {
            'status_code': 'job_pending',
            'status_message': 'testString',
            'schematics_resource_id': 'testString',
            'updated_at': '2019-01-01T12:00:00.000Z',
        }

        job_status_system_model = {
            'system_status_message': 'testString',
            'system_status_code': 'job_pending',
            'schematics_resource_status': [job_status_schematics_resources_model],
            'updated_at': '2019-01-01T12:00:00.000Z',
        }

        job_status_model = {
            'position_in_queue': 72.5,
            'total_in_queue': 72.5,
            'workspace_job_status': job_status_workspace_model,
            'action_job_status': job_status_action_model,
            'system_job_status': job_status_system_model,
            'flow_job_status': job_status_flow_model,
        }

        job_data_template_model = {
            'template_id': 'testString',
            'template_name': 'testString',
            'flow_index': 38,
            'inputs': [variable_data_model],
            'outputs': [variable_data_model],
            'settings': [variable_data_model],
            'updated_at': '2019-01-01T12:00:00.000Z',
        }

        job_data_workspace_model = {
            'workspace_name': 'testString',
            'flow_id': 'testString',
            'flow_name': 'testString',
            'inputs': [variable_data_model],
            'outputs': [variable_data_model],
            'settings': [variable_data_model],
            'template_data': [job_data_template_model],
            'updated_at': '2019-01-01T12:00:00.000Z',
        }

        inventory_resource_record_model = {
            'name': 'testString',
            'description': 'testString',
            'location': 'us-south',
            'resource_group': 'testString',
            'inventories_ini': 'testString',
            'resource_queries': ['testString'],
        }

        job_data_action_model = {
            'action_name': 'testString',
            'inputs': [variable_data_model],
            'outputs': [variable_data_model],
            'settings': [variable_data_model],
            'updated_at': '2019-01-01T12:00:00.000Z',
            'inventory_record': inventory_resource_record_model,
            'materialized_inventory': 'testString',
        }

        job_data_system_model = {
            'key_id': 'testString',
            'schematics_resource_id': ['testString'],
            'updated_at': '2019-01-01T12:00:00.000Z',
        }

        git_source_model = {
            'computed_git_repo_url': 'testString',
            'git_repo_url': 'testString',
            'git_token': 'testString',
            'git_repo_folder': 'testString',
            'git_release': 'testString',
            'git_branch': 'testString',
        }

        catalog_source_model = {
            'catalog_name': 'testString',
            'offering_name': 'testString',
            'offering_version': 'testString',
            'offering_kind': 'testString',
            'catalog_id': 'testString',
            'offering_id': 'testString',
            'offering_version_id': 'testString',
            'offering_repo_url': 'testString',
            'offering_provisioner_working_directory': 'testString',
        }

        external_source_model = {
            'source_type': 'local',
            'git': git_source_model,
            'catalog': catalog_source_model,
        }

        job_data_work_item_last_job_model = {
            'command_object': 'workspace',
            'command_object_name': 'testString',
            'command_object_id': 'testString',
            'command_name': 'workspace_plan',
            'job_id': 'testString',
            'job_status': 'job_pending',
        }

        job_data_work_item_model = {
            'command_object_id': 'testString',
            'command_object_name': 'testString',
            'layers': 'testString',
            'source_type': 'local',
            'source': external_source_model,
            'inputs': [variable_data_model],
            'outputs': [variable_data_model],
            'settings': [variable_data_model],
            'last_job': job_data_work_item_last_job_model,
            'updated_at': '2019-01-01T12:00:00.000Z',
        }

        job_data_flow_model = {
            'flow_id': 'testString',
            'flow_name': 'testString',
            'workitems': [job_data_work_item_model],
            'updated_at': '2019-01-01T12:00:00.000Z',
        }

        job_data_model = {
            'job_type': 'repo_download_job',
            'workspace_job_data': job_data_workspace_model,
            'action_job_data': job_data_action_model,
            'system_job_data': job_data_system_model,
            'flow_job_data': job_data_flow_model,
        }

        bastion_resource_definition_model = {
            'name': 'testString',
            'host': 'testString',
        }

        job_log_summary_repo_download_job_model = {
        }

        job_log_summary_workspace_job_model = {
        }

        job_log_summary_workitems_model = {
            'workspace_id': 'testString',
            'job_id': 'testString',
            'log_url': 'testString',
        }

        job_log_summary_flow_job_model = {
            'workitems': [job_log_summary_workitems_model],
        }

        job_log_summary_action_job_recap_model = {
            'target': ['testString'],
            'ok': 72.5,
            'changed': 72.5,
            'failed': 72.5,
            'skipped': 72.5,
            'unreachable': 72.5,
        }

        job_log_summary_action_job_model = {
            'recap': job_log_summary_action_job_recap_model,
        }

        job_log_summary_system_job_model = {
            'success': 72.5,
            'failed': 72.5,
        }

        job_log_summary_model = {
            'job_type': 'repo_download_job',
            'repo_download_job': job_log_summary_repo_download_job_model,
            'workspace_job': job_log_summary_workspace_job_model,
            'flow_job': job_log_summary_flow_job_model,
            'action_job': job_log_summary_action_job_model,
            'system_job': job_log_summary_system_job_model,
        }

        resource = {
            'job_id': 'testString',
            'refresh_token': 'testString',
            'command_object': 'workspace',
            'command_object_id': 'testString',
            'command_name': 'workspace_plan',
            'command_parameter': 'testString',
            'command_options': ['testString'],
            'inputs': [variable_data_model],
            'settings': [variable_data_model],
            'tags': ['testString'],
            'location': 'us-south',
            'status': job_status_model,
            'data': job_data_model,
            'bastion': bastion_resource_definition_model,
            'log_summary': job_log_summary_model,
        }

        patcher = patch(
            'plugins.modules.ibm_schematics_job.SchematicsV1.update_job')
        mock = patcher.start()
        mock.return_value = DetailedResponseMock(resource)

        get_job_patcher = patch(
            'plugins.modules.ibm_schematics_job.SchematicsV1.get_job')
        get_job_mock = get_job_patcher.start()
        get_job_mock.return_value = DetailedResponseMock(resource)

        set_module_args({
            'job_id': 'testString',
            'refresh_token': 'testString',
            'command_object': 'workspace',
            'command_object_id': 'testString',
            'command_name': 'workspace_plan',
            'command_parameter': 'testString',
            'command_options': ['testString'],
            'inputs': [variable_data_model],
            'settings': [variable_data_model],
            'tags': ['testString'],
            'location': 'us-south',
            'status': job_status_model,
            'data': job_data_model,
            'bastion': bastion_resource_definition_model,
            'log_summary': job_log_summary_model,
        })

        with self.assertRaises(AnsibleExitJson) as result:
            os.environ['SCHEMATICS_AUTH_TYPE'] = 'noAuth'
            os.environ['IC_API_KEY'] = 'noAuthAPIKey'
            ibm_schematics_job.main()

        assert result.exception.args[0]['changed'] is True
        assert result.exception.args[0]['msg'] == resource

        mock_data = dict(
            job_id='testString',
            refresh_token='testString',
            command_object='workspace',
            command_object_id='testString',
            command_name='workspace_plan',
            command_parameter='testString',
            command_options=['testString'],
            inputs=[variable_data_model],
            settings=[variable_data_model],
            tags=['testString'],
            location='us-south',
            status=job_status_model,
            data=job_data_model,
            bastion=bastion_resource_definition_model,
            log_summary=job_log_summary_model,
        )

        mock.assert_called_once()
        processed_result = post_process_result(
            mock_data, mock.call_args.kwargs)
        assert mock_data == processed_result

        get_job_mock_data = dict(
            job_id='testString',
            profile='summary',
        )
        # Set the variables that belong to the "read" path to `None`
        # since we test the "delete" path here.
        for param in get_job_mock_data:
            get_job_mock_data[param] = mock_data.get(param, None)

        get_job_mock.assert_called_once()
        get_job_processed_result = post_process_result(
            get_job_mock_data, get_job_mock.call_args.kwargs)
        assert get_job_mock_data == get_job_processed_result
        get_job_patcher.stop()
        patcher.stop()

    def test_update_ibm_schematics_job_failed(self):
        """Test the "update" path - failed."""
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

        job_status_workitem_model = {
            'workspace_id': 'testString',
            'workspace_name': 'testString',
            'job_id': 'testString',
            'status_code': 'job_pending',
            'status_message': 'testString',
            'updated_at': '2019-01-01T12:00:00.000Z',
        }

        job_status_flow_model = {
            'flow_id': 'testString',
            'flow_name': 'testString',
            'status_code': 'job_pending',
            'status_message': 'testString',
            'workitems': [job_status_workitem_model],
            'updated_at': '2019-01-01T12:00:00.000Z',
        }

        job_status_template_model = {
            'template_id': 'testString',
            'template_name': 'testString',
            'flow_index': 38,
            'status_code': 'job_pending',
            'status_message': 'testString',
            'updated_at': '2019-01-01T12:00:00.000Z',
        }

        job_status_workspace_model = {
            'workspace_name': 'testString',
            'status_code': 'job_pending',
            'status_message': 'testString',
            'flow_status': job_status_flow_model,
            'template_status': [job_status_template_model],
            'updated_at': '2019-01-01T12:00:00.000Z',
        }

        job_status_action_model = {
            'action_name': 'testString',
            'status_code': 'job_pending',
            'status_message': 'testString',
            'bastion_status_code': 'none',
            'bastion_status_message': 'testString',
            'targets_status_code': 'none',
            'targets_status_message': 'testString',
            'updated_at': '2019-01-01T12:00:00.000Z',
        }

        job_status_schematics_resources_model = {
            'status_code': 'job_pending',
            'status_message': 'testString',
            'schematics_resource_id': 'testString',
            'updated_at': '2019-01-01T12:00:00.000Z',
        }

        job_status_system_model = {
            'system_status_message': 'testString',
            'system_status_code': 'job_pending',
            'schematics_resource_status': [job_status_schematics_resources_model],
            'updated_at': '2019-01-01T12:00:00.000Z',
        }

        job_status_model = {
            'position_in_queue': 72.5,
            'total_in_queue': 72.5,
            'workspace_job_status': job_status_workspace_model,
            'action_job_status': job_status_action_model,
            'system_job_status': job_status_system_model,
            'flow_job_status': job_status_flow_model,
        }

        job_data_template_model = {
            'template_id': 'testString',
            'template_name': 'testString',
            'flow_index': 38,
            'inputs': [variable_data_model],
            'outputs': [variable_data_model],
            'settings': [variable_data_model],
            'updated_at': '2019-01-01T12:00:00.000Z',
        }

        job_data_workspace_model = {
            'workspace_name': 'testString',
            'flow_id': 'testString',
            'flow_name': 'testString',
            'inputs': [variable_data_model],
            'outputs': [variable_data_model],
            'settings': [variable_data_model],
            'template_data': [job_data_template_model],
            'updated_at': '2019-01-01T12:00:00.000Z',
        }

        inventory_resource_record_model = {
            'name': 'testString',
            'description': 'testString',
            'location': 'us-south',
            'resource_group': 'testString',
            'inventories_ini': 'testString',
            'resource_queries': ['testString'],
        }

        job_data_action_model = {
            'action_name': 'testString',
            'inputs': [variable_data_model],
            'outputs': [variable_data_model],
            'settings': [variable_data_model],
            'updated_at': '2019-01-01T12:00:00.000Z',
            'inventory_record': inventory_resource_record_model,
            'materialized_inventory': 'testString',
        }

        job_data_system_model = {
            'key_id': 'testString',
            'schematics_resource_id': ['testString'],
            'updated_at': '2019-01-01T12:00:00.000Z',
        }

        git_source_model = {
            'computed_git_repo_url': 'testString',
            'git_repo_url': 'testString',
            'git_token': 'testString',
            'git_repo_folder': 'testString',
            'git_release': 'testString',
            'git_branch': 'testString',
        }

        catalog_source_model = {
            'catalog_name': 'testString',
            'offering_name': 'testString',
            'offering_version': 'testString',
            'offering_kind': 'testString',
            'catalog_id': 'testString',
            'offering_id': 'testString',
            'offering_version_id': 'testString',
            'offering_repo_url': 'testString',
            'offering_provisioner_working_directory': 'testString',
        }

        external_source_model = {
            'source_type': 'local',
            'git': git_source_model,
            'catalog': catalog_source_model,
        }

        job_data_work_item_last_job_model = {
            'command_object': 'workspace',
            'command_object_name': 'testString',
            'command_object_id': 'testString',
            'command_name': 'workspace_plan',
            'job_id': 'testString',
            'job_status': 'job_pending',
        }

        job_data_work_item_model = {
            'command_object_id': 'testString',
            'command_object_name': 'testString',
            'layers': 'testString',
            'source_type': 'local',
            'source': external_source_model,
            'inputs': [variable_data_model],
            'outputs': [variable_data_model],
            'settings': [variable_data_model],
            'last_job': job_data_work_item_last_job_model,
            'updated_at': '2019-01-01T12:00:00.000Z',
        }

        job_data_flow_model = {
            'flow_id': 'testString',
            'flow_name': 'testString',
            'workitems': [job_data_work_item_model],
            'updated_at': '2019-01-01T12:00:00.000Z',
        }

        job_data_model = {
            'job_type': 'repo_download_job',
            'workspace_job_data': job_data_workspace_model,
            'action_job_data': job_data_action_model,
            'system_job_data': job_data_system_model,
            'flow_job_data': job_data_flow_model,
        }

        bastion_resource_definition_model = {
            'name': 'testString',
            'host': 'testString',
        }

        job_log_summary_repo_download_job_model = {
        }

        job_log_summary_workspace_job_model = {
        }

        job_log_summary_workitems_model = {
            'workspace_id': 'testString',
            'job_id': 'testString',
            'log_url': 'testString',
        }

        job_log_summary_flow_job_model = {
            'workitems': [job_log_summary_workitems_model],
        }

        job_log_summary_action_job_recap_model = {
            'target': ['testString'],
            'ok': 72.5,
            'changed': 72.5,
            'failed': 72.5,
            'skipped': 72.5,
            'unreachable': 72.5,
        }

        job_log_summary_action_job_model = {
            'recap': job_log_summary_action_job_recap_model,
        }

        job_log_summary_system_job_model = {
            'success': 72.5,
            'failed': 72.5,
        }

        job_log_summary_model = {
            'job_type': 'repo_download_job',
            'repo_download_job': job_log_summary_repo_download_job_model,
            'workspace_job': job_log_summary_workspace_job_model,
            'flow_job': job_log_summary_flow_job_model,
            'action_job': job_log_summary_action_job_model,
            'system_job': job_log_summary_system_job_model,
        }

        resource = {
            'job_id': 'testString',
            'refresh_token': 'testString',
            'command_object': 'workspace',
            'command_object_id': 'testString',
            'command_name': 'workspace_plan',
            'command_parameter': 'testString',
            'command_options': ['testString'],
            'inputs': [variable_data_model],
            'settings': [variable_data_model],
            'tags': ['testString'],
            'location': 'us-south',
            'status': job_status_model,
            'data': job_data_model,
            'bastion': bastion_resource_definition_model,
            'log_summary': job_log_summary_model,
        }

        patcher = patch(
            'plugins.modules.ibm_schematics_job.SchematicsV1.update_job')
        mock = patcher.start()
        mock.side_effect = ApiException(
            400, message='Update ibm_schematics_job error')

        get_job_patcher = patch(
            'plugins.modules.ibm_schematics_job.SchematicsV1.get_job')
        get_job_mock = get_job_patcher.start()
        get_job_mock.return_value = DetailedResponseMock(resource)

        set_module_args({
            'job_id': 'testString',
            'refresh_token': 'testString',
            'command_object': 'workspace',
            'command_object_id': 'testString',
            'command_name': 'workspace_plan',
            'command_parameter': 'testString',
            'command_options': ['testString'],
            'inputs': [variable_data_model],
            'settings': [variable_data_model],
            'tags': ['testString'],
            'location': 'us-south',
            'status': job_status_model,
            'data': job_data_model,
            'bastion': bastion_resource_definition_model,
            'log_summary': job_log_summary_model,
        })

        with self.assertRaises(AnsibleFailJson) as result:
            os.environ['SCHEMATICS_AUTH_TYPE'] = 'noAuth'
            os.environ['IC_API_KEY'] = 'noAuthAPIKey'
            ibm_schematics_job.main()

        assert result.exception.args[0]['msg'] == 'Update ibm_schematics_job error'

        mock_data = dict(
            job_id='testString',
            refresh_token='testString',
            command_object='workspace',
            command_object_id='testString',
            command_name='workspace_plan',
            command_parameter='testString',
            command_options=['testString'],
            inputs=[variable_data_model],
            settings=[variable_data_model],
            tags=['testString'],
            location='us-south',
            status=job_status_model,
            data=job_data_model,
            bastion=bastion_resource_definition_model,
            log_summary=job_log_summary_model,
        )

        mock.assert_called_once()
        processed_result = post_process_result(
            mock_data, mock.call_args.kwargs)
        assert mock_data == processed_result

        get_job_mock_data = dict(
            job_id='testString',
            profile='summary',
        )
        # Set the variables that belong to the "read" path to `None`
        # since we test the "delete" path here.
        for param in get_job_mock_data:
            get_job_mock_data[param] = mock_data.get(param, None)

        get_job_mock.assert_called_once()
        get_job_processed_result = post_process_result(
            get_job_mock_data, get_job_mock.call_args.kwargs)
        assert get_job_mock_data == get_job_processed_result

        get_job_patcher.stop()
        patcher.stop()

    def test_delete_ibm_schematics_job_success(self):
        """Test the "delete" path - successfull."""
        patcher = patch(
            'plugins.modules.ibm_schematics_job.SchematicsV1.delete_job')
        mock = patcher.start()
        mock.return_value = DetailedResponseMock()

        get_job_patcher = patch(
            'plugins.modules.ibm_schematics_job.SchematicsV1.get_job')
        get_job_mock = get_job_patcher.start()
        get_job_mock.return_value = DetailedResponseMock()

        args = {
            'job_id': 'testString',
            'refresh_token': 'testString',
            'force': True,
            'propagate': True,
            'state': 'absent',
        }

        set_module_args(args)

        with self.assertRaises(AnsibleExitJson) as result:
            os.environ['SCHEMATICS_AUTH_TYPE'] = 'noAuth'
            os.environ['IC_API_KEY'] = 'noAuthAPIKey'
            ibm_schematics_job.main()

        assert result.exception.args[0]['changed'] is True
        assert result.exception.args[0]['msg']['id'] == 'testString'
        assert result.exception.args[0]['msg']['status'] == 'deleted'

        mock_data = dict(
            job_id='testString',
            refresh_token='testString',
            force=True,
            propagate=True,
        )

        mock.assert_called_once()
        processed_result = post_process_result(
            mock_data, mock.call_args.kwargs)
        assert mock_data == processed_result

        get_job_mock_data = dict(
            job_id='testString',
            profile='summary',
        )
        # Set the variables that belong to the "read" path to `None`
        # since we test the "delete" path here.
        for param in get_job_mock_data:
            get_job_mock_data[param] = mock_data.get(param, None)

        get_job_mock.assert_called_once()
        get_job_processed_result = post_process_result(
            get_job_mock_data, get_job_mock.call_args.kwargs)
        assert get_job_mock_data == get_job_processed_result

        get_job_patcher.stop()
        patcher.stop()

    def test_delete_ibm_schematics_job_not_exists(self):
        """Test the "delete" path - not exists."""
        patcher = patch(
            'plugins.modules.ibm_schematics_job.SchematicsV1.delete_job')
        mock = patcher.start()
        mock.return_value = DetailedResponseMock()

        get_job_patcher = patch(
            'plugins.modules.ibm_schematics_job.SchematicsV1.get_job')
        get_job_mock = get_job_patcher.start()
        get_job_mock.side_effect = ApiException(404)

        args = {
            'job_id': 'testString',
            'refresh_token': 'testString',
            'force': True,
            'propagate': True,
            'state': 'absent',
        }

        set_module_args(args)

        with self.assertRaises(AnsibleExitJson) as result:
            os.environ['SCHEMATICS_AUTH_TYPE'] = 'noAuth'
            os.environ['IC_API_KEY'] = 'noAuthAPIKey'
            ibm_schematics_job.main()

        assert result.exception.args[0]['changed'] is False
        assert result.exception.args[0]['msg']['id'] == 'testString'
        assert result.exception.args[0]['msg']['status'] == 'not_found'

        mock_data = dict(
            job_id='testString',
            refresh_token='testString',
            force=True,
            propagate=True,
        )

        mock.assert_not_called()

        get_job_mock_data = dict(
            job_id='testString',
            profile='summary',
        )
        # Set the variables that belong to the "read" path to `None`
        # since we test the "delete" path here.
        for param in get_job_mock_data:
            get_job_mock_data[param] = mock_data.get(param, None)

        get_job_mock.assert_called_once()
        get_job_processed_result = post_process_result(
            get_job_mock_data, get_job_mock.call_args.kwargs)
        assert get_job_mock_data == get_job_processed_result

        get_job_patcher.stop()
        patcher.stop()

    def test_delete_ibm_schematics_job_failed(self):
        """Test the "delete" path - failed."""
        patcher = patch(
            'plugins.modules.ibm_schematics_job.SchematicsV1.delete_job')
        mock = patcher.start()
        mock.side_effect = ApiException(
            400, message='Delete ibm_schematics_job error')

        get_job_patcher = patch(
            'plugins.modules.ibm_schematics_job.SchematicsV1.get_job')
        get_job_mock = get_job_patcher.start()
        get_job_mock.return_value = DetailedResponseMock()

        set_module_args({
            'job_id': 'testString',
            'refresh_token': 'testString',
            'force': True,
            'propagate': True,
            'state': 'absent',
        })

        with self.assertRaises(AnsibleFailJson) as result:
            os.environ['SCHEMATICS_AUTH_TYPE'] = 'noAuth'
            os.environ['IC_API_KEY'] = 'noAuthAPIKey'
            ibm_schematics_job.main()

        assert result.exception.args[0]['msg'] == 'Delete ibm_schematics_job error'

        mock_data = dict(
            job_id='testString',
            refresh_token='testString',
            force=True,
            propagate=True,
        )

        mock.assert_called_once()
        processed_result = post_process_result(
            mock_data, mock.call_args.kwargs)
        assert mock_data == processed_result

        get_job_mock_data = dict(
            job_id='testString',
            profile='summary',
        )
        # Set the variables that belong to the "read" path to `None`
        # since we test the "delete" path here.
        for param in get_job_mock_data:
            get_job_mock_data[param] = mock_data.get(param, None)

        get_job_mock.assert_called_once()
        get_job_processed_result = post_process_result(
            get_job_mock_data, get_job_mock.call_args.kwargs)
        assert get_job_mock_data == get_job_processed_result

        get_job_patcher.stop()
        patcher.stop()
