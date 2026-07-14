<template>
  <div class="model-options mb-3">
    <h6 class="text-white mb-2">
      <i class="bi bi-gpu me-2"></i>Models
    </h6>
    <div class="model-grid">
      <div 
        v-for="model in models" 
        :key="model.id"
        class="model-card"
        :class="{ active: model.id === currentModel }"
        @click="selectModel(model.id)"
      >
        <div class="model-icon">
          <i :class="model.icon"></i>
        </div>
        <div class="model-info">
          <small class="model-name">{{ model.name }}</small>
          <small class="text-muted d-block">{{ model.category }}</small>
        </div>
      </div>
    </div>
  </div>
</template>

<script setup>
import { computed } from 'vue'
import { useChatStore } from '@/stores/chatStore'

const chatStore = useChatStore()

const models = [
  { id: 'llama2', name: 'Llama 2', category: 'General', icon: 'bi bi-robot' },
  { id: 'codellama', name: 'Code Llama', category: 'Coding', icon: 'bi bi-code-slash' },
  { id: 'mistral', name: 'Mistral', category: 'Fast', icon: 'bi bi-lightning-charge' },
  { id: 'mixtral', name: 'Mixtral', category: 'Quality', icon: 'bi bi-stars' }
]

const currentModel = computed(() => chatStore.currentModel)

const selectModel = (modelId) => {
  chatStore.setModel(modelId)
}
</script>

<style scoped>
.model-options {
  padding: 0.75rem;
  background-color: rgba(255, 255, 255, 0.05);
  border-radius: var(--border-radius);
}

.model-grid {
  display: grid;
  grid-template-columns: repeat(2, 1fr);
  gap: 0.5rem;
}

.model-card {
  display: flex;
  align-items: center;
  gap: 0.5rem;
  padding: 0.5rem;
  border-radius: 8px;
  cursor: pointer;
  transition: all 0.2s ease;
  border: 1px solid transparent;
}

.model-card:hover {
  background-color: rgba(108, 99, 255, 0.1);
}

.model-card.active {
  background-color: rgba(108, 99, 255, 0.2);
  border-color: var(--primary-color);
}

.model-icon {
  width: 32px;
  height: 32px;
  display: flex;
  align-items: center;
  justify-content: center;
  background-color: var(--primary-color);
  border-radius: 8px;
  font-size: 1rem;
}

.model-info {
  overflow: hidden;
}

.model-name {
  display: block;
  font-weight: 500;
  white-space: nowrap;
  overflow: hidden;
  text-overflow: ellipsis;
}
</style>
