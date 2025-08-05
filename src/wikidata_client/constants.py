"""Constants for Wikidata client."""

import re
from typing import TypeAlias

__all__ = [
    "USER_AGENT_NAME",
    "WIKIDATA_ENDPOINT",
    "WIKIDATA_ITEM_REGEX",
    "WIKIDATA_PROP_REGEX",
    "TimeoutHint",
]

#: The user agent name for this package
USER_AGENT_NAME = "python-wikidata-client"

#: #: A type hint for the timeout in :func:`requests.get`
TimeoutHint: TypeAlias = None | int | float | tuple[float | int, float | int]

WIKIDATA_ITEM_REGEX = re.compile(r"^Q[1-9]\d+$")
WIKIDATA_PROP_REGEX = re.compile(r"^P[1-9]\d+$")

#: Wikidata SPARQL endpoint. See https://www.wikidata.org/wiki/Wikidata:SPARQL_query_service#Interfacing
WIKIDATA_ENDPOINT = "https://query.wikidata.org/bigdata/namespace/wdq/sparql"
