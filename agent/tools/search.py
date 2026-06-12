from langchain_tavily import TavilySearch
from langchain_core.tools import tool
from dotenv import load_dotenv
load_dotenv()

tavily = TavilySearch(
    max_results = 3
)


@tool
def web_search(question:str):
    """
    Search the web when banking tools do not contain the answer.
    Use for insurance policies, latest rates, latest bank products,
    and any information unavailable in local banking tools.
    """
    # print("web search is using")
    response = tavily.invoke(question)
    output= []
    for i in response['results']:
        output.append(
            f"title:{i['title'][:300]}\n"
            f"Content:{i['content']}"
        )
    return '\n\n'.join(output)