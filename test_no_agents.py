from llama_index.llms.openai import OpenAI
from llama_index.llms.openai import OpenAI
from llama_index.core.llms import ChatMessage

import configparser

from prompts import Prompts

config = configparser.ConfigParser()
config.read('config.ini')


llm = OpenAI(
    model="gpt-4o-mini",
    api_key=config['OPEN_AI']['api_key']
)

messages = [
    ChatMessage(
        role="system", content=Prompts.EVALUATOR_PROMPT
    ),
    ChatMessage(role="user", content=Prompts.EXERCISE_PROMPT + " \r\n" + Prompts.SOLUTION_BAD_PROMPT),
]
evaluation = llm.chat(messages)
print("*" * 50) 
print("******EVALUTION********\r\n")
print (str(evaluation))

messages = [
    ChatMessage(
        role="system", content=Prompts.FEEDBACK_PROMPT
    ),
    ChatMessage(role="user", content=str(evaluation)),
]
feedback = llm.chat(messages)

print("\r\n"+"*" * 50) 
print("******Feedback********\r\n")
print (feedback)
