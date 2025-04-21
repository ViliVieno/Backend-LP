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
    with get_session() as session:
        player = session.exec(select(Players).where(Players.id == player_id)).first()
        if not player:
            return None
        events = session.exec(select(PlayerEvent).where(PlayerEvent.player_id == player_id)).all()
        return {
            "id": player.id,
            "name": player.name,
            "events": [event.dict() for event in events]
        }
