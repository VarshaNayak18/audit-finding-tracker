# AI Audit Finding Tracker — Demo Talking Points

# 1. Project Introduction

Hello everyone.

This project is an AI-powered Audit Finding Tracker designed to analyse and categorise audit/security findings using Large Language Models and intelligent backend workflows.

The system automates audit analysis, improves processing efficiency, and supports scalable deployment using Docker and Redis.

---

# 2. Problem Statement

Manual audit analysis can be time-consuming and inconsistent.

The goal of this project is to:
- automate audit finding categorisation
- improve analysis efficiency
- support scalable backend workflows
- demonstrate AI integration in enterprise systems

---

# 3. Technologies Used

## Backend
- Flask (Python)

## AI Integration
- Groq API
- Prompt engineering

## Database / Storage
- Redis cache
- ChromaDB vector database

## Deployment
- Docker
- Docker Compose

---

# 4. Key Features Demonstrated

## AI Categorisation
The system analyses audit findings and returns:
- category
- confidence score
- reasoning

## Redis Caching
Repeated requests are cached to reduce API calls and improve performance.

## Async Processing
Long-running report generation tasks are handled asynchronously.

## ChromaDB Integration
Embeddings are stored for semantic search and retrieval.

## Prompt QA Testing
Custom scripts evaluate AI response quality.

## Performance Testing
The system was tested for response speed and deployment stability.

---

# 5. API Demonstration Flow

## Step 1
Start Docker containers.

## Step 2
Verify the `/health` endpoint.

## Step 3
Send sample audit findings to `/categorise`.

## Step 4
Show cached responses.

## Step 5
Demonstrate async workflows and report generation.

---

# 6. Challenges Faced

- Docker deployment issues
- Redis connectivity handling
- Environment variable management
- GitHub push protection due to API keys
- Dependency installation timeouts

---

# 7. Learnings

Through this project I learned:
- Docker deployment workflows
- API integration
- backend debugging
- Redis caching
- vector database integration
- prompt engineering
- AI workflow testing

---

# 8. Final Outcome

The project successfully demonstrates an AI-powered backend system capable of audit analysis, caching, async processing, and scalable deployment.

The system is fully prepared for demonstration and future enhancement.

---

# 9. Future Improvements

Possible future enhancements include:
- frontend dashboard integration
- authentication system
- advanced analytics
- cloud deployment
- multi-model AI support

---

# 10. Conclusion

This project provided practical exposure to AI integration, backend development, Docker deployment, testing workflows, and real-world debugging practices.