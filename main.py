from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from openai import OpenAI
import os

client = OpenAI(
    api_key=os.getenv("AZURE_OPENAI_API_KEY"),
    base_url=os.getenv("AZURE_OPENAI_ENDPOINT"),
)

app = FastAPI()

class PlanRequest(BaseModel):
    goals: str

@app.post("/generate-plan")
async def generate_plan(request: PlanRequest):
    try:
        prompt = f"Create a personalized daily plan based on these goals: {request.goals}"
        response = client.chat.completions.create(
            model=os.getenv("AZURE_OPENAI_DEPLOYMENT"),
            messages=[{"role": "user", "content": prompt}]
        )
        return {"plan": response.choices[0].message.content}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
