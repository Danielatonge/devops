from fastapi import FastAPI
from fastapi.responses import HTMLResponse
import requests
from datetime import datetime
import pytz

app = FastAPI()


@app.get("/", response_class=HTMLResponse)
async def read_root():

    html_content = """
    <!doctype html>
    <html>
        <head>
            <title>Current Moscow Time</title>
        </head>
        <body >
            <h1 style="text-align: center;"><span style="font-family:verdana,geneva,sans-serif;">Current Moscow Time</span></h1>
            <p style="text-align: center;font-family:verdana,geneva,sans-serif;">%s</p>
        </body>
    </html>
        """

    res = requests.get("http://worldtimeapi.org/api/timezone/Europe/Moscow")
    if res.status_code == 200:
        full_date = datetime.strptime(res.json()["datetime"], "%Y-%m-%dT%H:%M:%S.%f%z")
        current_time = f"{full_date.hour}:{full_date.minute}:{full_date.second}"
        return HTMLResponse(content=html_content % (current_time), status_code=200)
    else:
        error = f"Error: {res.status_code}"
        return HTMLResponse(content=html_content % (error), status_code=404)