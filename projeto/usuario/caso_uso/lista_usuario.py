

from projeto.erros import NotFound
from .base_usuario import UsuarioBase
from .. import contrato_usuario


class ListaUsuario(contrato_usuario.ConsultaUsuarioContrato, UsuarioBase):
    def __init__(self, db: contrato_usuario.UsuarioDBContrato) -> None:
        self._db = db

    def executa(self, filtro: contrato_usuario.FiltroUsuario) -> contrato_usuario.ListaUsuario:
        try:
            return self._db.lista(filtro=filtro)
        except NotFound:
            # o que fazer? não retornar nada ou gerar um erro? R: retorna 204 (no content)
            raise Exception()
