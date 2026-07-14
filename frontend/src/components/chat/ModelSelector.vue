<template>
  <div class="model-selector dropdown">
    <button 
      class="btn btn-outline-light btn-sm dropdown-toggle w-100" 
      type="button" 
      data-bs-toggle="dropdown"
    >
      <i class="bi bi-cpu me-2"></i>
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
          <small class="text-muted d-block">{{ model.description }}</small>
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
  { id: 'llama2', name: 'Llama 2', description: 'General purpose' },
  { id: 'codellama', name: 'Code Llama', description: 'Code generation' },
  { id: 'mistral', name: 'Mistral', description: 'Fast & efficient' },
  { id: 'mixtral', name: 'Mixtral', description: 'High quality' }
])

const currentModel = computed(() => chatStore.currentModel)

const selectModel = (modelId) => {
  chatStore.setModel(modelId)
}

onMounted(async () => {
  try {
    const fetchedModels = await fetchModels()
    if (fetchedModels.length > 0) {
      models.value = fetchedModels
    }
  } catch (error) {
    console.error('Failed to load models:', error)
  }
})
</script>

<style scoped>
.model-selector {
  margin-bottom: 1rem;
}

.dropdown-item small {
  font-size: 0.75rem;
}
</style>
