from projeto.contratos.usuario import FiltroUsuarios, Usuario, UsuarioParametros, UsuarioUpdateParametros

from .db_sql import DBSQL


class UsuarioDB(DBSQL[UsuarioParametros, UsuarioUpdateParametros, FiltroUsuarios, Usuario]):
    def __init__(self) -> None:
        super().__init__(modelo=Usuario)
        self._tabela = 'usuario'

    @property
    def tabela(self) -> str:
        return self._tabela
