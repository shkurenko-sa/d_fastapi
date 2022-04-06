from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from app.database.base import database
from app.config import CORS_ALLOWED_ORIGINS
from app.handlers.users import router as user_router


app = FastAPI()
app.include_router(user_router, prefix='/users', tags=['users'])

app.add_middleware(
    CORSMiddleware,
    allow_origins=CORS_ALLOWED_ORIGINS,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


@app.on_event("startup")
async def startup():
    await database.connect()


@app.on_event("shutdown")
async def shutdown():
    await database.disconnect()
