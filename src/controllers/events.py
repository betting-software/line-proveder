from asyncio import gather

import aiohttp

from src.db.dao import EventsDAO
from src.schemas.events import \
    PendingEvent, Status, AddEventsRequest, UpdateEventRequest
from src.config import bet_maker_config


class EventsController:
    def __init__(self):
        self._dao = EventsDAO
        self._bet_maker_url = bet_maker_config.bet_maker_url

    async def get_events(self) -> list[PendingEvent]:
        records = await self._dao.select_filter(status=Status.PENDING)
        return [PendingEvent(**record.__dict__) for record in records]

    async def add_events(self, request: AddEventsRequest) -> None:
        if isinstance(request.events, list):
            events = [item.model_dump() for item in request.events]
            await self._dao.add_many(*events)
        else:
            await self._dao.add_one(**request.events.model_dump())

    async def update_event(self, request: UpdateEventRequest) -> None:
        await gather(
            aiohttp.request(
                'POST', self._bet_maker_url, json=request.model_dump()
            ),
            self._dao.update_filter(
                update_values=request.model_dump(), id=request.id
            )
        )
