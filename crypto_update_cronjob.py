from typing import List

from application import db
from application.models import *
import httpx, asyncio, os

coin_api = os.getenv("COIN_API")


async def fetch_crypto_prices(crypto_symbols):
    headers = {
        'X-CMC_PRO_API_KEY': coin_api,
        'Accepts': 'application/json'
    }
    async with httpx.AsyncClient() as client:
        response = await client.get(
            f'https://pro-api.coinmarketcap.com/v1/cryptocurrency/quotes/latest',
            params={'symbol': ','.join(crypto_symbols), 'convert': 'USD', 'skip_invalid': True},
            headers=headers
        )
        response.raise_for_status()
        return response.json()


def fill_crypto_prices():
    print("Filling crypto prices...")
    coins: List[Coins] = Coins.query.all()
    crypto_symbols = {x.symbol.strip() for x in coins}
    prices_data = asyncio.run(fetch_crypto_prices(crypto_symbols))

    price_lookup = {
        symbol: data.get('quote', {}).get('USD', {}).get('price', 0)
        for symbol, data in prices_data.get('data', {}).items()
    }
    for coin in coins:
        coin.rate = price_lookup.get(coin.symbol, 1)

    db.session.commit()
    print("Finished filling crypto prices")
    return True


fill_crypto_prices()
