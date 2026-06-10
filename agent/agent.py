from langchain_groq import ChatGroq
from langchain_core.prompts import ChatPromptTemplate
import os
from dotenv import load_dotenv

load_dotenv()


llm = ChatGroq(
    model='llama-3.3-70b-versatile',
    temperature = 0.2,
    api_key=os.getenv('GROQ_API_KEY')
)

history = []

prompt = ChatPromptTemplate.from_template(
'''
You are a banking assistant.
Rules:
1. Answer Only banking related questions and you may answer questions about your role and capabilities.
2.Banking TOpics include:
    -Savings Accounts
    -Current accounts
    -loans
    -credit cards
    -FIxed Deposits
    -Debit Cards
    -Interest Rated
    -Banking Regualtions
    -Digital Banking
3.If the question is not related to banking, then respond with:
'Sorry, i am a banking assitant. I only answer banking related questions.'
4.If the question is like "WHo are you" then respond with:
'Am a banking assitant. I will help you for the banking related queries.'
Question:{question}
history:{chat_history}
'''
)

chain = prompt | llm

while True:
    query = input('Ask a Question:')

    if query.lower() == 'exit':
        break

    response = chain.invoke({
        'question':query,
        'chat_history':history
    })

    print('\nAnswer : ')
    print(response.content)
    history.append(response.content)