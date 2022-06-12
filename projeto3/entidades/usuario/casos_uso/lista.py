from typing import List

from projeto3.contratos.caso_uso import CasoUso
from projeto3.entidades.usuario.base import UsuarioBase
from projeto3.entidades.usuario.retorno import Usuario
from projeto3.entidades.usuario.parametros import ListaFiltro


class ListaUsuario(UsuarioBase, CasoUso[ListaFiltro, Usuario]):

    def executa(self, filtro: ListaFiltro) -> List[Usuario]:
        return self._db.pega_varios(filtro=filtro)
