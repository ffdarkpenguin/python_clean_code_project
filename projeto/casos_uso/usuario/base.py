from projeto.dbs.db_usuario import UsuarioDB


class UsuarioBase():
    def __init__(self, db: UsuarioDB) -> None:
        self._db = db
