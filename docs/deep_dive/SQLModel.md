# SQLModel Documentation

## Introduction

`SQLModel` is a library that integrates `pydantic` validation with `SQLAlchemy` ORM capabilities. It provides a unified way to create data models and tables, simplifying both data validation and database operations.

## SQLModel vs BaseModel

-   ### BaseModel:

    -   Part of the `pydantic` library.
    -   Used for data validation.
    -   Converts arbitrary data types to Python data types.
    -   Provides serialization methods, allowing conversion to and from JSON, dictionaries, etc.

    ```python
    from pydantic import BaseModel

    class Item(BaseModel):
        name: str
        price: float
    ```

-   ### SQLModel:

    -   Integrates `pydantic`'s `BaseModel` and `SQLAlchemy`'s ORM model.
    -   Used for both data validation and database table creation.
    -   Inherits all capabilities from `BaseModel`, but adds ORM capabilities such as relationships, query API, etc.

    ```python
    from sqlmodel import SQLModel, Field

    class Item(SQLModel, table=True):
        id: int = Field(primary_key=True)
        name: str
        price: float
    ```

## Conclusion:

-   While `BaseModel` is ideal for data validation and serialization in FastAPI applications, SQLModel extends its functionalities to work with databases.
-   By using `SQLModel`, you can reduce redundancy in your code, as the same model is utilized for validation, serialization, and ORM.

## Other Links:

-   [Official SQLModel Documentation](https://sqlmodel.tiangolo.com/)
-   [Pydantic BaseModel Documentation](https://docs.pydantic.dev/latest/)
