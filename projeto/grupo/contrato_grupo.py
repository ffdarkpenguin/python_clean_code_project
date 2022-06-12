from abc import ABC, abstractmethod
from datetime import datetime
from typing import Optional, List

from pydantic import BaseModel


class GrupoModelo(BaseModel):
    id: int
    nome: str
    fone: str
    criado_em: datetime
    alterado_em: Optional[datetime]


ListaGrupo = List[GrupoModelo]


class CriaGrupoParams(BaseModel):
    nome: str
    fone: str


class FiltroGrupo(BaseModel):
    nome: Optional[str] = None
    fone: Optional[str] = None


class GrupoDBContrato(ABC):
    """Raises:
        NotFound: se usuário não foi encontrado
    """
    @abstractmethod
    def cria(self, params: CriaGrupoParams) -> GrupoModelo:
        raise NotImplementedError()

    @abstractmethod
    def consulta(self, _id: int) -> GrupoModelo:
        raise NotImplementedError()

    @abstractmethod
    def lista(self, filtro: FiltroGrupo) -> ListaGrupo:
        raise NotImplementedError()

    @abstractmethod
    def altera(self, _id: int, alteracoes: CriaGrupoParams) -> GrupoModelo:
        raise NotImplementedError()

    @abstractmethod
    def remove(self, _id: int) -> GrupoModelo:
        raise NotImplementedError()


class CriaGrupoContrato(ABC):
    @abstractmethod
    def executa(self, params: CriaGrupoParams):
        raise NotImplementedError()


class ConsultaGrupoContrato(ABC):
    @abstractmethod
    def executa(self, _id: int) -> GrupoModelo:
        raise NotImplementedError()


class ListaGrupoContrato(ABC):
    @abstractmethod
    def executa(self, filtro: Optional[FiltroGrupo] = None) -> ListaGrupo:
        raise NotImplementedError()


class AlteraGrupoContrato(ABC):
    @abstractmethod
    def executa(self, _id: int, alteracoes: CriaGrupoParams) -> GrupoModelo:
        raise NotImplementedError()


class RemoveGrupoContrato(ABC):
    @abstractmethod
    def executa(self, _id: int) -> GrupoModelo:
        raise NotImplementedError()
