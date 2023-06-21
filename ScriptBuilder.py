import random
import re

class ScriptObjects:

    funny_topics = [
    "The nutritional value of cotton candy",
    "Ways to use a toaster that doesn't involve bread",
    "Believing they discovered a new color",
    "Deciding which sock goes on which foot",
    "Using a GPS to navigate their own house",
    "Debating if plants can feel pain",
    "Confusing seagulls for penguins because they're both birds",
    "Setting a booby trap for the Tooth Fairy",
    "Arguing that the moon is made of cheese",
    "Testing if umbrellas work as parachutes",
    "Pouring cereal before realizing there's no milk",
    "Trying to microwave a microwave",
    "Building a DIY roller coaster in their backyard",
    "Looking for the left-handed screwdriver",
    "Insisting that 'gullible' isn't in the dictionary",
    "Wondering why animals don't wear clothes",
    "Naming each of their 142 pet rocks",
    "Finding Atlantis in a bathtub",
    "The quest for the end of the rainbow",
    "Searching for Bigfoot in their backyard",
    "Trying to sell their 'invisible' art",
    "Wondering why cats don't bark",
    "Convinced they're the reincarnation of a historical figure",
    "Hunting for unicorns in a zoo",
    "Believing they're allergic to water",
    "Trying to convince others they've invented a new letter",
    "Thinking they can talk to plants",
    "Debating if they can outsmart a dolphin",
    "Planning to open a fish walking service",
    "Making the world's largest paper airplane",
    "Comparing themselves to Albert Einstein because they're both humans",
    "Trying to figure out why pizzas are round but the boxes are square",
    "Believing every movie is based on a true story",
    "Wondering why there are no B-sharp or E-sharp in music",
    "Starting a fundraiser to fix the Leaning Tower of Pisa",
    "Opening a window to let WiFi signal in",
    "Trying to learn 'snake language' to communicate with reptiles",
    "Convincing themselves they're invisible",
    "Trying to out-stare the sun",
    "Debating whether the Earth is a giant doughnut",
    "Attempting to dig a hole to China",
    "A deep discussion about the aerodynamics of a taco",
    "Believing they can beat a cheetah in a foot race",
    "Thinking they can catch a cold from ice cream",
    "Insisting that Santa Claus is their best friend",
    "Trying to walk their pet fish",
    "Confusing a cactus for a cucumber",
    "Starting a petition to make unicorns the national animal",
    "Trying to teach a dog to meow",
    "Thinking there's a secret message in a shampoo's instructions",
        "Believing the dishwasher will wash clothes too",
    "The mystery of disappearing pens",
    "Trying to grow a money tree",
    "Arguing that earth could be square",
    "Using a GPS to find their way around their own house",
    "Believing they've invented a new color",
    "Thinking they can dig a hole to China",
    "Attempting to outsmart a pigeon",
    "Starting a pet rock collection, and naming each one",
    "Making a plan to kidnap the Tooth Fairy",
        "Creating a fashion line for houseplants",
    "Searching for a diet where they can eat only candies",
    "Considering a career as a professional snail racer",
    "Explaining why they think the moon landing was fake",
    "Wondering why cats can't send emails",
    "Hosting an annual sock-losing ceremony",
    "Planning to build a boat using duct tape",
    "Looking for the button to download more RAM",
    "Arguing that pizzas should be square to match the box",
    "Trying to learn the language of ants",
    "Confusing a car wash for a large shower",
    "Deciding that cows are just really big dogs",
    "Looking for ways to charge their phone with a potato",
    "Thinking they've cracked the code to the lottery",
    "Trying to sell sand at the beach",
    "Planning a trip to the sun at night, so it's cooler",
    "Trying to make a DIY elevator in their one-story house",
    "Convinced their goldfish can talk, but only when they're not around",
    "Rehearsing for the annual pillow fight championship",
    "Attempting to set a world record in blinking",
    "Insisting on serving a raw turkey because it's healthier",
    "Attempting to outrun their own shadow",
    "Believing that going to bed with shoes on will make them run faster in dreams",
    "Planning a fishing trip in their swimming pool",
    "Trying to domesticate a wild squirrel",

    ]
 



    characters = [
        ("Shawn", "A character always has R rated replies"),
        #"Naman - An old man that is always interjecting with random phrases/sentences that make no sense",
        ("Gabbi", "The main female protaganist"),
        #("Mitch", "A character who tries to be a gangsta"),
        ("Xage", "A knowledgable person who speaks like a caveman"),
        ("Faiz" , "A mentally handicapped crazy character"), #schizophrenic character
    #"Wiz - A virgin who is afraid of talking to women"
    ]

    names = [
    "Shawn",
    "Gabbi",
    "Xage",
    "Faiz",
    ]

    emotions = [ 
    "Angry", "Sad", "Happy", "Disgusted", "Neutral"
    ]

    locations = [
    "Home", "Bar", "Alley", "Park", "Mall"
    ]

    randomEvents = [
    {"POOP": "In the middle of the script, {} ubruptly shits them selves"},
    {"GAY" : "{} ubruptly announces they are gay"},
    {"SHOOT" : "{} shoots {}"},
    {"SIEZENOCARE" : "{} has a siezure and dies. No one is fazed. {} only says ... now"},
    {"SIEZECARE" : "{} s has a siezure and dies. Everyone freaks out. {} only says ... now"},
    {"SECRET": "{} immediately tells the most innapropriate secret. Add this the line before they say the secret"},
    #{"QUAKE" : "A earthquake happens, but only {} can notice"},
    #{"REPEAT" : "{} only repeats a single phrase"},
    {"STROKE" : "{} has a stroke and all their dialouge becomes hhhhhhhhhhhhhhhhhhhhhhhhhh"},
    {"ALIEN" : "{} is abducted by aliens and is now gone"},
    {"CAR" : "{} is hit by a car and dies"},
    {"EXPLODE" : "{} randomly explodes and dies"}
    ]



