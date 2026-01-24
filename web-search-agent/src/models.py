from dataclasses import dataclass

@dataclass
class SearchQuery:
    """
    Represents a user's search query.
    """
    text: str

@dataclass
class SearchResult:
    """
    Represents a single item returned by the search.
    """
    title: str
    snippet: str
    url: str
