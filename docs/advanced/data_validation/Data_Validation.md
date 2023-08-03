# Data Validation

## Excessively use Pydantic for data validation

Some of the key features of Pydantic library:

1. Checks for Required Fields
2. Default values for Non required fields
3. Enums for only limited allowed options
4. Regex Checks
5. Length validation
6. Email validations

```python
from enum import Enum
from pydantic import AnyUrl, BaseModel, EmailStr, Field, constr

class EmployeeRole(str, Enum):
   Manager = "SDM"
   Engineer = "SDE"
   Intern = "SDI"


class UserBase(BaseModel):
    name: str = Field(min_length=1, max_length=128)
    username: constr(regex="^[A-Za-z0-9-_]+$", to_lower=True, strip_whitespace=True)
    email: EmailStr
    age: int = Field(ge=18, default=None)  # must be greater or equal to 18
    Role: EmployeeRole = 'NA'  # only "SDM", "SDE", "SDI" values are allowed
    profile_url: AnyUrl = None
```

## Use dependencies for data validation vs DB

Pydantic can only validate the client input. For any custom validation (against database, etc.) we should use dependencies.

For example in the below code we are validating if the user with the provided username exist in the database or not.

```python
from fastapi import Depends
from src.user.models import User
from src.user.exceptions import UserNotFound

# dependency.py
async def valid_username(username: str, db: Session = Depends(get_db)) -> User:
    user = await db.get(User, username) # Again this should be moved to service.py
    if not user:
        raise UserNotFound()

    return user



# router.py
from src.user import service

@router.get("/user/{username}", response_model=UserBase)
async def get_user(user: Mapping = Depends(valid_username)):
    return user

@router.put("/user/{username}", response_model=UserBase)
async def update_user(user_update: UserUpdate, user: Mapping = Depends(valid_username)):

    updated_user: User = await service.update(id=user["id"], data=user_update)

    return updated_user
```

Dependencies will allow us to re-use the custom validation logics and standardize the application flow (client response / error logging)

## Decouple & Reuse dependencies. Dependency calls are cached

Dependencies can be called multiple times, and the FastAPI will cache the result of the dependency for that request cycle and won't re-calculate the dependency again and again. Reducing the latency, database and network calls.

E.g. [Copied from here](https://betterprogramming.pub/fastapi-best-practices-1f0deeba4fce#:~:text=4.-,Decouple%20%26%20Reuse%20dependencies.%20Dependency%20calls%20are%20cached,-Dependencies%20can%20be):

For example, in the code below we are using `parse_jwt_data` dependency three times:

1. `valid_owned_post`
2. `valid_active_creator`
3. `get_user_post`,
   but `parse_jwt_data` is called only once, in the very first call.

```python
# dependencies.py
from fastapi import BackgroundTasks
from fastapi.security import OAuth2PasswordBearer
from jose import JWTError, jwt

async def valid_post_id(post_id: UUID4) -> Mapping:
    post = await service.get_by_id(post_id)
    if not post:
        raise PostNotFound()

    return post


async def parse_jwt_data(
    token: str = Depends(OAuth2PasswordBearer(tokenUrl="/auth/token"))
) -> dict:
    try:
        payload = jwt.decode(token, "JWT_SECRET", algorithms=["HS256"])
    except JWTError:
        raise InvalidCredentials()

    return {"user_id": payload["id"]}


async def valid_owned_post(
    post: Mapping = Depends(valid_post_id),
    token_data: dict = Depends(parse_jwt_data),
) -> Mapping:
    if post["creator_id"] != token_data["user_id"]:
        raise UserNotOwner()

    return post


async def valid_active_creator(
    token_data: dict = Depends(parse_jwt_data),
):
    user = await users_service.get_by_id(token_data["user_id"])
    if not user["is_active"]:
        raise UserIsBanned()

    if not user["is_creator"]:
       raise UserNotCreator()

    return user


# router.py
@router.get("/users/{user_id}/posts/{post_id}", response_model=PostResponse)
async def get_user_post(
    worker: BackgroundTasks,
    post: Mapping = Depends(valid_owned_post),
    user: Mapping = Depends(valid_active_creator),
):
    """Get post that belong the active user."""
    worker.add_task(notifications_service.send_email, user["id"])
    return post
```

### Reducing code duplication further

When you need to use the `parse_jwt_data` dependency, you have to write the whole parameter with the type annotation and Depends():

```python
token_data: dict = Depends(parse_jwt_data)
```

In case we are using Annotated, we can store that Annotated value in a variable and use it in multiple places:

```python
from typing import Annotated

from typing import Annotated
commonDep = Annotated[dict, Depends(parse_jwt_data)]

async def valid_owned_post(..., token_data: commonDep):


async def valid_active_creator(token_data: commonDep):
```

> This is just standard Python, it's called a "type alias", it's actually not specific to FastAPI.

> `Note:` FastAPI added support for Annotated (and started recommending it) in version 0.95.0. If you have an older version, you would get errors when trying to use Annotated. Make sure you Upgrade the FastAPI version to at least 0.95.1 before using Annotated.

### [Next Topic: Proper Handling of Sync and Async tasks](/docs/advanced/performance/Async_Await.md)

### [Previous Topic: Project Structure](/docs/advanced/project_structure/Project_Structure.md)

## Topics to Cover:

- [Hierarchical Dependencies](https://fastapi.tiangolo.com/tutorial/dependencies/#__tabbed_1_2:~:text=etc.-,Simple%20and%20Powerful,-%C2%B6)
- [Classes as dependencies](https://fastapi.tiangolo.com/tutorial/dependencies/classes-as-dependencies/#:~:text=is%20a%20%22callable%22.-,Classes%20as%20dependencies,-%C2%B6)
- [Using the same dependency multiple times](https://fastapi.tiangolo.com/tutorial/dependencies/sub-dependencies/#using-the-same-dependency-multiple-times:~:text=/items/-,Using%20the%20same%20dependency%20multiple%20times,-%C2%B6)
- [Be careful with dynamic pydantic fields](https://betterprogramming.pub/fastapi-best-practices-1f0deeba4fce#:~:text=9.-,Be%20careful%20with%20dynamic%20pydantic%20fields,-If%20you%20have)
