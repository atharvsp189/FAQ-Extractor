from qdrant_client import QdrantClient
from qdrant_client.http.models import Distance, VectorParams
from langchain_openai import OpenAIEmbeddings
from langchain_openai import ChatOpenAI

import os 
from dotenv import load_dotenv
load_dotenv()

Qdrant_API_Key = os.getenv("Qdrant_API_Key")
Qdrant_URL = os.getenv("Qdrant_URL")

class Clients:
    def __init__(self):
        pass
    
    def get_llm(self, model="gpt-4o-mini", temperature = 0.0):
        
        llm = ChatOpenAI(
            model=model,
            temperature=temperature,
        )
        return llm

    
    def get_qdrant_client(self):
        qdrant_client = QdrantClient(
            url= Qdrant_URL,
            api_key=Qdrant_API_Key,
            timeout=60 
        )
        
        return qdrant_client
    

    def get_embed_model(self):
        embed_model = OpenAIEmbeddings(
            model="text-embedding-3-large",
        )
        
        return embed_model