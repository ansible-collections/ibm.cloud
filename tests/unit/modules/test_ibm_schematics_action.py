# (C) Copyright IBM Corp. 2024.
#
# GNU General Public License v3.0+ (see LICENSE or https://www.gnu.org/licenses/gpl-3.0.txt)

from __future__ import (absolute_import, division, print_function)
__metaclass__ = type

import os

from ansible_collections.community.internal_test_tools.tests.unit.compat.mock import patch
from ansible_collections.community.internal_test_tools.tests.unit.plugins.modules.utils import ModuleTestCase, AnsibleFailJson, AnsibleExitJson, set_module_args
from plugins.modules import ibm_schematics_action

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
        self.assertIsNone(ibm_schematics_action.MISSING_IMPORT_EXC)

        # Set-up mocks for each operation.
        self.read_patcher = patch('plugins.modules.ibm_schematics_action.SchematicsV1.get_action')
        self.read_mock = self.read_patcher.start()
        self.create_patcher = patch('plugins.modules.ibm_schematics_action.SchematicsV1.create_action')
        self.create_mock = self.create_patcher.start()
        self.update_patcher = patch('plugins.modules.ibm_schematics_action.SchematicsV1.update_action')
        self.update_mock = self.update_patcher.start()
        self.delete_patcher = patch('plugins.modules.ibm_schematics_action.SchematicsV1.delete_action')
        self.delete_mock = self.delete_patcher.start()

        # Run the actual function.
        func(self)

        # Stop the patchers.
        self.read_patcher.stop()
        self.create_patcher.stop()
        self.update_patcher.stop()
        self.delete_patcher.stop()

    return wrapper


