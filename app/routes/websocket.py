from fastapi import APIRouter, WebSocket, WebSocketDisconnect
from ..manager import manager

router = APIRouter()

@router.websocket("/ws/{sala_id}")
async def websocket_endpoint(websocket: WebSocket, sala_id: str, nickname: str):
    await manager.connect(sala_id, websocket, nickname)

    try:
        while True:
            data = await websocket.receive_text()
            await manager.broadcast(sala_id, data)
    except WebSocketDisconnect:
        await manager.disconnect(sala_id, websocket)
    