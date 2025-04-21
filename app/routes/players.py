from fastapi import APIRouter, HTTPException, status
from db import player_crud, event_crud
from db.models import Players, PlayerWithEvents, PlayerEventRead, EventCreate
from typing import List, Optional

router = APIRouter(prefix="/players", tags=["players"])

@router.post("/", response_model=Players, status_code=status.HTTP_201_CREATED)
def create_player(player: Players):
    return player_crud.create_player(player)

@router.get("/", response_model=List[Players])
def get_all_players():
    return player_crud.get_all_players()

@router.get("/{id}", response_model=PlayerWithEvents)
def get_player(player_id: int):
    player_data = player_crud.get_player_with_events(player_id)
    if not player_data:
        raise HTTPException(status_code=404, detail="Player not found")
    return player_data

@router.get("/{id}/events", response_model=List[PlayerEventRead])
def get_player_events(id: int, event_type: Optional[str] = None):
    player = player_crud.get_player_by_id(id)
    if not player:
        raise HTTPException(status_code=404, detail="Player not found")
    events = player_crud.get_events_by_player(id, event_type=event_type)
    return events

@router.post("/{id}/events", response_model=PlayerEventRead, status_code=status.HTTP_201_CREATED)
def create_event_for_player(id: int, event: EventCreate):
    player = player_crud.get_player_by_id(id)
    if not player:
        raise HTTPException(status_code=404, detail="Player not found")
    
    allowed_event_types = {"level_started", "level_completed"}
    if event.type not in allowed_event_types:
        raise HTTPException(status_code=400, detail="Unknown event type")
    
    new_event = event_crud.create_event(player_id = id, event_data = event)
    return new_event
