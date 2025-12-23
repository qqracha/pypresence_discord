import os
from dotenv import load_dotenv

load_dotenv()

CLIENT_ID = os.getenv("CLIENT_ID")
STATUS_STATE = os.getenv("STATUS_STATE", "Building something awesome")
STATUS_DETAILS = os.getenv("STATUS_DETAILS", "Using pypresence")