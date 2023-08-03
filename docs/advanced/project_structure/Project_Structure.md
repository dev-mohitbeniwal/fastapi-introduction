# Project Structure. Consistent & Predictable

There are two different Project structures that I have found depending on the use-case we can go with one of these.

## 1. Monolithic or very large applications

```
fastapi-project
├── alembic/ # (DB Migration scripts)
├── src
│   ├── entity-1
│   │   ├── router.py # HTTP Routes for entity-1
│   │   ├── schemas.py  # Pydantic models
│   │   ├── models.py  # DB Models
│   │   ├── dependencies.py # Dependable dependency injections
│   │   ├── config.py  # local configs
│   │   ├── constants.py
│   │   ├── exceptions.py
│   │   ├── service.py # The actual logic for the service
│   │   └── utils.py # Utility functions
│   ├── entity-2
│   │   ├── client.py  # client model for external service communication
│   │   ├── schemas.py
│   │   ├── config.py
│   │   ├── constants.py
│   │   ├── exceptions.py
│   │   └── utils.py
│   └── entity-3
│   │   ├── router.py
│   │   ├── schemas.py
│   │   ├── models.py
│   │   ├── dependencies.py
│   │   ├── constants.py
│   │   ├── exceptions.py
│   │   ├── service.py
│   │   └── utils.py
│   ├── config.py  # global configs
│   ├── models.py  # global models
│   ├── exceptions.py  # global exceptions
│   ├── pagination.py  # global module e.g. pagination
│   ├── database.py  # db connection related stuff
│   └── main.py
├── tests/
│   ├── auth
│   ├── aws
│   └── posts
├── templates/
│   └── index.html
├── requirements
│   ├── base.txt
│   ├── dev.txt
│   └── prod.txt
├── .env
├── .gitignore
├── logging.ini
└── alembic.ini # configuration for alembic
```

### Use of `__init__.py` file

If we use `__init__.py` inside the folders and sub-folders we can use each folder as a single package and import the classes and methods using an absolute path.

E.g.

```
from src.auth import constants as auth_constants
from src.notifications import service as notification_service
from src.posts.constants import ErrorCode as PostsErrorCode
```

## 2. Microservices or small applications

In FastAPI's official documentation also they have suggest the project structure that we can follow for small projects:

```
.
├── app                  # "app" is a Python package
│   ├── __init__.py      # this file makes "app" a "Python package"
│   ├── main.py          # "main" module, e.g. import app.main
│   ├── dependencies.py  # "dependencies" module, e.g. import app.dependencies
│   └── routers          # "routers" is a "Python subpackage"
│   │   ├── __init__.py  # makes "routers" a "Python subpackage"
│   │   ├── items.py     # "items" submodule, e.g. import app.routers.items
│   │   └── users.py     # "users" submodule, e.g. import app.routers.users
│   └── internal         # "internal" is a "Python subpackage"
│       ├── __init__.py  # makes "internal" a "Python subpackage"
│       └── admin.py     # "admin" submodule, e.g. import app.internal.admin

```

You can check this out in more detail on their [Bigger Applications - Multiple Files](https://fastapi.tiangolo.com/tutorial/bigger-applications/) document.

### [Next Topic: Data Validation](/docs/advanced/data_validation/Data_Validation.md)

### [Previous Topic: Advanced Topics in FastAPI](/docs/advanced/Advance_Topics.md)
