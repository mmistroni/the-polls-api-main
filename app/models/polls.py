from pydantic import BaseModel,Field
from datetime import datetime, timezone
from uuid import UUID, uuid4
from typing import List, Optional
from .choice import Choice

class PollCreate(BaseModel):
    """Poll write data model"""
    title:str = Field(min_length=5, max_length=50)
    expires_at:Optional[datetime] = None
    options:List[str]
    

class Poll(PollCreate):
    """Poll read data model"""
    id:UUID = Field(description="Unique id", default_factory=uuid4)
    options:List[Choice]
    created_at:Optional[datetime] = Field(default_factory=lambda : datetime.now(timezone.utc))