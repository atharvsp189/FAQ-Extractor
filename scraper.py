import asyncio
from browser_use import Agent, Browser, BrowserConfig, Controller
from typing import List
import json
from client_handler import Clients
from schema import qa_data

clients = Clients()
llm = clients.get_llm()

browser = Browser(
    config=BrowserConfig(
        browser_binary_path=r"C:\\Program Files\\Google\\Chrome\\Application\\chrome.exe",
    )
)

controller = Controller(output_model=qa_data)

Task = "get the all question and answer pair that exist on the webpage"


async def extract_qa_pairs_async(name: str, url: str):
    
    # Performing Intial action required
    initial_actions = [
        {'open_tab': {'url': url}},
    ]
    
    agent = Agent(
        task=Task,
        llm=llm,
        browser=browser,
        controller=controller,
        initial_actions=initial_actions,
        save_conversation_path="logs/conversation"
    )
    
    print("Agent Creation Done")
    
    history = await agent.run()
    result = history.final_result()
    print("Got the Result")
    
    if result:
        print("Result :", "-"*20)
        # Parse the JSON string to a Python dictionary
        try:
            result_dict = json.loads(result)
            qa_extr = qa_data.model_validate(result_dict)
            
            file_path = f"extracted_data/{name}.json"
            with open(file_path, "w") as file:
                json.dump(qa_extr.model_dump(), file, indent=4)
                
            print("Successfully Extracted Content")
        except json.JSONDecodeError:
            print("Error decoding JSON from LLM response")
            print(f"Raw result: {result}")
        except Exception as e:
            print(f"Error validating data: {str(e)}")
    else:
        print("No result found.")
    
    await browser.close()
    
    return file_path

def extract_qa_pairs(name:str, url: str):
    return asyncio.run(extract_qa_pairs_async(name, url))

if __name__ == '__main__':
    print("Staring Program")
    qads = extract_qa_pairs()
    print("-"*20)
    print("Result :", qads)
