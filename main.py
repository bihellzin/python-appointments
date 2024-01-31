from typing import Union
from datetime import datetime
from fastapi import FastAPI
from pydantic import BaseModel
from fastapi.responses import JSONResponse

app = FastAPI()

class ScheduleBody(BaseModel):
    isoString: str

@app.get("/")
def read_root():
    return {"Hello": "World"}


# @app.get(/users/{user_id}/availability)

@app.post("/schedule/", status_code=200)
def test(body: ScheduleBody):
    try:
        return body
    except:
        return JSONResponse(
            status_code=400,
            content={"message": "Invalid"}
        )