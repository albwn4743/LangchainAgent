# from nodes.SupervisorAgent import supervisor
from graph.workflow import app
from memory import user_message,ai_message
while True:
    question = input("\nQuestion:")
    try:
        response = app.invoke(
            {
                'question':question
            }
        )
        
        answer = response['answer']
    
        print("\nAgent:", answer)
        user_message(question)
        ai_message(answer)
    except Exception as e:
        print("error",e)
