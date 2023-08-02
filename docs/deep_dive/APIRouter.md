# FastAPI's APIRouter

## Introduction

The `APIRouter` is a FastAPI class that allows us to modularize our routes, effectively organizing our application into smaller, more manageable sub-applications.

## Basic Usage

Below is a simple example:

```python
from fastapi import APIRouter, FastAPI

router = APIRouter()

@router.get("/items/{item_id}")
def read_item(item_id: int):
    return {"item_id": item_id}

app = FastAPI()

app.include_router(router)
```

Here, `router` is an instance of `APIRouter`. We define our route functions as methods of `router`, instead of `app`. We then include these routes in our application by calling `app.include_router(router)`.

## Grouping Routes

`APIRouter` allows us to group related routes together. For example:

```python
from fastapi import APIRouter

router = APIRouter()

@router.get("/users/{user_id}")
def read_user(user_id: int):
    return {"user_id": user_id}

@router.get("/users/me")
def read_user_me():
    return {"user_id": "the current user"}

app.include_router(router, prefix="/v1")
```

Here, all routes in `router` will have the path prefix `/v1`. The final paths will be `/v1/users/{user_id}` and `/v1/users/me`.

## Tags

Tags can be used with `APIRouter` for better organization and documentation of routes.

```python
app.include_router(router, prefix="/v1", tags=["users"])
```

In the Swagger UI, all routes included in `router` will be grouped under the "users" tag.

## Advantages:

-   **Modularity:** Helps in keeping the codebase organized by logically separating routes into different routers based on their functionality.
-   **Reusability:** Routers can be re-used across different FastAPI applications.
-   **Maintainability:** Makes the application easier to maintain and scale by isolating changes to specific routers.

## Other Links:

-   [Official FastAPI APIRouter Documentation](`https://fastapi.tiangolo.com/tutorial/bigger-applications/#apirouter`)
