# filename: horoscope.py

import sys
import random
from datetime import datetime, timedelta

# Define the zodiac signs
zodiac_signs = ['Aries', 'Taurus', 'Gemini', 'Cancer', 'Leo', 'Virgo', 'Libra', 'Scorpio', 'Sagittarius', 'Capricorn', 'Aquarius', 'Pisces']

# Define some fictional horoscopes
horoscopes = [
    "Today is a great day for new beginnings.",
    "You will find joy in the most unexpected places.",
    "Your patience will be rewarded soon.",
    "A surprise encounter will bring you happiness.",
    "You will face a challenge that will make you stronger.",
    "Your creativity will lead you to success.",
    "A friend will need your advice.",
    "Your hard work will pay off.",
    "You will receive good news from a distant relative.",
    "A dream you have will come true.",
    "You will have a chance to travel to a place you've always wanted to visit.",
    "You will have a meaningful conversation with a stranger."
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