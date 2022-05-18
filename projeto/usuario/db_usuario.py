from .contrato_usuario import UsuarioDBContrato, CriaUsuarioParams
from ...db_sql import DB_SQL

class UsuarioDB(UsuarioDBContrato, DB_SQL):
    def __init__(self) -> None:
        self.table = 'usuario'

    def grava(self, params: CriaUsuarioParams):
        """ faz qualquer extra e chama o super"""
        return super().grava(params)