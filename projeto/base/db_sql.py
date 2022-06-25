from abc import abstractmethod
from typing import Generic, List

from psycopg2 import connect
from psycopg2.extras import RealDictCursor

from projeto.erros import NotFoundError
from projeto.contratos.db import DB

from projeto.contratos.base import Parametros, Filtro, Modelo


class DBSQL(DB, Generic[Parametros, Filtro, Modelo]):
    def __init__(self) -> None:
        dsn = 'postgres://projeto:123123@postgres:5432'
        self.conexao_db = connect(dsn=dsn, cursor_factory=RealDictCursor)
        self.conexao_db.set_session(autocommit=True)
        self.cursor = self.conexao_db.cursor()

    @abstractmethod
    def tabela(self) -> str:
        raise NotImplementedError()

    def insere(self, params: Parametros) -> Modelo:
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

    def insere_varios(self, params: Parametros) -> List[Modelo]:
        return []

    def pega_um(self, _id: int) -> Modelo:
        query = f'SELECT * FROM {self.tabela} WHERE id = %(id)s'
        params = {'id': _id}
        self.cursor.execute(query, params)
        return self._pega_um()

    def pega_varios(self, filtro: Filtro) -> List[Modelo]:
        params = filtro.__dict__
        where_str = self._monta_where(params)
        query = f'SELECT * FROM {self.tabela} WHERE {where_str}'
        self.cursor.execute(query, params)
        return self._pega_varios()

    def altera_um(self, _id: int, alteracoes: Parametros) -> Modelo:
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

    def altera_varios(self, filtro: Filtro, alteracoes: Parametros) -> List[Modelo]:
        return []

    def remove_um(self, _id: int) -> Modelo:
        query = f'DELETE FROM {self.tabela} WHERE id = %(id)s RETURNING *'
        params = {'id': _id}
        self.cursor.execute(query, params)
        return self._pega_um()

    def remove_varios(self, filtro: Filtro) -> List[Modelo]:
        return []

    def _pega_um(self) -> Modelo:
        ret = self.cursor.fetchone()
        if ret is None:
            raise NotFoundError('Não encontrado')
        return Modelo(**ret)  # type: ignore

    def _pega_varios(self) -> List[Modelo]:
        lista = self.cursor.fetchall()
        if not lista:
            raise NotFoundError('Não encontrado')
        ret: List[Modelo] = []
        for item in lista:
            ret.append(Modelo(**item))  # type: ignore

        return ret

    def _monta_where(self, filtro: dict) -> str:
        lista = [f'{x} = %({x})s' for x in filtro if filtro[x]]
        return ' AND '.join(lista)

    def _monta_campos_update(self, filtro: dict) -> str:
        lista = [f'{x} = %({x})s' for x in filtro if filtro[x]]
        return ', '.join(lista)
