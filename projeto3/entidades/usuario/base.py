from projeto3.entidades.usuario.db import UsuarioDB


class UsuarioBase():
    def __init__(self, db: UsuarioDB) -> None:
        self._db = db
