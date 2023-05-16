# -*- coding: utf-8 -*-
# (C) Copyright IBM Corp. .
#
# GNU General Public License v3.0+ (see LICENSE or https://www.gnu.org/licenses/gpl-3.0.txt)

from __future__ import (absolute_import, division, print_function)
__metaclass__ = type

import os

try:
    from ibm_cloud_sdk_core import get_authenticator_from_environment
    from ibm_cloud_sdk_core.authenticators import Authenticator, IAMAuthenticator
    from ibm_platform_services import ResourceControllerV2
except ImportError:
    raise


RESOURCE_CONTROLLER_SERVICE_NAME = 'resource_controller'


def get_authenticator(service_name: str) -> Authenticator:
    """Create and return an authenticator instance.

    1. Try to create an authenticator based on the service name and the environment variables
    2. If that wasn't successful try to get the `IC_API_KEY` from the environment and create an IAM authenticator
    3. If all the above have failed, return None.

    Args:
        service_name (str): name of the service

    Returns:
        Authenticator: the created authenticator or None
    """
    authenticator = get_authenticator_from_environment(service_name=service_name)
    if authenticator is None:
        apikey = os.getenv('IC_API_KEY', None)
        if apikey is None:
            return None

        authenticator = IAMAuthenticator(apikey=apikey)

    return authenticator


def get_service_url(resource_id: str, fallback_authenticator: Authenticator) -> str:
    """Fetch and return the service URL for the resource instance on the given resource ID.

    1. Try to authenticate with Resource Controller credentials
    2. If can't, try to use the authenticator from the default service.

    Args:
        resource_id (str): ID of the resource that holds the URL
        fallback_authenticator (Authenticator): the authenticator from the original service

    Raises:
        Exception: something went wrong during retrieving the resource instance

    Returns:
        str: the retrieved service URL for the resource or None
    """

    authenticator = get_authenticator(ResourceControllerV2.DEFAULT_SERVICE_NAME)
    if authenticator is not None:
        resource_controller = ResourceControllerV2(authenticator)
    else:
        resource_controller = ResourceControllerV2(fallback_authenticator)

    resource_controller.configure_service(RESOURCE_CONTROLLER_SERVICE_NAME)
    resource = resource_controller.get_resource_instance(resource_id).get_result()

    return resource.get('extensions', {}).get('endpoints', {}).get('public')
