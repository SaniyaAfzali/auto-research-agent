from langgraph.graph import StateGraph, END
from backend.state import AgentState

from backend.nodes.planner import planner_node
from backend.nodes.researcher import researcher_node
from backend.nodes.critic import critic_node
from backend.nodes.synthesizer import synthesizer_node


def build_graph():

    workflow = StateGraph(AgentState)

    workflow.add_node("planner", planner_node)
    workflow.add_node("researcher", researcher_node)
    workflow.add_node("critic", critic_node)
    workflow.add_node("synthesizer", synthesizer_node)

    workflow.set_entry_point("planner")

    workflow.add_edge("planner", "researcher")
    workflow.add_edge("researcher", "critic")

    workflow.add_conditional_edges(
        "critic",
        lambda state: state["next"],
        {
            "research_again": "researcher",
            "finish": "synthesizer"
        }
    )

    workflow.add_edge("synthesizer", END)

    return workflow.compile()