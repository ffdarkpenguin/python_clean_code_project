

from projeto.erros import NotFoundError
from .base import UsuarioBase
from .. import contrato_usuario


class RemoveUsuario(contrato_usuario.RemoveUsuarioContrato, UsuarioBase):
    def __init__(self, db: contrato_usuario.UsuarioDBContrato) -> None:
        self._db = db

    def executa(self, _id: int) -> contrato_usuario.UsuarioModelo:
        try:
            return self._db.remove(_id=_id)
        except NotFoundError:
            # o que fazer? não retornar nada ou gerar um erro? R: retorna 204 (no content)
            raise Exception()
