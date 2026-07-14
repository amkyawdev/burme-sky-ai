<template>
  <div class="history-list">
    <div class="d-flex justify-content-between align-items-center mb-1">
      <h6 class="mb-0 text-white" style="font-size: 0.75rem;">
        <i class="bi bi-clock-history me-1"></i>History
      </h6>
      <button 
        class="btn btn-sm btn-outline-danger py-0 px-1"
        @click="clearAll"
        :disabled="history.length === 0"
        title="Clear all"
        style="font-size: 0.65rem;"
      >
        <i class="bi bi-trash3"></i>
      </button>
    </div>

    <div v-if="history.length === 0" class="text-muted text-center py-2">
      <small style="font-size: 0.7rem;">No history</small>
    </div>

    <div v-else class="list-group list-group-flush" style="font-size: 0.7rem;">
      <a 
        v-for="(item, idx) in history" 
        :key="item.id || idx"
        href="#"
        class="list-group-item list-group-item-action py-1 px-2"
        @click.prevent="loadChat(item, idx)"
      >
        <div class="d-flex justify-content-between align-items-center">
          <span class="text-truncate" style="font-size: 0.7rem;">{{ item.title || 'Chat ' + (idx+1) }}</span>
          <small class="text-muted" style="font-size: 0.6rem;">{{ item.date }}</small>
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
  if (confirm('Clear all history?')) {
    chatStore.clearHistory()
  }
}

const loadChat = (item, index) => {
  router.push('/chat')
}
</script>

<style scoped>
.history-list {
  flex: 1;
  overflow-y: auto;
  font-size: 0.75rem;
}

.list-group-item {
  background-color: transparent;
  border-color: rgba(108, 99, 255, 0.2);
  color: var(--text-primary);
  transition: all 0.2s ease;
}

.list-group-item:hover {
  background-color: rgba(108, 99, 255, 0.1);
  border-color: var(--primary-color);
}
</style>
