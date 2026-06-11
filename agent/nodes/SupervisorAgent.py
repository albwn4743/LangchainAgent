from modelConfig import llm
def supervisor(state):
    prompt = f'''

decide which agent should answer.
Available agents are;
    -bankagent.
    -search.

question: {state['question']}

return only:
    banking or search
'''

    route = llm.invoke(prompt).content.strip()
    print("route: ",route)
    return {
        'route':route
    }