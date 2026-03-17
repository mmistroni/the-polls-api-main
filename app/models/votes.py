from pydantic import BaseModel, Field, field_validator
from datetime import datetime, timezone
from uuid import UUID, uuid4
from typing import List, Optional
from .choice import Choice
from fastapi import HTTPException
from .choice import Choice


class VoteCreate(BaseModel):
    """ Vote write data models"""
    voted_at:datetime = Field(default_factory=lambda : datetime.now(timezone.utc))

class Voter(VoteCreate):
    """ Voter read data model"""
    email:str = Field(email=True)



class Vote(BaseModel):
    """ Vote read data model"""
    poll_id:UUID
    choice_id:Choice
    voter:Voter

class VoteUUIDWrite(Vote):
    """ Vote write data model for uuid labels"""
    choice_id:UUID


    def create_vote(self) -> "Vote ":
        """
        Creates a new Vote from a choice UUID 
        
        :param self: Description
        """
        

        return Vote(poll_id=self.poll_id, choice_id=self.choice_id, voter=self.voter)


