# from fastapi import Response

# from projeto.erros import NotFoundError
from .base import UsuarioBase
from .. import contrato_usuario


class ListaUsuario(contrato_usuario.ConsultaUsuarioContrato, UsuarioBase):
    def __init__(self, db: contrato_usuario.UsuarioDBContrato) -> None:
        self._db = db

    def executa(self, filtro: contrato_usuario.FiltroUsuario) -> contrato_usuario.ListaUsuario:
        return self._db.lista(filtro=filtro)
