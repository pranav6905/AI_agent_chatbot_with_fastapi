from pydantic import BaseModel
from typing import List

class RequestState(BaseModel):
    model_name : str
    messages : List[str]
    allow_search : bool

from fastapi import FastAPI
from ai_agent import get_response_from_ai_agent

ALLOWED_MODEL_NAMES=["llama3-70b-8192", "gemma2-9b-it", "llama-3.3-70b-versatile"]

app=FastAPI(title="LangGraph AI Agent")

@app.post("/chat")
def chat_endpoint(request : RequestState):

    if request.model_name not in ALLOWED_MODEL_NAMES:
        return {"error": "Invalid model name. Kindly select a valid AI model"}
    
    llm_id = request.model_name
    query = request.messages
    allow_search = request.allow_search

    response=get_response_from_ai_agent(llm_id, query, allow_search)
    return response


if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="127.0.0.1", port=5000)
    