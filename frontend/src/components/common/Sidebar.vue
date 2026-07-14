<template>
  <aside v-if="isSidebarOpen" class="sidebar">
    <div class="sidebar-header mb-2">
      <img src="/images/logo.svg" alt="Logo" class="img-fluid" style="max-width: 50px;">
      <h6 class="mt-1 text-white">Burme Sky AI</h6>
    </div>

    <NewChat />
    
    <div class="flex-grow-1 overflow-auto my-2">
      <ModelOptions />
      <HistoryList />
    </div>

    <div class="sidebar-footer mt-auto pt-2 border-top">
      <router-link to="/settings" class="btn btn-outline-light btn-sm w-100 mb-1">
        <i class="bi bi-gear me-1"></i>Settings
      </router-link>
      <router-link to="/about" class="btn btn-outline-light btn-sm w-100">
        <i class="bi bi-info-circle me-1"></i>About
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
  width: 220px;
  background: linear-gradient(180deg, #16213e 0%, #1a1a2e 100%);
  border-right: 1px solid rgba(108, 99, 255, 0.2);
  height: 100vh;
  position: fixed;
  left: 0;
  top: 0;
  padding: 0.5rem;
  display: flex;
  flex-direction: column;
  z-index: 100;
  transition: transform 0.3s ease, opacity 0.3s ease;
}

.sidebar-header {
  text-align: center;
  padding: 0.5rem;
}

.sidebar-footer {
  border-color: rgba(108, 99, 255, 0.2) !important;
}
</style>
