from pathlib import Path
from models.category import Category
from models.note import Note
from settings import PRODUCTS_STORAGE_PATH
from storage.csv_storage import CSVStorage


# класс-хранилище для управления коллекцией заметок c возможностью фильтрации по категориям
class NoteStorage(CSVStorage):

    def __init__(self, filepath: Path, model_class=Note):
        super().__init__(filepath, model_class)

    # метод создания заметки
    def create(self, name: str, description: str, title: str, text: str, category: Category) -> Note:
        note = Note.create(
            name=name,
            description = description,
            title = title,
            text = text,
            category = category,
        )
        self.data[note.id] = note
        self.save()
        return note

    def all(self) -> list[Category]:
        return list(self.data.values())

    # метод фильтрации заметок по категории
    def get_by_category(self, category: Category) -> list[Note]:
        return [n for n in self.all() if n.category.id == category.id]


note_storage = NoteStorage(
    filepath = PRODUCTS_STORAGE_PATH
)
# загрузка данных из файла
note_storage.load()