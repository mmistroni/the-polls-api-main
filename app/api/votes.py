from fastapi import APIRouter
from app.models.votes import Vote, VoteByID, VoteByLabel, Voter, VoterCreate
from app.services import utils
from uuid import UUID   
import logging
router = APIRouter()

@router.post('/vote/{poll_id}/id')
def vote_by_id(poll_id:UUID, vote_by_id:VoteByID):
    logging.info('=== Voting By Id====')
    
    logging.info('Saving into redis..xxx.')
    vote = Vote(poll_id=poll_id, 
                choice_id=vote_by_id.choice_id,
                voter = vote_by_id.voter)


    return vote.model_dump_json()


    #utils.save_poll(new_poll)
    
    return vote_by_id.model_dump_json()
    
@router.post('/vote/{poll_id}/label')
def vote_by_label(poll_id:UUID, vote_by_label:VoteByLabel):
    logging.info('=== Voting By Label====')
    logging.info('Saving into redis...')
    choice_id = utils.get_choice_id_by_label(poll_id, 
                                             vote_by_label.choice_label
                                             )
    vote = Vote(poll_id=poll_id, 
                choice_id=choice_id,
                voter = vote_by_label.voter)

    return vote.model_dump_json()


