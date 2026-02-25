import os
from dotenv import load_dotenv

load_dotenv()

# Connectivity: Points to your AWS MongoDB Atlas or local instance
MONGO_URI = os.getenv("MONGODB_URI", "mongodb://localhost:27017")
DB_NAME = os.getenv("DB_NAME", "entry_shield")