class ScriptBuilder:

    def __init__(self):
        self.scriptObjects = ScriptObjects()
        self.characters = self.selectCharactersForScript()
        self.charNames = []
        for char in self.characters:
            self.charNames.append(char[0])


    def unique_random_items(self,source_list, num_items):
        container = set()  # Using a set to enforce uniqueness.
        while len(container) < num_items:
            item = random.choice(source_list)
            container.add(item)  # If the item is already in the set, it won't be added again.
        return list(container)


    def selectCharactersForScript(self):
        self.scriptObjects.characters;
        numCharacters = random.randrange(2, 5)
        return self.unique_random_items(self.scriptObjects.characters, numCharacters)


    def getCharactersString(self):
        outputString = ""
        for char in self.characters:
            outputString += char[0] + " - " + char[1] + "\n"
        return outputString;

    def rollForRandomEvent(self):
        num = random.randrange(0,10)
        num =4;
        if num > 2:
            eventName, eventDescrip = list(random.choice(self.scriptObjects.randomEvents).items())[0]
            numPlaceHolders = eventDescrip.count("{}")
            chosen_names = random.sample(self.charNames, numPlaceHolders)
            result = eventDescrip.format(*chosen_names)
            return "Add this on a new line in the middle of the script the line before it happens and follow what it says '[RANDOM EVENT= " + eventName +  " " + " ".join(chosen_names) + "]' "  + result
        else:
            return ""

    
    #They are talking about """ + random.choice(self.scriptObjects.funny_topics) +
    #At the end of the script '%' + write a 1 sentence summary of what happened in this scene
    def getNewScript(self):

        return """Write me a dialouge. The characters are foul mouthed.
        """ + """ 
       You can ONLY Use these characters : """ + self.getCharactersString() + """.
        """+ self.rollForRandomEvent() + """. 
        Start every dialouge line with # . 

        Format it as such #[Character] (emotion): dialouge. Do not include scene directions.
        
        """

    def getSystemPrompt(self):
        return """
                Write some funny dialouge for characters similar to South Park.
                The characters like to swear alot. They always say morally wrong things.
                Come up with a funny topic for our characters to talk about.
                        
                """

    def parse_string(self,text):

        if not text.startswith('#'):
            return None

        # Remove the hash character
        text = text[1:]

        # Find the first parenthesis (the start of the mood)
        mood_start = text.find('(')

        # Find the end of the mood
        mood_end = text.find(')')

        # Extract the name, mood and dialogue
        name = text[:mood_start].strip()
        mood = text[mood_start+1:mood_end]
        dialogue = text[mood_end+2:].strip()

        # Return as a dictionary
        return {
            'name': name,
            'mood': mood,
            'dialogue': dialogue
        }