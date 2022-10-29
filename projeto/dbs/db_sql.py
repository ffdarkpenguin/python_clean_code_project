from abc import abstractmethod
from typing import Callable, Generic, List

from psycopg2 import connect
from psycopg2.extras import RealDictCursor

from projeto.contratos.base import Filtro, Modelo, InsertParametros, UpdateParametros
from projeto.contratos.db import DB
from projeto.erros import NotFoundError


class DBSQL(DB, Generic[InsertParametros, UpdateParametros, Filtro, Modelo]):
    def __init__(self, modelo: Callable) -> None:
        self.modelo = modelo
        dsn = 'postgres://projeto:123123@postgres:5432'
        self.conexao_db = connect(dsn=dsn, cursor_factory=RealDictCursor)
        self.conexao_db.set_session(autocommit=True)
        self.cursor = self.conexao_db.cursor()
        self.dados = {}

    @property
    @abstractmethod
    def tabela(self) -> str:
        raise NotImplementedError()

    def insere(self, params: InsertParametros) -> Modelo:
        self.dados = params.dict()
        query = self._monta_insert()
        self.cursor.execute(query, self.dados)
        return self._pega_um('insert', '')

    def insere_varios(self, params: List[InsertParametros]) -> List[Modelo]:
        raise NotImplementedError()

    def pega_um(self, _id: int) -> Modelo:
        query = f'SELECT * FROM {self.tabela} WHERE id = %(id)s'
        params = {'id': _id}
        self.cursor.execute(query, params)
        return self._pega_um('_id', _id)

    def pega_varios(self, filtro: Filtro) -> List[Modelo]:
        params = filtro.__dict__
        where_str = self._monta_where(params)
        if where_str:
            query = f'SELECT * FROM {self.tabela} WHERE {where_str}'
        else:
            query = f'SELECT * FROM {self.tabela}'
        self.cursor.execute(query, params)
        return self._pega_varios('filtro', filtro)

    def altera_um(self, alteracoes: UpdateParametros) -> Modelo:
        self.dados = alteracoes.dict()
        query = self._monta_update()
        self.cursor.execute(query, self.dados)
        return self._pega_um('_id', self.dados['_id'])

    def altera_varios(self, filtro: Filtro, alteracoes: UpdateParametros) -> List[Modelo]:
        return []

    def remove_um(self, _id: int) -> Modelo:
        query = f'DELETE FROM {self.tabela} WHERE id = %(id)s RETURNING *'
        params = {'id': _id}
        self.cursor.execute(query, params)
        return self._pega_um('id', _id)

    def remove_varios(self, filtro: Filtro) -> List[Modelo]:
        raise NotImplementedError()

    def _pega_um(self, campo, valor) -> Modelo:
        ret = self.cursor.fetchone()
        if ret is None:
            raise NotFoundError(self.tabela, campo, valor)

        return self.modelo(**dict(ret))

    def _pega_varios(self, campo, valor) -> List[Modelo]:
        lista = self.cursor.fetchall()
        if not lista:
            raise NotFoundError(self.tabela, campo, valor)
        ret: List[Modelo] = []
        for item in lista:
            ret.append(self.modelo(**dict(item)))

        return ret

    def _monta_insert(self) -> str:
        campos = []
        valores = []
        for key in self.dados:
            campos.append(key)
            valores.append(f'%({key})s')

        campos = ', '.join(campos)
        valores = ', '.join(valores)

        query = f'INSERT INTO {self.tabela} ({campos}) VALUES ({valores}) RETURNING *'
        return query

    def _monta_update(self) -> str:
        campos = self._monta_campos_update()
        query = f'''
            UPDATE {self.tabela}
            SET {campos},
            alterado_em = CURRENT_TIMESTAMP
            WHERE id = %(id)s
            RETURNING *
        '''
        return query

    def _monta_where(self, filtro: dict) -> str:
        lista = [f'{x} = %({x})s' for x in filtro if filtro[x]]
        return '\nAND '.join(lista)

    def _monta_campos_update(self) -> str:
        lista = [f'{x} = %({x})s' for x in self.dados if x not in ['_id', 'criado_em']]
        return ',\n'.join(lista)
