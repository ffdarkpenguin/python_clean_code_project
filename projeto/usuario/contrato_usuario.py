from abc import ABC, abstractmethod
from datetime import datetime
from typing import Optional

from pydantic import BaseModel


class UsuarioModelo(BaseModel):
    id: int
    nome: str
    fone: str
    criado_em: datetime
    alterado_em: Optional[datetime]


class CriaUsuarioParams(BaseModel):
    nome: str
    fone: str


class UsuarioDBContrato(ABC):
    @abstractmethod
    def grava(self, params: CriaUsuarioParams):
        raise NotImplementedError()

    @abstractmethod
    def get_usuario_com_endereco(self):
        raise NotImplementedError()


class CriaUsuarioContrato(ABC):
    @abstractmethod
    def executa(self, params: CriaUsuarioParams):
        raise NotImplementedError()
    

