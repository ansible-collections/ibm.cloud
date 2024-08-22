# (C) Copyright IBM Corp. 2024.
#
# GNU General Public License v3.0+ (see LICENSE or https://www.gnu.org/licenses/gpl-3.0.txt)

from __future__ import (absolute_import, division, print_function)
__metaclass__ = type

import os

from ansible_collections.community.internal_test_tools.tests.unit.compat.mock import patch
from ansible_collections.community.internal_test_tools.tests.unit.plugins.modules.utils import ModuleTestCase, AnsibleFailJson, AnsibleExitJson, set_module_args
from plugins.modules import ibm_schematics_job

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
        self.assertIsNone(ibm_schematics_job.MISSING_IMPORT_EXC)

        # Set-up mocks for each operation.
        self.read_patcher = patch('plugins.modules.ibm_schematics_job.SchematicsV1.get_job')
        self.read_mock = self.read_patcher.start()
        self.create_patcher = patch('plugins.modules.ibm_schematics_job.SchematicsV1.create_job')
        self.create_mock = self.create_patcher.start()
        self.update_patcher = patch('plugins.modules.ibm_schematics_job.SchematicsV1.update_job')
        self.update_mock = self.update_patcher.start()
        self.delete_patcher = patch('plugins.modules.ibm_schematics_job.SchematicsV1.delete_job')
        self.delete_mock = self.delete_patcher.start()

        # Run the actual function.
        func(self)

        # Stop the patchers.
        self.read_patcher.stop()
        self.create_patcher.stop()
        self.update_patcher.stop()
        self.delete_patcher.stop()

    return wrapper


