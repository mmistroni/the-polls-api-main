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

    def create_poll(self) -> "Poll":
        """
        Creates a new Poll instalceDocstring for create_poll
        
        :param self: Description
        """
        choices = [Choice(label=idx + 1, description=desc) for 
                    idx, desc in enumerate(self.options)]
        if self.expires_at is not None and self.expires_at < datetime.now(timezone.utc):
            raise ValueError("Expires at must be in the future")
        return Poll(title=self.title, expires_at=self.expires_at,
                        options=choices)


    

class Poll(PollCreate):
    """Poll read data model"""
    id:UUID = Field(description="Unique id", default_factory=uuid4)
    options:List[Choice]
    created_at:Optional[datetime] = Field(default_factory=lambda : datetime.now(timezone.utc))