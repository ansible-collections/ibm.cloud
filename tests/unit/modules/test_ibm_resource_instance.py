# (C) Copyright IBM Corp. 2023.
#
# GNU General Public License v3.0+ (see LICENSE or https://www.gnu.org/licenses/gpl-3.0.txt)

from __future__ import (absolute_import, division, print_function)
__metaclass__ = type

import os

from ansible_collections.community.internal_test_tools.tests.unit.compat.mock import patch
from ansible_collections.community.internal_test_tools.tests.unit.plugins.modules.utils import ModuleTestCase, AnsibleFailJson, AnsibleExitJson, set_module_args
from plugins.modules import ibm_resource_instance

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
        self.assertIsNone(ibm_resource_instance.MISSING_IMPORT_EXC)

        # Set-up mocks for each operation.
        self.read_patcher = patch('plugins.modules.ibm_resource_instance.ResourceControllerV2.get_resource_instance')
        self.read_mock = self.read_patcher.start()
        self.create_patcher = patch('plugins.modules.ibm_resource_instance.ResourceControllerV2.create_resource_instance')
        self.create_mock = self.create_patcher.start()
        self.update_patcher = patch('plugins.modules.ibm_resource_instance.ResourceControllerV2.update_resource_instance')
        self.update_mock = self.update_patcher.start()
        self.delete_patcher = patch('plugins.modules.ibm_resource_instance.ResourceControllerV2.delete_resource_instance')
        self.delete_mock = self.delete_patcher.start()

        # Run the actual function.
        func(self)

        # Stop the patchers.
        self.read_patcher.stop()
        self.create_patcher.stop()
        self.update_patcher.stop()
        self.delete_patcher.stop()

    return wrapper


