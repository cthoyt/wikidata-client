"""Utilities for Wikibase."""

from __future__ import annotations

from collections import defaultdict
from collections.abc import Collection, Mapping
from textwrap import dedent
from typing import Any, Literal, cast, overload

import requests

from .constants import (
    USER_AGENT_NAME,
    WIKIDATA_ENDPOINT,
    WIKIDATA_ITEM_REGEX,
    WIKIDATA_PROP_REGEX,
    TimeoutHint,
)
from .version import get_version

__all__ = [
    "get_entities_by_property",
    "get_entity_by_property",
    "get_image",
    "get_label",
    "get_orcid",
    "get_properties",
    "get_property",
    "query",
]

USER_AGENT = f"{USER_AGENT_NAME} v{get_version()}"
HEADERS = {
    "User-Agent": USER_AGENT,
}


def query(
    sparql: str, *, timeout: TimeoutHint = None, endpoint: str | None = None
) -> list[Mapping[str, Any]]:
    """Query Wikidata's SPARQL service.

    :param sparql: A SPARQL query string
    :param timeout: Number of seconds before timeout. Defaults to 10 seconds.
    :param endpoint: The SPARQL service base URL.
    :return: A list of bindings
    """
    if timeout is None:
        timeout = 10
    res = requests.get(
        endpoint or WIKIDATA_ENDPOINT,
        params={"query": sparql, "format": "json"},
        headers=HEADERS,
        timeout=timeout,
    )
    res.raise_for_status()
    res_json = res.json()
    return [
        {key: _clean_value(value["value"]) for key, value in record.items()}
        for record in res_json["results"]["bindings"]
    ]


def _clean_value(value: str) -> str:
    value = value.removeprefix("http://www.wikidata.org/entity/")
    return value


def get_entity_by_property(
    prop: str, value: str, *, timeout: TimeoutHint = None, endpoint: str | None = None
) -> str | None:
    """Get the Wikidata item's QID based on the given property and value.

    :param prop:
        The Wikidata property, starting with P. For example, ``P496``
        is the ORCiD identifier property
    :param value:
        The value with the property. For example, ``0000-0003-4423-4370``
        is the ORCiD identifier for ``Q47475003``
    :param timeout: The optional timeout
    :param endpoint: The endpoint, defaults to :data:`WIKIDATA_ENDPOINT`
    :returns: The Wikidata item's QID, if it can be found

    >>> get_entity_by_property("P496", "0000-0003-4423-4370")
    'Q47475003'
    """
    if not WIKIDATA_PROP_REGEX.match(prop):
        raise ValueError(f"Wikidata property '{prop}' is not valid.")

    sparql = f'SELECT ?item WHERE {{ ?item wdt:{prop} "{value}" . }} LIMIT 1'
    records = query(sparql, timeout=timeout, endpoint=endpoint)
    if not records:
        return None
    return cast(str, records[0]["item"])


def get_entities_by_property(
    prop: str, values: str, *, timeout: TimeoutHint = None, endpoint: str | None = None
) -> str | None:
    """Get the Wikidata item's QID based on the given property and value.

    :param prop:
        The Wikidata property, starting with P. For example, ``P496``
        is the ORCiD identifier property
    :param value:
        The value with the property. For example, ``0000-0003-4423-4370``
        is the ORCiD identifier for ``Q47475003``
    :param timeout: The optional timeout
    :param endpoint: The endpoint, defaults to :data:`WIKIDATA_ENDPOINT`
    :returns: The Wikidata item's QID, if it can be found

    >>> get_entity_by_property("P496", "0000-0003-4423-4370")
    'Q47475003'
    """
    if not WIKIDATA_PROP_REGEX.match(prop):
        raise ValueError(f"Wikidata property '{prop}' is not valid.")

    sparql = f'SELECT ?item WHERE {{ ?item wdt:{prop} "{value}" . }} LIMIT 1'
    records = query(sparql, timeout=timeout, endpoint=endpoint)
    if not records:
        return None
    return cast(str, records[0]["item"])


