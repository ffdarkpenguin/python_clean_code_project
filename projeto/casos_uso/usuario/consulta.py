from fastapi import HTTPException

from projeto.erros import NotFoundError
from projeto.contratos.usuario import Usuario
from .base import UsuarioBase


class ConsultaUsuario(UsuarioBase):
    def executa(self, _id: int) -> Usuario:
        try:
            return self._db.pega_um(_id=_id)
        except NotFoundError:
            # o que fazer? não retornar nada ou gerar um erro? R: retorna 204 (no content)
            raise HTTPException(422, f'Usuario não encontrado id: {_id}')
