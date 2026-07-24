import nltk
from nltk.chat.util import Chat,reflections
import geocoder

lat = 0
long =0

def get_current_location():
    try:
        # Get location based on IP address
        g = geocoder.ip('me')
        
        if g.ok and g.latlng:
            latitude, longitude = g.latlng
            global lat, long
            lat = latitude
            long = longitude
        else:
            print("Unable to retrieve location. Please check your internet connection.")
    
    except Exception as e:
        print(f"An error occurred: {e}")

get_current_location()

pairs = [
    [
        r"my name is (.*)",
        ['Hello %1, How are you today?']
    ],
    [
        r"hi|hello|hey",
        ['Hello','Hey there']
    ],
    [
        r'what is your name?',
        ['I am a bot created my Diyan Amin. You can call me Botone']
    ],
    [
        r'how are you?',
        ["I'm doing good, how about you?"]
    ],
    [
        r'sorry (.*)',
        ["Dont do it again.","Why did you do that?"]
    ],
    [
        r'I am fine',
        ['Great to hear that, how can I help you?']
    ],
    [
        r"i'm (.*) doing good",
        ["Nice to hear that","How can I help you? 🙂😁"]
    ],
    [
        r"(.*) age?",
        ["Get out.","We're done.","Are you really asking me this?"]
    ],
    [
        r'what (.*) want?',
        ["Make me an offer I can't refuse"]
    ]
    ,
    [
        r"(.*) created?",
        ["Diyan Amin created me using Python's NLTK library.","top secret bud ;)"]
    ],
    [
        r"(.*) (location|city) ?",
        [f"Hmm....\n{lat} and {long}"]
    ],
    [
        r'how is weather (.*)',
        ["It's really amazing'","I'm a Python Script. How am I gonna get the weather?","Funny you ask..."]
    ],
    [
        r"i work in (.*)?",
        ["Quit immediatly","Never heard about it","Im surpirsed your not jobless"]
    ],
    [
        r"(.*)raining in (.*)",
        ["Well, I'm just a Python Script so I don't know about rain in %2"]
    ],
    [
        r'how (.*) health(.*)',
        ["Funny you ask..."]
    ],
    [
        r"(.*) (sports|game)?",
        ["Big fan of Slimes vs. The Divine."]
    ],
    [
        r"who (.*) (moviestar|actor)?",
        ["Doesn't matter."]
    ],
    [
        r"i am looking for  online guides and courses to learn data science, can you suggest?",
        ["Botone_Tech has many great articles with each step explanation along with code, you can explore"]
    ],
    [
        r"quit",
        ['Bye, take care. See you soon ;)',"It was nice talking to you.","It wasnt nice talking to you >:|"]
    ],
]

def chat():
    print('Hi! I am a chatbot created by Diyan Amin for your service')
    chat = Chat(pairs,reflections)
    chat.converse()


if __name__ == '__main__':
    chat()