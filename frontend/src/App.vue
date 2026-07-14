<template>
  <div class="app-container">
    <Sidebar />
    <div class="main-content" :class="{ 'full-width': !isSidebarOpen }">
      <Header v-if="showHeader" />
      <router-view />
    </div>
  </div>
</template>

<script setup>
import { computed } from 'vue'
import { useRoute } from 'vue-router'
import Sidebar from './components/common/Sidebar.vue'
import Header from './components/common/Header.vue'
import { useSidebar } from './composables/useSidebar'

const route = useRoute()
const { isSidebarOpen } = useSidebar()
const showHeader = computed(() => route.path === '/chat')
</script>

<style scoped>
.app-container {
  display: flex;
  min-height: 100vh;
}

.main-content {
  flex: 1;
  margin-left: 280px;
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
