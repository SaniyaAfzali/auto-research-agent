from fastapi import FastAPI
from backend.graph import build_graph

app = FastAPI()
graph = build_graph()


@app.post("/research")
def research(query: str):

    initial_state = {
        "query": query,
        "sub_questions": [],
        "research_data": "",
        "evaluation": "",
        "final_answer": "",
        "confidence": "0.8",
        "iteration": "",
        "next": "",
        "logs": []
    }

    result = graph.invoke(initial_state)

    return {
        "final_answer": result.get("final_answer"),
        "confidence": result.get("confidence"),
        "logs": result.get("logs")
    }