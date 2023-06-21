
from GPTConvo import *
from VoiceGenerator import *
from ScriptParser import *
from LocalDriveHandler import *
from EC2Grabber import *
import threading
from LocalZipper import *


gptConvo = GPTConvo(os.getenv("OPEN_AI_API_KEY"));

voiceGens = [
    #VoiceGenerator("https://d7ee9da4eb8bcfabe7.gradio.live"),
    #VoiceGenerator("https://a1f87a7aca444844d0.gradio.live")
    # Add more voice generators if needed
]

voiceDispatcher = VoiceGeneratorManager(voiceGens)


#====================================================================

#ec2 = EC2Grabber('ec2-52-53-189-156.us-west-1.compute.amazonaws.com',
 #                'C:/Users/10850K/Documents/GPT/wizPassword.pem',
  #               '/home/ubuntu/gptconvo/ai-voice-cloning/results/',
   #              'C:/Users/10850K/Documents/AI INPUTS/temp')

import time
from concurrent.futures import ThreadPoolExecutor

def generate_scripts(queue):
    while True:
        try:
            script = gptConvo.callGPT()
            parser = ScriptParser(script, gptConvo.scriptBuilder.charNames)
            unityScript = parser.getUnityScript()
            print(unityScript)
            queue.put((parser.lines, unityScript))  # Add the lines and unityScript to the queue
            time.sleep(4)
        except Exception as ex:
            print("Script creation error" + ex)
            time.sleep(1)


def process_scripts(queue):
    while True:
        if not queue.empty():
            lines, unityScript = queue.get()  # Get the lines and unityScript from the queue
            voiceDispatcher.run(lines)
            ec2.getVoiceResults()
            zip_files_in_dir("C:/Users/10850K/Documents/AI INPUTS/temp", unityScript, [line.character for line in lines])
        else:
            time.sleep(1)  # Wait for 1 second before checking the queue again


# Use a thread-safe queue to hold the scripts
queue = queue.Queue()

# Use a ThreadPoolExecutor to run the tasks in separate threads
with ThreadPoolExecutor(max_workers=2) as executor:
    executor.submit(generate_scripts, queue)
    #executor.submit(process_scripts, queue)


