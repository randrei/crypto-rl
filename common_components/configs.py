# ./main.py
SNAPSHOT_RATE = 10.0  # 0.25 = 4x second
BASKET = [['BTC-USD', 'BCH-USD', 'ETH-USD', 'LTC-USD', 'BTC-EUR', 'ETH-EUR', 'BTC-GBP', 'ETC-USD'],  # GDAX pairs
          ['tBTCUSD', 'tBCHUSD', 'tETHUSD', 'tLTCUSD', 'tBTCEUR', 'tETHEUR', 'tBTCGBP', 'tETCUSD']]  # Bitfinex pairs
#BASKET = [['BTC-USD', 'ETH-USD', 'LTC-USD', 'BCH-USD'],
#          ['tBTCUSD', 'tETHUSD', 'tLTCUSD', 'tBCHUSD']]


# ./common_components/client.py
GDAX_ENDPOINT = 'wss://ws-feed.pro.coinbase.com'
BITFINEX_ENDPOINT = 'wss://api.bitfinex.com/ws/2'
MAX_RECONNECTION_ATTEMPTS = 300


# ./common_components/book.py
MAX_BOOK_ROWS = 250


# ./common_components/database.py
CHUNK_SIZE = 100000
RECORD_DATA = True
MONGO_ENDPOINT = 'localhost'
ARCTIC_NAME = 'crypto.tickstore'