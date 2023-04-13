"""
Program to chat with OPEN AI API de chatGPT, make questions, have a conversation and more.
"""

# inmported libraries to work
import readline
import openai
# Set API_KEY to work
API_KEY = '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'
openai.api_key = API_KEY
TOP_P=1
FREQ_PENALTY=0
PRES_PENALTY=0
STOP=["You:","chatGPT:"]
MAX_TOKENS=1024
TEMPERATURE=0.75
NMAX=1
MODEL_ENGINE = "text-davinci-003"

# Method to get the menu initial to set the mode of chat
def get_initial():
    """
        Get the initial mode of chat
    """
    print('How do you want to start?')
    print('--easy converse')
    print('--convers converse')

    start = str(input('You: '))
    # return the initial mode choosen by user
    return start

# Method to get the user input
def get_user_text():
    """
        Get the user input
    """
    # Set up the model and prompt
    print("Enter input (or 'quit' to exit):")

    user_text = str(input("You: "))

    if len(user_text) == 0:
        raise ValueError("You don't have passed any text")
    # return the user's input
    return user_text

# Method to get response from the API server
def get_response():
    """
        Get the chat message from the API server
    """
    response = openai.Completion.create(
            engine=MODEL_ENGINE,
            prompt=CONVERSATION_HISTORY,
            max_tokens=MAX_TOKENS,
            n=NMAX,
            top_p=TOP_P,
            frequency_penalty=FREQ_PENALTY,
            presence_penalty=PRES_PENALTY,
            temperature=TEMPERATURE,
            stop=STOP)
    # return the response of AI
    return response.choices[0].text

# Method to update the conversation history
def update_history(conversation_history, name, text):
    """
        Update the conversation history
    """
    if START == '--convers':
        conversation_history += f"{name}:{text}\n"
    else:
        conversation_history = f"{name}:{text}\n"

    return conversation_history

#Set the User and AI names
USERNAME = "You"
AI_NAME = "chatGPT"

# Set the initial prompt to include a personality and habits
INITIAL_PROMPT = '''I am a friendly artificial intelligence.'''
# Add to the history to give a contex
CONVERSATION_HISTORY = INITIAL_PROMPT + "\n"

# Call the method to start the menu --converts or --easy
START = get_initial()

# Cycle while to continue conversation
while True:
    # Try ejectue the conversation
    try:
        # Check if the user typed something else don't start the conversation
        USER_TEXT = get_user_text()

    # Provide the ValueError exception to not break the code
    except ValueError as e:
    # Print the error message
        print(e)
    else:
        # Check if the user want to exit the conversation
        if USER_TEXT == 'quit':
            break

        # Update the conversation history
        CONVERSATION_HISTORY = update_history(CONVERSATION_HISTORY, USERNAME, USER_TEXT)

        # Get the OpenAI API message to print to the console
        message = get_response()

        # Update the conversation history
        CONVERSATION_HISTORY = update_history(CONVERSATION_HISTORY, AI_NAME, message)

        # Print the response
        print(f'{AI_NAME}: {message}')
        # The function start again until the conversation finish by user
