from fastapi import APIRouter
from db.models import PlayerEvent
from db import event_crud

router = APIRouter(prefix="/events", tags=["events"])

@router.post("/", response_model=PlayerEvent)
def create_event(event: PlayerEvent):
    return event_crud.create_event(event)

@router.get("/", response_model=list[PlayerEvent])
def get_all():
    return event_crud.get_all_events()

@router.get("/player/{player_id}", response_model=list[PlayerEvent])
def get_for_player(player_id: str):
    return event_crud.get_events_by_player(player_id)
