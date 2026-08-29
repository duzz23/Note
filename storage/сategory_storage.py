from pathlib import Path
from models.category import Category
from settings import CATEGORIES_STORAGE_PATH
from storage.csv_storage import CSVStorage


class CategoryStorage[T: Category](CSVStorage[T]):
    "Хранение типов товара"
    def __init__(self, filepath: Path, model_class: type[T] = Category):
        super().__init__(filepath, model_class)

    # Создать категорию
    def create(self, name: str, description: str) -> Category:
        category = Category.create(name, description)
        self.data[category.id] = category
        self.save()
        return category

    # Поиск по имени
    def get_by_name(self, name: str) -> Category | None:
        for category in self.all():
            if category.name == name:
                return category
        return None

category_storage = CategoryStorage(
    filepath=CATEGORIES_STORAGE_PATH

)

category_storage.load()