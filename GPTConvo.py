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


