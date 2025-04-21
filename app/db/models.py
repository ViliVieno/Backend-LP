from sqlmodel import SQLModel, Field
from datetime import datetime
from typing import List

class PlayerEvent(SQLModel, table=True):
    id: int | None = Field(default=None, primary_key=True)
    event_type: str
    detail: str
    timestamp: datetime
    player_id: int

class Players(SQLModel, table=True):
    id: int | None = Field(default=None, primary_key=True)
    name: str
    
class PlayerEventRead(SQLModel):
    id: int
    event_type: str
    detail: str
    timestamp: datetime
    player_id: int

class PlayerWithEvents(SQLModel):
    id: int
    name: str
    events: List[PlayerEventRead]

class LevelCompletedRequest(SQLModel):
    player_id: int
    level_name: str

class PlayerEventCreate(SQLModel):
    type: str
    detail: str

class EventCreate(SQLModel):
    type: str
    detail: str