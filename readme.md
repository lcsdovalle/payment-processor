# Payment Processor API

## Overview

External Services is a FastAPI-based project designed to handle file processing, payments, and email notifications efficiently. The API adheres to modern development practices, including API versioning, environment-specific configurations, and extensible architecture using SOLID principles.

## Features 
### File Processing:
- Processes large CSV files with asynchronous support for high performance.
### Payments:
- Integrates multiple payment providers: Stripe, PayPal, and PagBank.
### Email Notifications:
- Supports sending templated emails using Jinja2 templates.
### API Versioning:
- Default API version is /api/v1.
### Authentication:
- Mocked API key-based authentication for testing and development.

## Technologies Used
- FastAPI: High-performance web framework.
- Pydantic: Data validation and settings management.
- Jinja2: Email templating engine.
- Poetry: Dependency management.
- Asyncio: Asynchronous processing.

## Prerequisites
- Python 3.10+
- Poetry (for dependency management)

## Installation

### Clone the repo
```
git clone https://github.com/lcsdovalle/payment-processor.git
cd external_services
```

### Install Dependencies
```poetry install```

### Copy the env
```
cp .env.example .env

```

### Run the projet
```
poetry run uvicorn app.main:app --reload
```

### Example
```
curl --location 'http://127.0.0.1:8000/api/v1/payment/bulk/' \
--form 'file=@"large_file_1000.csv"'
```

### Testing
```
poetry run pytest
```

### Licence
This project is licensed under the MIT License.
