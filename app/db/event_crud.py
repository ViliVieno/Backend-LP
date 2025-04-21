from .models import PlayerEvent
from .database import get_session
from sqlmodel import select
from typing import List
from datetime import datetime, timezone

def create_event(event: PlayerEvent) -> PlayerEvent:
    with get_session() as session:
        session.add(event)
        session.commit()
        session.refresh(event)
        return event

def create_level_started_event(player_id: int, level_name: str) -> PlayerEvent:
    event = PlayerEvent(
        player_id = player_id,
        event_type = "level_started",
        detail = level_name,
        timestamp = datetime.now(timezone.utc),
    )
    
    with get_session() as session:
        session.add(event)
        session.commit()
        session.refresh(event)
        return event
    
def get_all_events() -> List[PlayerEvent]:
    with get_session() as session:
        return session.exec(select(PlayerEvent)).all()

def get_events_by_player(player_name: str) -> List[PlayerEvent]:
    with get_session() as session:
        return session.exec(
            select(PlayerEvent).where(PlayerEvent.player_name == player_name)
        ).all()

def get_events_by_type(event_type: str) -> List[PlayerEvent]:
    with get_session() as session:
        return session.exec(
            select(PlayerEvent).where(PlayerEvent.event_type == event_type)
        ).all()
