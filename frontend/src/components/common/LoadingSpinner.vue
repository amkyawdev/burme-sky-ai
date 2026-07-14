<template>
  <div class="loading-spinner-container" :class="{ 'inline': inline }">
    <div class="spinner-wrapper">
      <div class="spinner"></div>
      <p v-if="text" class="mt-2 text-muted small">{{ text }}</p>
    </div>
  </div>
</template>

<script setup>
defineProps({
  text: {
    type: String,
    default: ''
  },
  inline: {
    type: Boolean,
    default: false
  }
})
</script>

<style scoped>
.loading-spinner-container {
  display: flex;
  justify-content: center;
  align-items: center;
  padding: 2rem;
}

.loading-spinner-container.inline {
  padding: 0.5rem;
}

.spinner-wrapper {
  text-align: center;
}

.spinner {
  width: 40px;
  height: 40px;
  border: 3px solid rgba(108, 99, 255, 0.2);
  border-top-color: var(--primary-color);
  border-radius: 50%;
  animation: spin 0.8s linear infinite;
}

@keyframes spin {
  to { transform: rotate(360deg); }
}
</style>
