from fastapi import FastAPI, Request
import openai
import os

app = FastAPI()

# Azure OpenAI settings
openai.api_type = "azure"
openai.api_base = os.getenv("AZURE_OPENAI_ENDPOINT")  # e.g., "https://your-resource-name.openai.azure.com/"
openai.api_version = "2024-02-15-preview"  # check Azure's current version
openai.api_key = os.getenv("AZURE_OPENAI_KEY")
deployment_name = "gpt-4o"  # must match the exact name used in Azure deployment

@app.post("/generate-plan")
async def generate_plan(request: Request):
    data = await request.json()
    goals = data.get("goals")

    try:
        response = openai.ChatCompletion.create(
            engine=deployment_name,
            messages=[
                {"role": "system", "content": "You are a helpful assistant that generates action plans."},
                {"role": "user", "content": f"My goals are: {goals}"}
            ]
        )
        return {"plan": response.choices[0].message["content"]}
    except Exception as e:
        return {"error": str(e)}
