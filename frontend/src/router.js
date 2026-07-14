import { createRouter, createWebHistory } from 'vue-router'
import GetStart from './views/GetStart.vue'
import ChatPage from './views/ChatPage.vue'
import Setting from './views/Setting.vue'
import About from './views/About.vue'

const routes = [
  { path: '/', component: GetStart },
  { path: '/chat', component: ChatPage },
  { path: '/settings', component: Setting },
  { path: '/about', component: About }
]

const router = createRouter({
  history: createWebHistory(),
  routes
})

export default router
