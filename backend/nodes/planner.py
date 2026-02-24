from backend.llm import get_llm
def planner_node(state):

    response = get_llm().invoke(
        f"Break this research query into 3 sub-questions:\n\n{state['query']} within 150 words"
    )

    sub_questions = response.content.split("\n")

    state["sub_questions"] = sub_questions
    state["logs"].append({
        "step": "Planner",
        "message": sub_questions
    })

    return state