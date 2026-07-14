<template>
  <div class="about-page container py-4">
    <div class="text-center mb-5">
      <img src="/images/logo.svg" alt="Logo" class="about-logo mb-4">
      <h1 class="display-5 text-white">Burme Sky AI</h1>
      <p class="lead text-muted">Version 1.0.0</p>
    </div>

    <div class="row justify-content-center">
      <div class="col-lg-8">
        <div class="about-card mb-4">
          <h4><i class="bi bi-info-circle me-2"></i>About</h4>
          <p>
            Burme Sky AI is a modern chat application powered by Ollama, 
            enabling you to interact with various AI models locally on your machine.
            Built with Vue 3, FastAPI, and Docker for a seamless experience.
          </p>
        </div>

        <div class="about-card mb-4">
          <h4><i class="bi bi-stack me-2"></i>Technology Stack</h4>
          <div class="tech-grid">
            <div class="tech-item">
              <i class="bi bi-filetype-vue"></i>
              <span>Vue 3</span>
            </div>
            <div class="tech-item">
              <i class="bi bi-lightning-charge"></i>
              <span>Vite</span>
            </div>
            <div class="tech-item">
              <i class="bi bi-filetype-py"></i>
              <span>FastAPI</span>
            </div>
            <div class="tech-item">
              <i class="bi bi-box"></i>
              <span>Docker</span>
            </div>
            <div class="tech-item">
              <i class="bi bi-robot"></i>
              <span>Ollama</span>
            </div>
            <div class="tech-item">
              <i class="bi bi-bootstrap"></i>
              <span>Bootstrap</span>
            </div>
          </div>
        </div>

        <div class="about-card mb-4">
          <h4><i class="bi bi-braces me-2"></i>Features</h4>
          <ul class="feature-list">
            <li><i class="bi bi-check2 me-2"></i>Real-time streaming responses</li>
            <li><i class="bi bi-check2 me-2"></i>Multiple AI model support</li>
            <li><i class="bi bi-check2 me-2"></i>Markdown rendering with syntax highlighting</li>
            <li><i class="bi bi-check2 me-2"></i>Chat history management</li>
            <li><i class="bi bi-check2 me-2"></i>File upload support</li>
            <li><i class="bi bi-check2 me-2"></i>Webhook integration</li>
            <li><i class="bi bi-check2 me-2"></i>Dark mode UI</li>
          </ul>
        </div>

        <div class="about-card mb-4">
          <h4><i class="bi bi-github me-2"></i>Links</h4>
          <div class="d-flex gap-2 flex-wrap">
            <a href="https://github.com" class="btn btn-outline-light">
              <i class="bi bi-github me-2"></i>GitHub
            </a>
            <a href="https://ollama.ai" class="btn btn-outline-light">
              <i class="bi bi-robot me-2"></i>Ollama
            </a>
            <a href="https://vuejs.org" class="btn btn-outline-light">
              <i class="bi bi-filetype-vue me-2"></i>Vue.js
            </a>
          </div>
        </div>

        <div class="text-center text-muted small">
          <p>&copy; 2024 Burme Sky AI. All rights reserved.</p>
          <p>Built with <i class="bi bi-heart-fill text-danger"></i> using modern web technologies</p>
        </div>
      </div>
    </div>
  </div>
</template>

<script setup>
</script>

<style scoped>
.about-page {
  max-width: 900px;
  margin: 0 auto;
}

.about-logo {
  width: 120px;
  height: 120px;
}

.about-card {
  background-color: var(--bg-card);
  border-radius: var(--border-radius);
  padding: 1.5rem;
  border: 1px solid rgba(108, 99, 255, 0.2);
}

.about-card h4 {
  color: var(--text-primary);
  margin-bottom: 1rem;
}

.about-card p {
  color: var(--text-secondary);
  line-height: 1.8;
}

.tech-grid {
  display: grid;
  grid-template-columns: repeat(3, 1fr);
  gap: 1rem;
}

.tech-item {
  display: flex;
  flex-direction: column;
  align-items: center;
  padding: 1rem;
  background-color: rgba(108, 99, 255, 0.1);
  border-radius: 8px;
  transition: all 0.3s ease;
}

.tech-item:hover {
  background-color: rgba(108, 99, 255, 0.2);
  transform: translateY(-3px);
}

.tech-item i {
  font-size: 2rem;
  color: var(--primary-color);
  margin-bottom: 0.5rem;
}

.tech-item span {
  font-size: 0.875rem;
  color: var(--text-primary);
}

.feature-list {
  list-style: none;
  padding: 0;
}

.feature-list li {
  padding: 0.5rem 0;
  color: var(--text-secondary);
}

.feature-list li i {
  color: var(--primary-color);
}

@media (max-width: 576px) {
  .tech-grid {
    grid-template-columns: repeat(2, 1fr);
  }
}
</style>
