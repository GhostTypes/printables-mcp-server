import sys
import os
import logging
from typing import List, Dict, Any, Optional

# Add parent directory to path to import printables_api
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from mcp.server.fastmcp import FastMCP
import printables_api

# Configure logging to stderr (NEVER use stdout as it will corrupt MCP JSON-RPC messages)
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    handlers=[logging.StreamHandler(sys.stderr)]
)
logger = logging.getLogger("printables-mcp")

# Initialize FastMCP server
mcp = FastMCP(
    "printables-mcp",
    instructions="Printables MCP Server - Access to Printables.com search, files, and descriptions"
)

@mcp.tool()
def search_printables(search_term: str, limit: int = 5) -> List[Dict[str, Any]]:
    """
    Search Printables.com for 3D models.
    
    Args:
        search_term: The search query (e.g. "benchy", "miniature", "vase")
        limit: Maximum number of results to return (default: 5, max: 50)
    
    Returns:
        List of model dictionaries containing id, name, slug, stats, user info, and image
    """
    try:
        # Validate limit
        limit = max(1, min(limit, 50))
        
        logger.info(f"Searching Printables for '{search_term}' with limit {limit}")
        results = printables_api.search_models(search_term, limit)
        
        if not results:
            return []
        
        # Format results for MCP
        formatted_results = []
        for model in results:
            formatted_model = {
                "id": model.get("id"),
                "name": model.get("name"),
                "slug": model.get("slug"),
                "url": f"https://www.printables.com/model/{model.get('id')}-{model.get('slug')}" if model.get("id") and model.get("slug") else None,
                "stats": {
                    "rating": model.get("ratingAvg"),
                    "likes": model.get("likesCount"),
                    "downloads": model.get("downloadCount"),
                    "published": model.get("datePublished")
                },
                "author": model.get("user", {}).get("publicUsername"),
                "image_url": f"https://media.printables.com/{model.get('image', {}).get('filePath')}" if model.get("image", {}).get("filePath") else None
            }
            formatted_results.append(formatted_model)
        
        logger.info(f"Found {len(formatted_results)} models")
        return formatted_results
        
    except Exception as e:
        error_msg = f"Error searching Printables: {str(e)}"
        logger.error(error_msg)
        raise RuntimeError(error_msg)

@mcp.tool()
def get_printables_files(model_id) -> List[Dict[str, Any]]:
    """
    Get downloadable files for a specific Printables model.
    
    Args:
        model_id: The numeric ID of the model (accepts int or string)
    
    Returns:
        List of file dictionaries containing name, download_url, size_bytes, and file_type
    """
    try:
        # Convert to string if needed and validate
        model_id_str = str(model_id).strip()
        if not model_id_str or not model_id_str.isdigit():
            raise ValueError(f"Invalid model_id: must be a numeric string, got '{model_id}'")
            
        logger.info(f"Fetching files for model ID {model_id_str}")
        files = printables_api.get_model_files(model_id_str)
        
        if not files:
            return []
        
        logger.info(f"Found {len(files)} files for model {model_id_str}")
        return files
        
    except Exception as e:
        error_msg = f"Error fetching files for model {model_id}: {str(e)}"
        logger.error(error_msg)
        raise RuntimeError(error_msg)

@mcp.tool()
def get_printables_description(model_url: str) -> str:
    """
    Get the description text for a Printables model by scraping its page.
    
    Args:
        model_url: Full URL to the model page (e.g. https://www.printables.com/model/12345-model-name)
    
    Returns:
        Formatted description text in markdown format
    """
    try:
        logger.info(f"Fetching description for {model_url}")
        description = printables_api.get_model_description(model_url)
        
        if description.startswith("Error:"):
            raise RuntimeError(description)
        
        logger.info("Description fetched successfully")
        return description
        
    except Exception as e:
        error_msg = f"Error fetching description from {model_url}: {str(e)}"
        logger.error(error_msg)
        raise RuntimeError(error_msg)

if __name__ == "__main__":
    logger.info("Starting Printables MCP server with stdio transport")
    mcp.run(transport="stdio")
