# Getting Started with FastAPI

This guide will take us through the basic steps needed to create and run a FastAPI application.

## Create the Basic Application

First, we'll create a very simple FastAPI application. In our project directory, create a new Python file (e.g., `main.py`) and add the following code:

```python
from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def read_root():
return {"Hello": "World"}
```

Here, we create a FastAPI instance `app` and a route `/` that returns a JSON response `{"Hello": "World"}`.

## Run FastAPI on a Specific Port

FastAPI uses Uvicorn as an ASGI server to run our application. By default, it will run on `localhost` on port `8000`.

To run the server on a different port, we can specify the port parameter when running Uvicorn, like this:

```bash
uvicorn main:app --port 3000 --reload
```

This command will start the FastAPI application on port `3000`.

## Add the First Endpoint

We have already created a root endpoint in the first step. Here is another one. Update `main.py` to look like this:

```python
from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def read_root():
    return {"Hello": "World"}

@app.get("/items/{item_id}")
def read_item(item_id: int):
    return {"item_id": item_id}
```

We just added a new endpoint `/items/{item_id}`, which uses a path parameter item_id. When we access `/items/5`, we'll see `{"item_id": 5}` as the response.

## Documentation URLs

FastAPI automatically generates two sets of interactive API documentation. You can see them once our app is running, by going to:

-   Swagger UI: http://localhost:8000/docs
-   ReDoc: http://localhost:8000/redoc

Remember to replace `8000` with the port we're running our application on.

## Create an Endpoint that Accepts URL Parameters

We have already created a simple endpoint with a path parameter. You can also have more than one path parameter and parameters of other types. For example:

```python
@app.get("/users/{user_id}/items/{item_id}")
def read_user_item(user_id: int, item_id: str):
    return {"user_id": user_id, "item_id": item_id}
```

## Create an Endpoint that Accepts Query Parameters

FastAPI recognizes parameters not included in the path as query parameters. For example:

```python
from typing import Optional

@app.get("/items/")
def read_items(skip: int = 0, limit: Optional[int] = None):
    return {"skip": skip, "limit": limit}
```

Here, `skip` and `limit` are optional query parameters. You can use them like this: `/items/?skip=0&limit=10`.

## Create an Endpoint that Accepts Request Body

FastAPI also makes it easy to define endpoints that need to receive JSON bodies. You can use Pydantic models for this. For example:

```python
from pydantic import BaseModel
from typing import Optional

class Item(BaseModel):
    name: str
    description: Optional[str] = None
    price: float

@app.post("/items/")
def create_item(item: Item):
    return item
```

Here, `Item` is a Pydantic model that defines the structure and data types of the JSON body the `/items/` POST endpoint expects.

You can test this endpoint using Postman or using swagger UI.

## Application Events

FastAPI provides a way to handle application events, such as startup and shutdown events. For example:

```python
@app.on_event("startup")
async def startup_event():
    print("Starting up...")

@app.on_event("shutdown")
async def shutdown_event():
    print("Shutting down...")
```

`startup_event` will be executed when the Uvicorn server starts up, and `shutdown_event` will be executed when the server is shutting down.

Remember to run our application with `uvicorn main:app --reload` every time we make changes.

## Also See

-   ### [Naming Conventions](/docs/standard/Naming_Conventions.md)

### [Next Topic: Deep Dive](/docs/deep_dive/Deep_Dive.md)

### [Previous Topic: Environment Setup](/docs/Environment_Setup.md)
