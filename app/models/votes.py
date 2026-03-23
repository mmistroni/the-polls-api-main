from pydantic import BaseModel, Field, field_validator, EmailStr
from datetime import datetime, timezone
from uuid import UUID, uuid4
from typing import List, Optional
from .choice import Choice, ChoiceCreate
from fastapi import HTTPException
from .choice import Choice


class Voter(BaseModel):
    """ Voter read data model"""
    email:str = EmailStr

class VoterCreate(BaseModel):
    """ Voter write data model"""
    voted_at:datetime = Field(default_factory=lambda : datetime.now(timezone.utc))


class Vote(BaseModel):
    """ Vote read data model"""
    poll_id:UUID
    choice_id:UUID
    voter:Voter

class VoteByID(BaseModel):
    """ Vote write data model for uuid labels"""
    choice_id:UUID
    voter:VoterCreate


class VoteByLabel(BaseModel):
    """ Vote write data model for int labels"""
    choice_label:int
    voter:VoterCreate

    