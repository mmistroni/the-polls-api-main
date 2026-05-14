from fastapi import APIRouter, HTTPException
from app.models.votes import Vote, VoteByID, VoteByLabel, Voter, VoterCreate
from app.services import utils
from uuid import UUID   
from datetime import datetime
import logging
router = APIRouter()

@router.post('/vote/{poll_id}/id')
def vote_by_id(poll_id:UUID, vote_by_id:VoteByID):
    logging.info('=== Voting By Id====')
    
    is_poll_active(poll_id)

    if utils.get_vote(poll_id, vote_by_id.voter.email) is not None:
        raise HTTPException(status_code=404, detail=f"Already voted!")
    
    
    logging.info('Saving into redis..xxx.')
    vote = Vote(poll_id=poll_id, 
                choice_id=vote_by_id.choice_id,
                voter = Voter(
                    **vote_by_id.voter.model_dump())
    )
    utils.save_vote(poll_id, vote)
    return {"message" : "Vote recorded",
            "vote": vote
            }
            

    
@router.post('/vote/{poll_id}/label')
def vote_by_label(poll_id:UUID, vote_by_label:VoteByLabel):
    logging.info('=== Voting By Label====')
    
    is_poll_active(poll_id)
    
    if utils.get_vote(poll_id, vote_by_label.voter.email) is not None:
        raise HTTPException(status_code=404, detail=f"Already voted!")
    
    logging.info('Saving into redis...')
    choice_id = utils.get_choice_id_by_label(poll_id, 
                                             vote_by_label.choice_label
                                             )
    if not choice_id:
        raise HTTPException(
            status_code = 400,
            detail='Invalid choice provided')
    vote = Vote(poll_id=poll_id, 
                choice_id=choice_id,
                voter = Voter(
                    **vote_by_label.voter.model_dump()
                )
            )
    utils.save_vote(vote)
    return {"message" : "Vote recorded",
            "vote": vote
            }
    
def is_poll_active(poll_id:UUID) -> None :
    if not  utils.get_poll(poll_id).is_active():
         raise HTTPException(status_code=404, detail=f"Poll has expired!")
    

        






