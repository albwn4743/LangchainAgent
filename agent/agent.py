from knowledge import bank_details
from prompt import prompts
from modelConfig import llm
from memory import user_message, ai_message,full_history


chain = prompts | llm


while True:
    query=input("Question:")
    if query.lower() == 'exit':
        break
    check_knowledge = bank_details(query)
    if check_knowledge:
        # print('Answer:',check_knowledge)

        user_message(query)
        ai_message(check_knowledge)
    #     continue
    response = chain.invoke({
        'query':query,
        'history':full_history(),
        'context':check_knowledge
    })


    print('Bot:',response.content)

    user_message(query)
    ai_message(response.content)