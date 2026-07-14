import { useSettingsStore } from '@/stores/settingsStore'

const getApiUrl = () => {
  const settings = useSettingsStore()
  // Use environment variable if available, otherwise fall back to settings
  const envUrl = import.meta.env.VITE_API_URL || '/api'
  return settings.apiUrl || envUrl
}

export const streamChat = async (message, model, onChunk, onDone) => {
  const baseUrl = getApiUrl()
  
  try {
    const response = await fetch(`${baseUrl}/chat/stream`, {
      method: 'POST',
      headers: {
        'Content-Type': 'application/json',
      },
      body: JSON.stringify({ message, model })
    })

    if (!response.ok) {
      throw new Error(`HTTP error! status: ${response.status}`)
    }

    const reader = response.body.getReader()
    const decoder = new TextDecoder()

    while (true) {
      const { done, value } = await reader.read()
      if (done) break

      const chunk = decoder.decode(value)
      const lines = chunk.split('\n')

      for (const line of lines) {
        if (line.startsWith('data: ')) {
          try {
            const data = JSON.parse(line.slice(6))
            if (data.done) {
              onDone && onDone()
            } else if (data.chunk) {
              onChunk && onChunk(data.chunk)
            }
          } catch (e) {
            console.error('Error parsing SSE data:', e)
          }
        }
      }
    }
  } catch (error) {
    console.error('Stream error:', error)
    throw error
  }
}

export const fetchModels = async () => {
  const baseUrl = getApiUrl()
  
  try {
    const response = await fetch(`${baseUrl}/models`)
    if (!response.ok) throw new Error('Failed to fetch models')
    return await response.json()
  } catch (error) {
    console.error('Error fetching models:', error)
    return []
  }
}

export const fetchHistory = async () => {
  const baseUrl = getApiUrl()
  
  try {
    const response = await fetch(`${baseUrl}/history`)
    if (!response.ok) throw new Error('Failed to fetch history')
    return await response.json()
  } catch (error) {
    console.error('Error fetching history:', error)
    return []
  }
}

export const sendWebhook = async (payload) => {
  const settings = useSettingsStore()
  if (!settings.webhookUrl) return

  try {
    await fetch(settings.webhookUrl, {
      method: 'POST',
      headers: { 'Content-Type': 'application/json' },
      body: JSON.stringify(payload)
    })
  } catch (error) {
    console.error('Webhook error:', error)
  }
}
