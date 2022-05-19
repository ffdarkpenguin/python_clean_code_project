from ..contrato_usuario import CriaUsuarioParams, CriaUsuarioContrato, UsuarioDBContrato, UsuarioModelo
from .base_usuario import UsuarioBase

class CriaUsuario(CriaUsuarioContrato, UsuarioBase):
    def __init__(self, db: UsuarioDBContrato) -> None:
        self.db = db
        
    def executa(self, params: CriaUsuarioParams, ) -> UsuarioModelo:
        return self.db.cria(params)
