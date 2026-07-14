<template>
  <header class="header">
    <div class="d-flex align-items-center">
      <h5 class="mb-0 text-white">Chat</h5>
      <span v-if="currentModel" class="badge bg-primary ms-2">{{ currentModel }}</span>
    </div>
    <div class="d-flex align-items-center gap-2">
      <button class="btn btn-sm btn-outline-light" @click="clearChat" :disabled="messages.length === 0">
        <i class="bi bi-trash3"></i>
      </button>
      <ModelSelector />
    </div>

    <!-- Animation overlays -->
    <div v-if="showThanking" class="position-fixed top-0 start-50 translate-middle-x mt-3">
      <div class="alert alert-success animate__animated animate__fadeInDown">
        <i class="bi bi-check-circle me-2"></i>{{ animationMessage }}
      </div>
    </div>
  </header>
</template>

<script setup>
import { computed } from 'vue'
import { useChatStore } from '@/stores/chatStore'
import ModelSelector from '@/components/chat/ModelSelector.vue'
import { useAnimation } from '@/composables/useAnimation'

const chatStore = useChatStore()
const { showThanking, animationMessage } = useAnimation()

const messages = computed(() => chatStore.messages)
const currentModel = computed(() => chatStore.currentModel)

const clearChat = () => {
  chatStore.clearMessages()
}
</script>

<style scoped>
.header {
  background-color: var(--bg-card);
  padding: 1rem 1.5rem;
  border-bottom: 1px solid rgba(108, 99, 255, 0.2);
  display: flex;
  align-items: center;
  justify-content: space-between;
}
</style>
