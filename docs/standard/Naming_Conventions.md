# FastAPI Naming Conventions

In our ongoing effort to maintain clarity and consistency in our FastAPI projects, we adhere to certain naming conventions. This document outlines these conventions, which should guide our code writing practices.

> Note: Some of the naming conventions are used in the documentation generation, such as route function names. You can try chaging to camel case you will see the difference.

## Variable Names

-   Variables should be named in `snake_case`.
-   The variable names should be descriptive and not abbreviated. For example, we use `item_id` rather than `id`.

## Function Names

-   Function names should be written in `snake_case`.
-   Function names should start with a verb and describe what the function does. For example, `get_items` or `update_user`.

## Class Names

-   Class names should follow the `CapWords` or `CamelCase` convention.
-   Class names should be descriptive and use nouns. For example, `Item` or `UserModel`.

## Path Operation Function Names

-   Although FastAPI doesn't require any specific name or even decorators for path operation functions, it's recommended that we name them in a way that makes sense to us and our team, in `snake_case`.
-   As FastAPI allows us to use the same function name for different paths and methods without collision, we can name them based on their tasks. For example, `read_items` or `create_user`.

## Pydantic Models

-   Pydantic model class names should be in `CamelCase`. For example, `ItemModel` or `UserModel`.
-   The attribute names of Pydantic models (which become the keys of the model's JSON schema) should be in `snake_case`.

These guidelines will help us write more readable, self-describing code, making our projects more maintainable and our collaboration more efficient. Remember, consistency is key in a shared codebase.
