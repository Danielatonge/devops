""" python FastApi main runner
"""

from datetime import datetime
from os import path

import requests
from fastapi import FastAPI
from fastapi.responses import HTMLResponse, StreamingResponse

app = FastAPI()


@app.get("/", response_class=HTMLResponse)
async def read_root():
    """ The function response to the "/" endpoint by sending some HTML
        with current moscow time on success and no time on failure
    """
    html_content = """
    <!doctype html>
    <html>
        <head>
            <title>Current Moscow Time</title>
        </head>
        <body >
            <h1 style="text-align: center;">
                <span style="font-family:verdana,geneva,sans-serif;">Current Moscow Time</span>
            </h1>
            <p style="text-align: center;font-family:verdana,geneva,sans-serif;">%s</p>
        </body>
    </html>
        """

    res = requests.get("http://worldtimeapi.org/api/timezone/Europe/Moscow")

    if res.status_code == 200:
        full_date = datetime.strptime(res.json()["datetime"], "%Y-%m-%dT%H:%M:%S.%f%z")
        current_time = f"{full_date.hour}:{full_date.minute}:{full_date.second}"
        await record_time(current_time)
        return HTMLResponse(content=html_content % current_time, status_code=200)

    error = f"Error: {res.status_code}"
    return HTMLResponse(content=html_content % error, status_code=404)


async def record_time(time):
    with open("visit.txt", "a") as output:
        output.write(f"Recorded-time: {time}\n")


@app.get("/visits")
async def load_visiting():
    """ The function response to the "/visits" endpoint by sending some response
        with current moscow time which "/" was accessed
    """
    if path.exists('visit.txt'):
        with open('visit.txt', 'r') as output:
            return output.readlines()

    return "Visit '/' route"
