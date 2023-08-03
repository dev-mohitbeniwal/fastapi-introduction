# Proper Handling Sync and Async tasks

> This point is taken from [here](https://betterprogramming.pub/fastapi-best-practices-1f0deeba4fce#:~:text=5.-,Don%E2%80%99t%20make%20your%20routes%20async%2C%20if%20you%20have%20only%20blocking%20I/O%20operations,-Under%20the%20hood). Please test the same on your own to understand this better.

## Don’t make your routes async, if you have only blocking I/O operations

Under the hood, FastAPI can effectively handle both async and sync I/O operations.

- FastAPI runs `sync` routes in the threadpool and blocking I/O operations won't stop the event loop from executing the tasks.
- Otherwise, if the route is defined `async` then it's called regularly via await and FastAPI trusts you to do only non-blocking I/O operations.

The caveat is if you fail that trust and execute blocking operations within `async` routes, the event loop will not be able to run the next tasks until that blocking operation is done.

```python
import asyncio
import time

@router.get("/terrible-ping")
async def terrible_catastrophic_ping():
    time.sleep(10) # I/O blocking operation for 10 seconds
    pong = service.get_pong()  # I/O blocking operation to get pong from DB

    return {"pong": pong}

@router.get("/good-ping")
def good_ping():
    time.sleep(10) # I/O blocking operation for 10 seconds, but in another thread
    pong = service.get_pong()  # I/O blocking operation to get pong from DB, but in another thread

    return {"pong": pong}

@router.get("/perfect-ping")
async def perfect_ping():
    await asyncio.sleep(10) # non I/O blocking operation
    pong = await service.async_get_pong()  # non I/O blocking db call

    return {"pong": pong}
```

## Save files in chunks

Don’t hope your clients will send small files.

```python
import aiofiles
from fastapi import UploadFile

DEFAULT_CHUNK_SIZE = 1024 * 1024 * 50  # 50 megabytes

async def save_video(video_file: UploadFile):
   async with aiofiles.open("/file/path/name.mp4", "wb") as f:
     while chunk := await video_file.read(DEFAULT_CHUNK_SIZE):
         await f.write(chunk)
```

## If you must use sync SDK, then run it in a thread pool

If you must use an SDK to interact with external services, and it’s not `async` then make the HTTP calls in an external worker thread.

For a simple example, we could use our well-known `run_in_threadpool` from `starlette`.

E.g.

```python
from fastapi import FastAPI
from fastapi.concurrency import run_in_threadpool
from my_sync_library import SyncAPIClient

app = FastAPI()


@app.get("/")
async def call_my_sync_library():
    my_data = await service.get_my_data()

    client = SyncAPIClient()
    await run_in_threadpool(client.make_request, data=my_data)
```
