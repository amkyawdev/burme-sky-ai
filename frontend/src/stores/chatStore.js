import { defineStore } from 'pinia'
import { ref } from 'vue'

export const useChatStore = defineStore('chat', () => {
  const messages = ref([])
  const history = ref([])
  const currentModel = ref('llama2')
  const isStreaming = ref(false)

  const addMessage = (msg) => messages.value.push(msg)
  const clearMessages = () => messages.value = []
  const clearHistory = () => history.value = []
  const setModel = (model) => currentModel.value = model
  const setStreaming = (streaming) => isStreaming.value = streaming

  const addToHistory = (title) => {
    history.value.unshift({
      id: Date.now(),
      title,
      date: new Date().toLocaleTimeString()
    })
  }

  return { 
    messages, 
    history, 
    currentModel, 
    isStreaming, 
    addMessage, 
    clearMessages,
    clearHistory, 
    setModel, 
    setStreaming,
    addToHistory 
  }
})
