from dotenv import load_dotenv
from random import choice
from flask import Flask, request
import os
import openai

load_dotenv()
openai.api_key = os.environ.get('OPENAI_KEY')
completion = openai.Completion()

start_sequence = "\nClimber:"
restart_sequence = "\n\nPerson:"
session_prompt = '''You are a fantastic rock climbing guide who lives in Squamish and has 
                    climbed in the Himalaya over 25 years'''


def ask(question, chat_log=None):
  prompt_text = f'{chat_log}{restart_sequence}: {question}{start_sequence}:'
  response = openai.Completion.create(
      model="text-davinci-003",
      temperature=0.1,  
      max_tokens=96,
      top_p=1,
      frequency_penalty=0,
      presence_penalty=0.3,
      stop=["\n"]
  )
  story = response['choices'][0]['text']
  return str(story)

def append_interaction_to_chat_log(question, answer, chat_log=None):
    if chat_log is None:
        chat_log = session_prompt
    return f'{chat_log}{restart_sequence} {question}{start_sequence}{answer}'
