from projeto.contratos.usuario import Usuario
from projeto.erros import NotFoundError, UseCaseError

from .base import UsuarioBase


class RemoveUsuario(UsuarioBase):
    def executa(self, _id: int) -> Usuario:
        try:
            return self._db.remove_um(_id=_id)
        except NotFoundError as e:
            # o que fazer? não retornar nada ou gerar um erro? R: retorna 204 (no content)
            raise UseCaseError(e.msg)
