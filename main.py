from dotenv import load_dotenv
load_dotenv()

from fastapi import FastAPI, Request
from fastapi.responses import JSONResponse
from router import blog_router
import traceback
from datetime import datetime

app = FastAPI()

@app.middleware("http")
async def add_process_time_header(request: Request, call_next):
    try:
        response = await call_next(request)
        return response
    except Exception:
        file_name = datetime.strftime(datetime.now(), "%m-%d-%Y_%H:%M:%S")
        with open(f"./error_logs/error_{file_name}.log", "w") as f:
            f.write(traceback.format_exc())
        return JSONResponse(status_code=500, content="Something went wrong")

app.include_router(
    blog_router,
    prefix='/v1' # Check https://www.youtube.com/watch?v=ySo4-G6Ycfw&t=3s
)
