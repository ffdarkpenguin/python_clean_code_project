from typing import List

from projeto.contratos.caso_uso import CasoUso
from projeto.entidades.usuario.base import UsuarioBase
from projeto.entidades.usuario.contratos import Usuario, FiltroUsuarios


class ListaUsuario(UsuarioBase, CasoUso[FiltroUsuarios, Usuario]):

    def executa(self, params: FiltroUsuarios) -> List[Usuario]:
        return self._db.pega_varios(filtro=params)
