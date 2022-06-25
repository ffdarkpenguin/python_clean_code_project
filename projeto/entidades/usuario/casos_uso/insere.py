from projeto.contratos.caso_uso import CasoUso
from projeto.entidades.usuario.parametros import UsuarioParametros
from projeto.entidades.usuario.retorno import Usuario
from projeto.entidades.usuario.base import UsuarioBase


class InsereUsuario(UsuarioBase, CasoUso[UsuarioParametros, Usuario]):
    def executa(self, params: UsuarioParametros) -> Usuario:
        return self._db.insere(params)
