from litellm import completion
from dotenv import load_dotenv , find_dotenv
import os

load_dotenv(find_dotenv())




def llm_call():
    response = completion(
        model=os.getenv('MODEL'),
        messages=[{
            "role": "user",
            "content": "who is The FOunder of Pakistan"
        }]
    )
    return response['choices'][0]['message']['content']
