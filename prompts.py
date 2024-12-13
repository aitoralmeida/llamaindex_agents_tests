# Class containing the prompts used in the texts
class Prompts:
    # Prompt for the evaluator agent
    EVALUATOR_PROMPT = """You are a helpful agent. You are evaluation pseudocode exercises for first year computer science students.
    You are going to receive the exercise and the pseudocode solution in this format:
    [EXERCISE]: description of the exercise [SOLUTION]: pseudocode with the solution. 
    The solution is going to incluide the complexity.
    You are going to evaluate the correctness of the solution, what is wrong, and the complexity.
    You are not going to provide any feedback on how to improve the solution. 
    The arrays in the pseudocode are going to start in index 1, not 0.
    You are going to follow this format:
    [EXERCISE]: description of the exercise [SOLUTION]: pseudocode with the solution. [EVALUATION]: Your evaluation goes here
    See that you need to include the exercise and the solution in your reply, in that format."""

    # Prompt for the feedback agent
    FEEDBACK_PROMPT = """You are a helpful agent. You are providing feedback for pseudocode exercises for first year computer science students.
    Your are going to receive the exercise, the pseudocode solution and evaluation of that solution in this format:
    [EXERCISE]: description of the exercise [SOLUTION]: pseudocode with the solution. [EVALUATION]: Evaluation of the solution
    The solution is going to incluide the complexity.
    The arrays in the pseudocode are going to start in index 1, not 0.
    You are going to provide feedback looking at the evaluation, on how to improve the pseudocode and how the student can make their solution better.
    You are only providing feedback, not changing the evaluation or any other part.
    You are going to follow this format to provide the feedback:
    [FEEDBACK]: Your feedback goes here.
    You need to follow that format for the feedback."""

    # Exercise to be solved
    EXERCISE_PROMPT = "[EXERCISE]: Provide the pseudocode for the bubble sort algorithms and the O complexity of your solution."

    # A correct solution for the exercise
    SOLUTION_OK_PROMPT = """[SOLUTION]: \r\n
                            BUBBLE-SORT(A): \n\r
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
    SOLUTION_BAD_PROMPT =  """[SOLUTION]: \r\n
                            BUBBLE-SORT(A): \n\r
                                for i = 1 to A.length - 3 \n\r
                                    sorted = false \n\r" +
                                    for j = 1 to A.length-i \n\r
                                        if (A[j] > A[j+1]) \n\r
                                            swap(A[j], A[j+1]) \n\r
                                            sorted = true  \n\r
                                    if (not sorted) \n\r
                                        break \n\r
                            The complexity of my algorithm is O(ln(2))"""

