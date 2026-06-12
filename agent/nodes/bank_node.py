from Agents.BaseAgent import banking_executor
from memory import full_history
def banking_node(state):
    try:
        response = banking_executor.invoke(
            {
                "input": state["question"],
                "messages": full_history()[-6:]
            }
        )

        return {
            "answer": response["output"]
        }
    except Exception as e:

        return {"answer":f"Error: failed to generate the answer:'{e}"}