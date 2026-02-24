from backend.llm import get_llm

def critic_node(state):

    if not state.get("research_data"):
        state["next"] = "research_again"
        return state

    response = get_llm().invoke(
        f"Evaluate this research. If sufficient say COMPLETE.\n\n{state['research_data']}"
    )

    evaluation = response.content

    state["evaluation"] = evaluation

    state["logs"].append({
        "step": "Critic",
        "message": evaluation
    })

    if "COMPLETE" not in evaluation and state["iteration"] < 2:
        state["iteration"] += 1
        state["next"] = "research_again"
        return state

    state["next"] = "finish"
    return state