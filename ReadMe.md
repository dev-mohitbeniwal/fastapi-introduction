# FastAPI POC

This project demonstrates the capabilities and features of FastAPI.

# Introduction

- FastAPI is a powerful, easiy to use Python web-framework. Built with **asynchronous support** from the ground up, it offers high perfromance compared to other web-frameworks.
- FastAPI takes advantage of Python's type hints to provide robust way to define APIs.
- It includes automatic data validation, serialization, and good API documentation out of the box.

# Advantages of FastAPI

1. High Performance: Fastest Python framework (Built on uvicorn and starlette)
2. Rapid development (Pydantic handles the data validation using typehints and reduces boilerplate code)
3. Automatic API Docs (Generate docs with OpenAPI standard)
4. Robust Data Validation (Reduces the run-time errors)
5. Asynchronous Support (Highly efficient and scalable application)

## Why FastAPI is actually fast?

- **Uvicorn:** Since it is built on top of **Uvicorn** which is a lightning-fast "ASGI" (Async Server Gateway Interface) as an interface between async-capable web servers, frameworks and applications. (Provides High-concurrency capability)
- **Starlette:** is a lightweight ASGI framework/toolkit. FastAPI is built on top of Starlette for the web parts. This includes: routing based paths, handling HTTP methods, query/path parameters, headers, cookies, request bodies, HTTP response.
- **Pydantic:** is a data validation library that allows data parsing using Python type annotations. (Python 3.6+). FastAPI uses Pydantic for data validation, serialization (to/from JSON) and model documentation.

# Key Features of FastAPI

1. Path Parameters, Query Parameters and Reques Body: easily define these in the route functions and FastAPI will validate, parse and document them.
2. Handling Errors: FastAPI allows us to handle errors in very pythonic way, and it will automatically generate error responses for us. (raise HTTPExceptions anywhere and response will be returned to the client)
3. Dependency Injection (easy to use, allows better modularity and testing of the application)
4. Security and Authentication:
5. Serialization and Models (Pydantic again)

## More on Security and Authentication

FastAPI provides server built-in tools and practices for securing the APIs.

This supports: HTTP Basic Authentication, OAuth2, JWT tokens, secure password hashing, CORS, etc.

### [Next Topic: Environment Setup](/docs/Environment_Setup.md)
