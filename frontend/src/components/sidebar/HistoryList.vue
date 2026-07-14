<template>
  <div class="history-list">
    <div class="d-flex justify-content-between align-items-center mb-3">
      <h6 class="mb-0 text-white">
        <i class="bi bi-clock-history me-2"></i>History
      </h6>
      <button 
        class="btn btn-sm btn-outline-danger" 
        @click="clearAll"
        :disabled="history.length === 0"
        title="Clear all history"
      >
        <i class="bi bi-trash3"></i>
      </button>
    </div>

    <div v-if="history.length === 0" class="text-muted text-center py-3">
      <i class="bi bi-inbox fs-4"></i>
      <p class="small mb-0">No history yet</p>
    </div>

    <div v-else class="list-group list-group-flush">
      <a 
        v-for="(item, idx) in history" 
        :key="item.id || idx"
        href="#"
        class="list-group-item list-group-item-action"
        @click.prevent="loadChat(item, idx)"
      >
        <div class="d-flex justify-content-between align-items-center">
          <span class="text-truncate">{{ item.title || 'Chat ' + (idx+1) }}</span>
          <small class="text-muted">{{ item.date || 'Just now' }}</small>
        </div>
      </a>
    </div>
  </div>
</template>

<script setup>
import { computed } from 'vue'
import { useChatStore } from '@/stores/chatStore'
import { useRouter } from 'vue-router'

const chatStore = useChatStore()
const router = useRouter()
const history = computed(() => chatStore.history)

const clearAll = () => {
  if (confirm('Clear all history? This action cannot be undone.')) {
    chatStore.clearHistory()
  }
}

const loadChat = (item, index) => {
  console.log('Loading chat:', item.title || index)
  router.push('/chat')
}
</script>

<style scoped>
.history-list {
  flex: 1;
  overflow-y: auto;
}

.list-group-item {
  background-color: transparent;
  border-color: rgba(108, 99, 255, 0.2);
  color: var(--text-primary);
  padding: 0.75rem 1rem;
  transition: all 0.2s ease;
}

.list-group-item:hover {
  background-color: rgba(108, 99, 255, 0.1);
  border-color: var(--primary-color);
}

.list-group-item-action.active {
  background-color: var(--primary-color);
  border-color: var(--primary-color);
}
</style>
