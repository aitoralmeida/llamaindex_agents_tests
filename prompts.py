# Class containing the prompts used in the texts
# Expected formats:
# To get the evaluation of an exercise: [EXERCISE]: description of the exercise [SOLUTION]: pseudocode with the solution. 
# To get the feedback of an exercise: [EXERCISE]: description of the exercise [SOLUTION]: pseudocode with the solution. [EVALUATION]: Your evaluation goes here
class Prompts:
    # Prompt for the feedback agent
    IMAGE_EXTRACTOR_PROMPT = """You are a helpful agent. Your are transcribing text from images.
    Transcribe the text without changing it. 
    The pseudocode might be wrong, don't correct it.
    Be cautious to mantain the text  indentation. The indentation will be similar to Python.
    Do not say anything else, just transcribe it.
    Don't change the original text, make sure that the trancribed text is the same.
    """

    # Prompt for the evaluator agent
    EVALUATOR_PROMPT = """You are a helpful agent. You are evaluation pseudocode exercises for first year computer science students.
    You are going to receive the exercise and the pseudocode solution in this format:
    [EXERCISE]: description of the exercise [SOLUTION]: pseudocode with the solution. 
    The solution is going to incluide the complexity.
    You are going to evaluate the correctness of the solution, what is wrong, and the complexity.
    You are not going to provide any feedback on how to improve the solution. 
    The arrays in the pseudocode are going to start in index 1, not 0.
    To talk about the worst case complexity, use the big O notation. To talk about the best case complexity use the big omega notation.
    """

    # Prompt for the feedback agent
    FEEDBACK_PROMPT = """You are a helpful agent. You are providing feedback for pseudocode exercises for first year computer science students.
    You are going to receive the exercise, the pseudocode solution and evaluation of that solution in this format:
    [EXERCISE]: description of the exercise [SOLUTION]: pseudocode with the solution. [EVALUATION]: Evaluation of the solution
    The solution is going to incluide the complexity.
    The arrays in the pseudocode are going to start in index 1, not 0.
    You are going to provide feedback looking at the evaluation, on how to improve the pseudocode and how the student can make their solution better.
    You are only providing feedback, not changing the evaluation or any other part.
    To talk about the worst case complexity, use the big O notation. To talk about the best case complexity use the big omega notation.
    """  

    # Header for the exercise description section
    EXERCISE_HEADER = "[EXERCISE]: "
    # Header for the solution section
    SOLUTION_HEADER = "\r\n[SOLUTION]: \r\n"
    # Header for the evaluation section
    EVALUATION_HEADER = "\r\n[EVALUATION]: "
    # Header for the feedback section
    FEEDBACK_HEADER =  "[FEEDBACK]: "

    # Exercise to be solved
    EXERCISE_1_PROMPT = "Provide the pseudocode for the bubble sort algorithms and the O complexity of your solution."

    # A correct solution for the exercise
    SOLUTION_1_OK_PROMPT = """BUBBLE-SORT(A): \n\r
                                for i = 1 to A.length-1 \n\r
                                    sorted = false \n\r" +
                                    for j = 1 to A.length-i \n\r
                                        if (A[j] > A[j+1]) \n\r
                                            swap(A[j], A[j+1]) \n\r
                                            sorted = true  \n\r
                                    if (not sorted) \n\r
                                        break \n\r
                            The complexity of my algorithm is O(n^2) """

    # An incorrect solution for the exercise
    SOLUTION_1_BAD_PROMPT =  """BUBBLE-SORT(A): \n\r
                                for i = 1 to A.length - 3 \n\r
                                    sorted = false \n\r" +
                                    for j = 1 to A.length-i \n\r
                                        if (A[j] > A[j+1]) \n\r
                                            swap(A[j], A[j+1]) \n\r
                                            sorted = true  \n\r
                                    if (not sorted) \n\r
                                        break \n\r
                            The complexity of my algorithm is O(ln(2))"""

