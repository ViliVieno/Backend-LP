from fastapi import FastAPI
from .routes import player_events, players
from contextlib import asynccontextmanager
from .db.database import create_db_and_tables

# Define lifespan event handlers
@asynccontextmanager
async def lifespan(app: FastAPI):
    print("Starting")
    create_db_and_tables()
    yield
    print("Finishing")

app = FastAPI(lifespan=lifespan)

app.include_router(player_events.router)
app.include_router(players.router)