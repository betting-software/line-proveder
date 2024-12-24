from typing import Annotated
from asyncio import gather

from fastapi import APIRouter, Depends, HTTPException

from src.schemas import events
from src.controllers.manager import ServiceManager, get_service_manager


router = APIRouter(prefix="/v1/events", tags=["Events"])


@router.get("/events")
async def get_events(
    manager: Annotated[ServiceManager, Depends(get_service_manager)]
) -> events.EventsResponse:
    return await manager.line_provider.get_events()


@router.get("/event/{id_event}")
async def get_event(
    id_event: int,
    manager: Annotated[ServiceManager, Depends(get_service_manager)]
) -> events.Event:
    event = await manager.line_provider.get_event(id_event)
    if not event:
        raise HTTPException(status_code=404, detail="Event not found")
    return event


@router.post("/add_events")
async def add_events(
    request: events.AddEventsRequest,
    manager: Annotated[ServiceManager, Depends(get_service_manager)]
) -> None:
    await manager.line_provider.add_events(request)


@router.put("/update_events")
async def update_events(
    request: events.UpdateEventRequest,
    manager: Annotated[ServiceManager, Depends(get_service_manager)]
) -> None:
    await gather(
        manager.bet_maker.update_bets(request),
        manager.line_provider.update_event(request)
    )
