import requests
import json
from kafka import KafkaProducer
from time import sleep
import logging

KAFKA_TOPIC = "crypto_prices"
KAFKA_SERVER = "localhost:9092"
COINBASE_URL = "https://api.exchange.coinbase.com/products/{}/ticker"
COINS = ["BTC-USD", "ETH-USD", "SOL-USD"]  

import logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger("CryptoPriceProducer")

producer = KafkaProducer(
    bootstrap_servers=KAFKA_SERVER,
    value_serializer=lambda v: json.dumps(v).encode('utf-8')
)

def get_crypto_prices():
    for coin in COINS:
        url = COINBASE_URL.format(coin)
        response = requests.get(url, timeout=10)

        if response.status_code == 200:
            data = response.json()

            message = {
                "currency": coin.split("-")[0],
                "price": float(data["price"]),
                "volume": float(data["volume"]),
                "time": data["time"]
            }

            logger.info(f"Enviando para Kafka: {message}")
            producer.send(KAFKA_TOPIC, message)
        else:
            logger.error(f"Erro ao obter dados de {coin}: {response.status_code}")

        sleep(1)

producer = KafkaProducer(
    bootstrap_servers=KAFKA_SERVER,
    value_serializer=lambda v: json.dumps(v).encode('utf-8')
)

if __name__ == "__main__":
    while True:
        for coin in COINS:
            get_crypto_prices()
        sleep(5)
