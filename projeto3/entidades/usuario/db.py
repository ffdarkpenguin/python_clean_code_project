from projeto3.base.db_sql import DBSQL
from projeto3.entidades.usuario.parametros import UsuarioParametros, ListaFiltro
from projeto3.entidades.usuario.retorno import Usuario


class UsuarioDB(DBSQL[UsuarioParametros, ListaFiltro, Usuario]):
    def __init__(self) -> None:
        super().__init__()
        self._tabela = 'usuario'

    def tabela(self) -> str:
        return self._tabela
