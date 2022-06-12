from projeto3.contratos.caso_uso import CasoUso
from projeto3.entidades.usuario.parametros import UsuarioParametros
from projeto3.entidades.usuario.retorno import Usuario
from projeto3.entidades.usuario.base import UsuarioBase


class InsereUsuario(UsuarioBase, CasoUso[UsuarioParametros, Usuario]):
    def executa(self, params: UsuarioParametros) -> Usuario:
        return self._db.insere(params)
