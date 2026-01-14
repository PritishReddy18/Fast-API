from app.db.migrate import run_migrations
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

    # side way imports to load tables via Base
from app.orm_models.profile_orm_models import CreateProfile
from app.orm_models.posts_orm_model import CreatePost
from app.orm_models.post_likes import PostLikes

    # side way imports to load routers
from app.api_routers.user_routers import router as user_router
from app.api_routers.profile_routers import router as profile_router
from app.api_routers.post_routers import router as post_router

    # side way imports to load routers
from app.api_routers.user_routers import login
from app.api_routers.profile_routers import view_profile_by_token

app = FastAPI()

import os

@app.on_event("startup")
def startup():
    if os.getenv("ENV") != "test":
        run_migrations()

origins = ["*"]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(user_router)
app.include_router(profile_router)
app.include_router(post_router)

@app.get("/")
def root():
    return {
        "message" : "HELLO, Welcome to the world of API!!"
    }