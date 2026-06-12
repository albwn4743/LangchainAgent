from Agents.WebSearch_Agent import search_executor
from memory import full_history
def search_node(state):
    response = search_executor.invoke(
        {
            "input": state["question"],
            'messages':full_history()[-6:]
        }
    )
    return {
        "answer": response["output"]
    }