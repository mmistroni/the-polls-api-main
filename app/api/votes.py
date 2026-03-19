from fastapi import APIRouter, Depends, HTTPException
from app.models.votes import Vote, VoteByID, VoteByLabel, Voter, VoterCreate
from app.services import utils
from uuid import UUID   
import logging
router = APIRouter()

@router.post('/create_vote_by_id')
def create_vote(voter:Voter, vote_by_id:VoteByID):
    logging.info('=== Creating Polls====')
    
    logging.info('Saving into redis...')
    #utils.save_poll(new_poll)
    
    return {
        
    }
    
@router.post('/create_vote_by_label')
def create_vote(voter:Voter, vote_by_label:VoteByLabel):
    logging.info('=== Creating Polls====')
    
    logging.info('Saving into redis...')
    utils.save_poll(new_poll)
    
    return {
        
    }


