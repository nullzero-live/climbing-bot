from dotenv import load_dotenv
from random import choice
from flask import Flask, request
import os
import openai

load_dotenv()
openai.api_key = os.environ.get('OPENAI_KEY')
completion = openai.Completion()

start_sequence = "\nHonnold:"
restart_sequence = "\n\nClimber:"
session_prompt = '''You are a fantastic rock climbing guide who lives in Squamish and has 
                    climbed in the Himalayas, USA, Canada during your 25 year career. A climber wants advice on climbing safely.'''


def ask(question, chat_log=None):
  response = openai.Completion.create(
      model="text-davinci-003",
      prompt="You are the rock climbing professional Alex Honnold who lives in a van in Yoeemite and has  climbed in Patagonia, the USA, Canada during your 25 year career. A climber wants advice on climbing safely. Your greatest achievement is climbing El Capitan free solo. You are friendly and polite.\n\nClimber: Who are you?\nGuide: I am Alex Honnold\n\nClimber: I’d like to know more about safety please?\nGuide: I can help you with that based on my experience. Have you been climbing a long time?\n\nClimber: Can you tell me about your greatest achievement?\nGuide:Honnold:\n\nMy greatest achievement is climbing El Capitan free solo.ClimberHonnold:\n\nFantastic. Tell me more about safety?\n\n\nThere are a few things to keep in mind when climbing. First, always use a partner when possible. Second, be aware of your surroundings and be cautious when climbing. Finally, always take safety precautions, like wearing a helmet and climbing with proper gear.",
      temperature=0.5,
      max_tokens=500,
      top_p=1,
      frequency_penalty=0,
      presence_penalty=0,
      stop=["\n"]
  )
  story = response['choices'][0]['text']
  return str(story)

def append_interaction_to_chat_log(question, answer, chat_log=None):
    if chat_log is None:
        chat_log = session_prompt
    return f'{chat_log}{restart_sequence}{question}{start_sequence}{answer}'

