from __future__ import (absolute_import, division, print_function)
__metaclass__ = type

import os
from ibm_cloud_sdk_core import get_authenticator_from_environment
from ibm_cloud_sdk_core.authenticators import Authenticator, IAMAuthenticator
from ibm_platform_services import CatalogManagementV1, ResourceControllerV2, ResourceManagerV2, IamAccessGroupsV2, IamIdentityV1, GlobalCatalogV1
from ibm_schematics import SchematicsV1


def get_authenticator() -> Authenticator:
    apikey = os.getenv('IC_API_KEY')
    if apikey is None:
        raise ValueError(
            "[ERROR] Please export IC_API_KEY. Value for APIKey is None")
    authenticator = IAMAuthenticator(apikey=apikey)
    return authenticator


def get_catalog_management_sdk():
    return CatalogManagementV1(
        authenticator=get_authenticator(),
    )


def get_resource_contollerV2_sdk():
    return ResourceControllerV2(
        authenticator=get_authenticator(),
    )


def get_resource_manager_sdk():
    return ResourceManagerV2(
        authenticator=get_authenticator(),
    )


def get_iam_access_group_sdk():
    return IamAccessGroupsV2(
        authenticator=get_authenticator(),
    )


def get_iam_identity_sdk():
    return IamIdentityV1(
        authenticator=get_authenticator(),
    )


def get_schematicsv1_sdk():
    return SchematicsV1(
        authenticator=get_authenticator(),
    )


def get_global_catalog_sdk():
    return GlobalCatalogV1(
        authenticator=get_authenticator(),
    )
