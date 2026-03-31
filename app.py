from fastapi import FastAPI, Request
import datetime

app = FastAPI()

@app.post("/webhook") 
async def webhook(request: Request):
    data = await request.json()
    
    print(f"[{datetime.datetime.now()}] Incoming webhook:", data)

    return {
        "status": "received",
        "length": len(data)
    }
