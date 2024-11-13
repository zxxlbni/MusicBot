from os import getenv

API_ID = getenv("API_ID", 22419004)
API_HASH = getenv("API_HASH", "34982b52c4a83c2af3ce8f4fe12fe4e1")
BOT_TOKEN = getenv("BOT_TOKEN", "7564755990:AAH30wsTjb6ZjhLA4v_ddfoNiRaWv8U2KMk")
BOT_COMMANDS = (
    ("start", "Initialize the bot and check its status"),
    ("settings", "Configure and manage bot settings"),
    ("help", "Get information on how to use the bot"),
    ("about", "Learn more about the bot and its features"),
)

DATABASE_URL = getenv("DATABASE_URL", None)
HOST = getenv("HOST", "0.0.0.0")
PORT = int(getenv("PORT", "8080"))
