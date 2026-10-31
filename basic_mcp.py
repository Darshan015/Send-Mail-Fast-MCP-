from fastmcp import FastMCP

app = FastMCP("Basic MCP Server")

@app.tool
def add_number(a:float,b:float) ->float:
    """ This tool is to take the 2 numbers and return the sum of those numbers"""
    return (a+b)

##Transport layer
#STDIO==>If the server is running locally and if we want to connect to any local AI host
#HTTP===>If the server is running outside

app.run(transport="streamable-http")
