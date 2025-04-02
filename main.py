from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from openai import OpenAI

# Initialize OpenAI client with your API key
client = OpenAI(api_key="sk-svcacct-plQMD5SgwjO5NKJgoU4pCU2VtQnqZZJ-nGI8bCWoTpZsVa6IcqfWHUD1y9o8GT3BlbkFJmEY-OaCeioz9SypiGHAOZLfJhFkn2Gk_ovZvu7FdPRt2Pr0Hvt15yKVc-LGAA")

app = FastAPI()

class PlanRequest(BaseModel):
    goals: str

@app.post("/generate-plan")
async def generate_plan(request: PlanRequest):
    try:
        prompt = f"Create a personalized daily plan based on these goals: {request.goals}"

        response = client.chat.completions.create(
            model="gpt-3.5-turbo",
            messages=[
                {"role": "user", "content": prompt}
            ]
        )

        return {"plan": response.choices[0].message.content}
    
    except Exception as e:
        import traceback
        traceback.print_exc()
        raise HTTPException(status_code=500, detail=f"Connection error: {str(e)}")

