from fastapi import FastAPI, HTTPException
from pydantic import BaseModel

app = FastAPI()

# In-memory subscription store (just a Python set for now)
subscriptions = set()

# Request model
class NotificationRequest(BaseModel):
    accountId: int
    notifyType: str  # like "email", "sms", etc.

# Helper function to generate a unique key
def make_key(account_id: int, notify_type: str) -> str:
    return f"{account_id}:{notify_type}"

# Subscribe endpoint
@app.post("/notifications/subscribe")
def subscribe(req: NotificationRequest):
    key = make_key(req.accountId, req.notifyType)
    subscriptions.add(key)
    return {"message": f"Subscribed to {req.notifyType} notifications."}

# Unsubscribe endpoint
@app.post("/notifications/unsubscribe")
def unsubscribe(req: NotificationRequest):
    key = make_key(req.accountId, req.notifyType)
    if key in subscriptions:
        subscriptions.remove(key)
        return {"message": f"Unsubscribed from {req.notifyType} notifications."}
    else:
        raise HTTPException(status_code=404, detail="Subscription not found.")
