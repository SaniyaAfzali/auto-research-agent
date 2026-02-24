# import streamlit as st
# from backend.graph import build_graph
# from backend.state import AgentState

# st.set_page_config(page_title="AutoResearch Agent", layout="wide")

# st.title("          🔎 AutoResearch Agent")
# st.write("Autonomous AI Research with Multi-Step Reasoning")

# query = st.text_input("Enter Research Query")

# if st.button("Start Research"):

#     if not query:
#         st.warning("Please enter a query")
#     else:
#         graph = build_graph()

#         initial_state = {
#             "query": query,
#             "sub_questions": [],
#             "research_data": [],
#             "final_answer": None,
#             "logs": [],
#             "iteration": 0,
#             "next": ""
#         }

#         with st.spinner("Agent is thinking..."):
#             result = graph.invoke(initial_state)

#         st.success("Research Complete")

#         # Final Answer
#         st.subheader("📌 Final Answer")
#         st.write(result["final_answer"])

#         # Thinking Log
#         st.subheader("🧠 Thinking Log")

#         for log in result["logs"]:
#             with st.expander(f"{log['step']}"):
#                 st.write(log["message"])

#         # Confidence
#         if "confidence" in result:
#             st.subheader("📊 Confidence Level")
#             st.write(result["confidence"]) 
import streamlit as st
from backend.graph import build_graph

st.set_page_config(layout="wide")

st.title("🔎 AutoResearch Agent")

query = st.text_input("Enter your research query:")

if st.button("Run Research") and query:

    graph = build_graph()

    initial_state = {
        "query": query,
        "sub_questions": [],
        "research_data": "",
        "logs": [],
        "iteration": 0,
        "next": ""
    }

    result = graph.invoke(initial_state)

    col1, col2 = st.columns([1, 1])

    # LEFT SIDE — THINKING LOG
    with col1:
        st.subheader("🧠 Thinking Log")

        for log in result["logs"]:
            with st.expander(f"{log['step']}"):
                st.write(log["message"])

    # RIGHT SIDE — FINAL ANSWER
    with col2:
        st.subheader("📄 Final Answer")

        st.markdown(
            f"""
            <div style="
                background-color: #080808;
                padding: 20px;
                border-radius: 10px;
                box-shadow: 0 2px 10px rgba(0,0,0,0.1);
                ">
                {result.get("final_answer", "No final answer generated.")}
            </div>
            """,
            unsafe_allow_html=True
        )
        if "confidence" in result:
            st.subheader("📊 Confidence Level")
            st.write(result["confidence"])