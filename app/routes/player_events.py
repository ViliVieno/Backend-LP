from fastapi import APIRouter
from db.models import PlayerEvent
from db import event_crud
from typing import List

router = APIRouter(prefix="/events", tags=["events"])

@router.post("/level_started", response_model=PlayerEvent)
def start_level(player_id: int, player_name: str, level_name: str):
    event = event_crud.create_level_started_event(player_id, player_name, level_name)
    return event

@router.get("/", response_model=List[PlayerEvent])
def get_all_events():
    return event_crud.get_all_events()

@router.get("/player/{player_name}", response_model=List[PlayerEvent])
def get_events_by_player(player_name: str):
    return event_crud.get_events_by_player(player_name)

@router.get("/type/{event_type}", response_model=List[PlayerEvent])
def get_events_by_type(event_type: str):
    return event_crud.get_events_by_type(event_type)
