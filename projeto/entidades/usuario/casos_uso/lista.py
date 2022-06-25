from typing import List

from projeto.contratos.caso_uso import CasoUso
from projeto.entidades.usuario.base import UsuarioBase
from projeto.entidades.usuario.retorno import Usuario
from projeto.entidades.usuario.parametros import ListaFiltro


class ListaUsuario(UsuarioBase, CasoUso[ListaFiltro, Usuario]):

    def executa(self, filtro: ListaFiltro) -> List[Usuario]:
        return self._db.pega_varios(filtro=filtro)
