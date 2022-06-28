from fastapi import HTTPException

from projeto.erros import NotFoundError
from projeto.contratos.caso_uso import CasoUso
from projeto.entidades.usuario.contratos import Usuario
from projeto.entidades.usuario.base import UsuarioBase


class ConsultaUsuario(UsuarioBase, CasoUso[int, Usuario]):
    def executa(self, _id: int) -> Usuario:
        try:
            return self._db.pega_um(_id=_id)
        except NotFoundError:
            # o que fazer? não retornar nada ou gerar um erro? R: retorna 204 (no content)
            raise HTTPException(422, f'Usuario não encontrado id: {_id}')
