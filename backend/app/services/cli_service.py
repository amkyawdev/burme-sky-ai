import asyncio
import subprocess
import re
from typing import AsyncGenerator


class CLIService:
    CLI_PATTERNS = [
        r'^\\?\s*(ls|dir|cd|pwd|mkdir|rm|cp|mv|cat|echo|grep|find|chmod|chown)',
        r'^\\?\s*(npm|yarn|pnpm|node|python|pip|git|docker|kubectl)',
        r'^\\?\s*(curl|wget|ssh|scp|rsync)',
        r'^\\?.*`.*`',  # Backtick commands
    ]
    
    def is_cli_command(self, text: str) -> bool:
        """Check if the message contains CLI commands"""
        for pattern in self.CLI_PATTERNS:
            if re.search(pattern, text.strip(), re.IGNORECASE):
                return True
        return False
    
    async def execute_command(self, command: str) -> str:
        """Execute a CLI command and return the output"""
        # Remove command prefixes like /execute or \
        clean_command = re.sub(r'^[/\\]?\s*', '', command.strip())
        clean_command = clean_command.strip('`')
        
        try:
            # Execute command
            process = await asyncio.create_subprocess_shell(
                clean_command,
                stdout=asyncio.subprocess.PIPE,
                stderr=asyncio.subprocess.STDOUT,
                shell=True
            )
            
            output, _ = await process.communicate()
            result = output.decode('utf-8', errors='replace')
            
            return result if result else "Command executed successfully (no output)"
            
        except Exception as e:
            return f"Error executing command: {str(e)}"
    
    def format_output(self, output: str) -> str:
        """Format CLI output with basic styling"""
        lines = output.split('\n')
        formatted_lines = []
        
        for line in lines:
            # Highlight paths
            line = re.sub(r'(/[a-zA-Z0-9_./-]+)', r'`\1`', line)
            # Highlight errors in red
            line = re.sub(r'\b(error|failed|fatal)\b', r'**\1**', line, flags=re.IGNORECASE)
            # Highlight success in green
            line = re.sub(r'\b(success|done|completed)\b', r'**\1**', line, flags=re.IGNORECASE)
            formatted_lines.append(line)
        
        return '\n'.join(formatted_lines)
