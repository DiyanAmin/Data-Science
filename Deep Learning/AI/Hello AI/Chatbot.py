import datetime as dt
from diyanLib.data import store,retrieve

name = input(
    "Hello I am a AI chatbot created by Diyan. What's your name?\n>"
)

print(f"Nice to meet you, {name}!\n")

mood = input(f"So, how are you feeling today, {name}?\n>").lower()

if mood=='good' or mood=='excellent' or mood=='amazing':print("I'm glad to hear that.")
elif mood=='fine':print("Ok, hope you feel better.")
elif mood=='bad':print(f"Oh, I'm sorry to hear that {name}.")
else:print("I see.")

prev_data = retrieve("Conversations.log")

print(f"Well, It was nice knowing you {name}. Diyan is shutting me down now. Bye!")

is_valid=False

while not is_valid:
    try:
        rating = float(input(f"\n\nDiyan: Please rate your conversation with my AI chatbot from 1-10.\n{name}: "))
        if rating>=0 and rating<=10:
            if rating>8:
                print('Diyan: Thank you!')
            elif rating>5:
                print("Diyan: Oh! Ok I will try to improve.")
            elif rating>=1:
                print("Diyan: I see...")
            else:
                print("Diyan: You will never use my AI chatbot again.\n\nYou have been banned from Diyan's Chatbot.\n")


        prev_data+=f"{dt.datetime.now()}:\n\tName: {name}\n\tMood: {mood}\ntRating: {rating}\n\n"
        store("Conversations.log",prev_data)

        is_valid=True
        break
        
    except ValueError:
        print("Unknown rating.")