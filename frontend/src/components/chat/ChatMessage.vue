<template>
  <div class="message" :class="messageClass">
    <div class="message-header" v-if="showHeader">
      <img :src="avatarSrc" :alt="role" class="avatar">
      <span class="message-role">{{ roleLabel }}</span>
      <small class="text-muted ms-auto">{{ formattedTime }}</small>
    </div>
    <div class="message-content" v-html="formattedContent"></div>
  </div>
</template>

<script setup>
import { computed } from 'vue'
import { parseMarkdown } from '@/utils/markdown'

const props = defineProps({
  message: {
    type: Object,
    required: true
  },
  showHeader: {
    type: Boolean,
    default: true
  }
})

const messageClass = computed(() => props.message.role)
const role = computed(() => props.message.role)
const roleLabel = computed(() => role.value === 'user' ? 'You' : 'AI Assistant')
const avatarSrc = computed(() => {
  return role.value === 'user' 
    ? '/images/admin.png' 
    : '/images/bot.svg'
})

const formattedContent = computed(() => {
  if (!props.message.content) return ''
  
  // Check if content contains HTML (from CLI formatter)
  if (props.message.content.includes('<')) {
    return props.message.content
  }
  
  return parseMarkdown(props.message.content)
})

const formattedTime = computed(() => {
  if (!props.message.timestamp) return ''
  return new Date(props.message.timestamp).toLocaleTimeString()
})
</script>

<style scoped>
.message {
  max-width: 70%;
  margin-bottom: 1rem;
  padding: 1rem;
  border-radius: var(--border-radius);
  animation: fadeIn 0.3s ease;
}

.message.user {
  background: linear-gradient(135deg, var(--primary-color), var(--secondary-color));
  color: white;
  margin-left: auto;
  border-bottom-right-radius: 4px;
}

.message.assistant {
  background-color: var(--bg-card);
  border: 1px solid rgba(108, 99, 255, 0.2);
  margin-right: auto;
  border-bottom-left-radius: 4px;
}

.message-header {
  display: flex;
  align-items: center;
  gap: 0.5rem;
  margin-bottom: 0.5rem;
}

.avatar {
  width: 24px;
  height: 24px;
  border-radius: 50%;
  object-fit: cover;
}

.message-role {
  font-weight: 600;
  font-size: 0.875rem;
}

.message-content {
  line-height: 1.6;
}

.message-content :deep(p) {
  margin-bottom: 0.5rem;
}

.message-content :deep(p:last-child) {
  margin-bottom: 0;
}

.message-content :deep(pre) {
  background-color: #0f0f23;
  padding: 1rem;
  border-radius: 8px;
  overflow-x: auto;
  margin: 0.5rem 0;
}

.message-content :deep(code) {
  font-family: 'Fira Code', 'Consolas', monospace;
  font-size: 0.9em;
}

.message-content :deep(pre code) {
  background: none;
  padding: 0;
}

.message-content :deep(ul),
.message-content :deep(ol) {
  margin: 0.5rem 0;
  padding-left: 1.5rem;
}

.message-content :deep(blockquote) {
  border-left: 3px solid var(--primary-color);
  padding-left: 1rem;
  margin: 0.5rem 0;
  color: var(--text-secondary);
}

@keyframes fadeIn {
  from { opacity: 0; transform: translateY(10px); }
  to { opacity: 1; transform: translateY(0); }
}
</style>
