"""Interact with Wikidata programmatically."""

from .api import (
    get_entities_by_property,
    get_entity_by_property,
    get_image,
    get_label,
    get_orcid,
    get_orcids,
    get_properties,
    get_property,
    query,
)
from .properties import (
    get_entities_by_orcid,
    get_entity_by_arxiv,
    get_entity_by_biorxiv,
    get_entity_by_github,
    get_entity_by_orcid,
    get_entity_by_pubchem_compound,
    get_entity_by_pubmed,
    get_entity_by_ror,
)

__all__ = [
    "get_entities_by_orcid",
    "get_entities_by_property",
    "get_entity_by_arxiv",
    "get_entity_by_biorxiv",
    "get_entity_by_github",
    "get_entity_by_orcid",
    "get_entity_by_property",
    "get_entity_by_pubchem_compound",
    "get_entity_by_pubmed",
    "get_entity_by_ror",
    "get_image",
    "get_label",
    "get_orcid",
    "get_orcids",
    "get_properties",
    "get_property",
    "query",
]
