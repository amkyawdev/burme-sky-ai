<template>
  <div class="chat-messages" ref="messagesContainer">
    <div v-if="messages.length === 0" class="empty-state">
      <img src="/images/bot.svg" alt="Bot" class="empty-icon">
      <h5>Start a conversation</h5>
      <p class="text-muted">Send a message to begin chatting with AI</p>
    </div>
    
    <ChatMessage 
      v-for="(message, index) in messages" 
      :key="index"
      :message="message"
      :show-header="index === 0 || messages[index - 1]?.role !== message.role"
    />
    
    <div v-if="isStreaming" class="typing-indicator">
      <span></span>
      <span></span>
      <span></span>
    </div>
  </div>
</template>

<script setup>
import { ref, watch, nextTick, computed } from 'vue'
import ChatMessage from './ChatMessage.vue'
import { useChatStore } from '@/stores/chatStore'

const chatStore = useChatStore()
const messagesContainer = ref(null)

const messages = computed(() => chatStore.messages)
const isStreaming = computed(() => chatStore.isStreaming)

watch(messages, async () => {
  await nextTick()
  scrollToBottom()
}, { deep: true })

const scrollToBottom = () => {
  if (messagesContainer.value) {
    messagesContainer.value.scrollTop = messagesContainer.value.scrollHeight
  }
}
</script>

<style scoped>
.chat-messages {
  flex: 1;
  overflow-y: auto;
  padding: 1.5rem;
  display: flex;
  flex-direction: column;
}

.empty-state {
  display: flex;
  flex-direction: column;
  align-items: center;
  justify-content: center;
  height: 100%;
  text-align: center;
  color: var(--text-secondary);
}

.empty-icon {
  width: 80px;
  height: 80px;
  margin-bottom: 1rem;
  opacity: 0.5;
}

.typing-indicator {
  display: flex;
  gap: 4px;
  padding: 1rem;
  background-color: var(--bg-card);
  border-radius: var(--border-radius);
  width: fit-content;
}

.typing-indicator span {
  width: 8px;
  height: 8px;
  background-color: var(--primary-color);
  border-radius: 50%;
  animation: typing 1.4s infinite ease-in-out;
}

.typing-indicator span:nth-child(1) { animation-delay: 0s; }
.typing-indicator span:nth-child(2) { animation-delay: 0.2s; }
.typing-indicator span:nth-child(3) { animation-delay: 0.4s; }

@keyframes typing {
  0%, 60%, 100% { transform: translateY(0); opacity: 0.4; }
  30% { transform: translateY(-8px); opacity: 1; }
}
</style>
