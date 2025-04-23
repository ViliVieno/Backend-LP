from .models import Players, PlayerEvent
from .database import get_session
from sqlmodel import select
from typing import List, Optional

def create_player(player: Players) -> Players:
    with get_session() as session:
        session.add(player)
        session.commit()
        session.refresh(player)
        return player

def get_all_players() -> List[Players]:
    with get_session() as session:
        return session.exec(select(Players)).all()

def get_player_with_events(player_id: int) -> Optional[dict]:
    with get_session() as session: # Opens database
        player = session.exec(select(Players).where(Players.id == player_id)).first() # Uses SQL query Select on players and then matches id and returns .first
        if not player:
            return None # If no player, returns None
        events = session.exec(select(PlayerEvent).where(PlayerEvent.player_id == player_id)).all() # Uses SQL query Select to find from the table PlayerEvent where player_id in this is the same as there
        return {
            "id": player.id,
            "name": player.name,
            "events": [event.model_dump() for event in events] # More ChatGPT, but this helps us convert PlayerEvent object to a dictionary
        }
    
def get_events_by_player(player_id: int, event_type: Optional[str] = None):
    with get_session() as session:
        query = select(PlayerEvent).where(PlayerEvent.player_id == player_id)
        if event_type:
            query = query.where(PlayerEvent.event_type == event_type)
        return session.exec(query).all()

def get_player_by_id(player_id: int) -> Players | None:
    with get_session() as session:
        return session.exec(select(Players).where(Players.id == player_id)).first()