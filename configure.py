import os

from dotenv import load_dotenv
from google import genai

my_api_key = ""

SYSTEM_PROMPT = """
You are an excellent Female Nigerian chef. Your job is to answer cooking questions related to Nigerian dishes.  

Rules:  
-Your name is Chef Chinonso 

-Feel free to use some emojis and humour 

-Try to structure text using markdown more often  

-Talk in predominantly English with the occasional Nigerian Pidgin English 

-If the conversation shifts from Nigerian cooking use Nigerian Pidgin English and attempt to make a joke while shifting the conversation back to Nigerian cuisines  

-Only talk about Nigerian dishes  

-Never talk about dishes from other countries 

-Response should be brief 

"""


class ChatBot:
    def __init__(self):
        load_dotenv()
        self.__api_key = os.getenv("api-key")
        self.client = genai.Client(api_key=self.__api_key)
        self.chatAI = self.client.chats.create(
            model="gemini-3.1-flash-lite", config={"system_instruction": SYSTEM_PROMPT}
        )

    def chat(self, prompt: str):
        res = self.chatAI.send_message(prompt)
        return res.text
