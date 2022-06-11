from projeto.usuario.caso_uso.cria_usuario import CriaUsuario
from projeto.usuario.caso_uso.consulta_usuario import ConsultaUsuario
from projeto.usuario.caso_uso.lista_usuario import ListaUsuario
from projeto.usuario.caso_uso.altera_usuario import AlteraUsuario
from projeto.usuario.caso_uso.remove_usuario import RemoveUsuario
from projeto.usuario.db_usuario import UsuarioDB

db = UsuarioDB()


def cria_usuario_fabrica():
    return CriaUsuario(db=db)


def consulta_usuario_fabrica():
    return ConsultaUsuario(db=db)


def lista_usuario_fabrica():
    return ListaUsuario(db=db)


def altera_usuario_fabrica():
    return AlteraUsuario(db=db)


def remove_usuario_fabrica():
    return RemoveUsuario(db=db)
