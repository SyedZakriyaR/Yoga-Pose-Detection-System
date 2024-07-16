import openai

# Set your OpenAI API key
openai.api_key = "your_openai_api_key"

# Define the function to be analyzed
function_code = """
def example_function(x, y):
    \"\"\"Adds two numbers and returns the result.\"\"\"
    return x + y
"""

# Define prompts for different details
prompts = {
    "description": "Provide a detailed description of the following Python function:\n\n" + function_code,
    "parameters": "List the parameters of the following Python function with their data types:\n\n" + function_code,
    "test_cases": "Generate test cases for the following Python function:\n\n" + function_code,
    "optimized_function": "Provide an optimized version of the following Python function:\n\n" + function_code,
    "rewritten_function": "Rewrite the following Python function in a different style:\n\n" + function_code,
    "bugs": "Identify any bugs in the following Python function:\n\n" + function_code,
    "variable_descriptions": "Describe the variables used in the following Python function:\n\n" + function_code,
    "return_type": "What is the return type of the following Python function:\n\n" + function_code,
    "arguments": "What are the arguments of the following Python function:\n\n" + function_code
}

# Function to call OpenAI API with a given prompt
def get_llm_response(prompt):
    response = openai.Completion.create(
        engine="text-davinci-003",
        prompt=prompt,
        max_tokens=150
    )
    return response.choices[0].text.strip()

# Extract details from the function
function_details = {key: get_llm_response(prompt) for key, prompt in prompts.items()}

# Print the extracted details
for key, detail in function_details.items():
    print(f"{key.capitalize()}:\n{detail}\n{'='*40}\n")