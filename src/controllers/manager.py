from src.controllers.events import EventsController


class ServiceManager(object):
    events: EventsController

    def __init__(self):
        self.events = EventsController()


async def get_service_manager() -> ServiceManager:
    return ServiceManager()
