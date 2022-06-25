from projeto.contratos.caso_uso import CasoUso
from projeto.entidades.usuario.parametros import UsuarioParametros
from projeto.entidades.usuario.retorno import Usuario
from projeto.entidades.usuario.base import UsuarioBase
from projeto.erros import NotFoundError


class AlteraUsuario(UsuarioBase, CasoUso[UsuarioParametros, Usuario]):

    def executa(self, _id: int, alteracoes: UsuarioParametros) -> Usuario:
        try:
            return self._db.altera_um(_id=_id, alteracoes=alteracoes)
        except NotFoundError:
            # o que fazer? não retornar nada ou gerar um erro? R: retorna 204 (no content)
            raise Exception()
