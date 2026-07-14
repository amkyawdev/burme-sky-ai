<template>
  <div class="chat-page">
    <!-- Chat Header -->
    <header class="chat-header">
      <div class="d-flex align-items-center">
        <button class="btn btn-outline-light btn-sm me-2" @click="toggleSidebar" title="Toggle Sidebar">
          <i class="bi bi-list"></i>
        </button>
        <h6 class="mb-0 text-white">Chat</h6>
        <span v-if="currentModel" class="badge bg-primary ms-2">{{ currentModel }}</span>
      </div>
      <div class="d-flex align-items-center gap-2">
        <button class="btn btn-sm btn-outline-light" @click="clearChat" :disabled="messages.length === 0">
          <i class="bi bi-trash3"></i>
        </button>
        <ModelSelector />
      </div>
    </header>

    <!-- Chat Messages Area -->
    <ChatMessages />
    
    <!-- Chat Input Area -->
    <ChatInput @send-message="handleSendMessage" @file-uploaded="handleFileUpload" />
    
    <!-- Error Toast -->
    <div v-if="error" class="error-toast">
      <div class="alert alert-danger m-3">
        <i class="bi bi-exclamation-triangle me-2"></i>
        {{ error }}
        <button class="btn-close btn-close-white float-end" @click="error = null"></button>
      </div>
    </div>
  </div>
</template>

<script setup>
import { ref } from 'vue'
import ChatMessages from '@/components/chat/ChatMessages.vue'
import ChatInput from '@/components/chat/ChatInput.vue'
import ModelSelector from '@/components/chat/ModelSelector.vue'
import { useChat } from '@/composables/useChat'
import { useSidebar } from '@/composables/useSidebar'
import { useChatStore } from '@/stores/chatStore'

const { sendMessage, error } = useChat()
const { toggleSidebar } = useSidebar()
const chatStore = useChatStore()

const messages = ref(chatStore.messages)
const currentModel = chatStore.currentModel

const handleSendMessage = async (message) => {
  await sendMessage(message)
}

const handleFileUpload = (file) => {
  console.log('File uploaded:', file)
}

const clearChat = () => {
  chatStore.clearMessages()
}
</script>

<style scoped>
.chat-page {
  display: flex;
  flex-direction: column;
  height: 100vh;
  width: 100%;
}

.chat-header {
  background-color: var(--bg-card);
  padding: 0.5rem 1rem;
  border-bottom: 1px solid rgba(108, 99, 255, 0.2);
  display: flex;
  align-items: center;
  justify-content: space-between;
}

.error-toast {
  position: fixed;
  bottom: 70px;
  left: 50%;
  transform: translateX(-50%);
  z-index: 1000;
}
</style>
