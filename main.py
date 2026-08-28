from uuid import uuid4

from models.note import Note
from settings import CATEGORIES_STORAGE_PATH, PRODUCTS_STORAGE_PATH
from models.category import Category
from storage.csv_storage import CSVStorage
from storage.note_storage import note_storage
from storage.сategory_storage import category_storage


def demo_create_and_read():
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


def example_category_storege():
    category = category_storage.create(
        name="лопата",
        description="New description",
    )
    # print(category)
    # for c in category_storage.all():
    #     print(c)

    test_category_storage = category_storage.get_by_name("лопата")
    print(test_category_storage)

def main():
    category = category_storage.create(
        name="Дом",
        description="Работа по дому",
    )

    new_note = note_storage.create(
        name = "вторая заметка",
        description = "новая заментка",
        title = "работа работа",
        text = "Завоевать весь мир",
        category = category
    )
    print(new_note)
    print(note_storage.data)

    for n in note_storage.all():
        print(n)

if __name__ == '__main__':
    main()