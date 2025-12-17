from fastapi import FastAPI
from fastapi.exceptions import RequestValidationError
from app.models import polls
import uvicorn
#from app.api import votes, danger, exceptions
from app.models.polls import Poll
import logging

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
def create_polls(input:Poll) -> Poll:
    logging.info('=== Creating Polls====')
    return Poll(options=['One', 'Two', 'Three'], title=input.title)
    
