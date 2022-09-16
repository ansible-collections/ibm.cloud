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

from __future__ import (absolute_import, division, print_function)
__metaclass__ = type

import os

from .common import DetailedResponseMock
from plugins.modules import ibm_schematics_action
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


class TestActionModule(ModuleTestCase):
    """
    Test class for Action module testing.
    """

    def test_read_ibm_schematics_action_failed(self):
        """Test the inner "read" path in this module with a server error response."""

        patcher = patch(
            'plugins.modules.ibm_schematics_action.SchematicsV1.get_action')
        mock = patcher.start()
        mock.side_effect = ApiException(500, message='Something went wrong...')

        set_module_args({
            'action_id': 'testString',
            'profile': 'summary',
        })

        with self.assertRaises(AnsibleFailJson) as result:
            os.environ['SCHEMATICS_AUTH_TYPE'] = 'noAuth'
            os.environ['IC_API_KEY'] = 'noAuthAPIKey'
            ibm_schematics_action.main()

        assert result.exception.args[0]['msg'] == 'Something went wrong...'

        mock_data = dict(
            action_id='testString',
            profile='summary',
        )

        mock.assert_called_once()
        processed_result = post_process_result(
            mock_data, mock.call_args.kwargs)
        assert mock_data == processed_result

        patcher.stop()

    def test_create_ibm_schematics_action_success(self):
        """Test the "create" path - successful."""
        user_state_model = {
            'state_': 'draft',
            'set_by': 'testString',
            'set_at': '2019-01-01T12:00:00.000Z',
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

        credential_variable_metadata_model = {
            'type': 'string',
            'aliases': ['testString'],
            'description': 'testString',
            'cloud_data_type': 'testString',
            'default_value': 'testString',
            'link_status': 'normal',
            'immutable': True,
            'hidden': True,
            'required': True,
            'position': 38,
            'group_by': 'testString',
            'source': 'testString',
        }

        credential_variable_data_model = {
            'name': 'testString',
            'value': 'testString',
            'use_default': True,
            'metadata': credential_variable_metadata_model,
        }

        bastion_resource_definition_model = {
            'name': 'testString',
            'host': 'testString',
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

        action_state_model = {
            'status_code': 'normal',
            'status_job_id': 'testString',
            'status_message': 'testString',
        }

        system_lock_model = {
            'sys_locked': True,
            'sys_locked_by': 'testString',
            'sys_locked_at': '2019-01-01T12:00:00.000Z',
        }

        resource = {
            'name': 'Stop Action',
            'description': 'The description of your action.',
            'location': 'us-south',
            'resource_group': 'testString',
            'bastion_connection_type': 'ssh',
            'inventory_connection_type': 'ssh',
            'tags': ['testString'],
            'user_state': user_state_model,
            'source_readme_url': 'testString',
            'source': external_source_model,
            'source_type': 'local',
            'command_parameter': 'testString',
            'inventory': 'testString',
            'credentials': [credential_variable_data_model],
            'bastion': bastion_resource_definition_model,
            'bastion_credential': credential_variable_data_model,
            'targets_ini': 'testString',
            'inputs': [variable_data_model],
            'outputs': [variable_data_model],
            'settings': [variable_data_model],
            'state_': action_state_model,
            'sys_lock': system_lock_model,
            'x_github_token': 'testString',
        }

        patcher = patch(
            'plugins.modules.ibm_schematics_action.SchematicsV1.create_action')
        mock = patcher.start()
        mock.return_value = DetailedResponseMock(resource)

        get_action_patcher = patch(
            'plugins.modules.ibm_schematics_action.SchematicsV1.get_action')
        get_action_mock = get_action_patcher.start()

        set_module_args({
            'name': 'Stop Action',
            'description': 'The description of your action.',
            'location': 'us-south',
            'resource_group': 'testString',
            'bastion_connection_type': 'ssh',
            'inventory_connection_type': 'ssh',
            'tags': ['testString'],
            'user_state': user_state_model,
            'source_readme_url': 'testString',
            'source': external_source_model,
            'source_type': 'local',
            'command_parameter': 'testString',
            'inventory': 'testString',
            'credentials': [credential_variable_data_model],
            'bastion': bastion_resource_definition_model,
            'bastion_credential': credential_variable_data_model,
            'targets_ini': 'testString',
            'inputs': [variable_data_model],
            'outputs': [variable_data_model],
            'settings': [variable_data_model],
            'state_': action_state_model,
            'sys_lock': system_lock_model,
            'x_github_token': 'testString',
        })

        with self.assertRaises(AnsibleExitJson) as result:
            os.environ['SCHEMATICS_AUTH_TYPE'] = 'noAuth'
            os.environ['IC_API_KEY'] = 'noAuthAPIKey'
            ibm_schematics_action.main()

        assert result.exception.args[0]['changed'] is True
        assert result.exception.args[0]['msg'] == resource

        mock_data = dict(
            name='Stop Action',
            description='The description of your action.',
            location='us-south',
            resource_group='testString',
            bastion_connection_type='ssh',
            inventory_connection_type='ssh',
            tags=['testString'],
            user_state=user_state_model,
            source_readme_url='testString',
            source=external_source_model,
            source_type='local',
            command_parameter='testString',
            inventory='testString',
            credentials=[credential_variable_data_model],
            bastion=bastion_resource_definition_model,
            bastion_credential=credential_variable_data_model,
            targets_ini='testString',
            inputs=[variable_data_model],
            outputs=[variable_data_model],
            settings=[variable_data_model],
            state=action_state_model,
            sys_lock=system_lock_model,
            x_github_token='testString',
        )

        mock.assert_called_once()
        processed_result = post_process_result(
            mock_data, mock.call_args.kwargs)
        assert mock_data == processed_result

        get_action_mock.assert_not_called()

        get_action_patcher.stop()
        patcher.stop()

    def test_create_ibm_schematics_action_failed(self):
        """Test the "create" path - failed."""

        get_action_patcher = patch(
            'plugins.modules.ibm_schematics_action.SchematicsV1.get_action')
        get_action_mock = get_action_patcher.start()

        patcher = patch(
            'plugins.modules.ibm_schematics_action.SchematicsV1.create_action')
        mock = patcher.start()
        mock.side_effect = ApiException(
            400, message='Create ibm_schematics_action error')

        user_state_model = {
            'state_': 'draft',
            'set_by': 'testString',
            'set_at': '2019-01-01T12:00:00.000Z',
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

        credential_variable_metadata_model = {
            'type': 'string',
            'aliases': ['testString'],
            'description': 'testString',
            'cloud_data_type': 'testString',
            'default_value': 'testString',
            'link_status': 'normal',
            'immutable': True,
            'hidden': True,
            'required': True,
            'position': 38,
            'group_by': 'testString',
            'source': 'testString',
        }

        credential_variable_data_model = {
            'name': 'testString',
            'value': 'testString',
            'use_default': True,
            'metadata': credential_variable_metadata_model,
        }

        bastion_resource_definition_model = {
            'name': 'testString',
            'host': 'testString',
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

        action_state_model = {
            'status_code': 'normal',
            'status_job_id': 'testString',
            'status_message': 'testString',
        }

        system_lock_model = {
            'sys_locked': True,
            'sys_locked_by': 'testString',
            'sys_locked_at': '2019-01-01T12:00:00.000Z',
        }

        set_module_args({
            'name': 'Stop Action',
            'description': 'The description of your action.',
            'location': 'us-south',
            'resource_group': 'testString',
            'bastion_connection_type': 'ssh',
            'inventory_connection_type': 'ssh',
            'tags': ['testString'],
            'user_state': user_state_model,
            'source_readme_url': 'testString',
            'source': external_source_model,
            'source_type': 'local',
            'command_parameter': 'testString',
            'inventory': 'testString',
            'credentials': [credential_variable_data_model],
            'bastion': bastion_resource_definition_model,
            'bastion_credential': credential_variable_data_model,
            'targets_ini': 'testString',
            'inputs': [variable_data_model],
            'outputs': [variable_data_model],
            'settings': [variable_data_model],
            'state_': action_state_model,
            'sys_lock': system_lock_model,
            'x_github_token': 'testString',
        })

        with self.assertRaises(AnsibleFailJson) as result:
            os.environ['SCHEMATICS_AUTH_TYPE'] = 'noAuth'
            os.environ['IC_API_KEY'] = 'noAuthAPIKey'
            ibm_schematics_action.main()

        assert result.exception.args[0]['msg'] == 'Create ibm_schematics_action error'

        mock_data = dict(
            name='Stop Action',
            description='The description of your action.',
            location='us-south',
            resource_group='testString',
            bastion_connection_type='ssh',
            inventory_connection_type='ssh',
            tags=['testString'],
            user_state=user_state_model,
            source_readme_url='testString',
            source=external_source_model,
            source_type='local',
            command_parameter='testString',
            inventory='testString',
            credentials=[credential_variable_data_model],
            bastion=bastion_resource_definition_model,
            bastion_credential=credential_variable_data_model,
            targets_ini='testString',
            inputs=[variable_data_model],
            outputs=[variable_data_model],
            settings=[variable_data_model],
            state=action_state_model,
            sys_lock=system_lock_model,
            x_github_token='testString',
        )

        mock.assert_called_once()
        processed_result = post_process_result(
            mock_data, mock.call_args.kwargs)
        assert mock_data == processed_result

        get_action_mock.assert_not_called()

        get_action_patcher.stop()
        patcher.stop()

    def test_update_ibm_schematics_action_success(self):
        """Test the "update" path - successful."""
        user_state_model = {
            'state_': 'draft',
            'set_by': 'testString',
            'set_at': '2019-01-01T12:00:00.000Z',
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

        credential_variable_metadata_model = {
            'type': 'string',
            'aliases': ['testString'],
            'description': 'testString',
            'cloud_data_type': 'testString',
            'default_value': 'testString',
            'link_status': 'normal',
            'immutable': True,
            'hidden': True,
            'required': True,
            'position': 38,
            'group_by': 'testString',
            'source': 'testString',
        }

        credential_variable_data_model = {
            'name': 'testString',
            'value': 'testString',
            'use_default': True,
            'metadata': credential_variable_metadata_model,
        }

        bastion_resource_definition_model = {
            'name': 'testString',
            'host': 'testString',
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

        action_state_model = {
            'status_code': 'normal',
            'status_job_id': 'testString',
            'status_message': 'testString',
        }

        system_lock_model = {
            'sys_locked': True,
            'sys_locked_by': 'testString',
            'sys_locked_at': '2019-01-01T12:00:00.000Z',
        }

        resource = {
            'action_id': 'testString',
            'name': 'Stop Action',
            'description': 'The description of your action.',
            'location': 'us-south',
            'resource_group': 'testString',
            'bastion_connection_type': 'ssh',
            'inventory_connection_type': 'ssh',
            'tags': ['testString'],
            'user_state': user_state_model,
            'source_readme_url': 'testString',
            'source': external_source_model,
            'source_type': 'local',
            'command_parameter': 'testString',
            'inventory': 'testString',
            'credentials': [credential_variable_data_model],
            'bastion': bastion_resource_definition_model,
            'bastion_credential': credential_variable_data_model,
            'targets_ini': 'testString',
            'inputs': [variable_data_model],
            'outputs': [variable_data_model],
            'settings': [variable_data_model],
            'state_': action_state_model,
            'sys_lock': system_lock_model,
            'x_github_token': 'testString',
        }

        patcher = patch(
            'plugins.modules.ibm_schematics_action.SchematicsV1.update_action')
        mock = patcher.start()
        mock.return_value = DetailedResponseMock(resource)

        get_action_patcher = patch(
            'plugins.modules.ibm_schematics_action.SchematicsV1.get_action')
        get_action_mock = get_action_patcher.start()
        get_action_mock.return_value = DetailedResponseMock(resource)

        set_module_args({
            'action_id': 'testString',
            'name': 'Stop Action',
            'description': 'The description of your action.',
            'location': 'us-south',
            'resource_group': 'testString',
            'bastion_connection_type': 'ssh',
            'inventory_connection_type': 'ssh',
            'tags': ['testString'],
            'user_state': user_state_model,
            'source_readme_url': 'testString',
            'source': external_source_model,
            'source_type': 'local',
            'command_parameter': 'testString',
            'inventory': 'testString',
            'credentials': [credential_variable_data_model],
            'bastion': bastion_resource_definition_model,
            'bastion_credential': credential_variable_data_model,
            'targets_ini': 'testString',
            'inputs': [variable_data_model],
            'outputs': [variable_data_model],
            'settings': [variable_data_model],
            'state_': action_state_model,
            'sys_lock': system_lock_model,
            'x_github_token': 'testString',
        })

        with self.assertRaises(AnsibleExitJson) as result:
            os.environ['SCHEMATICS_AUTH_TYPE'] = 'noAuth'
            os.environ['IC_API_KEY'] = 'noAuthAPIKey'
            ibm_schematics_action.main()

        assert result.exception.args[0]['changed'] is True
        assert result.exception.args[0]['msg'] == resource

        mock_data = dict(
            action_id='testString',
            name='Stop Action',
            description='The description of your action.',
            location='us-south',
            resource_group='testString',
            bastion_connection_type='ssh',
            inventory_connection_type='ssh',
            tags=['testString'],
            user_state=user_state_model,
            source_readme_url='testString',
            source=external_source_model,
            source_type='local',
            command_parameter='testString',
            inventory='testString',
            credentials=[credential_variable_data_model],
            bastion=bastion_resource_definition_model,
            bastion_credential=credential_variable_data_model,
            targets_ini='testString',
            inputs=[variable_data_model],
            outputs=[variable_data_model],
            settings=[variable_data_model],
            state=action_state_model,
            sys_lock=system_lock_model,
            x_github_token='testString',
        )

        mock.assert_called_once()
        processed_result = post_process_result(
            mock_data, mock.call_args.kwargs)
        assert mock_data == processed_result

        get_action_mock_data = dict(
            action_id='testString',
            profile='summary',
        )
        # Set the variables that belong to the "read" path to `None`
        # since we test the "delete" path here.
        for param in get_action_mock_data:
            get_action_mock_data[param] = mock_data.get(param, None)

        get_action_mock.assert_called_once()
        get_action_processed_result = post_process_result(
            get_action_mock_data, get_action_mock.call_args.kwargs)
        assert get_action_mock_data == get_action_processed_result
        get_action_patcher.stop()
        patcher.stop()

    def test_update_ibm_schematics_action_failed(self):
        """Test the "update" path - failed."""
        user_state_model = {
            'state_': 'draft',
            'set_by': 'testString',
            'set_at': '2019-01-01T12:00:00.000Z',
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

        credential_variable_metadata_model = {
            'type': 'string',
            'aliases': ['testString'],
            'description': 'testString',
            'cloud_data_type': 'testString',
            'default_value': 'testString',
            'link_status': 'normal',
            'immutable': True,
            'hidden': True,
            'required': True,
            'position': 38,
            'group_by': 'testString',
            'source': 'testString',
        }

        credential_variable_data_model = {
            'name': 'testString',
            'value': 'testString',
            'use_default': True,
            'metadata': credential_variable_metadata_model,
        }

        bastion_resource_definition_model = {
            'name': 'testString',
            'host': 'testString',
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

        action_state_model = {
            'status_code': 'normal',
            'status_job_id': 'testString',
            'status_message': 'testString',
        }

        system_lock_model = {
            'sys_locked': True,
            'sys_locked_by': 'testString',
            'sys_locked_at': '2019-01-01T12:00:00.000Z',
        }

        resource = {
            'action_id': 'testString',
            'name': 'Stop Action',
            'description': 'The description of your action.',
            'location': 'us-south',
            'resource_group': 'testString',
            'bastion_connection_type': 'ssh',
            'inventory_connection_type': 'ssh',
            'tags': ['testString'],
            'user_state': user_state_model,
            'source_readme_url': 'testString',
            'source': external_source_model,
            'source_type': 'local',
            'command_parameter': 'testString',
            'inventory': 'testString',
            'credentials': [credential_variable_data_model],
            'bastion': bastion_resource_definition_model,
            'bastion_credential': credential_variable_data_model,
            'targets_ini': 'testString',
            'inputs': [variable_data_model],
            'outputs': [variable_data_model],
            'settings': [variable_data_model],
            'state_': action_state_model,
            'sys_lock': system_lock_model,
            'x_github_token': 'testString',
        }

        patcher = patch(
            'plugins.modules.ibm_schematics_action.SchematicsV1.update_action')
        mock = patcher.start()
        mock.side_effect = ApiException(
            400, message='Update ibm_schematics_action error')

        get_action_patcher = patch(
            'plugins.modules.ibm_schematics_action.SchematicsV1.get_action')
        get_action_mock = get_action_patcher.start()
        get_action_mock.return_value = DetailedResponseMock(resource)

        set_module_args({
            'action_id': 'testString',
            'name': 'Stop Action',
            'description': 'The description of your action.',
            'location': 'us-south',
            'resource_group': 'testString',
            'bastion_connection_type': 'ssh',
            'inventory_connection_type': 'ssh',
            'tags': ['testString'],
            'user_state': user_state_model,
            'source_readme_url': 'testString',
            'source': external_source_model,
            'source_type': 'local',
            'command_parameter': 'testString',
            'inventory': 'testString',
            'credentials': [credential_variable_data_model],
            'bastion': bastion_resource_definition_model,
            'bastion_credential': credential_variable_data_model,
            'targets_ini': 'testString',
            'inputs': [variable_data_model],
            'outputs': [variable_data_model],
            'settings': [variable_data_model],
            'state_': action_state_model,
            'sys_lock': system_lock_model,
            'x_github_token': 'testString',
        })

        with self.assertRaises(AnsibleFailJson) as result:
            os.environ['SCHEMATICS_AUTH_TYPE'] = 'noAuth'
            os.environ['IC_API_KEY'] = 'noAuthAPIKey'
            ibm_schematics_action.main()

        assert result.exception.args[0]['msg'] == 'Update ibm_schematics_action error'

        mock_data = dict(
            action_id='testString',
            name='Stop Action',
            description='The description of your action.',
            location='us-south',
            resource_group='testString',
            bastion_connection_type='ssh',
            inventory_connection_type='ssh',
            tags=['testString'],
            user_state=user_state_model,
            source_readme_url='testString',
            source=external_source_model,
            source_type='local',
            command_parameter='testString',
            inventory='testString',
            credentials=[credential_variable_data_model],
            bastion=bastion_resource_definition_model,
            bastion_credential=credential_variable_data_model,
            targets_ini='testString',
            inputs=[variable_data_model],
            outputs=[variable_data_model],
            settings=[variable_data_model],
            state=action_state_model,
            sys_lock=system_lock_model,
            x_github_token='testString',
        )

        mock.assert_called_once()
        processed_result = post_process_result(
            mock_data, mock.call_args.kwargs)
        assert mock_data == processed_result

        get_action_mock_data = dict(
            action_id='testString',
            profile='summary',
        )
        # Set the variables that belong to the "read" path to `None`
        # since we test the "delete" path here.
        for param in get_action_mock_data:
            get_action_mock_data[param] = mock_data.get(param, None)

        get_action_mock.assert_called_once()
        get_action_processed_result = post_process_result(
            get_action_mock_data, get_action_mock.call_args.kwargs)
        assert get_action_mock_data == get_action_processed_result

        get_action_patcher.stop()
        patcher.stop()

    def test_delete_ibm_schematics_action_success(self):
        """Test the "delete" path - successfull."""
        patcher = patch(
            'plugins.modules.ibm_schematics_action.SchematicsV1.delete_action')
        mock = patcher.start()
        mock.return_value = DetailedResponseMock()

        get_action_patcher = patch(
            'plugins.modules.ibm_schematics_action.SchematicsV1.get_action')
        get_action_mock = get_action_patcher.start()
        get_action_mock.return_value = DetailedResponseMock()

        args = {
            'action_id': 'testString',
            'force': True,
            'propagate': True,
            'state': 'absent',
        }

        set_module_args(args)

        with self.assertRaises(AnsibleExitJson) as result:
            os.environ['SCHEMATICS_AUTH_TYPE'] = 'noAuth'
            os.environ['IC_API_KEY'] = 'noAuthAPIKey'
            ibm_schematics_action.main()

        assert result.exception.args[0]['changed'] is True
        assert result.exception.args[0]['msg']['id'] == 'testString'
        assert result.exception.args[0]['msg']['status'] == 'deleted'

        mock_data = dict(
            action_id='testString',
            force=True,
            propagate=True,
        )

        mock.assert_called_once()
        processed_result = post_process_result(
            mock_data, mock.call_args.kwargs)
        assert mock_data == processed_result

        get_action_mock_data = dict(
            action_id='testString',
            profile='summary',
        )
        # Set the variables that belong to the "read" path to `None`
        # since we test the "delete" path here.
        for param in get_action_mock_data:
            get_action_mock_data[param] = mock_data.get(param, None)

        get_action_mock.assert_called_once()
        get_action_processed_result = post_process_result(
            get_action_mock_data, get_action_mock.call_args.kwargs)
        assert get_action_mock_data == get_action_processed_result

        get_action_patcher.stop()
        patcher.stop()

    def test_delete_ibm_schematics_action_not_exists(self):
        """Test the "delete" path - not exists."""
        patcher = patch(
            'plugins.modules.ibm_schematics_action.SchematicsV1.delete_action')
        mock = patcher.start()
        mock.return_value = DetailedResponseMock()

        get_action_patcher = patch(
            'plugins.modules.ibm_schematics_action.SchematicsV1.get_action')
        get_action_mock = get_action_patcher.start()
        get_action_mock.side_effect = ApiException(404)

        args = {
            'action_id': 'testString',
            'force': True,
            'propagate': True,
            'state': 'absent',
        }

        set_module_args(args)

        with self.assertRaises(AnsibleExitJson) as result:
            os.environ['SCHEMATICS_AUTH_TYPE'] = 'noAuth'
            os.environ['IC_API_KEY'] = 'noAuthAPIKey'
            ibm_schematics_action.main()

        assert result.exception.args[0]['changed'] is False
        assert result.exception.args[0]['msg']['id'] == 'testString'
        assert result.exception.args[0]['msg']['status'] == 'not_found'

        mock_data = dict(
            action_id='testString',
            force=True,
            propagate=True,
        )

        mock.assert_not_called()

        get_action_mock_data = dict(
            action_id='testString',
            profile='summary',
        )
        # Set the variables that belong to the "read" path to `None`
        # since we test the "delete" path here.
        for param in get_action_mock_data:
            get_action_mock_data[param] = mock_data.get(param, None)

        get_action_mock.assert_called_once()
        get_action_processed_result = post_process_result(
            get_action_mock_data, get_action_mock.call_args.kwargs)
        assert get_action_mock_data == get_action_processed_result

        get_action_patcher.stop()
        patcher.stop()

    def test_delete_ibm_schematics_action_failed(self):
        """Test the "delete" path - failed."""
        patcher = patch(
            'plugins.modules.ibm_schematics_action.SchematicsV1.delete_action')
        mock = patcher.start()
        mock.side_effect = ApiException(
            400, message='Delete ibm_schematics_action error')

        get_action_patcher = patch(
            'plugins.modules.ibm_schematics_action.SchematicsV1.get_action')
        get_action_mock = get_action_patcher.start()
        get_action_mock.return_value = DetailedResponseMock()

        set_module_args({
            'action_id': 'testString',
            'force': True,
            'propagate': True,
            'state': 'absent',
        })

        with self.assertRaises(AnsibleFailJson) as result:
            os.environ['SCHEMATICS_AUTH_TYPE'] = 'noAuth'
            os.environ['IC_API_KEY'] = 'noAuthAPIKey'
            ibm_schematics_action.main()

        assert result.exception.args[0]['msg'] == 'Delete ibm_schematics_action error'

        mock_data = dict(
            action_id='testString',
            force=True,
            propagate=True,
        )

        mock.assert_called_once()
        processed_result = post_process_result(
            mock_data, mock.call_args.kwargs)
        assert mock_data == processed_result

        get_action_mock_data = dict(
            action_id='testString',
            profile='summary',
        )
        # Set the variables that belong to the "read" path to `None`
        # since we test the "delete" path here.
        for param in get_action_mock_data:
            get_action_mock_data[param] = mock_data.get(param, None)

        get_action_mock.assert_called_once()
        get_action_processed_result = post_process_result(
            get_action_mock_data, get_action_mock.call_args.kwargs)
        assert get_action_mock_data == get_action_processed_result

        get_action_patcher.stop()
        patcher.stop()
