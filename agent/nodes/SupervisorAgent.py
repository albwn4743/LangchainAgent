from modelConfig import llm
from memory import full_history
def supervisor(state):
    current_answer = state.get('answer','')
    question = state['question']
    history = full_history()
    prompt = f'''
You are the main supervisor agent for a Banking Assistant.
Your task is to decide the next step (route) to resolve the user's question.
Available routes:
- 'banking': Choose this if the question is about the banking/financial sector and we have NOT queried the local database yet. The local database supports interest rates, EMI calculations, FAQs, and card types for the
 following banks: SBI, HDFC, ICICI, Federal, and Canara.
- 'search': Choose this if the question is about the banking/financial sector but:
  1. We already queried the 'banking' agent and it failed to find a proper answer (i.e. the current answer is "I do not have verified information for that request.", contains "Error:", or similar failure message).
  2. The question is about a non-supported bank or financial product not in the local database.
- 'not_banking': Choose this ONLY if the question is completely outside the banking or financial sector and has no relation to banking, loans, cards, interest, or finance, OR if it is a simple greeting (like 'hello').
 Do NOT choose 'not_banking' if the question is a follow-up query referring to a bank or financial topic in the Conversation History (e.g., 'which bank is this?', 'what are their rates?').
- 'end': Choose this ONLY if we already have a valid, helpful answer in the 'Current Answer' field below (which means one of the agents has just answered the current question). Do NOT choose 'end' if the 'Current Answer'
 field is empty, not set, or is an error message.

Conversation History:{history}
Question: {question}
Current Answer: {current_answer}

Analyze the state and conversation history carefully.
CRITICAL RULE 1: If the 'Current Answer' field is empty, you must NOT choose 'end'. You must choose 'banking', 'search', or 'not_banking' to get an answer generated.
CRITICAL RULE 2: If the user's question refers to previous topics, banks, or details from the Conversation History (e.g., using pronouns like 'this', 'that', 'they', or asking follow-up questions like 'which bank you
 are talking about?', 'what are their rates then?'), you must route to 'banking' or 'search' (never to 'not_banking' or 'end').
Respond with ONLY one word from the available routes: banking, search, not_banking, or end. Do not include any other text.
'''
    route = llm.invoke(prompt).content.strip()
    # print("route: ",route)
    if 'not_banking' in route:
        return {'route':'end','answer':'its not a banking sector question'}
    elif 'end' in route:
        if not current_answer:
            return{'route':'banking'}
        return {'route':'end'}
    elif 'search' in route:
        return {'route':'search'}
    else:
        return {'route':'banking'}