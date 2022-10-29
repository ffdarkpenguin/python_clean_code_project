from projeto.contratos.usuario import UsuarioUpdateParametros, Usuario
from projeto.erros import NotFoundError, UseCaseError

from .base import UsuarioBase


class AlteraUsuario(UsuarioBase):

    def executa(self, params: UsuarioUpdateParametros) -> Usuario:
        try:
            return self._db.altera_um(params)
        except NotFoundError as e:
            raise UseCaseError(e.msg)
