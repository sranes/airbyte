#
# Copyright (c) 2021 Airbyte, Inc., all rights reserved.
#

"""
    Airbyte Configuration API

    Airbyte Configuration API [https://airbyte.io](https://airbyte.io).  This API is a collection of HTTP RPC-style methods. While it is not a REST API, those familiar with REST should find the conventions of this API recognizable.  Here are some conventions that this API follows: * All endpoints are http POST methods. * All endpoints accept data via `application/json` request bodies. The API does not accept any data via query params. * The naming convention for endpoints is: localhost:8000/{VERSION}/{METHOD_FAMILY}/{METHOD_NAME} e.g. `localhost:8000/v1/connections/create`. * For all `update` methods, the whole object must be passed in, even the fields that did not change.  Change Management: * The major version of the API endpoint can be determined / specified in the URL `localhost:8080/v1/connections/create` * Minor version bumps will be invisible to the end user. The user cannot specify minor versions in requests. * All backwards incompatible changes will happen in major version bumps. We will not make backwards incompatible changes in minor version bumps. Examples of non-breaking changes (includes but not limited to...):   * Adding fields to request or response bodies.   * Adding new HTTP endpoints.   # noqa: E501

    The version of the OpenAPI document: 1.0.0
    Contact: contact@airbyte.io
    Generated by: https://openapi-generator.tech
"""


import unittest

import airbyte_api_client
from airbyte_api_client.api.operation_api import OperationApi  # noqa: E501


class TestOperationApi(unittest.TestCase):
    """OperationApi unit test stubs"""

    def setUp(self):
        self.api = OperationApi()  # noqa: E501

    def tearDown(self):
        pass

    def test_check_operation(self):
        """Test case for check_operation

        Check if an operation to be created is valid  # noqa: E501
        """
        pass

    def test_create_operation(self):
        """Test case for create_operation

        Create an operation to be applied as part of a connection pipeline  # noqa: E501
        """
        pass

    def test_delete_operation(self):
        """Test case for delete_operation

        Delete an operation  # noqa: E501
        """
        pass

    def test_get_operation(self):
        """Test case for get_operation

        Returns an operation  # noqa: E501
        """
        pass

    def test_list_operations_for_connection(self):
        """Test case for list_operations_for_connection

        Returns all operations for a connection.  # noqa: E501
        """
        pass

    def test_update_operation(self):
        """Test case for update_operation

        Update an operation  # noqa: E501
        """
        pass


if __name__ == "__main__":
    unittest.main()
