# 🧠 AI Planner API

A lightweight FastAPI app that generates a daily plan from user goals using Azure OpenAI (GPT-4o). Built for rapid deployment, with minimal configuration, and tested with both OpenAI and Azure OpenAI endpoints.

---

## 📌 Features

- ✅ Accepts user goals via JSON
- 🧠 Uses GPT-4o to generate a structured day plan
- 🔒 Secure API key management using environment variables
- 🚀 Deployable on Render or Replit (via FastAPI & Uvicorn)

---

## 🛠️ Local Development Setup

### 1. Clone the repository
```bash
git clone https://github.com/<your-username>/ai-planner-api.git
cd ai-planner-api
```

### 2. Create a virtual environment
```bash
python -m venv venv
source venv/bin/activate   # macOS/Linux
venv\Scripts\activate      # Windows
```

### 3. Install dependencies
```bash
pip install -r requirements.txt
```

### 4. Set your environment variable
You can use `.env` or PowerShell for testing:

```bash
export AZURE_OPENAI_API_KEY=<your-key>
export AZURE_OPENAI_ENDPOINT=<your-endpoint>
export AZURE_DEPLOYMENT_NAME=gpt-4o
```

Or on Windows PowerShell:
```powershell
$env:AZURE_OPENAI_API_KEY = "<your-key>"
$env:AZURE_OPENAI_ENDPOINT = "<your-endpoint>"
$env:AZURE_DEPLOYMENT_NAME = "gpt-4o"
```

---

## ▶️ Run the App

```bash
uvicorn main:app --reload
```

Visit: [http://127.0.0.1:8000/docs](http://127.0.0.1:8000/docs) for Swagger UI.

---

## 🔁 API Endpoint

### `POST /generate-plan`

#### Request Body (JSON)
```json
{
  "goals": "Go for a walk, finish report, family dinner"
}
```

#### Response
```json
{
  "plan": "1. 7AM Walk...\n2. 9AM Write report...\n3. 7PM Family dinner..."
}
```

---

## ☁️ Deploying to Render

### Steps:
1. Push code to GitHub
2. Create new Web Service on [Render](https://render.com/)
3. Set build command:
   ```
   pip install -r requirements.txt
   ```
4. Set start command:
   ```
   uvicorn main:app --host=0.0.0.0 --port=10000
   ```
5. Add environment variables in Render dashboard:
   - `AZURE_OPENAI_API_KEY`
   - `AZURE_OPENAI_ENDPOINT`
   - `AZURE_DEPLOYMENT_NAME`

### Example public endpoint:
```
POST https://ai-planner-api.onrender.com/generate-plan
```

---

## 💡 Why Azure OpenAI?

Using Azure's OpenAI allows enterprise-grade API access with regional compliance, custom capacity, and scalable quotas—ideal for production deployment within corporate boundaries.

---

## 📂 Project Structure

```
ai-planner-api/
├── main.py                # FastAPI app
├── requirements.txt       # Dependencies
├── .env                   # (optional) Local secrets
└── README.md              # This file
```

---

## 🧠 Built With

- [FastAPI](https://fastapi.tiangolo.com/)
- [Azure OpenAI](https://learn.microsoft.com/en-us/azure/cognitive-services/openai/)
- [Uvicorn](https://www.uvicorn.org/)

---

## 🔐 Security Notes

- Never commit `.env` or secret keys.
- Use Render’s Secrets UI or GitHub Actions secrets for deployments.

---

## 📬 License

MIT – Use it. Modify it. Deploy it 🚀
