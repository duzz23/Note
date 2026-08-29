from uuid import uuid4

from models.note import Note
from settings import CATEGORIES_STORAGE_PATH, PRODUCTS_STORAGE_PATH
from models.category import Category
from storage.csv_storage import CSVStorage
from storage.note_storage import note_storage
from storage.сategory_storage import category_storage


def create_category():
    category_storage.create(
        name="Дом",
        description="Все что связано с делами по домом"
    )

    category_storage.create(
        name="Работа",
        description="Все что связано с делами по работе"
    )

    category_storage.create(
        name="Семья",
        description="Все что связано с делами с семьей"
    )

def create_note():
    # вытаскиваем котегории
    home_category = category_storage.get_by_name("Дом")
    work_category = category_storage.get_by_name("Работа")
    family_category = category_storage.get_by_name("Семья")

    note_storage.create(
        name="Крыльцо",
        description="Расчитать стоимость крыльца",
        title = "первый этап расчеты",
        text = "Померить стоимость размеры, расчитать стоимость материалов",
        category = home_category,
    )

    note_storage.create(
        name="Python",
        description="AI Agents",
        title = "task",
        text = "Сделать задачу по доработке агентов",
        category = work_category,
    )

    note_storage.create(
        name="Сын",
        description="Курсы",
        title = "Хотел пойти на карате",
        text = "Посмотреть на районе школы по карате",
        category = family_category,
    )


def main():
    if not category_storage.data:
        create_category()
        print("Категории созданы")

    if not note_storage.data:
        create_note()
        print("Заметки созданы")


    all_category = category_storage.all()
    for category in all_category:
        print("Дом", category.name)
        notes = note_storage.get_by_category(category)
        for note in notes:
            print("-", note)

        print()


if __name__ == '__main__':
    main()