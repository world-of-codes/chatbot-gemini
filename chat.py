from config import getkey
from google import genai

client=genai.Client(api_key=getkey())

def talk(question:str)->str:
    '''
    CHATBOT LOGIC
    '''
    response=client.models.generate_content(
        model='gemini-3.5-flash',
        contents=question
    )
    return response.text

