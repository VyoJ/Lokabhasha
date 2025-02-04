from pydantic import BaseModel, ConfigDict
from typing import Optional


class QuestionCreate(BaseModel):
    m_id: int
    question: str
    exp_ans: str
    category: str


class QuestionUpdate(BaseModel):
    m_id: Optional[int] = None
    question: Optional[str] = None
    exp_ans: Optional[str] = None
    category: Optional[str] = None


class QuestionInDB(BaseModel):
    model_config = ConfigDict(from_attributes=True)
    q_id: int
    m_id: int
    question: str
    exp_ans: str
    category: str
