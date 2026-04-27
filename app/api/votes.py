from fastapi import APIRouter, HTTPException
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
                voter = Voter(
                    **vote_by_id.voter.model_dump())
    )


    return {"message" : "Vote recorded",
            "vote": vote
            }
            

    
@router.post('/vote/{poll_id}/label')
def vote_by_label(poll_id:UUID, vote:VoteByLabel):
    logging.info('=== Voting By Label====')
    logging.info('Saving into redis...')
    choice_id = utils.get_choice_id_by_label(poll_id, 
                                             vote.choice_label
                                             )
    if not choice_id:
        raise HTTPException(
            status_code = 400,
            detail='Invalid choice provided')
    vote = Vote(poll_id=poll_id, 
                choice_id=choice_id,
                voter = Voter(
                    **vote.voter.model_dump_json()
                )
            )

    return {"message" : "Vote recorded",
            "vote": vote
            }
    


