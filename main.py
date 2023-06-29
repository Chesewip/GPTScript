
from GPTConvo import *
from VoiceGenerator import *
from ScriptParser import *
from LocalDriveHandler import *
from EC2Grabber import *
import threading
from LocalZipper import *
from StreamLabsClient import *
import os
from pathlib import Path


gptConvo = GPTConvo(os.getenv("OPEN_AI_API_KEY"));

voiceGens = [
    VoiceGenerator("https://956fff992f57c85934.gradio.live"),
    VoiceGenerator("https://181f7a2a6f70f2f1d1.gradio.live")
    # Add more voice generators if needed
]

voiceDispatcher = VoiceGeneratorManager(voiceGens)


#====================================================================

pem_path = Path('Documents/GPT/wizPassword.pem')
local_dir = Path('Documents/AI INPUTS/temp')

ec2 = EC2Grabber(
    'ec2-52-53-212-50.us-west-1.compute.amazonaws.com',
    str(Path.home() / pem_path),  # where the password file is
    '/home/ubuntu/gptconvo/ai-voice-cloning/results/',
    str(Path.home() / local_dir)  #where to temp put the files when we grab them from EC2
)

import time
from concurrent.futures import ThreadPoolExecutor

def generate_scripts(queue):
    while True:
        try:
            if (queue.qsize() > 2):
                time.sleep(30)
            script = gptConvo.callGPTForOneOffScript()
            parser = ScriptParser(script, gptConvo.scriptBuilder.charNames)
            unityScript = parser.getUnityScript()
            print(unityScript)
            queue.put((parser.lines, unityScript))  # Add the lines and unityScript to the queue
            time.sleep(10)
        except Exception as ex:
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
    executor.submit(process_scripts, queue)


