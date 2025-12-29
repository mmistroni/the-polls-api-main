from pydantic import BaseModel,Field
from datetime import datetime, timezone
from uuid import UUID, uuid4
from typing import List, Optional

class ChoiceCreate(BaseModel):
    """ Choice write data model representing a single choice in a poll"""
    description:str = Field

class Choice(BaseModel):
    """ Choice read data model wih a label and an auto gen uuid"""
    id:UUID = Field(description="Unique id", default_factory=uuid4)
    label:int = Field(description="Label", gt=0, le=5)