from fastapi import FastAPI
from pydantic import BaseModel
import os
from openai import AzureOpenAI

# Setup Azure OpenAI
client = AzureOpenAI(
    api_key=os.getenv("AZURE_OPENAI_KEY"),
    api_version="2024-02-15-preview",
    azure_endpoint=os.getenv("AZURE_OPENAI_ENDPOINT")
)

deployment_name = "gpt-4o"  # Your deployment name in Azure

app = FastAPI()

class PlanRequest(BaseModel):
    goals: str

@app.post("/generate-plan")
async def generate_plan(request: PlanRequest):
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
