# filename: horoscope.py

import sys
import random
from datetime import datetime, timedelta

# Define the zodiac signs
zodiac_signs = ['Aries', 'Taurus', 'Gemini', 'Cancer', 'Leo', 'Virgo', 'Libra', 'Scorpio', 'Sagittarius', 'Capricorn', 'Aquarius', 'Pisces']

# Define some fictional horoscopes
horoscopes = [
    "Today is a great day for new beginnings, especially if you’ve been procrastinating on ending old things.",
    "You will find joy in the most unexpected places, like your sock drawer.",
    "Your patience will be rewarded soon, probably with more opportunities to practice patience.",
    "A surprise encounter will bring you happiness, or a new pet. Who knows, it’s a surprise!",
    "You will face a challenge that will make you stronger, or at least make for a good story.",
    "Your creativity will lead you to success, or at least a very colorful mess.",
    "A friend will need your advice, but remember, telling them to grow up is not always the best advice.",
    "Your hard work will pay off, in monopoly money, unfortunately.",
    "You will receive good news from a distant relative, probably on social media because who calls anymore?",
    "A dream you have will come true, especially if it’s about sleeping in tomorrow.",
    "You will have a chance to travel to a place you've always wanted to visit, even if it’s just the new coffee shop down the street.",
    "You will have a meaningful conversation with a stranger, about whether pineapple belongs on pizza."
    "You'll discover a new talent today: the ability to trip over flat surfaces.",
    "An unexpected windfall is coming your way, might just be leaves falling from trees.",
    "You will encounter a rare opportunity to show off your interpretive dance skills.",
    "You’ll finally find that thing you’ve been looking for, in the last place you look, of course.",
    "Today, your charm will be irresistible; even the coffee machine will finally work for you.",
    "You’ll have a profound realization today, probably about something trivial like why they call it a hamburger.",
    "A moment of clarity will strike you in the shower, but it’ll be gone by the time you’re dried off.",
    "You’ll have a chance to face your fears today, especially if your fear is of overcooked pasta.",
    "You will meet someone who will change your life, they might just be delivering your pizza.",
    "Today is a good day to embrace change, just not all the coins in your couch cushions.",
    "Your outlook will be bright today, wear sunglasses to shield your eyes from the dazzling possibilities.",
    "Expect the unexpected today, like finding out your cat has a secret blog.",
    "You’ll be on a roll today, hopefully not down a hill.",
    "The stars predict you will wake up, do things, and then go back to sleep.",
    "Today, you will see the silver lining in every cloud, even if it’s just airplane contrails.",
    "You’ll stumble upon a new favorite song today, most likely while wrestling with the radio dial.",
    "You will have a moment of deja vu, or did this already happen?",
    "Your intuition will be your guide, even if it's suggesting you to take a nap.",
    "A burst of energy will help you accomplish a personal goal, like the world record for most naps in a day.",
    "You will be inspired to start a new hobby, probably something that involves less responsibility than a goldfish."
]




# Check if the required arguments are provided
if len(sys.argv) < 3:
    print("Error: Please provide a start date and an end date in the format 'YYYY-MM-DD'.")
    sys.exit(1)

# Get the start and end dates from the command line arguments
start_date = datetime.strptime(sys.argv[1], '%Y-%m-%d')
end_date = datetime.strptime(sys.argv[2], '%Y-%m-%d')

# Generate a horoscope for each day and each zodiac sign
current_date = start_date
while current_date <= end_date:
    print(f"Horoscopes for {current_date.strftime('%Y-%m-%d')}:")
    for sign in zodiac_signs:
        print(f"{sign}: {random.choice(horoscopes)}")
    print("\n")
    current_date += timedelta(days=1)