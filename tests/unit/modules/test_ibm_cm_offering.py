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


import os

from ibm_cloud_sdk_core import ApiException
from ansible_collections.community.internal_test_tools.tests.unit.compat.mock import patch
from ansible_collections.community.internal_test_tools.tests.unit.plugins.modules.utils import ModuleTestCase, AnsibleFailJson, AnsibleExitJson, set_module_args

from .common import DetailedResponseMock
from plugins.modules import ibm_cm_offering


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


class TestOfferingModule(ModuleTestCase):
    """
    Test class for Offering module testing.
    """

    def test_read_ibm_cm_offering_failed(self):
        """Test the inner "read" path in this module with a server error response."""

        patcher = patch(
            'plugins.modules.ibm_cm_offering.CatalogManagementV1.get_offering')
        mock = patcher.start()
        mock.side_effect = ApiException(500, message='Something went wrong...')

        set_module_args({
            'catalog_identifier': 'testString',
            'offering_id': 'testString',
            'type': 'testString',
            'digest': True,
        })

        with self.assertRaises(AnsibleFailJson) as result:
            os.environ['CATALOG_MANAGEMENT_AUTH_TYPE'] = 'noAuth'
            os.environ['IC_API_KEY'] = 'noAuthAPIKey'
            ibm_cm_offering.main()

        assert result.exception.args[0]['msg'] == 'Something went wrong...'

        mock_data = dict(
            catalog_identifier='testString',
            offering_id='testString',
            type='testString',
            digest=True,
        )

        mock.assert_called_once()
        processed_result = post_process_result(
            mock_data, mock.call_args.kwargs)
        assert mock_data == processed_result

        patcher.stop()

    def test_create_ibm_cm_offering_success(self):
        """Test the "create" path - successful."""
        rating_model = {
            'one_star_count': 38,
            'two_star_count': 38,
            'three_star_count': 38,
            'four_star_count': 38,
        }

        feature_model = {
            'title': 'testString',
            'description': 'testString',
        }

        configuration_model = {
            'key': 'testString',
            'type': 'testString',
            'default_value': 'testString',
            'value_constraint': 'testString',
            'description': 'testString',
            'required': True,
            'options': ['testString'],
            'hidden': True,
        }

        validation_model = {
            'validated': '2019-01-01T12:00:00.000Z',
            'requested': '2019-01-01T12:00:00.000Z',
            'state_': 'testString',
            'last_operation': 'testString',
            'target': {'key1': 'testString'},
        }

        resource_model = {
            'type': 'mem',
            # 'value': 'testString',
        }

        script_model = {
            'instructions': 'testString',
            'script': 'testString',
            'script_permission': 'testString',
            'delete_script': 'testString',
            'scope': 'testString',
        }

        version_entitlement_model = {
            'provider_name': 'testString',
            'provider_id': 'testString',
            'product_id': 'testString',
            'part_numbers': ['testString'],
            'image_repo_name': 'testString',
        }

        license_model = {
            'id': 'testString',
            'name': 'testString',
            'type': 'testString',
            'url': 'testString',
            'description': 'testString',
        }

        state_model = {
            'current': 'testString',
            'current_entered': '2019-01-01T12:00:00.000Z',
            'pending': 'testString',
            'pending_requested': '2019-01-01T12:00:00.000Z',
            'previous': 'testString',
        }

        version_model = {
            'id': 'testString',
            'rev': 'testString',
            'crn': 'testString',
            'version': 'testString',
            'sha': 'testString',
            'created': '2019-01-01T12:00:00.000Z',
            'updated': '2019-01-01T12:00:00.000Z',
            'offering_id': 'testString',
            'catalog_id': 'testString',
            'kind_id': 'testString',
            'tags': ['testString'],
            'repo_url': 'testString',
            'source_url': 'testString',
            'tgz_url': 'testString',
            'configuration': [configuration_model],
            'metadata': {'key1': 'testString'},
            'validation': validation_model,
            'required_resources': [resource_model],
            'single_instance': True,
            'install': script_model,
            'pre_install': [script_model],
            'entitlement': version_entitlement_model,
            'licenses': [license_model],
            'image_manifest_url': 'testString',
            'deprecated': True,
            'package_version': 'testString',
            'state_': state_model,
            'version_locator': 'testString',
            'console_url': 'testString',
            'long_description': 'testString',
            'whitelisted_accounts': ['testString'],
        }

        deployment_model = {
            'id': 'testString',
            'label': 'testString',
            'name': 'testString',
            'short_description': 'testString',
            'long_description': 'testString',
            'metadata': {'key1': 'testString'},
            'tags': ['testString'],
            'created': '2019-01-01T12:00:00.000Z',
            'updated': '2019-01-01T12:00:00.000Z',
        }

        plan_model = {
            'id': 'testString',
            'label': 'testString',
            'name': 'testString',
            'short_description': 'testString',
            'long_description': 'testString',
            'metadata': {'key1': 'testString'},
            'tags': ['testString'],
            'additional_features': [feature_model],
            'created': '2019-01-01T12:00:00.000Z',
            'updated': '2019-01-01T12:00:00.000Z',
            'deployments': [deployment_model],
        }

        kind_model = {
            'id': 'testString',
            'format_kind': 'testString',
            'target_kind': 'testString',
            'metadata': {'key1': 'testString'},
            'install_description': 'testString',
            'tags': ['testString'],
            'additional_features': [feature_model],
            'created': '2019-01-01T12:00:00.000Z',
            'updated': '2019-01-01T12:00:00.000Z',
            'versions': [version_model],
            'plans': [plan_model],
        }

        provider_info_model = {
            'id': 'testString',
            'name': 'testString',
        }

        repo_info_model = {
            'token': 'testString',
            'type': 'testString',
        }

        support_model = {
            'url': 'testString',
            'process': 'testString',
            'locations': ['testString'],
        }

        media_item_model = {
            'url': 'testString',
            'caption': 'testString',
            'type': 'testString',
            'thumbnail_url': 'testString',
        }

        resource = {
            'catalog_identifier': 'testString',
            'id': 'testString',
            'rev': 'testString',
            'url': 'testString',
            'crn': 'testString',
            'label': 'testString',
            'name': 'testString',
            'offering_icon_url': 'testString',
            'offering_docs_url': 'testString',
            'offering_support_url': 'testString',
            'tags': ['testString'],
            'keywords': ['testString'],
            'rating': rating_model,
            'created': '2019-01-01T12:00:00.000Z',
            'updated': '2019-01-01T12:00:00.000Z',
            'short_description': 'testString',
            'long_description': 'testString',
            'features': [feature_model],
            'kinds': [kind_model],
            'pc_managed': True,
            'publish_approved': True,
            'share_with_all': True,
            'share_with_ibm': True,
            'share_enabled': True,
            'permit_request_ibm_public_publish': True,
            'ibm_publish_approved': True,
            'public_publish_approved': True,
            'public_original_crn': 'testString',
            'publish_public_crn': 'testString',
            'portal_approval_record': 'testString',
            'portal_ui_url': 'testString',
            'catalog_id': 'testString',
            'catalog_name': 'testString',
            'metadata': {'key1': 'testString'},
            'disclaimer': 'testString',
            'hidden': True,
            'provider': 'testString',
            'provider_info': provider_info_model,
            'repo_info': repo_info_model,
            'support': support_model,
            'media': [media_item_model],
        }

        patcher = patch(
            'plugins.modules.ibm_cm_offering.CatalogManagementV1.create_offering')
        mock = patcher.start()
        mock.return_value = DetailedResponseMock(resource)

        get_offering_patcher = patch(
            'plugins.modules.ibm_cm_offering.CatalogManagementV1.get_offering')
        get_offering_mock = get_offering_patcher.start()

        set_module_args({
            'catalog_identifier': 'testString',
            'id': 'testString',
            'rev': 'testString',
            'url': 'testString',
            'crn': 'testString',
            'label': 'testString',
            'name': 'testString',
            'offering_icon_url': 'testString',
            'offering_docs_url': 'testString',
            'offering_support_url': 'testString',
            'tags': ['testString'],
            'keywords': ['testString'],
            'rating': rating_model,
            'created': '2019-01-01T12:00:00.000Z',
            'updated': '2019-01-01T12:00:00.000Z',
            'short_description': 'testString',
            'long_description': 'testString',
            'features': [feature_model],
            'kinds': [kind_model],
            'pc_managed': True,
            'publish_approved': True,
            'share_with_all': True,
            'share_with_ibm': True,
            'share_enabled': True,
            'permit_request_ibm_public_publish': True,
            'ibm_publish_approved': True,
            'public_publish_approved': True,
            'public_original_crn': 'testString',
            'publish_public_crn': 'testString',
            'portal_approval_record': 'testString',
            'portal_ui_url': 'testString',
            'catalog_id': 'testString',
            'catalog_name': 'testString',
            'metadata': {'key1': 'testString'},
            'disclaimer': 'testString',
            'hidden': True,
            'provider': 'testString',
            'provider_info': provider_info_model,
            'repo_info': repo_info_model,
            'support': support_model,
            'media': [media_item_model],
        })

        with self.assertRaises(AnsibleExitJson) as result:
            os.environ['CATALOG_MANAGEMENT_AUTH_TYPE'] = 'noAuth'
            os.environ['IC_API_KEY'] = 'noAuthAPIKey'
            ibm_cm_offering.main()

        assert result.exception.args[0]['changed'] is True
        assert result.exception.args[0]['msg'] == resource

        mock_data = dict(
            catalog_identifier='testString',
            id='testString',
            rev='testString',
            url='testString',
            crn='testString',
            label='testString',
            name='testString',
            offering_icon_url='testString',
            offering_docs_url='testString',
            offering_support_url='testString',
            tags=['testString'],
            keywords=['testString'],
            rating=rating_model,
            created='2019-01-01T12:00:00.000Z',
            updated='2019-01-01T12:00:00.000Z',
            short_description='testString',
            long_description='testString',
            features=[feature_model],
            kinds=[kind_model],
            pc_managed=True,
            publish_approved=True,
            share_with_all=True,
            share_with_ibm=True,
            share_enabled=True,
            permit_request_ibm_public_publish=True,
            ibm_publish_approved=True,
            public_publish_approved=True,
            public_original_crn='testString',
            publish_public_crn='testString',
            portal_approval_record='testString',
            portal_ui_url='testString',
            catalog_id='testString',
            catalog_name='testString',
            metadata={'key1': 'testString'},
            disclaimer='testString',
            hidden=True,
            provider='testString',
            provider_info=provider_info_model,
            repo_info=repo_info_model,
            support=support_model,
            media=[media_item_model],
        )

        mock.assert_called_once()
        processed_result = post_process_result(
            mock_data, mock.call_args.kwargs)
        assert mock_data == processed_result

        get_offering_mock.assert_not_called()

        get_offering_patcher.stop()
        patcher.stop()

    def test_create_ibm_cm_offering_failed(self):
        """Test the "create" path - failed."""

        get_offering_patcher = patch(
            'plugins.modules.ibm_cm_offering.CatalogManagementV1.get_offering')
        get_offering_mock = get_offering_patcher.start()

        patcher = patch(
            'plugins.modules.ibm_cm_offering.CatalogManagementV1.create_offering')
        mock = patcher.start()
        mock.side_effect = ApiException(
            400, message='Create ibm_cm_offering error')

        rating_model = {
            'one_star_count': 38,
            'two_star_count': 38,
            'three_star_count': 38,
            'four_star_count': 38,
        }

        feature_model = {
            'title': 'testString',
            'description': 'testString',
        }

        configuration_model = {
            'key': 'testString',
            'type': 'testString',
            'default_value': 'testString',
            'value_constraint': 'testString',
            'description': 'testString',
            'required': True,
            'options': ['testString'],
            'hidden': True,
        }

        validation_model = {
            'validated': '2019-01-01T12:00:00.000Z',
            'requested': '2019-01-01T12:00:00.000Z',
            'state_': 'testString',
            'last_operation': 'testString',
            'target': {'key1': 'testString'},
        }

        resource_model = {
            'type': 'mem',
            # 'value': 'testString',
        }

        script_model = {
            'instructions': 'testString',
            'script': 'testString',
            'script_permission': 'testString',
            'delete_script': 'testString',
            'scope': 'testString',
        }

        version_entitlement_model = {
            'provider_name': 'testString',
            'provider_id': 'testString',
            'product_id': 'testString',
            'part_numbers': ['testString'],
            'image_repo_name': 'testString',
        }

        license_model = {
            'id': 'testString',
            'name': 'testString',
            'type': 'testString',
            'url': 'testString',
            'description': 'testString',
        }

        state_model = {
            'current': 'testString',
            'current_entered': '2019-01-01T12:00:00.000Z',
            'pending': 'testString',
            'pending_requested': '2019-01-01T12:00:00.000Z',
            'previous': 'testString',
        }

        version_model = {
            'id': 'testString',
            'rev': 'testString',
            'crn': 'testString',
            'version': 'testString',
            'sha': 'testString',
            'created': '2019-01-01T12:00:00.000Z',
            'updated': '2019-01-01T12:00:00.000Z',
            'offering_id': 'testString',
            'catalog_id': 'testString',
            'kind_id': 'testString',
            'tags': ['testString'],
            'repo_url': 'testString',
            'source_url': 'testString',
            'tgz_url': 'testString',
            'configuration': [configuration_model],
            'metadata': {'key1': 'testString'},
            'validation': validation_model,
            'required_resources': [resource_model],
            'single_instance': True,
            'install': script_model,
            'pre_install': [script_model],
            'entitlement': version_entitlement_model,
            'licenses': [license_model],
            'image_manifest_url': 'testString',
            'deprecated': True,
            'package_version': 'testString',
            'state_': state_model,
            'version_locator': 'testString',
            'console_url': 'testString',
            'long_description': 'testString',
            'whitelisted_accounts': ['testString'],
        }

        deployment_model = {
            'id': 'testString',
            'label': 'testString',
            'name': 'testString',
            'short_description': 'testString',
            'long_description': 'testString',
            'metadata': {'key1': 'testString'},
            'tags': ['testString'],
            'created': '2019-01-01T12:00:00.000Z',
            'updated': '2019-01-01T12:00:00.000Z',
        }

        plan_model = {
            'id': 'testString',
            'label': 'testString',
            'name': 'testString',
            'short_description': 'testString',
            'long_description': 'testString',
            'metadata': {'key1': 'testString'},
            'tags': ['testString'],
            'additional_features': [feature_model],
            'created': '2019-01-01T12:00:00.000Z',
            'updated': '2019-01-01T12:00:00.000Z',
            'deployments': [deployment_model],
        }

        kind_model = {
            'id': 'testString',
            'format_kind': 'testString',
            'target_kind': 'testString',
            'metadata': {'key1': 'testString'},
            'install_description': 'testString',
            'tags': ['testString'],
            'additional_features': [feature_model],
            'created': '2019-01-01T12:00:00.000Z',
            'updated': '2019-01-01T12:00:00.000Z',
            'versions': [version_model],
            'plans': [plan_model],
        }

        provider_info_model = {
            'id': 'testString',
            'name': 'testString',
        }

        repo_info_model = {
            'token': 'testString',
            'type': 'testString',
        }

        support_model = {
            'url': 'testString',
            'process': 'testString',
            'locations': ['testString'],
        }

        media_item_model = {
            'url': 'testString',
            'caption': 'testString',
            'type': 'testString',
            'thumbnail_url': 'testString',
        }

        set_module_args({
            'catalog_identifier': 'testString',
            'id': 'testString',
            'rev': 'testString',
            'url': 'testString',
            'crn': 'testString',
            'label': 'testString',
            'name': 'testString',
            'offering_icon_url': 'testString',
            'offering_docs_url': 'testString',
            'offering_support_url': 'testString',
            'tags': ['testString'],
            'keywords': ['testString'],
            'rating': rating_model,
            'created': '2019-01-01T12:00:00.000Z',
            'updated': '2019-01-01T12:00:00.000Z',
            'short_description': 'testString',
            'long_description': 'testString',
            'features': [feature_model],
            'kinds': [kind_model],
            'pc_managed': True,
            'publish_approved': True,
            'share_with_all': True,
            'share_with_ibm': True,
            'share_enabled': True,
            'permit_request_ibm_public_publish': True,
            'ibm_publish_approved': True,
            'public_publish_approved': True,
            'public_original_crn': 'testString',
            'publish_public_crn': 'testString',
            'portal_approval_record': 'testString',
            'portal_ui_url': 'testString',
            'catalog_id': 'testString',
            'catalog_name': 'testString',
            'metadata': {'key1': 'testString'},
            'disclaimer': 'testString',
            'hidden': True,
            'provider': 'testString',
            'provider_info': provider_info_model,
            'repo_info': repo_info_model,
            'support': support_model,
            'media': [media_item_model],
        })

        with self.assertRaises(AnsibleFailJson) as result:
            os.environ['CATALOG_MANAGEMENT_AUTH_TYPE'] = 'noAuth'
            os.environ['IC_API_KEY'] = 'noAuthAPIKey'
            ibm_cm_offering.main()

        assert result.exception.args[0]['msg'] == 'Create ibm_cm_offering error'

        mock_data = dict(
            catalog_identifier='testString',
            id='testString',
            rev='testString',
            url='testString',
            crn='testString',
            label='testString',
            name='testString',
            offering_icon_url='testString',
            offering_docs_url='testString',
            offering_support_url='testString',
            tags=['testString'],
            keywords=['testString'],
            rating=rating_model,
            created='2019-01-01T12:00:00.000Z',
            updated='2019-01-01T12:00:00.000Z',
            short_description='testString',
            long_description='testString',
            features=[feature_model],
            kinds=[kind_model],
            pc_managed=True,
            publish_approved=True,
            share_with_all=True,
            share_with_ibm=True,
            share_enabled=True,
            permit_request_ibm_public_publish=True,
            ibm_publish_approved=True,
            public_publish_approved=True,
            public_original_crn='testString',
            publish_public_crn='testString',
            portal_approval_record='testString',
            portal_ui_url='testString',
            catalog_id='testString',
            catalog_name='testString',
            metadata={'key1': 'testString'},
            disclaimer='testString',
            hidden=True,
            provider='testString',
            provider_info=provider_info_model,
            repo_info=repo_info_model,
            support=support_model,
            media=[media_item_model],
        )

        mock.assert_called_once()
        processed_result = post_process_result(
            mock_data, mock.call_args.kwargs)
        assert mock_data == processed_result

        get_offering_mock.assert_not_called()

        get_offering_patcher.stop()
        patcher.stop()

    def test_update_ibm_cm_offering_success(self):
        """Test the "update" path - successful."""
        json_patch_operation_model = {
            'op': 'add',
            'path': 'testString',
            'from_': 'testString',
            # 'value': 'testString',
        }

        resource = {
            'catalog_identifier': 'testString',
            'offering_id': 'testString',
            'if_match': 'testString',
            'updates': [json_patch_operation_model],
        }

        patcher = patch(
            'plugins.modules.ibm_cm_offering.CatalogManagementV1.update_offering')
        mock = patcher.start()
        mock.return_value = DetailedResponseMock(resource)

        get_offering_patcher = patch(
            'plugins.modules.ibm_cm_offering.CatalogManagementV1.get_offering')
        get_offering_mock = get_offering_patcher.start()
        get_offering_mock.return_value = DetailedResponseMock(resource)

        set_module_args({
            'catalog_identifier': 'testString',
            'offering_id': 'testString',
            'if_match': 'testString',
            'updates': [json_patch_operation_model],
        })

        with self.assertRaises(AnsibleExitJson) as result:
            os.environ['CATALOG_MANAGEMENT_AUTH_TYPE'] = 'noAuth'
            os.environ['IC_API_KEY'] = 'noAuthAPIKey'
            ibm_cm_offering.main()

        assert result.exception.args[0]['changed'] is True
        assert result.exception.args[0]['msg'] == resource

        mock_data = dict(
            catalog_identifier='testString',
            offering_id='testString',
            if_match='testString',
            updates=[json_patch_operation_model],
        )

        mock.assert_called_once()
        processed_result = post_process_result(
            mock_data, mock.call_args.kwargs)
        assert mock_data == processed_result

        get_offering_mock_data = dict(
            catalog_identifier='testString',
            offering_id='testString',
            type='testString',
            digest=True,
        )
        # Set the variables that belong to the "read" path to `None`
        # since we test the "delete" path here.
        for param in get_offering_mock_data:
            get_offering_mock_data[param] = mock_data.get(param, None)

        get_offering_mock.assert_called_once()
        get_offering_processed_result = post_process_result(
            get_offering_mock_data, get_offering_mock.call_args.kwargs)
        assert get_offering_mock_data == get_offering_processed_result
        get_offering_patcher.stop()
        patcher.stop()

    def test_update_ibm_cm_offering_failed(self):
        """Test the "update" path - failed."""
        json_patch_operation_model = {
            'op': 'add',
            'path': 'testString',
            'from_': 'testString',
            'value': 'testString',
        }

        resource = {
            'catalog_identifier': 'testString',
            'offering_id': 'testString',
            'if_match': 'testString',
            'updates': [json_patch_operation_model],
        }

        patcher = patch(
            'plugins.modules.ibm_cm_offering.CatalogManagementV1.update_offering')
        mock = patcher.start()
        mock.side_effect = ApiException(
            400, message='Update ibm_cm_offering error')

        get_offering_patcher = patch(
            'plugins.modules.ibm_cm_offering.CatalogManagementV1.get_offering')
        get_offering_mock = get_offering_patcher.start()
        get_offering_mock.return_value = DetailedResponseMock(resource)

        set_module_args({
            'catalog_identifier': 'testString',
            'offering_id': 'testString',
            'if_match': 'testString',
            'updates': [json_patch_operation_model],
        })

        with self.assertRaises(AnsibleFailJson) as result:
            os.environ['CATALOG_MANAGEMENT_AUTH_TYPE'] = 'noAuth'
            os.environ['IC_API_KEY'] = 'noAuthAPIKey'
            ibm_cm_offering.main()

        assert result.exception.args[0]['msg'] == 'Update ibm_cm_offering error'

        mock_data = dict(
            catalog_identifier='testString',
            offering_id='testString',
            if_match='testString',
            updates=[json_patch_operation_model],
        )

        mock.assert_called_once()
        processed_result = post_process_result(
            mock_data, mock.call_args.kwargs)
        assert mock_data == processed_result

        get_offering_mock_data = dict(
            catalog_identifier='testString',
            offering_id='testString',
            type='testString',
            digest=True,
        )
        # Set the variables that belong to the "read" path to `None`
        # since we test the "delete" path here.
        for param in get_offering_mock_data:
            get_offering_mock_data[param] = mock_data.get(param, None)

        get_offering_mock.assert_called_once()
        get_offering_processed_result = post_process_result(
            get_offering_mock_data, get_offering_mock.call_args.kwargs)
        assert get_offering_mock_data == get_offering_processed_result

        get_offering_patcher.stop()
        patcher.stop()

    def test_delete_ibm_cm_offering_success(self):
        """Test the "delete" path - successfull."""
        patcher = patch(
            'plugins.modules.ibm_cm_offering.CatalogManagementV1.delete_offering')
        mock = patcher.start()
        mock.return_value = DetailedResponseMock()

        get_offering_patcher = patch(
            'plugins.modules.ibm_cm_offering.CatalogManagementV1.get_offering')
        get_offering_mock = get_offering_patcher.start()
        get_offering_mock.return_value = DetailedResponseMock()

        args = {
            'catalog_identifier': 'testString',
            'offering_id': 'testString',
            'state': 'absent',
        }

        set_module_args(args)

        with self.assertRaises(AnsibleExitJson) as result:
            os.environ['CATALOG_MANAGEMENT_AUTH_TYPE'] = 'noAuth'
            os.environ['IC_API_KEY'] = 'noAuthAPIKey'
            ibm_cm_offering.main()

        assert result.exception.args[0]['changed'] is True
        assert result.exception.args[0]['msg']['id'] == 'testString'
        assert result.exception.args[0]['msg']['status'] == 'deleted'

        mock_data = dict(
            catalog_identifier='testString',
            offering_id='testString',
        )

        mock.assert_called_once()
        processed_result = post_process_result(
            mock_data, mock.call_args.kwargs)
        assert mock_data == processed_result

        get_offering_mock_data = dict(
            catalog_identifier='testString',
            offering_id='testString',
            type='testString',
            digest=True,
        )
        # Set the variables that belong to the "read" path to `None`
        # since we test the "delete" path here.
        for param in get_offering_mock_data:
            get_offering_mock_data[param] = mock_data.get(param, None)

        get_offering_mock.assert_called_once()
        get_offering_processed_result = post_process_result(
            get_offering_mock_data, get_offering_mock.call_args.kwargs)
        assert get_offering_mock_data == get_offering_processed_result

        get_offering_patcher.stop()
        patcher.stop()

    def test_delete_ibm_cm_offering_not_exists(self):
        """Test the "delete" path - not exists."""
        patcher = patch(
            'plugins.modules.ibm_cm_offering.CatalogManagementV1.delete_offering')
        mock = patcher.start()
        mock.return_value = DetailedResponseMock()

        get_offering_patcher = patch(
            'plugins.modules.ibm_cm_offering.CatalogManagementV1.get_offering')
        get_offering_mock = get_offering_patcher.start()
        get_offering_mock.side_effect = ApiException(404)

        args = {
            'catalog_identifier': 'testString',
            'offering_id': 'testString',
            'state': 'absent',
        }

        set_module_args(args)

        with self.assertRaises(AnsibleExitJson) as result:
            os.environ['CATALOG_MANAGEMENT_AUTH_TYPE'] = 'noAuth'
            os.environ['IC_API_KEY'] = 'noAuthAPIKey'
            ibm_cm_offering.main()

        assert result.exception.args[0]['changed'] is False
        assert result.exception.args[0]['msg']['id'] == 'testString'
        assert result.exception.args[0]['msg']['status'] == 'not_found'

        mock_data = dict(
            catalog_identifier='testString',
            offering_id='testString',
        )

        mock.assert_not_called()

        get_offering_mock_data = dict(
            catalog_identifier='testString',
            offering_id='testString',
            type='testString',
            digest=True,
        )
        # Set the variables that belong to the "read" path to `None`
        # since we test the "delete" path here.
        for param in get_offering_mock_data:
            get_offering_mock_data[param] = mock_data.get(param, None)

        get_offering_mock.assert_called_once()
        get_offering_processed_result = post_process_result(
            get_offering_mock_data, get_offering_mock.call_args.kwargs)
        assert get_offering_mock_data == get_offering_processed_result

        get_offering_patcher.stop()
        patcher.stop()

    def test_delete_ibm_cm_offering_failed(self):
        """Test the "delete" path - failed."""
        patcher = patch(
            'plugins.modules.ibm_cm_offering.CatalogManagementV1.delete_offering')
        mock = patcher.start()
        mock.side_effect = ApiException(
            400, message='Delete ibm_cm_offering error')

        get_offering_patcher = patch(
            'plugins.modules.ibm_cm_offering.CatalogManagementV1.get_offering')
        get_offering_mock = get_offering_patcher.start()
        get_offering_mock.return_value = DetailedResponseMock()

        set_module_args({
            'catalog_identifier': 'testString',
            'offering_id': 'testString',
            'state': 'absent',
        })

        with self.assertRaises(AnsibleFailJson) as result:
            os.environ['CATALOG_MANAGEMENT_AUTH_TYPE'] = 'noAuth'
            os.environ['IC_API_KEY'] = 'noAuthAPIKey'
            ibm_cm_offering.main()

        assert result.exception.args[0]['msg'] == 'Delete ibm_cm_offering error'

        mock_data = dict(
            catalog_identifier='testString',
            offering_id='testString',
        )

        mock.assert_called_once()
        processed_result = post_process_result(
            mock_data, mock.call_args.kwargs)
        assert mock_data == processed_result

        get_offering_mock_data = dict(
            catalog_identifier='testString',
            offering_id='testString',
            type='testString',
            digest=True,
        )
        # Set the variables that belong to the "read" path to `None`
        # since we test the "delete" path here.
        for param in get_offering_mock_data:
            get_offering_mock_data[param] = mock_data.get(param, None)

        get_offering_mock.assert_called_once()
        get_offering_processed_result = post_process_result(
            get_offering_mock_data, get_offering_mock.call_args.kwargs)
        assert get_offering_mock_data == get_offering_processed_result

        get_offering_patcher.stop()
        patcher.stop()