class TestJobModule(ModuleTestCase):
    """
    Test class for Job module testing.
    """

    @mock_operations
    def test_read_ibm_schematics_job_failed(self):
        """Test the inner "read" path in this module with a server error response."""
        self.read_mock.side_effect = ApiException(500, message='Something went wrong...')

        set_module_args({
            'job_id': 'testString',
            'profile': 'summary',
        })

        with self.assertRaises(AnsibleFailJson) as result:
            os.environ['SCHEMATICS_AUTH_TYPE'] = 'noAuth'
            ibm_schematics_job.main()

        self.assertEqual(result.exception.args[0]['msg'], 'Something went wrong...')

        mock_data = dict(
            job_id='testString',
            profile='summary',
        )

        self.read_mock.assert_called_once()
        self.assertTrue(checkResult(mock_data, self.read_mock.call_args.kwargs))

    @mock_operations
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

        cart_order_data_model = {
            'name': 'testString',
            'value': 'testString',
            'type': 'testString',
            'usage_kind': ['servicetags'],
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
            'catalog_id': 'testString',
            'offering_name': 'testString',
            'offering_version': 'testString',
            'offering_kind': 'testString',
            'offering_target_kind': 'testString',
            'offering_id': 'testString',
            'offering_version_id': 'testString',
            'offering_version_flavour_name': 'testString',
            'offering_repo_url': 'testString',
            'offering_provisioner_working_directory': 'testString',
            'dry_run': True,
            'owning_account': 'testString',
            'item_icon_url': 'testString',
            'item_id': 'testString',
            'item_name': 'testString',
            'item_readme_url': 'testString',
            'item_url': 'testString',
            'launch_url': 'testString',
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

        agent_info_model = {
            'id': 'testString',
            'name': 'testString',
            'assignment_policy_id': 'testString',
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
            'cart_order_data': [cart_order_data_model],
            'data': job_data_model,
            'bastion': bastion_resource_definition_model,
            'log_summary': job_log_summary_model,
            'agent': agent_info_model,
        }

        self.read_mock.side_effect = ApiException(404)
        self.create_mock.return_value = DetailedResponseMock(resource)

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
            'schematics_job_status': job_status_model,
            'cart_order_data': [cart_order_data_model],
            'data': job_data_model,
            'bastion': bastion_resource_definition_model,
            'log_summary': job_log_summary_model,
            'agent': agent_info_model,
        })

        with self.assertRaises(AnsibleExitJson) as result:
            os.environ['SCHEMATICS_AUTH_TYPE'] = 'noAuth'
            ibm_schematics_job.main()

        self.assertTrue(result.exception.args[0]['changed'])
        for field, value in resource.items():
            self.assertEqual(value, result.exception.args[0].get(field))

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
            cart_order_data=[cart_order_data_model],
            data=job_data_model,
            bastion=bastion_resource_definition_model,
            log_summary=job_log_summary_model,
            agent=agent_info_model,
        )

        self.create_mock.assert_called_once()
        self.assertTrue(checkResult(mock_data, self.create_mock.call_args.kwargs))

    @mock_operations
    def test_create_ibm_schematics_job_failed(self):
        """Test the "create" path - failed."""
        self.read_mock.side_effect = ApiException(404)
        self.create_mock.side_effect = ApiException(400, message='Create ibm_schematics_job error')

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

        cart_order_data_model = {
            'name': 'testString',
            'value': 'testString',
            'type': 'testString',
            'usage_kind': ['servicetags'],
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
            'catalog_id': 'testString',
            'offering_name': 'testString',
            'offering_version': 'testString',
            'offering_kind': 'testString',
            'offering_target_kind': 'testString',
            'offering_id': 'testString',
            'offering_version_id': 'testString',
            'offering_version_flavour_name': 'testString',
            'offering_repo_url': 'testString',
            'offering_provisioner_working_directory': 'testString',
            'dry_run': True,
            'owning_account': 'testString',
            'item_icon_url': 'testString',
            'item_id': 'testString',
            'item_name': 'testString',
            'item_readme_url': 'testString',
            'item_url': 'testString',
            'launch_url': 'testString',
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

        agent_info_model = {
            'id': 'testString',
            'name': 'testString',
            'assignment_policy_id': 'testString',
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
            'schematics_job_status': job_status_model,
            'cart_order_data': [cart_order_data_model],
            'data': job_data_model,
            'bastion': bastion_resource_definition_model,
            'log_summary': job_log_summary_model,
            'agent': agent_info_model,
        })

        with self.assertRaises(AnsibleFailJson) as result:
            os.environ['SCHEMATICS_AUTH_TYPE'] = 'noAuth'
            ibm_schematics_job.main()

        self.assertEqual(result.exception.args[0]['msg'], 'Create ibm_schematics_job error')

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
            cart_order_data=[cart_order_data_model],
            data=job_data_model,
            bastion=bastion_resource_definition_model,
            log_summary=job_log_summary_model,
            agent=agent_info_model,
        )

        self.create_mock.assert_called_once()
        self.assertTrue(checkResult(mock_data, self.create_mock.call_args.kwargs))

    @mock_operations
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

        cart_order_data_model = {
            'name': 'testString',
            'value': 'testString',
            'type': 'testString',
            'usage_kind': ['servicetags'],
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
            'catalog_id': 'testString',
            'offering_name': 'testString',
            'offering_version': 'testString',
            'offering_kind': 'testString',
            'offering_target_kind': 'testString',
            'offering_id': 'testString',
            'offering_version_id': 'testString',
            'offering_version_flavour_name': 'testString',
            'offering_repo_url': 'testString',
            'offering_provisioner_working_directory': 'testString',
            'dry_run': True,
            'owning_account': 'testString',
            'item_icon_url': 'testString',
            'item_id': 'testString',
            'item_name': 'testString',
            'item_readme_url': 'testString',
            'item_url': 'testString',
            'launch_url': 'testString',
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

        agent_info_model = {
            'id': 'testString',
            'name': 'testString',
            'assignment_policy_id': 'testString',
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
            'schematics_job_status': job_status_model,
            'cart_order_data': [cart_order_data_model],
            'data': job_data_model,
            'bastion': bastion_resource_definition_model,
            'log_summary': job_log_summary_model,
            'agent': agent_info_model,
        }

        self.read_mock.return_value = DetailedResponseMock(resource)
        self.update_mock.return_value = DetailedResponseMock(resource)

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
            'schematics_job_status': job_status_model,
            'cart_order_data': [cart_order_data_model],
            'data': job_data_model,
            'bastion': bastion_resource_definition_model,
            'log_summary': job_log_summary_model,
            'agent': agent_info_model,
        })

        with self.assertRaises(AnsibleExitJson) as result:
            os.environ['SCHEMATICS_AUTH_TYPE'] = 'noAuth'
            ibm_schematics_job.main()

        self.assertTrue(result.exception.args[0]['changed'])
        for field, value in resource.items():
            self.assertEqual(value, result.exception.args[0].get(field))

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
            cart_order_data=[cart_order_data_model],
            data=job_data_model,
            bastion=bastion_resource_definition_model,
            log_summary=job_log_summary_model,
            agent=agent_info_model,
        )

        self.update_mock.assert_called_once()
        self.assertTrue(checkResult(mock_data, self.update_mock.call_args.kwargs))

        read_mock_data = dict(
            job_id='testString',
            profile='summary',
        )
        # Set the variables that belong to the "read" path to `None`
        # because we test the "update" path here.
        for param in read_mock_data:
            read_mock_data[param] = mock_data.get(param, None)

        self.read_mock.assert_called_once()
        self.assertTrue(checkResult(read_mock_data, self.read_mock.call_args.kwargs))

    @mock_operations
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

        cart_order_data_model = {
            'name': 'testString',
            'value': 'testString',
            'type': 'testString',
            'usage_kind': ['servicetags'],
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
            'catalog_id': 'testString',
            'offering_name': 'testString',
            'offering_version': 'testString',
            'offering_kind': 'testString',
            'offering_target_kind': 'testString',
            'offering_id': 'testString',
            'offering_version_id': 'testString',
            'offering_version_flavour_name': 'testString',
            'offering_repo_url': 'testString',
            'offering_provisioner_working_directory': 'testString',
            'dry_run': True,
            'owning_account': 'testString',
            'item_icon_url': 'testString',
            'item_id': 'testString',
            'item_name': 'testString',
            'item_readme_url': 'testString',
            'item_url': 'testString',
            'launch_url': 'testString',
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

        agent_info_model = {
            'id': 'testString',
            'name': 'testString',
            'assignment_policy_id': 'testString',
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
            'schematics_job_status': job_status_model,
            'cart_order_data': [cart_order_data_model],
            'data': job_data_model,
            'bastion': bastion_resource_definition_model,
            'log_summary': job_log_summary_model,
            'agent': agent_info_model,
        }

        self.read_mock.return_value = DetailedResponseMock(resource)
        self.update_mock.side_effect = ApiException(400, message='Update ibm_schematics_job error')

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
            'schematics_job_status': job_status_model,
            'cart_order_data': [cart_order_data_model],
            'data': job_data_model,
            'bastion': bastion_resource_definition_model,
            'log_summary': job_log_summary_model,
            'agent': agent_info_model,
        })

        with self.assertRaises(AnsibleFailJson) as result:
            os.environ['SCHEMATICS_AUTH_TYPE'] = 'noAuth'
            ibm_schematics_job.main()

        self.assertEqual(result.exception.args[0]['msg'], 'Update ibm_schematics_job error')

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
            cart_order_data=[cart_order_data_model],
            data=job_data_model,
            bastion=bastion_resource_definition_model,
            log_summary=job_log_summary_model,
            agent=agent_info_model,
        )

        self.update_mock.assert_called_once()
        self.assertTrue(checkResult(mock_data, self.update_mock.call_args.kwargs))

        read_mock_data = dict(
            job_id='testString',
            profile='summary',
        )
        # Set the variables that belong to the "read" path to `None`
        # because we test the "update" path here.
        for param in read_mock_data:
            read_mock_data[param] = mock_data.get(param, None)

        self.read_mock.assert_called_once()
        self.assertTrue(checkResult(read_mock_data, self.read_mock.call_args.kwargs))

    @mock_operations
    def test_delete_ibm_schematics_job_success(self):
        """Test the "delete" path - successfull."""
        self.read_mock.return_value = DetailedResponseMock()
        self.delete_mock.return_value = DetailedResponseMock()

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
            ibm_schematics_job.main()

        self.assertTrue(result.exception.args[0]['changed'])
        self.assertEqual(result.exception.args[0]['id'], 'testString')
        self.assertEqual(result.exception.args[0]['status'], 'deleted')

        mock_data = dict(
            job_id='testString',
            refresh_token='testString',
            force=True,
            propagate=True,
        )

        self.delete_mock.assert_called_once()
        self.assertTrue(checkResult(mock_data, self.delete_mock.call_args.kwargs))

        read_mock_data = dict(
            job_id='testString',
            profile='summary',
        )
        # Set the variables that belong to the "read" path to `None`
        # because we test the "delete" path here.
        for param in read_mock_data:
            read_mock_data[param] = mock_data.get(param, None)

        self.read_mock.assert_called_once()
        self.assertTrue(checkResult(read_mock_data, self.read_mock.call_args.kwargs))

    @mock_operations
    def test_delete_ibm_schematics_job_not_exists(self):
        """Test the "delete" path - not exists."""
        self.read_mock.side_effect = ApiException(404)
        self.delete_mock.return_value = DetailedResponseMock()

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
            ibm_schematics_job.main()

        self.assertFalse(result.exception.args[0]['changed'])
        self.assertEqual(result.exception.args[0]['id'], 'testString')
        self.assertEqual(result.exception.args[0]['status'], 'not_found')

        mock_data = dict(
            job_id='testString',
            refresh_token='testString',
            force=True,
            propagate=True,
        )

        self.delete_mock.assert_not_called()

        read_mock_data = dict(
            job_id='testString',
            profile='summary',
        )
        # Set the variables that belong to the "read" path to `None`
        # because we test the "delete" path here.
        for param in read_mock_data:
            read_mock_data[param] = mock_data.get(param, None)

        self.read_mock.assert_called_once()
        self.assertTrue(checkResult(read_mock_data, self.read_mock.call_args.kwargs))

    @mock_operations
    def test_delete_ibm_schematics_job_failed(self):
        """Test the "delete" path - failed."""
        self.read_mock.return_value = DetailedResponseMock()
        self.delete_mock.side_effect = ApiException(400, message='Delete ibm_schematics_job error')

        set_module_args({
            'job_id': 'testString',
            'refresh_token': 'testString',
            'force': True,
            'propagate': True,
            'state': 'absent',
        })

        with self.assertRaises(AnsibleFailJson) as result:
            os.environ['SCHEMATICS_AUTH_TYPE'] = 'noAuth'
            ibm_schematics_job.main()

        self.assertEqual(result.exception.args[0]['msg'], 'Delete ibm_schematics_job error')

        mock_data = dict(
            job_id='testString',
            refresh_token='testString',
            force=True,
            propagate=True,
        )

        self.delete_mock.assert_called_once()
        self.assertTrue(checkResult(mock_data, self.delete_mock.call_args.kwargs))

        read_mock_data = dict(
            job_id='testString',
            profile='summary',
        )
        # Set the variables that belong to the "read" path to `None`
        # because we test the "delete" path here.
        for param in read_mock_data:
            read_mock_data[param] = mock_data.get(param, None)

        self.read_mock.assert_called_once()
        self.assertTrue(checkResult(read_mock_data, self.read_mock.call_args.kwargs))
