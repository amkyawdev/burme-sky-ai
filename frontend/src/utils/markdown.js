import { marked } from 'marked'
import hljs from 'highlight.js'
import DOMPurify from 'dompurify'

marked.setOptions({
  highlight: function(code, lang) {
    if (lang && hljs.getLanguage(lang)) {
      try {
        return hljs.highlight(code, { language: lang }).value
      } catch (e) {
        console.error('Highlight error:', e)
      }
    }
    return hljs.highlightAuto(code).value
  },
  breaks: true,
  gfm: true
})

export const parseMarkdown = (text) => {
  const html = marked.parse(text)
  return DOMPurify.sanitize(html)
}

export const parseInline = (text) => {
  const html = marked.parseInline(text)
  return DOMPurify.sanitize(html)
}
