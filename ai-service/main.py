from fastapi import FastAPI
import requests
import os
from openai import OpenAI

app = FastAPI()

client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

@app.get("/analysis")
def analyze():
    response = requests.get("http://data-service:8000/metrics")
    data = response.json()

    prompt = f"""
    Analysiere folgende Google-Trends-Daten:

    {data}

    Gib eine kurze datenbasierte Interpretation:
    - stärkste Begriffe
    - Trends
    - Auffälligkeiten
    - Unterschiede zwischen Begriffen

    Wichtig:
    - keine Fantasie
    - nur Aussagen auf Basis der Daten
    - kurz und verständlich
    """

    ai_response = client.chat.completions.create(
        model="gpt-4o-mini",
        messages=[
            {"role": "user", "content": prompt}
        ]
    )

    return {
        "data": data,
        "analysis": ai_response.choices[0].message.content
    }

@app.get("/health")
def health():
    return {"status": "ok"}