from fastapi import FastAPI, Request, Header, HTTPException
from pydantic import BaseModel
import os
from openai import AzureOpenAI

from fastapi.middleware.cors import CORSMiddleware

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # or restrict to ["http://localhost:3000"] for security
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


app = FastAPI()

# Azure OpenAI client setup
client = AzureOpenAI(
    api_key=os.getenv("AZURE_OPENAI_KEY"),
    api_version="2024-02-15-preview",
    azure_endpoint=os.getenv("AZURE_OPENAI_ENDPOINT")
)

deployment_name = "gpt-4o"
EXPECTED_API_KEY = os.getenv("INTERNAL_API_KEY")

# Input model
class PlanRequest(BaseModel):
    goals: str

# Protected endpoint
@app.post("/generate-plan")
async def generate_plan(
    request: PlanRequest,
    x_api_key: str = Header(default=None)
):
    if x_api_key != EXPECTED_API_KEY:
        raise HTTPException(status_code=401, detail="Unauthorized")

    try:
        response = client.chat.completions.create(
            model=deployment_name,
            messages=[
                {"role": "system", "content": "You are a helpful assistant that creates a daily plan based on the user's goals."},
                {"role": "user", "content": f"My goals are: {request.goals}"}
            ]
        )
        return {"plan": response.choices[0].message.content}
    except Exception as e:
        return {"error": str(e)}