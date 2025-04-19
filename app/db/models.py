from sqlmodel import SQLModel, Field
from datetime import datetime
from typing import Optional

class PlayerEvent(SQLModel, table=True):
    id: Optional[int] = Field(default=None, primary_key=True)
    player_id: str
    level_id: str
    event_type: str
    timestamp: datetime
