import { ref, onMounted } from 'vue'
import { useChatStore } from '@/stores/chatStore'
import { fetchHistory } from '@/utils/api'

export const useHistory = () => {
  const chatStore = useChatStore()
  const isLoading = ref(false)
  const error = ref(null)

  const loadHistory = async () => {
    isLoading.value = true
    error.value = null
    
    try {
      const history = await fetchHistory()
      chatStore.history = history
    } catch (err) {
      error.value = err.message
      console.error('Failed to load history:', err)
    } finally {
      isLoading.value = false
    }
  }

  const saveToHistory = (title, messages) => {
    chatStore.addToHistory(title || messages[0]?.content?.slice(0, 50) || 'New Chat')
  }

  const clearHistory = () => {
    chatStore.clearHistory()
  }

  onMounted(() => {
    loadHistory()
  })

  return {
    history: chatStore.history,
    isLoading,
    error,
    loadHistory,
    saveToHistory,
    clearHistory
  }
}
