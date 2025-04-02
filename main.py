from fastapi import FastAPI
from pydantic import BaseModel
import openai
import os

# Azure OpenAI config
openai.api_type = "azure"
openai.api_key = os.getenv("AZURE_OPENAI_KEY")
openai.api_base = os.getenv("AZURE_OPENAI_ENDPOINT")  # e.g. https://your-resource.openai.azure.com/
openai.api_version = "2024-02-15-preview"

deployment_name = "gpt-4o"  # match your Azure deployment name

app = FastAPI()

# Define request model
class PlanRequest(BaseModel):
    goals: str

@app.post("/generate-plan")
async def generate_plan(request: PlanRequest):
    try:
        response = openai.ChatCompletion.create(
            engine=deployment_name,  # Azure requires engine, not model
            messages=[
                {"role": "system", "content": "You are a helpful assistant that creates daily plans based on user goals."},
                {"role": "user", "content": f"My goals are: {request.goals}"}
            ]
        )
        return {"plan": response.choices[0].message["content"]}
    except Exception as e:
        return {"error": str(e)}
