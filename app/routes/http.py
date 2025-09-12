from fastapi import APIRouter
# from ..manager import ConnectionManager
# from ..database import get_history

router = APIRouter()
@router.get("/")
async def root():
    return {"message": "Bem vindo à API Chat com WebSocket e Histórico no MongoDB! Conecte-se em /ws/{sala_id}?nickname=SeuNome para iniciar o chat."}

@router.get("/salas")
async def list_rooms():
    return {"message": "Funcionalidade de listar salas em desenvolvimento."}

@router.get("/history/{room_id}")
async def history(room_id: str):
    return [{"message": "aqui vai o histórico de mensagens da sala"}]
    