class TestResourceInstancePostModule(ModuleTestCase):
    """
    Test class for ResourceInstancePost module testing.
    """

    @mock_operations
    def test_read_ibm_resource_instance_failed(self):
        """Test the inner "read" path in this module with a server error response."""
        self.read_mock.side_effect = ApiException(500, message='Something went wrong...')

        set_module_args({
            'id': 'testString',
        })

        with self.assertRaises(AnsibleFailJson) as result:
            os.environ['RESOURCE_CONTROLLER_AUTH_TYPE'] = 'noAuth'
            ibm_resource_instance.main()

        self.assertEqual(result.exception.args[0]['msg'], 'Something went wrong...')

        mock_data = dict(
            id='testString',
        )

        self.read_mock.assert_called_once()
        self.assertTrue(checkResult(mock_data, self.read_mock.call_args.kwargs))

    @mock_operations
    def test_create_ibm_resource_instance_success(self):
        """Test the "create" path - successful."""
        resource = {
            'name': 'my-instance',
            'location': 'bluemix-us-south',
            'resource_group': '5c49eabc-f5e8-5881-a37e-2d100a33b3df',
            'plan': 'cloudant-standard',
            'tags': ['testString'],
            'allow_cleanup': False,
            'parameters': {'key1': 'testString'},
            'entity_lock': False,
        }

        self.read_mock.side_effect = ApiException(404)
        self.create_mock.return_value = DetailedResponseMock(resource)

        set_module_args({
            'name': 'my-instance',
            'location': 'bluemix-us-south',
            'resource_group': '5c49eabc-f5e8-5881-a37e-2d100a33b3df',
            'plan': 'cloudant-standard',
            'tags': ['testString'],
            'allow_cleanup': False,
            'parameters': {'key1': 'testString'},
            'entity_lock': False,
        })

        with self.assertRaises(AnsibleExitJson) as result:
            os.environ['RESOURCE_CONTROLLER_AUTH_TYPE'] = 'noAuth'
            os.environ['IC_API_KEY'] = 'noAuthAPIKey'
            os.environ['GLOBAL_CATALOG_AUTH_TYPE'] = 'noAuth'
            ibm_resource_instance.main()

        assert result.exception.args[0]['changed'] is True
        assert result.exception.args[0]['msg'] == resource

        mock_data = dict(
            name='my-instance',
            target='',
            resource_group='5c49eabc-f5e8-5881-a37e-2d100a33b3df',
            resource_plan_id='',
            tags=['testString'],
            allow_cleanup=False,
            parameters={'key1': 'testString'},
            entity_lock=False,
        )

        self.create_mock.assert_called_once()
        self.assertTrue(checkResult(mock_data, self.create_mock.call_args.kwargs))

    @mock_operations
    def test_create_ibm_resource_instance_failed(self):
        """Test the "create" path - failed."""
        self.read_mock.side_effect = ApiException(404)
        self.create_mock.side_effect = ApiException(400, message='Create ibm_resource_instance error')

        set_module_args({
            'name': 'my-instance',
            'location': 'bluemix-us-south',
            'resource_group': '5c49eabc-f5e8-5881-a37e-2d100a33b3df',
            'plan': 'cloudant-standard',
            'tags': ['testString'],
            'allow_cleanup': False,
            'parameters': {'key1': 'testString'},
            'entity_lock': False,
        })

        with self.assertRaises(AnsibleFailJson) as result:
            os.environ['RESOURCE_CONTROLLER_AUTH_TYPE'] = 'noAuth'
            os.environ['IC_API_KEY'] = 'noAuthAPIKey'
            os.environ['GLOBAL_CATALOG_AUTH_TYPE'] = 'noAuth'
            ibm_resource_instance.main()

        self.assertEqual(result.exception.args[0]['msg'], 'Create ibm_resource_instance error')

        mock_data = dict(
            name='my-instance',
            target='',
            resource_group='5c49eabc-f5e8-5881-a37e-2d100a33b3df',
            resource_plan_id='',
            tags=['testString'],
            allow_cleanup=False,
            parameters={'key1': 'testString'},
            entity_lock=False,
        )

        self.create_mock.assert_called_once()
        self.assertTrue(checkResult(mock_data, self.create_mock.call_args.kwargs))

    @mock_operations
    def test_update_ibm_resource_instance_success(self):
        """Test the "update" path - successful."""
        resource = {
            'id': 'testString',
            'name': 'my-new-instance-name',
            'parameters': {'key1': 'testString'},
            'plan': 'a8dff6d3-d287-4668-a81d-c87c55c2656d',
            'allow_cleanup': True,
        }

        self.read_mock.return_value = DetailedResponseMock(resource)
        self.update_mock.return_value = DetailedResponseMock(resource)

        set_module_args({
            'id': 'testString',
            'name': 'my-new-instance-name',
            'parameters': {'key1': 'testString'},
            'plan': 'a8dff6d3-d287-4668-a81d-c87c55c2656d',
            'allow_cleanup': True,
        })

        with self.assertRaises(AnsibleExitJson) as result:
            os.environ['RESOURCE_CONTROLLER_AUTH_TYPE'] = 'noAuth'
            os.environ['IC_API_KEY'] = 'noAuthAPIKey'
            os.environ['GLOBAL_CATALOG_AUTH_TYPE'] = 'noAuth'
            ibm_resource_instance.main()

        assert result.exception.args[0]['changed'] is True
        assert result.exception.args[0]['msg'] == resource

        mock_data = dict(
            id='testString',
            name='my-new-instance-name',
            parameters={'key1': 'testString'},
            resource_plan_id='a8dff6d3-d287-4668-a81d-c87c55c2656d',
            allow_cleanup=True,
        )

        self.update_mock.assert_called_once()
        self.assertTrue(checkResult(mock_data, self.update_mock.call_args.kwargs))

        read_mock_data = dict(
            id='testString',
        )
        # Set the variables that belong to the "read" path to `None`
        # because we test the "update" path here.
        for param in read_mock_data:
            read_mock_data[param] = mock_data.get(param, None)

        self.read_mock.assert_called_once()
        self.assertTrue(checkResult(read_mock_data, self.read_mock.call_args.kwargs))

    @mock_operations
    def test_update_ibm_resource_instance_failed(self):
        """Test the "update" path - failed."""
        resource = {
            'id': 'testString',
            'name': 'my-new-instance-name',
            'parameters': {'key1': 'testString'},
            'plan': 'a8dff6d3-d287-4668-a81d-c87c55c2656d',
            'allow_cleanup': True,
        }

        self.read_mock.return_value = DetailedResponseMock(resource)
        self.update_mock.side_effect = ApiException(400, message='Update ibm_resource_instance error')

        set_module_args({
            'id': 'testString',
            'name': 'my-new-instance-name',
            'parameters': {'key1': 'testString'},
            'plan': 'a8dff6d3-d287-4668-a81d-c87c55c2656d',
            'allow_cleanup': True,
        })

        with self.assertRaises(AnsibleFailJson) as result:
            os.environ['RESOURCE_CONTROLLER_AUTH_TYPE'] = 'noAuth'
            os.environ['IC_API_KEY'] = 'noAuthAPIKey'
            os.environ['GLOBAL_CATALOG_AUTH_TYPE'] = 'noAuth'
            ibm_resource_instance.main()

        self.assertEqual(result.exception.args[0]['msg'], 'Update ibm_resource_instance error')

        mock_data = dict(
            id='testString',
            name='my-new-instance-name',
            parameters={'key1': 'testString'},
            resource_plan_id='a8dff6d3-d287-4668-a81d-c87c55c2656d',
            allow_cleanup=True,
        )

        self.update_mock.assert_called_once()
        self.assertTrue(checkResult(mock_data, self.update_mock.call_args.kwargs))

        read_mock_data = dict(
            id='testString',
        )
        # Set the variables that belong to the "read" path to `None`
        # because we test the "update" path here.
        for param in read_mock_data:
            read_mock_data[param] = mock_data.get(param, None)

        self.read_mock.assert_called_once()
        self.assertTrue(checkResult(read_mock_data, self.read_mock.call_args.kwargs))

    @mock_operations
    def test_delete_ibm_resource_instance_success(self):
        """Test the "delete" path - successfull."""
        self.read_mock.return_value = DetailedResponseMock()
        self.delete_mock.return_value = DetailedResponseMock()

        args = {
            'id': 'testString',
            'recursive': False,
            'state': 'absent',
        }

        set_module_args(args)

        with self.assertRaises(AnsibleExitJson) as result:
            os.environ['RESOURCE_CONTROLLER_AUTH_TYPE'] = 'noAuth'
            ibm_resource_instance.main()

        self.assertTrue(result.exception.args[0]['changed'])
        self.assertEqual(result.exception.args[0]['id'], 'testString')
        self.assertEqual(result.exception.args[0]['status'], 'deleted')

        mock_data = dict(
            id='testString',
            recursive=False,
        )

        self.delete_mock.assert_called_once()
        self.assertTrue(checkResult(mock_data, self.delete_mock.call_args.kwargs))

        read_mock_data = dict(
            id='testString',
        )
        # Set the variables that belong to the "read" path to `None`
        # because we test the "delete" path here.
        for param in read_mock_data:
            read_mock_data[param] = mock_data.get(param, None)

        self.read_mock.assert_called_once()
        self.assertTrue(checkResult(read_mock_data, self.read_mock.call_args.kwargs))

    @mock_operations
    def test_delete_ibm_resource_instance_not_exists(self):
        """Test the "delete" path - not exists."""
        self.read_mock.side_effect = ApiException(404)
        self.delete_mock.return_value = DetailedResponseMock()

        args = {
            'id': 'testString',
            'recursive': False,
            'state': 'absent',
        }

        set_module_args(args)

        with self.assertRaises(AnsibleExitJson) as result:
            os.environ['RESOURCE_CONTROLLER_AUTH_TYPE'] = 'noAuth'
            ibm_resource_instance.main()

        self.assertFalse(result.exception.args[0]['changed'])
        self.assertEqual(result.exception.args[0]['id'], 'testString')
        self.assertEqual(result.exception.args[0]['status'], 'not_found')

        mock_data = dict(
            id='testString',
            recursive=False,
        )

        self.delete_mock.assert_not_called()

        read_mock_data = dict(
            id='testString',
        )
        # Set the variables that belong to the "read" path to `None`
        # because we test the "delete" path here.
        for param in read_mock_data:
            read_mock_data[param] = mock_data.get(param, None)

        self.read_mock.assert_called_once()
        self.assertTrue(checkResult(read_mock_data, self.read_mock.call_args.kwargs))

    @mock_operations
    def test_delete_ibm_resource_instance_failed(self):
        """Test the "delete" path - failed."""
        self.read_mock.return_value = DetailedResponseMock()
        self.delete_mock.side_effect = ApiException(400, message='Delete ibm_resource_instance error')

        set_module_args({
            'id': 'testString',
            'recursive': False,
            'state': 'absent',
        })

        with self.assertRaises(AnsibleFailJson) as result:
            os.environ['RESOURCE_CONTROLLER_AUTH_TYPE'] = 'noAuth'
            ibm_resource_instance.main()

        self.assertEqual(result.exception.args[0]['msg'], 'Delete ibm_resource_instance error')

        mock_data = dict(
            id='testString',
            recursive=False,
        )

        self.delete_mock.assert_called_once()
        self.assertTrue(checkResult(mock_data, self.delete_mock.call_args.kwargs))

        read_mock_data = dict(
            id='testString',
        )
        # Set the variables that belong to the "read" path to `None`
        # because we test the "delete" path here.
        for param in read_mock_data:
            read_mock_data[param] = mock_data.get(param, None)

        self.read_mock.assert_called_once()
        self.assertTrue(checkResult(read_mock_data, self.read_mock.call_args.kwargs))
