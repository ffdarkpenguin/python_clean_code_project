from psycopg2 import connect
from psycopg2.extras import RealDictCursor

from .contrato_usuario import UsuarioDBContrato, CriaUsuarioParams, UsuarioModelo

class UsuarioDB(UsuarioDBContrato):
    def __init__(self) -> None:
        dsn = "postgres://clean_code:123123@localhost:49153"
        self.conexao_db = connect(dsn=dsn, cursor_factory=RealDictCursor)
        self.conexao_db.set_session(autocommit=True)
        self.cursor = self.conexao_db.cursor()
        self.tabela = 'usuario'

    def cria(self, params: CriaUsuarioParams) -> UsuarioModelo:
        """ faz qualquer extra e chama o super"""
        dados = params.__dict__
        campos = []
        valores = []
        for key in dados:
            campos.append(key)
            valores.append(f"%({key})s")

        campos = ", ".join(campos)
        valores = ", ".join(valores)

        query = f"INSERT INTO {self.tabela} ({campos}) VALUES ({valores}) RETURNING *"
        self.cursor.execute(query, dados)
        return self._pega_resultado()

    def consulta(self, _id: int) -> UsuarioModelo:
        query = f"SELECT * FROM {self.tabela} WHERE id = %(id)s"
        params = {"id": _id}
        self.cursor.execute(query, params)
        return self._pega_resultado()


    def _pega_resultado(self) -> UsuarioModelo:
        ret = self.cursor.fetchone()
        if ret is None:
            raise Exception("Não encontrado")
        return UsuarioModelo(**ret) # type: ignore
