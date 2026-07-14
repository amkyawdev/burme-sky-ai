import re
from typing import Optional


class MarkdownParser:
    """Simple markdown parser for formatting AI responses"""
    
    @staticmethod
    def parse_inline(text: str) -> str:
        """Parse inline markdown elements"""
        # Bold
        text = re.sub(r'\*\*(.+?)\*\*', r'<strong>\1</strong>', text)
        text = re.sub(r'__(.+?)__', r'<strong>\1</strong>', text)
        
        # Italic
        text = re.sub(r'\*(.+?)\*', r'<em>\1</em>', text)
        text = re.sub(r'_(.+?)_', r'<em>\1</em>', text)
        
        # Inline code
        text = re.sub(r'`([^`]+)`', r'<code>\1</code>', text)
        
        return text
    
    @staticmethod
    def parse_block(text: str) -> str:
        """Parse block-level markdown elements"""
        lines = text.split('\n')
        result = []
        in_code_block = False
        code_buffer = []
        code_language = ""
        
        for line in lines:
            # Code blocks
            if line.startswith('```'):
                if not in_code_block:
                    in_code_block = True
                    code_language = line[3:].strip()
                    code_buffer = []
                else:
                    in_code_block = False
                    code_class = f' class="language-{code_language}"' if code_language else ''
                    result.append(f'<pre><code{code_class}>{"".join(code_buffer)}</code></pre>')
                    code_buffer = []
                    code_language = ""
                continue
            
            if in_code_block:
                code_buffer.append(line + '\n')
                continue
            
            # Headers
            if line.startswith('### '):
                result.append(f'<h3>{line[4:]}</h3>')
            elif line.startswith('## '):
                result.append(f'<h2>{line[3:]}</h2>')
            elif line.startswith('# '):
                result.append(f'<h1>{line[2:]}</h1>')
            # Unordered lists
            elif line.startswith('- ') or line.startswith('* '):
                result.append(f'<li>{line[2:]}</li>')
            # Ordered lists
            elif re.match(r'^\d+\. ', line):
                result.append(f'<li>{re.sub(r"^\d+\. ", "", line)}</li>')
            # Blockquotes
            elif line.startswith('> '):
                result.append(f'<blockquote>{line[2:]}</blockquote>')
            # Horizontal rules
            elif line in ('---', '***', '___'):
                result.append('<hr>')
            # Regular paragraphs
            elif line.strip():
                result.append(f'<p>{MarkdownParser.parse_inline(line)}</p>')
            else:
                result.append('')
        
        return '\n'.join(result)
    
    @staticmethod
    def parse(text: str) -> str:
        """Parse complete markdown text"""
        return MarkdownParser.parse_block(text)
