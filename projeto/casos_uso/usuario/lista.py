from typing import List

from projeto.contratos.usuario import FiltroUsuarios, Usuario

from .base import UsuarioBase


class ListaUsuario(UsuarioBase):

    def executa(self, params: FiltroUsuarios) -> List[Usuario]:
        return self._db.pega_varios(filtro=params)
