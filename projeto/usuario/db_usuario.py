from psycopg2 import connect
from psycopg2.extras import RealDictCursor

from . import contrato_usuario


class UsuarioDB(contrato_usuario.UsuarioDBContrato):
    def __init__(self) -> None:
        dsn = 'postgres://projeto:123123@postgres:5432'
        self.conexao_db = connect(dsn=dsn, cursor_factory=RealDictCursor)
        self.conexao_db.set_session(autocommit=True)
        self.cursor = self.conexao_db.cursor()
        self.tabela = 'usuario'
        self.nome = 'Usuário'
        self.artigo = 'o'

    def cria(self, params: contrato_usuario.CriaUsuarioParams) -> contrato_usuario.UsuarioModelo:
        ''' faz qualquer extra e chama o super'''
        dados = params.__dict__
        campos = []
        valores = []
        for key in dados:
            campos.append(key)
            valores.append(f'%({key})s')

        campos = ', '.join(campos)
        valores = ', '.join(valores)

        query = f'INSERT INTO {self.tabela} ({campos}) VALUES ({valores}) RETURNING *'
        self.cursor.execute(query, dados)
        return self._pega_um()

    def consulta(self, _id: int) -> contrato_usuario.UsuarioModelo:
        query = f'SELECT * FROM {self.tabela} WHERE id = %(id)s'
        params = {'id': _id}
        self.cursor.execute(query, params)
        return self._pega_um()

    def lista(self, filtro: contrato_usuario.FiltroUsuario) -> contrato_usuario.ListaUsuario:
        params = filtro.__dict__
        where_str = self._monta_where(params)
        query = f'SELECT * FROM {self.tabela} WHERE {where_str}'
        self.cursor.execute(query, params)
        return self._pega_varios()

    def altera(self, _id: int, alteracoes: contrato_usuario.CriaUsuarioParams) -> contrato_usuario.UsuarioModelo:
        params = alteracoes.__dict__
        campos = self._monta_campos_update(params)
        query = f'''
            UPDATE {self.tabela}
            SET {campos}
            WHERE id = %(id)s
            RETURNING *
        '''
        params['id'] = _id
        self.cursor.execute(query, params)
        return self._pega_um()

    def remove(self, _id: int) -> contrato_usuario.UsuarioModelo:
        query = f'DELETE FROM {self.tabela} WHERE id = %(id)s RETURNING *'
        params = {'id': _id}
        self.cursor.execute(query, params)
        return self._pega_um()

    def _pega_um(self) -> contrato_usuario.UsuarioModelo:
        ret = self.cursor.fetchone()
        if ret is None:
            raise Exception('Não encontrado')
        return contrato_usuario.UsuarioModelo(**ret)  # type: ignore

    def _pega_varios(self) -> contrato_usuario.ListaUsuario:
        lista = self.cursor.fetchall()
        if not lista:
            raise Exception('Não encontrado')
        ret: contrato_usuario.ListaUsuario = []
        for item in lista:
            ret.append(contrato_usuario.UsuarioModelo(**item))  # type: ignore

        return ret

    def _monta_where(self, filtro: dict) -> str:
        lista = [f'{x} = %({x})s' for x in filtro if filtro[x]]
        return ' AND '.join(lista)

    def _monta_campos_update(self, filtro: dict) -> str:
        lista = [f'{x} = %({x})s' for x in filtro if filtro[x]]
        return ', '.join(lista)
