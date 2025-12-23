from pypresence import Presence
from pypresence.types import ActivityType, StatusDisplayType
import time
from config import CLIENT_ID, STATUS_DETAILS, STATUS_STATE

if not CLIENT_ID:
    raise ValueError("CLIENT_ID not found in .env!")
try:
    RPC = Presence(CLIENT_ID)
    print("[INFO] Connect to Discord...")
    RPC.connect()

    # Or use StatusDisplayType to control what appears in the user's status
    RPC.update(
        status_display_type=StatusDisplayType.STATE,
        state=STATUS_STATE,
        details=STATUS_DETAILS
    )
    print(f"[SUCCESS] Status was updated: {STATUS_DETAILS} - {STATUS_STATE}")

    print("[INFO] Script is online! Check your activity.")
    while True:
        time.sleep(15)
except Exception as e:
    print(f"[ERROR] Somethings wrong: {e}")
    