"""Interact with Wikidata programmatically."""

from .api import get_entity_by_property, get_image, query

__all__ = [
    "get_entity_by_property",
    "get_image",
    "query",
]
