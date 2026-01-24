import streamlit as st
from models import SearchQuery
from search_service import DuckDuckGoSearchService, SearchResult
import logging

# Configure logging for the app
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

st.set_page_config(page_title="Web Search Agent", page_icon="🔍")

def display_search_results(results: list[SearchResult]):
    """Displays the list of search results in Streamlit."""
    if not results:
        st.info("No results found for your query.")
        return

    for i, result in enumerate(results):
        st.markdown(f"**[{result.title}]({result.url})**")
        st.write(result.snippet)
        st.markdown(f"<sub>{result.url}</sub>")
        if i < len(results) - 1:
            st.divider()

def main():
    st.title("🔍 Web Search Agent")
    st.markdown("Enter a search query below to find relevant information using the DuckDuckGo API.")

    search_query_text = st.text_input("Enter your search query:", placeholder="e.g., Gemini CLI features")

    if st.button("Search", type="primary"):
        if search_query_text:
            search_service = DuckDuckGoSearchService()
            query = SearchQuery(text=search_query_text)

            with st.spinner(f"Searching for '{search_query_text}'..."):
                try:
                    results = search_service.search(query)
                    display_search_results(results)
                except Exception as e:
                    logging.error(f"An unexpected error occurred during search: {e}")
                    st.error("An error occurred while performing the search. Please try again.")
        else:
            st.warning("Please enter a search query.")

if __name__ == "__main__":
    main()
