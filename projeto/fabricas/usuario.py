from projeto.usuario.caso_uso.cria_usuario import CriaUsuario
from projeto.usuario.db_usuario import UsuarioDB

def cria_usuario_factory():
    return CriaUsuario(db = UsuarioDB())