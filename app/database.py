# app/database.py

from pymongo import MongoClient
from .config import MONGOURL, MONGODB
# Removida a linha 'import datetime' duplicada
from datetime import datetime # Esta importação é a correta para o seu código

client = MongoClient(MONGOURL)
db = client[MONGODB]
mensagens = db["mensagens"]
usuarios = db["usuarios"]

def salvar_mensagem(sala_id: str, nickname: str, mensagem: str):
    mensagens.insert_one(
        {   
            "sala_id": sala_id,
            "nickname": nickname,
            "mensagem": mensagem,
            "timestamp": datetime.utcnow()
        }
    )
    return True