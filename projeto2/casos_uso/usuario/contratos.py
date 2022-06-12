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


ListaUsuario = List[UsuarioModelo]


class CriaUsuarioParams(BaseModel):
    nome: str
    fone: str


class FiltroUsuario(BaseModel):
    nome: Optional[str] = None
    fone: Optional[str] = None


class UsuarioDBContrato(ABC):
    '''Raises:
        NotFound: se usuário não foi encontrado
    '''
    @abstractmethod
    def cria(self, params: CriaUsuarioParams) -> UsuarioModelo:
        raise NotImplementedError()

    @abstractmethod
    def consulta(self, _id: int) -> UsuarioModelo:
        raise NotImplementedError()

    @abstractmethod
    def lista(self, filtro: FiltroUsuario) -> ListaUsuario:
        raise NotImplementedError()

    @abstractmethod
    def altera(self, _id: int, alteracoes: CriaUsuarioParams) -> UsuarioModelo:
        raise NotImplementedError()

    @abstractmethod
    def remove(self, _id: int) -> UsuarioModelo:
        raise NotImplementedError()


class CriaUsuarioContrato(ABC):
    @abstractmethod
    def executa(self, params: CriaUsuarioParams):
        raise NotImplementedError()


class ConsultaUsuarioContrato(ABC):
    @abstractmethod
    def executa(self, _id: int) -> UsuarioModelo:
        raise NotImplementedError()


class ListaUsuarioContrato(ABC):
    @abstractmethod
    def executa(self, filtro: Optional[FiltroUsuario] = None) -> ListaUsuario:
        raise NotImplementedError()


class AlteraUsuarioContrato(ABC):
    @abstractmethod
    def executa(self, _id: int, alteracoes: CriaUsuarioParams) -> UsuarioModelo:
        raise NotImplementedError()


class RemoveUsuarioContrato(ABC):
    @abstractmethod
    def executa(self, _id: int) -> UsuarioModelo:
        raise NotImplementedError()
