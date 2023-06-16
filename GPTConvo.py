import os
import openai
import random
import re
from ScriptBuilder import *


class GPTConvo:

    def __init__(self, apiKey ):
        self.scriptBuilder = ScriptBuilder();
        openai.api_key = apiKey;
        self.conversation_history = [
        {
            "role": "system",
            "content": self.scriptBuilder.getSystemPrompt()         
        }]

    def callGPT(self, retries = 3):
        if retries < 0:
            print("Failed after several retries.")
            return None

        self.conversation_history.append({"role": "user", "content": self.scriptBuilder.getNewScript()})

        try:
            response = openai.ChatCompletion.create(
                model="gpt-3.5-turbo",  # use your model
                messages=self.conversation_history
            )
            self.conversation_history.append({"role": "assistant", "content": response['choices'][0]['message']['content']})
            return response['choices'][0]['message']['content']

        except Exception as ex:
            print(ex);
            self.callGPT(retries -1)

gptConvo = GPTConvo(os.getenv("OPEN_AI_API_KEY"));

while True:

    script = gptConvo.callGPT();
    if script is not None:
        print (script);
        lines = script.split('\n')

        #dialogue_list = []
        #for line in lines:
         #   parsed = scriptBuilder.parse_string(line);
          #  if parsed is not None:
           #     dialogue_list.append(parsed)

#        print(dialogue_list);

        #if line.startswith("[OBJECTIVE"):
         #   objective = line.split("=")[1].strip().strip("]")

        #for d in dialogue_list:
         #   name, mood, line = d
          #  print(f"Character: {name}\nMood: {mood}\nDialogue: {line}\n")
 
    input("Press enter to continue...")
