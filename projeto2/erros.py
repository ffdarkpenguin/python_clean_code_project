class NotFoundError(Exception):
    def __init__(self, _id) -> None:
        self.msg = f"Registro não encontrado: {_id}"
        super().__init__(self.msg)
