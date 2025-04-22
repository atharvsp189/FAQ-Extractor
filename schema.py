from pydantic import BaseModel
from typing import List


class qa_pair(BaseModel):
    question: str
    answer: str

class qa_data(BaseModel):
    qas: List[qa_pair]