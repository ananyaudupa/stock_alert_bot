from fetch_stocks import get_market_data
from bot import send_message
from datetime import datetime


def job():

    gainers, losers = get_market_data()

    now = datetime.now().strftime("%H:%M")

    message = f"📊 Pre-Open Market Update ({now})\n\n"

    message += "🟢 Top 2 Gainers\n\n"

    for g in gainers:
        gap = g["price"] - g["prev_close"]

        message += (
            f"{g['symbol']}\n"
            f"Price: ₹{g['price']}\n"
            f"Prev Close: ₹{g['prev_close']}\n"
            f"Change: +{g['percentChange']}%\n"
            f"Gap: ₹{round(gap,2)}\n\n"
        )

    message += "🔴 Top 2 Losers\n\n"

    for l in losers:
        gap = l["price"] - l["prev_close"]

        message += (
            f"{l['symbol']}\n"
            f"Price: ₹{l['price']}\n"
            f"Prev Close: ₹{l['prev_close']}\n"
            f"Change: {l['percentChange']}%\n"
            f"Gap: ₹{round(gap,2)}\n\n"
        )

    send_message(message)


if __name__ == "__main__":
    job()