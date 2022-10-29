from fastapi import APIRouter, Depends

from projeto.fabricas import usuario
from projeto.contratos.usuario import UsuarioParametros, FiltroUsuarios, UsuarioUpdateParametros
from projeto.erros import UseCaseError

roteador = APIRouter(
    prefix='/usuarios',
    tags=['usuarios'],
    dependencies=[],
    responses={}
)


@roteador.post('')
def cria(params: UsuarioParametros):
    caso_uso = usuario.cria_usuario_fabrica()
    return caso_uso.executa(params)


@roteador.get('')
def lista(filtro: FiltroUsuarios = Depends()):
    caso_uso = usuario.lista_usuario_fabrica()
    return caso_uso.executa(filtro)


@roteador.get('/{_id}')
def consulta(_id: int):
    caso_uso = usuario.consulta_usuario_fabrica()
    return caso_uso.executa(_id)


@roteador.put('/{_id}')
def altera(_id: int, alteracoes: UsuarioParametros):
    parametros = UsuarioUpdateParametros(id=_id, **alteracoes.dict())
    caso_uso = usuario.altera_usuario_fabrica()
    try:
        return caso_uso.executa(params=parametros)
    except UseCaseError as e:
        return str(e)


@roteador.delete('/{_id}')
def remove(_id: int):
    caso_uso = usuario.remove_usuario_fabrica()
    try:
        return caso_uso.executa(_id)
    except UseCaseError as e:
        return str(e)
