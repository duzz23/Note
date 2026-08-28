from typing import Self
from uuid import uuid4, UUID
from models.entity import Entity
from models.category import Category
from mixins.serializable import Serializable



# Создаем блокнот с заметками
class Note(Serializable, Entity):

    serializable_fields = (
        "id",
        "name",
        "description",
        "title",
        "text",
        "category",
    )

    def __init__(self, id: UUID, name: str, description: str, title: str, text:str, category: Category ):
        Entity.__init__(self, id, name, description)
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

    def serialize_category(self) -> str:
        return str(self.category.id)

    @classmethod
    def deserialize_category(cls, value: str) -> None:
        from storage.сategory_storage import category_storage
        return category_storage.data(UUID(value))


    def __str__(self) -> str:
        return f" id:{self._id}, name: {self.name}, title: {self.title}"

    def __repr__(self) -> str:
        return f"{__class__.__name__}(id={self._id!r}, name={self.name!r}, description={self.description!r}, title={self.title!r}, text={self.text!r}, category={self.category!r}"