<template>
  <div class="model-selector dropdown">
    <button 
      class="btn btn-outline-light btn-sm dropdown-toggle w-100" 
      type="button" 
      data-bs-toggle="dropdown"
    >
      <i class="bi bi-cpu me-1"></i>
      {{ currentModel }}
    </button>
    <ul class="dropdown-menu dropdown-menu-dark w-100">
      <li v-for="model in models" :key="model.id">
        <a 
          class="dropdown-item" 
          :class="{ active: model.id === currentModel }"
          href="#"
          @click.prevent="selectModel(model.id)"
        >
          {{ model.name }}
        </a>
      </li>
    </ul>
  </div>
</template>

<script setup>
import { ref, computed, onMounted } from 'vue'
import { useChatStore } from '@/stores/chatStore'
import { fetchModels } from '@/utils/api'

const chatStore = useChatStore()
const models = ref([
  { id: 'minimax-m2.5', name: 'MiniMax-M2.5' },
  { id: 'minimax-m3', name: 'MiniMax-M3' },
  { id: 'ministral-3:8b', name: 'Ministral-3:8b' },
  { id: 'ministral-3:14b', name: 'Ministral-3:14b' },
  { id: 'nemotron-3-nano:30b', name: 'Nemotron-3:30b' }
])

const currentModel = computed(() => chatStore.currentModel)

const selectModel = (modelId) => {
  chatStore.setModel(modelId)
}

onMounted(async () => {
  try {
    const fetchedModels = await fetchModels()
    if (fetchedModels.models && fetchedModels.models.length > 0) {
      models.value = fetchedModels.models
    }
  } catch (error) {
    console.error('Failed to load models:', error)
  }
})
</script>

<style scoped>
.model-selector {
  margin-bottom: 0;
}
</style>
