class UseCaseError(Exception):
    def __init__(self, msg) -> None:
        self.msg = msg
        super().__init__(self.msg)


class NotFoundError(Exception):
    def __init__(self, tabela, campo, valor) -> None:
        self.msg = f'Registro não encontrado. Tabela: {tabela} => {campo}: {valor}'
        super().__init__(self.msg)
