import pytest
from src.models import SearchQuery, SearchResult

def test_search_query_creation():
    query_text = "test search"
    query = SearchQuery(text=query_text)
    assert query.text == query_text

def test_search_query_repr():
    query = SearchQuery(text="another test")
    assert repr(query) == "SearchQuery(text='another test')"

def test_search_result_creation():
    title = "Test Title"
    snippet = "This is a test snippet."
    url = "http://example.com"
    result = SearchResult(title=title, snippet=snippet, url=url)
    assert result.title == title
    assert result.snippet == snippet
    assert result.url == url

def test_search_result_repr():
    result = SearchResult(title="Title", snippet="Snippet", url="http://url.com")
    assert repr(result) == "SearchResult(title='Title', snippet='Snippet', url='http://url.com')"

def test_search_result_equality():
    result1 = SearchResult(title="Title1", snippet="Snippet1", url="http://url1.com")
    result2 = SearchResult(title="Title1", snippet="Snippet1", url="http://url1.com")
    result3 = SearchResult(title="Title2", snippet="Snippet2", url="http://url2.com")
    assert result1 == result2
    assert result1 != result3
