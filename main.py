from GPTConvo import *

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
