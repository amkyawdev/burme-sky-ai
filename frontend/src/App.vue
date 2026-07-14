<template>
  <div class="app-container">
    <Sidebar v-if="showSidebar" />
    <div class="main-content" :class="{ 'full-width': !showSidebar }">
      <Header v-if="showSidebar" />
      <router-view />
    </div>
  </div>
</template>

<script setup>
import { computed } from 'vue'
import { useRoute } from 'vue-router'
import Sidebar from './components/common/Sidebar.vue'
import Header from './components/common/Header.vue'

const route = useRoute()
const showSidebar = computed(() => route.path !== '/')
</script>

<style scoped>
.app-container {
  display: flex;
  min-height: 100vh;
}

.full-width {
  width: 100%;
}
</style>
