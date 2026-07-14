import { ref } from 'vue'

const isSidebarOpen = ref(true)

export const useSidebar = () => {
  const toggleSidebar = () => {
    isSidebarOpen.value = !isSidebarOpen.value
  }

  const openSidebar = () => {
    isSidebarOpen.value = true
  }

  const closeSidebar = () => {
    isSidebarOpen.value = false
  }

  return {
    isSidebarOpen,
    toggleSidebar,
    openSidebar,
    closeSidebar
  }
}
