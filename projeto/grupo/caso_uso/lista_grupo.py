# from fastapi import Response

# from projeto.erros import NotFoundError
from .base_grupo import GrupoBase
from .. import contrato_grupo


class ListaGrupo(contrato_grupo.ConsultaGrupoContrato, GrupoBase):
    def __init__(self, db: contrato_grupo.GrupoDBContrato) -> None:
        self._db = db

    def executa(self, filtro: contrato_grupo.FiltroGrupo) -> contrato_grupo.ListaGrupo:
        return self._db.lista(filtro=filtro)
