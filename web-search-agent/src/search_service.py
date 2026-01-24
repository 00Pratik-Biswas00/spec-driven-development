from ddgs import DDGS
from typing import List
from models import SearchQuery, SearchResult
import logging

logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

class DuckDuckGoSearchService:
    """
    Service for integrating with the DuckDuckGo Search API using the duckduckgo-search library.
    """

    def search(self, query: SearchQuery, max_results: int = 10) -> List[SearchResult]:
        """
        Executes a search query using the duckduckgo-search library and returns a list of SearchResult objects.
        """
        results: List[SearchResult] = []
        try:
            with DDGS() as ddgs:
                ddgs_results = ddgs.text(query.text, max_results=max_results)
                if ddgs_results:
                    for r in ddgs_results:
                        results.append(SearchResult(
                            title=r.get('title', 'No Title'),
                            snippet=r.get('body', 'No Snippet'),
                            url=r.get('href', '')
                        ))
        except Exception as e:
            logging.error(f"Error during DuckDuckGo search: {e}")
        return results

