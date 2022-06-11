from fastapi import APIRouter, Depends

from projeto.fabricas import usuario
from projeto.usuario import contrato_usuario

roteador = APIRouter(
    prefix='/usuarios',
    tags=['usuarios'],
    dependencies=[],
    responses={}
)


@roteador.post('')
def cria(params: contrato_usuario.CriaUsuarioParams):
    caso_uso = usuario.cria_usuario_fabrica()
    return caso_uso.executa(params)


@roteador.get('')
def lista(filtro: contrato_usuario.FiltroUsuario = Depends()):
    caso_uso = usuario.lista_usuario_fabrica()
    print(filtro)
    return caso_uso.executa(filtro=filtro)


@roteador.get('/{_id}')
def consulta(_id: int):
    caso_uso = usuario.consulta_usuario_fabrica()
    return caso_uso.executa(_id)


@roteador.put('/{_id}')
def altera(_id: int, alteracoes: contrato_usuario.CriaUsuarioParams):
    caso_uso = usuario.altera_usuario_fabrica()
    return caso_uso.executa(_id=_id, alteracoes=alteracoes)


@roteador.delete('/{_id}')
def remove(_id: int):
    caso_uso = usuario.remove_usuario_fabrica()
    return caso_uso.executa(_id=_id)
