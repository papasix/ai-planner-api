import os
import openai
from fastapi import FastAPI, Request

app = FastAPI()

# Azure OpenAI specific setup
openai.api_type = "azure"
openai.api_key = os.getenv("AZURE_OPENAI_KEY")
openai.api_base = os.getenv("AZURE_OPENAI_ENDPOINT")  # should end with /
openai.api_version = "2024-02-15-preview"  # or as per your Azure deployment

deployment_name = "gpt-4o"  # match your Azure deployment name exactly

@app.post("/generate-plan")
async def generate_plan(request: Request):
    data = await request.json()
    goals = data.get("goals", "")

    try:
        response = openai.ChatCompletion.create(
            engine=deployment_name,  # not model=, for Azure
            messages=[
                {"role": "system", "content": "You are a helpful assistant that creates daily plans based on user goals."},
                {"role": "user", "content": f"My goals are: {goals}"}
            ]
        )
        return {"plan": response.choices[0].message["content"]}
    except Exception as e:
        return {"error": str(e)}
