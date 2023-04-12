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
STOP=None
MAX_TOKENS=1024
TEMPERATURE=0.75
NMAX=1
MODEL_ENGINE = "text-davinci-003"


#Set the User and AI names
USERNAME = "You"
AI_NAME = "chatGPT"

# Set the initial prompt to include a personality and habits
INITIAL_PROMPT = '''I am a friendly artificial intelligence.'''

CONVERSATION_HISTORY = INITIAL_PROMPT + "\n"

# Cycle while to continue conversation
while True:
    # Try ejectue the conversation
    try:
        print("Enter input (or 'quit' to exit):")
        # Get the user's input
        USER_TEXT = str(input("You: "))
        if USER_TEXT == 'quit':
            break
        # Check if the user typed something else don't start the conversation
        if len(USER_TEXT) > 0:
        # Set up the model and prompt
            # Update the conversation history
            CONVERSATION_HISTORY += f"{USERNAME}: {USER_TEXT}\n"
        # Get the response for the given prompt using the OpenAI API.
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
    # Provide the NameError exception to not break the code
    except NameError:
        # Print the error message
        print("You don't have passed any text")
    else:
        # Get the OpenAI API message to print to the console
        message = response.choices[0].text
        # Update the conversation history
        CONVERSATION_HISTORY += f"{AI_NAME}:{message}\n"
        # Print the response
        print(f'{AI_NAME}: {message}')
        # The function start again until the conversation finish by user
