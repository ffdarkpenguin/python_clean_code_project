from abc import ABC, abstractmethod
from datetime import datetime
from typing import Optional, List

from pydantic import BaseModel


class UsuarioModelo(BaseModel):
    id: int
    nome: str
    fone: str
    criado_em: datetime
    alterado_em: Optional[datetime]


class ListaUsuario(BaseModel):
    List[UsuarioModelo]

class CriaUsuarioParams(BaseModel):
    nome: str
    fone: str


class UsuarioDBContrato(ABC):
    """Raises:
        NotFound: se usuário não foi encontrado
    """
    @abstractmethod
    def cria(self, params: CriaUsuarioParams):
        raise NotImplementedError()

    def consulta(self, _id: int):
        raise NotImplementedError()


class CriaUsuarioContrato(ABC):
    @abstractmethod
    def executa(self, params: CriaUsuarioParams):
        raise NotImplementedError()


class ConsultaUsuarioContrato(ABC):
    @abstractmethod
    def executa(self, id: int):
        raise NotImplementedError()
