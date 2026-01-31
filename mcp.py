"""
Example MCP Server using FastMCP
Demonstrates tools, resources, and prompts
"""

from fastmcp import FastMCP
import trnt

# Initialize the server
mcp = FastMCP(name="Trenton: Document Creation Assistant")

@mcp.tool()
def create_markdown_file(filename: str, contents: str) -> str:
    """Create a markdown file with the given contents."""
    return trnt.create_markdown_file(filename, contents)

@mcp.tool()
def modify_markdown_file(filename: str, contents: str) -> str:
    """Modify a markdown file's contents."""
    return trnt.modify_markdown_file(filename, contents)

@mcp.tool()
def convert_markdown_to_pdf(markdown_file: str, output_file: str) -> str:
    """Convert a markdown file to PDF."""
    return trnt.convert_markdown_to_pdf(markdown_file, output_file)

@mcp.tool()
def convert_markdown_to_word(markdown_file: str, output_file: str) -> str:
    """Convert a markdown file to Word document."""
    return trnt.convert_markdown_to_word(markdown_file, output_file)

@mcp.prompt()
def document_creation_guide() -> str:
    """Guide for creating and converting documents."""
    return trnt.document_creation_guide()

if __name__ == "__main__":
    # Run the server
    mcp.run()