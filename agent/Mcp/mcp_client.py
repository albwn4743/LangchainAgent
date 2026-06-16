from langchain_mcp_adapters.client import MultiServerMCPClient

async def get_mcp_tools():
    client = MultiServerMCPClient(
        {
            'financial':{
                'command':'python',
                'args':['agent/Mcp/mcpServer.py'],
                'transport':'stdio',
            }
        }
    )
    return await client.get_tools()