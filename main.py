from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from openai import OpenAI
import os

# Access API key from Render environment variable
client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

app = FastAPI()

class PlanRequest(BaseModel):
    goals: str

@app.post("/generate-plan")
async def generate_plan(request: PlanRequest):
    try:
        prompt = f"Create a personalized daily plan based on these goals: {request.goals}"
        response = client.chat.completions.create(
            model="gpt-3.5-turbo",
            messages=[{"role": "user", "content": prompt}]
        )
        return {"plan": response.choices[0].message.content}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))