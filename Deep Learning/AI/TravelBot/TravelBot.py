import re,random
from colorama import Fore as c
from colorama import init

init(True)

name = ''

destinations={
    "beaches":["Bali","Maldives",'Phuket','Goa'],
    'mountains':['Swiss Alps','Rocky Mountains','Himalayas'],
    "cities":['Tokyo','Paris','New York']
}

jokes = [
    "Why don't programmers like nature? Too many bugs!",
    "Why did the computer go to the doctor? Because it had a virus!",
    "Why do travellers always feel warm? Because of all their hot spots!"
]

def normalize_text(text:str):
    return re.sub(r"\s+"," ", text.strip().lower())

def say(color:str,msg):
    color  = color.upper()
    exec(f"print(c.{color}+'TravelBot: {msg}')")

prev_suggestion = ''

def recommend():
    say('cyan','Beaches, mountains or cities?')
    preference = input(c.YELLOW+'You: ')
    preference=normalize_text(preference)

    if preference in destinations:
        while suggestion==prev_suggestion:
            suggestion = random.choice(destinations[preference])
        prev_suggestion = suggestion
        say('green',f'How about {suggestion}?')
        say('cyan','Do you like it? (yes/no)')
        answer = input(c.YELLOW+"You: ").lower().strip()

        if answer=='yes':
            say('green',f'Awesome! Enjoy {suggestion}')

        elif answer=='no':
            say('red',"Let's try again.")
            recommend()

        else:
            say('red',"I'll suggest again.")
            recommend()

    else:
        say('red',f"Sorry, I don't have that type of destination. Let's try again, {name}.")
        recommend()

def packaging_tips():
    say('cyan',"Where to?")
    location = normalize_text(input(c.YELLOW+"You: "))
    say('cyan',"How many days?")
    days = input(c.YELLOW+"You: ")

    if days<40:
        say('green',f"""
    Packing tips for {days} days in {location}:

    -Pack versatile clothes
    - Bring chargers/adapters
    - Check the weather forecast.
    """)
    else:
        say('red',f"Woah! That's alot of days! I don't believe you, {name}.")
        packaging_tips()

def tell_joke():
    say('yellow',random.choice(jokes))

def show_help():
    say('magenta','\nI can:')
    say('green',"""
- Suggest travel spots (say 'recommendations')
- Offer packing tips (say 'packing tips')
- Tell a joke (say 'joke')
- Understand misspelled messages too! (Feature added by Diyan Amin)
""")

    say('cyan',"Type 'exit' or 'bye' to end.\n")


def chat():
    say('cyan',"Hello! I'm TravelBot")
    name = input(c.YELLOW+"Your name?\n>>")