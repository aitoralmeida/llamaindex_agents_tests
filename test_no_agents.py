from llama_index.llms.openai import OpenAI
from llama_index.llms.openai import OpenAI
from llama_index.core.llms import ChatMessage

import configparser

from prompts import Prompts

def get_api_key():
    config = configparser.ConfigParser()
    config.read('config.ini')
    return config['OPEN_AI']['api_key']

def get_exercise_evaluation(llm, prompt, exercise, solution):
    messages = [
        ChatMessage(
            role="system", content=prompt
        ),
        ChatMessage(role="user", content=Prompts.EXERCISE_HEADER + exercise + Prompts.SOLUTION_HEADER + solution),
    ]
    evaluation = llm.chat(messages)
    return evaluation

def get_exercise_feedback(llm, prompt, exercise, solution, evaluation):
    messages = [
        ChatMessage(
            role="system", content=prompt
        ),
        ChatMessage(role="user", content=Prompts.EXERCISE_HEADER + exercise + Prompts.SOLUTION_HEADER + solution + Prompts.EVALUATION_HEADER + evaluation),
    ]
    feedback = llm.chat(messages)
    return feedback



llm = OpenAI(
    model="gpt-4o-mini",
    api_key= get_api_key()
)

evaluation = get_exercise_evaluation(llm, Prompts.EVALUATOR_PROMPT, Prompts.EXERCISE_1_PROMPT, Prompts.SOLUTION_1_BAD_PROMPT)
print (Prompts.EVALUATION_HEADER + str(evaluation))
feedback = get_exercise_feedback(llm, Prompts.FEEDBACK_PROMPT, Prompts.EXERCISE_1_PROMPT, Prompts.SOLUTION_1_BAD_PROMPT, str(evaluation))
print (Prompts.FEEDBACK_HEADER + str(feedback))

""" messages = [
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
print (feedback) """
