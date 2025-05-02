import uvicorn
from fastapi import FastAPI, Request
from starlette.responses import HTMLResponse
from starlette.staticfiles import StaticFiles
from starlette.templating import Jinja2Templates

from probo_app.order_book_route import router as ProboRouter
from probo_app.order_book_service import OrderBook

order_book = OrderBook()


app = FastAPI()

app.mount("/static", StaticFiles(directory="static"), name="static")
templates = Jinja2Templates(directory="templates")

""" Route for rendering templates"""


@app.get("/", response_class=HTMLResponse)
async def home(request: Request):
    return templates.TemplateResponse("index.html", {"request": request})


# includes router for apis of probo app
app.include_router(ProboRouter)


if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000)