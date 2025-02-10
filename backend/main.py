import firebase_admin
from firebase_admin import credentials, firestore
import os  # For environment variables
from fastapi import FastAPI # If you're using FastAPI

app = FastAPI() # Create your FastAPI app instance

# Initialize Firebase (using environment variables - BEST PRACTICE)
firebase_credentials_json = os.environ.get("FIREBASE_CREDENTIALS")
if firebase_credentials_json:
    try:
        firebase_credentials = credentials.Certificate(json.loads(firebase_credentials_json)) # Load from JSON string
        firebase_admin.initialize_app(firebase_credentials)
        db = firestore.client() # Access Firestore after successful initialization
    except ValueError as e: # Catch JSON decode errors
        print(f"Error decoding Firebase credentials: {e}")
        exit(1) # Exit if initialization fails

else:
    print("Error: FIREBASE_CREDENTIALS environment variable not set.")
    exit(1) # Exit if no credentials are found

# Example API endpoint (if you are using FastAPI)
@app.get("/")
async def root():
    return {"message": "Hello from your Firebase-connected app!"}



# If you are NOT using FastAPI (e.g., just a simple script):
# You can remove the app = FastAPI() and the @app.get("/") decorator
# and leave only the Firebase initialization code

# ... rest of your code ...