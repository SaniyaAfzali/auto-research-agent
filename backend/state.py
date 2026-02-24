from typing import TypedDict, List, Dict

class AgentState(TypedDict):
    query: str
    sub_questions: List[str]
    research_data: str
    evaluation: str
    final_answer: str
    confidence: float
    iteration: int
    next: str
    logs: List[Dict]