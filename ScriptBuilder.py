import random
import re

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
    "Believing the dishwasher will wash clothes too"
]


characters = [
    "Shawn- A character always has R rated replies",
    #"Naman - An old man that is always interjecting with random phrases/sentences that make no sense",
    "Gabbi - A character who is addicted to drugs and has mommy issues",
    #"Mitch- A character who tries to be a gangsta",
    "Xage - A knowledgable person who speaks like a caveman",
    "Faiz - A schizophrenic character",
    #"Wiz - A virgin who is afraid of talking to women"
    ]

names = [
    "Shawn",
    "Gabbi",
    "Xage",
    "Faiz"
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
    {"SIEZENOCARE" : "{} has a siezure and dies. No one is fazed. {} still has dialouge lines but they say nothing"},
    {"SIEZECARE" : "{} s has a siezure and dies. Everyone freaks out. {} still has dialouge lines but they say nothing"},
    {"SECRET": "{} announces they have a secret, and then tell the most innapropriate secret"},
    {"QUAKE" : "A earthquake happens, but only {} can notice"},
    {"REPEAT" : "{} only repeats a single phrase"},
    {"STROKE" : "{} has a stroke and all their dialouge becomes hhhhhhhhhhhhhhhhhhhhhhhhhh"}
]

def getCharacters():
    numCharacters = random.randrange(4, 5)
    print(numCharacters)
    chars = unique_random_items(characters, numCharacters)
    outputString = ""
    for character in chars:
        outputString += character + "\n"
    return outputString

def rollForRandomEvent():
    eventName, eventDescrip = list(random.choice(randomEvents).items())[0]
    numPlaceHolders = eventDescrip.count("{}")
    chosen_names = random.sample(names, numPlaceHolders)
    result = eventDescrip.format(*chosen_names)
    return "['RANDOM EVENT'= " + eventName +  " " + chosen_names[0] + "] "  + result

def unique_random_items(source_list, num_items):
    container = set()  # Using a set to enforce uniqueness.
    while len(container) < num_items:
        item = random.choice(source_list)
        container.add(item)  # If the item is already in the set, it won't be added again.
    return list(container)

def getNewScript():
    return """Write me a dialouge. The characters are foul mouthed. They are talking about""" + random.choice(funny_topics) + """
    You can ONLY Use these characters : """ + getCharacters() + """.
    """+ rollForRandomEvent() + """. 
    Start every dialouge line with # . 

    Format it as such #[Character] (emotion) dialouge. Do not include scene directions."""

def getSystemPrompt():
    return """
            Write some funny dialouge for characters similar to South Park.
            The characters like to swear alot. They always say morally wrong things. Come up with a funny topic for our characters to talk about.
                        
            ONLY If I say [RANDOM EVENT =], add the tag [RANDOM EVENT = ] in the script, and follow whatever the random event says to do.
            """

def parse_string(text):

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