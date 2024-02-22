import aiohttp
import asyncio
import platform
from datetime import datetime, timedelta
import sys


class HttpError(Exception):
    pass


currencies = ['USD', 'EUR']
async def request(url: str):
    async with aiohttp.ClientSession() as session:
        try:
            async with session.get(url) as resp:
                if resp.status == 200:
                    result = await resp.json()
                    return result
                else:
                    raise HttpError(f"Error status: {resp.status} for {url}")
        except (aiohttp.ClientConnectorError, aiohttp.InvalidURL) as err:
            raise HttpError(f'Connection error: {url}', str(err))


async def main(index_day):
    result = []
    global currencies
    
    for el in range(int(index_day)):
        d = datetime.now() - timedelta(days=el)
        shift = d.strftime("%d.%m.%Y")
        try:
            response = await request(f'https://api.privatbank.ua/p24api/exchange_rates?json&date={shift}')
            dict_date ={}
            dict_date[shift] = {}
            for el in response['exchangeRate']:
                if el['currency'] in currencies:
                    t = el['currency']
                    dict_date[shift][t] = {}
                    dict_date[shift][t]['sale'] = el['saleRate']
                    dict_date[shift][t]['purchase'] = el['purchaseRate']

            result.append(dict_date)
        except HttpError as err:
            print(err)
            return None
    return result


def valid_quantity(arg):
    quantity = arg
    while True:
        try:
            int(quantity)
            if int(quantity) < 11:
                break
            else:
                print('Quantity of days <11')
        except:
            print('Quantity of days must be integer')
        quantity = input('Enter quantity of days: ')
    return quantity   


def new_currency():
    next_cur = input('Add new currency to USD and EUR currencies, if you want: ')
    cur = next_cur.split(',')
    for el in cur:
        el1 = el.upper()
        next_cur1 = el1.strip()
        if next_cur1 in ['CHF', 'GBP', 'CZK', 'PLZ']:
            currencies.append(next_cur1)
if __name__ == '__main__':
    if platform.system() == 'Windows':
        asyncio.set_event_loop_policy(asyncio.WindowsSelectorEventLoopPolicy())
    quantity = valid_quantity(sys.argv[1])  
    #можна додавати кілька валют через кому
    new_currency()
    r = asyncio.run(main(quantity))
    print(r)