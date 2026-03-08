import schedule
import time
from fetch_stocks import get_market_data
from bot import send_message


def job():

    gainers, losers = get_market_data()

    message = "Market Open Update\n\n"

    message += "Top 2 Gainers:\n"
    for g in gainers:
        message += f"{g['symbol']} +{g['percentChange']}%\n"

    message += "\nTop 2 Losers:\n"
    for l in losers:
        message += f"{l['symbol']} {l['percentChange']}%\n"

    send_message(message)



schedule.every().day.at("09:20").do(job)
while True:
    schedule.run_pending()
    time.sleep(1)