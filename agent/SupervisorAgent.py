from modelConfig import llm
def supervisor(state):
    prompt = f'''

decide which agent should answer.
Available agents are;
    -bankagent.
    -web search agent.

question: {state['question']}

return only:
    -bankagent
    -web search agent.
'''

    route = llm.invoke(prompt).content.strip()
    return {
        'route':route
    }