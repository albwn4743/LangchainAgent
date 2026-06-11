from Agents.BaseAgent import banking_executor

def banking_node(state):

    response = banking_executor.invoke(
        {
            "input": state["question"],
            "messages": state.get("messages", [])
        }
    )

    return {
        "answer": response["output"]
    }