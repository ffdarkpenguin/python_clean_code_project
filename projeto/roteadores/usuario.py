from fastapi import APIRouter, Depends

from projeto.fabricas import usuario
from projeto.entidades.usuario.contratos import UsuarioParametros, FiltroUsuarios

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
    caso_uso = usuario.altera_usuario_fabrica()
    return caso_uso.executa(_id=_id, alteracoes=alteracoes)


@roteador.delete('/{_id}')
def remove(_id: int):
    caso_uso = usuario.remove_usuario_fabrica()
    return caso_uso.executa(_id=_id)
