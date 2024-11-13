from os import getenv

# Environment configurations with default values
API_ID = int(getenv("API_ID", "22419004"))  # Ensure API_ID is an integer
API_HASH = getenv("API_HASH", "34982b52c4a83c2af3ce8f4fe12fe4e1")
BOT_TOKEN = getenv("BOT_TOKEN", "7564755990:AAH30wsTjb6ZjhLA4v_ddfoNiRaWv8U2KMk")

# Bot commands configuration
BOT_COMMANDS = (
    ("start", "Initialize the bot and check its status"),
    ("settings", "Configure and manage bot settings"),
    ("help", "Get information on how to use the bot"),
    ("about", "Learn more about the bot and its features"),
)

# Database configuration, host, and port settings
DATABASE_URL = getenv("DATABASE_URL", "mongodb+srv://mrnoobx:DAZCdTczVWyECi04@cluster0.sedgwxy.mongodb.net/?retryWrites=true&w=majority")
HOST = getenv("HOST", "")
PORT = int(getenv("PORT", "8484"))  # Convert PORT to an integer
