from projeto.base.db_sql import DBSQL
from projeto.entidades.usuario.contratos import UsuarioParametros, FiltroUsuarios, Usuario


class UsuarioDB(DBSQL[UsuarioParametros, FiltroUsuarios, Usuario]):
    def __init__(self) -> None:
        super().__init__()
        self._tabela = 'usuario'

    def tabela(self) -> str:
        return self._tabela
