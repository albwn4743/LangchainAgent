from Agents.WebSearch_Agent import search_executor
def search_node(state):
    response = search_executor.invoke(
        {
            "input": state["question"]
        }
    )
    return {
        "answer": response["output"]
    }