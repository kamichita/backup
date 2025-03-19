import os

BOTTOKEN = os.getenv("DISCORD_TOKEN")
CLIENT_ID = "1347091568552841226"
CLIENT_SECRET = "D4MCHJWG8fCQTcXMn0S-fbOrUkdSF5XB"
REDIRECT_URI = "https://kamichita-verification.up.railway.app/"

usadata_path = "userdata.json"
serverdata_folder_path = "./server/"
authurl = "https://discord.com/oauth2/authorize?client_id=1347091568552841226&response_type=code&redirect_uri=https%3A%2F%2Fkamichita-verification.up.railway.app%2F&scope=identify+guilds.join"
