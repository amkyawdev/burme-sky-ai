<template>
  <div class="settings-page container py-4">
    <div class="row justify-content-center">
      <div class="col-lg-8">
        <h2 class="text-white mb-4">
          <i class="bi bi-gear me-2"></i>Settings
        </h2>

        <div class="settings-card mb-4">
          <h5 class="card-title mb-3">
            <i class="bi bi-plug me-2"></i>API Configuration
          </h5>
          <div class="mb-3">
            <label class="form-label">Backend API URL</label>
            <input 
              type="text" 
              class="form-control" 
              v-model="apiUrl"
              placeholder="http://localhost:8000/api"
            />
            <small class="text-muted">The URL of your Ollama backend server</small>
          </div>
        </div>

        <div class="settings-card mb-4">
          <h5 class="card-title mb-3">
            <i class="bi bi-webhook me-2"></i>Webhook Integration
          </h5>
          <div class="mb-3">
            <label class="form-label">Webhook URL (Optional)</label>
            <input 
              type="url" 
              class="form-control" 
              v-model="webhookUrl"
              placeholder="https://your-webhook.com/endpoint"
            />
            <small class="text-muted">Receive chat notifications via webhook</small>
          </div>
        </div>

        <div class="settings-card mb-4">
          <h5 class="card-title mb-3">
            <i class="bi bi-palette me-2"></i>Appearance
          </h5>
          <div class="row">
            <div class="col-md-6 mb-3">
              <label class="form-label">Theme</label>
              <select class="form-select" v-model="theme">
                <option value="dark">Dark</option>
                <option value="light">Light</option>
                <option value="auto">Auto (System)</option>
              </select>
            </div>
            <div class="col-md-6 mb-3">
              <label class="form-label">Font Size</label>
              <select class="form-select" v-model="fontSize">
                <option value="small">Small</option>
                <option value="medium">Medium</option>
                <option value="large">Large</option>
              </select>
            </div>
          </div>
        </div>

        <div class="settings-card mb-4">
          <h5 class="card-title mb-3">
            <i class="bi bi-database me-2"></i>Data Management
          </h5>
          <div class="d-flex gap-2">
            <button class="btn btn-outline-warning" @click="clearHistory">
              <i class="bi bi-trash3 me-2"></i>Clear History
            </button>
            <button class="btn btn-outline-info" @click="exportData">
              <i class="bi bi-download me-2"></i>Export Data
            </button>
          </div>
        </div>

        <div class="d-flex gap-2">
          <button class="btn btn-primary" @click="saveSettings">
            <i class="bi bi-check2 me-2"></i>Save Settings
          </button>
          <button class="btn btn-secondary" @click="resetSettings">
            <i class="bi bi-arrow-counterclockwise me-2"></i>Reset
          </button>
        </div>
      </div>
    </div>

    <SettingsModal />
  </div>
</template>

<script setup>
import { ref } from 'vue'
import { useSettingsStore } from '@/stores/settingsStore'
import { useChatStore } from '@/stores/chatStore'
import SettingsModal from '@/components/settings/SettingsModal.vue'

const settingsStore = useSettingsStore()
const chatStore = useChatStore()

const apiUrl = ref(settingsStore.apiUrl)
const webhookUrl = ref(settingsStore.webhookUrl)
const theme = ref(settingsStore.theme)
const fontSize = ref(settingsStore.fontSize)

const saveSettings = () => {
  settingsStore.setApiUrl(apiUrl.value)
  settingsStore.setWebhookUrl(webhookUrl.value)
  settingsStore.setTheme(theme.value)
  settingsStore.setFontSize(fontSize.value)
  
  // Apply font size
  document.documentElement.style.setProperty('--font-size-base', 
    fontSize.value === 'small' ? '14px' : 
    fontSize.value === 'large' ? '18px' : '16px'
  )
  
  alert('Settings saved successfully!')
}

const resetSettings = () => {
  apiUrl.value = '/api'
  webhookUrl.value = ''
  theme.value = 'dark'
  fontSize.value = 'medium'
}

const clearHistory = () => {
  if (confirm('Are you sure you want to clear all chat history?')) {
    chatStore.clearHistory()
    chatStore.clearMessages()
    alert('History cleared!')
  }
}

const exportData = () => {
  const data = {
    history: chatStore.history,
    messages: chatStore.messages,
    settings: {
      apiUrl: settingsStore.apiUrl,
      webhookUrl: settingsStore.webhookUrl,
      theme: settingsStore.theme,
      fontSize: settingsStore.fontSize
    },
    exportedAt: new Date().toISOString()
  }
  
  const blob = new Blob([JSON.stringify(data, null, 2)], { type: 'application/json' })
  const url = URL.createObjectURL(blob)
  const a = document.createElement('a')
  a.href = url
  a.download = `burme-sky-ai-export-${Date.now()}.json`
  a.click()
  URL.revokeObjectURL(url)
}
</script>

<style scoped>
.settings-page {
  max-width: 900px;
  margin: 0 auto;
}

.settings-card {
  background-color: var(--bg-card);
  border-radius: var(--border-radius);
  padding: 1.5rem;
  border: 1px solid rgba(108, 99, 255, 0.2);
}

.card-title {
  color: var(--text-primary);
}

.form-label {
  color: var(--text-primary);
  font-weight: 500;
}

.form-control,
.form-select {
  background-color: rgba(255, 255, 255, 0.05);
  border-color: rgba(108, 99, 255, 0.3);
  color: var(--text-primary);
}

.form-control:focus,
.form-select:focus {
  background-color: rgba(255, 255, 255, 0.1);
  border-color: var(--primary-color);
  color: var(--text-primary);
}

.btn-primary {
  background: linear-gradient(135deg, var(--primary-color), var(--secondary-color));
  border: none;
}

.btn-primary:hover {
  opacity: 0.9;
}
</style>
