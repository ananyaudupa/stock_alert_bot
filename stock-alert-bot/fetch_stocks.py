import requests

def get_market_data():

    url = "https://www.nseindia.com/api/market-data-pre-open?key=ALL"

    headers = {
        "User-Agent": "Mozilla/5.0",
        "Accept-Language": "en-US,en;q=0.9",
        "Accept": "application/json"
    }

    session = requests.Session()

    # NSE requires visiting homepage first
    session.get("https://www.nseindia.com", headers=headers)

    response = session.get(url, headers=headers)

    json_data = response.json()

    stocks = []

    for item in json_data["data"]:
        info = item["metadata"]

        stocks.append({
            "symbol": info["symbol"],
            "percentChange": info["pChange"]
        })

    # sort stocks
    sorted_stocks = sorted(stocks, key=lambda x: x["percentChange"], reverse=True)

    gainers = sorted_stocks[:2]
    losers = sorted_stocks[-2:]

    return gainers, losers