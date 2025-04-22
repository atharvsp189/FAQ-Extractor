from llama_index.vector_stores.qdrant import QdrantVectorStore
from llama_index.core import Document, StorageContext, VectorStoreIndex
from qdrant_client.http.models import Distance, VectorParams
from llama_index.embeddings.openai import OpenAIEmbedding
from qdrant_client import QdrantClient

import uuid
import os
from dotenv import load_dotenv
load_dotenv()

Qdrant_API_Key = os.getenv("Qdrant_API_Key")
Qdrant_URL = os.getenv("Qdrant_URL")

# Configure the embedding model
embed_model = OpenAIEmbedding(
    model="text-embedding-3-small",
    api_key=os.getenv("OPENAI_API_KEY")
)

# Initialize Qdrant client
qdrant_client = QdrantClient(
    url= Qdrant_URL,
    api_key=Qdrant_API_Key,
    timeout=60 
)

def upload_embedding(
    chunks:list, 
    url:str, 
    collection:str):
    documents = []
    for chunk in chunks:
        documents.append(Document(text=chunk, 
                                metadata={
                                    url: url
                                    }))
    
    print(f"Created {len(documents)} documents from chunks")
    
    # Check if collection exists
    if collection in [collection.name for collection in qdrant_client.get_collections().collections]:
        print(f"Collection '{collection}' already exists.")
    else:
        print(f"Collection '{collection}' not found. Creating now...")
        qdrant_client.create_collection(
            collection_name=collection,
            vectors_config=VectorParams(
                size=1536,
                distance=Distance.COSINE
            )
        )
        print(f"✅ Collection '{collection}' created successfully.")
    
    vector_store = QdrantVectorStore(
        client=qdrant_client,
        collection_name=collection,
        prefer_grpc=True
    )
    
    storage_context = StorageContext.from_defaults(vector_store=vector_store)
    
    # Create vector index from chunked documents using the embedding model
    try:
        vector_index = VectorStoreIndex.from_documents(
            documents,
            storage_context=storage_context,
            embed_model=embed_model
        )
        print("Vector index creation completed")
    except Exception as e:
        raise RuntimeError(f"Failed to create vector index: {e}")