export const formatCLI = (output) => {
  if (!output) return ''
  
  // Remove ANSI escape codes
  let formatted = output.replace(/\x1B\[[0-9;]*[a-zA-Z]/g, '')
  
  // Format command blocks
  formatted = formatted.replace(/\$\s+(.*)/gm, '<span class="cli-prompt">$</span> <span class="cli-command">$1</span>')
  
  // Format paths
  formatted = formatted.replace(/\/([\w\-\./]+)/g, '<span class="cli-path">/$1</span>')
  
  // Format errors
  formatted = formatted.replace(/error|failed|fatal/gi, '<span class="cli-error">$&</span>')
  
  // Format success
  formatted = formatted.replace(/success|done|completed/gi, '<span class="cli-success">$&</span>')
  
  return formatted
}

export const isCLIContent = (text) => {
  const cliPatterns = [
    /^\$\s+/m,
    /\|\s*\w+/,
    /\[.*?\]\s*=/,
    /--[\w-]+/,
    /\\\w+\s+/
  ]
  
  return cliPatterns.some(pattern => pattern.test(text))
}
