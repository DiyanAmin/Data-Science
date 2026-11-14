import colorama
from colorama import Fore,Style
from textblob import TextBlob
from diyanLib.data import store,retrieve
from datetime import datetime as dt

colorama.init()

print(
    f"{Fore.CYAN} 🐍 Welcome to Sentiment Spy! 🐍{Style.RESET_ALL}"
)

username = input(f"{Fore.MAGENTA}Please enter your name: {Style.RESET_ALL}").strip()
if not username:
    username = 'Unknown'

if username=='ovrlrd':
    username==-1

elif username.lower()=='creator' or username.lower()=='diyan':
    username='Random Person'

conv_his = []

if username!=-1:
    print(f"{Fore.CYAN}Hello, Agent {username}!")
elif username==-1:
    print(f"{Fore.CYAN}Hello, Creator")
print(f"Type a sentence and I will analyse your sentences with TextBlob and show you the sentiment.")
print(f"Type {Fore.YELLOW}reset{Fore.CYAN} to quit.{Style.RESET_ALL}\n")

while True:
    userInput=input(f"{Fore.GREEN}>> {Style.RESET_ALL}").strip().lower()

    if not userInput:
        print(f"{Fore.RED}Please enter some text or a valid command.{Style.RESET_ALL}")
        continue

    if userInput=='exit':
        print(f"\n{Fore.BLUE} Exiting Sentiment Spy. Farewell, Agent {username}! 😊{Style.RESET_ALL}")
        time = dt.now()
        store(retrieve("Conversations.log")+f"{time}:\n\t{conv_his}\n\n")

        break

    elif userInput=='reset':
        conv_his.clear()

    elif userInput=='history':
        if not conv_his:
            print(f"{Fore.YELLOW}No conversation history yet. {Style.RESET_ALL}")
        else:
            print(f"{Fore.CYAN} Conversation History:{Style.RESET_ALL}")
            for idx,(text,polarity,sentimentType) in enumerate(conv_his,start=1):

                if sentimentType=='Positive':
                    color=Fore.GREEN
                    emoji='😊'

                elif sentimentType=='Negative':
                    color=Fore.RED
                    emoji="😔"

                else:
                    color=Fore.YELLOW
                    emoji="😐"

                print(f"{idx}. {color}{emoji} {text} ")
                print(f"Polarity: {polarity:.2f}, {sentimentType}{Style.RESET_ALL}\n")
            continue

    polarity=TextBlob(userInput).sentiment[0]

    if polarity>.25:
        sentimentType="Positive"
        color=Fore.GREEN
        emoji="😊"

    elif polarity<-.25:
        sentimentType="Negative"
        color=Fore.RED
        emoji = "😔"

    else:
        sentimentType="Neutral"
        color=Fore.YELLOW
        emoji = "😐"

    conv_his.append((userInput,polarity,sentimentType))

    print(f"{color}{emoji} {sentimentType} sentiment detected!")
    print(f"Polarity: {polarity:.2f}")