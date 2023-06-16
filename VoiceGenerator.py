from gradio_client import Client
from ScriptParser import *
import asyncio
from concurrent.futures import ThreadPoolExecutor
import concurrent.futures
from typing import List


class VoiceGenerator:

    def __init__(self, url):
        self.client = Client(url)
        self.url = url
        self.input_prompt = ""
        self.line_delimiter = "\\n"
        self.emotion = "Angry"
        self.custom_emotion = None
        self.voice = "Random"
        self.microphone_source = None
        self.voice_chunks = 0
        self.candidates = 1
        self.seed = None
        self.samples = 2
        self.iterations = 16
        self.temperature = 1.0
        self.diffusion_samplers = "DDIM"
        self.pause_size = 8
        self.cvvp_weight = 0
        self.top_p = 0.8
        self.diffusion_temperature = 1
        self.length_penalty = 7
        self.repetition_penalty = 7
        self.conditioningfree_k = 2
        self.experimental_flags = ["Conditioning-Free"]
        self.use_original_latents_method_ar = False
        self.use_original_latents_method_diffusion = False
        self.api = "/generate"

    def generateLines(self, lines, voice):
        for line in lines:
            self.generateLine(line, voice)

    def generateLine(self, text, voice):
        try:
            result = self.client.predict(
            text,
            self.line_delimiter,
            self.emotion,
            self.custom_emotion,
            voice,
            self.microphone_source,
            self.voice_chunks,
            self.candidates,
            self.seed,
            self.samples,
            self.iterations,
            self.temperature,
            self.diffusion_samplers,
            self.pause_size,
            self.cvvp_weight,
            self.top_p,
            self.diffusion_temperature,
            self.length_penalty,
            self.repetition_penalty,
            self.conditioningfree_k,
            self.experimental_flags,
            self.use_original_latents_method_ar,
            self.use_original_latents_method_diffusion,
            api_name = self.api
        )
            print("File Generated")
        except:
            print("File Generated, return failed though?")


class VoiceGeneratorManager:

    def __init__(self):
        self.generators = {}
        self.executor = concurrent.futures.ThreadPoolExecutor(max_workers=20)
        self.loop = asyncio.get_event_loop()

    def dispatchGenerators(self, dialogueLines : list[DialogueLine] ):

        charLines = {}

        for line in dialogueLines:
            if line.character not in charLines:
                charLines[line.character] = []
            charLines[line.character].append(line.dialogue)

        tasks = []

        for character, lines in charLines.items():
            charGen = self.generators.get(character)
            if charGen is None:
                print(f"No generator for character {character}")
                continue

            task = self.loop.create_task(self.loop.run_in_executor(self.executor, charGen.generateLines, lines))
            tasks.append(task)

        return tasks

    def run(self, dialogueLines : list[DialogueLine] ):
        tasks = self.dispatchGenerators(dialogueLines)
        if tasks:
            done, pending = self.loop.run_until_complete(asyncio.wait(tasks))




