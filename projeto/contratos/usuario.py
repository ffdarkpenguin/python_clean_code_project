from datetime import datetime
from typing import Optional

from .base import MyBaseModel


class UsuarioParametros(MyBaseModel):
    nome: str
    fone: str


class UsuarioUpdateParametros(UsuarioParametros):
    id: int


class FiltroUsuarios(MyBaseModel):
    nome: Optional[str] = None
    fone: Optional[str] = None


class Usuario(UsuarioUpdateParametros):
    criado_em: datetime
    alterado_em: Optional[datetime] = None
