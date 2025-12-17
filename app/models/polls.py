from pydantic import BaseModel,Field
from datetime import datetime, timezone
from uuid import UUID, uuid4
from typing import List, Optional

class Poll(BaseModel):
    id:UUID = Field(description="Unique id", default_factory=uuid4)
    options:List[str]
    created:datetime = Field(description='Created Time', 
                                        default_factory= lambda: datetime.now(timezone.utc))
    title:str = Field(min_length=5, max_length=50)
    expires_at:Optional[datetime] = None