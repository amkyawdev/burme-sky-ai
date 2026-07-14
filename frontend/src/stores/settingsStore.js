import { defineStore } from 'pinia'
import { ref, watch } from 'vue'

export const useSettingsStore = defineStore('settings', () => {
  const apiUrl = ref(localStorage.getItem('apiUrl') || '/api')
  const webhookUrl = ref(localStorage.getItem('webhookUrl') || '')
  const theme = ref(localStorage.getItem('theme') || 'dark')
  const fontSize = ref(localStorage.getItem('fontSize') || 'medium')

  watch(apiUrl, (val) => localStorage.setItem('apiUrl', val))
  watch(webhookUrl, (val) => localStorage.setItem('webhookUrl', val))
  watch(theme, (val) => localStorage.setItem('theme', val))
  watch(fontSize, (val) => localStorage.setItem('fontSize', val))

  const setApiUrl = (url) => apiUrl.value = url
  const setWebhookUrl = (url) => webhookUrl.value = url
  const setTheme = (newTheme) => theme.value = newTheme
  const setFontSize = (size) => fontSize.value = size

  return { 
    apiUrl, 
    webhookUrl, 
    theme, 
    fontSize,
    setApiUrl,
    setWebhookUrl,
    setTheme,
    setFontSize
  }
})
