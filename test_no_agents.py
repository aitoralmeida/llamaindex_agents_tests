from llama_index.llms.openai import OpenAI
from llama_index.llms.openai import OpenAI
from llama_index.core.llms import ChatMessage
from llama_index.core.llms import (
    ChatMessage,
    ImageBlock,
    TextBlock,
    MessageRole,
)


import configparser
from pathlib import Path
import requests
import shutil

from prompts import Prompts

"""
TODO:
        * The image extractor keeps correcting the pseudocode and the complexity in the wrong examples.
        * Try RAG
        * Try Agents

"""
# gets the api_key for open_ai from the config.ini file
def get_api_key():
    config = configparser.ConfigParser()
    config.read('config.ini')
    return config['OPEN_AI']['api_key']

# extracts the pseudocode and the complexity from a picture
def extract_image_text(llm, img_path):
    messages = ChatMessage(
        role=MessageRole.USER,
        blocks=[
            TextBlock(text=Prompts.IMAGE_EXTRACTOR_PROMPT),
            ImageBlock(path=img_path, image_mimetype="image/jpeg"),
        ],
    )
    response = llm.chat([messages])
    return response

# evaluates a solution, without providing feedback.
def get_exercise_evaluation(llm, prompt, exercise, solution):
    messages = [
        ChatMessage(
            role="system", content=prompt
        ),
        ChatMessage(role="user", content=Prompts.EXERCISE_HEADER + exercise + Prompts.SOLUTION_HEADER + solution),
    ]
    evaluation = llm.chat(messages)
    return evaluation

# uses the evaluation to provide feedback on how to improve the solution
def get_exercise_feedback(llm, prompt, exercise, solution, evaluation):
    messages = [
        ChatMessage(
            role="system", content=prompt
        ),
        ChatMessage(role="user", content=Prompts.EXERCISE_HEADER + exercise + Prompts.SOLUTION_HEADER + solution + Prompts.EVALUATION_HEADER + evaluation),
    ]
    feedback = llm.chat(messages)
    return feedback

if __name__ == '__main__':
    # gpt-4o
    # gpt-4o-mini
    # To work in images you need to use gpt-4o
    
    # If true, it expects a picture of the pseudocode, if false, it expects text.
    use_image = True

    if use_image:
        llm = OpenAI(
            model="gpt-4o",
            api_key= get_api_key()
        )
        img_path = Path().resolve() / "./test_images/bubble_sort_bad.jpg"
        pseudocode = extract_image_text(llm, img_path)
        print ("Extracted text:")
        print (pseudocode)
        evaluation = get_exercise_evaluation(llm, Prompts.EVALUATOR_PROMPT, str(pseudocode), Prompts.SOLUTION_1_BAD_PROMPT)
        print (Prompts.EVALUATION_HEADER + str(evaluation))
        feedback = get_exercise_feedback(llm, Prompts.FEEDBACK_PROMPT, Prompts.EXERCISE_1_PROMPT, Prompts.SOLUTION_1_BAD_PROMPT, str(evaluation))
        print (Prompts.FEEDBACK_HEADER + str(feedback))
    else:
        llm = OpenAI(
            model="gpt-4o-mini",
            api_key= get_api_key()
        )
        evaluation = get_exercise_evaluation(llm, Prompts.EVALUATOR_PROMPT, Prompts.EXERCISE_1_PROMPT, Prompts.SOLUTION_1_BAD_PROMPT)
        print (Prompts.EVALUATION_HEADER + str(evaluation))
        feedback = get_exercise_feedback(llm, Prompts.FEEDBACK_PROMPT, Prompts.EXERCISE_1_PROMPT, Prompts.SOLUTION_1_BAD_PROMPT, str(evaluation))
        print (Prompts.FEEDBACK_HEADER + str(feedback))


