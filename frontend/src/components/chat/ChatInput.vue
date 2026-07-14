<template>
  <div class="chat-input-wrapper">
    <div class="input-group">
      <button class="btn btn-outline-secondary" @click="triggerFileUpload" title="Upload file">
        <i class="bi bi-paperclip"></i>
      </button>
      <input type="file" ref="fileInput" class="d-none" @change="handleFile" />
      <input 
        type="text" 
        class="form-control smooth-input" 
        v-model="message"
        placeholder="Type your message..."
        @keydown.enter.prevent="send"
        :disabled="isStreaming"
      />
      <button class="btn btn-primary" @click="send" :disabled="!message.trim() || isStreaming">
        <i v-if="!isStreaming" class="bi bi-send-fill send-icon" :class="{ 'animate-send': sending }"></i>
        <span v-else class="loading-spinner"></span>
      </button>
    </div>
  </div>
</template>

<script setup>
import { ref, computed } from 'vue'
import { useChatStore } from '@/stores/chatStore'

const chatStore = useChatStore()
const message = ref('')
const sending = ref(false)
const fileInput = ref(null)

const isStreaming = computed(() => chatStore.isStreaming)

const emit = defineEmits(['send-message', 'file-uploaded'])

const send = () => {
  if (!message.value.trim() || isStreaming.value) return
  sending.value = true
  emit('send-message', message.value)
  message.value = ''
  setTimeout(() => sending.value = false, 500)
}

const triggerFileUpload = () => fileInput.value.click()

const handleFile = (e) => {
  const file = e.target.files[0]
  if (file) {
    console.log('File selected:', file.name)
    emit('file-uploaded', file)
  }
  fileInput.value.value = ''
}
</script>

<style scoped>
.chat-input-wrapper {
  padding: 1rem 1.5rem;
  background-color: var(--bg-card);
  border-top: 1px solid rgba(108, 99, 255, 0.2);
}

.input-group {
  gap: 0.5rem;
}

.smooth-input {
  border-radius: 20px;
  padding: 12px 20px;
  border: 1px solid #e0e0e0;
  transition: all 0.3s ease;
  background-color: rgba(255, 255, 255, 0.05);
  color: var(--text-primary);
}

.smooth-input:focus {
  border-color: var(--primary-color);
  box-shadow: 0 0 0 0.2rem rgba(108, 99, 255, 0.25);
  background-color: rgba(255, 255, 255, 0.1);
}

.smooth-input::placeholder {
  color: var(--text-secondary);
}

.send-icon {
  transition: transform 0.3s ease;
}

.animate-send {
  animation: sendPulse 0.5s ease;
}

@keyframes sendPulse {
  0% { transform: scale(1); }
  50% { transform: scale(1.3); }
  100% { transform: scale(1); }
}

.loading-spinner {
  display: inline-block;
  width: 16px;
  height: 16px;
  border: 2px solid rgba(255, 255, 255, 0.3);
  border-radius: 50%;
  border-top-color: white;
  animation: spin 0.8s linear infinite;
}

@keyframes spin {
  to { transform: rotate(360deg); }
}
</style>
