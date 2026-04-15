from fastapi import APIRouter, HTTPException
from models.session import Session, SessionCreate
from utils.session_manager import SessionManager

router = APIRouter()
session_manager = SessionManager()

@router.post("", response_model=Session)
def create_session(session: SessionCreate):
    """创建新会话"""
    new_session = session_manager.create_session(session.name)
    return new_session

@router.get("", response_model=list[Session])
def get_sessions():
    """获取所有会话"""
    return session_manager.get_all_sessions()

@router.get("/{session_id}", response_model=Session)
def get_session(session_id: str):
    """获取指定会话"""
    session = session_manager.get_session(session_id)
    if not session:
        raise HTTPException(status_code=404, detail="Session not found")
    return session

@router.delete("/{session_id}")
def delete_session(session_id: str):
    """删除会话"""
    success = session_manager.delete_session(session_id)
    if not success:
        raise HTTPException(status_code=404, detail="Session not found")
    return {"message": "Session deleted successfully"}