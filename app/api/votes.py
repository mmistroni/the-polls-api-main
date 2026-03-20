from fastapi import APIRouter, Depends, HTTPException
from app.models.votes import Vote, VoteByID, VoteByLabel, Voter, VoterCreate
from app.services import utils
from uuid import UUID   
import logging
router = APIRouter()

@router.post('/vote/{poll_id}/id')
def vote_by_id(poll_id:UUID, vote_by_id:VoteByID):
    logging.info('=== Voting By Id====')
    
    logging.info('Saving into redis...')
    #utils.save_poll(new_poll)
    
    return {"message": "Vote recorded"}
    
@router.post('/vote/{poll_id}/label')
def vote_by_label(poll_id:UUID, vote_by_label:VoteByLabel):
    logging.info('=== Voting By Label====')
    
    logging.info('Saving into redis...')
    
    return {"message": "Vote recorded"}


