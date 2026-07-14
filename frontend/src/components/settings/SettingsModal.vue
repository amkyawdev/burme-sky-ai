<template>
  <div class="modal fade" id="settingsModal" tabindex="-1" aria-hidden="true">
    <div class="modal-dialog modal-dialog-centered">
      <div class="modal-content">
        <div class="modal-header">
          <h5 class="modal-title">
            <i class="bi bi-gear me-2"></i>Settings
          </h5>
          <button type="button" class="btn-close btn-close-white" data-bs-dismiss="modal"></button>
        </div>
        <div class="modal-body">
          <div class="mb-4">
            <label class="form-label">API URL</label>
            <input 
              type="text" 
              class="form-control" 
              v-model="apiUrl"
              placeholder="http://localhost:8000/api"
            />
            <small class="text-muted">Backend API endpoint</small>
          </div>

          <div class="mb-4">
            <label class="form-label">Webhook URL (Optional)</label>
            <input 
              type="url" 
              class="form-control" 
              v-model="webhookUrl"
              placeholder="https://your-webhook.com/endpoint"
            />
            <small class="text-muted">Receive notifications via webhook</small>
          </div>

          <div class="mb-4">
            <label class="form-label">Theme</label>
            <select class="form-select" v-model="theme">
              <option value="dark">Dark</option>
              <option value="light">Light</option>
              <option value="auto">Auto</option>
            </select>
          </div>

          <div class="mb-4">
            <label class="form-label">Font Size</label>
            <select class="form-select" v-model="fontSize">
              <option value="small">Small</option>
              <option value="medium">Medium</option>
              <option value="large">Large</option>
            </select>
          </div>
        </div>
        <div class="modal-footer">
          <button type="button" class="btn btn-secondary" data-bs-dismiss="modal">Cancel</button>
          <button type="button" class="btn btn-primary" @click="saveSettings">Save Changes</button>
        </div>
      </div>
    </div>
  </div>
</template>

<script setup>
import { ref, watch } from 'vue'
import { useSettingsStore } from '@/stores/settingsStore'

const settingsStore = useSettingsStore()

const apiUrl = ref(settingsStore.apiUrl)
const webhookUrl = ref(settingsStore.webhookUrl)
const theme = ref(settingsStore.theme)
const fontSize = ref(settingsStore.fontSize)

watch(() => settingsStore.apiUrl, (val) => apiUrl.value = val)
watch(() => settingsStore.webhookUrl, (val) => webhookUrl.value = val)
watch(() => settingsStore.theme, (val) => theme.value = val)
watch(() => settingsStore.fontSize, (val) => fontSize.value = val)

const saveSettings = () => {
  settingsStore.setApiUrl(apiUrl.value)
  settingsStore.setWebhookUrl(webhookUrl.value)
  settingsStore.setTheme(theme.value)
  settingsStore.setFontSize(fontSize.value)
  
  // Close modal using Bootstrap
  const modalEl = document.getElementById('settingsModal')
  const modal = window.bootstrap?.Modal.getInstance(modalEl)
  if (modal) modal.hide()
}
</script>

<style scoped>
.modal-content {
  background-color: var(--bg-card);
  color: var(--text-primary);
}

.modal-header {
  border-bottom-color: rgba(108, 99, 255, 0.2);
}

.modal-footer {
  border-top-color: rgba(108, 99, 255, 0.2);
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

.form-label {
  color: var(--text-primary);
  font-weight: 500;
}
</style>
