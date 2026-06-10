history = []

def user_message(message):
    history.append({
        'role':'user',
        'content':message
    })

def ai_message(message):
    history.append({
        'role':'assistant',
        "content":message
    })

def full_history():
    return history