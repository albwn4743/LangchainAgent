# from nodes.SupervisorAgent import supervisor
from langgraph.workflow import app
from memory import user_message,ai_message
import asyncio
while True:
    question = input("\nQuestion:")
    try:
        response = asyncio.run(
            app.ainvoke(
            {
                'question':question
            }
        )
        )
        
        answer = response['answer']
    
        print("\nAgent:", answer)
        user_message(question)
        ai_message(answer)
    except Exception as e:
        print("error",e)
