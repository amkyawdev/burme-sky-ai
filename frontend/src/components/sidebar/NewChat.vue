<template>
  <button class="btn btn-primary btn-sm w-100 mb-2" @click="startNewChat">
    <i class="bi bi-plus-lg me-1"></i>
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
  padding: 0.4rem 0.75rem;
  font-size: 0.8rem;
}
</style>
