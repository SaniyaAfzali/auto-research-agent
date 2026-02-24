from backend import llm, state
from backend.llm import get_llm
import re
def synthesizer_node(state):

    llm = get_llm()
    final_prompt = f"""
You are an expert research analyst.

Instructions:
- Provide a concise final answer (max 150 words).
- Directly answer the original query.
- If factual, respond in 2–5 sentences.
- Briefly mention key sources used.
- Do NOT write a long academic report.

Original Query:
{state["query"]}

Research Data:
{state["research_data"]}
"""

    final_response = llm.invoke(final_prompt)

    state["final_answer"] = final_response.content.strip()

    confidence_prompt = f"""
Based on the answer below, return ONLY a confidence score between 0 and 1.
Do not explain anything. Only return a decimal number.

Answer:
{state["final_answer"]}
"""
    confidence_response = llm.invoke(
        f"""
        Give ONLY a number between 0 and 1.
        Do not explain.
        Just return the number.

        Based on this answer:
        {state['final_answer']}
        """
    )

    raw_conf = confidence_response.content.strip()

    # Extract float using regex
    match = re.search(r"\d*\.?\d+", raw_conf)

    if match:
        value = float(match.group())
        state["confidence"] = max(0.0, min(1.0, value))
    else:
        state["confidence"] = 0.5  # safe fallback


    # -------- LOGGING (Thinking Log Visible in UI) --------
    state["logs"].append({
        "step": "Synthesizer",
        "message": state["final_answer"]
    })
    return state