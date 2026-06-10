from prompt import prompts
from modelConfig import llm
from memory import user_message, ai_message,full_history
from langchain.agents import create_agent
from banking_tools import get_interest, bank_FAQs,calculate_emi,bank_names,general_banking_faq,card_types_faq,loan_details_faq

tools = [
    get_interest,
    bank_FAQs,
    calculate_emi,
    bank_names,
    general_banking_faq,
    loan_details_faq,
    card_types_faq
]

agent = create_agent(model=llm, tools=tools,system_prompt=prompts)

# agent_executor = AgentExecutor(agent=agent,tools=tools)

while True:
    question = input("\nQuestion:")
    user_message(question)
    try:
        response = agent.invoke(
            {
                'messages':full_history()
            }
        )
        
        answer = response['messages'][-1].content
    
        print("\nAgent:", answer)
        ai_message(answer)
    except Exception as e:
        print('Error', e)

    



# chain = prompts | llm
# while True:
#     query=input("Question:")
#     if query.lower() == 'exit':
#         break
#     check_knowledge = retrieve_context(query)
#     if check_knowledge:
#         # print('Answer:',check_knowledge)

#         user_message(query)
#         ai_message(check_knowledge)
#     #     continue
#     response = chain.invoke({
#         'query':query,
#         'history':full_history(),
#         'context':check_knowledge
#     })


#     print('Bot:',response.content)

#     user_message(query)
#     ai_message(response.content)