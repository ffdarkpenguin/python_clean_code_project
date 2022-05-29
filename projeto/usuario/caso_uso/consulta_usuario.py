from .base_usuario import UsuarioBase
from ..contrato_usuario import ConsultaUsuarioContrato, UsuarioDBContrato


class ConsultaUsuario(ConsultaUsuarioContrato, UsuarioBase):
    def __init__(self, db: UsuarioDBContrato) -> None:
        self._db = db

    def executa(self, _id: int):
        return self._db.consulta(_id = _id)
