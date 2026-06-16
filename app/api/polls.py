from fastapi import APIRouter, Depends, HTTPException
from app.models.polls import Poll, PollCreate, PollStatus
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
@router.get('/')
def browse_polls(poll_status: PollStatus = PollStatus.ACTIVE):
    logging.info('=== Browsing Polls====')
    polls =  utils.get_all_polls()
    if not polls:
        raise HTTPException(status_code=404, detail="No polls found")   
    if poll_status == PollStatus.ACTIVE:
        polls = [poll for poll in polls if poll.is_active()]
    elif poll_status == PollStatus.EXPIRED:
        polls = [poll for poll in polls if not poll.is_active()]
    return polls    

@router.get('/{poll_id}')
def read_poll(poll_id: UUID):
    """Fetch a poll by its unique identifier.

    The path parameter ``id`` is a string representation of the UUID used as
    the key in Redis.  If the poll cannot be found the endpoint raises a
    ``404`` error.
    """
    logging.info(f"Fetching poll {poll_id} from redis")
    poll = utils.get_poll(poll_id)
    if poll is None:
        from fastapi import HTTPException
        raise HTTPException(status_code=404, detail=f"Poll for id {poll_id} was not found")
    return poll

