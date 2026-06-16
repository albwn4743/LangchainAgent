from mcp.server.fastmcp import FastMCP

mcp = FastMCP('first MCP server')


@mcp.tool()
def greet(name:str)->str:
    '''Greet a user'''
    return f"Hello, {name}"

if __name__ == '__main__':
    mcp.run()