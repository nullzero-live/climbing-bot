#Rock climbing instructor
from dotenv import load_dotenv
import os
import openai

load_dotenv()

#Set openAI key
def set_openai_key(key):
    """Sets OpenAI key."""
    openai.api_key = key

#OpenAI key info
KEY_NAME = os.getenv("OPENAI_KEY")
set_openai_key(KEY_NAME)

completion = openai.Completion()

start_sequence = "\nmountainbot:"
restart_sequence = "\n\nPerson:"
session_prompt = '''Johnny is a mountaineering and rock climbing instructor that lives in Squamish, Canada. He speaks directly, and prefers to be honest 
                    with people he speaks to because of safety reasons. He has lived all over the world and knows people like Alex Honnold, John Long and knew the Huber brothers.
                    The instructor also knows Reinhold Messler well and likes to refer to his talents regularly. He has climbed all over the world including Yosemite and the Himalaya. 
                    Two highlights including The Nose on El Capitan, and Ama Dablam in the Himalaya.'''


def ask(questionBot, chat_log = None):
    questionBot = f'{chat_log}{restart_sequence}:{questionBot}{start_sequence}:'
    completion = openai.Completion.create(
      engine="text-davinci-003",
      prompt= questionBot,
      temperature=0.4,
      max_tokens=96,
      top_p=1,
      frequency_penalty=0,
      presence_penalty=0.3,
      stop=["\n"],
    )

    response = completion.choices[0].text
    return str(response)



def append_interaction_to_chat_log(question, answer, chat_log=None):
    if chat_log is None:
        chat_log = session_prompt
    return f'{chat_log}{restart_sequence} {question}{start_sequence}{answer}'

