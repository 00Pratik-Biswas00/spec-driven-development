# Quickstart: Web Search Agent

This guide will help you set up and run the Web Search Agent application.

## Prerequisites

- Python 3.x installed on your system.
- `pip` (Python package installer) installed.

## Setup Instructions

1.  **Clone the repository (if you haven't already):**
    ```bash
    git clone [REPOSITORY_URL]
    cd web-search-agent
    ```
    (Replace `[REPOSITORY_URL]` with the actual repository URL)

2.  **Create a virtual environment (recommended):**
    ```bash
    python -m venv venv
    ```

3.  **Activate the virtual environment:**
    -   **On Windows:**
        ```bash
        .\venv\Scripts\activate
        ```
    -   **On macOS/Linux:**
        ```bash
        source venv/bin/activate
        ```

4.  **Install dependencies:**
    ```bash
    pip install streamlit requests
    ```

## Running the Application

1.  **Navigate to the project directory:**
    ```bash
    cd [YOUR_PROJECT_DIRECTORY]
    ```
    (Ensure your virtual environment is active)

2.  **Run the Streamlit application:**
    ```bash
    streamlit run src/app.py
    ```

3.  **Access the application:**
    Open your web browser and go to the URL displayed in your terminal (usually `http://localhost:8501`).

## Using the Application

-   Enter your search query in the provided input field.
-   Click the "Search" button or press Enter.
-   View the search results displayed on the page.
-   Click on any result's title or URL to navigate to the respective web page.
