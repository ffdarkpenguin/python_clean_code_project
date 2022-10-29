from projeto.casos_uso.usuario.insere import InsereUsuario
from projeto.casos_uso.usuario.consulta import ConsultaUsuario
from projeto.casos_uso.usuario.lista import ListaUsuario
from projeto.casos_uso.usuario.altera import AlteraUsuario
from projeto.casos_uso.usuario.remove import RemoveUsuario
from projeto.dbs.db_usuario import UsuarioDB

db = UsuarioDB()


def cria_usuario_fabrica():
    return InsereUsuario(db=db)


def consulta_usuario_fabrica():
    return ConsultaUsuario(db=db)


def lista_usuario_fabrica():
    return ListaUsuario(db=db)


def altera_usuario_fabrica():
    return AlteraUsuario(db=db)


def remove_usuario_fabrica():
    return RemoveUsuario(db=db)
