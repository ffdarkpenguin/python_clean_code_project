from typing import Optional

from pydantic import BaseModel


class UsuarioParametros(BaseModel):
    nome: str
    fone: str


class ListaFiltro(BaseModel):
    nome: Optional[str] = None
    fone: Optional[str] = None
