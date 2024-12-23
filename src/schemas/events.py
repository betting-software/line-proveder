from enum import Enum

from pydantic import BaseModel


class Status(Enum):
    PENDING = "pending"
    TEAM_1_WINS = "team_1_wins"
    TEAM_2_WINS = "team_2_wins"


class BaseEvent(BaseModel):
    id: int
    name: str
    coefficient: float
    timestamp: int


class PendingEvent(BaseEvent):
    pass


class Event(BaseEvent):
    status: Status


class AddEventsRequest(BaseModel):
    events: list[Event] | Event


class UpdateEventRequest(BaseModel):
    id: int
    status: Status


class EventsResponse(BaseModel):
    events: list[PendingEvent]
