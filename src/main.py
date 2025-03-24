from extract import get_crypto_prices
from transform import transform_crypto_prices
import threading

if __name__ == '__main__':
    print("Iniciando a extração contínua de preços de criptomoedas")
    t1 = threading.Thread(target=get_crypto_prices)
    t1.start()