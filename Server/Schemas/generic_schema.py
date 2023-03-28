from pydantic.generics import GenericModel
from pydantic import BaseModel
from typing import Generic, List, TypeVar
X = TypeVar("X", bound=BaseModel)

class GenericResponse(GenericModel, Generic[X]):
    data: List[X]
    metadata: dict = {}