def get_image(item: str, *, timeout: TimeoutHint = None, endpoint: str | None = None) -> str | None:
    """Get a URL for an image for the Wikibase item, if it exists.

    :param item: The Wikidata identifier
    :param timeout: The number of seconds before timeout. Defaults to 10 seconds.
    :param endpoint: The SPARQL service base URL. Defaults to Wikidata's.
    :return:
        The URL for an image for the item, if it exists. If multiple images exist,
        arbitrarily return the first.
    :raises ValueError: If the item does not match the Wikidata item regular expression.

    >>> get_image("Q47475003")
    'http://commons.wikimedia.org/wiki/Special:FilePath/Charles%20Tapley%20Hoyt%202019.jpg'

    >>> assert get_image("Q109302693") is None
    """
    if not WIKIDATA_ITEM_REGEX.match(item):
        raise ValueError(f"Wikidata item '{item}' is not valid under {WIKIDATA_ITEM_REGEX}.")

    sparql = dedent(f"""\
        SELECT ?imageLabel WHERE {{
          wd:{item} wdt:P18 ?image.
          SERVICE wikibase:label {{ bd:serviceParam wikibase:language "[AUTO_LANGUAGE],en". }}
        }}
        LIMIT 1
    """)
    records = query(sparql, timeout=timeout, endpoint=endpoint)
    if not records:
        return None
    return cast(str, records[0]["imageLabel"])


def get_label(
    item: str, *, timeout: TimeoutHint = None, endpoint: str | None = None, language: str = "en"
) -> str | None:
    """Get the label."""
    if not WIKIDATA_ITEM_REGEX.match(item):
        raise ValueError(f"Wikidata item '{item}' is not valid under {WIKIDATA_ITEM_REGEX}.")

    sparql = dedent(f"""\
        SELECT ?label WHERE {{
          wd:{item} rdfs:label ?label .
          FILTER(lang(?label) = '{language}')
        }}
        LIMIT 1
    """)
    records = query(sparql, timeout=timeout, endpoint=endpoint)
    if not records:
        return None
    return cast(str, records[0]["label"])


def get_orcid(item: str, *, timeout: TimeoutHint = None, endpoint: str | None = None) -> str | None:
    """Get the ORCID."""
    return get_property(
        item,
        "P496",
        timeout=timeout,
        endpoint=endpoint,
    )


def get_property(
    item: str, prop: str, *, timeout: TimeoutHint = None, endpoint: str | None = None
) -> str | None:
    """Get the value for the property."""
    if not WIKIDATA_ITEM_REGEX.match(item):
        raise ValueError(f"Wikidata item '{item}' is not valid under {WIKIDATA_ITEM_REGEX}.")

    sparql = dedent(f"""\
        SELECT ?value WHERE {{
          wd:{item} wdt:{prop} ?value .
        }}
        LIMIT 1
    """)
    records = query(sparql, timeout=timeout, endpoint=endpoint)
    if not records:
        return None
    return cast(str, records[0]["value"])


@overload
def get_properties(
    items: Collection[str],
    prop: str,
    *,
    timeout: TimeoutHint = None,
    endpoint: str | None = ...,
    single_value: Literal[True] = ...,
) -> dict[str, str]: ...


@overload
def get_properties(
    items: Collection[str],
    prop: str,
    *,
    timeout: TimeoutHint = None,
    endpoint: str | None = ...,
    single_value: Literal[False] = ...,
) -> dict[str, set[str]]: ...


def get_properties(
    items: Collection[str],
    prop: str,
    *,
    timeout: TimeoutHint = None,
    endpoint: str | None = None,
    single_value: bool = True,
) -> dict[str, str] | dict[str, set[str]]:
    """Get the value for the property for multime entities."""
    if not WIKIDATA_PROP_REGEX.match(prop):
        raise ValueError(f"Wikidata property '{prop}' is not valid.")

    sparql = dedent(f"""\
        SELECT ?s ?o WHERE {{
            VALUES ?s {{ {_values_for_sparql(items)} }}
            ?s wdt:{prop} ?o .
        }}
    """)
    records = query(sparql, timeout=timeout, endpoint=endpoint)

    if single_value:
        return {record["s"]: record["o"] for record in records}
    else:
        rv: defaultdict[str, set[str]] = defaultdict(set)
        for record in records:
            rv[record["s"]].add(record["o"])
        return dict(rv)


def _values_for_sparql(wikidata_ids: Collection[str]) -> str:
    return " ".join("wd:" + x for x in sorted(wikidata_ids))
