# personal-telegram-notifications

## Telegram Notification Bot for Radarr

### Requirements:
- Python 3.x
- pip install python-telegram-bot
- A Radarr instance with API key and Telegram notification method set up
- Your own Telegram bot token and chat ID (obtained from BotFather)

### Setup:
1. Install Radarr from https://radarr.video/.
2. Once you've installed Radarr, log in to the web interface and navigate to Settings > General > API Keys. Generate a new API key by clicking on "Add New" and providing a name for it.
3. Copy the generated API key and save it in your script's environment variables or settings file as `RADARR_API_KEY`.
4. Navigate to Settings > Notifications and set up a new notification method by clicking on "Add New" and selecting the desired notification type (Telegram Bot is one of them). Provide your bot token, chat ID, and other necessary details.
5. Install `python-telegram-bot` by running `pip install python-telegram-bot`.
6. Save the script as `radarr_notification.py` and set up environment variables for `RADARR_API_KEY`, `TELEGRAM_BOT_TOKEN`, and `TELEGRAM_CHAT_ID` using a `.env` file.
7. Set up a cron job to run the script every minute: `* * * * * * python3 /path/to/radarr_notification.py > /dev/null 2>&1`

### Usage:
The script will continuously monitor for new movies downloaded by Radarr and send a Telegram notification if any are found.

### Error Handling:
If the script encounters an error, it will simply log it to the console. You can set up a service like supervisord or pm2 to monitor and restart the script automatically if needed.

### Contributing:
Feel free to contribute by forking this repository, making changes, and submitting a pull request!

'''
* * * * * * python3 /path/to/radarr_notification.py > /dev/null 2>&1
'''


## IMDb Movie Folder Creator

This Python script automates the process of organizing your movie files based on their IMDb ID. It creates a folder with the movie's title in Spanish and the production year in parentheses, then moves the provided video file into this folder, renaming it to match the folder's title.

### Features

Fetches movie title and production year in Spanish from IMDb using IMDb ID.

Creates a folder named after the movie title and production year.

Moves the video file into the created folder, renaming it accordingly.

### Requirements

- Python 3.x
- IMDbPY library (imdbpy), version 2022.0.1

## Usage

- Install the required dependencies listed in requirements.txt:

pip install -r requirements.txt

- Run the script:

'''
python imdb_movie_folder_creator.py
'''

Follow the prompts to enter the IMDb ID of the movie and the path to the video file.

### Example

Suppose you have a video file named my_movie.mp4 and its IMDb ID is tt1234567. Running the script will create a folder named Movie Title (Year) and move my_movie.mp4 into it, renaming it to Movie Title (Year).mp4.