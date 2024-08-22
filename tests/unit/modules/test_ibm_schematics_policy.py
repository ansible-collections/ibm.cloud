# (C) Copyright IBM Corp. 2024.
#
# GNU General Public License v3.0+ (see LICENSE or https://www.gnu.org/licenses/gpl-3.0.txt)

from __future__ import (absolute_import, division, print_function)
__metaclass__ = type

import os

from ansible_collections.community.internal_test_tools.tests.unit.compat.mock import patch
from ansible_collections.community.internal_test_tools.tests.unit.plugins.modules.utils import ModuleTestCase, AnsibleFailJson, AnsibleExitJson, set_module_args
from plugins.modules import ibm_schematics_policy

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
        self.assertIsNone(ibm_schematics_policy.MISSING_IMPORT_EXC)

        # Set-up mocks for each operation.
        self.read_patcher = patch('plugins.modules.ibm_schematics_policy.SchematicsV1.get_policy')
        self.read_mock = self.read_patcher.start()
        self.create_patcher = patch('plugins.modules.ibm_schematics_policy.SchematicsV1.create_policy')
        self.create_mock = self.create_patcher.start()
        self.update_patcher = patch('plugins.modules.ibm_schematics_policy.SchematicsV1.update_policy')
        self.update_mock = self.update_patcher.start()
        self.delete_patcher = patch('plugins.modules.ibm_schematics_policy.SchematicsV1.delete_policy')
        self.delete_mock = self.delete_patcher.start()

        # Run the actual function.
        func(self)

        # Stop the patchers.
        self.read_patcher.stop()
        self.create_patcher.stop()
        self.update_patcher.stop()
        self.delete_patcher.stop()

    return wrapper


