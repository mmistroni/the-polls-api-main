from fastapi import FastAPI
from fastapi.exceptions import RequestValidationError
from app.models import polls
from app.services import utils
from uuid import UUID
import uvicorn
#from app.api import votes, danger, exceptions
from app.models.polls import Poll, PollCreate
import logging
import os

app = FastAPI(
    title="Polls API",
    description="A simple API to create and vote on polls",
    version="0.1",
    openapi_tags=[
        {
            "name": "polls",
            "description": "Operations related to creating and viewing polls",
        },
        {
            "name": "danger",
            "description": "Operations that lead to irreversible data loss",
        },
        {
            "name": "votes",
            "description": "Operations related to casting votes",
        },
    ],
)


'''
app.add_exception_handler(
    RequestValidationError, exceptions.custom_validation_exception_handler
)
app.include_router(polls.router, prefix="/polls", tags=["polls"])
app.include_router(danger.router, prefix="/polls", tags=["danger"])
app.include_router(votes.router, prefix="/vote", tags=["votes"])
'''

# Objective:
# - reshape the pydantic error messages into custom messages that only
# include the "msg" property of the error

@app.get('/test')
def test():
    return {'message' : 'Hello there'}

@app.post('/polls/create')
def create_polls(poll:PollCreate):
    logging.info('=== Creating Polls====')
    new_poll = poll.create_poll()
    
    logging.info('Saving into redis...')
    utils.save_poll(new_poll)
    
    return {
        "detail" : "Poll successfully created",
        "poll_id" : new_poll.id,
        "poll" : new_poll
        
    }
    
@app.get('/polls/{id}')
def read_poll(id: UUID):
    """Fetch a poll by its unique identifier.

    The path parameter ``id`` is a string representation of the UUID used as
    the key in Redis.  If the poll cannot be found the endpoint raises a
    ``404`` error.
    """
    logging.info(f"Fetching poll {id} from redis")
    poll = utils.get_poll(id)
    if poll is None:
        from fastapi import HTTPException
        raise HTTPException(status_code=404, detail=f"Poll for id {id} was not found")
    return poll


