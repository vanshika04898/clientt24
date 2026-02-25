import os
from pymongo import MongoClient
from dotenv import load_dotenv

# Load environment variables (MONGODB_URI should be in your .env file)
load_dotenv()

# Connectivity: This uses the URI for your AWS MongoDB Atlas cluster
# It defaults to a local connection if the environment variable is missing
MONGO_URI = os.getenv("MONGODB_URI", "mongodb://localhost:27017")

# Initialize the MongoDB Client
client = MongoClient(MONGO_URI)

# Connectivity: Using the explicit DB name "entry_shield" as defined in your seed files
# References: 00-roles-admin.js and 04-gate-passes-student.js
db = client.entry_shield

# Connectivity: This collection stores both Student and Visitor/Parent passes
# as per the logic in your 04-gate-passes-student.js file
visits_collection = db.gate_passes

# Optional: Initialize indexes defined in your seed files if they don't exist
def init_db_indexes():
    try:
        # Create unique index on studentId to prevent duplicate entries
        # as specified in 04-gate-passes-student.js
        visits_collection.create_index("formData.studentId", unique=True, sparse=True)
        
        # Create unique index on roles as specified in 00-roles-admin.js
        db.roles.create_index("role", unique=True)
        
        print("✅ Database indexes verified and connected.")
    except Exception as e:
        print(f"⚠️ Index initialization notice: {e}")

# Run index initialization
init_db_indexes()