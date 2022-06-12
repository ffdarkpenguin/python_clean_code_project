from projeto3.contratos.caso_uso import CasoUso
from projeto3.entidades.usuario.parametros import UsuarioParametros
from projeto3.entidades.usuario.retorno import Usuario
from projeto3.entidades.usuario.base import UsuarioBase
from projeto3.erros import NotFoundError


class AlteraUsuario(UsuarioBase, CasoUso[UsuarioParametros, Usuario]):

    def executa(self, _id: int, alteracoes: UsuarioParametros) -> Usuario:
        try:
            return self._db.altera_um(_id=_id, alteracoes=alteracoes)
        except NotFoundError:
            # o que fazer? não retornar nada ou gerar um erro? R: retorna 204 (no content)
            raise Exception()
