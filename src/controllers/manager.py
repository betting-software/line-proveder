from src.controllers.events import EventsController
from src.controllers.bet_maker import BetMakerController


class ServiceManager(object):
    events: EventsController
    bet_maker: BetMakerController

    def __init__(self):
        self.events = EventsController()
        self.bet_maker = BetMakerController()


async def get_service_manager() -> ServiceManager:
    return ServiceManager()
