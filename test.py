# application configuration
APP_NAME = "SecretDetector"
VERSION = "1.0.0"

# database setup
db_host = "localhost"
db_user = "admin"
db_port = 5432

# logging
def setup_logger():
    print("Logger initialized")

# fake business logic
def calculate(a, b):
    return a + b

# user service
class UserService:
    def __init__(self):
        self.users = []

    def add_user(self, name):
        self.users.append(name)

# --- פה "טעות אמיתית" ---

password = "12345678"

# עוד קוד רגיל
def connect():
    print("Connecting to DB...")

# API config
api_url = "https://api.example.com"

# --- עוד טעות ---
api_key = "ABCDEFG1234567890ABCDEFG"

# עוד קוד
def run():
    print("App running")

# --- טעות מוסתרת ---
aws_key = "AKIA1234567890ABCDEF"
