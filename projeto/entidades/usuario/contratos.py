from datetime import datetime
from typing import Optional

from pydantic import BaseModel


class UsuarioParametros(BaseModel):
    nome: str
    fone: str


class FiltroUsuarios(BaseModel):
    nome: Optional[str] = None
    fone: Optional[str] = None


class Usuario(BaseModel):
    id: int
    nome: str
    fone: str
    criado_em: datetime
    alterado_em: Optional[datetime]
