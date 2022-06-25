from projeto.entidades.usuario.casos_uso.insere import InsereUsuario
from projeto.entidades.usuario.casos_uso.consulta import ConsultaUsuario
from projeto.entidades.usuario.casos_uso.lista import ListaUsuario
from projeto.entidades.usuario.casos_uso.altera import AlteraUsuario
from projeto.entidades.usuario.casos_uso.remove import RemoveUsuario
from projeto.entidades.usuario.db import UsuarioDB

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
