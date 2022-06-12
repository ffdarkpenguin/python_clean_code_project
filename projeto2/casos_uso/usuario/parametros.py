from typing import Optional, List

from pydantic import BaseModel
from .modelos import UsuarioModelo


ListaUsuario = List[UsuarioModelo]


class CriaUsuarioParams(BaseModel):
    nome: str
    fone: str


class FiltroUsuario(BaseModel):
    nome: Optional[str] = None
    fone: Optional[str] = None
