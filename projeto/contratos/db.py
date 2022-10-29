from abc import ABC, abstractmethod
from typing import Generic, List

from projeto.contratos.base import InsertParametros, UpdateParametros, Filtro, Modelo


class DB(ABC, Generic[InsertParametros, UpdateParametros, Filtro, Modelo]):
    '''Raises:
        NotFound: se usuário não foi encontrado
    '''
    @abstractmethod
    def insere(self, params: InsertParametros) -> Modelo:
        raise NotImplementedError()

    @abstractmethod
    def insere_varios(self, params: List[InsertParametros]) -> List[Modelo]:
        raise NotImplementedError()

    @abstractmethod
    def pega_um(self, _id: int) -> Modelo:
        raise NotImplementedError()

    @abstractmethod
    def pega_varios(self, filtro: Filtro) -> List[Modelo]:
        raise NotImplementedError()

    @abstractmethod
    def altera_um(self, alteracoes: UpdateParametros) -> Modelo:
        raise NotImplementedError()

    @abstractmethod
    def altera_varios(self, filtro: Filtro, alteracoes: UpdateParametros) -> List[Modelo]:
        raise NotImplementedError()

    @abstractmethod
    def remove_um(self, _id: int) -> Modelo:
        raise NotImplementedError()

    @abstractmethod
    def remove_varios(self, filtro: Filtro) -> List[Modelo]:
        raise NotImplementedError()
