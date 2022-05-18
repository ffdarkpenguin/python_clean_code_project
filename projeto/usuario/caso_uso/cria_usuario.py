from ..contrato_usuario import CriaUsuarioParams, CriaUsuarioContrato, UsuarioDBContrato, UsuarioModelo
from .base_usuario import UsuarioBase

class UsuarioBase(CriaUsuarioContrato, UsuarioBase):
    def executa(self, params: CriaUsuarioParams, db: UsuarioDBContrato) -> UsuarioModelo:
        return db.grava(params)


