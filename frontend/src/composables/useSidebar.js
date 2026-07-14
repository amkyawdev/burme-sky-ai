import { reactive } from 'vue'

const state = reactive({
  isOpen: false
})

export function useSidebar() {
  const toggleSidebar = () => {
    state.isOpen = !state.isOpen
  }

  const openSidebar = () => {
    state.isOpen = true
  }

  const closeSidebar = () => {
    state.isOpen = false
  }

  return {
    sidebarState: state,
    toggleSidebar,
    openSidebar,
    closeSidebar
  }
}
