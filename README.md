<div align="center">
  <h1>Printables MCP Server</h1>
  <p>A Model Context Protocol (MCP) server for interacting with Printables.com</p>
</div>

<p align="center">
  <img src="https://img.shields.io/badge/Python-3.8+-blue?style=for-the-badge&logo=python&logoColor=white">
  <img src="https://img.shields.io/github/stars/GhostTypes/printables-mcp-server?style=for-the-badge">
  <img src="https://img.shields.io/github/forks/GhostTypes/printables-mcp-server?style=for-the-badge">
</p>

---

<div align="center">
  <h2>Core Features</h2>
</div>

<div align="center">
<table>
  <tr>
    <th>Feature</th>
    <th>Description</th>
  </tr>
  <tr>
    <td><strong>Model Search</strong></td>
    <td>Search for models with rich metadata.</td>
  </tr>
  <tr>
    <td><strong>File Retrieval</strong></td>
    <td>Get all downloadable files associated with a specific model ID.</td>
  </tr>
  <tr>
    <td><strong>Description Scraping</strong></td>
    <td>Fetches and formats the detailed description text from a model's main page.</td>
  </tr>
</table>
</div>

---

<div align="center">
  <h2>Model Search</h2>
</div>

This feature enables users to query the Printables.com database for 3D models.

<div align="center">
<table>
  <tr>
    <th>Sub-Feature</th>
    <th>Description</th>
  </tr>
  <tr>
    <td><strong>Search by Term</strong></td>
    <td>Finds models using a specific query string (e.g., "benchy", "vase").</td>
  </tr>
  <tr>
    <td><strong>Result Limiting</strong></td>
    <td>Controls the maximum number of search results returned in a single query.</td>
  </tr>
  <tr>
    <td><strong>Detailed Metadata</strong></td>
    <td>Returns rich information for each model, including ID, name, URL, statistics (ratings, likes, downloads), author, and image URL.</td>
  </tr>
</table>
</div>

---

<div align="center">
  <h2>File Retrieval</h2>
</div>

This feature provides access to the files for a given model.

<div align="center">
<table>
  <tr>
    <th>Sub-Feature</th>
    <th>Description</th>
  </tr>
  <tr>
    <td><strong>Fetch by ID</strong></td>
    <td>Retrieves all associated files by using a model's unique numeric ID.</td>
  </tr>
  <tr>
    <td><strong>Detailed File Information</strong></td>
    <td>Provides comprehensive data for each file, including its name, direct download URL, size in bytes, and file type.</td>
  </tr>
</table>
</div>

---

<div align="center">
  <h2>Description Retrieval</h2>
</div>

This feature fetches the description content directly from a model's web page.

<div align="center">
<table>
  <tr>
    <th>Sub-Feature</th>
    <th>Description</th>
  </tr>
  <tr>
    <td><strong>Fetch by URL</strong></td>
    <td>Get the full description from a model's page using its complete URL.</td>
  </tr>
  <tr>
    <td><strong>Markdown Formatting</strong></td>
    <td>Returns the extracted description text in markdown format for proper rendering and readability.</td>
  </tr>
</table>
</div>

---

<div align="center">
  <h2>Getting Started</h2>
</div>

### Prerequisites

  - Python 3.8+
  - pip

---

<div align="center">
  <h2>Installation</h2>
</div>

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
