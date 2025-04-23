from .models import PlayerEvent, PlayerEventCreate
from .database import get_session
from sqlmodel import select
from typing import List, Optional
from datetime import datetime, timezone

def create_event(event: PlayerEvent) -> PlayerEvent:
    with get_session() as session:
        session.add(event)
        session.commit()
        session.refresh(event)
        return event

# Below, Optional is used to say "Event type is optional and if it is used, then make it a string" and the List[] says "Return [x] in a list"
def get_all_events(event_type: Optional[str] = None) -> List[PlayerEvent]: 
    with get_session() as session:
        query = select(PlayerEvent)
        if event_type:
            query = query.where(PlayerEvent.event_type == event_type)
        return session.exec(query).all()
    
# Below, event_type is a must and it will return [x] in a list
def get_events_by_type(event_type: str) -> List[PlayerEvent]:
    with get_session() as session:
        return session.exec(
            select(PlayerEvent).where(PlayerEvent.event_type == event_type)
        ).all()
    
def create_event(player_id: int, event_data: PlayerEventCreate) -> PlayerEvent:
    event = PlayerEvent(
        player_id = player_id,
        event_type = event_data.type,
        detail = event_data.detail,
        timestamp = datetime.now(timezone.utc),
    )
    with get_session() as session:
        session.add(event)
        session.commit()
        session.refresh(event)
        return event