class TestActionModule(ModuleTestCase):
    """
    Test class for Action module testing.
    """

    @mock_operations
    def test_read_ibm_schematics_action_failed(self):
        """Test the inner "read" path in this module with a server error response."""
        self.read_mock.side_effect = ApiException(500, message='Something went wrong...')

        set_module_args({
            'action_id': 'testString',
            'profile': 'summary',
        })

        with self.assertRaises(AnsibleFailJson) as result:
            os.environ['SCHEMATICS_AUTH_TYPE'] = 'noAuth'
            ibm_schematics_action.main()

        self.assertEqual(result.exception.args[0]['msg'], 'Something went wrong...')

        mock_data = dict(
            action_id='testString',
            profile='summary',
        )

        self.read_mock.assert_called_once()
        self.assertTrue(checkResult(mock_data, self.read_mock.call_args.kwargs))

    @mock_operations
    def test_create_ibm_schematics_action_success(self):
        """Test the "create" path - successful."""
        user_state_model = {
            'state': 'draft',
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

        resource = {
            'name': 'Stop Action',
            'description': (
                'The description of your action. The description can be up to 2048 characte'
                'rs long in size. **Example** you can use the description to stop the targe'
                'ts.'),
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
            'x_github_token': 'testString',
        }

        self.read_mock.side_effect = ApiException(404)
        self.create_mock.return_value = DetailedResponseMock(resource)

        set_module_args({
            'name': 'Stop Action',
            'description': (
                'The description of your action. The description can be up to 2048 characters long in s'
                'ize. **Example** you can use the description to stop the targets.'),
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
            'x_github_token': 'testString',
        })

        with self.assertRaises(AnsibleExitJson) as result:
            os.environ['SCHEMATICS_AUTH_TYPE'] = 'noAuth'
            ibm_schematics_action.main()

        self.assertTrue(result.exception.args[0]['changed'])
        for field, value in resource.items():
            self.assertEqual(value, result.exception.args[0].get(field))

        mock_data = dict(
            name='Stop Action',
            description=(
                'The description of your action. The description can be up to 2048 characters long in s'
                'ize. **Example** you can use the description to stop the targets.'),
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
            x_github_token='testString',
        )

        self.create_mock.assert_called_once()
        self.assertTrue(checkResult(mock_data, self.create_mock.call_args.kwargs))

    @mock_operations
    def test_create_ibm_schematics_action_failed(self):
        """Test the "create" path - failed."""
        self.read_mock.side_effect = ApiException(404)
        self.create_mock.side_effect = ApiException(400, message='Create ibm_schematics_action error')

        user_state_model = {
            'state': 'draft',
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

        set_module_args({
            'name': 'Stop Action',
            'description': (
                'The description of your action. The description can be up to 2048 characters long in s'
                'ize. **Example** you can use the description to stop the targets.'),
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
            'x_github_token': 'testString',
        })

        with self.assertRaises(AnsibleFailJson) as result:
            os.environ['SCHEMATICS_AUTH_TYPE'] = 'noAuth'
            ibm_schematics_action.main()

        self.assertEqual(result.exception.args[0]['msg'], 'Create ibm_schematics_action error')

        mock_data = dict(
            name='Stop Action',
            description=(
                'The description of your action. The description can be up to 2048 characters long in s'
                'ize. **Example** you can use the description to stop the targets.'),
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
            x_github_token='testString',
        )

        self.create_mock.assert_called_once()
        self.assertTrue(checkResult(mock_data, self.create_mock.call_args.kwargs))

    @mock_operations
    def test_update_ibm_schematics_action_success(self):
        """Test the "update" path - successful."""
        user_state_model = {
            'state': 'draft',
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

        resource = {
            'action_id': 'testString',
            'name': 'Stop Action',
            'description': (
                'The description of your action. The description can be up to 2048 characte'
                'rs long in size. **Example** you can use the description to stop the targe'
                'ts.'),
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
            'x_github_token': 'testString',
        }

        self.read_mock.return_value = DetailedResponseMock(resource)
        self.update_mock.return_value = DetailedResponseMock(resource)

        set_module_args({
            'action_id': 'testString',
            'name': 'Stop Action',
            'description': (
                'The description of your action. The description can be up to 2048 characters long in s'
                'ize. **Example** you can use the description to stop the targets.'),
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
            'x_github_token': 'testString',
        })

        with self.assertRaises(AnsibleExitJson) as result:
            os.environ['SCHEMATICS_AUTH_TYPE'] = 'noAuth'
            ibm_schematics_action.main()

        self.assertTrue(result.exception.args[0]['changed'])
        for field, value in resource.items():
            self.assertEqual(value, result.exception.args[0].get(field))

        mock_data = dict(
            action_id='testString',
            name='Stop Action',
            description=(
                'The description of your action. The description can be up to 2048 characters long in s'
                'ize. **Example** you can use the description to stop the targets.'),
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
            x_github_token='testString',
        )

        self.update_mock.assert_called_once()
        self.assertTrue(checkResult(mock_data, self.update_mock.call_args.kwargs))

        read_mock_data = dict(
            action_id='testString',
            profile='summary',
        )
        # Set the variables that belong to the "read" path to `None`
        # because we test the "update" path here.
        for param in read_mock_data:
            read_mock_data[param] = mock_data.get(param, None)

        self.read_mock.assert_called_once()
        self.assertTrue(checkResult(read_mock_data, self.read_mock.call_args.kwargs))

    @mock_operations
    def test_update_ibm_schematics_action_failed(self):
        """Test the "update" path - failed."""
        user_state_model = {
            'state': 'draft',
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

        resource = {
            'action_id': 'testString',
            'name': 'Stop Action',
            'description': (
                'The description of your action. The description can be up to 2048 characte'
                'rs long in size. **Example** you can use the description to stop the targe'
                'ts.'),
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
            'x_github_token': 'testString',
        }

        self.read_mock.return_value = DetailedResponseMock(resource)
        self.update_mock.side_effect = ApiException(400, message='Update ibm_schematics_action error')

        set_module_args({
            'action_id': 'testString',
            'name': 'Stop Action',
            'description': (
                'The description of your action. The description can be up to 2048 characters long in s'
                'ize. **Example** you can use the description to stop the targets.'),
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
            'x_github_token': 'testString',
        })

        with self.assertRaises(AnsibleFailJson) as result:
            os.environ['SCHEMATICS_AUTH_TYPE'] = 'noAuth'
            ibm_schematics_action.main()

        self.assertEqual(result.exception.args[0]['msg'], 'Update ibm_schematics_action error')

        mock_data = dict(
            action_id='testString',
            name='Stop Action',
            description=(
                'The description of your action. The description can be up to 2048 characters long in s'
                'ize. **Example** you can use the description to stop the targets.'),
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
            x_github_token='testString',
        )

        self.update_mock.assert_called_once()
        self.assertTrue(checkResult(mock_data, self.update_mock.call_args.kwargs))

        read_mock_data = dict(
            action_id='testString',
            profile='summary',
        )
        # Set the variables that belong to the "read" path to `None`
        # because we test the "update" path here.
        for param in read_mock_data:
            read_mock_data[param] = mock_data.get(param, None)

        self.read_mock.assert_called_once()
        self.assertTrue(checkResult(read_mock_data, self.read_mock.call_args.kwargs))

    @mock_operations
    def test_delete_ibm_schematics_action_success(self):
        """Test the "delete" path - successfull."""
        self.read_mock.return_value = DetailedResponseMock()
        self.delete_mock.return_value = DetailedResponseMock()

        args = {
            'action_id': 'testString',
            'force': True,
            'propagate': True,
            'state': 'absent',
        }

        set_module_args(args)

        with self.assertRaises(AnsibleExitJson) as result:
            os.environ['SCHEMATICS_AUTH_TYPE'] = 'noAuth'
            ibm_schematics_action.main()

        self.assertTrue(result.exception.args[0]['changed'])
        self.assertEqual(result.exception.args[0]['id'], 'testString')
        self.assertEqual(result.exception.args[0]['status'], 'deleted')

        mock_data = dict(
            action_id='testString',
            force=True,
            propagate=True,
        )

        self.delete_mock.assert_called_once()
        self.assertTrue(checkResult(mock_data, self.delete_mock.call_args.kwargs))

        read_mock_data = dict(
            action_id='testString',
            profile='summary',
        )
        # Set the variables that belong to the "read" path to `None`
        # because we test the "delete" path here.
        for param in read_mock_data:
            read_mock_data[param] = mock_data.get(param, None)

        self.read_mock.assert_called_once()
        self.assertTrue(checkResult(read_mock_data, self.read_mock.call_args.kwargs))

    @mock_operations
    def test_delete_ibm_schematics_action_not_exists(self):
        """Test the "delete" path - not exists."""
        self.read_mock.side_effect = ApiException(404)
        self.delete_mock.return_value = DetailedResponseMock()

        args = {
            'action_id': 'testString',
            'force': True,
            'propagate': True,
            'state': 'absent',
        }

        set_module_args(args)

        with self.assertRaises(AnsibleExitJson) as result:
            os.environ['SCHEMATICS_AUTH_TYPE'] = 'noAuth'
            ibm_schematics_action.main()

        self.assertFalse(result.exception.args[0]['changed'])
        self.assertEqual(result.exception.args[0]['id'], 'testString')
        self.assertEqual(result.exception.args[0]['status'], 'not_found')

        mock_data = dict(
            action_id='testString',
            force=True,
            propagate=True,
        )

        self.delete_mock.assert_not_called()

        read_mock_data = dict(
            action_id='testString',
            profile='summary',
        )
        # Set the variables that belong to the "read" path to `None`
        # because we test the "delete" path here.
        for param in read_mock_data:
            read_mock_data[param] = mock_data.get(param, None)

        self.read_mock.assert_called_once()
        self.assertTrue(checkResult(read_mock_data, self.read_mock.call_args.kwargs))

    @mock_operations
    def test_delete_ibm_schematics_action_failed(self):
        """Test the "delete" path - failed."""
        self.read_mock.return_value = DetailedResponseMock()
        self.delete_mock.side_effect = ApiException(400, message='Delete ibm_schematics_action error')

        set_module_args({
            'action_id': 'testString',
            'force': True,
            'propagate': True,
            'state': 'absent',
        })

        with self.assertRaises(AnsibleFailJson) as result:
            os.environ['SCHEMATICS_AUTH_TYPE'] = 'noAuth'
            ibm_schematics_action.main()

        self.assertEqual(result.exception.args[0]['msg'], 'Delete ibm_schematics_action error')

        mock_data = dict(
            action_id='testString',
            force=True,
            propagate=True,
        )

        self.delete_mock.assert_called_once()
        self.assertTrue(checkResult(mock_data, self.delete_mock.call_args.kwargs))

        read_mock_data = dict(
            action_id='testString',
            profile='summary',
        )
        # Set the variables that belong to the "read" path to `None`
        # because we test the "delete" path here.
        for param in read_mock_data:
            read_mock_data[param] = mock_data.get(param, None)

        self.read_mock.assert_called_once()
        self.assertTrue(checkResult(read_mock_data, self.read_mock.call_args.kwargs))
