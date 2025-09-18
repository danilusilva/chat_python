from fastapi import APIRouter
from ..manager import ConnectionManager
# from ..database import get_history
from ..database import salvar_mensagem

router = APIRouter()

manager = ConnectionManager()

@router.get("/")
async def root():
    return {"message": "Bem vindo à API Chat com WebSocket e Histórico no MongoDB! Conecte-se em /ws/{sala_id}?nickname=SeuNome para iniciar o chat."}

@router.get("/salas")
async def list_rooms():
    return {sala_id: list(nickname.values()) for sala_id, nickname in manager.salas.items()}

@router.get("/history/{room_id}")
async def history(room_id: str):
    return [{"message": "aqui vai o histórico de mensagens da sala"}]

@router.get("/teste")
async def teste():
    salvar_mensagem(1, "brayan","oi oi oi")

    return {"message": "Aqui temos o histórico"}