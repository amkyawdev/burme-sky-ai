<template>
  <aside v-if="isSidebarOpen" class="sidebar">
    <div class="sidebar-header mb-4">
      <img src="/images/logo.svg" alt="Logo" class="img-fluid" style="max-width: 80px;">
      <h5 class="mt-2 text-white">Burme Sky AI</h5>
    </div>

    <NewChat />
    
    <div class="flex-grow-1 overflow-auto my-3">
      <ModelOptions />
      <HistoryList />
    </div>

    <div class="sidebar-footer mt-auto pt-3 border-top">
      <router-link to="/settings" class="btn btn-outline-light w-100 mb-2">
        <i class="bi bi-gear me-2"></i>Settings
      </router-link>
      <router-link to="/about" class="btn btn-outline-light w-100">
        <i class="bi bi-info-circle me-2"></i>About
      </router-link>
    </div>
  </aside>
</template>

<script setup>
import { useSidebar } from '@/composables/useSidebar'
import NewChat from '@/components/sidebar/NewChat.vue'
import HistoryList from '@/components/sidebar/HistoryList.vue'
import ModelOptions from '@/components/sidebar/ModelOptions.vue'

const { isSidebarOpen } = useSidebar()
</script>

<style scoped>
.sidebar {
  width: 280px;
  background: linear-gradient(180deg, #16213e 0%, #1a1a2e 100%);
  border-right: 1px solid rgba(108, 99, 255, 0.2);
  height: 100vh;
  position: fixed;
  left: 0;
  top: 0;
  padding: 1rem;
  display: flex;
  flex-direction: column;
  z-index: 100;
  transition: transform 0.3s ease, opacity 0.3s ease;
}

.sidebar-header {
  text-align: center;
  padding: 1rem;
}

.sidebar-footer {
  border-color: rgba(108, 99, 255, 0.2) !important;
}
</style>
