from uuid import UUID

from models.base import Base

class Entity(Base):
    def __init__(
            self,
            id: UUID,
            name: str,
            description: str
    ):
        super().__init__(id=id)
        self.name = name
        self.description = description

    def __str__(self) -> str:
        return f"{self.__class__.__name__} {self.id} {self.name} {self.description}"

    def __repr__(self) -> str:
        return  str(self)


