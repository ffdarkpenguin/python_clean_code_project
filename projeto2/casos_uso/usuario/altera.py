

from projeto.erros import NotFoundError
from .base import UsuarioBase
from .contratos import CriaUsuarioParams, UsuarioModelo, UsuarioDBContrato, AlteraUsuarioContrato


class AlteraUsuario(AlteraUsuarioContrato, UsuarioBase):
    def __init__(self, db: UsuarioDBContrato) -> None:
        self._db = db

    def executa(self, _id: int, alteracoes: CriaUsuarioParams) -> UsuarioModelo:
        try:
            return self._db.altera(_id=_id, alteracoes=alteracoes)
        except NotFoundError:
            # o que fazer? não retornar nada ou gerar um erro? R: retorna 204 (no content)
            raise Exception()
