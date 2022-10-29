from projeto.contratos.usuario import UsuarioParametros, Usuario
from .base import UsuarioBase


class InsereUsuario(UsuarioBase):
    def executa(self, params: UsuarioParametros) -> Usuario:
        return self._db.insere(params)
