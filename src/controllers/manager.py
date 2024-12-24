from src.controllers.line_provider import LineProviderController
from src.controllers.bet_maker import BetMakerController


class ServiceManager(object):
    line_provider: LineProviderController
    bet_maker: BetMakerController

    def __init__(self):
        self.line_provider = LineProviderController()
        self.bet_maker = BetMakerController()


async def get_service_manager() -> ServiceManager:
    return ServiceManager()
