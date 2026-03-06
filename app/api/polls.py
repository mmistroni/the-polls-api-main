from fastapi import APIRouter, Depends, HTTPException
from app.models.polls import Poll, PollCreate
from app.services import utils
from uuid import UUID   
import logging
router = APIRouter()

@router.post('/create')
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
    
@router.get('/{poll_id}')
def read_poll(poll_id: UUID):
    """Fetch a poll by its unique identifier.

    The path parameter ``id`` is a string representation of the UUID used as
    the key in Redis.  If the poll cannot be found the endpoint raises a
    ``404`` error.
    """
    logging.info(f"Fetching poll {poll_id} from redis")
    poll = utils.get_poll(id)
    if poll is None:
        from fastapi import HTTPException
        raise HTTPException(status_code=404, detail=f"Poll for id {poll_id} was not found")
    return poll

