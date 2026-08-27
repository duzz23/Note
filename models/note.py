from typing import Self
from uuid import uuid4, UUID
from models.category import Category
from models.entity import Entity


# Создаем блокнот с заметками
class Note(Entity):
    def __init__(self, id: UUID, name: str, description: str, title: str, text:str, category: Category ):
        super().__init__(id, name, description)
        self._id = id
        self.title = title
        self.text = text
        self._category = category

    @classmethod
    def create(cls, name: str, description: str, title: str, text: str, category: Category ) -> Self:
        return cls(
            id = uuid4(),
            name = name,
            description = description,
            title = title,
            text = text,
            category = category,
        )

    @property
    def category(self) -> Category:
        return self._category

    def __str__(self) -> str:
        return f" id:{self._id}, name: {self.name}, title: {self.title}"

    def __repr__(self) -> str:
        return f"{__class__.__name__}(id={self._id}, name={self.name}, description={self.description}, title={self.title}, text={self.text}, category={self.category}"