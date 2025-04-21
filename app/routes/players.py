from fastapi import APIRouter, HTTPException, status
from db import player_crud
from db.models import Players, PlayerWithEvents
from typing import List

router = APIRouter(prefix="/players", tags=["players"])

@router.post("/", response_model=Players, status_code=status.HTTP_201_CREATED)
def create_player(player: Players):
    return player_crud.create_player(player)

@router.get("/", response_model=List[Players])
def get_all_players():
    return player_crud.get_all_players()

@router.get("/{player_id}", response_model=PlayerWithEvents)
def get_player(player_id: int):
    player_data = player_crud.get_player_with_events(player_id)
    if not player_data:
        raise HTTPException(status_code=404, detail="Player not found")
    return player_data
