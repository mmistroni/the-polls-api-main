from pydantic import BaseModel,Field
from datetime import datetime
import uuid
from typing import List

class Poll(BaseModel):
    id:uuid.UUID = Field(description="Unique id", default_factory=lambda : uuid.UUID())
    options:List[str]
    created:datetime = Field(description='Created Time', default=datetime.now())