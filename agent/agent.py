from prompt import prompts
from modelConfig import llm
from memory import user_message, ai_message,full_history
from langchain_core.prompts import MessagesPlaceholder,ChatPromptTemplate
from langchain.agents import create_agent
from banking_tools import bank_interest_rates,calculate_emi,bank_names,general_banking_faq,card_types_faq,loan_details_faq

tools = [
    bank_interest_rates,
    calculate_emi,
    bank_names,
    general_banking_faq,
    loan_details_faq,
    card_types_faq
]
prompt = ChatPromptTemplate.from_messages([
    ('system',prompts),
    MessagesPlaceholder(variable_name='messages')
])

agent = create_agent(model=llm, tools=tools,system_prompt=prompts)


while True:
    question = input("\nQuestion:")
    user_message(question)
    try:
        response = agent.invoke(
            {
                'messages':full_history()[-6:]
            }
        )
        
        answer = response['messages'][-1].content
    
        print("\nAgent:", answer)
        ai_message(answer)
    except Exception as e:
        print("I dont have the prior information for that")

    


