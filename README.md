# Burme Sky AI

A modern AI chat application powered by Ollama, built with Vue 3, FastAPI, and Docker.

![Burme Sky AI](frontend/public/images/logo.svg)

## Features

- 💬 **Real-time Chat** - Streaming responses from AI models
- 🤖 **Multiple Models** - Switch between different Ollama models
- 📝 **Markdown Support** - Beautiful code highlighting and formatting
- 💾 **Chat History** - Save and manage your conversations
- 📎 **File Upload** - Upload files for context
- 🔗 **Webhook Integration** - Get notified via webhooks
- 🌙 **Dark Mode** - Easy on the eyes UI
- 🐳 **Docker Ready** - One-command deployment

## Quick Start

### Prerequisites

- Node.js 18+
- Python 3.11+
- Docker & Docker Compose
- Ollama installed locally

### Using Docker Compose (Recommended)

```bash
# Clone the repository
git clone <your-repo-url>
cd burme-sky-ai

# Copy environment file
cp backend/.env.example backend/.env
# Edit backend/.env and add your OLLAMA_API_KEY

# Start all services
docker-compose up -d

# View logs
docker-compose logs -f
```

The app will be available at:
- Frontend: http://localhost:5173
- Backend API: http://localhost:8000

### Manual Setup

#### Backend

```bash
cd backend

# Create virtual environment
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate

# Install dependencies
pip install -r requirements.txt

# Run the server
uvicorn app.main:app --reload --port 8000
```

#### Frontend

```bash
cd frontend

# Install dependencies
npm install

# Run the dev server
npm run dev
```

## Configuration

### Environment Variables

**Backend (.env)**
```env
OLLAMA_API_KEY=your_api_key
OLLAMA_URL=http://localhost:11434
HOST=0.0.0.0
PORT=8000
```

### Ollama Setup

Make sure Ollama is running with your desired models:

```bash
# Pull models
ollama pull llama2
ollama pull codellama
ollama pull mistral

# Check running models
ollama list
```

## Tech Stack

### Frontend
- Vue 3 (Composition API)
- Vite
- Pinia (State Management)
- Vue Router
- Bootstrap 5
- Highlight.js (Code Highlighting)

### Backend
- FastAPI
- Uvicorn
- httpx
- Pydantic
- Ollama SDK

### DevOps
- Docker
- Docker Compose
- Vercel (Deployments)

## API Endpoints

### Chat
- `POST /api/chat/stream` - Stream chat responses
- `POST /api/chat` - Non-streaming chat

### History
- `GET /api/history` - Get chat history
- `POST /api/history` - Add to history
- `DELETE /api/history/{id}` - Delete history item
- `DELETE /api/history` - Clear all history

### Models
- `GET /api/models` - List available models
- `GET /api/models/{id}` - Get model info

## Development

### Project Structure

```
burme-sky-ai/
├── frontend/           # Vue 3 + Vite frontend
│   ├── src/
│   │   ├── components/  # Vue components
│   │   ├── views/        # Page views
│   │   ├── stores/       # Pinia stores
│   │   ├── composables/  # Vue composables
│   │   └── utils/        # Utility functions
│   └── public/           # Static assets
├── backend/            # FastAPI backend
│   ├── app/
│   │   ├── routes/      # API routes
│   │   ├── services/    # Business logic
│   │   ├── models/      # Pydantic models
│   │   └── utils/       # Utilities
│   └── Dockerfile
├── docker-compose.yml  # Docker orchestration
└── README.md
```

### Running Tests

```bash
# Backend
cd backend
pytest

# Frontend
cd frontend
npm test
```

## Deployment

### Vercel

The project supports Vercel deployment for both frontend and backend.

1. Connect your GitHub repository to Vercel
2. Configure environment variables
3. Deploy!

### Docker

```bash
# Build images
docker build -t burme-sky-ai-backend ./backend
docker build -t burme-sky-ai-frontend ./frontend

# Run containers
docker run -d -p 8000:8000 --name backend burme-sky-ai-backend
docker run -d -p 5173:5173 --name frontend burme-sky-ai-frontend
```

## Contributing

1. Fork the repository
2. Create a feature branch (`git checkout -b feature/amazing-feature`)
3. Commit your changes (`git commit -m 'Add amazing feature'`)
4. Push to the branch (`git push origin feature/amazing-feature`)
5. Open a Pull Request

## License

This project is licensed under the MIT License.

## Acknowledgments

- [Ollama](https://ollama.ai/) - For the amazing local AI runtime
- [Vue.js](https://vuejs.org/) - The progressive JavaScript framework
- [FastAPI](https://fastapi.tiangolo.com/) - The modern Python web framework
