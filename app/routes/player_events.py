from fastapi import APIRouter
from app.db.models import PlayerEvent, PlayerEventRead
from app.db import event_crud
from typing import List, Optional

router = APIRouter(prefix="/events", tags=["events"])

@router.get("/", response_model=List[PlayerEvent])
def get_all_events():
    return event_crud.get_all_events()

@router.get("/type/{event_type}", response_model=List[PlayerEvent])
def get_events_by_type(event_type: str):
    return event_crud.get_events_by_type(event_type)
