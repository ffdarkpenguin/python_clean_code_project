

from projeto.erros import NotFoundError
from .base import UsuarioBase
from ..contrato_usuario import ConsultaUsuarioContrato, UsuarioDBContrato


class ConsultaUsuario(ConsultaUsuarioContrato, UsuarioBase):
    def __init__(self, db: UsuarioDBContrato) -> None:
        self._db = db

    def executa(self, _id: int):
        try:
            return self._db.consulta(_id=_id)
        except NotFoundError:
            # o que fazer? não retornar nada ou gerar um erro? R: retorna 204 (no content)
            pass
