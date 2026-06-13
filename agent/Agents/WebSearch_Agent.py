from langchain_classic.agents import create_tool_calling_agent,AgentExecutor
from modelConfig import llm
from prompt import search_prompt
from tools.search import web_search
from langchain_core.prompts import MessagesPlaceholder,ChatPromptTemplate
from webscrap import search_and_scrape

tools = [
    search_and_scrape
]
prompt = ChatPromptTemplate.from_messages([
    ("system", search_prompt),
    MessagesPlaceholder(variable_name="messages"),
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
    # max_iterations=1,
    # verbose=True,
    # return_intermediate_steps=True
    # early_stopping_method='generate'
)