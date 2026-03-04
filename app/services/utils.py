from upstash_redis import Redis
from app.models.polls import Poll, PollCreate

import os
redis_client = Redis(
    url=os.environ['KV_REST_API_URL'],
    token=os.environ['KV_REST_API_TOKEN']
    )

def save_poll(poll: Poll) -> Poll:
    redis_client.set(f"poll:{poll.id}", poll.model_dump_json())  
    return poll


def get_poll(id: str) -> Poll | None:
    """Retrieve a poll by its id from Redis.

    Returns the stored object if found or ``None`` if the key does not
    exist.  The caller (typically a FastAPI path operation) can raise an
    ``HTTPException`` if it needs to convert ``None`` into a 404 response.
    """
    # ``redis_client.get`` will return ``None`` when the key is missing.  We
    # simply forward what the client returns; serialization behavior is
    # controlled by the Upstash client configuration (it will decode JSON
    # automatically if the value was set as a Pydantic model).
    obj =  redis_client.get(id)
    return Poll.model_validate_json(obj) if obj is not None else None