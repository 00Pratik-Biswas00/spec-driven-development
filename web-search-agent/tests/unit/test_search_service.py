import pytest
from unittest.mock import patch
from src.models import SearchQuery, SearchResult
from src.search_service import DuckDuckGoSearchService

@pytest.fixture
def search_service():
    """Fixture to create an instance of DuckDuckGoSearchService."""
    return DuckDuckGoSearchService()

def test_search_success(search_service):
    """
    Test successful search with results.
    """
    mock_ddgs_results = [
        {'title': 'Test Title 1', 'body': 'Test Snippet 1', 'href': 'http://example.com/1'},
        {'title': 'Test Title 2', 'body': 'Test Snippet 2', 'href': 'http://example.com/2'}
    ]

    with patch('src.search_service.DDGS') as mock_ddgs:
        # Configure the context manager
        mock_ddgs_instance = mock_ddgs.return_value
        mock_ddgs_instance.__enter__.return_value.text.return_value = mock_ddgs_results

        query = SearchQuery(text="test query")
        results = search_service.search(query, max_results=2)

        # Assert that text was called on the instance returned by __enter__
        mock_ddgs_instance.__enter__.return_value.text.assert_called_once_with("test query", max_results=2)

        assert len(results) == 2
        assert results[0] == SearchResult(title='Test Title 1', snippet='Test Snippet 1', url='http://example.com/1')
        assert results[1] == SearchResult(title='Test Title 2', snippet='Test Snippet 2', url='http://example.com/2')

def test_search_no_results(search_service):
    """
    Test search with no results.
    """
    with patch('src.search_service.DDGS') as mock_ddgs:
        mock_ddgs_instance = mock_ddgs.return_value
        mock_ddgs_instance.__enter__.return_value.text.return_value = []

        query = SearchQuery(text="no results query")
        results = search_service.search(query)

        mock_ddgs_instance.__enter__.return_value.text.assert_called_once_with("no results query", max_results=10)
        assert len(results) == 0

def test_search_exception(search_service):
    """
    Test search when the DDGS library raises an exception.
    """
    with patch('src.search_service.DDGS') as mock_ddgs:
        mock_ddgs_instance = mock_ddgs.return_value
        mock_ddgs_instance.__enter__.return_value.text.side_effect = Exception("Test Exception")

        query = SearchQuery(text="exception query")
        results = search_service.search(query)

        mock_ddgs_instance.__enter__.return_value.text.assert_called_once_with("exception query", max_results=10)
        assert len(results) == 0

