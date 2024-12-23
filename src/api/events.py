from typing import Annotated
from asyncio import gather

from fastapi import APIRouter, Depends

from src.schemas import events
from src.controllers.manager import ServiceManager, get_service_manager


router = APIRouter(prefix="/v1/events", tags=["Events"])


@router.post("/get_events")
async def get_events(
    manager: Annotated[ServiceManager, Depends(get_service_manager)]
) -> events.EventsResponse:
    return await manager.events.get_events()


@router.post("/add_events")
async def add_events(
    request: events.AddEventsRequest,
    manager: Annotated[ServiceManager, Depends(get_service_manager)]
) -> None:
    await manager.events.add_events(request)


@router.put("/update_events")
async def update_events(
    request: events.UpdateEventRequest,
    manager: Annotated[ServiceManager, Depends(get_service_manager)]
) -> None:
    await gather(
        manager.bet_maker.update_bets(request), 
        manager.events.update_event(request)
    )
