from pydantic import BaseModel
from typing import List

class Prospect(BaseModel):
    prospect: str
    messages: List[str]

class Request(BaseModel):
    prospects: List[Prospect]
