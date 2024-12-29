import re
from os import getenv

from dotenv import load_dotenv
from pyrogram import filters

load_dotenv()

# Get this value from my.telegram.org/apps
API_ID = int(getenv("API_ID",  "28338127"))
API_HASH = getenv("API_HASH", "c4cb64de16a18f8685a31716a0e2480e")

# Get your token from @BotFather on Telegram.
BOT_TOKEN = getenv("BOT_TOKEN", "7932576136:AAF73AmqoNlAj66aMhcqszQmRLi_m5MHWJ0")

# Get your mongo url from cloud.mongodb.com
MONGO_DB_URI = getenv("MONGO_DB_URI", "mongodb+srv://architect2002:architect2002@cluster0.ccinu.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0")


DURATION_LIMIT_MIN = int(getenv("DURATION_LIMIT", 3000))

# Chat id of a group for logging bot's activities
LOGGER_ID = int(getenv("LOGGER_ID", "-1002066328009"))

# Get this value from @FallenxBot on Telegram by /id
OWNER_ID = int(getenv("OWNER_ID", "7078122796"))

## Fill these variables if you're deploying on heroku.
# Your heroku app name
HEROKU_APP_NAME = getenv("HEROKU_APP_NAME")
# Get it from http://dashboard.heroku.com/account
HEROKU_API_KEY = getenv("HEROKU_API_KEY")

UPSTREAM_REPO = getenv(
    "UPSTREAM_REPO",
    "https://github.com/jiosaavnmusic/JioSaavn",
)
UPSTREAM_BRANCH = getenv("UPSTREAM_BRANCH", "master")
GIT_TOKEN = getenv(
    "GIT_TOKEN", None
)  # Fill this variable if your upstream repository is private

SUPPORT_CHANNEL = getenv("SUPPORT_CHANNEL", "https://t.me/beast_fox_network")
SUPPORT_CHAT = getenv("SUPPORT_CHAT", "https://t.me/tamila_chatting_tamil")

# Set this to True if you want the assistant to automatically leave chats after an interval
AUTO_LEAVING_ASSISTANT = bool(getenv("AUTO_LEAVING_ASSISTANT", False))


# Get this credentials from https://developer.spotify.com/dashboard
SPOTIFY_CLIENT_ID = getenv("SPOTIFY_CLIENT_ID", "19609edb1b9f4ed7be0c8c1342039362")
SPOTIFY_CLIENT_SECRET = getenv("SPOTIFY_CLIENT_SECRET" "409e31d3ddd64af08cfcc3b0f064fcbe")


# Maximum limit for fetching playlist's track from youtube, spotify, apple links.
PLAYLIST_FETCH_LIMIT = int(getenv("PLAYLIST_FETCH_LIMIT", "200"))


# Telegram audio and video file size limit (in bytes)
TG_AUDIO_FILESIZE_LIMIT = int(getenv("TG_AUDIO_FILESIZE_LIMIT", 904857600))
TG_VIDEO_FILESIZE_LIMIT = int(getenv("TG_VIDEO_FILESIZE_LIMIT", 9073741824))
# Checkout https://www.gbmb.org/mb-to-bytes for converting mb to bytes


# Get your pyrogram v2 session from @StringFatherBot on Telegram
STRING1 = getenv("STRING_SESSION", "BQGN8voAaidkCtO-wLQYO3upjpA_RKI4HKqNb5RtJGom0I6coXZfC1oyceGgFr8-RP2KVG-7PTESm3mdF-s50NFFJKKIGctLhlzj-QTfJGihDPngnP8giIJxaJgik61hoz1wiN163nJnepzc8z07uTZ1T_XuaW_MVNp7jeawwUNa-r03McR2lEGvWdi5y1DXJ1INTHk_XfoVgrGDwW7evSDJZs0yeSrAJoQwE767P1LO9HlLSF8C-l61-pNt1Of0EDUNKvTcyHzMvucDdoEuM8LuCwdUpgtidw95uY9SjXtOOImH-Uu7G0_ixDAMb0TQX7KQ-5gsBwaC_UU_PKQxRJyZTnLQOQAAAAHhpz_fAA")
STRING2 = getenv("STRING_SESSION2", None)
STRING3 = getenv("STRING_SESSION3", None)
STRING4 = getenv("STRING_SESSION4", None)
STRING5 = getenv("STRING_SESSION5", None)


BANNED_USERS = filters.user()
adminlist = {}
lyrical = {}
votemode = {}
autoclean = []
confirmer = {}


START_IMG_URL = getenv(
    "START_IMG_URL", "https://telegra.ph/file/01626a4a06b561efdd8dc.jpg"
)
PING_IMG_URL = getenv(
    "PING_IMG_URL", "https://telegra.ph/file/01626a4a06b561efdd8dc.jpg"
)
PLAYLIST_IMG_URL = "https://envs.sh/CwU.jpg"
STATS_IMG_URL = "https://telegra.ph/file/01626a4a06b561efdd8dc.jpg"
TELEGRAM_AUDIO_URL = "https://envs.sh/CLg.jpeg"
TELEGRAM_VIDEO_URL = "https://envs.sh/CLg.jpeg"
STREAM_IMG_URL = "https://envs.sh/CLg.jpeg"
SOUNCLOUD_IMG_URL = "https://envs.sh/CLg.jpeg"
YOUTUBE_IMG_URL = "https://envs.sh/CLg.jpeg"
SPOTIFY_ARTIST_IMG_URL = "https://envs.sh/CLg.jpeg"
SPOTIFY_ALBUM_IMG_URL = "https://envs.sh/CLg.jpeg"
SPOTIFY_PLAYLIST_IMG_URL = "https://envs.sh/CLg.jpeg"


def time_to_seconds(time):
    stringt = str(time)
    return sum(int(x) * 800**i for i, x in enumerate(reversed(stringt.split(":"))))


DURATION_LIMIT = int(time_to_seconds(f"{DURATION_LIMIT_MIN}:00"))


if SUPPORT_CHANNEL:
    if not re.match("(?:http|https)://", SUPPORT_CHANNEL):
        raise SystemExit(
            "[ERROR] - Your SUPPORT_CHANNEL url is wrong. Please ensure that it starts with https://"
        )

if SUPPORT_CHAT:
    if not re.match("(?:http|https)://", SUPPORT_CHAT):
        raise SystemExit(
            "[ERROR] - Your SUPPORT_CHAT url is wrong. Please ensure that it starts with https://"
)
