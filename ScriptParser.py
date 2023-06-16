
from tkinter.font import names


class DialogueLine:

    def __init__(self, charName,emotion,line):
        self.character = charName
        self.emotion = emotion
        self.dialogue = line

class ScriptParser:

    def __init__(self, script, valid_names):
        self.script = script
        self.valid_script_names = valid_names
        self.lines = self.parse_lines(script,valid_names)

    def parse_lines(self, script, valid_names):
        dLines = []
        lines = script.split('\n')
        for line in lines:
            newDLine = self.parse_line(line,valid_names)
            if newDLine is not None:
                dLines.append(newDLine)
        self.lines = dLines
        return dLines


    def parse_line(self, line, valid_names):
        if not line.startswith("#"):
            return None

        line = line[1:]  # remove the leading '#'
        name_end = line.find(' ')  # find the end of the name
        name = line[:name_end]  # extract the name

        if name not in valid_names:
            return None

        # Find the end of the emotion and check for the colon
        emotion_end = line.find(')')
        if line[emotion_end + 1] != ':':
            # Insert the colon
            line = line[:emotion_end + 1] + ':' + line[emotion_end + 1:]

        emotion_start = line.find('(') + 1  # find the start of the emotion
        emotion = line[emotion_start:emotion_end]  # extract the emotion

        dialogue_start = line.find(':') + 2  # find the start of the dialogue
        dialogue = line[dialogue_start:]  # extract the dialogue
    
        return DialogueLine(name,emotion,dialogue)

    def getUnityScript(self):
        outputString = ""
        for dLine in self.lines:
            nameString = "[NAME={}]".format(dLine.character)
            outputString += (nameString + "  " + dLine.dialogue + "\n")
        return outputString



