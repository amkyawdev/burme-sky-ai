<template>
  <div class="get-start-container">
    <div class="text-center">
      <img src="/images/logo.svg" alt="Burme Sky AI" class="get-start-logo">
      <h1 class="display-4 text-white mb-3">Welcome to Burme Sky AI</h1>
      <p class="lead text-muted mb-5">
        Your intelligent AI assistant powered by Ollama. Start chatting to explore the possibilities.
      </p>
      
      <div class="features-grid mb-5">
        <div class="feature-card" v-for="feature in features" :key="feature.title">
          <i :class="feature.icon" class="feature-icon"></i>
          <h5>{{ feature.title }}</h5>
          <p class="text-muted small">{{ feature.description }}</p>
        </div>
      </div>

      <router-link to="/chat" class="btn btn-primary btn-lg px-5 py-3">
        <i class="bi bi-chat-dots me-2"></i>
        Start Chatting
      </router-link>

      <div class="mt-4">
        <router-link to="/about" class="text-muted me-3">
          <small>Learn more</small>
        </router-link>
        <router-link to="/settings" class="text-muted">
          <small>Configure</small>
        </router-link>
      </div>
    </div>
  </div>
</template>

<script setup>
const features = [
  {
    icon: 'bi bi-lightning-charge',
    title: 'Fast Responses',
    description: 'Real-time streaming responses'
  },
  {
    icon: 'bi bi-robot',
    title: 'Multiple Models',
    description: 'Switch between AI models'
  },
  {
    icon: 'bi bi-shield-check',
    title: 'Secure',
    description: 'Your data stays private'
  },
  {
    icon: 'bi bi-code',
    title: 'Code Support',
    description: 'Syntax highlighting for code'
  }
]
</script>

<style scoped>
.get-start-container {
  display: flex;
  flex-direction: column;
  align-items: center;
  justify-content: center;
  min-height: calc(100vh - 60px);
  text-align: center;
  padding: 2rem;
  background: radial-gradient(ellipse at top, rgba(108, 99, 255, 0.1) 0%, transparent 50%);
}

.get-start-logo {
  width: 150px;
  height: 150px;
  margin-bottom: 2rem;
  animation: float 3s ease-in-out infinite;
}

@keyframes float {
  0%, 100% { transform: translateY(0); }
  50% { transform: translateY(-15px); }
}

.features-grid {
  display: grid;
  grid-template-columns: repeat(4, 1fr);
  gap: 1.5rem;
  max-width: 900px;
}

.feature-card {
  padding: 1.5rem;
  background-color: var(--bg-card);
  border-radius: var(--border-radius);
  border: 1px solid rgba(108, 99, 255, 0.2);
  transition: all 0.3s ease;
}

.feature-card:hover {
  transform: translateY(-5px);
  border-color: var(--primary-color);
  box-shadow: 0 10px 30px rgba(108, 99, 255, 0.2);
}

.feature-icon {
  font-size: 2.5rem;
  color: var(--primary-color);
  margin-bottom: 1rem;
}

.feature-card h5 {
  color: var(--text-primary);
  margin-bottom: 0.5rem;
}

.btn-primary {
  background: linear-gradient(135deg, var(--primary-color), var(--secondary-color));
  border: none;
  font-weight: 600;
  transition: all 0.3s ease;
}

.btn-primary:hover {
  transform: scale(1.05);
  box-shadow: 0 10px 30px rgba(108, 99, 255, 0.4);
}

@media (max-width: 768px) {
  .features-grid {
    grid-template-columns: repeat(2, 1fr);
  }
}

@media (max-width: 480px) {
  .features-grid {
    grid-template-columns: 1fr;
  }
}
</style>
