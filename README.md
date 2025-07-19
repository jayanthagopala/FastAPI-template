# FastAPI Production Template 🚀

A production-ready FastAPI project template with modern Python development practices. Use this template to quickly bootstrap new FastAPI projects with all the essential components already configured.

## 🎯 Template Overview

This template provides a solid foundation for building scalable FastAPI applications with industry best practices built-in. Simply clone, customize, and start building your API. 

## ✨ What's Included

### 🏗️ **Project Architecture**
- Clean, modular project structure following Python packaging standards
- Separation of concerns with dedicated layers (API, services, models, schemas)
- Dependency injection patterns with FastAPI's `Depends()`
- Async/await implementation throughout the application

### 🔧 **Development Environment**
- **UV** for ultra-fast Python dependency management and project setup
- **Pre-commit hooks** with code formatting, linting, and security checks
- **Docker & Docker Compose** for containerized development and deployment
- **Environment-based configuration** with Pydantic Settings

### 📊 **Database & ORM**
- **SQLAlchemy 2.0+** with async support
- **Alembic** database migrations
- **PostgreSQL** with proper connection pooling
- UUID primary keys and soft delete patterns

### 🧪 **Testing Strategy**
- **Pytest** with async support and comprehensive test coverage (>90%)
- **Factory Boy** for test data generation
- Integration tests for API endpoints
- **pytest-cov** for coverage reporting
- Separate test database configuration

### 🛡️ **Security Implementation**
- **JWT authentication** with proper token handling
- **OAuth2 with scopes** for authorization
- **bcrypt** password hashing
- **Rate limiting** and CORS configuration
- **Input validation** and sanitization with Pydantic
- **Security headers** middleware

### 📈 **Code Quality & Standards**
- **Black** code formatting
- **isort** import sorting  
- **Ruff/Flake8** linting
- **mypy** static type checking
- **bandit** security linting
- **100% type hints** coverage

### 🚀 **CI/CD Pipeline**
- **GitHub Actions** workflows for testing, building, and deployment
- Automated code quality checks and security scanning
- **Docker image building** and registry push
- **Automated deployment** with rollback capabilities
- **Dependency vulnerability scanning**



### 📊 **Monitoring & Observability**
- **Structured logging** with JSON format and correlation IDs
- **Health check endpoints** for load balancer integration
- **Prometheus metrics** integration ready
- **Error tracking** setup (Sentry integration ready)
- **Performance monitoring** with request/response timing

### 📚 **API Documentation**
- **OpenAPI/Swagger** automatic documentation
- **API versioning** (v1, v2 support)
- **Comprehensive endpoint documentation** with examples
- **Request/response models** with validation

## 🛠️ **Tech Stack**

- **Python**: 3.12+
- **Framework**: FastAPI 0.100+
- **Database**: PostgreSQL with SQLAlchemy 2.0+
- **Authentication**: JWT with OAuth2
- **Testing**: pytest, httpx, factory-boy
- **Code Quality**: black, ruff, mypy, bandit
- **Containerization**: Docker & Docker Compose
- **CI/CD**: GitHub Actions
- **Monitoring**: Structured logging, health checks

## 🚀 **Quick Start**

### Using this Template

1. **Use as GitHub Template**: Click "Use this template" button on GitHub
2. **Or clone directly**:
   ```bash
   git clone <your-new-repo-url>
   cd your-project-name
   ```

3. **Customize for your project**:
   - Update `pyproject.toml` with your project details
   - Modify environment variables in `.env.example`
   - Update API endpoints in `app/api/`
   - Customize database models in `app/models/`

## 🛠️ **Development Setup**

```bash
# Install UV (if not already installed)
curl -LsSf https://astral.sh/uv/install.sh | sh

# Create virtual environment and install dependencies
uv sync

# Set up pre-commit hooks
uv run pre-commit install

# Copy and configure environment variables
cp .env.example .env
# Edit .env with your configuration

# Start development environment
docker-compose up -d

# Run database migrations
uv run alembic upgrade head

# Start the development server
uv run uvicorn app.main:app --reload
```

Your API will be available at `http://localhost:8000` with docs at `http://localhost:8000/docs`.

## 📖 **Documentation**

- [Project Setup Guide](docs/setup.md)
- [Development Workflow](docs/development.md)
- [Testing Strategy](docs/testing.md)
- [Deployment Guide](docs/deployment.md)
- [API Documentation](docs/api.md)
- [Contributing Guidelines](CONTRIBUTING.md)

## 🔧 **Customization**

### Project Structure
```
your-project/
├── app/
│   ├── api/v1/          # API routes - customize your endpoints here
│   ├── core/            # Configuration and security
│   ├── models/          # Database models - define your data structures
│   ├── schemas/         # Pydantic models - API request/response schemas
│   └── services/        # Business logic - implement your core functionality
├── tests/               # Test suite - add your tests here
├── alembic/            # Database migrations
└── docker-compose.yml   # Development environment
```

### Common Customizations
- **Database Models**: Add your models in `app/models/`
- **API Endpoints**: Create new routes in `app/api/v1/`
- **Business Logic**: Implement services in `app/services/`
- **Configuration**: Update settings in `app/core/config.py`
- **Authentication**: Customize JWT settings in `app/core/security.py`

## 🧪 **Testing & Quality**

```bash
# Run tests
uv run pytest

# Run tests with coverage
uv run pytest --cov=app

# Code formatting and linting
uv run black .
uv run ruff check .
uv run mypy .
```

## 🚀 **Deployment**

### Docker Production Build
```bash
docker build -t your-app-name .
docker run -p 8000:8000 your-app-name
```

### Environment Variables
Copy `.env.example` to `.env` and configure:
- `DATABASE_URL`: Your PostgreSQL connection string
- `SECRET_KEY`: JWT secret key
- `ENVIRONMENT`: `development`, `staging`, or `production`

## 📄 **License**

MIT License - use this template freely for any project.

---

**Ready to build something amazing? Start with this template and focus on your business logic!** 🚀