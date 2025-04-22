import json
from client_handler import Clients

clients = Clients()

class JsonFileChunking:
    """
        Handles Chunking and Embeddings for a Json File
    """
    def __init__(self):
        self.embed_model = clients.get_embed_model()
        
    def load_data(self, local_file_path):
        with open(local_file_path, 'r') as f:
            data = json.load(f)
        return data
    
    def get_chunk(self, data):
        chunks = []
        for qa in data["qas"]:
            chunks.append(f"Q: {qa['question']} \n A: {qa['answer']}")            


        return chunks
