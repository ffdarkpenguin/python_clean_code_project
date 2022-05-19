from projeto.fabricas.usuario import cria_usuario_factory
from projeto.usuario.contrato_usuario import CriaUsuarioParams

cria_usuario = cria_usuario_factory()

ret = cria_usuario.executa(CriaUsuarioParams(nome="ff", fone="123123"))