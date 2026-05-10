import sys
import os
import re

def markdown_to_html(md_text):
    # Basic Markdown to HTML conversion logic
    html = md_text
    
    # Headers
    html = re.sub(r'^# (.*)$', r'<h1>\1</h1>', html, flags=re.M)
    html = re.sub(r'^## (.*)$', r'<h2>\1</h2>', html, flags=re.M)
    html = re.sub(r'^### (.*)$', r'<h3>\1</h3>', html, flags=re.M)
    
    # Bold and Italic
    html = re.sub(r'\*\*(.*?)\*\*', r'<strong>\1</strong>', html)
    html = re.sub(r'\*(.*?)\*', r'<em>\1</em>', html)
    
    # Lists
    html = re.sub(r'^\* (.*)$', r'<li>\1</li>', html, flags=re.M)
    # Wrap li in ul (simplistic)
    html = re.sub(r'(<li>.*</li>)', r'<ul>\1</ul>', html, flags=re.S)
    
    # Links
    html = re.sub(r'\[(.*?)\]\((.*?)\)', r'<a href="\2">\1</a>', html)
    
    # Paragraphs (crude)
    lines = html.split('\n')
    new_lines = []
    for line in lines:
        if line.strip() and not line.startswith('<'):
            new_lines.append(f"<p>{line}</p>")
        else:
            new_lines.append(line)
    html = '\n'.join(new_lines)
    
    return html

def convert_file(input_path):
    if not os.path.exists(input_path):
        print(f"Error: {input_path} not found.")
        return

    with open(input_path, 'r', encoding='utf-8') as f:
        md_content = f.read()
    
    html_content = f"""
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Converted Markdown</title>
    <style>
        body {{ font-family: -apple-system, BlinkMacSystemFont, "Segoe UI", Roboto, Helvetica, Arial, sans-serif; line-height: 1.6; color: #333; max-width: 800px; margin: 2rem auto; padding: 0 1rem; }}
        h1, h2, h3 {{ color: #1a1a1a; }}
        code {{ background: #f4f4f4; padding: 0.2rem 0.4rem; border-radius: 3px; }}
        blockquote {{ border-left: 4px solid #ddd; padding-left: 1rem; color: #666; margin-left: 0; }}
        a {{ color: #0366d6; text-decoration: none; }}
        a:hover {{ text-decoration: underline; }}
    </style>
</head>
<body>
    {markdown_to_html(md_content)}
</body>
</html>
"""
    output_path = input_path.replace('.md', '.html')
    with open(output_path, 'w', encoding='utf-8') as f:
        f.write(html_content)
    print(f"Successfully converted {input_path} to {output_path}")

if __name__ == "__main__":
    if len(sys.argv) > 1:
        convert_file(sys.argv[1])
    else:
        print("Usage: python md_to_html.py <filename.md>")
