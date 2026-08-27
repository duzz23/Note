from uuid import uuid4
from typing import Self
from models.entity import Entity
from mixins.serializable import Serializable



class Category(Entity, Serializable):

    serializable_fields = (
        "id",
        "name",
        "description",
    )

    @classmethod
    def create(cls, name: str, description: str) -> Self:
        return cls(
            id = uuid4(),
            name = name,
            description = description
        )




