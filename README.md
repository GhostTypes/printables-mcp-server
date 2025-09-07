# Printables MCP Server 🖨️

A Model Context Protocol (MCP) server for interacting with Printables.com 🌐

## 🎯 Core Features

| Feature | Description |
| :--- | :--- |
| **Model Search** | Search for models with rich metadata. |
| **File Retrieval** | Get all downloadable files associated with a specific model ID. |
| **Description Scraping**| Fetches and formats the detailed description text from a model's main page. |

## 🔎 Model Search

This feature enables users to query the Printables.com database for 3D models.

| Sub-Feature | Description |
| :--- | :--- |
| **Search by Term** | Finds models using a specific query string (e.g., "benchy", "vase"). |
| **Result Limiting** | Controls the maximum number of search results returned in a single query. |
| **Detailed Metadata** | Returns rich information for each model, including ID, name, URL, statistics (ratings, likes, downloads), author, and image URL. |

## 📂 File Retrieval

This feature provides access to the files for a given model.

| Sub-Feature | Description |
| :--- | :--- |
| **Fetch by ID** | Retrieves all associated files by using a model's unique numeric ID. |
| **Detailed File Information** | Provides comprehensive data for each file, including its name, direct download URL, size in bytes, and file type. |

## 📄 Description Retrieval

This feature fetches the description content directly from a model's web page.

| Sub-Feature | Description |
| :--- | :--- |
| **Fetch by URL** | Get the full description from a model's page using its complete URL. |
| **Markdown Formatting** | Returns the extracted description text in markdown format for proper rendering and readability. |

## 🚀 Getting Started

### Prerequisites

  - Python 3.8+
  - pip

### Installation

1.  Clone the repository to your local machine.

    ```bash
    git clone https://github.com/GhostTypes/printables-mcp-server.git
    ```

2.  Navigate to the cloned repository's directory.

    ```bash
    cd printables-mcp-server
    ```

3.  Install the required Python dependencies.

    ```bash
    pip install -r requirements.txt
    ```

4.  Add to your desired MCP client (example for VSCode)

    ```bash
    "printables-mcp": {
			"type": "stdio",
			"command": "python",
			"args": [
				"path/to/printables_mcp_server.py"
			]
		}
    ```
