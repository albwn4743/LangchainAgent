from Agents.BaseAgent import create_base_agent
from memory import full_history
banking_executor = None

async def initialize_agent():
    global banking_executor
    banking_executor = await create_base_agent()

async def banking_node(state):
    # banking_executor = await create_base_agent()
    try:
        response = await banking_executor.ainvoke(
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