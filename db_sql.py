from psycopg2 import connect
from psycopg2.extras import RealDictCursor

class DB_SQL():
    def __init__(self) -> None:
        dsn = "postgres://clean_code:123123@localhost:49153"
        self.conexao_db = connect(dns=dsn, cursor_factory=RealDictCursor)
        self.conexao_db.set_session(autocommit=True)

    def create(self, params):  # params é um classe especial que suporta todas as classes de dados do sistema
        dados = params.__dict__
        
        self._params = params
        query = self._prepara_query()
        return self.db.execute(query, params)

    def get_one(self):
        

    def get_many(self):
        pass
    
    def update_one(self):
        pass

    def update_many(self):
        pass

    def delete_one(self):
        pass

    def delete_many(self):
        pass

    def execute_query(self, query, params):
        pass

    def _prepara_insert(self) -> str:
        print(f'usando {self._params} para montar query')
        return "query com params"
