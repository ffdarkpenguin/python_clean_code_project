from typing import TypeVar

from pydantic import BaseModel


Modelo = TypeVar('Modelo', bound=BaseModel)
InsertParametros = TypeVar('InsertParametros', bound=BaseModel)
UpdateParametros = TypeVar('UpdateParametros', bound=BaseModel)
Filtro = TypeVar('Filtro')
Retorno = TypeVar('Retorno', bound=BaseModel)


class MyBaseModel(BaseModel):
    class Config:
        use_enum_values = True
