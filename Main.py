
from GPTConvo import *
from ScriptParser import *

gptConvo = GPTConvo(os.getenv("OPEN_AI_API_KEY"));

while True:

    script = gptConvo.callGPT();
    if script is not None:
        print (script);
        lines = script.split('\n')
        parser = ScriptParser(script, ["Xage", "Gabbi", "Faiz", "Shawn"])
        print(parser.getUnityScript())
 
    input("Press enter to continue...")

