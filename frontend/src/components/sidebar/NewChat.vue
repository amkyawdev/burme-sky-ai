<template>
  <button class="btn btn-primary w-100 mb-3" @click="startNewChat">
    <i class="bi bi-plus-lg me-2"></i>
    New Chat
  </button>
</template>

<script setup>
import { useRouter } from 'vue-router'
import { useChatStore } from '@/stores/chatStore'

const router = useRouter()
const chatStore = useChatStore()

const startNewChat = () => {
  chatStore.clearMessages()
  router.push('/chat')
}
</script>

<style scoped>
.btn-primary {
  background: linear-gradient(135deg, var(--primary-color), var(--secondary-color));
  border: none;
  padding: 0.75rem 1rem;
  font-weight: 600;
  transition: all 0.3s ease;
}

.btn-primary:hover {
  transform: translateY(-2px);
  box-shadow: 0 4px 15px rgba(108, 99, 255, 0.4);
}
</style>
