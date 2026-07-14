<template>
  <div class="chat-page">
    <ChatMessages />
    <ChatInput @send-message="handleSendMessage" @file-uploaded="handleFileUpload" />
    
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
import { useChat } from '@/composables/useChat'

const { sendMessage, error } = useChat()

const handleSendMessage = async (message) => {
  await sendMessage(message)
}

const handleFileUpload = (file) => {
  console.log('File uploaded:', file)
  // TODO: Implement file upload logic
}
</script>

<style scoped>
.chat-page {
  display: flex;
  flex-direction: column;
  height: calc(100vh - 60px);
}

.error-toast {
  position: fixed;
  bottom: 80px;
  left: 50%;
  transform: translateX(-50%);
  z-index: 1000;
}
</style>
