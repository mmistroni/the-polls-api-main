from pydantic import BaseModel,Field
from datetime import datetime
from uuid import UUID, uuid4
from typing import List

class Poll(BaseModel):
    id:uuid.UUID = Field(description="Unique id", default_factory=lambda : uuid4)
    options:List[str]
    created:datetime = Field(description='Created Time', default_factory= lambda: datetime.now())