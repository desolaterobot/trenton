# Trenton: Document Creation Assistant MCP Server

A FastMCP server for creating and converting documents programmatically. Provides tools for markdown file management and format conversion to PDF and Word documents.

## Features

- **Create Markdown Files** - Generate markdown documents programmatically
- **Modify Markdown Files** - Edit existing markdown content
- **Convert to PDF** - Transform markdown files to PDF format
- **Convert to Word** - Transform markdown files to DOCX format
- **Document Guide** - Access best practices for document creation

## Installation

### Requirements
- Python 3.8+

### Setup

```bash
pip install -r requirements.txt
```

## Usage

### Running the Server

```bash
python mcp.py
```

The server will start and expose the document creation tools via MCP.

### Available Tools

#### `create_markdown_file(filename: str, contents: str)`
Create a new markdown file with the specified content.

```python
create_markdown_file("report.md", "# My Report\n\nThis is content.")
```

#### `modify_markdown_file(filename: str, contents: str)`
Modify an existing markdown file's content.

```python
modify_markdown_file("report.md", "# Updated Report\n\nNew content here.")
```

#### `convert_markdown_to_pdf(markdown_file: str, output_file: str)`
Convert a markdown file to PDF format.

```python
convert_markdown_to_pdf("report.md", "report.pdf")
```

#### `convert_markdown_to_word(markdown_file: str, output_file: str)`
Convert a markdown file to Word DOCX format.

```python
convert_markdown_to_word("report.md", "report.docx")
```

## Architecture

- **mcp.py** - FastMCP server layer that exposes tools and prompts
- **trnt.py** - Core functions that handle actual document operations

This separation allows the core logic to be used independently of the MCP framework.

## Example Workflow

1. Create a markdown document:
   ```
   create_markdown_file("summary.md", "# Project Summary\n\nKey findings...")
   ```

2. Convert to PDF for sharing:
   ```
   convert_markdown_to_pdf("summary.md", "summary.pdf")
   ```

3. Convert to Word for editing:
   ```
   convert_markdown_to_word("summary.md", "summary.docx")
   ```

## License

MIT
