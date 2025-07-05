import os
from dotenv import load_dotenv
load_dotenv()

groq_api_key=os.getenv("GROQ_API_KEY")
tavily_api_key= os.getenv("TAVILY_API_KEY")
openai_api_key = os.getenv("OPENAI_API_KEY")

from langchain_groq import ChatGroq
from langchain_tavily import TavilySearch

grop_llm = ChatGroq(model = "llama-3.3-70b-versatile")

from langgraph.prebuilt import create_react_agent
from langchain_core.messages.ai import AIMessage

def get_response_from_ai_agent(llm_id, query, allow_search):
    
    llm=ChatGroq(model=llm_id)
    
    tools=[TavilySearch(max_results=2)] if allow_search else []
    agent=create_react_agent(
        model=llm,
        tools=tools,
    )
    state={"messages": query}
    response=agent.invoke(state)
    messages=response.get("messages")
    ai_messages=[message.content for message in messages if isinstance(message, AIMessage)]
    return ai_messages[-1]