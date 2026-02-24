from backend.llm import get_llm

def researcher_node(state):

    combined_questions = "\n".join(state["sub_questions"])

    response = get_llm().invoke(
        f"Provide detailed research for:\n\n{combined_questions}"
    )

    state["research_data"] = response.content

    state["logs"].append({
        "step": "Researcher",
        "message": response.content[:]
    })

    return state