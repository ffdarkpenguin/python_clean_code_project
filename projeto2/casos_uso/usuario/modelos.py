from datetime import datetime
from typing import Optional

from pydantic import BaseModel


class UsuarioModelo(BaseModel):
    id: int
    nome: str
    fone: str
    criado_em: datetime
    alterado_em: Optional[datetime]
