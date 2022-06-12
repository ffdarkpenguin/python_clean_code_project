from .. import contrato_grupo
from .base_grupo import GrupoBase


class CriaGrupo(contrato_grupo.CriaGrupoContrato, GrupoBase):
    def __init__(self, db: contrato_grupo.GrupoDBContrato) -> None:
        self.db = db

    def executa(self, params: contrato_grupo.CriaGrupoParams) -> contrato_grupo.GrupoModelo:
        return self.db.cria(params)
