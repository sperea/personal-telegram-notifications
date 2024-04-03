import requests
from dotenv import load_dotenv
import os
import time

load_dotenv()

# Set up environment variables for Radarr API key and Telegram bot information
radarr_api_key = os.getenv('RADARR_API_KEY')
telegram_bot_token = os.getenv('TELEGRAM_BOT_TOKEN')
telegram_chat_id = os.getenv('TELEGRAM_CHAT_ID')

# Set up Telegram bot client
from telegram import Bot, Update, ReplyKeyboardMarkup, KeyboardButton
bot = Bot(token=telegram_bot_token)

# Set up the URL for the Radarr API endpoint to retrieve movie information
url = f'http://localhost:7878/api/movie?apikey={radarr_api_key}' # Replace with your Radarr URL

def get_new_movies():
    """
    Queries the Radarr API for new movies and sends a notification to Telegram if any are found.
    """
    # Get all movies from Radarr's API
    response = requests.get(url)
    if response.status_code == 200:
        movies = response.json()
        # Check for new movies
        new_movies = []
        for movie in movies:
            if movie['status'] == 'Downloaded':
                new_movies.append(movie)
        # Send notification to Telegram if any movies were found
        if len(new_movies) > 0:
            for movie in new_movies:
                message = f"New movie downloaded: {movie['title']} ({movie['year']})"
                bot.send_message(chat_id=telegram_chat_id, text=message)
    else:
        print('Error connecting to Radarr API')

if __name__ == '__main__':
    while True:
        get_new_movies()
        time.sleep(60) # Run the function every 60 seconds to check for new movies