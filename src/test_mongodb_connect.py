import os
from pymongo import MongoClient
from dotenv import load_dotenv
from pathlib import Path

env_path = Path(__file__).resolve().parent.parent / '.env'
load_dotenv(dotenv_path=env_path)

uri = os.getenv("MONGO_URI")
# print(f"URI carregada: {repr(uri)}")

try:
    client = MongoClient(
    uri,
    tls=True,
    tlsAllowInvalidCertificates=True,
    serverSelectionTimeoutMS=30000  # opcional, timeout maior pra debug
    )
    print("Conectado ao MongoDB Atlas!")
    print("Databases disponíveis:", client.list_database_names())
except Exception as e:
    print("Erro na conexão:")
    print(e)
