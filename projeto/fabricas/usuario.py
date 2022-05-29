from projeto.usuario.caso_uso.cria_usuario import CriaUsuario
from projeto.usuario.caso_uso.consulta_usuario import ConsultaUsuario
from projeto.usuario.db_usuario import UsuarioDB

db = UsuarioDB()

def cria_usuario_factory():
    return CriaUsuario(db=db)

def consulta_usuario_factory():
    return ConsultaUsuario(db=db)
