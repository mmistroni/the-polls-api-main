from fastapi import APIRouter, HTTPException, Depends
from app.models.votes import Vote, VoteByID, VoteByLabel, Voter, VoterCreate
from app.models.polls import Poll
from app.services import utils
from uuid import UUID   
from datetime import datetime
from typing import Union
import logging
router = APIRouter()


def common_vote_validations(poll_id:UUID, vote: Union[VoteByID, VoteByLabel]) -> Poll:
    poll = utils.get_poll(poll_id)
    vote_by_email = vote.voter.email
    if not poll:
        raise HTTPException(status_code=404, detail="The poll was not found")

    if not poll.is_active():
        raise HTTPException(status_code=404, detail=f"Poll has expired!")

    if utils.get_vote(poll_id, vote_by_email) is not None:
        raise HTTPException(status_code=404, detail=f"Already voted!")
    
    return poll


@router.post('/vote/{poll_id}/id')
def vote_by_id(poll_id:UUID, 
               vote_by_id:VoteByID,
               poll: Poll = Depends(common_vote_validations)):
    logging.info('=== Voting By Id====')
    
    # Validating choices
    choice_id = vote_by_id.choice_id
    poll_choice_ids = [choice.id for choice in poll.options]
    if choice_id not in  poll_choice_ids :
        raise HTTPException(status_code=404, 
                            detail=f"Invalid choice for poll.Should be one of {poll_choice_ids}")
    

    logging.info('Saving into redis..xxx.')
    vote = Vote(poll_id=poll_id, 
                choice_id=vote_by_id.choice_id,
                voter = Voter(
                    **vote_by_id.voter.model_dump()),
                channel=vote_by_id.channel
    )
    utils.save_vote(poll_id, vote)
    return {"message" : "Vote recorded",
            "vote": vote
            }
            

    
@router.post('/vote/{poll_id}/label')
def vote_by_label(poll_id:UUID, 
                  vote_by_label:VoteByLabel, 
                  poll: Poll = Depends(common_vote_validations)):
    logging.info('=== Voting By Label====')
    logging.info('Saving into redis...')
    choice_id = utils.get_choice_id_by_label_given(vote_by_label.choice_label, poll)
    if not choice_id:
        raise HTTPException(
            status_code = 400,
            detail='Invalid choice provided')
    vote = Vote(poll_id=poll_id, 
                choice_id=choice_id,
                voter = Voter(
                    **vote_by_label.voter.model_dump()
                ),
                channel=vote_by_label.channel
            )
    utils.save_vote(vote)
    return {"message" : "Vote recorded",
            "vote": vote
            }
    
    

        






