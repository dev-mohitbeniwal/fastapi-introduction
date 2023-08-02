# Deep Dive into FastAPI

This guide provides a deeper understanding of various aspects of FastAPI.

## FastAPI Basics

FastAPI allows us to build APIs quickly through a simple syntax. Here are some of the fundamental components:

-   **Routing:** We define routes using Python decorator syntax on top of our route handling functions. We use `@app.get("/")`, `@app.post("/items")`, etc., to define routes.

-   **Parameters:** Parameters in FastAPI can be path parameters (e.g., `@app.get("/items/{item_id}")`), query parameters (e.g., `def read_items(skip: int = 0, limit: int = None):`), or even complex parameters with Pydantic models.

-   **Request Bodies:** FastAPI allows us to define complex data input using Pydantic models. FastAPI will automatically handle validation and parsing of request bodies.

-   **Responses:** By default, FastAPI will convert Python dict, list, etc., into JSON responses. We can also define Pydantic models for output data.

-   **Cookies, Headers, and Status Codes:** FastAPI allows us to define cookies, headers, and status codes for our API responses. It provides a set of parameter options like `status_code`, `response_model`, `tags`, `summary`, `description`, etc., for this purpose.

## Pydantic Models

Pydantic is a data validation library that FastAPI uses to perform input data validation, serialization, and documentation. We define Pydantic models like this:

```python
from sqlmodel import Field, Session, SQLModel, create_engine, select

class Item(SQLModel, table=True):
    id: Optional[int] = Field(default=None, primary_key=True)
    name: str
    price: float
    is_offer: Optional[bool] = None

```

Here, we have a model `Item` with fields `name`, `description`, `price`, and `is_offer`.

## Dependency Injection

FastAPI provides a simple dependency injection system. It allows us to define dependencies and use them in our path operation functions:

```python
from fastapi import Depends
from sqlmodel import Session, create_engine, select

# SQLite database URL
DATABASE_URL = "sqlite:///./test.db"

# Create an engine for the SQLite database
engine = create_engine(DATABASE_URL, echo=True)

# Function to get a new SQLModel session
def get_db_session():
    with Session(engine) as session:
        yield session

@app.get("/items/{item_id}")
def read_item(item_id: int, db: Session = Depends(get_db_session)):
    item = db.exec(select(Item).where(Item.id == item_id)).first()
    if not item:
        raise HTTPException(status_code=404, detail="Item not found")
    return item

@app.post("/items/")
def create_item(item: Item, db: Session = Depends(get_db_session)):
    db.add(item)
    db.commit()
    db.refresh(item)
    return item
```

Here, `get_db_session` is a dependency that provides a database session. FastAPI will automatically manage the lifecycle of the session.

## Authentication & Authorization

FastAPI provides several tools to handle authentication and authorization:

-   **OAuth2 with Password (and hashing), Bearer with JWT tokens:** FastAPI provides all the tools needed to implement the entire OAuth2 flow, including JWT tokens.

-   **OAuth2 with Password (and hashing), Bearer with JWT tokens, scopes, and roles:** Here, FastAPI adds support for defining scopes and roles in OAuth2.

-   **HTTP Basic Auth:** We can implement HTTP Basic Auth using HTTPBasic dependencies.

## Error Handling

FastAPI provides a model for handling errors and exceptions:

```python
from fastapi import FastAPI, HTTPException

@app.get("/items/{item_id}")
def read_item(item_id: str):
    if item_id not in items:
    raise HTTPException(status_code=404, detail="Item not found")
    return items[item_id]
```

Here, we raise an `HTTPException` if the item is not found. FastAPI will automatically convert the exception into an appropriate HTTP response.

This guide provides a quick overview of these topics. Each of them has in-depth documentation and examples in the [official FastAPI documentation](https://fastapi.tiangolo.com/). Remember to consult it whenever you need a more detailed explanation or examples.

### [Next Topic: Advanced Topics in FastAPI](/docs/advanced/Advance_Topics.md)

### [Previous Topic: Getting Started with Fast API](/docs/Getting_Started.md)

## Also See

-   ### [SQLModel and BaseModel](/docs/deep_dive/SQLModel.md)

-   ### [FastAPI's APIRouter](/docs/deep_dive/APIRouter.md)
