from .models import PlayerEvent
from .database import get_session
from sqlmodel import select

def create_event(event: PlayerEvent):
    session = get_session()
    session.add(event)
    session.commit()
    session.refresh(event)
    return event

def get_all_events():
    session = get_session()
    events = session.exec(select(PlayerEvent)).all()
    return events

def get_events_by_player(player_id: str):
    session = get_session()
    events = session.exec(select(PlayerEvent).where(PlayerEvent.player_id == player_id)).all()
    return events
