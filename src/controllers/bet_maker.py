import aiohttp

from src.config import bet_maker_config
from src.schemas.events import UpdateEventRequest


class BetMakerController:
    def __init__(self):
        self._bet_maker_url = bet_maker_config.bet_maker_url

    async def update_bets(self, request: UpdateEventRequest) -> None:
        url = f"{self._bet_maker_url}/v1/bets/update_bet"
        data = {"id": request.id, "status": request.status.value}
        async with aiohttp.ClientSession() as session:
            await session.put(url, json=data)
