# (C) Copyright IBM Corp. 2022.
# GNU General Public License v3.0+ (see LICENSE or https://www.gnu.org/licenses/gpl-3.0.txt)

from __future__ import (absolute_import, division, print_function)
__metaclass__ = type


class DetailedResponseMock:
    """Mock class for the DetailedResponse object."""

    def __init__(self, result=None):
        self.result = result

    def get_result(self):
        """Returns the set value."""
        return self.result
