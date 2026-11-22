from diyanLib.imports.ai import *
from diyanLib.data import json_handler
import pandas as pd
from textblob import TextBlob
from time import sleep

# Load movie dataset
try:
    df = pd.read_csv("movies.csv")
except FileNotFoundError:
    print(f"{red}Error: movies.csv file not found!")
    raise SystemExit

# Load saved user data
try:
    saved_data = json_handler("saved_data").get()
    if not saved_data:
        saved_data = False
except FileNotFoundError:
    saved_data = False
    print(f"{red}No saved data found.")

# Extract available genres
genres = sorted({
    g.strip()
    for xs in df["Genre"].dropna().str.split(",")
    for g in xs
})

# Loading animation
def dots():
    for _ in range(3):
        print(yellow + ".", end="", flush=True)
        sleep(0.5)

# Sentiment classification
def senti(p):
    if p > 0:
        return "Positive 😊"
    elif p < 0:
        return "Negative 😔"
    return "Neutral 😐"

# Get user genre
def get_genre():

    print(f"{green}Available Genres:")

    for i, g in enumerate(genres, 1):
        print(f"{cyan}{i}. {g}")

    while True:
        x = input(f"{yellow}Enter genre number or name: ").strip()

        if x.isdigit() and 1 <= int(x) <= len(genres):
            return genres[int(x) - 1]

        for g in genres:
            if x.lower() == g.lower():
                return g

        print(f"{red}Invalid input. Try again.")

# Get IMDb rating
def get_rating():

    while True:
        x = input(
            f"{yellow}Enter minimum IMDb rating (7.6-9.3) or skip: "
        ).strip()

        if x.lower() == "skip":
            return None

        try:
            r = float(x)

            if 7.6 <= r <= 9.3:
                return r

            print(f"{red}Rating out of range.")

        except ValueError:
            print(f"{red}Invalid input.")

# AI movie recommendation
def recommend(genre=None, mood=None, rating=None, n=5):

    d = df.copy()

    # Filter by genre
    if genre:
        d = d[
            d["Genre"].str.contains(
                genre, case=False, na=False, regex=False
            )
        ]

    # Filter by IMDb rating
    if rating is not None:
        d = d[d["IMDB_Rating"] >= rating]

    if d.empty:
        return []

    # Analyze user's mood
    mood_polarity = TextBlob(mood).sentiment.polarity

    d = d.sample(frac=1).reset_index(drop=True)

    recommendations = []

    for _, r in d.iterrows():

        overview = r.get("Overview")

        if pd.isna(overview):
            continue

        # Analyze movie description
        polarity = TextBlob(str(overview)).sentiment.polarity

        # Match movie sentiment with user's mood
        if mood_polarity < -0.1:
            suitable = polarity > 0

        elif mood_polarity > 0.1:
            suitable = polarity >= 0

        else:
            suitable = abs(polarity) < 0.2

        if suitable:
            recommendations.append(
                (r["Series_Title"], polarity, r["IMDB_Rating"])
            )

        if len(recommendations) == n:
            break

    return recommendations

# Display recommendations
def show(recs, name):

    print(f"\n{yellow}🍿 AI Movie Recommendations for {name}")

    if not recs:
        print(f"{red}No suitable movie recommendations found.")
        return

    for i, (title, polarity, rating) in enumerate(recs, 1):

        print(
            f"{cyan}{i}. 🎥 {title}"
            f" | IMDb: {rating}"
            f" | Polarity: {polarity:.2f}"
            f" | {senti(polarity)}"
        )

# Welcome message
print(f"{blue}\n🎥 Welcome to Your Personal Movie Recommendation Assistant! 🎥")

# Get user name
if saved_data:
    name = saved_data["name"]
    print(f"{green}Welcome back, {name}!")

else:
    name = input(f"{yellow}What's your name? ").strip()

# Get mood
if saved_data:
    ans = input(
        f"{cyan}Would you like to change your mood? (y/n): "
    ).strip().lower()

    if ans.startswith("y"):
        mood = input(f"{yellow}Describe your mood: ").strip()
    else:
        mood = saved_data["mood"]

else:
    mood = input(
        f"{yellow}How do you feel today? Describe your mood: "
    ).strip()

# Mood analysis
print(f"{blue}\nAnalyzing your mood", end="", flush=True)
dots()

mp = TextBlob(mood).sentiment.polarity

print(f"\n{green}Your mood is: {senti(mp)}")
print(f"{green}Mood polarity: {mp:.2f}")

# Get IMDb rating
if saved_data:
    ans = input(
        f"{cyan}Would you like to change your rating? (y/n): "
    ).strip().lower()

    if ans.startswith("y"):
        rating = get_rating()
    else:
        rating = saved_data["rating"]

else:
    rating = get_rating()

# Get genre
if saved_data:
    ans = input(
        f"{cyan}Would you like to change your genre? (y/n): "
    ).strip().lower()

    if ans.startswith("y"):
        genre = get_genre()
    else:
        genre = saved_data["genre"]

else:
    genre = get_genre()

# Save user preferences
user_data = {
    "name": name,
    "mood": mood,
    "rating": rating,
    "genre": genre
}

try:
    json_handler("saved_data").save(user_data)
    print(f"{green}\nYour preferences have been saved!")
except Exception as e:
    print(f"{red}Could not save preferences: {e}")

# Generate recommendations
print(f"\n{blue}Finding the best movies for {name}", end="", flush=True)
dots()

recs = recommend(genre, mood, rating)

# Display results
show(recs, name)

print(f"\n{green}Thank you for using the AI Movie Recommendation Assistant! 🎬")