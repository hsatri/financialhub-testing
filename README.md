# Budget Management Web App Tests

A comprehensive test suite for the Budget Management Web Application built with Django (backend) and React (frontend).

Original project repository: [FinancialHub Django](https://github.com/fun-projects-hub/financialhub-django/tree/develop)

## Overview

This test suite provides automated API tests for the Budget Management Web App, covering authentication, budget operations, and transaction management. The tests are designed to work with the [FinancialHub Django](https://github.com/fun-projects-hub/financialhub-django/tree/develop) project.

## Requirements

```
pytest
requests
```

Install dependencies with:

```
pip install -r requirements.txt
```

## Test Structure

- **conftest.py**: Common fixtures and test setup
- **test_auth.py**: Authentication tests (login, registration, token refresh)
- **test_budget.py**: Budget CRUD operation tests
- **test_transaction.py**: Transaction management tests

## Running Tests

Run all tests:

```
pytest
```

Run specific test file:

```
pytest test_auth.py
```

Run with verbose output:

```
pytest -v
```

## Test Environment

The tests are configured to run against a local development server:

- **Base URL**: http://localhost:5173
- **API Base**: http://localhost:8000/api

## Test Data

The tests use predefined test data for consistent testing:

- **Test User**: testuser@example.com / SecurePass123
- **Test Budget**: Monthly Expenses with amount 5000
- **Test Transaction**: Grocery Shopping with amount 150

## Features Tested

- User registration and authentication
- JWT token management
- Budget creation, retrieval, updating, and deletion
- Transaction management within budgets
- Input validation and error handling
- Security features (SQL injection prevention)

## Test Design

Tests are designed to be:
- Independent: Each test can run in isolation
- Comprehensive: Covering both positive and negative scenarios
- Efficient: Using fixtures for common setup and teardown operations
- Clean: Tests clean up after themselves to ensure repeatability