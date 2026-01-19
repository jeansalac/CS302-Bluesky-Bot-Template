from atproto import Client, models
import bluesky_config as config

client = Client(base_url="https://bsky.social")
client.login("REPLACE WITH YOUR BLUESKY BOT USERNAME", config.PASSWORD)