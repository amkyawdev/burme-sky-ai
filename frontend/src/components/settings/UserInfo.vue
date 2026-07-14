<template>
  <div class="user-info">
    <div class="d-flex align-items-center gap-3">
      <div class="user-avatar">
        <img src="/images/admin.png" alt="User" class="rounded-circle">
      </div>
      <div class="user-details">
        <h6 class="mb-0">User</h6>
        <small class="text-muted">{{ status }}</small>
      </div>
      <div class="ms-auto">
        <div class="status-indicator" :class="statusClass"></div>
      </div>
    </div>
  </div>
</template>

<script setup>
import { computed, ref, onMounted } from 'vue'

const isOnline = ref(false)

onMounted(() => {
  isOnline.value = navigator.onLine
  window.addEventListener('online', () => isOnline.value = true)
  window.addEventListener('offline', () => isOnline.value = false)
})

const status = computed(() => isOnline.value ? 'Online' : 'Offline')
const statusClass = computed(() => isOnline.value ? 'online' : 'offline')
</script>

<style scoped>
.user-info {
  padding: 1rem;
  background-color: rgba(255, 255, 255, 0.05);
  border-radius: var(--border-radius);
}

.user-avatar img {
  width: 48px;
  height: 48px;
  object-fit: cover;
  border: 2px solid var(--primary-color);
}

.user-details h6 {
  color: var(--text-primary);
}

.status-indicator {
  width: 12px;
  height: 12px;
  border-radius: 50%;
}

.status-indicator.online {
  background-color: #28a745;
  box-shadow: 0 0 8px rgba(40, 167, 69, 0.5);
}

.status-indicator.offline {
  background-color: #dc3545;
  box-shadow: 0 0 8px rgba(220, 53, 69, 0.5);
}
</style>
