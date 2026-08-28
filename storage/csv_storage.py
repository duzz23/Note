from uuid import uuid4, UUID
from pathlib import Path
from csv import DictReader, DictWriter
from mixins.serializable import Serializable
from models.base import HasID
from storage.base import StorageProtocol


# model_class -> определяем тип через абстакный класс T:
# CSVStorage будет хранить данные такой то модели типа Т -> Serializable
class CSVStorage[T: Serializable | HasID](StorageProtocol):
    # type[T] Тип от экземпляра класса -> Класс
    def __init__(self, filepath: Path, model_class: type[T]):
        self.filepath = filepath
        # Тип от экземпляра класса -> Класс
        self.model_class = model_class
        # Кэш-храним данные в словаре
        self.data: dict[UUID, T] = {}

    def save(self) -> None:
        # создаем папку
        self.filepath.parent.mkdir(parents=True, exist_ok=True)
        # открываем файл
        with self.filepath.open('w') as file:
            # записываем данные
            writer = DictWriter(
                # Записываем в файл
                f=file,
                # Заголовки
                fieldnames=self.model_class.serializable_fields,
            )
            # Записываем заголовки
            writer.writeheader()
            # Записываем данные
            writer.writerows(
                item.to_dict() for item in self.data.values()
            )

    def load(self) -> None:
        if not self.filepath.exists():
            return None
        # Открываем файл
            # Читаем файл
            reader = DictReader(file)
            for row in reader:
                # Создаем экземпляр класса
                entity = self.model_class.from_dict(row)
                # Добавляем в кэш
                self.data[entity.id] = entity






