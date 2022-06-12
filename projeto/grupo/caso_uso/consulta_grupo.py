

from projeto.erros import NotFoundError
from .base_grupo import GrupoBase
from ..contrato_grupo import ConsultaGrupoContrato, GrupoDBContrato


class ConsultaGrupo(ConsultaGrupoContrato, GrupoBase):
    def __init__(self, db: GrupoDBContrato) -> None:
        self._db = db

    def executa(self, _id: int):
        try:
            return self._db.consulta(_id=_id)
        except NotFoundError:
            # o que fazer? não retornar nada ou gerar um erro? R: retorna 204 (no content)
            pass
