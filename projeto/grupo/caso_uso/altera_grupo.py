

from projeto.erros import NotFoundError
from .base_grupo import GrupoBase
from .. import contrato_grupo


class AlteraGrupo(contrato_grupo.AlteraGrupoContrato, GrupoBase):
    def __init__(self, db: contrato_grupo.GrupoDBContrato) -> None:
        self._db = db

    def executa(self, _id: int, alteracoes: contrato_grupo.CriaGrupoParams) -> contrato_grupo.GrupoModelo:
        try:
            return self._db.altera(_id=_id, alteracoes=alteracoes)
        except NotFoundError:
            # o que fazer? não retornar nada ou gerar um erro? R: retorna 204 (no content)
            raise Exception()
