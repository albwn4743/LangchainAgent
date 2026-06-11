from prompt import prompts
from modelConfig import llm
from search import web_search
from memory import user_message, ai_message,full_history
from langchain_core.prompts import MessagesPlaceholder,ChatPromptTemplate
# from langchain.agents import create_tool
from langchain_classic.agents import AgentExecutor, create_tool_calling_agent
# from langchain.agents.tool_calling_agent import create_tool_calling_agent
from banking_tools import bank_interest_rates,calculate_emi,bank_names,general_banking_faq,card_types_faq,loan_details_faq
# from langchain.agents import 
tools = [
    bank_interest_rates,
    calculate_emi,
    bank_names,
    general_banking_faq,
    loan_details_faq,
    card_types_faq,
    web_search
]
prompt = ChatPromptTemplate.from_messages([
    ('system',prompts),
    MessagesPlaceholder(variable_name='messages'),
    ('human','{input}'),
    MessagesPlaceholder(variable_name='agent_scratchpad'),
])

agent = create_tool_calling_agent(
    llm=llm,
    tools=tools,
    prompt=prompt
)
agent_executor = AgentExecutor(
    agent=agent,
    tools=tools,
    verbose=True
)

while True:
    question = input("\nQuestion:")
    try:
        response = agent_executor.invoke(
            {
                'input':question,
                'messages':full_history()[-6:]
            }
        )
        
        answer = response['output']
    
        print("\nAgent:", answer)
        user_message(question)
        ai_message(answer)
    except Exception as e:
        print("error",e)

    


