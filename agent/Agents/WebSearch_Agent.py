from langchain_classic.agents import create_tool_calling_agent,AgentExecutor
from modelConfig import llm
from prompt import search_prompt
from tools.search import web_search
from langchain_core.prompts import MessagesPlaceholder,ChatPromptTemplate

tools = [
    web_search
]
prompt = ChatPromptTemplate.from_messages([
    ("system", search_prompt),
    ("human", "{input}"),
    MessagesPlaceholder(variable_name="agent_scratchpad"),
])

agent = create_tool_calling_agent(
    llm=llm,
    tools=tools,
    prompt=prompt
)

search_executor = AgentExecutor(
    agent=agent,
    tools=tools
)