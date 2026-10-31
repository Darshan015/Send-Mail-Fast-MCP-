import jwt
import uvicorn
from fastapi import FastAPI
from pydantic import BaseModel
from datetime import timedelta, datetime

app = FastAPI(
    title="JWT Token Generator"
)

JWT_SECRET_KEY = "0262d58e-cb13-467a-ba1b-692b6be832f7"
JWT_ISSUER = "http://localhost:8001/"
JWT_AUDIENCE = "my-mcp-server"
JWT_ALGO = "HS256"
JWT_EXPIRE_HOURS = 2

class TokenRequest(BaseModel):
    user_id:str
    email:str
    password:str

class TokenResponse(BaseModel):
    access_token:str
    expires_in:int

@app.post("/token",response_model=TokenResponse)
def generate_token(req:TokenRequest):
    now = datetime.now()
    exp = now + timedelta(hours=JWT_EXPIRE_HOURS)

    payload = {
        "sub":req.user_id,
        "email": req.email,
        "iat": now,
        "exp": exp,
        "iss":JWT_ISSUER,
        "aud":JWT_AUDIENCE
    }
    token = jwt.encode(payload, JWT_SECRET_KEY,algorithm=JWT_ALGO )
    return TokenResponse(access_token=token, expires_in=JWT_EXPIRE_HOURS)

@app.get("/health")
def health():
    return {"status":"OK"}

if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port = 8001)