class TestPolicyModule(ModuleTestCase):
    """
    Test class for Policy module testing.
    """

    @mock_operations
    def test_read_ibm_schematics_policy_failed(self):
        """Test the inner "read" path in this module with a server error response."""
        self.read_mock.side_effect = ApiException(500, message='Something went wrong...')

        set_module_args({
            'policy_id': 'testString',
            'profile': 'summary',
        })

        with self.assertRaises(AnsibleFailJson) as result:
            os.environ['SCHEMATICS_AUTH_TYPE'] = 'noAuth'
            ibm_schematics_policy.main()

        self.assertEqual(result.exception.args[0]['msg'], 'Something went wrong...')

        mock_data = dict(
            policy_id='testString',
            profile='summary',
        )

        self.read_mock.assert_called_once()
        self.assertTrue(checkResult(mock_data, self.read_mock.call_args.kwargs))

    @mock_operations
    def test_create_ibm_schematics_policy_success(self):
        """Test the "create" path - successful."""
        user_state_model = {
            'state': 'draft',
            'set_by': 'testString',
            'set_at': '2019-01-01T12:00:00.000Z',
        }

        policy_object_selector_model = {
            'kind': 'workspace',
            'tags': ['testString'],
            'resource_groups': ['testString'],
            'locations': ['us-south'],
        }

        policy_objects_model = {
            'selector_kind': 'ids',
            'selector_ids': ['testString'],
            'selector_scope': [policy_object_selector_model],
        }

        agent_assignment_policy_parameter_model = {
            'selector_kind': 'ids',
            'selector_ids': ['testString'],
            'selector_scope': [policy_object_selector_model],
        }

        policy_parameter_model = {
            'agent_assignment_policy_parameter': agent_assignment_policy_parameter_model,
        }

        scoped_resource_model = {
            'kind': 'workspace',
            'id': 'testString',
        }

        resource = {
            'name': 'Agent1-DevWS',
            'description': 'Policy for job execution of secured workspaces on agent1',
            'resource_group': 'Default',
            'tags': ['policy:secured-job'],
            'location': 'us-south',
            'state': user_state_model,
            'kind': 'agent_assignment_policy',
            'target': policy_objects_model,
            'parameter': policy_parameter_model,
            'scoped_resources': [scoped_resource_model],
        }

        self.read_mock.side_effect = ApiException(404)
        self.create_mock.return_value = DetailedResponseMock(resource)

        set_module_args({
            'name': 'Agent1-DevWS',
            'description': 'Policy for job execution of secured workspaces on agent1',
            'resource_group': 'Default',
            'tags': ['policy:secured-job'],
            'location': 'us-south',
            'schematics_policy_state': user_state_model,
            'kind': 'agent_assignment_policy',
            'target': policy_objects_model,
            'parameter': policy_parameter_model,
            'scoped_resources': [scoped_resource_model],
        })

        with self.assertRaises(AnsibleExitJson) as result:
            os.environ['SCHEMATICS_AUTH_TYPE'] = 'noAuth'
            ibm_schematics_policy.main()

        self.assertTrue(result.exception.args[0]['changed'])
        for field, value in resource.items():
            self.assertEqual(value, result.exception.args[0].get(field))

        mock_data = dict(
            name='Agent1-DevWS',
            description='Policy for job execution of secured workspaces on agent1',
            resource_group='Default',
            tags=['policy:secured-job'],
            location='us-south',
            state=user_state_model,
            kind='agent_assignment_policy',
            target=policy_objects_model,
            parameter=policy_parameter_model,
            scoped_resources=[scoped_resource_model],
        )

        self.create_mock.assert_called_once()
        self.assertTrue(checkResult(mock_data, self.create_mock.call_args.kwargs))

    @mock_operations
    def test_create_ibm_schematics_policy_failed(self):
        """Test the "create" path - failed."""
        self.read_mock.side_effect = ApiException(404)
        self.create_mock.side_effect = ApiException(400, message='Create ibm_schematics_policy error')

        user_state_model = {
            'state': 'draft',
            'set_by': 'testString',
            'set_at': '2019-01-01T12:00:00.000Z',
        }

        policy_object_selector_model = {
            'kind': 'workspace',
            'tags': ['testString'],
            'resource_groups': ['testString'],
            'locations': ['us-south'],
        }

        policy_objects_model = {
            'selector_kind': 'ids',
            'selector_ids': ['testString'],
            'selector_scope': [policy_object_selector_model],
        }

        agent_assignment_policy_parameter_model = {
            'selector_kind': 'ids',
            'selector_ids': ['testString'],
            'selector_scope': [policy_object_selector_model],
        }

        policy_parameter_model = {
            'agent_assignment_policy_parameter': agent_assignment_policy_parameter_model,
        }

        scoped_resource_model = {
            'kind': 'workspace',
            'id': 'testString',
        }

        set_module_args({
            'name': 'Agent1-DevWS',
            'description': 'Policy for job execution of secured workspaces on agent1',
            'resource_group': 'Default',
            'tags': ['policy:secured-job'],
            'location': 'us-south',
            'schematics_policy_state': user_state_model,
            'kind': 'agent_assignment_policy',
            'target': policy_objects_model,
            'parameter': policy_parameter_model,
            'scoped_resources': [scoped_resource_model],
        })

        with self.assertRaises(AnsibleFailJson) as result:
            os.environ['SCHEMATICS_AUTH_TYPE'] = 'noAuth'
            ibm_schematics_policy.main()

        self.assertEqual(result.exception.args[0]['msg'], 'Create ibm_schematics_policy error')

        mock_data = dict(
            name='Agent1-DevWS',
            description='Policy for job execution of secured workspaces on agent1',
            resource_group='Default',
            tags=['policy:secured-job'],
            location='us-south',
            state=user_state_model,
            kind='agent_assignment_policy',
            target=policy_objects_model,
            parameter=policy_parameter_model,
            scoped_resources=[scoped_resource_model],
        )

        self.create_mock.assert_called_once()
        self.assertTrue(checkResult(mock_data, self.create_mock.call_args.kwargs))

    @mock_operations
    def test_update_ibm_schematics_policy_success(self):
        """Test the "update" path - successful."""
        user_state_model = {
            'state': 'draft',
            'set_by': 'testString',
            'set_at': '2019-01-01T12:00:00.000Z',
        }

        policy_object_selector_model = {
            'kind': 'workspace',
            'tags': ['testString'],
            'resource_groups': ['testString'],
            'locations': ['us-south'],
        }

        policy_objects_model = {
            'selector_kind': 'ids',
            'selector_ids': ['testString'],
            'selector_scope': [policy_object_selector_model],
        }

        agent_assignment_policy_parameter_model = {
            'selector_kind': 'ids',
            'selector_ids': ['testString'],
            'selector_scope': [policy_object_selector_model],
        }

        policy_parameter_model = {
            'agent_assignment_policy_parameter': agent_assignment_policy_parameter_model,
        }

        scoped_resource_model = {
            'kind': 'workspace',
            'id': 'testString',
        }

        resource = {
            'policy_id': 'testString',
            'name': 'Agent1-DevWS',
            'description': 'Policy for job execution of secured workspaces on agent1',
            'resource_group': 'Default',
            'tags': ['policy:secured-job'],
            'location': 'us-south',
            'schematics_policy_state': user_state_model,
            'kind': 'agent_assignment_policy',
            'target': policy_objects_model,
            'parameter': policy_parameter_model,
            'scoped_resources': [scoped_resource_model],
        }

        self.read_mock.return_value = DetailedResponseMock(resource)
        self.update_mock.return_value = DetailedResponseMock(resource)

        set_module_args({
            'policy_id': 'testString',
            'name': 'Agent1-DevWS',
            'description': 'Policy for job execution of secured workspaces on agent1',
            'resource_group': 'Default',
            'tags': ['policy:secured-job'],
            'location': 'us-south',
            'schematics_policy_state': user_state_model,
            'kind': 'agent_assignment_policy',
            'target': policy_objects_model,
            'parameter': policy_parameter_model,
            'scoped_resources': [scoped_resource_model],
        })

        with self.assertRaises(AnsibleExitJson) as result:
            os.environ['SCHEMATICS_AUTH_TYPE'] = 'noAuth'
            ibm_schematics_policy.main()

        self.assertTrue(result.exception.args[0]['changed'])
        for field, value in resource.items():
            self.assertEqual(value, result.exception.args[0].get(field))

        mock_data = dict(
            policy_id='testString',
            name='Agent1-DevWS',
            description='Policy for job execution of secured workspaces on agent1',
            resource_group='Default',
            tags=['policy:secured-job'],
            location='us-south',
            state=user_state_model,
            kind='agent_assignment_policy',
            target=policy_objects_model,
            parameter=policy_parameter_model,
            scoped_resources=[scoped_resource_model],
        )

        self.update_mock.assert_called_once()
        self.assertTrue(checkResult(mock_data, self.update_mock.call_args.kwargs))

        read_mock_data = dict(
            policy_id='testString',
            profile='summary',
        )
        # Set the variables that belong to the "read" path to `None`
        # because we test the "update" path here.
        for param in read_mock_data:
            read_mock_data[param] = mock_data.get(param, None)

        self.read_mock.assert_called_once()
        self.assertTrue(checkResult(read_mock_data, self.read_mock.call_args.kwargs))

    @mock_operations
    def test_update_ibm_schematics_policy_failed(self):
        """Test the "update" path - failed."""
        user_state_model = {
            'state': 'draft',
            'set_by': 'testString',
            'set_at': '2019-01-01T12:00:00.000Z',
        }

        policy_object_selector_model = {
            'kind': 'workspace',
            'tags': ['testString'],
            'resource_groups': ['testString'],
            'locations': ['us-south'],
        }

        policy_objects_model = {
            'selector_kind': 'ids',
            'selector_ids': ['testString'],
            'selector_scope': [policy_object_selector_model],
        }

        agent_assignment_policy_parameter_model = {
            'selector_kind': 'ids',
            'selector_ids': ['testString'],
            'selector_scope': [policy_object_selector_model],
        }

        policy_parameter_model = {
            'agent_assignment_policy_parameter': agent_assignment_policy_parameter_model,
        }

        scoped_resource_model = {
            'kind': 'workspace',
            'id': 'testString',
        }

        resource = {
            'policy_id': 'testString',
            'name': 'Agent1-DevWS',
            'description': 'Policy for job execution of secured workspaces on agent1',
            'resource_group': 'Default',
            'tags': ['policy:secured-job'],
            'location': 'us-south',
            'schematics_policy_state': user_state_model,
            'kind': 'agent_assignment_policy',
            'target': policy_objects_model,
            'parameter': policy_parameter_model,
            'scoped_resources': [scoped_resource_model],
        }

        self.read_mock.return_value = DetailedResponseMock(resource)
        self.update_mock.side_effect = ApiException(400, message='Update ibm_schematics_policy error')

        set_module_args({
            'policy_id': 'testString',
            'name': 'Agent1-DevWS',
            'description': 'Policy for job execution of secured workspaces on agent1',
            'resource_group': 'Default',
            'tags': ['policy:secured-job'],
            'location': 'us-south',
            'schematics_policy_state': user_state_model,
            'kind': 'agent_assignment_policy',
            'target': policy_objects_model,
            'parameter': policy_parameter_model,
            'scoped_resources': [scoped_resource_model],
        })

        with self.assertRaises(AnsibleFailJson) as result:
            os.environ['SCHEMATICS_AUTH_TYPE'] = 'noAuth'
            ibm_schematics_policy.main()

        self.assertEqual(result.exception.args[0]['msg'], 'Update ibm_schematics_policy error')

        mock_data = dict(
            policy_id='testString',
            name='Agent1-DevWS',
            description='Policy for job execution of secured workspaces on agent1',
            resource_group='Default',
            tags=['policy:secured-job'],
            location='us-south',
            state=user_state_model,
            kind='agent_assignment_policy',
            target=policy_objects_model,
            parameter=policy_parameter_model,
            scoped_resources=[scoped_resource_model],
        )

        self.update_mock.assert_called_once()
        self.assertTrue(checkResult(mock_data, self.update_mock.call_args.kwargs))

        read_mock_data = dict(
            policy_id='testString',
            profile='summary',
        )
        # Set the variables that belong to the "read" path to `None`
        # because we test the "update" path here.
        for param in read_mock_data:
            read_mock_data[param] = mock_data.get(param, None)

        self.read_mock.assert_called_once()
        self.assertTrue(checkResult(read_mock_data, self.read_mock.call_args.kwargs))

    @mock_operations
    def test_delete_ibm_schematics_policy_success(self):
        """Test the "delete" path - successfull."""
        self.read_mock.return_value = DetailedResponseMock()
        self.delete_mock.return_value = DetailedResponseMock()

        args = {
            'policy_id': 'testString',
            'state': 'absent',
        }

        set_module_args(args)

        with self.assertRaises(AnsibleExitJson) as result:
            os.environ['SCHEMATICS_AUTH_TYPE'] = 'noAuth'
            ibm_schematics_policy.main()

        self.assertTrue(result.exception.args[0]['changed'])
        self.assertEqual(result.exception.args[0]['id'], 'testString')
        self.assertEqual(result.exception.args[0]['status'], 'deleted')

        mock_data = dict(
            policy_id='testString',
        )

        self.delete_mock.assert_called_once()
        self.assertTrue(checkResult(mock_data, self.delete_mock.call_args.kwargs))

        read_mock_data = dict(
            policy_id='testString',
            profile='summary',
        )
        # Set the variables that belong to the "read" path to `None`
        # because we test the "delete" path here.
        for param in read_mock_data:
            read_mock_data[param] = mock_data.get(param, None)

        self.read_mock.assert_called_once()
        self.assertTrue(checkResult(read_mock_data, self.read_mock.call_args.kwargs))

    @mock_operations
    def test_delete_ibm_schematics_policy_not_exists(self):
        """Test the "delete" path - not exists."""
        self.read_mock.side_effect = ApiException(404)
        self.delete_mock.return_value = DetailedResponseMock()

        args = {
            'policy_id': 'testString',
            'state': 'absent',
        }

        set_module_args(args)

        with self.assertRaises(AnsibleExitJson) as result:
            os.environ['SCHEMATICS_AUTH_TYPE'] = 'noAuth'
            ibm_schematics_policy.main()

        self.assertFalse(result.exception.args[0]['changed'])
        self.assertEqual(result.exception.args[0]['id'], 'testString')
        self.assertEqual(result.exception.args[0]['status'], 'not_found')

        mock_data = dict(
            policy_id='testString',
        )

        self.delete_mock.assert_not_called()

        read_mock_data = dict(
            policy_id='testString',
            profile='summary',
        )
        # Set the variables that belong to the "read" path to `None`
        # because we test the "delete" path here.
        for param in read_mock_data:
            read_mock_data[param] = mock_data.get(param, None)

        self.read_mock.assert_called_once()
        self.assertTrue(checkResult(read_mock_data, self.read_mock.call_args.kwargs))

    @mock_operations
    def test_delete_ibm_schematics_policy_failed(self):
        """Test the "delete" path - failed."""
        self.read_mock.return_value = DetailedResponseMock()
        self.delete_mock.side_effect = ApiException(400, message='Delete ibm_schematics_policy error')

        set_module_args({
            'policy_id': 'testString',
            'state': 'absent',
        })

        with self.assertRaises(AnsibleFailJson) as result:
            os.environ['SCHEMATICS_AUTH_TYPE'] = 'noAuth'
            ibm_schematics_policy.main()

        self.assertEqual(result.exception.args[0]['msg'], 'Delete ibm_schematics_policy error')

        mock_data = dict(
            policy_id='testString',
        )

        self.delete_mock.assert_called_once()
        self.assertTrue(checkResult(mock_data, self.delete_mock.call_args.kwargs))

        read_mock_data = dict(
            policy_id='testString',
            profile='summary',
        )
        # Set the variables that belong to the "read" path to `None`
        # because we test the "delete" path here.
        for param in read_mock_data:
            read_mock_data[param] = mock_data.get(param, None)

        self.read_mock.assert_called_once()
        self.assertTrue(checkResult(read_mock_data, self.read_mock.call_args.kwargs))
