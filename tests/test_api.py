"""Test the API."""

import unittest

from wikidata_client import get_entity_by_github, get_entity_by_orcid, get_label, get_orcid


class TestAPI(unittest.TestCase):
    """Test the API."""

    def test_get_label(self) -> None:
        """Test getting a label."""
        self.assertEqual("Douglas Adams", get_label("Q42", language="en"))

    def test_orcid(self) -> None:
        """Test getting a ORCiD."""
        self.assertEqual("0000-0003-4423-4370", get_orcid("Q47475003"))
        self.assertEqual("Q47475003", get_entity_by_orcid("0000-0003-4423-4370"))

    def test_github(self) -> None:
        """Test GitHub."""
        self.assertEqual("Q47475003", get_entity_by_github("cthoyt"))
