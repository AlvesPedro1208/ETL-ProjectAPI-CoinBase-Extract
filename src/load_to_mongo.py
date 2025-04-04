import os
import json
from pymongo import MongoClient
from kafka import KafkaConsumer
from dotenv import load_dotenv
from pathlib import Path
import certifi

# Carrega as variáveis de ambiente
env_path = Path(__file__).resolve().parent.parent / '.env'
load_dotenv(dotenv_path=env_path)

uri = os.getenv("MONGO_URI")
# print(f"URI carregada: {repr(uri)}")

# Variáveis de ambiente
KAFKA_TOPIC = os.getenv("KAFKA_TOPIC")
KAFKA_SERVER = os.getenv("KAFKA_SERVER")
MONGO_URI = os.getenv("MONGO_URI")

# Conecta ao MongoDB
mongo_client = MongoClient(MONGO_URI, tlsCAFile=certifi.where())
mongo_db = mongo_client["crypto_stream"]
mongo_collection = mongo_db["temp_prices"]

# Conecta ao Kafka
consumer = KafkaConsumer(
    KAFKA_TOPIC,
    bootstrap_servers=[KAFKA_SERVER],
    value_deserializer=lambda m: json.loads(m.decode("utf-8")),
    auto_offset_reset='latest',
    enable_auto_commit=True,
    group_id='mongo_loader_group'
)

print("Conectado ao Kafka. Aguardando mensagens...")

# Consome mensagens do Kafka e insere no MongoDB
for message in consumer:
    data = message.value
    print(f"Mensagem recebida: {data}")
    
    mongo_collection.insert_one(data)
    print("Documento inserido no MongoDB Atlas.")
