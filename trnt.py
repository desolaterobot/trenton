"""
Core document creation functions for Trenton
"""

import markdown
from weasyprint import HTML, CSS
from docx import Document
from docx.shared import Pt


def create_markdown_file(filename: str, contents: str) -> str:
    """Create a markdown file with the given contents."""
    with open(filename, 'w') as f:
        f.write(contents)
    return f"Markdown file '{filename}' created successfully."


def modify_markdown_file(filename: str, contents: str) -> str:
    """Modify a markdown file's contents."""
    with open(filename, 'w') as f:
        f.write(contents)
    return f"Markdown file '{filename}' modified successfully."


def convert_markdown_to_pdf(markdown_file: str, output_file: str) -> str:
    """Convert a markdown file to PDF."""
    
    with open(markdown_file, 'r') as f:
        markdown_content = f.read()
    
    html_content = markdown.markdown(markdown_content)
    html_document = f"<html><body>{html_content}</body></html>"
    
    HTML(string=html_document).write_pdf(output_file)
    return f"PDF file '{output_file}' created successfully from '{markdown_file}'."


def convert_markdown_to_word(markdown_file: str, output_file: str) -> str:
    """Convert a markdown file to Word document."""
    
    with open(markdown_file, 'r') as f:
        markdown_content = f.read()
    
    doc = Document()
    for line in markdown_content.split('\n'):
        if line.strip():
            doc.add_paragraph(line)
    
    doc.save(output_file)
    return f"Word file '{output_file}' created successfully from '{markdown_file}'."


def document_creation_prompt() -> str:
    """Guide for creating and converting documents."""
    return """You are a document creation assistant.
When asked to create a document, always create a sample markdown file first using the create_markdown_file tool.
After creating the markdown file, you may convert it to other formats onl when asked.
Always ask for clarification on formatting preferences and ensure content is properly structured."""
