from abc import ABC, abstractmethod
from typing import Generic, List

from projeto.contratos.base import Parametros, Filtro, Modelo


class DB(ABC, Generic[Parametros, Filtro, Modelo]):
    '''Raises:
        NotFound: se usuário não foi encontrado
    '''
    @abstractmethod
    def insere(self, params: Parametros) -> Modelo:
        raise NotImplementedError()

    @abstractmethod
    def insere_varios(self, params: Parametros) -> List[Modelo]:
        raise NotImplementedError()

    @abstractmethod
    def pega_um(self, _id: int) -> Modelo:
        raise NotImplementedError()

    @abstractmethod
    def pega_varios(self, filtro: Filtro) -> List[Modelo]:
        raise NotImplementedError()

    @abstractmethod
    def altera_um(self, _id: int, alteracoes: Parametros) -> Modelo:
        raise NotImplementedError()

    @abstractmethod
    def altera_varios(self, filtro: Filtro, alteracoes: Parametros) -> List[Modelo]:
        raise NotImplementedError()

    @abstractmethod
    def remove_um(self, _id: int) -> Modelo:
        raise NotImplementedError()

    @abstractmethod
    def remove_varios(self, filtro: Filtro) -> List[Modelo]:
        raise NotImplementedError()
