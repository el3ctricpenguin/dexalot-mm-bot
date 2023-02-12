import ccxt

# OKXの通貨ペアのlast priceを返す

def getLastPrice(pair_name='AVAX/USDT',exchange_name='okx'):
    exchange = eval('ccxt.'+exchange_name+'()')
    ticker = exchange.fetch_ticker(pair_name)
    return ticker['last']

if __name__ == '__main__':
    print(str(getLastPrice()))

# tickerの中身
# {'symbol': 'BTC/USDT', 'timestamp': 1676189640013, 'datetime': '2023-02-12T08:14:00.013Z', 'high': 21898.5, 'low': 21620.4, 'bid': 21807.9, 'bidVolume': 0.26913087, 'ask': 21808.0, 'askVolume': 2.20688187, 'vwap': 21752.562420739458, 'open': 21698.2, 'close': 21807.9, 'last': 21807.9, 'previousClose': None, 'change': 109.7, 'percentage': 0.5055718907559152, 'average': 21753.05, 'baseVolume': 2178.87669954, 'quoteVolume': 47396151.41383862, 'info': {'instType': 'SPOT', 'instId': 'BTC-USDT', 'last': '21807.9', 'lastSz': '0.00318', 'askPx': '21808', 'askSz': '2.20688187', 'bidPx': '21807.9', 'bidSz': '0.26913087', 'open24h': '21698.2', 'high24h': '21898.5', 'low24h': '21620.4', 'volCcy24h': '47396151.41383862', 'vol24h': '2178.87669954', 'ts': '1676189640013', 'sodUtc0': '21856.2', 'sodUtc8': '21733.9'}}