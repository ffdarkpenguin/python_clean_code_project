import logging

from projeto.fabricas.usuario import cria_usuario_factory
from projeto.usuario.contrato_usuario import CriaUsuarioParams

# cria_usuario = cria_usuario_factory()

# ret = cria_usuario.executa(CriaUsuarioParams(nome="ff", fone="123123"))


class B():
    def faz_b(self):
        raise ValueError("Não fez B")
class A():
    def __init__(self) -> None:
        self.b = B()
    def faz_b(self):
        try:
            self.b.faz_b()
        except Exception:
            raise TypeError("Erro de tipo")


def a():
    obj = A()
    try:
        obj.faz_b()
    except Exception as e:
        trata_excessao(e)


def trata_excessao(e):
    nome = e.__class__.__name__
    if "Portal"  in nome:
        logging.error(f"Tratei excessão {nome}")
    else:
        logging.exception('Erro imprevisto...')
