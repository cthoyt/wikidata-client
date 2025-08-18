"""Test the API."""

import unittest

from wikidata_client.api import get_label


class TestAPI(unittest.TestCase):
    """Test the API."""

    def test_get_label(self) -> None:
        """Test getting a label."""
        self.assertEqual("Douglas Adams", get_label("Q42", language="en"))
