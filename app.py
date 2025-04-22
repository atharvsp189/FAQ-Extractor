from scraper import extract_qa_pairs
from chunking_handler import JsonFileChunking
from qdrant_handler import upload_embedding

chunk_obj = JsonFileChunking()

name = input("Enter Name of a Project: ")
url = input("Enter URL: ")
collection = input("Enter collection name: ")

extraction_file_path = extract_qa_pairs(name, url)
print("Data Extraction Done")
data = chunk_obj.load_data(extraction_file_path)
print("Data Loading Done")
chunks = chunk_obj.get_chunk(data)
print("Data Chunking Done")
print("-"*20)
print(chunks)

upload_embedding(
    chunks=chunks, 
    url=url,
    collection=collection,
)