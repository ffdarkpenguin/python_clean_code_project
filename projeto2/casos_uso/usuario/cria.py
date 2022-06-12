from .contratos import UsuarioDBContrato, UsuarioModelo, CriaUsuarioParams, CriaUsuarioContrato
from .base import UsuarioBase


class CriaUsuario(CriaUsuarioContrato, UsuarioBase):
    def __init__(self, db: UsuarioDBContrato) -> None:
        self.db = db

    def executa(self, params: CriaUsuarioParams) -> UsuarioModelo:
        return self.db.cria(params)
