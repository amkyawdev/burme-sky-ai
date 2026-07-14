import { ref } from 'vue'
import { useChatStore } from '@/stores/chatStore'
import { streamChat } from '@/utils/api'
import { parseMarkdown } from '@/utils/markdown'
import { formatCLI, isCLIContent } from '@/utils/cliFormatter'
import { useAnimation } from './useAnimation'

export const useChat = () => {
  const chatStore = useChatStore()
  const { showConnectionAnimation, showThankingAnimation } = useAnimation()
  const error = ref(null)
  const isLoading = ref(false)

  const sendMessage = async (message) => {
    if (!message.trim()) return

    error.value = null
    isLoading.value = true
    chatStore.setStreaming(true)

    const userMessage = { role: 'user', content: message }
    chatStore.addMessage(userMessage)

    const assistantMessage = { role: 'assistant', content: '' }
    chatStore.addMessage(assistantMessage)

    try {
      await streamChat(
        message,
        chatStore.currentModel,
        (chunk) => {
          assistantMessage.content += chunk
          // Trigger reactivity
          const lastIndex = chatStore.messages.length - 1
          chatStore.messages[lastIndex] = { ...assistantMessage }
        },
        () => {
          isLoading.value = false
          chatStore.setStreaming(false)
          showThankingAnimation()

          // Format CLI content if detected
          if (isCLIContent(assistantMessage.content)) {
            assistantMessage.content = formatCLI(assistantMessage.content)
          }
        }
      )
    } catch (err) {
      error.value = err.message
      isLoading.value = false
      chatStore.setStreaming(false)
      chatStore.addMessage({
        role: 'assistant',
        content: `Error: ${err.message}`
      })
    }
  }

  const clearChat = () => {
    chatStore.clearMessages()
    error.value = null
  }

  return {
    messages: chatStore.messages,
    isStreaming: chatStore.isStreaming,
    isLoading,
    error,
    sendMessage,
    clearChat
  }
}
