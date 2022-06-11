from .. import contrato_usuario
from .base_usuario import UsuarioBase


class CriaUsuario(contrato_usuario.CriaUsuarioContrato, UsuarioBase):
    def __init__(self, db: contrato_usuario.UsuarioDBContrato) -> None:
        self.db = db

    def executa(self, params: contrato_usuario.CriaUsuarioParams) -> contrato_usuario.UsuarioModelo:
        return self.db.cria(params)
