from uuid import uuid4
from settings import CATEGORIES_STORAGE_PATH
from models.category import Category
from storage.csv_storage import CSVStorage


def main():
    category = Category.create(
        name='Test category',
        description='Test description'
    )
    print(category)
    print()
    print(category.to_dict())
    print()

    data = {
        "id": uuid4(),
        "name": "New name",
        "description": "New description",
    }

    print("New category: from data", data)
    new_category = Category.from_dict(data)
    print(new_category)

    print()
    print("Save and Load")

    # путь от текущего файла
    category_storage = CSVStorage(
        filepath=CATEGORIES_STORAGE_PATH,
        model_class=Category,

    )
    category_storage.data[category.id] = category
    category_storage.data[new_category.id] = new_category

    # category_storage.save()
    category_storage.load()
    print(category_storage.data)


if __name__ == '__main__':
    main()