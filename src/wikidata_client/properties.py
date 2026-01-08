"""Getters for entities by properties."""

from __future__ import annotations

from collections.abc import Collection

from .api import get_entities_by_property, get_entity_by_property
from .constants import TimeoutHint

__all__ = [
    "get_entities_by_orcid",
    "get_entity_by_arxiv",
    "get_entity_by_biorxiv",
    "get_entity_by_github",
    "get_entity_by_orcid",
    "get_entity_by_property",
    "get_entity_by_pubchem_compound",
    "get_entity_by_pubmed",
    "get_entity_by_ror",
]


def get_entity_by_orcid(
    orcid: str, *, timeout: TimeoutHint = None, endpoint: str | None = None
) -> str | None:
    """Get an entity by its ORCiD identifier.

    :param orcid: An ORCiD identifier
    :param timeout: The optional timeout
    :param endpoint: The endpoint, defaults to :data:`WIKIDATA_ENDPOINT`
    :returns: The Wikidata item's QID, if it can be found

    >>> get_entity_by_orcid("0000-0003-4423-4370")
    'Q47475003'
    """
    return get_entity_by_property("P496", orcid, timeout=timeout, endpoint=endpoint)


def get_entities_by_orcid(
    orcids: Collection[str], *, timeout: TimeoutHint = None, endpoint: str | None = None
) -> str | None:
    """Get an entity by its ORCiD identifier.

    :param orcids: A collection ORCiD identifies
    :param timeout: The optional timeout
    :param endpoint: The endpoint, defaults to :data:`WIKIDATA_ENDPOINT`
    :returns: The Wikidata item's QID, if it can be found

    >>> get_entities_by_orcid(["0000-0003-4423-4370"])
    {'0000-0003-4423-4370': 'Q47475003'}
    """
    return get_entities_by_property("P496", orcid, timeout=timeout, endpoint=endpoint)


def get_entity_by_github(
    github: str, *, timeout: TimeoutHint = None, endpoint: str | None = None
) -> str | None:
    """Get an entity by its GitHub username.

    :param github: A GitHub identifier
    :param timeout: The optional timeout
    :param endpoint: The endpoint, defaults to :data:`WIKIDATA_ENDPOINT`
    :returns: The Wikidata item's QID, if it can be found

    >>> get_entity_by_github("cthoyt")
    'Q47475003'
    """
    return get_entity_by_property("P2037", github, timeout=timeout, endpoint=endpoint)


def get_entity_by_pubchem_compound(
    pubchem_compound_id: str, *, timeout: TimeoutHint = None, endpoint: str | None = None
) -> str | None:
    """Get an entity by its PubChem compound identifier.

    :param pubchem_compound_id: A PubChem Compound identifier
    :param timeout: The optional timeout
    :param endpoint: The endpoint, defaults to :data:`WIKIDATA_ENDPOINT`
    :returns: The Wikidata item's QID, if it can be found

    >>> get_entity_by_pubchem_compound("14123361")
    'Q289372'
    """
    return get_entity_by_property("P662", pubchem_compound_id, timeout=timeout, endpoint=endpoint)


def get_entity_by_arxiv(
    arxiv_id: str, *, timeout: TimeoutHint = None, endpoint: str | None = None
) -> str | None:
    """Get an entity by its arXiv identifier.

    :param arxiv_id: An arXiv identifier
    :param timeout: The optional timeout
    :param endpoint: The endpoint, defaults to :data:`WIKIDATA_ENDPOINT`
    :returns: The Wikidata item's QID, if it can be found

    >>> get_entity_by_arxiv("1507.04180")
    'Q27036443'
    """
    return get_entity_by_property("P818", arxiv_id, timeout=timeout, endpoint=endpoint)


def get_entity_by_biorxiv(
    biorxiv_id: str, *, timeout: TimeoutHint = None, endpoint: str | None = None
) -> str | None:
    """Get an entity by its bioRxiv identifier.

    :param biorxiv_id: An bioRxiv identifier
    :param timeout: The optional timeout
    :param endpoint: The endpoint, defaults to :data:`WIKIDATA_ENDPOINT`
    :returns: The Wikidata item's QID, if it can be found

    >>> get_entity_by_biorxiv("2020.08.20.259226")
    'Q104920313'
    """
    return get_entity_by_property("P3951", biorxiv_id, timeout=timeout, endpoint=endpoint)


def get_entity_by_pubmed(
    pubmed: str, *, timeout: TimeoutHint = None, endpoint: str | None = None
) -> str | None:
    """Get an entity by its PubMed identifier.

    :param pubmed: An PubMed identifier
    :param timeout: The optional timeout
    :param endpoint: The endpoint, defaults to :data:`WIKIDATA_ENDPOINT`
    :returns: The Wikidata item's QID, if it can be found

    >>> get_entity_by_pubmed("29029422")
    'Q42371516'
    """
    return get_entity_by_property("P698", pubmed, timeout=timeout, endpoint=endpoint)


def get_entity_by_ror(
    ror: str, *, timeout: TimeoutHint = None, endpoint: str | None = None
) -> str | None:
    """Get an entity by its PubMed identifier.

    :param ror: An ROR identifier
    :param timeout: The optional timeout
    :param endpoint: The endpoint, defaults to :data:`WIKIDATA_ENDPOINT`
    :returns: The Wikidata item's QID, if it can be found

    >>> get_entity_by_ror("038321296")
    'Q5566337'
    """
    return get_entity_by_property("P6782", ror, timeout=timeout, endpoint=endpoint)
