from langchain_core.messages import HumanMessage, AIMessage

history = []

def user_message(message):
    history.append(HumanMessage(content=message))

def ai_message(message):
    history.append(AIMessage(content=message))

def full_history():
    return history