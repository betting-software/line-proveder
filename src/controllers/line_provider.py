from src.db.dao import EventsDAO
from src.schemas.events import \
    Event, Status, AddEventsRequest, UpdateEventRequest, EventsResponse


class LineProviderController:
    def __init__(self):
        self._dao = EventsDAO

    async def get_events(self) -> EventsResponse:
        records = await self._dao.select_filter(status=Status.PENDING)
        data = [
            Event(
                id=record.id, name=record.name, coefficient=record.coefficient,
                timestamp=record.timestamp, status=record.status
            ) for record in records
        ]
        return EventsResponse(events=data)

    async def get_event(self, id_event: int) -> Event:
        record = await self._dao.select_one_filter(id=id_event)
        if record:
            return Event(
                id=record.id, name=record.name, coefficient=record.coefficient,
                timestamp=record.timestamp, status=record.status
            )
        return None

    async def add_events(self, request: AddEventsRequest) -> None:
        if isinstance(request.events, list):
            events = [item.model_dump() for item in request.events]
            await self._dao.add_many(*events)
        else:
            await self._dao.add_one(**request.events.model_dump())

    async def update_event(self, request: UpdateEventRequest) -> None:
        await self._dao.update_filter(
            update_values=request.model_dump(), id=request.id
        )
