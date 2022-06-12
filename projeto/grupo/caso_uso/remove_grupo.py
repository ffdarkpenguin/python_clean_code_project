

from projeto.erros import NotFoundError
from .base_grupo import GrupoBase
from .. import contrato_grupo


class RemoveGrupo(contrato_grupo.RemoveGrupoContrato, GrupoBase):
    def __init__(self, db: contrato_grupo.GrupoDBContrato) -> None:
        self._db = db

    def executa(self, _id: int) -> contrato_grupo.GrupoModelo:
        try:
            return self._db.remove(_id=_id)
        except NotFoundError:
            # o que fazer? não retornar nada ou gerar um erro? R: retorna 204 (no content)
            raise Exception()
