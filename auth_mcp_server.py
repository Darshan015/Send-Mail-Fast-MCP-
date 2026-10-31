from fastmcp import FastMCP
from fastmcp.server.auth.providers.jwt import JWTVerifier
from fastmcp.server.dependencies import get_access_token

JWT_SECRET_KEY = "0262d58e-cb13-467a-ba1b-692b6be832f7"
JWT_ISSUER = "http://localhost:8001/"
JWT_AUDIENCE = "my-mcp-server"
JWT_ALGO = "HS256"
JWT_EXPIRE_HOURS = 2

verifier  =JWTVerifier(public_key=JWT_SECRET_KEY,
                       algorithm=JWT_ALGO,
                       issuer=JWT_ISSUER,
                       audience=JWT_AUDIENCE)

mcp = FastMCP("secure MCP server", auth=verifier)

@mcp.tool
def who_am_i()->dict:
    """ returns the userid of the current authenticated user"""
    token = get_access_token()
    print("\n\n",token,"\n\n")
    return {
        "client_id":token.client_id
    }

mcp.run(transport="streamable-http")