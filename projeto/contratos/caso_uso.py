from abc import ABC, abstractmethod
from typing import Generic

from projeto.contratos.base import Parametros, Retorno
from projeto.contratos.db import DB


class CasoUso(ABC, Generic[Parametros, Retorno]):
    @abstractmethod
    def __init__(self, db: DB) -> None:
        raise NotImplementedError()

    @abstractmethod
    def executa(self, params: Parametros) -> Retorno:
        raise NotImplementedError()
