from datetime import datetime
from typing import Optional

from pydantic import BaseModel


class Usuario(BaseModel):
    id: int
    nome: str
    fone: str
    criado_em: datetime
    alterado_em: Optional[datetime]
