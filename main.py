from fastapi import FastAPI, HTMLResponse
import nest_asyncio
import uvicorn

portifolio = FastAPI(title = "I am who I am")
@portifolio.get('/')
def home():
    pass