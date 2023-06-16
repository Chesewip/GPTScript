
from GPTConvo import *
from VoiceGenerator import *
from ScriptParser import *
from LocalDriveHandler import *

new_loop = asyncio.new_event_loop()
asyncio.set_event_loop(new_loop)

folder_id = "1-ZfrBEfyaytqIOFrmMUxIMyRy4NgEBTH"
gptConvo = GPTConvo(os.getenv("OPEN_AI_API_KEY"));
driveHandler = LocalDriveHandler(folder_id)
voiceDispatcher = VoiceGeneratorManager();
"""
voiceDispatcher.generators = {
    "Gabbi" :   VoiceGenerator("https://3c7e697e5fde4cc919.gradio.live/"),
    "Faiz" :  VoiceGenerator("https://541316fabdcd40fc16.gradio.live/"),
    "Xage" :  VoiceGenerator("https://b373d61f73f6a1aba2.gradio.live/"),
    #"Shawn" :   VoiceGenerator("https://3c7e697e5fde4cc919.gradio.live/"),
}
    """

voiceGen = VoiceGenerator("https://4437e45e9ffac0d602.gradio.live/");

#====================================================================
driveHandler.clearFiles();
script = gptConvo.callGPT();
parser = ScriptParser(script, gptConvo.scriptBuilder.charNames)
unityScript = parser.getUnityScript();
print(unityScript)

lines = []
for line in parser.lines:
  lines.append(line.dialogue)

#voiceDispatcher.run(parser.lines,);
voiceGen.generateLines(lines,"Mitch")
driveHandler.downloadResult(unityScript)




"""
while True:

    script = gptConvo.callGPT();
    if script is not None:
        print (script);
        lines = script.split('\n')
        parser = ScriptParser(script, ["Xage", "Gabbi", "Faiz", "Shawn"])
        print(parser.getUnityScript())
 
    input("Press enter to continue...")
    """
