# (C) Copyright IBM Corp. 2022.
# GNU General Public License v3.0+ (see LICENSE or https://www.gnu.org/licenses/gpl-3.0.txt)


import os

from ibm_cloud_sdk_core import ApiException
from ansible_collections.community.internal_test_tools.tests.unit.compat.mock import patch
from ansible_collections.community.internal_test_tools.tests.unit.plugins.modules.utils import ModuleTestCase, AnsibleFailJson, AnsibleExitJson, set_module_args

from .common import DetailedResponseMock
from plugins.modules import ibm_cm_catalog


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


class TestCatalogModule(ModuleTestCase):
    """
    Test class for Catalog module testing.
    """

    def test_read_ibm_cm_catalog_failed(self):
        """Test the inner "read" path in this module with a server error response."""

        patcher = patch(
            'plugins.modules.ibm_cm_catalog.CatalogManagementV1.get_catalog')
        mock = patcher.start()
        mock.side_effect = ApiException(500, message='Something went wrong...')

        set_module_args({
            'catalog_identifier': 'testString',
        })

        with self.assertRaises(AnsibleFailJson) as result:
            os.environ['CATALOG_MANAGEMENT_AUTH_TYPE'] = 'noAuth'
            os.environ['IC_API_KEY'] = 'noAuthAPIKey'
            ibm_cm_catalog.main()

        assert result.exception.args[0]['msg'] == 'Something went wrong...'

        mock_data = dict(
            catalog_identifier='testString',
        )

        mock.assert_called_once()
        processed_result = post_process_result(
            mock_data, mock.call_args.kwargs)
        assert mock_data == processed_result

        patcher.stop()

    def test_create_ibm_cm_catalog_success(self):
        """Test the "create" path - successful."""
        feature_model = {
            'title': 'testString',
            'description': 'testString',
        }

        filter_terms_model = {
            'filter_terms': ['testString'],
        }

        category_filter_model = {
            'include': True,
            'filter': filter_terms_model,
        }

        id_filter_model = {
            'include': filter_terms_model,
            'exclude': filter_terms_model,
        }

        filters_model = {
            'include_all': True,
            'category_filters': category_filter_model,
            'id_filters': id_filter_model,
        }

        syndication_cluster_model = {
            'region': 'testString',
            'id': 'testString',
            'name': 'testString',
            'resource_group_name': 'testString',
            'type': 'testString',
            'namespaces': ['testString'],
            'all_namespaces': True,
        }

        syndication_history_model = {
            'namespaces': ['testString'],
            'clusters': [syndication_cluster_model],
            'last_run': '2019-01-01T12:00:00.000Z',
        }

        syndication_authorization_model = {
            'token': 'testString',
            'last_run': '2019-01-01T12:00:00.000Z',
        }

        syndication_resource_model = {
            'remove_related_components': True,
            'clusters': [syndication_cluster_model],
            'history': syndication_history_model,
            'authorization': syndication_authorization_model,
        }

        resource = {
            'id': 'testString',
            'rev': 'testString',
            'label': 'testString',
            'short_description': 'testString',
            'catalog_icon_url': 'testString',
            'tags': ['testString'],
            'features': [feature_model],
            'disabled': True,
            'resource_group_id': 'testString',
            'owning_account': 'testString',
            'catalog_filters': filters_model,
            'syndication_settings': syndication_resource_model,
            'kind': 'testString',
        }

        patcher = patch(
            'plugins.modules.ibm_cm_catalog.CatalogManagementV1.create_catalog')
        mock = patcher.start()
        mock.return_value = DetailedResponseMock(resource)

        get_catalog_patcher = patch(
            'plugins.modules.ibm_cm_catalog.CatalogManagementV1.get_catalog')
        get_catalog_mock = get_catalog_patcher.start()

        set_module_args({
            'id': 'testString',
            'rev': 'testString',
            'label': 'testString',
            'short_description': 'testString',
            'catalog_icon_url': 'testString',
            'tags': ['testString'],
            'features': [feature_model],
            'disabled': True,
            'resource_group_id': 'testString',
            'owning_account': 'testString',
            'catalog_filters': filters_model,
            'syndication_settings': syndication_resource_model,
            'kind': 'testString',
        })

        with self.assertRaises(AnsibleExitJson) as result:
            os.environ['CATALOG_MANAGEMENT_AUTH_TYPE'] = 'noAuth'
            os.environ['IC_API_KEY'] = 'noAuthAPIKey'
            ibm_cm_catalog.main()

        assert result.exception.args[0]['changed'] is True
        assert result.exception.args[0]['msg'] == resource

        mock_data = dict(
            id='testString',
            rev='testString',
            label='testString',
            short_description='testString',
            catalog_icon_url='testString',
            tags=['testString'],
            features=[feature_model],
            disabled=True,
            resource_group_id='testString',
            owning_account='testString',
            catalog_filters=filters_model,
            syndication_settings=syndication_resource_model,
            kind='testString',
        )

        mock.assert_called_once()
        processed_result = post_process_result(
            mock_data, mock.call_args.kwargs)
        assert mock_data == processed_result

        get_catalog_mock.assert_not_called()

        get_catalog_patcher.stop()
        patcher.stop()

    def test_create_ibm_cm_catalog_failed(self):
        """Test the "create" path - failed."""

        get_catalog_patcher = patch(
            'plugins.modules.ibm_cm_catalog.CatalogManagementV1.get_catalog')
        get_catalog_mock = get_catalog_patcher.start()

        patcher = patch(
            'plugins.modules.ibm_cm_catalog.CatalogManagementV1.create_catalog')
        mock = patcher.start()
        mock.side_effect = ApiException(
            400, message='Create ibm_cm_catalog error')

        feature_model = {
            'title': 'testString',
            'description': 'testString',
        }

        filter_terms_model = {
            'filter_terms': ['testString'],
        }

        category_filter_model = {
            'include': True,
            'filter': filter_terms_model,
        }

        id_filter_model = {
            'include': filter_terms_model,
            'exclude': filter_terms_model,
        }

        filters_model = {
            'include_all': True,
            'category_filters': category_filter_model,
            'id_filters': id_filter_model,
        }

        syndication_cluster_model = {
            'region': 'testString',
            'id': 'testString',
            'name': 'testString',
            'resource_group_name': 'testString',
            'type': 'testString',
            'namespaces': ['testString'],
            'all_namespaces': True,
        }

        syndication_history_model = {
            'namespaces': ['testString'],
            'clusters': [syndication_cluster_model],
            'last_run': '2019-01-01T12:00:00.000Z',
        }

        syndication_authorization_model = {
            'token': 'testString',
            'last_run': '2019-01-01T12:00:00.000Z',
        }

        syndication_resource_model = {
            'remove_related_components': True,
            'clusters': [syndication_cluster_model],
            'history': syndication_history_model,
            'authorization': syndication_authorization_model,
        }

        set_module_args({
            'id': 'testString',
            'rev': 'testString',
            'label': 'testString',
            'short_description': 'testString',
            'catalog_icon_url': 'testString',
            'tags': ['testString'],
            'features': [feature_model],
            'disabled': True,
            'resource_group_id': 'testString',
            'owning_account': 'testString',
            'catalog_filters': filters_model,
            'syndication_settings': syndication_resource_model,
            'kind': 'testString',
        })

        with self.assertRaises(AnsibleFailJson) as result:
            os.environ['CATALOG_MANAGEMENT_AUTH_TYPE'] = 'noAuth'
            os.environ['IC_API_KEY'] = 'noAuthAPIKey'
            ibm_cm_catalog.main()

        assert result.exception.args[0]['msg'] == 'Create ibm_cm_catalog error'

        mock_data = dict(
            id='testString',
            rev='testString',
            label='testString',
            short_description='testString',
            catalog_icon_url='testString',
            tags=['testString'],
            features=[feature_model],
            disabled=True,
            resource_group_id='testString',
            owning_account='testString',
            catalog_filters=filters_model,
            syndication_settings=syndication_resource_model,
            kind='testString',
        )

        mock.assert_called_once()
        processed_result = post_process_result(
            mock_data, mock.call_args.kwargs)
        assert mock_data == processed_result

        get_catalog_mock.assert_not_called()

        get_catalog_patcher.stop()
        patcher.stop()

    def test_update_ibm_cm_catalog_success(self):
        """Test the "update" path - successful."""
        feature_model = {
            'title': 'testString',
            'description': 'testString',
        }

        filter_terms_model = {
            'filter_terms': ['testString'],
        }

        category_filter_model = {
            'include': True,
            'filter': filter_terms_model,
        }

        id_filter_model = {
            'include': filter_terms_model,
            'exclude': filter_terms_model,
        }

        filters_model = {
            'include_all': True,
            'category_filters': category_filter_model,
            'id_filters': id_filter_model,
        }

        syndication_cluster_model = {
            'region': 'testString',
            'id': 'testString',
            'name': 'testString',
            'resource_group_name': 'testString',
            'type': 'testString',
            'namespaces': ['testString'],
            'all_namespaces': True,
        }

        syndication_history_model = {
            'namespaces': ['testString'],
            'clusters': [syndication_cluster_model],
            'last_run': '2019-01-01T12:00:00.000Z',
        }

        syndication_authorization_model = {
            'token': 'testString',
            'last_run': '2019-01-01T12:00:00.000Z',
        }

        syndication_resource_model = {
            'remove_related_components': True,
            'clusters': [syndication_cluster_model],
            'history': syndication_history_model,
            'authorization': syndication_authorization_model,
        }

        resource = {
            'catalog_identifier': 'testString',
            'id': 'testString',
            'rev': 'testString',
            'label': 'testString',
            'short_description': 'testString',
            'catalog_icon_url': 'testString',
            'tags': ['testString'],
            'features': [feature_model],
            'disabled': True,
            'resource_group_id': 'testString',
            'owning_account': 'testString',
            'catalog_filters': filters_model,
            'syndication_settings': syndication_resource_model,
            'kind': 'testString',
        }

        patcher = patch(
            'plugins.modules.ibm_cm_catalog.CatalogManagementV1.replace_catalog')
        mock = patcher.start()
        mock.return_value = DetailedResponseMock(resource)

        get_catalog_patcher = patch(
            'plugins.modules.ibm_cm_catalog.CatalogManagementV1.get_catalog')
        get_catalog_mock = get_catalog_patcher.start()
        get_catalog_mock.return_value = DetailedResponseMock(resource)

        set_module_args({
            'catalog_identifier': 'testString',
            'id': 'testString',
            'rev': 'testString',
            'label': 'testString',
            'short_description': 'testString',
            'catalog_icon_url': 'testString',
            'tags': ['testString'],
            'features': [feature_model],
            'disabled': True,
            'resource_group_id': 'testString',
            'owning_account': 'testString',
            'catalog_filters': filters_model,
            'syndication_settings': syndication_resource_model,
            'kind': 'testString',
        })

        with self.assertRaises(AnsibleExitJson) as result:
            os.environ['CATALOG_MANAGEMENT_AUTH_TYPE'] = 'noAuth'
            os.environ['IC_API_KEY'] = 'noAuthAPIKey'
            ibm_cm_catalog.main()

        assert result.exception.args[0]['changed'] is True
        assert result.exception.args[0]['msg'] == resource

        mock_data = dict(
            catalog_identifier='testString',
            id='testString',
            rev='testString',
            label='testString',
            short_description='testString',
            catalog_icon_url='testString',
            tags=['testString'],
            features=[feature_model],
            disabled=True,
            resource_group_id='testString',
            owning_account='testString',
            catalog_filters=filters_model,
            syndication_settings=syndication_resource_model,
            kind='testString',
        )

        mock.assert_called_once()
        processed_result = post_process_result(
            mock_data, mock.call_args.kwargs)
        assert mock_data == processed_result

        get_catalog_mock_data = dict(
            catalog_identifier='testString',
        )
        # Set the variables that belong to the "read" path to `None`
        # since we test the "delete" path here.
        for param in get_catalog_mock_data:
            get_catalog_mock_data[param] = mock_data.get(param, None)

        get_catalog_mock.assert_called_once()
        get_catalog_processed_result = post_process_result(
            get_catalog_mock_data, get_catalog_mock.call_args.kwargs)
        assert get_catalog_mock_data == get_catalog_processed_result
        get_catalog_patcher.stop()
        patcher.stop()

    def test_update_ibm_cm_catalog_failed(self):
        """Test the "update" path - failed."""
        feature_model = {
            'title': 'testString',
            'description': 'testString',
        }

        filter_terms_model = {
            'filter_terms': ['testString'],
        }

        category_filter_model = {
            'include': True,
            'filter': filter_terms_model,
        }

        id_filter_model = {
            'include': filter_terms_model,
            'exclude': filter_terms_model,
        }

        filters_model = {
            'include_all': True,
            'category_filters': category_filter_model,
            'id_filters': id_filter_model,
        }

        syndication_cluster_model = {
            'region': 'testString',
            'id': 'testString',
            'name': 'testString',
            'resource_group_name': 'testString',
            'type': 'testString',
            'namespaces': ['testString'],
            'all_namespaces': True,
        }

        syndication_history_model = {
            'namespaces': ['testString'],
            'clusters': [syndication_cluster_model],
            'last_run': '2019-01-01T12:00:00.000Z',
        }

        syndication_authorization_model = {
            'token': 'testString',
            'last_run': '2019-01-01T12:00:00.000Z',
        }

        syndication_resource_model = {
            'remove_related_components': True,
            'clusters': [syndication_cluster_model],
            'history': syndication_history_model,
            'authorization': syndication_authorization_model,
        }

        resource = {
            'catalog_identifier': 'testString',
            'id': 'testString',
            'rev': 'testString',
            'label': 'testString',
            'short_description': 'testString',
            'catalog_icon_url': 'testString',
            'tags': ['testString'],
            'features': [feature_model],
            'disabled': True,
            'resource_group_id': 'testString',
            'owning_account': 'testString',
            'catalog_filters': filters_model,
            'syndication_settings': syndication_resource_model,
            'kind': 'testString',
        }

        patcher = patch(
            'plugins.modules.ibm_cm_catalog.CatalogManagementV1.replace_catalog')
        mock = patcher.start()
        mock.side_effect = ApiException(
            400, message='Update ibm_cm_catalog error')

        get_catalog_patcher = patch(
            'plugins.modules.ibm_cm_catalog.CatalogManagementV1.get_catalog')
        get_catalog_mock = get_catalog_patcher.start()
        get_catalog_mock.return_value = DetailedResponseMock(resource)

        set_module_args({
            'catalog_identifier': 'testString',
            'id': 'testString',
            'rev': 'testString',
            'label': 'testString',
            'short_description': 'testString',
            'catalog_icon_url': 'testString',
            'tags': ['testString'],
            'features': [feature_model],
            'disabled': True,
            'resource_group_id': 'testString',
            'owning_account': 'testString',
            'catalog_filters': filters_model,
            'syndication_settings': syndication_resource_model,
            'kind': 'testString',
        })

        with self.assertRaises(AnsibleFailJson) as result:
            os.environ['CATALOG_MANAGEMENT_AUTH_TYPE'] = 'noAuth'
            os.environ['IC_API_KEY'] = 'noAuthAPIKey'
            ibm_cm_catalog.main()

        assert result.exception.args[0]['msg'] == 'Update ibm_cm_catalog error'

        mock_data = dict(
            catalog_identifier='testString',
            id='testString',
            rev='testString',
            label='testString',
            short_description='testString',
            catalog_icon_url='testString',
            tags=['testString'],
            features=[feature_model],
            disabled=True,
            resource_group_id='testString',
            owning_account='testString',
            catalog_filters=filters_model,
            syndication_settings=syndication_resource_model,
            kind='testString',
        )

        mock.assert_called_once()
        processed_result = post_process_result(
            mock_data, mock.call_args.kwargs)
        assert mock_data == processed_result

        get_catalog_mock_data = dict(
            catalog_identifier='testString',
        )
        # Set the variables that belong to the "read" path to `None`
        # since we test the "delete" path here.
        for param in get_catalog_mock_data:
            get_catalog_mock_data[param] = mock_data.get(param, None)

        get_catalog_mock.assert_called_once()
        get_catalog_processed_result = post_process_result(
            get_catalog_mock_data, get_catalog_mock.call_args.kwargs)
        assert get_catalog_mock_data == get_catalog_processed_result

        get_catalog_patcher.stop()
        patcher.stop()

    def test_delete_ibm_cm_catalog_success(self):
        """Test the "delete" path - successfull."""
        patcher = patch(
            'plugins.modules.ibm_cm_catalog.CatalogManagementV1.delete_catalog')
        mock = patcher.start()
        mock.return_value = DetailedResponseMock()

        get_catalog_patcher = patch(
            'plugins.modules.ibm_cm_catalog.CatalogManagementV1.get_catalog')
        get_catalog_mock = get_catalog_patcher.start()
        get_catalog_mock.return_value = DetailedResponseMock()

        args = {
            'catalog_identifier': 'testString',
            'state': 'absent',
        }

        set_module_args(args)

        with self.assertRaises(AnsibleExitJson) as result:
            os.environ['CATALOG_MANAGEMENT_AUTH_TYPE'] = 'noAuth'
            os.environ['IC_API_KEY'] = 'noAuthAPIKey'
            ibm_cm_catalog.main()

        assert result.exception.args[0]['changed'] is True
        assert result.exception.args[0]['msg']['id'] == 'testString'
        assert result.exception.args[0]['msg']['status'] == 'deleted'

        mock_data = dict(
            catalog_identifier='testString',
        )

        mock.assert_called_once()
        processed_result = post_process_result(
            mock_data, mock.call_args.kwargs)
        assert mock_data == processed_result

        get_catalog_mock_data = dict(
            catalog_identifier='testString',
        )
        # Set the variables that belong to the "read" path to `None`
        # since we test the "delete" path here.
        for param in get_catalog_mock_data:
            get_catalog_mock_data[param] = mock_data.get(param, None)

        get_catalog_mock.assert_called_once()
        get_catalog_processed_result = post_process_result(
            get_catalog_mock_data, get_catalog_mock.call_args.kwargs)
        assert get_catalog_mock_data == get_catalog_processed_result

        get_catalog_patcher.stop()
        patcher.stop()

    def test_delete_ibm_cm_catalog_not_exists(self):
        """Test the "delete" path - not exists."""
        patcher = patch(
            'plugins.modules.ibm_cm_catalog.CatalogManagementV1.delete_catalog')
        mock = patcher.start()
        mock.return_value = DetailedResponseMock()

        get_catalog_patcher = patch(
            'plugins.modules.ibm_cm_catalog.CatalogManagementV1.get_catalog')
        get_catalog_mock = get_catalog_patcher.start()
        get_catalog_mock.side_effect = ApiException(404)

        args = {
            'catalog_identifier': 'testString',
            'state': 'absent',
        }

        set_module_args(args)

        with self.assertRaises(AnsibleExitJson) as result:
            os.environ['CATALOG_MANAGEMENT_AUTH_TYPE'] = 'noAuth'
            os.environ['IC_API_KEY'] = 'noAuthAPIKey'
            ibm_cm_catalog.main()

        assert result.exception.args[0]['changed'] is False
        assert result.exception.args[0]['msg']['id'] == 'testString'
        assert result.exception.args[0]['msg']['status'] == 'not_found'

        mock_data = dict(
            catalog_identifier='testString',
        )

        mock.assert_not_called()

        get_catalog_mock_data = dict(
            catalog_identifier='testString',
        )
        # Set the variables that belong to the "read" path to `None`
        # since we test the "delete" path here.
        for param in get_catalog_mock_data:
            get_catalog_mock_data[param] = mock_data.get(param, None)

        get_catalog_mock.assert_called_once()
        get_catalog_processed_result = post_process_result(
            get_catalog_mock_data, get_catalog_mock.call_args.kwargs)
        assert get_catalog_mock_data == get_catalog_processed_result

        get_catalog_patcher.stop()
        patcher.stop()

    def test_delete_ibm_cm_catalog_failed(self):
        """Test the "delete" path - failed."""
        patcher = patch(
            'plugins.modules.ibm_cm_catalog.CatalogManagementV1.delete_catalog')
        mock = patcher.start()
        mock.side_effect = ApiException(
            400, message='Delete ibm_cm_catalog error')

        get_catalog_patcher = patch(
            'plugins.modules.ibm_cm_catalog.CatalogManagementV1.get_catalog')
        get_catalog_mock = get_catalog_patcher.start()
        get_catalog_mock.return_value = DetailedResponseMock()

        set_module_args({
            'catalog_identifier': 'testString',
            'state': 'absent',
        })

        with self.assertRaises(AnsibleFailJson) as result:
            os.environ['CATALOG_MANAGEMENT_AUTH_TYPE'] = 'noAuth'
            os.environ['IC_API_KEY'] = 'noAuthAPIKey'
            ibm_cm_catalog.main()

        assert result.exception.args[0]['msg'] == 'Delete ibm_cm_catalog error'

        mock_data = dict(
            catalog_identifier='testString',
        )

        mock.assert_called_once()
        processed_result = post_process_result(
            mock_data, mock.call_args.kwargs)
        assert mock_data == processed_result

        get_catalog_mock_data = dict(
            catalog_identifier='testString',
        )
        # Set the variables that belong to the "read" path to `None`
        # since we test the "delete" path here.
        for param in get_catalog_mock_data:
            get_catalog_mock_data[param] = mock_data.get(param, None)

        get_catalog_mock.assert_called_once()
        get_catalog_processed_result = post_process_result(
            get_catalog_mock_data, get_catalog_mock.call_args.kwargs)
        assert get_catalog_mock_data == get_catalog_processed_result

        get_catalog_patcher.stop()
        patcher.stop()
