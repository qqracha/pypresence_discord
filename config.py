import os
from dotenv import load_dotenv

load_dotenv()

CLIENT_ID = os.getenv("CLIENT_ID")
# Данные трека
TRACK_NAME = "That Sinking Feeling (Main Theme)"
ALBUM_NAME = "Schedule I OST"
TRACK_DURATION = 128  # в секундах
SPOTIFY_URL = "https://open.spotify.com/track/6N4bA5VmWdgNDuHyqGgWnU"
# Ссылка на обложку (можно загрузить в Rich Presence Assets или использовать прямую ссылку)
IMAGE_URL = "https://i.scdn.co/image/ab67616d0000b2736d1a0da6e0e5dfdff798da9a" 
