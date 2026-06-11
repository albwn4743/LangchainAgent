from langchain_classic.agents import create_tool_calling_agent, AgentExecutor
from modelConfig import llm
from prompt import banking_prompt
from langchain_core.prompts import ChatPromptTemplate,MessagesPlaceholder
from tools.banking_tools import bank_interest_rates,calculate_emi,bank_names,general_banking_faq,card_types_faq,loan_details_faq
# from langchain.agents import 
tools = [
    bank_interest_rates,
    calculate_emi,
    bank_names,
    general_banking_faq,
    loan_details_faq,
    card_types_faq,
]
prompt = ChatPromptTemplate.from_messages([
    ('system',banking_prompt),
    MessagesPlaceholder(variable_name='messages'),
    ('human','{input}'),
    MessagesPlaceholder(variable_name='agent_scratchpad'),
])

agent = create_tool_calling_agent(
    llm=llm,
    tools=tools,
    prompt=prompt
)
banking_executor = AgentExecutor(
    agent=agent,
    tools=tools
)