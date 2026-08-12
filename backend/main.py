import os, json
from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
from dotenv import load_dotenv
import google.generativeai as genai

load_dotenv()
app = FastAPI()
app.add_middleware(CORSMiddleware, allow_origins=["*"], allow_credentials=True, allow_methods=["*"], allow_headers=["*"])

api_key = os.getenv("GEMINI_API_KEY")
if api_key:
    genai.configure(api_key=api_key)

class PromptRequest(BaseModel):
    prompt: str

SYSTEM_PROMPT = """You are a Spatial 3D Engine Assistant. Convert user prompt into structured JSON. Return ONLY raw JSON:
{
    "nodes": [{"id": "node_1", "label": "Label Name", "position": [x, y, z], "color": "#ff0055"}],
    "connections": [{"from": "node_1", "to": "node_2"}],
    "camera_target": [0, 0, 0]
}"""

@app.post("/api/spatial-command")
async def process_spatial_command(data: PromptRequest):
    if not api_key:
        raise HTTPException(status_code=400, detail="Missing GEMINI_API_KEY")
    try:
        model = genai.GenerativeModel("gemini-2.5-flash", generation_config={"response_mime_type": "application/json"})
        response = model.generate_content(f"{SYSTEM_PROMPT}\nUser Request: {data.prompt}")
        clean_text = response.text.replace("```json", "").replace("```", "").strip()
        return json.loads(clean_text)
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
