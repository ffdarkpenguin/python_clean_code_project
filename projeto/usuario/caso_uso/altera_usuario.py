

from projeto.erros import NotFound
from .base_usuario import UsuarioBase
from .. import contrato_usuario


class AlteraUsuario(contrato_usuario.AlteraUsuarioContrato, UsuarioBase):
    def __init__(self, db: contrato_usuario.UsuarioDBContrato) -> None:
        self._db = db

    def executa(self, _id: int, alteracoes: contrato_usuario.CriaUsuarioParams) -> contrato_usuario.UsuarioModelo:
        try:
            return self._db.altera(_id=_id, alteracoes=alteracoes)
        except NotFound:
            # o que fazer? não retornar nada ou gerar um erro? R: retorna 204 (no content)
            raise Exception()
