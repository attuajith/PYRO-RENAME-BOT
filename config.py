import re, os

id_pattern = re.compile(r'^.\d+$') 

API_ID = os.environ.get("API_ID", "27884084")

API_HASH = os.environ.get("API_HASH", "f41ef10f7e283ba0b6b18fac6fbe8226")

BOT_TOKEN = os.environ.get("BOT_TOKEN", "5631979252:AAGn16G2Cr7AXL708FNrt3fLaFuQ7FCenBw") 

FORCE_SUB = os.environ.get("FORCE_SUB", "https://t.me/vedigundi_LinkZz") 

DB_NAME = os.environ.get("DB_NAME","cluster0")     

DB_URL = os.environ.get("DB_URL","mongodb+srv://MrStark:20urcm06@cluster0.qhcpkym.mongodb.net/?retryWrites=true&w=majority")
 
FLOOD = int(os.environ.get("FLOOD", "10"))

START_PIC = os.environ.get("START_PIC", "https://telegra.ph/file/3583efe74f1b3179b7640.jpg")

ADMIN = [int(admin) if id_pattern.search(admin) else admin for admin in os.environ.get('ADMIN', '1899869233').split()]

PORT = os.environ.get('PORT', '8080')
