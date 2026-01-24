# Data Model: Web Search Agent

## Entities

### Search Query
- **Description**: The text string entered by the user to initiate a search.
- **Attributes**:
    - `text`: String, required. The actual search terms.

### Search Result
- **Description**: A single item returned by the search, comprising a title, a short descriptive snippet, and a URL.
- **Attributes**:
    - `title`: String, required. The title of the search result.
    - `snippet`: String, required. A brief description or excerpt from the search result.
    - `url`: String, required. The URL of the web page.
