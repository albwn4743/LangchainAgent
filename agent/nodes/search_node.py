from Agents.WebSearch_Agent import search_executor
from memory import full_history
async def search_node(state):
    response = await search_executor.ainvoke(
        {
            "input": state["question"],
            'messages':full_history()[-6:]
        }
    )
    print(response)
    return {
        "answer": response["output"]
    }