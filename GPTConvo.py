import os
import openai
import random
import re
from characterTraits import getRandomBeckyTrait
from ScriptBuilder import *

# Load your API key from an environment variable or secret management service
openai.api_key = "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"

conversation_history = [
        {
            "role": "system",
            "content": getSystemPrompt()         
        },
]
newConvo = True;
objective = ""
currentCharacters = getCharacters();
while True:

    newInput = getNewScript();
    
    if newConvo is False:
        newInput = "Continue this story with 10 more lines. Remember, the previous objective was this : " + objective + ". In this scene one characters randomly kills another one of the characters. You can ONLY use these characters" + currentCharacters

    # Add the user's message to the conversation history
    conversation_history.append({"role": "user", "content": newInput})

    # Get the model's response
    response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",  # use your model
        messages=conversation_history
    )

    # Add the assistant's response to the conversation history
    script = response['choices'][0]['message']['content']
    conversation_history.append({"role": "assistant", "content": script})
    print (script);
    lines = script.split('\n')

    dialogue_list = []
    for line in lines:
        parsed = parse_string(line);
        if parsed is not None:
            dialogue_list.append(parsed)

    print(dialogue_list);

        #if line.startswith("[OBJECTIVE"):
         #   objective = line.split("=")[1].strip().strip("]")

    #for d in dialogue_list:
     #   name, mood, line = d
      #  print(f"Character: {name}\nMood: {mood}\nDialogue: {line}\n")

    # Limit the conversation history to the last 10 exchanges (20 messages)
    if len(conversation_history) > 3:
        conversation_history = conversation_history[-3:]

    #newConvo = False;    
    input("Press enter to continue...")

#dialogue = script.split('---')[1]
#print(dialogue)
#dialogue_list = re.findall(r"(\w+): \((\w+)\) (.*)", dialogue)

#for d in dialogue_list:
#    name, mood, line = d
#    print(f"Character: {name}\nMood: {mood}\nDialogue: {line}\n")
