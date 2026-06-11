# from nodes.SupervisorAgent import supervisor
from graph.workflow import app
from memory import user_message,ai_message,full_history
while True:
    question = input("\nQuestion:")
    try:
        response = app.invoke(
            {
                'question':question,
                'messages':full_history()[-6:]
            }
        )
        
        answer = response['answer']
    
        print("\nAgent:", answer)
        user_message(question)
        ai_message(answer)
    except Exception as e:
        print("error",e)
