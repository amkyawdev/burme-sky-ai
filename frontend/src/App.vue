<template>
  <div class="app-container">
    <Sidebar />
    <div class="main-content" :class="{ 'full-width': !sidebarState.isOpen }">
      <router-view />
    </div>
  </div>
</template>

<script setup>
import { useSidebar } from './composables/useSidebar'
import Sidebar from './components/common/Sidebar.vue'

const { sidebarState } = useSidebar()
</script>

<style scoped>
.app-container {
  display: flex;
  min-height: 100vh;
}

.main-content {
  flex: 1;
  margin-left: 220px;
  display: flex;
  flex-direction: column;
  min-height: 100vh;
  transition: margin-left 0.3s ease;
}

.full-width {
  margin-left: 0;
}

@media (max-width: 768px) {
  .main-content {
    margin-left: 0;
  }
}
</style>
