from langchain_classic.agents import create_tool_calling_agent, AgentExecutor
from modelConfig import llm
from prompt import banking_prompt
from mcp_client import get_mcp_tools
from langchain_core.prompts import ChatPromptTemplate,MessagesPlaceholder
from tools.banking_tools import bank_interest_rates,calculate_emi,bank_names,general_banking_faq,card_types_faq,loan_details_faq
# from langchain.agents import 

async def create_base_agent():
    mcp_tools = await get_mcp_tools()

    tools = [
        bank_interest_rates,
        # calculate_emi,
        bank_names,
        general_banking_faq,
        loan_details_faq,
        card_types_faq,
    ]
    all_tools = tools+mcp_tools

    prompt = ChatPromptTemplate.from_messages([
        ('system',banking_prompt),
        MessagesPlaceholder(variable_name='messages'),
        ('human','{input}'),
        MessagesPlaceholder(variable_name='agent_scratchpad'),
    ])

    agent = create_tool_calling_agent(
        llm=llm,
        tools=all_tools,
        prompt=prompt
    )
    return AgentExecutor(
        agent=agent,
        tools=all_tools
    )

# banking_executor = await create_base_agent()