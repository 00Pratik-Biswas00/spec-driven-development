import pytest
from unittest.mock import patch, Mock
import streamlit as st
from src.app import main, display_search_results
from src.models import SearchResult

# Mock the DuckDuckGoSearchService for integration tests
@pytest.fixture
def mock_search_service():
    with patch('src.app.DuckDuckGoSearchService') as MockService:
        instance = MockService.return_value
        yield instance

# Test display_search_results function
def test_display_search_results_empty():
    with patch.object(st, 'info') as mock_st_info:
        display_search_results([])
        mock_st_info.assert_called_once_with("No results found for your query.")

def test_display_search_results_with_data():
    results = [
        SearchResult(title="Test 1", snippet="Snippet 1", url="http://test1.com"),
        SearchResult(title="Test 2", snippet="Snippet 2", url="http://test2.com"),
    ]
    with patch.object(st, 'markdown') as mock_st_markdown, \
         patch.object(st, 'write') as mock_st_write, \
         patch.object(st, 'divider') as mock_st_divider:
        
        display_search_results(results)
        
        assert mock_st_markdown.call_count == 4 # 2 titles + 2 urls
        mock_st_markdown.assert_any_call(f"**[{results[0].title}]({results[0].url})**")
        mock_st_markdown.assert_any_call(f"<sub>{results[0].url}</sub>")
        mock_st_markdown.assert_any_call(f"**[{results[1].title}]({results[1].url})**")
        mock_st_markdown.assert_any_call(f"<sub>{results[1].url}</sub>")
        
        assert mock_st_write.call_count == 2
        mock_st_write.assert_any_call(results[0].snippet)
        mock_st_write.assert_any_call(results[1].snippet)
        
        mock_st_divider.assert_called_once() # Only one divider for two results

# Test the main application flow (requires mocking streamlit inputs)
def test_main_search_success(mock_search_service):
    # Mock the search service to return some results
    mock_search_service.search.return_value = [
        SearchResult(title="Mock Title", snippet="Mock Snippet", url="http://mock.com")
    ]

    # Mock Streamlit input widgets
    with patch.object(st, 'text_input', return_value="test query"), \
         patch.object(st, 'button', return_value=True), \
         patch.object(st, 'spinner'): # Context manager mock for spinner
        
        # Mock display_search_results to check if it's called
        with patch('src.app.display_search_results') as mock_display:
            main()
            mock_search_service.search.assert_called_once()
            mock_display.assert_called_once()
            args, kwargs = mock_display.call_args
            assert len(args[0]) == 1 # Expecting one result
            assert args[0][0].title == "Mock Title"

def test_main_empty_query():
    with patch.object(st, 'text_input', return_value=""), \
         patch.object(st, 'button', return_value=True), \
         patch.object(st, 'warning') as mock_st_warning:
        main()
        mock_st_warning.assert_called_once_with("Please enter a search query.")

def test_main_search_error(mock_search_service):
    mock_search_service.search.side_effect = Exception("API Error")
    with patch.object(st, 'text_input', return_value="error query"), \
         patch.object(st, 'button', return_value=True), \
         patch.object(st, 'spinner'), \
         patch.object(st, 'error') as mock_st_error:
        main()
        mock_search_service.search.assert_called_once()
        mock_st_error.assert_called_once_with("An error occurred while performing the search. Please try again.")
